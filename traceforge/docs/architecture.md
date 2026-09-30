# Architecture

Traceforge separates reasoning, capability routing, execution, evidence, and
verification.

## Layers

### L5 — Reasoner

A human or LLM decides which uncertainty matters and proposes hypotheses.

### L4 — Planner / Capability Router

Maps a research question onto a minimal set of capabilities and ranks candidate
experiments by expected information gain, cost, and risk.

### L3 — Skills / Workflows

Reusable domain knowledge: APK reconnaissance, runtime acquisition, native RE,
API mapping, differential analysis, evidence correlation, reporting.

### L2 — Tool Adapters

Typed integration boundaries for external tools. Adapters normalize outputs and
should not expose unrestricted shell access when a narrower capability exists.

### L1 — Evidence Store

SQLite-backed mission state plus content-addressed artifacts (planned).
The evidence store is the source of truth; chat context is not.

## OODA mapping

| OODA | Traceforge |
|---|---|
| Observe | adapters emit artifacts/observations |
| Orient | entity resolution + existing evidence + priors |
| Decide | experiment planner / information gain |
| Act | scoped tool invocation |
| Learn | verifier updates facts/hypotheses/failures |

## Trust model

Tool output is untrusted input.

The system should distinguish:

- tool says an action completed,
- artifact structurally validates,
- independent observation corroborates it,
- semantic claim is justified.

These are different trust levels.

## Adapter contract

An adapter should provide:

- name/version
- capabilities
- healthcheck
- structured action parameters
- structured observations
- artifact references
- errors/failures
- provenance

Adapters should not decide research conclusions.
