# Project Definition — ADOS Quality Drift Auditor v0.2

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | pdd |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | project_definition |
| GOVERNANCE_AREA | project; quality; glossary |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when interpreting the accepted scope and architecture of v0.2. |
| HOW_TO_USE | Read with PACKAGE.json, GLOSSARY.md, and accepted ADRs. Treat this as the definition of this package, not as a required PDD model for Projects being evaluated. |
| DOCUMENT_CONTENT | Goal, Objectives, scope, architecture boundaries, and acceptance conditions for v0.2. |


## GOAL

Provide a glossary-centered, ADOS-specific quality-drift auditor that guides an agent to evaluate how a Project evolves from User Request, Intent, Goal, Objectives, Archetype, Domain, and ADOS Profile through Build Package, Building Agent Work, and Build Result, without imposing an execution-governance process.

## OBJECTIVES

1. **OBJ-01:** Make GLOSSARY.md the primary semantic and retrieval authority for every evaluation.
2. **OBJ-02:** Define the core ADOS project, package, work, geometry, artifact, archetype, domain, evidence, and drift concepts needed by the auditor.
3. **OBJ-03:** Evaluate build-package, building-agent-work, and build-result inputs for one or many versions of the same Project.
4. **OBJ-04:** Select one project Archetype and one Domain from governed banks and use them to focus evaluation questions, metrics, and drift risks.
5. **OBJ-05:** Represent project quality through Goal-Attractor Geometry coordinates and Metrics used as interpretive guardrails rather than execution gates.
6. **OBJ-06:** Identify quality drift, drift consequence, drift risk, and reusable problem patterns across stages and versions.
7. **OBJ-07:** Produce structured JSON reports that cite the glossary concepts used and distinguish confirmed, partial, contradicted, and unconfirmed conclusions.
8. **OBJ-08:** Generate focused corrective prompt text while preserving the governing User Request, Intent, Goal, and Objectives.
9. **OBJ-09:** Remain non-invasive: do not require the evaluated Project or evaluating agent to use ADOS ledgers, Atomic Work, package validators, or a prescribed workflow.
10. **OBJ-10:** Adapt relevant ADOS Glossary v1.3 and ADOS Profile v1.23 doctrine while generalizing app-specific concepts to project-level concepts.

## Scope

### In scope

- ADOS-specific concept definitions.
- RAG-style retrieval of glossary concepts.
- Archetype and Domain classification.
- Goal-Attractor Geometry coordinates and Metrics.
- Build Package, Building Agent Work, Build Result, and cross-version evaluation.
- Quality Drift, consequence, risk, Problem Pattern, Baseline Version, and corrective prompt analysis.
- JSON schemas for evaluator inputs, banks, skill, and reports.
- Adapted doctrine from ADOS Glossary v1.3 and ADOS Profile v1.23.

### Out of scope

- Enforcing the evaluated Project's execution method.
- Requiring ADOS Work Plans, ledgers, or one-file Atomic Work.
- Building or packaging the evaluated Project.
- Acting as an independent release validator.
- Treating source terminology as authoritative without applicability review.

## Architecture contracts

1. `GLOSSARY.md` is the semantic authority.
2. `doc/` explains doctrine; `adr/` records adopted decisions.
3. Banks and schemas reference glossary term IDs rather than redefining concepts.
4. One primary Archetype and one primary Domain are selected for an evaluation.
5. Metrics are Goal-Attractor Geometry guardrails, not process gates.
6. Evidence status and confidence remain distinct from numeric scores.
7. Final assessment uses `improvement`, `mixed`, `degradation`, `unchanged`, or `insufficient_evidence`, not package release PASS/FAIL.
8. Missing evidence is reported explicitly; it is not converted into an assumed score.
9. `app-requirements` is generalized to `Project Requirement` except inside historically quoted source notes.
10. Real v1.4/v1.5 examples belong in the Problem Bank and must not dictate this package's runtime architecture.

## Acceptance for v0.2

- Required files exist.
- Every active JSON file validates against its declared schema.
- All schema documents meta-validate under JSON Schema Draft 2020-12.
- Glossary term IDs referenced by banks and examples exist.
- Archetype and Domain IDs are unique.
- Metric coordinate and term references resolve.
- Problem Pattern references resolve.
- The report template and example report validate.
- No mandatory execution ledger, claim ledger, evidence ledger, validator, or build workflow is introduced.
- One ADR contains the complete prompt for a future production-grade v1.0 build.
