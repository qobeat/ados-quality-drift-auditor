# Project Evolution Quality and Drift Auditor

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | skill |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | primary_execution_skill |
| GOVERNANCE_AREA | evaluation; quality; project_evolution |
| CONSUMERS | evaluator; architect; reviewer; self_test |
| WHEN_TO_USE | Use when one or more versions of a project have build controls, agent execution records, or delivered artifacts to evaluate. |
| HOW_TO_USE | Load the authority files in the stated order, execute STEP-00 through STEP-12, and emit schema-conformant JSON reports. |
| DOCUMENT_CONTENT | General-purpose method for claim-ledger evaluation and project-evolution drift analysis. |

## GOAL

Provide a deterministic, evidence-traceable, archetype-aware skill for evaluating build controls, building-agent execution, and produced project versions across time, so quality drift, false-PASS risk, regression, and the best improvement baseline can be identified.

## Inputs

The skill accepts one or many versions of the same project. Each version may supply zero or more artifacts of these types:

1. **`build_package`** — prompt, PDD, requirements, ADRs, baseline, control pack, fixtures, acceptance rules.
2. **`agent_work`** — final response, thinking or activity log, commands, diffs, work plan, evidence, QA records, correction history.
3. **`build_result`** — ZIP, repository snapshot, generated package, binary, dataset, configuration, or other delivered version.

A missing input type is recorded as missing. It is not reconstructed from later claims.

## Authority load order

1. `PACKAGE.json`
2. `MANIFEST.md`
3. `GLOSSARY.md`
4. `PDD.md`
5. `adr/index.json` and applicable ADRs
6. `profiles/archetype-bank.json` and the selected profile
7. `metrics/metric-bank.json`
8. `metrics/report-policy.json`
9. `problems/problem-bank.json`
10. `schema/schema-index.json`

## Core evaluation rules

- Evaluate only the supplied sources.
- Do not reward polish when the underlying idea, contract, execution, or evidence is weak.
- Keep observed evidence, derived calculations, inference, evaluator judgment, and unconfirmed propositions separate.
- For a decisive unsupported point, write exactly: **`I cannot confirm this.`**
- Preserve stable IDs from extraction through verdict.
- Do not score before claims are extracted and weighted.
- A count is evidence only for the counted property. File count does not prove completeness; schema coverage does not prove schema strength; test count does not prove correct oracles.
- A fixture proves only the claims its oracle directly exercises.
- The same builder may provide useful validation, but builder-owned validation is not independent evidence.
- The newest version is not automatically the best baseline.

---

## STEP-00 — Normalize the source set

For every artifact assign:

- `source_id`
- `version_id`
- `input_type`
- source name and type
- apparent scope
- primary purpose
- assumed target user
- evidence basis
- availability: available, partial, missing, or reference-only

Create an explicit version lineage. Use the supplied chronology, not filename sorting alone.

### Required checks

- No source is silently merged with another source.
- A ZIP and its agent summary are separate sources.
- Historical evidence is not treated as current evidence.
- External proof artifacts remain distinct from the package they purport to prove.

---

## STEP-01 — Determine domain and archetype

Select exactly one primary archetype from `profiles/archetype-bank.json`.

Use:

1. the project’s primary purpose;
2. the delivered artifact type;
3. the release decision being evaluated;
4. the profile whose mandatory evidence and failure modes best fit the project.

Do not select an archetype only because a keyword appears. Record alternatives and why they were not selected. If no specialized profile reaches 0.60 confidence, select `ARCH-GENERAL-ENGINEERED-ARTIFACT`.

A project may have modifiers, such as “schema-governed knowledge package with runtime bootstrap behavior,” but one profile remains primary. For such a project, prefer `ARCH-MULTI-ARTIFACT-PROFILE-RUNTIME` when the runtime claim is decisive; otherwise prefer `ARCH-SCHEMA-GOVERNED-KNOWLEDGE`.

---

## STEP-02 — Inventory evidence

Create an evidence ledger before scoring.

### Evidence classes

| Class | Meaning |
|---|---|
| `observed` | Directly visible in a supplied file, command output, archive, diff, or test record |
| `derived` | Deterministic calculation from observed evidence |
| `inference` | Reasoned conclusion supported by observations but not directly stated |
| `judgment` | Evaluator assessment under the declared rubric |
| `unconfirmed` | Needed proposition that supplied evidence does not establish |

For each evidence record capture a locator, observation, verifier, timestamp, independence class, integrity hash when available, and supported claim IDs.

### Evidence independence

Rank evidence by logic independence:

1. builder-owned;
2. same-logic cross-check;
3. independently implemented logic;
4. external attestation.

Higher independence does not replace relevance. An independent test with the wrong oracle remains weak evidence.

Calculate evidence coverage as:

```text
verified applicable required evidence items
───────────────────────────────────────────
all applicable required evidence items
```

Do not count non-applicable evidence in the denominator.

---

## STEP-03 — Extract atomic claims

One claim is one independently testable proposition.

For each source, preserve:

- `claim_id`
- exact quote
- normalized claim
- claim type: goal, scope, rule, method, scoring, output, constraint, or verdict logic
- dependencies
- evidence references
- evaluator note

Split compound obligations. Do not paraphrase away cardinality, ordering, scope, or verdict conditions.

Stable claim IDs must remain unchanged in later tables and comparisons.

---

## STEP-04 — Weight and score claims

For every claim score these dimensions from 0 to 5:

- goal impact
- decision leverage
- dependency centrality
- scope breadth
- verification burden

```text
raw_claim_weight = sum(five dimensions)
normalized_claim_weight =
  100 × raw_claim_weight / sum(raw weights for that source)
```

Round normalized weights to one decimal place and adjust the last nonzero record only when needed so each source totals exactly 100.0.

Score each claim from 0 to 10:

| Score | Meaning |
|---:|---|
| 10 | Explicit, precise, central, supported, and operational |
| 8 | Explicit and useful with minor ambiguity |
| 6 | Partly specified or weakly operationalized |
| 4 | Vague, underspecified, or weakly connected |
| 2 | Materially flawed, contradicted, or self-undermining |
| 0 | Absent, unusable, or directly broken |

Assign `strong`, `acceptable`, `weak`, or `broken`. Use `not_scored` when evidence is insufficient.

```text
weighted_claim_score =
  normalized_claim_weight × claim_score / 10
```

---

## STEP-05 — Evaluate the build package

Use the selected archetype’s weights for `BP-001` through `BP-009`.

Evaluate:

- goal and objective precision;
- baseline and change-set control;
- scope and file obligations;
- architecture and archetype fit;
- verification design;
- evidence contract;
- drift safeguards;
- oracle independence and defect sensitivity;
- deliverable and acceptance clarity.

### Build-package drift risks

Check whether the control pack:

- authorizes schema weakening to achieve coverage;
- leaves essential implementation or proof selection to the builder after planning;
- uses a score as an acceptance gate;
- defines only positive-path fixtures;
- lacks a baseline regression floor;
- allows PASS with unresolved or assertion-only evidence.

A strong build package can still be executed badly. Score the control pack separately from agent work and result.

---

## STEP-06 — Evaluate building-agent work

Use `AW-001` through `AW-009`.

Evaluate what the agent did, not only what it reported.

Required distinctions:

- read authority vs claimed understanding;
- planned work vs actual modifications;
- command execution vs summary;
- observation-bearing evidence vs PASS assertions;
- proof created by the final artifact vs proof created by hidden builder logic;
- failed test detection vs detection of the intended defect;
- correction loop vs rewriting the record to show success.

A thinking or activity log is evidence of sequence and intent. It is not automatically evidence that produced files satisfy their contracts.

---

## STEP-07 — Evaluate the build result

Use `BR-001` through `BR-010`.

Apply metrics appropriate to the selected archetype. For a schema-governed knowledge package, contract and semantic integrity receive more weight. For a runtime or software artifact, functionality, replay, and resilience receive more weight.

### Mandatory result checks where applicable

- exact fresh-extraction inventory;
- version and package identity;
- reference resolution;
- schema meta-validation and instance validation;
- critical contract-strength comparison to baseline;
- positive and isolated negative tests;
- semantic synchronization;
- package-local replay;
- repeated clean-environment execution;
- cache and generated-file contamination;
- evidence-to-release-claim resolution;
- mutation-sensitive or independently implemented validation.

A validator PASS is one observation. Its defect sensitivity is a separate claim.

---

## STEP-08 — Score common axes

Score every evaluated source with the nine fixed axes in `metrics/metric-bank.json`:

1. Goal coverage and decision usefulness
2. Core idea strength
3. Technical soundness
4. Structural completeness
5. Operationalization detail
6. Evidence traceability
7. Risk and control adequacy
8. Internal consistency
9. Document discipline and terminology

These weights always total 100. They provide a common comparison frame across different input types. Stage-specific metrics remain the primary operational assessment for that stage.

Each axis rationale must reference claim IDs. Do not duplicate the same rationale across axes.

---

## STEP-09 — Trace evolution and drift

Perform all comparisons supported by the supplied source set:

- baseline result → target build package;
- build package → agent work;
- agent work → build result;
- build package → build result;
- result version → later result version.

Compare atomic claims using logical entailment:

- Same Claims
- Almost Same Claims
- Opposite Claims
- Almost Opposite Claims
- Unique Claim From
- Unique Claim To
- Unconfirmed

Classify drift across the governed dimensions:

- goal;
- scope;
- semantic;
- contract;
- structure;
- evidence;
- validator;
- reproducibility;
- dependency;
- discipline.

For every drift finding record:

- direction: improvement, degradation, mixed, unchanged, or unconfirmed;
- severity;
- observation;
- evidence;
- consequence.

### Drift interpretation

A new control is not an improvement until it is implemented and evidenced.  
A new folder is not a quality gain unless it supports the goal.  
A preserved file is not a preserved contract if its constraints were weakened.  
A stable fixture result can coexist with broad project-quality degradation.

---

## STEP-10 — Match problem patterns

Use `problems/problem-bank.json`.

A match requires at least:

1. one observed signal; and
2. one evidence reference.

Do not diagnose from keywords alone. Use confidence:

- low — one weak signal;
- medium — multiple consistent signals;
- high — direct observation or reproduced defect.

Import the pattern’s risk, consequences, corrective actions, and prevention controls, then tailor them to the project.

---

## STEP-11 — Select the best baseline

The baseline is the strongest verified starting point for the intended next improvement.

Rank candidate versions using:

- whole-document score;
- build-result stage score;
- evidence coverage;
- hard-gate status;
- critical problem severity;
- preservation of archetype-specific contracts;
- suitability for the next goal.

Do not select by recency. A later version may be a donor for a verified component while an older version remains the primary baseline.

State:

- selected baseline;
- decisive reasons;
- rejected alternatives;
- donor components and conditions;
- regression floors that the next build must preserve.

---

## STEP-12 — Derive verdict and emit reports

Use `metrics/report-policy.json`.

### Verdicts

- **PASS:** score at least 85, evidence coverage at least 0.80, no failed hard gate, no unresolved critical problem.
- **CONDITIONAL_PASS:** score 70–84.99, evidence coverage at least 0.50, no failed FAIL gate, explicit conditions.
- **FAIL:** score below 70 or any FAIL hard gate.
- **INSUFFICIENT_EVIDENCE:** decisive sources are unavailable or coverage is below 0.50.
- **NOT_EVALUATED:** template or stage not assessed.

Never write PASS before gates are complete.

### Required output files

1. Claim ledger conforming to `schema/claim-ledger.schema.json`
2. Evidence ledger conforming to `schema/evidence-ledger.schema.json`
3. Evaluation report conforming to `schema/evaluation-report.schema.json`

Write reports under `out/`. Preserve examples; create new filenames.

## Required report content

- domain and archetype;
- source normalization;
- claim ledger summary;
- top five heaviest claims per source;
- semantic alignment;
- common axes;
- stage-specific scores;
- whole-document scores;
- drift findings and consequences;
- problem matches;
- source judgments;
- baseline recommendation;
- final verdict and corrective actions;
- limitations and unconfirmed claims.

## Special rule for sample applications

A sample such as `simple-calculator.zip` can be valid evidence for:

- package creation;
- extraction;
- arithmetic function;
- explicit division-by-zero behavior;
- a narrowly defined profile check.

It cannot, without additional oracles, establish:

- semantic correctness of the parent project;
- schema strength;
- complete inventory;
- evidence integrity;
- ADR/reference integrity;
- general runtime capability;
- replayability of the final release;
- mutation sensitivity;
- package-level PASS.

When a build repeatedly passes the same sample while broader quality declines, classify the sample as a false-confidence amplifier, not automatically as the root cause.
