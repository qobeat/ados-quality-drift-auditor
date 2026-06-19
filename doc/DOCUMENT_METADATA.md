# ADOS Document Metadata for v0.2

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | normative |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | document_metadata_model |
| GOVERNANCE_AREA | document |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when writing or interpreting Markdown documents in this package. |
| HOW_TO_USE | Apply the required fields near the top of each governed Markdown document. Do not use metadata fields to redefine the document's semantic content. |
| DOCUMENT_CONTENT | Adapted ADOS document metadata model for v0.2. |


## Required fields

| Field | Meaning |
|---|---|
| `DOCUMENT_TYPE` | Authority or artifact class, such as glossary, guide, manifest, PDD, ADR, or change log. |
| `DOCUMENT_STATUS` | Lifecycle state: draft, candidate, final, superseded, or historical. |
| `UPDATED_AT` | Latest approved content date in `YYYY-MM-DD`. |
| `DOCUMENT_ROLE` | Operational role of the document in this Package. |
| `GOVERNANCE_AREA` | Main ownership area; metadata only, not a Goal-Attractor Coordinate. |
| `CONSUMERS` | Roles expected to use the document. |
| `WHEN_TO_USE` | Trigger for loading the document. |
| `HOW_TO_USE` | Required interpretation or operation. |
| `DOCUMENT_CONTENT` | Concise content description. |

## Content principle

Metadata helps agents retrieve the right document. It does not prove that the document is correct, current, or applicable to an evaluated Project.

## v1.23 field adaptation

ADOS Profile v1.23 uses `FILE_TYPE`, `FILE_STATUS`, `AUDIENCE`, and `FILE_CONTENT`. v0.2 normalizes those concepts to the v1.3-style `DOCUMENT_*` model because it more clearly distinguishes document identity from package files.
