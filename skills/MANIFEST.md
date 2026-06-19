# skills/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | execution_skill |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `skills/`. |
| HOW_TO_USE | Load the Markdown skill for method and JSON skill for machine routing. |
| DOCUMENT_CONTENT | Purpose and current contents of `skills/`. |

## Role

Execution skill.

## Current files

- `PROJECT-EVOLUTION-QUALITY-AUDITOR.json`
- `PROJECT-EVOLUTION-QUALITY-AUDITOR.md`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
