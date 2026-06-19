# Execution Flow as an Evaluated ADOS Concept

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | execution_flow_interpretation |
| GOVERNANCE_AREA | execution; quality |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when an evaluated Project exposes an execution flow, Work Plan, Directives, trace, or state transitions. |
| HOW_TO_USE | Interpret the flow against GLOSSARY.md and the Project's own claimed model. Do not impose this document as the agent's required workflow. |
| DOCUMENT_CONTENT | Guidance for auditing execution-flow concepts without governing execution. |


## Reference ADOS flow

ADOS source models may use a chain such as:

```text
User Request
→ Intent
→ Requirement
→ Atomic Requirement
→ PDD
→ Work Plan
→ Atomic Work
   ├── Apply Directive
   └── Verify Directive
→ Evidence Ledger / Execution Trace
→ QA Evidence
→ Delivery
```

## v0.2 boundary

This chain is a reference concept model. The auditor may use it to:

- interpret source terms;
- locate build-package-to-agent or agent-to-result drift;
- distinguish instruction from Work and evidence;
- evaluate whether a Project's own claimed flow is coherent.

The auditor must not mark a Project defective merely because it uses another valid flow.

## Questions

- Which flow does the Project claim?
- Which stages are actually evidenced?
- Was a missing stage inferred?
- Did Apply/Verify checks assess the intended target?
- Does the Execution Trace agree with the Build Result?
- Did process compliance displace Goal alignment?
