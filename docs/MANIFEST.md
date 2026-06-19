# docs/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | method_documentation |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `docs/`. |
| HOW_TO_USE | Use these documents for archetype, metric, drift, evidence, workflow, and reporting details. |
| DOCUMENT_CONTENT | Purpose and current contents of `docs/`. |

## Role

Method documentation.

## Current files

- `ARCHETYPE_MODEL.md`
- `DRIFT_MODEL.md`
- `EVIDENCE_AND_CLAIMS.md`
- `METRICS.md`
- `REPORTING.md`
- `WORKFLOW.md`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
