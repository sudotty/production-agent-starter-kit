# Evidence Model

Traceforge uses three conceptual objects: facts, hypotheses, and experiments.

## Fact

A claim supported strongly enough to be treated as current working truth within
a defined scope.

Example:

> Artifact SHA X parses as a DEX and contains package com.example.pay.

The evidence should point to the artifact and parser/run.

## Hypothesis

A falsifiable explanation with explicit uncertainty.

Example:

> The payment module is decrypted only after entering the checkout flow.

A hypothesis should include a prior/posterior and a falsification condition.

## Experiment

A scoped action intended to discriminate among hypotheses.

Example:

> Compare loaded DEX hashes immediately before and after entering checkout.

A useful experiment records:

- question,
- action,
- expected observations,
- cost,
- risk/reversibility,
- information gain,
- result.

## Failure

Failures are first-class evidence.

Examples:

- runtime attach consistently terminates the app,
- artifact parses but method bodies are empty,
- a symbol is absent on one Android build,
- two observation planes disagree.

Do not erase a failure by simply retrying until one invocation succeeds.

## Confidence

Confidence is not cosmetic. Agents should state why a value changed.

A future Bayesian layer can update hypothesis probability using likelihoods.
Until then, manual confidence updates should preserve rationale and evidence.
