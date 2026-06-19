# ADOS Quality Drift Auditor v0.2

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | human_entrypoint |
| GOVERNANCE_AREA | project; glossary; quality |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use first when a human needs to understand the package and its intended use. |
| HOW_TO_USE | Read this overview, then load MANIFEST.md and GLOSSARY.md before using the machine skill. |
| DOCUMENT_CONTENT | Human-readable description and usage guide for the glossary-centered quality-drift auditor. |


## Purpose

`ados-quality-drift-auditor` evaluates how the quality and meaning of a Project change across versions and across three input surfaces:

1. **Build Package** — prompts and supplied materials that shape a build.
2. **Building Agent Work** — the visible work, decisions, checks, and claims made by the building agent.
3. **Build Result** — the produced Package or version.

The auditor compares those surfaces against the Project's User Request, Intent, Goal, Objectives, Archetype, Domain, ADOS Profile expectations, and selected Baseline Version.

## Product boundary

This package is an **evaluation skill and semantic model**. It does not tell a builder how to schedule work, maintain ledgers, package files, or execute Apply/Verify directives.

ADOS execution concepts are defined in `GLOSSARY.md` because they may appear in Projects being audited. Their presence in the glossary does not make them mandatory for the auditor or for evaluated Projects.

## Semantic architecture

```text
User Request
→ Intent
→ Goal and Objectives
→ Project
   ├── Archetype
   ├── Domain
   ├── ADOS Profile expectations
   ├── Flow
   ├── Skill
   └── Package versions
        ├── Build Package
        ├── Building Agent Work
        └── Build Result
→ Quality Drift
   ├── Drift Consequence
   ├── Drift Risk
   ├── Problem Pattern
   └── Corrective Prompt
```

## How to use

1. Read `MANIFEST.md`.
2. Load `GLOSSARY.md` as the semantic/RAG authority.
3. Load the machine skill.
4. Select one Archetype and one Domain.
5. Retrieve the glossary terms relevant to the current evaluation.
6. Apply relevant coordinates, Metrics, and Problem Patterns.
7. Compare stages and versions.
8. Write a JSON report conforming to `schema/evaluation-report.schema.json`.

## Expected outputs

The report should answer:

- What was the original User Request and normalized Intent?
- What Goal and Objectives govern the Project?
- Which Archetype and Domain apply?
- What did the Build Package ask for?
- What did the building agent actually do?
- What did the Build Result deliver?
- Which quality coordinates improved, degraded, remained unchanged, or could not be confirmed?
- Where did drift enter?
- What consequence and risk followed?
- Which version is the strongest Baseline Version?
- What focused corrective prompt should guide the next version?

## Package authority

- `GLOSSARY.md` — concept meaning.
- `PDD.md` — v0.2 Project definition.
- `adr/` — architectural decisions.
- `doc/` — explanatory doctrine.
- JSON banks — archetypes, domains, metrics, report policy, and problem patterns.
- JSON schemas — structural guardrails for active JSON files.

## Important interpretation

A high score is not a release verdict.  
A missing artifact is not automatically a defect.  
An Evidence Ledger or Execution Trace is evaluated when present but is not required from every Project.  
A sample such as `simple-calculator.zip` proves only the behavior directly exercised by its test surface.
