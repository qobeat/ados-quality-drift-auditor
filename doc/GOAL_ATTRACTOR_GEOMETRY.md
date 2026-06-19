# Goal-Attractor Geometry for Quality Drift

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | candidate |
| UPDATED_AT | 2026-06-19 |
| DOCUMENT_ROLE | geometry_model |
| GOVERNANCE_AREA | goal; quality |
| CONSUMERS | owner; architect; evaluator; agent; reviewer |
| WHEN_TO_USE | Use when defining quality coordinates or comparing Project states across stages or versions. |
| HOW_TO_USE | Use the geometry as an operational semantic model. Do not claim literal physical or mathematical attractor dynamics unless formally specified. |
| DOCUMENT_CONTENT | Adapted Goal-Attractor Geometry model for project-evolution auditing. |


## Geometry objects

- **Semantic Meaning Space:** interpretation space selected by Goal, Archetype, Domain, and ADOS Profile.
- **Goal Figure:** desired end-state structure.
- **Goal Surface:** boundary distinguishing sufficient from adjacent or inadequate states.
- **Goal Attractor:** directional governance pull toward the Goal Figure.
- **Attractor Basin:** legitimate variation region preserving Goal identity.
- **Coordinate Dimension:** one separable quality or meaning dimension.
- **Coordinate:** current or target value on a dimension.
- **Metric:** procedure for assessing a coordinate.
- **Quality Drift:** movement away from governing meaning or an unintended movement of the Goal Surface.

## Auditor geometry

```text
current version coordinates
      ↓ compare
baseline coordinates ── Goal Figure / Goal Surface
      ↑
Build Package → Agent Work → Build Result
```

The auditor records improvement, degradation, mixed movement, unchanged state, or insufficient evidence per coordinate.

## Coordinate priorities

Coordinates should derive from the Project Goal and Objectives, then be adjusted by Archetype, Domain, Profile expectations, and Problem Patterns.

## No false scalar reduction

A single total score may summarize an evaluation but cannot replace coordinate-level explanation. A version can improve in structural completeness while degrading in semantic integrity.
