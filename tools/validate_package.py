#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
except Exception as exc:  # pragma: no cover
    print(json.dumps({"verdict": "fail", "findings": [{"code": "DEPENDENCY_MISSING", "message": f"jsonschema is required: {exc}", "path": None}]}, indent=2))
    raise SystemExit(2)

REQUIRED_ROOT_FILES = {
    "PACKAGE.json", "README.md", "MANIFEST.md", "GLOSSARY.md",
    "PDD.md", "CHANGE-LOG.md", "manifest.json"
}
REQUIRED_DIRS = {"adr", "schema", "skills", "profiles", "metrics", "problems", "docs", "examples", "tools", "out"}
ABSOLUTE_PATH_PATTERNS = [
    re.compile("/mnt" + "/data/"),
    re.compile(r"[A-Za-z]:\\\\Users\\\\"),
]
SCHEMA_DRAFT = "https://json-schema.org/draft/2020-12/schema"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel_files(root: Path) -> list[str]:
    return sorted(
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    )


def rel_dirs(root: Path) -> list[str]:
    return sorted(
        p.relative_to(root).as_posix() + "/"
        for p in root.rglob("*")
        if p.is_dir() and "__pycache__" not in p.parts
    )


def validate_package(root_arg: str | Path = ".") -> dict[str, Any]:
    root = Path(root_arg).resolve()
    findings: list[dict[str, Any]] = []

    def add(code: str, message: str, path: str | Path | None = None, severity: str = "error") -> None:
        if isinstance(path, Path):
            try:
                path = path.relative_to(root).as_posix()
            except Exception:
                path = str(path)
        findings.append({"code": code, "severity": severity, "message": message, "path": path})

    if not root.is_dir():
        add("ROOT_NOT_DIRECTORY", "Package root is not a directory.", root)
        return {"verdict": "fail", "finding_count": len(findings), "findings": findings}

    for name in sorted(REQUIRED_ROOT_FILES):
        if not (root / name).is_file():
            add("MISSING_ROOT_FILE", f"Missing required root file: {name}", name)
    for name in sorted(REQUIRED_DIRS):
        if not (root / name).is_dir():
            add("MISSING_REQUIRED_FOLDER", f"Missing required folder: {name}/", name)
        elif not (root / name / "MANIFEST.md").is_file():
            add("FOLDER_MANIFEST_MISSING", f"Missing {name}/MANIFEST.md", f"{name}/MANIFEST.md")

    # Contamination and portability.
    for p in root.rglob("*"):
        if "__pycache__" in p.parts or p.suffix == ".pyc":
            add("CACHE_CONTAMINATION", "Cache or bytecode artifact is forbidden.", p)
        if p.is_file():
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in ABSOLUTE_PATH_PATTERNS:
                if pattern.search(text):
                    add("ABSOLUTE_PATH_LEAK", "Workspace-specific absolute path found.", p)

    # Parse all JSON first.
    json_docs: dict[str, Any] = {}
    for p in sorted(root.rglob("*.json")):
        rel = p.relative_to(root).as_posix()
        try:
            json_docs[rel] = load_json(p)
        except Exception as exc:
            add("JSON_PARSE_ERROR", str(exc), rel)

    # Meta-validate schemas.
    schema_docs: dict[str, Any] = {}
    for p in sorted((root / "schema").glob("*.schema.json")):
        rel = p.relative_to(root).as_posix()
        try:
            schema = load_json(p)
            Draft202012Validator.check_schema(schema)
            if schema.get("$schema") != SCHEMA_DRAFT:
                add("SCHEMA_DRAFT_MISMATCH", "Schema must declare JSON Schema Draft 2020-12.", rel)
            schema_docs[rel] = schema
        except Exception as exc:
            add("SCHEMA_META_INVALID", str(exc), rel)

    # Schema index and complete JSON governance.
    index_path = root / "schema" / "schema-index.json"
    indexed_schema_paths: set[str] = set()
    bound_instances: dict[str, str] = {}
    exemptions: set[str] = set()
    if index_path.is_file() and "schema/schema-index.json" in json_docs:
        index = json_docs["schema/schema-index.json"]
        for rec in index.get("schemas", []):
            sp = rec.get("path")
            if not isinstance(sp, str):
                continue
            indexed_schema_paths.add(sp)
            target = root / sp
            if not target.is_file():
                add("SCHEMA_INDEX_MISSING_SCHEMA", f"Missing indexed schema: {sp}", "schema/schema-index.json")
            elif rec.get("sha256") != sha256_file(target):
                add("SCHEMA_INDEX_HASH_MISMATCH", f"Schema hash mismatch: {sp}", sp)
        for rec in index.get("bindings", []):
            inst, sch = rec.get("instance"), rec.get("schema")
            if isinstance(inst, str) and isinstance(sch, str):
                if inst in bound_instances:
                    add("DUPLICATE_SCHEMA_BINDING", f"Duplicate binding for {inst}", "schema/schema-index.json")
                bound_instances[inst] = sch
        exemptions = {x.get("path") for x in index.get("exemptions", []) if isinstance(x.get("path"), str)}

        actual_schema_paths = set(schema_docs)
        for missing in sorted(actual_schema_paths - indexed_schema_paths):
            add("UNINDEXED_SCHEMA", f"Schema is not indexed: {missing}", missing)
        for stale in sorted(indexed_schema_paths - actual_schema_paths):
            add("STALE_SCHEMA_INDEX_ENTRY", f"Index references a non-schema or missing file: {stale}", "schema/schema-index.json")

        for inst, sch in sorted(bound_instances.items()):
            if inst not in json_docs:
                add("BINDING_INSTANCE_MISSING", f"Bound instance is missing: {inst}", "schema/schema-index.json")
                continue
            if sch not in schema_docs:
                add("BINDING_SCHEMA_MISSING", f"Binding schema is missing: {sch}", "schema/schema-index.json")
                continue
            validator = Draft202012Validator(schema_docs[sch], format_checker=FormatChecker())
            errors = sorted(validator.iter_errors(json_docs[inst]), key=lambda e: list(e.absolute_path))
            for err in errors[:20]:
                locator = "/".join(str(x) for x in err.absolute_path)
                add("SCHEMA_INSTANCE_INVALID", f"{inst} at {locator or '<root>'}: {err.message}", inst)

        active_json = {
            rel for rel in json_docs
            if not (rel.startswith("schema/") and rel.endswith(".schema.json"))
        }
        for rel in sorted(active_json - set(bound_instances) - exemptions):
            add("UNGOVERNED_JSON_INSTANCE", f"Active JSON has no schema binding or exemption: {rel}", rel)

    # Manifest exactness and hashes.
    manifest_path = root / "manifest.json"
    if manifest_path.is_file() and "manifest.json" in json_docs:
        manifest = json_docs["manifest.json"]
        actual_files = rel_files(root)
        actual_dirs = rel_dirs(root)
        mfiles = [x.get("path") for x in manifest.get("files", [])]
        mdirs = [x.get("path") for x in manifest.get("folders", [])]
        if sorted(mfiles) != actual_files:
            add("MANIFEST_FILE_INVENTORY_MISMATCH", f"Manifest files={len(mfiles)}, actual={len(actual_files)}.", "manifest.json")
        if sorted(mdirs) != actual_dirs:
            add("MANIFEST_FOLDER_INVENTORY_MISMATCH", f"Manifest folders={len(mdirs)}, actual={len(actual_dirs)}.", "manifest.json")
        if len(mfiles) != len(set(mfiles)):
            add("MANIFEST_DUPLICATE_PATH", "Manifest contains duplicate file paths.", "manifest.json")
        for rec in manifest.get("files", []):
            rel = rec.get("path")
            if not isinstance(rel, str) or not (root / rel).is_file():
                continue
            actual_size = (root / rel).stat().st_size
            if rec.get("size_bytes") != actual_size:
                add("MANIFEST_SIZE_MISMATCH", f"Size mismatch for {rel}.", rel)
            if rel == "manifest.json":
                if rec.get("sha256") is not None:
                    add("MANIFEST_SELF_HASH_POLICY", "manifest.json sha256 must be null.", "manifest.json")
            elif rec.get("sha256") != sha256_file(root / rel):
                add("MANIFEST_HASH_MISMATCH", f"Hash mismatch for {rel}.", rel)

    # Core banks and references.
    metric_bank = json_docs.get("metrics/metric-bank.json", {})
    profile_bank = json_docs.get("profiles/archetype-bank.json", {})
    problem_bank = json_docs.get("problems/problem-bank.json", {})
    hard_gate_ids = {x.get("gate_id") for x in metric_bank.get("hard_gates", [])}
    drift_ids = {x.get("dimension_id") for x in metric_bank.get("drift_dimensions", [])}
    problem_ids = [x.get("problem_id") for x in problem_bank.get("patterns", [])]
    if len(problem_ids) != len(set(problem_ids)):
        add("DUPLICATE_PROBLEM_ID", "Problem IDs must be unique.", "problems/problem-bank.json")
    problem_id_set = set(problem_ids)

    common_weight = sum(x.get("weight", 0) for x in metric_bank.get("common_axes", []))
    if not math.isclose(common_weight, 100.0, abs_tol=1e-9):
        add("COMMON_AXIS_WEIGHT_TOTAL", f"Common-axis weights total {common_weight}, expected 100.", "metrics/metric-bank.json")
    metric_ids_by_stage: dict[str, set[str]] = {}
    default_weights: dict[str, dict[str, float]] = {}
    for stage, rows in metric_bank.get("stage_metrics", {}).items():
        ids = [x.get("metric_id") for x in rows]
        metric_ids_by_stage[stage] = set(ids)
        default_weights[stage] = {x.get("metric_id"): x.get("default_weight") for x in rows}
        if len(ids) != len(set(ids)):
            add("DUPLICATE_METRIC_ID", f"Duplicate metric ID in {stage}.", "metrics/metric-bank.json")
        total = sum(x.get("default_weight", 0) for x in rows)
        if not math.isclose(total, 100.0, abs_tol=1e-9):
            add("METRIC_WEIGHT_TOTAL", f"Default {stage} weights total {total}, expected 100.", "metrics/metric-bank.json")

    profile_paths: dict[str, str] = {}
    for rec in profile_bank.get("profiles", []):
        pid, path = rec.get("profile_id"), rec.get("path")
        if pid in profile_paths:
            add("DUPLICATE_ARCHETYPE_ID", f"Duplicate archetype ID: {pid}", "profiles/archetype-bank.json")
        profile_paths[pid] = path
        if not isinstance(path, str) or path not in json_docs:
            add("ARCHETYPE_PROFILE_MISSING", f"Missing archetype profile: {path}", "profiles/archetype-bank.json")

    profiles: dict[str, Any] = {}
    for pid, path in profile_paths.items():
        if path not in json_docs:
            continue
        prof = json_docs[path]
        profiles[pid] = prof
        if prof.get("profile_id") != pid:
            add("ARCHETYPE_ID_MISMATCH", f"Bank/profile ID mismatch for {pid}.", path)
        for stage in ("build_package", "agent_work", "build_result"):
            rows = prof.get("stage_metric_weights", {}).get(stage, [])
            total = sum(x.get("weight", 0) for x in rows)
            if not math.isclose(total, 100.0, abs_tol=1e-9):
                add("PROFILE_WEIGHT_TOTAL", f"{pid} {stage} weights total {total}, expected 100.", path)
            ids = {x.get("metric_id") for x in rows}
            if ids != metric_ids_by_stage.get(stage, set()):
                add("PROFILE_METRIC_SET_MISMATCH", f"{pid} {stage} metric set differs from metric bank.", path)
        for prob in prof.get("applicable_problem_ids", []):
            if prob not in problem_id_set:
                add("UNKNOWN_PROFILE_PROBLEM_REF", f"{pid} references unknown problem {prob}.", path)
        for did in prof.get("drift_dimensions", []):
            if did not in drift_ids:
                add("UNKNOWN_PROFILE_DRIFT_REF", f"{pid} references unknown drift dimension {did}.", path)

    for row in problem_bank.get("patterns", []):
        for gid in row.get("related_hard_gate_ids", []):
            if gid not in hard_gate_ids:
                add("UNKNOWN_PROBLEM_GATE_REF", f"{row.get('problem_id')} references unknown gate {gid}.", "problems/problem-bank.json")
        for aid in row.get("applicable_archetype_ids", []):
            if aid != "*" and aid not in profiles:
                add("UNKNOWN_PROBLEM_ARCHETYPE_REF", f"{row.get('problem_id')} references unknown archetype {aid}.", "problems/problem-bank.json")

    # Collect source, evidence, and claim IDs.
    source_sets: dict[str, Any] = {}
    source_ids: set[str] = set()
    version_ids: set[str] = set()
    for rel, doc in json_docs.items():
        if bound_instances.get(rel) == "schema/source-set.schema.json":
            source_sets[rel] = doc
            for v in doc.get("versions", []):
                vid = v.get("version_id")
                if vid in version_ids:
                    add("DUPLICATE_VERSION_ID", f"Duplicate version ID: {vid}", rel)
                version_ids.add(vid)
            local_versions = {v.get("version_id") for v in doc.get("versions", [])}
            for art in doc.get("artifacts", []):
                sid = art.get("source_id")
                if sid in source_ids:
                    add("DUPLICATE_SOURCE_ID", f"Duplicate source ID: {sid}", rel)
                source_ids.add(sid)
                if art.get("version_id") not in local_versions:
                    add("UNKNOWN_ARTIFACT_VERSION_REF", f"{sid} references unknown version.", rel)

    claim_ids: set[str] = set()
    claim_ledgers: dict[str, Any] = {}
    for rel, doc in json_docs.items():
        if bound_instances.get(rel) == "schema/claim-ledger.schema.json":
            claim_ledgers[rel] = doc
            by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for c in doc.get("claims", []):
                cid = c.get("claim_id")
                if cid in claim_ids:
                    add("DUPLICATE_CLAIM_ID", f"Duplicate claim ID: {cid}", rel)
                claim_ids.add(cid)
                by_source[c.get("source_id")].append(c)
                dims = c.get("weight_dimensions", {})
                raw = sum(dims.get(k, 0) for k in ["goal_impact","decision_leverage","dependency_centrality","scope_breadth","verification_burden"])
                if raw != c.get("raw_claim_weight"):
                    add("CLAIM_RAW_WEIGHT_MISMATCH", f"{cid} raw weight mismatch.", rel)
                score = c.get("claim_score")
                expected = None if score is None else round(c.get("normalized_claim_weight", 0) * score / 10, 2)
                if expected is not None and not math.isclose(expected, c.get("weighted_claim_score"), abs_tol=0.011):
                    add("CLAIM_WEIGHTED_SCORE_MISMATCH", f"{cid} weighted score mismatch.", rel)
            for sid, rows in by_source.items():
                total = round(sum(x.get("normalized_claim_weight", 0) for x in rows), 1)
                if not math.isclose(total, 100.0, abs_tol=0.05):
                    add("CLAIM_WEIGHT_TOTAL", f"{sid} normalized claim weights total {total}, expected 100.0.", rel)
            for c in doc.get("claims", []):
                for dep in c.get("dependency_on_other_claims", []):
                    if dep not in {x.get("claim_id") for x in doc.get("claims", [])}:
                        add("UNKNOWN_CLAIM_DEPENDENCY", f"{c.get('claim_id')} references unknown dependency {dep}.", rel)

    evidence_ids: set[str] = set()
    evidence_ledgers: dict[str, Any] = {}
    for rel, doc in json_docs.items():
        if bound_instances.get(rel) == "schema/evidence-ledger.schema.json":
            evidence_ledgers[rel] = doc
            for e in doc.get("entries", []):
                eid = e.get("evidence_id")
                if eid in evidence_ids:
                    add("DUPLICATE_EVIDENCE_ID", f"Duplicate evidence ID: {eid}", rel)
                evidence_ids.add(eid)
                for cid in e.get("supports_claim_ids", []):
                    if claim_ids and cid not in claim_ids:
                        add("UNKNOWN_EVIDENCE_CLAIM_REF", f"{eid} references unknown claim {cid}.", rel)

    # Check claim evidence references after all evidence IDs are known.
    for rel, doc in claim_ledgers.items():
        for c in doc.get("claims", []):
            if c.get("source_id") not in source_ids:
                add("UNKNOWN_CLAIM_SOURCE_REF", f"{c.get('claim_id')} references unknown source {c.get('source_id')}.", rel)
            for eid in c.get("evidence_refs", []):
                if eid not in evidence_ids:
                    add("UNKNOWN_CLAIM_EVIDENCE_REF", f"{c.get('claim_id')} references unknown evidence {eid}.", rel)

    # Report arithmetic and reference integrity.
    for rel, report in json_docs.items():
        if bound_instances.get(rel) != "schema/evaluation-report.schema.json":
            continue
        local_versions = set(report.get("project", {}).get("version_ids", []))
        profile_id = report.get("archetype_selection", {}).get("primary_profile_id")
        selected_profile = profiles.get(profile_id)
        if selected_profile is None:
            add("UNKNOWN_REPORT_ARCHETYPE", f"Unknown report archetype: {profile_id}", rel)
        for sn in report.get("source_normalization", []):
            if sn.get("source_id") not in source_ids:
                add("UNKNOWN_REPORT_SOURCE_REF", f"Unknown report source: {sn.get('source_id')}", rel)
            if sn.get("version_id") not in local_versions:
                add("UNKNOWN_REPORT_VERSION_REF", f"Unknown normalized version: {sn.get('version_id')}", rel)

        result_scores: dict[str, float] = {}
        for stage in report.get("stage_evaluations", []):
            input_type = stage.get("input_type")
            if stage.get("version_id") not in local_versions:
                add("UNKNOWN_STAGE_VERSION_REF", f"Unknown stage version: {stage.get('version_id')}", rel)
            for sid in stage.get("source_ids", []):
                if sid not in source_ids:
                    add("UNKNOWN_STAGE_SOURCE_REF", f"Unknown stage source: {sid}", rel)
            expected_weights = {}
            if selected_profile:
                expected_weights = {x.get("metric_id"): x.get("weight") for x in selected_profile.get("stage_metric_weights", {}).get(input_type, [])}
            calc = 0.0
            for m in stage.get("metrics", []):
                mid, weight, score = m.get("metric_id"), m.get("weight"), m.get("score")
                if mid not in metric_ids_by_stage.get(input_type, set()):
                    add("UNKNOWN_REPORT_METRIC", f"Unknown {input_type} metric {mid}.", rel)
                if expected_weights and not math.isclose(weight, expected_weights.get(mid, -1), abs_tol=1e-9):
                    add("REPORT_PROFILE_WEIGHT_MISMATCH", f"{mid} weight does not match selected profile.", rel)
                expected = None if score is None else round(weight * score / 10, 4)
                if expected is not None:
                    calc += expected
                    if not math.isclose(expected, m.get("weighted_score"), abs_tol=0.00011):
                        add("REPORT_WEIGHTED_SCORE_MISMATCH", f"{stage.get('stage_evaluation_id')} {mid} weighted score mismatch.", rel)
                for eid in m.get("evidence_refs", []):
                    if eid not in evidence_ids:
                        add("UNKNOWN_REPORT_EVIDENCE_REF", f"{mid} references unknown evidence {eid}.", rel)
            stage_score = stage.get("stage_score")
            if stage_score is not None and not math.isclose(round(calc, 2), stage_score, abs_tol=0.011):
                add("REPORT_STAGE_SCORE_MISMATCH", f"{stage.get('stage_evaluation_id')} score {stage_score}, calculated {round(calc,2)}.", rel)
            failed = any(g.get("status") == "fail" for g in stage.get("hard_gates", []))
            verdict = stage.get("verdict")
            coverage = stage.get("evidence_coverage", 0)
            if failed and verdict != "FAIL":
                add("VERDICT_POLICY_VIOLATION", "Failed hard gate requires FAIL.", rel)
            if stage_score is None and verdict not in {"NOT_EVALUATED","INSUFFICIENT_EVIDENCE"}:
                add("VERDICT_POLICY_VIOLATION", "Null score requires NOT_EVALUATED or INSUFFICIENT_EVIDENCE.", rel)
            if stage_score is not None and not failed:
                if coverage < 0.5 and verdict != "INSUFFICIENT_EVIDENCE":
                    add("VERDICT_POLICY_VIOLATION", "Coverage below 0.50 requires INSUFFICIENT_EVIDENCE.", rel)
                elif stage_score < 70 and verdict != "FAIL":
                    add("VERDICT_POLICY_VIOLATION", "Score below 70 requires FAIL.", rel)
                elif 70 <= stage_score < 85 and verdict != "CONDITIONAL_PASS":
                    add("VERDICT_POLICY_VIOLATION", "Score from 70 to 84.99 requires CONDITIONAL_PASS.", rel)
                elif stage_score >= 85 and coverage >= 0.8 and verdict != "PASS":
                    add("VERDICT_POLICY_VIOLATION", "Eligible score and coverage require PASS unless another declared blocker exists.", rel)
            for g in stage.get("hard_gates", []):
                if g.get("gate_id") not in hard_gate_ids:
                    add("UNKNOWN_REPORT_GATE", f"Unknown gate {g.get('gate_id')}.", rel)
                for eid in g.get("evidence_refs", []):
                    if eid not in evidence_ids:
                        add("UNKNOWN_REPORT_EVIDENCE_REF", f"Gate references unknown evidence {eid}.", rel)
            if input_type == "build_result" and stage_score is not None:
                result_scores[stage.get("version_id")] = stage_score

        common_axis_ids = {x.get("axis_id") for x in metric_bank.get("common_axes", [])}
        common_weight_map = {x.get("axis_id"): x.get("weight") for x in metric_bank.get("common_axes", [])}
        for ce in report.get("common_axis_evaluations", []):
            if ce.get("source_id") not in source_ids:
                add("UNKNOWN_COMMON_AXIS_SOURCE", f"Unknown common-axis source {ce.get('source_id')}.", rel)
            calc = 0.0
            seen: set[str] = set()
            for a in ce.get("axes", []):
                aid, weight, score = a.get("axis_id"), a.get("weight"), a.get("score")
                seen.add(aid)
                if aid not in common_axis_ids:
                    add("UNKNOWN_REPORT_AXIS", f"Unknown axis {aid}.", rel)
                if not math.isclose(weight, common_weight_map.get(aid, -1), abs_tol=1e-9):
                    add("REPORT_AXIS_WEIGHT_MISMATCH", f"Axis {aid} weight mismatch.", rel)
                expected = None if score is None else round(weight * score / 10, 4)
                if expected is not None:
                    calc += expected
                    if not math.isclose(expected, a.get("weighted_score"), abs_tol=0.00011):
                        add("REPORT_AXIS_SCORE_MISMATCH", f"Axis {aid} weighted score mismatch.", rel)
                for cid in a.get("claim_ids", []):
                    if cid not in claim_ids:
                        add("UNKNOWN_REPORT_CLAIM_REF", f"Axis references unknown claim {cid}.", rel)
            if seen != common_axis_ids:
                add("REPORT_AXIS_SET_MISMATCH", "Common-axis set is incomplete or contains extras.", rel)
            if ce.get("whole_document_score") is not None and not math.isclose(round(calc,2), ce.get("whole_document_score"), abs_tol=0.011):
                add("REPORT_WHOLE_SCORE_MISMATCH", f"Whole-document score mismatch for {ce.get('source_id')}.", rel)

        for cmp in report.get("comparisons", []):
            if cmp.get("from_version_id") not in local_versions or cmp.get("to_version_id") not in local_versions:
                add("UNKNOWN_COMPARISON_VERSION_REF", f"Comparison {cmp.get('comparison_id')} references unknown version.", rel)
            for d in cmp.get("drift_findings", []):
                if d.get("dimension_id") not in drift_ids:
                    add("UNKNOWN_REPORT_DRIFT_REF", f"Unknown drift dimension {d.get('dimension_id')}.", rel)
                for eid in d.get("evidence_refs", []):
                    if eid not in evidence_ids:
                        add("UNKNOWN_REPORT_EVIDENCE_REF", f"Drift finding references unknown evidence {eid}.", rel)
        for pm in report.get("problem_matches", []):
            if pm.get("problem_id") not in problem_id_set:
                add("UNKNOWN_REPORT_PROBLEM_REF", f"Unknown problem {pm.get('problem_id')}.", rel)
            for vid in pm.get("version_ids", []):
                if vid not in local_versions:
                    add("UNKNOWN_REPORT_VERSION_REF", f"Problem match references unknown version {vid}.", rel)
            for eid in pm.get("evidence_refs", []):
                if eid not in evidence_ids:
                    add("UNKNOWN_REPORT_EVIDENCE_REF", f"Problem match references unknown evidence {eid}.", rel)

        selected = report.get("baseline_recommendation", {}).get("selected_version_id")
        if selected is not None and selected not in local_versions:
            add("UNKNOWN_BASELINE_VERSION_REF", f"Unknown baseline version {selected}.", rel)
        for row in report.get("final_verdict", {}).get("ranking", []):
            vid = row.get("version_id")
            if vid not in local_versions:
                add("UNKNOWN_RANKING_VERSION_REF", f"Unknown ranking version {vid}.", rel)
            if vid in result_scores and row.get("score") is not None and not math.isclose(row.get("score"), result_scores[vid], abs_tol=0.011):
                add("RANKING_SCORE_MISMATCH", f"Ranking score for {vid} differs from build-result score.", rel)

    # Production prompt marker.
    prompt_path = root / "adr" / "adr-005.md"
    if prompt_path.is_file():
        text = prompt_path.read_text(encoding="utf-8")
        required_markers = [
            "PRODUCTION-GRADE V1.0 BUILD PROMPT",
            "## GOAL", "## OBJECTIVES", "## REQUIRED MUTATION SUITE",
            "## ACCEPTANCE GATES", "Do not state “production-grade”"
        ]
        missing = [x for x in required_markers if x not in text]
        if missing:
            add("PRODUCTION_PROMPT_MISSING", f"Production prompt missing markers: {missing}", "adr/adr-005.md")

    return {
        "verdict": "pass" if not findings else "fail",
        "finding_count": len(findings),
        "findings": findings,
        "summary": {
            "json_count": len(json_docs),
            "schema_count": len(schema_docs),
            "binding_count": len(bound_instances),
            "profile_count": len(profiles),
            "problem_count": len(problem_id_set),
            "claim_count": len(claim_ids),
            "evidence_count": len(evidence_ids),
        },
    }


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    result = validate_package(root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
