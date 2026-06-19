# ADOS Quality Drift Auditor v0.2 Manifest

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | manifest |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | agent_load_order |
| GOVERNANCE_AREA | project; glossary; navigation |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use before an agent evaluates a Project or modifies this package. |
| HOW_TO_USE | Load the authority surfaces in the specified order. Do not interpret this manifest as an execution-governance workflow. |
| DOCUMENT_CONTENT | Agent navigation, authority order, package roles, and evaluation entry instructions. |


## Authority load order

1. `PACKAGE.json` — machine identity, Goal, Objectives, entrypoints, and non-goals.
2. `GLOSSARY.md` — semantic authority and retrieval vocabulary.
3. `PDD.md` — Project definition and scope.
4. `adr/index.json` and accepted ADR Markdown records — architecture decisions.
5. `doc/` — explanatory doctrine.
6. `skills/PROJECT-EVOLUTION-QUALITY-AUDITOR.json` — evaluator behavior.
7. `profiles/archetype-bank.json` and `profiles/domain-bank.json`.
8. `metrics/metric-bank.json` and `metrics/report-policy.json`.
9. `problems/problem-bank.json`.
10. `schema/schema-index.json` and bound schemas.
11. User-supplied Project versions and evidence.

## Evaluation load pattern

```text
retrieve relevant glossary terms
→ identify Project, User Request, Intent, Goal, and Objectives
→ select Archetype and Domain
→ inspect available Build Package / Agent Work / Build Result inputs
→ evaluate quality coordinates
→ compare stages and versions
→ match Problem Patterns
→ identify consequence and risk
→ recommend Baseline Version and corrective prompt
```

This is an interpretation sequence, not a mandatory build workflow.

## File roles

| Surface | Role |
|---|---|
| `PACKAGE.json` | Machine package identity and entrypoints. |
| `README.md` | Human explanation and usage. |
| `MANIFEST.md` | Agent authority order and navigation. |
| `GLOSSARY.md` | Semantic/RAG authority. |
| `PDD.md` | Project definition for this auditor package. |
| `adr/` | Accepted architecture decisions. |
| `doc/` | Adapted ADOS doctrine and methodology. |
| `skills/` | Machine-readable evaluator skill. |
| `profiles/` | Archetype and Domain banks. |
| `metrics/` | Coordinates, Metrics, and report interpretation policy. |
| `problems/` | Reusable quality-drift problem patterns. |
| `schema/` | JSON structure guardrails. |
| `out/` | Report template and example output. |

## Content principles for core files

### `PACKAGE.json`

Contains machine identity, version, Goal, Objectives, semantic authority, entrypoints, methodology sources, clean-room status, and non-goals. It does not duplicate glossary definitions or report content.

### `MANIFEST.md`

Contains agent load order, authority map, file roles, and evaluation navigation. It does not prescribe how a builder must perform work.

### `README.md`

Explains the package to humans, states the product boundary, and provides a concise usage path. It is not the semantic authority.

### `GLOSSARY.md`

Owns approved concept definitions and prevents local redefinition by banks, schemas, docs, or reports.

## Non-governance rule

The auditor may assess PDDs, Requirements, Atomic Work, Evidence Ledgers, Execution Traces, and QA Evidence when those surfaces exist. It must not require them solely because they are defined in the glossary.
