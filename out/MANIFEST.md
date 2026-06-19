# out/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | machine-readable_reports |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `out/`. |
| HOW_TO_USE | Store claim ledgers, evidence ledgers, and evaluation reports here; preserve provided examples. |
| DOCUMENT_CONTENT | Purpose and current contents of `out/`. |

## Role

Machine-readable reports.

## Current files

- `example-ados-glossary-claim-ledger.json`
- `example-ados-glossary-evidence-ledger.json`
- `example-ados-glossary-evolution-report.json`
- `report-template.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
