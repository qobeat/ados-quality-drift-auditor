# Coordinate Model

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | normative |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | coordinate_model |
| GOVERNANCE_AREA | goal; metrics |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when defining or interpreting Goal-Attractor Coordinates. |
| HOW_TO_USE | A Coordinate Dimension must have stable meaning, scale, polarity, target condition, evidence expectations, and glossary references. |
| DOCUMENT_CONTENT | Coordinate Dimension and Coordinate doctrine for the auditor. |


## Coordinate Dimension fields

Each coordinate in `metrics/metric-bank.json` defines:

- stable `coordinate_id`;
- name and definition;
- referenced glossary terms;
- applicable evaluation surfaces;
- scale;
- polarity;
- target condition;
- evidence guidance;
- default Metric IDs.

## v0.2 coordinates

1. User Request and Intent alignment
2. Goal alignment
3. Objective coverage
4. Archetype fit
5. Domain fit
6. ADOS Profile alignment
7. Build Package quality
8. Building Agent Work fidelity
9. Build Result quality
10. Semantic integrity
11. Evidence sufficiency
12. Drift control
13. Corrective focus

## Coordinate value rule

Score and confidence are separate:

```text
score = evaluator judgment on the defined scale
confidence = strength of available support
evidence_status = confirmed / partial / contradicted / unconfirmed
```

An unconfirmed coordinate may have no numeric score. Missing evidence must not be replaced with a midpoint.
