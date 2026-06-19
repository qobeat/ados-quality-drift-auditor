# tools/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | validation_and_initialization_tools |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `tools/`. |
| HOW_TO_USE | Run package validation, mutation self-tests, report validation, and audit initialization. |
| DOCUMENT_CONTENT | Purpose and current contents of `tools/`. |

## Role

Validation and initialization tools.

## Current files

- `initialize_audit.py`
- `self_test.py`
- `validate_package.py`
- `validate_report.py`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
