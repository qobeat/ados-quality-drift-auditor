#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_report.py <report.json>", file=sys.stderr)
        return 2
    root = Path(__file__).resolve().parents[1]
    report_path = Path(sys.argv[1])
    schema = json.loads((root / "schema" / "evaluation-report.schema.json").read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(report), key=lambda e: list(e.absolute_path))
    result = {
        "verdict": "pass" if not errors else "fail",
        "finding_count": len(errors),
        "findings": [
            {"path": "/".join(str(x) for x in e.absolute_path) or "<root>", "message": e.message}
            for e in errors[:50]
        ],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
