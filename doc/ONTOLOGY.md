# Ontology Model for Quality Drift Auditing

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | ontology_model |
| GOVERNANCE_AREA | glossary; project |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when interpreting relationships among glossary concepts. |
| HOW_TO_USE | Read after GLOSSARY.md. Use this model for retrieval and report organization; do not redefine terms locally. |
| DOCUMENT_CONTENT | Concept relationship model for the auditor. |


## Core ontology

```text
Project
├── User Request
│   └── Intent
│       ├── Goal
│       │   ├── Objectives
│       │   └── Goal-Attractor Geometry
│       ├── Archetype
│       └── Domain
├── ADOS Profile expectations
├── Flow
├── Skills
└── Package versions
    ├── Build Package
    ├── Building Agent Work
    └── Build Result
```

```text
Quality Drift
├── affected Goal / Objective / Profile / Coordinate
├── source transition
├── direction
├── Drift Consequence
├── Drift Risk
├── Problem Pattern
└── Corrective Prompt
```

## Instruction and work ontology

```text
Prompt
└── Directive
    ├── Apply Directive
    └── Verify Directive

Requirement
└── Project Requirement
    └── Atomic Requirement

Work
└── Atomic Work
```

These relations describe ADOS concepts that may appear in evaluated material. They are not mandatory process requirements for the auditor.

## Document ontology

```text
Package
├── PACKAGE.json — machine identity
├── README.md — human entrypoint
├── MANIFEST.md — agent navigation
├── GLOSSARY.md — semantic authority
├── PDD.md — Project definition
├── adr/ — accepted decisions
├── doc/ — doctrine
├── banks — profiles, metrics, policy, problems
├── schema/ — structural guardrails
└── out/ — evaluation reports
```

## Key cardinalities

- One evaluated Intent has one primary Archetype and one primary Domain.
- One comparison has one primary Baseline Version.
- One Coordinate Dimension has one stable meaning inside an active geometry.
- One ADR records one primary architecture decision.
- One Package has one primary semantic authority for a declared scope.
