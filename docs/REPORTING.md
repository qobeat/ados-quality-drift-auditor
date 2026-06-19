# Reporting Contract

The JSON report is the machine authority. A human summary may be generated from it but must not change scores or verdicts.

## Required sections

- project and source normalization;
- archetype selection;
- evidence assessment;
- stage evaluations;
- common-axis evaluations;
- comparisons and drift;
- problem matches;
- baseline recommendation;
- final verdict;
- limitations.

## Score precision

Retain full precision during calculation. Round displayed final scores to two decimals.

## Verdict precedence

Hard gates override averages. Evidence coverage can reduce the verdict to INSUFFICIENT_EVIDENCE. The final verdict is computed after all stage evaluations and comparisons.

## Baseline language

State one primary baseline. List donor components separately, with verification conditions. Do not call an unverified hybrid tree the baseline.
