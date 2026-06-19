# profiles/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | archetype_profiles |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `profiles/`. |
| HOW_TO_USE | Select one primary profile through `archetype-bank.json`; validate weights and references. |
| DOCUMENT_CONTENT | Purpose and current contents of `profiles/`. |

## Role

Archetype profiles.

## Current files

- `archetype-bank.json`
- `data-pipeline-dataset.json`
- `documentation-specification.json`
- `general-engineered-artifact.json`
- `infrastructure-platform.json`
- `ml-agent-system.json`
- `multi-artifact-profile-runtime.json`
- `policy-control-pack.json`
- `schema-governed-knowledge.json`
- `software-application-service.json`
- `software-library-cli-sdk.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
