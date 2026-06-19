# Simplified Semantic-Layer Mapping

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | semantic_layer_mapping |
| GOVERNANCE_AREA | schema; glossary |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when mapping current v0.2 surfaces to possible RDF/SHACL roles. |
| HOW_TO_USE | Use this as an explanatory analogy only. It does not create RDF authority in v0.2. |
| DOCUMENT_CONTENT | Mapping between Markdown, JSON guardrails, and optional semantic-web layers. |


| Semantic role | v0.2 surface |
|---|---|
| Vocabulary authority | `GLOSSARY.md` |
| Concept relations | `doc/ONTOLOGY.md` and `doc/TAXONOMY.md` |
| Structured configuration | JSON banks under `profiles/`, `metrics/`, and `problems/` |
| Shapes / constraints | `schema/*.schema.json` |
| Project instances | User-supplied source sets and `out/*.json` reports |
| Validation result | External schema validation or host-agent checking |

JSON Schema is the active structural guardrail. Markdown remains the human semantic authority.
