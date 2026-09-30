# Evaluation Philosophy

Traceforge should be evaluated as a research system.

## Claims to test

1. Durable mission state reduces repeated work.
2. Differential observation reduces irrelevant analysis.
3. Information-gain planning reduces low-value experiments.
4. Independent verification reduces unsupported claims.
5. Recovery Score predicts analyst usefulness better than "dump succeeded."

## Anti-metrics

Avoid optimizing for:

- number of tools invoked,
- number of files dumped,
- size of generated report,
- number of findings without verification,
- token consumption as a proxy for depth.

## Reproducibility bundle

A future mission export should contain:

- target hashes (not necessarily target bytes),
- tool lock/provenance,
- experiment definitions,
- normalized observations,
- artifact hashes,
- claim graph,
- failures,
- planner decisions,
- generated report.
