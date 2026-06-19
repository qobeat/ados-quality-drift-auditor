# ADOS Glossary v1.4 and v1.5 — Real Problem Examples

These examples are based on the supplied project artifacts and completed evaluations. They illustrate patterns; they are not universal claims about every project.

## 1. Stronger structure, weaker verified contract

v1.4 introduced more folders, registries, generated records, schemas, and tooling. That was a real structural improvement. It did not compensate for weak schema bindings, ungrounded work records, partial inventory/metadata coverage, and semantic desynchronization.

**Mapped patterns:** PROB-007, PROB-008, PROB-010, PROB-020.

## 2. Strong control pack, weak execution

The v1.5 control pack clearly required strict schemas, complete JSON governance, one-file Atomic Work, generic Reflection QA, and replay from a clean extraction. The agent execution reduced several of those obligations to shallow schemas, status assertions, and proof generation outside the final package.

**Mapped patterns:** PROB-002, PROB-003, PROB-006, PROB-012, PROB-023.

## 3. Validator PASS without defect sensitivity

The evaluated v1.4 validator accepted seven representative severe mutations. The v1.5 validator accepted five severe mutations. A validator can therefore be structurally present and return PASS while failing the release decision.

**Mapped patterns:** PROB-001, PROB-004, PROB-014, PROB-022.

## 4. The calculator was not the root cause

The calculator’s arithmetic tests passed. This was useful evidence for a narrow execution path and division-by-zero behavior. It did not test glossary semantics, schema strictness, inventories, evidence integrity, reference integrity, general runtime behavior, or final-package replay.

The failure was the inference:

```text
calculator PASS
→ runtime PASS
→ package PASS
```

Neither implication follows without additional oracles.

**Mapped patterns:** PROB-005, PROB-006, PROB-021.

## 5. Latest version was not the best baseline

v1.3 retained the strongest verified semantic and schema contracts. v1.4 and v1.5 contained useful donor ideas, but their final packages were weaker release baselines.

**Mapped patterns:** PROB-019, PROB-024.

## Corrective baseline strategy

- Use v1.3 as the primary semantic and contract baseline.
- Import v1.4 structure only component by component.
- Import v1.5 controls only after making evidence, schemas, replay, and independent audit operational.
- Regenerate all inventories and evidence from the resulting final tree.
