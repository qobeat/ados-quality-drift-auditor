# examples/ Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | input_and_real-problem_examples |
| GOVERNANCE_AREA | package |
| CONSUMERS | evaluator; architect; maintainer; self_test |
| WHEN_TO_USE | Read before using or modifying files in `examples/`. |
| HOW_TO_USE | Examples illustrate usage and are not hidden authority for other projects. |
| DOCUMENT_CONTENT | Purpose and current contents of `examples/`. |

## Role

Input and real-problem examples.

## Current files

- `ados-glossary-evolution-input.json`
- `ados-glossary-problem-examples.md`
- `input-template.json`

## Change rule

Register new JSON instances in `schema/schema-index.json`, update `manifest.json`, and rerun `tools/validate_package.py` plus `tools/self_test.py`.
