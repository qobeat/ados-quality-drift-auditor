# Archetype Model

The evaluator selects one primary archetype because the same evidence has different decision value for different projects.

## Selection order

1. Determine the project’s purpose.
2. Identify the principal delivered artifact.
3. Identify the highest-impact failure modes.
4. Compare mandatory evidence across profiles.
5. Select the profile that best explains the release decision.
6. Use the general profile only when no specialized profile reaches 0.60 confidence.

## Why one primary archetype

Multiple unconstrained profiles allow metric shopping. One primary profile fixes the scoring frame. Secondary characteristics may be recorded as modifiers and may add checks, but they do not replace the primary weights.

## Profile bank

The v0.1 bank includes:

- general engineered artifact;
- schema-governed knowledge package;
- profile plus runtime bootstrap package;
- software application or service;
- software library, CLI, or SDK;
- data pipeline or dataset;
- ML, LLM, or agent system;
- policy or control pack;
- documentation or specification;
- infrastructure or platform.

The bank is extensible through new profile JSON files validated by `schema/archetype-profile.schema.json`.
