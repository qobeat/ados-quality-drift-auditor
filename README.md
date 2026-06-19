# ADOS Quality Drift Auditor v0.1

## Metadata

| Attribute | Value |
|---|---|
| DOCUMENT_TYPE | guide |
| DOCUMENT_STATUS | prototype |
| UPDATED_AT | 2026-06-18 |
| DOCUMENT_ROLE | usage_entrypoint |
| GOVERNANCE_AREA | quality; evaluation; project_evolution |
| CONSUMERS | owner; architect; evaluator; builder; reviewer; self_test |
| WHEN_TO_USE | Use when comparing build controls, agent execution, and delivered versions of one project. |
| HOW_TO_USE | Read `MANIFEST.md`, then the skill, archetype bank, metric bank, problem bank, and schemas in that order. |
| DOCUMENT_CONTENT | Human entrypoint for the project-evolution quality and drift evaluation skill. |

## Goal

Provide a deterministic, evidence-traceable, archetype-aware skill for evaluating build controls, building-agent execution, and produced project versions across time, so quality drift, false-PASS risk, regression, and the best improvement baseline can be identified.

## Objectives

1. Accept build-package, building-agent-work, and build-result inputs for one or many versions of the same project.
2. Normalize every supplied artifact, extract stable atomic claims, and preserve claim identifiers through scoring and verdict.
3. Select one primary project archetype from a governed archetype bank and apply its evidence requirements, metrics, hard gates, and drift risks.
4. Score each input stage using stage-specific metrics and a common nine-axis comparison frame.
5. Trace changes from baseline result to target build package, agent work, built result, and later versions.
6. Separate observed evidence, derived calculations, inference, and evaluator judgment in every report.
7. Detect known quality-failure patterns using a machine-readable problem bank with risks, visible effects, corrections, and prevention controls.
8. Prevent false release acceptance through evidence coverage thresholds, hard gates, mutation-sensitive validation, replay checks, and verdict derivation rules.
9. Emit JSON claim ledgers and evaluation reports conforming to JSON Schema Draft 2020-12 in the out/ folder.
10. Remain usable when evidence is incomplete by returning explicit unknowns and INSUFFICIENT_EVIDENCE rather than inventing support.

## What this package evaluates

The skill accepts any combination of three evidence classes for one or more versions:

| Input class | Meaning | Typical artifacts |
|---|---|---|
| `build_package` | Instructions and supply materials that authorize a build | prompt, PDD, requirements, ADRs, baseline package, test fixtures, control pack |
| `agent_work` | What the building agent actually did and claimed | response, thinking/activity log, work plan, commands, diffs, evidence, QA reports |
| `build_result` | The resulting version or release candidate | ZIP, source tree, binary, data package, schema package, deployment manifest |

The evaluator may compare:

```text
baseline build result
→ target build package
→ target agent work
→ target build result
→ later build packages and results
```

Missing stages remain explicit. They are never silently reconstructed.

## Core method

1. Normalize the source set and assign stable source IDs.
2. Select one primary archetype from `profiles/archetype-bank.json`.
3. Inventory evidence and record coverage and independence.
4. Decompose source statements into atomic claims with stable IDs.
5. Weight and score the claims.
6. Score each available stage with stage-specific metrics.
7. Score each source with the common nine-axis frame.
8. Compare versions and stages, then classify drift by dimension and consequence.
9. Match observed conditions to `problems/problem-bank.json`.
10. Apply hard gates and derive—not author—the final verdict.
11. Save JSON reports in `out/`.

## Non-negotiable safeguards

- Evaluate only supplied material.
- Use `I cannot confirm this.` when a proposition lacks evidence.
- Keep observations, calculations, inference, and judgment distinct.
- A functional sample such as `simple-calculator.zip` is a bounded proof fixture. It cannot establish release quality outside the claims it directly tests.
- A validator written by the builder is evidence, not an independent oracle.
- PASS requires observation-bearing evidence, sufficient evidence coverage, no failed hard gate, and a score meeting policy.
- Structure, file count, schema coverage, or test count cannot substitute for semantic and contract strength.

## Quick start

```bash
python tools/validate_package.py .
python tools/self_test.py
python tools/initialize_audit.py examples/ados-glossary-evolution-input.json out/new-audit.json
```

Then use `skills/PROJECT-EVOLUTION-QUALITY-AUDITOR.md` to complete the claim ledger and report.

## Outputs

- `out/report-template.json` — empty conforming report template.
- `out/example-ados-glossary-claim-ledger.json` — abbreviated stable-claim example.
- `out/example-ados-glossary-evolution-report.json` — real-problem example based on supplied v1.3–v1.5 review findings.
- New reports should use a new filename; do not overwrite examples.

## Prototype boundary

v0.1 provides the governed method, schemas, archetypes, problem patterns, examples, a package validator, mutation self-tests, and an audit initializer. It does not pretend that qualitative evaluation can be reduced to filename scanning. Human or reasoning-agent assessment is still required for claim extraction, semantic comparison, and evidence interpretation.
