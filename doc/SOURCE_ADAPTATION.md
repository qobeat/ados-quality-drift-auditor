# Source Adaptation Record

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | review_report |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | source_adaptation |
| GOVERNANCE_AREA | architecture; terminology |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when reviewing why source doctrine was retained, changed, or excluded. |
| HOW_TO_USE | Read as explanatory provenance. Accepted design choices are recorded separately in adr/. |
| DOCUMENT_CONTENT | Review of ADOS Glossary v1.3 and ADOS Profile v1.23 concepts used in v0.2. |


## ADOS Glossary v1.3

Adapted:

- concept-oriented glossary records;
- document metadata model;
- ontology and taxonomy method;
- competency questions;
- Prompt / Directive / Work / Claim / Requirement distinctions;
- Project / Package / Archetype / Domain concepts;
- optional minimal RDF/SHACL boundary.

Not transferred as governing source:

- PDD model document;
- execution-ledger runtime;
- one-file Atomic Work as a universal auditor requirement;
- package production workflow.

## ADOS Profile v1.23

Adapted:

- Pillars;
- Semantic Meaning Space;
- Goal-Attractor Geometry;
- Coordinate Dimension and Coordinate;
- Evaluation Metric doctrine;
- Archetype and Domain separation;
- Requirement applicability;
- Project as broader than App;
- package core-file content principles.

Adjusted:

- `App Requirement` generalized to `Project Requirement`.
- `APP-REQS.md` methodology represented as `PROJECT_REQUIREMENTS_MODEL.md`.
- pillar wording generalized where it assumed all Projects are apps.
- Metric scale adapted from 1–100 profile grading to optional 0–10 auditor scoring.
- strict validator and release-gate mechanics were not imported.

## v1.4 / v1.5 failure examples

Those releases are used only as Problem Pattern examples, including false PASS, schema coverage without strength, proof-fixture overgeneralization, semantic export drift, and baseline regression. They do not define v0.2 execution architecture.
