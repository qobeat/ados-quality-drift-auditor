# schema/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | JSON_Schema_authority |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `schema/`. |
| HOW_TO_USE | Meta-validate every `*.schema.json`, then validate instances through `schema-index.json`. |
| DOCUMENT_CONTENT | Purpose and current contents of `schema/`. |

## Role

Json schema authority.

## Current files

- `adr-index.schema.json`
- `archetype-bank.schema.json`
- `archetype-profile.schema.json`
- `claim-ledger.schema.json`
- `evaluation-report.schema.json`
- `evidence-ledger.schema.json`
- `manifest.schema.json`
- `metric-bank.schema.json`
- `package.schema.json`
- `problem-bank.schema.json`
- `report-policy.schema.json`
- `schema-index.schema.json`
- `skill.schema.json`
- `source-set.schema.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
