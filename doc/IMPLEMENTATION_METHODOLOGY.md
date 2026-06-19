# Evaluation Implementation Methodology

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | implementation_methodology |
| GOVERNANCE_AREA | quality; skill |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when implementing or running the evaluator skill. |
| HOW_TO_USE | Follow the semantic sequence while choosing implementation details appropriate to the host agent. This document does not mandate ledgers or a packaging process. |
| DOCUMENT_CONTENT | Recommended methodology for applying the v0.2 concept model. |


## Method

1. Normalize the Project and version set.
2. Record available input types for each version.
3. Retrieve glossary concepts for User Request, Intent, Goal, Objectives, Project, Package, and relevant ADOS concepts.
4. Select one primary Archetype and one primary Domain with confidence and rationale.
5. Retrieve applicable Pillars, Coordinates, Metrics, and Problem Patterns.
6. Evaluate the Build Package if supplied.
7. Evaluate Building Agent Work if supplied.
8. Evaluate the Build Result if supplied.
9. Compare stages and versions coordinate by coordinate.
10. Identify where drift entered and separate observed consequence from future risk.
11. Select the strongest Baseline Version for the next improvement Goal.
12. Produce a focused Corrective Prompt.
13. Write a JSON report conforming to the report schema.

## Implementation discretion

The host agent decides how to search files, summarize text, run safe inspections, or store temporary notes. v0.2 does not prescribe an internal ledger or work scheduler.

## Quality protection

- Retrieve before judging.
- Define before scoring.
- Compare meanings, not only filenames or counts.
- Treat missing evidence as uncertainty.
- State when a conclusion cannot be confirmed.
- Keep corrective action focused on the observed mechanism.
