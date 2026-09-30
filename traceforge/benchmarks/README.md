# Benchmarks

Traceforge benchmarks should measure research quality, not just whether a tool
returned exit code 0.

## Suggested benchmark dimensions

- artifact acquisition rate
- semantic Recovery Score
- analyst-rated usefulness
- number of experiments
- repeated/low-information experiments
- manual interventions
- time to first supported hypothesis
- time to verified conclusion
- false-positive claims
- evidence provenance completeness
- mission resume success

## Corpus principles

Use only targets that can be legally redistributed or built locally:

- purpose-built test applications,
- open-source applications built from source,
- intentionally protected benchmark variants,
- CTF/lab samples with redistribution permission.

For protection experiments, retain an unprotected ground-truth build whenever
possible. This allows recovered class/method/package coverage to be measured
rather than guessed.

## Baselines

Compare at least:

1. fixed checklist workflow,
2. unstructured LLM + shell workflow,
3. Traceforge evidence + planner workflow.

The benchmark should be allowed to falsify Traceforge's design assumptions.
