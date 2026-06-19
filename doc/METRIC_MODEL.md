# Metric Model

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | normative |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | metric_model |
| GOVERNANCE_AREA | metrics; quality |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when scoring coordinates or defining metric records. |
| HOW_TO_USE | Apply Metrics as interpretive guardrails. Always report confidence, evidence status, and rationale separately from score. |
| DOCUMENT_CONTENT | Metric derivation and use model for v0.2. |


## Metric derivation

A Metric should derive from:

```text
Goal or Objective
+ Coordinate Dimension
+ Archetype emphasis
+ Domain interpretation
+ evidence expectations
= Evaluation Metric
```

## Required properties

A Metric record defines:

- `metric_id`;
- name;
- referenced Coordinate;
- glossary terms;
- applicable input surfaces;
- question or procedure;
- score anchors;
- evidence guidance;
- guardrails;
- Archetype emphasis.

## Score scale

v0.2 uses `0..10` when a numeric score is useful:

- 9–10: strong and well-supported
- 7–8: good with bounded limitations
- 5–6: mixed or incomplete
- 3–4: weak or materially drifting
- 0–2: broken or contradicted
- null: not scored because evidence is insufficient or the metric is inapplicable

## Guardrails

- Counts do not establish semantic quality.
- Test PASS proves only the tested property.
- Confidence is not derived from score.
- A total score does not erase coordinate-level degradation.
- Metrics guide diagnosis; they do not impose an execution process or release verdict.
