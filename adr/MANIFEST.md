# adr/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | architecture_decisions |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `adr/`. |
| HOW_TO_USE | Read accepted decisions before changing evaluation contracts; `adr-005.md` contains the complete v1.0 build prompt. |
| DOCUMENT_CONTENT | Purpose and current contents of `adr/`. |

## Role

Architecture decisions.

## Current files

- `adr-001.md`
- `adr-002.md`
- `adr-003.md`
- `adr-004.md`
- `adr-005.md`
- `index.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
