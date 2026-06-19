# ADOS Quality Drift Auditor v0.1 Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | registry |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | package_manifest_and_agent_bootstrap |
| GOVERNANCE_AREA | governance; execution |
| CONSUMERS | owner; architect; evaluator; builder; reviewer; self_test |
| WHEN_TO_USE | Read before running or modifying the package. |
| HOW_TO_USE | Follow the load order and execution sequence below; use `manifest.json` for exact inventory and hashes. |
| DOCUMENT_CONTENT | Agent instructions, authority order, package boundary, folder roles, and validation sequence. |

## Agent bootstrap

1. Read `PACKAGE.json` for identity, GOAL, OBJECTIVES, standards, and entrypoints.
2. Read this `MANIFEST.md`.
3. Read `GLOSSARY.md` before interpreting project terms.
4. Read `PDD.md`.
5. Read `adr/index.json` and all accepted ADRs. `adr/adr-005.md` is the full v1.0 production prompt.
6. Load `profiles/archetype-bank.json`.
7. Load `metrics/metric-bank.json` and `metrics/report-policy.json`.
8. Load `problems/problem-bank.json`.
9. Load `skills/PROJECT-EVOLUTION-QUALITY-AUDITOR.md` and its JSON companion.
10. Validate the package before evaluating any project.

## Run sequence

```bash
python tools/validate_package.py .
python tools/self_test.py
python tools/initialize_audit.py examples/ados-glossary-evolution-input.json out/new-audit.json
python tools/validate_report.py out/new-audit.json
```

Complete the initialized report by following the skill. Create claim and evidence ledgers before adding scores.

## Authority order

```text
PACKAGE.json
→ MANIFEST.md
→ GLOSSARY.md
→ PDD.md
→ accepted ADRs
→ archetype bank and selected profile
→ metric bank and report policy
→ problem bank
→ skill
→ schemas
→ project-specific source set and evidence
```

Project-specific sources do not override this package’s scoring or schema rules unless an explicit package ADR changes them.

## Folder roles

| Folder | Role |
|---|---|
| `adr/` | Architectural decisions and v1.0 production prompt |
| `schema/` | JSON Schema Draft 2020-12 contracts and bindings |
| `skills/` | Human and machine execution skill |
| `profiles/` | Archetype bank and profiles |
| `metrics/` | Stage metrics, common axes, drift dimensions, hard gates, verdict policy |
| `problems/` | Problem-pattern bank |
| `docs/` | Explanatory method documents |
| `examples/` | Input templates and ADOS v1.4/v1.5 problem examples |
| `tools/` | Validator, self-test, initializer, and report validator |
| `out/` | Schema-conformant reports |

## Input boundary

Inputs may contain arbitrary project artifacts. Inventorying them does not authorize executing them. v0.1 tools do not execute untrusted source artifacts.

## Output boundary

All generated evaluation records belong in `out/`. Do not write evaluation results into the source packages being evaluated.

## Validation contract

A package PASS requires:

- exact file and folder inventory;
- SHA-256 for every file except the self-referential `manifest.json` entry;
- JSON parsing;
- schema meta-validation;
- complete JSON instance governance;
- binding validation;
- weight totals;
- stable-ID and reference integrity;
- report arithmetic and verdict policy;
- production prompt markers;
- representative mutation self-tests.

## Package inventory

The exact machine inventory, sizes, roles, and hashes are in `manifest.json`. The schema binding inventory is in `schema/schema-index.json`.

## Non-drift rule

Do not weaken schemas, evidence fields, hard gates, or verdict rules to make a failing report pass. Correct the report or source evaluation instead.
