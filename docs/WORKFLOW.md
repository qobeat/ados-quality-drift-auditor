# Evaluation Workflow

```text
normalize sources
→ select archetype
→ inventory evidence
→ extract and weight claims
→ evaluate build package
→ evaluate agent work
→ evaluate build result
→ score common axes
→ compare stages and versions
→ match problem patterns
→ select baseline
→ apply hard gates
→ derive verdict
→ validate JSON reports
```

## Iteration

When a report fails schema validation or contains unresolved references, correct the report; do not weaken the schema to make the report pass.

When evidence changes, supersede affected evidence records and recompute scores. Preserve the prior report as historical evidence.

## Recommended filenames

```text
out/<project>-<evaluation-date>-claim-ledger.json
out/<project>-<evaluation-date>-evidence-ledger.json
out/<project>-<evaluation-date>-evaluation-report.json
```
