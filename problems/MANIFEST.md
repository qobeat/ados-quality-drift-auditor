# problems/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | quality-failure_pattern_bank |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `problems/`. |
| HOW_TO_USE | Match only when observed signals and evidence support the pattern. |
| DOCUMENT_CONTENT | Purpose and current contents of `problems/`. |

## Role

Quality-failure pattern bank.

## Current files

- `problem-bank.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
