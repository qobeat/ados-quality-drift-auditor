# Semantic Audit Flow

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | audit_flow_model |
| GOVERNANCE_AREA | quality; project |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when an evaluator needs the recommended interpretation sequence. |
| HOW_TO_USE | Follow the semantic sequence while leaving implementation details to the agent. This is not a mandatory build workflow. |
| DOCUMENT_CONTENT | Glossary-first evaluation flow for project evolution. |


```text
normalize Project and versions
→ retrieve User Request / Intent / Goal / Objective concepts
→ select Archetype and Domain
→ retrieve applicable Pillars, Coordinates, Metrics, and Problem Patterns
→ evaluate available Build Package
→ evaluate available Building Agent Work
→ evaluate available Build Result
→ compare stages and versions
→ identify Quality Drift, consequence, and risk
→ recommend Baseline Version
→ formulate Corrective Prompt
→ write schema-conformant report
```

## Missing stages

A missing Build Package, agent trace, or Build Result remains missing. The evaluator may compare available surfaces but must not invent the absent stage.

## Difference from ADOS execution workflow

The ADOS execution chain can include Requirement, Atomic Requirement, PDD, Work Plan, Atomic Work, Apply Directive, Verify Directive, Evidence Ledger, and QA. v0.2 may inspect those surfaces but does not require or orchestrate them.

## File-level versus Project-level interpretation

A file-level check can support one bounded claim. Project-level quality requires interpretation against the User Request, Intent, Goal, Objectives, Archetype, Domain, Profile, and material Delivery.
