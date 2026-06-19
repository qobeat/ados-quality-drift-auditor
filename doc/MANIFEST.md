# Documentation Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | folder_manifest |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | documentation_navigation |
| GOVERNANCE_AREA | documentation |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when locating explanatory doctrine for the auditor. |
| HOW_TO_USE | Read GLOSSARY.md first, then use this manifest to select supporting documents. Documentation explains concepts; accepted architecture choices remain in adr/. |
| DOCUMENT_CONTENT | Navigation and roles for adapted ADOS doctrine documents. |


## Documentation roles

| File | Role |
|---|---|
| `DOCUMENT_METADATA.md` | ADOS document metadata fields and usage. |
| `EXECUTION_FLOW.md` | Reference execution-flow concepts and the auditor non-governance boundary. |
| `ONTOLOGY.md` | Concept relations for Project evolution and drift auditing. |
| `TAXONOMY.md` | Classification hierarchy for Archetypes, Domains, inputs, drift, and evidence. |
| `WORKFLOW.md` | Semantic audit flow; not mandatory agent execution governance. |
| `COMPETENCY_QUESTIONS.md` | Questions v0.2 should be able to answer. |
| `RDF_SKOS_OWL_SHACL.md` | Optional semantic-web export boundary. |
| `SIMPLIFIED_RDF_SHACL_LAYER.md` | Relationship between Markdown, JSON Schema, and optional RDF layers. |
| `PILLARS.md` | Adapted twenty-pillar doctrine. |
| `GOAL_ATTRACTOR_GEOMETRY.md` | Geometry model for quality drift. |
| `COORDINATE_MODEL.md` | Coordinate Dimension and Coordinate design. |
| `METRIC_MODEL.md` | Metric derivation and guardrails. |
| `REQUIREMENTS_DOCTRINE.md` | Requirement applicability and traceability doctrine. |
| `PROJECT_REQUIREMENTS_MODEL.md` | Generalized Project Requirement model replacing app-wide terminology. |
| `IMPLEMENTATION_METHODOLOGY.md` | Recommended evaluator implementation sequence. |
| `SOURCE_ADAPTATION.md` | Source review and adaptation decisions. |

## Boundary

These documents explain doctrine and methods. They do not override `GLOSSARY.md`, accepted ADRs, or JSON schemas.
