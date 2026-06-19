# Taxonomy for v0.2

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | taxonomy_model |
| GOVERNANCE_AREA | glossary; classification |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when classifying Projects, Domains, inputs, drift, evidence status, or Problem Patterns. |
| HOW_TO_USE | Apply the controlled categories below and defer term meanings to GLOSSARY.md. |
| DOCUMENT_CONTENT | Classification hierarchy for quality-drift evaluation. |


## Project Archetypes

```text
Archetype
├── App Archetype
├── Research Archetype
├── Runtime Archetype
├── Profile Archetype
├── Prompt Archetype
└── Other Archetype
```

## Domains

```text
Domain
├── Business Domain
├── Business-Trading Domain
├── Science Domain
├── Education Domain
├── Software-Engineering Domain
├── Governance Domain
└── Other Domain
```

## Evaluation inputs

```text
Project Version Input
├── Build Package
├── Building Agent Work
└── Build Result
```

## Drift dimensions

```text
Quality Drift
├── intent drift
├── goal drift
├── objective drift
├── scope drift
├── archetype drift
├── domain drift
├── ADOS profile drift
├── semantic drift
├── contract/schema drift
├── evidence drift
├── validator/QA drift
├── identity/packaging drift
└── corrective-action drift
```

## Evidence status

- `confirmed`
- `partial`
- `contradicted`
- `unconfirmed`

## Evolution assessment

- `improvement`
- `mixed`
- `degradation`
- `unchanged`
- `insufficient_evidence`
