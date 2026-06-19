# Project Definition — ADOS Quality Drift Auditor v0.1

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | pdd |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | primary_project_definition |
| GOVERNANCE_AREA | planning; architecture; quality |
| CONSUMERS | owner; architect; evaluator; maintainer |
| WHEN_TO_USE | Use to determine project scope and acceptance boundaries. |
| HOW_TO_USE | Treat GOAL and OBJECTIVES as controlling intent; ADRs govern architecture. |
| DOCUMENT_CONTENT | Definition of the v0.1 quality-drift evaluation project. |

## GOAL

Provide a deterministic, evidence-traceable, archetype-aware skill for evaluating build controls, building-agent execution, and produced project versions across time, so quality drift, false-PASS risk, regression, and the best improvement baseline can be identified.

## OBJECTIVES

1. **OBJ-01:** Accept build-package, building-agent-work, and build-result inputs for one or many versions of the same project.
2. **OBJ-02:** Normalize every supplied artifact, extract stable atomic claims, and preserve claim identifiers through scoring and verdict.
3. **OBJ-03:** Select one primary project archetype from a governed archetype bank and apply its evidence requirements, metrics, hard gates, and drift risks.
4. **OBJ-04:** Score each input stage using stage-specific metrics and a common nine-axis comparison frame.
5. **OBJ-05:** Trace changes from baseline result to target build package, agent work, built result, and later versions.
6. **OBJ-06:** Separate observed evidence, derived calculations, inference, and evaluator judgment in every report.
7. **OBJ-07:** Detect known quality-failure patterns using a machine-readable problem bank with risks, visible effects, corrections, and prevention controls.
8. **OBJ-08:** Prevent false release acceptance through evidence coverage thresholds, hard gates, mutation-sensitive validation, replay checks, and verdict derivation rules.
9. **OBJ-09:** Emit JSON claim ledgers and evaluation reports conforming to JSON Schema Draft 2020-12 in the out/ folder.
10. **OBJ-10:** Remain usable when evidence is incomplete by returning explicit unknowns and INSUFFICIENT_EVIDENCE rather than inventing support.

## Primary components

| Component | Responsibility |
|---|---|
| Skill | Deterministic evaluation procedure and output contract |
| Archetype bank | Project-type identification and profile selection |
| Metric bank | Common and stage-specific quality dimensions |
| Problem bank | Reusable quality-failure patterns and corrections |
| Schemas | Closed machine contracts for inputs, ledgers, profiles, and reports |
| Tools | Package validation, mutation self-test, and report initialization |
| Examples | Concrete v1.4/v1.5 false-PASS and drift illustrations |
| Outputs | Schema-conformant JSON reports |

## In scope

- One or many versions of the same project.
- Partial or complete evidence for all three input stages.
- Baseline selection, regression analysis, process-to-result traceability, and drift-risk analysis.
- General engineered artifacts plus predefined specialized archetypes.

## Out of scope for v0.1

- Automatic truth verification against the public internet.
- Domain-specific execution of arbitrary proprietary build systems.
- Replacing expert judgment with keyword counts.
- Treating self-reported PASS or fixture success as conclusive evidence.

## Acceptance for v0.1

1. All required package files and folders exist.
2. Every JSON file parses.
3. Every schema meta-validates as JSON Schema Draft 2020-12.
4. All declared schema bindings validate.
5. Metric weights and profile weights sum to 100 per applicable frame.
6. Archetype and problem references resolve.
7. Example claim ledger and report validate.
8. Manifest inventory and hashes match a fresh extraction.
9. Mutation self-tests detect representative false-PASS defects.
10. `adr/adr-005.md` contains a complete v1.0 production build prompt.
