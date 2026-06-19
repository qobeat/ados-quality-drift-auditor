# Requirements Doctrine

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | requirements_doctrine |
| GOVERNANCE_AREA | requirements; project |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when evaluated material contains Requirements or when deriving audit questions from Goal and Objectives. |
| HOW_TO_USE | Interpret Requirements through applicability, traceability, and semantic preservation. Do not require every Project to use ADOS requirement files. |
| DOCUMENT_CONTENT | Generalized ADOS Requirements doctrine for all supported Archetypes. |


## Relationship

```text
User Request
→ Intent
→ Goal
→ Objectives
→ Requirement
   └── Project Requirement
       └── Atomic Requirement
```

## Applicability

Requirements must be interpreted under:

- Project;
- Archetype;
- Domain;
- Goal and Objectives;
- ADOS Profile;
- version and scope.

A copied Requirement is not automatically applicable.

## Project Requirement

`Project Requirement` is the general owner-specific term. `App Requirement` is valid only when a Requirement is specifically owned by an App-Archetype Project.

## Audit questions

- Is the Requirement traceable to the User Request, Goal, Objective, Profile, law, contract, or other authority?
- Is it applicable to this Archetype and Domain?
- Was normative force weakened or strengthened?
- Did the agent satisfy only a convenient fragment?
- Did evidence actually assess the Requirement?
