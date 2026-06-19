# ADOS Quality Drift Auditor Glossary

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | glossary |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | controlled_vocabulary |
| GOVERNANCE_AREA | terminology |
| CONSUMERS | evaluator; architect; reviewer; builder |
| WHEN_TO_USE | Load before interpreting metrics, problem patterns, reports, or verdicts. |
| HOW_TO_USE | Use the preferred terms and boundaries below; do not broaden them silently. |
| DOCUMENT_CONTENT | Minimal project dictionary for cross-version quality and drift evaluation. |

## Terms

### Archetype

A predefined category describing the primary purpose, artifact form, evidence needs, failure modes, and metric emphasis of a project.

**Must not mean:** a keyword label chosen without evidence.

### Archetype Profile

The machine-readable evaluation configuration for one Archetype, including selection signals, stage weights, mandatory evidence, risks, and applicable problems.

### Build Package

The prompt and supplied authority used to control a build, including requirements, baseline materials, ADRs, schemas, fixtures, and acceptance rules.

### Building Agent Work

Available evidence of the builder’s execution: response, reasoning or activity log, work plan, commands, diffs, tests, evidence, corrections, and verdict.

### Build Result

The produced version or release candidate whose observable quality is evaluated.

### Source Set

The normalized collection of versioned Build Package, Building Agent Work, and Build Result artifacts for one project.

### Baseline Version

The strongest verified starting version for the intended next change. It is selected by quality evidence, not recency.

### Donor Component

An individually verified component taken from a version that is not the primary Baseline Version.

### Atomic Claim

One independently testable proposition extracted from a source and assigned a stable Claim ID.

### Claim Ledger

The persistent set of Atomic Claims, dependencies, weights, scores, statuses, and evidence references.

### Evidence Ledger

The persistent index of observations and their provenance. It is separate from evaluator scores and verdicts.

### Observation

A fact directly visible in supplied material or reproduced from a declared procedure.

### Derived Fact

A deterministic calculation from one or more Observations.

### Inference

A reasoned proposition supported by evidence but not directly observed.

### Evaluator Judgment

A rubric-based assessment, such as a score or risk level, that must state its evidence basis.

### Unconfirmed Claim

A needed proposition not established by the supplied evidence. Its required report phrase is `I cannot confirm this.`

### Evidence Coverage

The proportion of applicable required evidence items that are present and verified.

### Quality Metric

A defined, scored property of a Build Package, Building Agent Work, or Build Result.

### Common Axis

One of the fixed nine cross-source evaluation dimensions used to compare heterogeneous artifacts.

### Hard Gate

A mandatory condition whose failure forces FAIL or INSUFFICIENT_EVIDENCE regardless of average score.

### Quality Drift

A quality-relevant change across versions or between control, execution, and result. Drift may improve, degrade, mix, remain unchanged, or remain unconfirmed.

### Drift Consequence

An observed or strongly inferred effect of drift on correctness, maintainability, trust, safety, or future work.

### Drift Risk

A credible future consequence when a detected drift mechanism remains unresolved.

### False-PASS

A PASS verdict not supported by the claims, evidence, gates, or defect sensitivity required for that verdict.

### Oracle

The rule that determines whether a check passed for the intended reason.

### Mutation Test

A controlled, usually single-fault change used to verify that a validator detects a specified defect with the expected finding.

### Proof Fixture

A bounded example artifact used to exercise explicitly mapped claims. Fixture PASS is not package PASS.

### Independent Audit

A check implemented through a materially separate logic path from the builder and package-owned validator.

### Release Verdict

A derived outcome: PASS, CONDITIONAL_PASS, FAIL, INSUFFICIENT_EVIDENCE, or NOT_EVALUATED.
