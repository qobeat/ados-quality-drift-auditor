#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
sys.dont_write_bytecode = True
import shutil
import tempfile
from pathlib import Path

from validate_package import validate_package


def mutate_json(path: Path, fn) -> None:
    doc = json.loads(path.read_text(encoding="utf-8"))
    fn(doc)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    package_root = Path(__file__).resolve().parents[1]
    baseline = validate_package(package_root)
    results = [{"test_id": "BASELINE", "expected": "pass", "observed": baseline["verdict"], "pass": baseline["verdict"] == "pass"}]
    if baseline["verdict"] != "pass":
        print(json.dumps({"verdict": "fail", "results": results, "baseline_findings": baseline["findings"]}, indent=2, ensure_ascii=False))
        return 1

    mutations = []

    def add_case(case_id, expected_code, mutator):
        mutations.append((case_id, expected_code, mutator))

    add_case("UNREGISTERED_FILE", "MANIFEST_FILE_INVENTORY_MISMATCH",
             lambda r: (r / "rogue.txt").write_text("unregistered\n", encoding="utf-8"))

    def bad_profile_weight(r: Path):
        p = r / "profiles" / "multi-artifact-profile-runtime.json"
        mutate_json(p, lambda d: d["stage_metric_weights"]["build_result"][0].update({"weight": d["stage_metric_weights"]["build_result"][0]["weight"] + 1}))
    add_case("PROFILE_WEIGHT", "PROFILE_WEIGHT_TOTAL", bad_profile_weight)

    def bad_verdict(r: Path):
        p = r / "out" / "example-ados-glossary-evolution-report.json"
        def mutate(d):
            for stage in d["stage_evaluations"]:
                if stage["stage_evaluation_id"] == "STAGEEVAL-V1.5-BUILD-PACKAGE":
                    stage["verdict"] = "PASS"
        mutate_json(p, mutate)
    add_case("PREMATURE_PASS", "VERDICT_POLICY_VIOLATION", bad_verdict)

    def bad_claim_total(r: Path):
        p = r / "out" / "example-ados-glossary-claim-ledger.json"
        mutate_json(p, lambda d: d["claims"][0].update({"normalized_claim_weight": d["claims"][0]["normalized_claim_weight"] + 1}))
    add_case("CLAIM_WEIGHT", "CLAIM_WEIGHT_TOTAL", bad_claim_total)

    def remove_prompt_marker(r: Path):
        p = r / "adr" / "adr-005.md"
        p.write_text(p.read_text(encoding="utf-8").replace("## REQUIRED MUTATION SUITE", "## MUTATION TESTS"), encoding="utf-8")
    add_case("PRODUCTION_PROMPT", "PRODUCTION_PROMPT_MISSING", remove_prompt_marker)

    def unknown_problem(r: Path):
        p = r / "out" / "example-ados-glossary-evolution-report.json"
        mutate_json(p, lambda d: d["problem_matches"][0].update({"problem_id": "PROB-999"}))
    add_case("UNKNOWN_PROBLEM", "UNKNOWN_REPORT_PROBLEM_REF", unknown_problem)

    with tempfile.TemporaryDirectory(prefix="ados-qda-self-test-") as td:
        td_path = Path(td)
        for case_id, expected_code, mutator in mutations:
            case_root = td_path / case_id
            shutil.copytree(package_root, case_root)
            mutator(case_root)
            result = validate_package(case_root)
            codes = {f["code"] for f in result["findings"]}
            ok = result["verdict"] == "fail" and expected_code in codes
            results.append({
                "test_id": case_id,
                "expected": expected_code,
                "observed_codes": sorted(codes),
                "pass": ok,
            })

    verdict = "pass" if all(x["pass"] for x in results) else "fail"
    print(json.dumps({"verdict": verdict, "test_count": len(results), "results": results}, indent=2, ensure_ascii=False))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
