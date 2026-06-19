# Project Requirements Model

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | project_requirements_model |
| GOVERNANCE_AREA | requirements; project |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when adapting app-oriented ADOS source material or evaluating Project-specific obligations. |
| HOW_TO_USE | Use Project Requirement as the general concept. Introduce App Requirement only as an App-Archetype subtype. |
| DOCUMENT_CONTENT | General replacement for app-wide requirements terminology. |


## Generalization decision

Source ADOS Profile v1.23 owns Project-specific obligations in `project/APP-REQS.md`. That name is too narrow for a quality auditor supporting App, Research, Runtime, Profile, Prompt, and Other Archetypes.

v0.2 uses:

```text
Project Requirement
```

instead of:

```text
App Requirement
```

unless the obligation is inherently App-specific.

## Archetype-specific subtypes

- App Requirement
- Research Requirement
- Runtime Requirement
- Profile Requirement
- Prompt Requirement
- Other/Custom Project Requirement

These are optional subtypes, not separate top-level requirement systems.

## Translation examples

| Source wording | v0.2 interpretation |
|---|---|
| “Every app must define…” | Review applicability; generalize to Project only if true across supported Archetypes. |
| `APP-REQ-NNN` | Historical source ID; do not reuse as a v0.2 Project Requirement ID. |
| “App scaffolding” | Project scaffolding when the principle applies generally. |
| “App Delivery” | Project Delivery unless specifically application-like. |
