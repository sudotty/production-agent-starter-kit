# AGENTS.md — Traceforge

## Mission

Traceforge is an evidence-driven Android reverse-engineering research harness for
owned or explicitly authorized targets.

Agents working in this repository must optimize for:

1. reproducibility,
2. evidence quality,
3. minimal-risk experiments,
4. explicit uncertainty,
5. durable mission state.

## Core research loop

Use:

\`Observe → Hypothesize → Design experiment → Execute → Verify → Record → Re-plan\`

Do not turn a tool result directly into a fact.

## Evidence discipline

Every durable claim should identify:

- source tool or observation plane,
- artifact or run reference,
- time / experiment context when relevant,
- confidence,
- what would falsify the claim.

Prefer independent corroboration before promoting a hypothesis to a fact.

## Tool failures are evidence

A failed attach, empty DEX, missing symbol, parser failure, or unstable hook is
not "nothing happened." Record the failure and use it to update hypotheses.

## Capability risk classes

Future adapters should classify operations as:

- observe: read-only acquisition and inspection,
- mutate: changes local target state or instrumented process behavior,
- destructive: deletes data, damages state, or has external side effects.

Default to observe. Mutation requires an explicit experiment rationale.
Destructive actions are outside the default Traceforge workflow.

## Authorization

Do not use Traceforge to facilitate unauthorized access to third-party systems.
The mission record requires an authorization note. Treat that note as scope, not
as a blanket permission to expand into unrelated systems.

## Engineering rules

- Keep the core dependency-light.
- Prefer typed/structured adapter outputs over parsing terminal prose.
- Persist artifacts by content hash where possible.
- Make planner decisions inspectable.
- Add a verifier before adding autonomous mutation.
- Pin external tools and record provenance before production use.
- Tests must not require a live third-party service.
