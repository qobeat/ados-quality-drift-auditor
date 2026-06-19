# Optional RDF / SKOS / OWL / SHACL Boundary

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | semantic_export_boundary |
| GOVERNANCE_AREA | schema; glossary |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when considering semantic-web exports for glossary concepts. |
| HOW_TO_USE | Treat JSON Schema as the active machine-structure guardrail. RDF-family exports are optional interoperability surfaces for later versions. |
| DOCUMENT_CONTENT | Boundary for optional semantic-web exports. |


## v0.2 decision

v0.2 does not ship RDF, SKOS, OWL, or SHACL instance files. It preserves the concept-oriented methodology and a future-compatible boundary.

| Layer | Potential future role |
|---|---|
| SKOS | Publish preferred terms, definitions, broader/narrower relations, and related concepts. |
| OWL | Express minimal concept classes and properties. |
| SHACL | Express graph-level constraints if RDF instances become active. |
| JSON Schema | Validate active JSON banks, skill, source sets, and reports in v0.2. |

## Complexity rule

Do not introduce mandatory advanced reasoning, external ontology imports, or full SHACL execution without an ADR and demonstrated need.

## Synchronization rule

If semantic exports are added later, `GLOSSARY.md` remains the semantic authority and exports must be generated or checked against stable term IDs.
