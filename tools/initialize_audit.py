#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Z0-9._-]+", "-", value.upper()).strip("-") or "UNSET"


def validate(instance, schema, label: str) -> None:
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(instance),
        key=lambda e: list(e.absolute_path),
    )
    if errors:
        lines = [f"{label} is invalid:"]
        for err in errors[:20]:
            loc = "/".join(str(x) for x in err.absolute_path) or "<root>"
            lines.append(f"- {loc}: {err.message}")
        raise ValueError("\n".join(lines))


def choose_profile(source_set: dict, package_root: Path) -> tuple[dict, float, list[dict]]:
    bank = load(package_root / "profiles" / "archetype-bank.json")
    profiles = [load(package_root / rec["path"]) for rec in bank["profiles"]]
    declared = source_set["project"].get("declared_archetype_id")
    by_id = {p["profile_id"]: p for p in profiles}
    if declared in by_id:
        alternatives = [
            {"profile_id": p["profile_id"], "confidence": 0.0, "reason_not_selected": "A valid declared archetype was supplied; confirm it during substantive evaluation."}
            for p in profiles if p["profile_id"] != declared
        ][:2]
        return by_id[declared], 0.95, alternatives

    text = " ".join([
        source_set["project"].get("name", ""),
        source_set["project"].get("description", ""),
        *[a.get("name", "") + " " + a.get("role", "") + " " + " ".join(a.get("evidence_scope", [])) for a in source_set["artifacts"]],
    ]).lower()

    ranked = []
    for p in profiles:
        signals = [s.lower() for s in p["selection"]["positive_signals"]]
        matches = sum(1 for s in signals if s in text)
        exclusions = sum(1 for s in p["selection"]["exclusion_signals"] if s.lower() in text)
        score = max(0.0, min(1.0, matches / max(1, len(signals)) - 0.20 * exclusions))
        ranked.append((score, p))
    ranked.sort(key=lambda x: (-x[0], x[1]["profile_id"]))
    best_score, best = ranked[0]
    if best_score < 0.60:
        best = by_id["ARCH-GENERAL-ENGINEERED-ARTIFACT"]
        best_score = max(best_score, 0.40)
    alternatives = [
        {"profile_id": p["profile_id"], "confidence": round(score, 2), "reason_not_selected": "Lower preliminary signal match; substantive evaluator review is required."}
        for score, p in ranked if p["profile_id"] != best["profile_id"]
    ][:2]
    return best, round(best_score, 2), alternatives


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: initialize_audit.py <source-set.json> <output-report.json>", file=sys.stderr)
        return 2

    source_path = Path(sys.argv[1]).resolve()
    output_path = Path(sys.argv[2]).resolve()
    package_root = Path(__file__).resolve().parents[1]

    source_set = load(source_path)
    validate(source_set, load(package_root / "schema" / "source-set.schema.json"), "source set")

    profile, confidence, alternatives = choose_profile(source_set, package_root)
    metric_bank = load(package_root / "metrics" / "metric-bank.json")
    metric_names = {
        m["metric_id"]: m["name"]
        for rows in metric_bank["stage_metrics"].values()
        for m in rows
    }

    artifacts_by_stage = defaultdict(list)
    for art in source_set["artifacts"]:
        artifacts_by_stage[(art["version_id"], art["input_type"])].append(art)

    stage_evaluations = []
    for (version_id, input_type), artifacts in sorted(artifacts_by_stage.items()):
        metrics = []
        for row in profile["stage_metric_weights"][input_type]:
            metrics.append({
                "metric_id": row["metric_id"],
                "weight": row["weight"],
                "score": None,
                "weighted_score": None,
                "status": "not_scored",
                "evidence_refs": [],
                "rationale": f"{metric_names[row['metric_id']]} has not been evaluated.",
            })
        stage_evaluations.append({
            "stage_evaluation_id": f"STAGEEVAL-{safe_id(version_id)}-{safe_id(input_type)}",
            "version_id": version_id,
            "input_type": input_type,
            "source_ids": [a["source_id"] for a in artifacts],
            "profile_id": profile["profile_id"],
            "metrics": metrics,
            "stage_score": None,
            "evidence_coverage": 0.0,
            "hard_gates": [],
            "verdict": "NOT_EVALUATED",
            "strengths": [],
            "limitations": ["Substantive claim and evidence evaluation has not been performed."],
        })

    source_normalization = [{
        "source_id": a["source_id"],
        "version_id": a["version_id"],
        "input_type": a["input_type"],
        "source_name": a["name"],
        "source_type": a["media_type"],
        "apparent_scope": ", ".join(a["evidence_scope"]),
        "primary_purpose": a["role"],
        "assumed_target_user": "To be confirmed by evaluator.",
        "evidence_basis": a["availability"],
    } for a in source_set["artifacts"]]

    version_ids = [v["version_id"] for v in sorted(source_set["versions"], key=lambda x: x["sequence"])]
    input_types = sorted({a["input_type"] for a in source_set["artifacts"]})

    report = {
        "$schema": "../schema/evaluation-report.schema.json",
        "schema_version": "0.1.0",
        "report_id": f"REPORT-{safe_id(source_set['project']['project_id'])}-INITIAL",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "project": {
            "project_id": source_set["project"]["project_id"],
            "name": source_set["project"]["name"],
            "version_ids": version_ids,
        },
        "source_set_ref": str(source_path),
        "claim_ledger_ref": None,
        "evidence_ledger_ref": None,
        "evaluation_scope": {
            "version_ids": version_ids,
            "input_types": input_types,
            "excluded_items": [],
        },
        "source_normalization": source_normalization,
        "archetype_selection": {
            "primary_profile_id": profile["profile_id"],
            "confidence": confidence,
            "rationale": "Preliminary selection from declared archetype or profile signals; the evaluator must confirm it against project purpose and failure modes.",
            "evidence_refs": [],
            "alternatives": alternatives,
        },
        "evidence_assessment": {
            "coverage": 0.0,
            "independence": 0.0,
            "decisive_gaps": ["Evidence ledger and atomic claim ledger have not been created."],
            "assessment": "insufficient",
        },
        "stage_evaluations": stage_evaluations,
        "common_axis_evaluations": [],
        "comparisons": [],
        "problem_matches": [],
        "baseline_recommendation": {
            "selected_version_id": None,
            "confidence": 0.0,
            "rationale": "No baseline has been evaluated.",
            "donor_components": [],
            "rejected_alternatives": [],
        },
        "final_verdict": {
            "overall": "NOT_EVALUATED",
            "ranking": [
                {"version_id": vid, "rank": i + 1, "score": None}
                for i, vid in enumerate(version_ids)
            ],
            "decisive_reasons": [],
            "priority_actions": [
                "Create evidence and claim ledgers.",
                "Confirm the archetype.",
                "Complete stage and common-axis scoring.",
            ],
            "limitations": ["This file is an initialized scaffold, not an evaluation."],
        },
    }

    validate(report, load(package_root / "schema" / "evaluation-report.schema.json"), "report")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": "pass", "output": str(output_path), "profile_id": profile["profile_id"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
