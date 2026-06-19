# Metric Model

## Two scoring frames

The skill uses two complementary frames:

1. **Stage-specific metrics** evaluate the obligations particular to build controls, agent work, or delivered result.
2. **Common axes** compare heterogeneous sources under one stable nine-axis frame.

The stage score answers: “How good is this artifact for its role?”  
The common-axis score answers: “How strong is this source as an evaluation or engineering artifact overall?”

## Calculation

Each applicable metric has a weight totaling 100 for the selected archetype.

```text
weighted metric = metric weight × score / 10
stage score = sum(weighted metrics)
```

Unknown metrics are null, not zero. The report must separately state evidence coverage. A high calculated score cannot produce PASS when evidence coverage or hard gates prohibit it.

## Claim-ledger relationship

Metric rationales should cite the heaviest relevant claims and their evidence. This prevents low-impact polish from dominating central contract failures.

## Count metrics

Counts may describe inventory but do not prove quality:

- 100% schema binding does not prove strict schemas.
- 100 tests do not prove correct oracles.
- 100 evidence records do not prove observations.
- More files do not prove completeness or usefulness.
