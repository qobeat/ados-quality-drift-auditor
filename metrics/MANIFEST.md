# metrics/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | quality_metrics_and_verdict_policy |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `metrics/`. |
| HOW_TO_USE | Use archetype stage weights, fixed common axes, hard gates, and report policy. |
| DOCUMENT_CONTENT | Purpose and current contents of `metrics/`. |

## Role

Quality metrics and verdict policy.

## Current files

- `metric-bank.json`
- `report-policy.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
