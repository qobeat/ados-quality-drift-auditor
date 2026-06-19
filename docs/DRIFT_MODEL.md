# Drift Model

## Comparison chain

```text
baseline result
→ target build package
→ target agent work
→ target build result
→ next version
```

Each arrow can introduce drift.

## Dimensions

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

## Drift versus change

Change is any difference. Drift is a quality-relevant difference against a controlling goal, baseline, contract, or evidence obligation.

An intentional change is not harmful drift when it is authorized, implemented, verified, and reflected across all affected surfaces.

## Consequence tracing

For each finding record:

1. observed difference;
2. governing claim or baseline;
3. direction;
4. severity;
5. direct consequence;
6. future risk;
7. corrective action;
8. prevention control.

## Cross-stage examples

- A control requires strict schemas; the agent creates generic schemas; the result validates contradictory records. This is control-to-execution contract drift with result-level false-PASS consequences.
- A control requires final-artifact replay; the agent builds the proof first; the result lacks the generator. This is execution-order and reproducibility drift.
- A sample application still passes while semantic exports degrade. This is unchanged fixture behavior alongside semantic quality degradation.
