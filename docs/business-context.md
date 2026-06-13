# Business Context

## Who this is for

This project is for engineers and teams that need a clear reference architecture for production-style AI agents.

Typical users:

- Applied AI engineers building agent applications.
- Backend engineers moving from LLM demos to real systems.
- AI platform teams defining common runtime patterns.
- Hiring managers who want to evaluate production judgment.

## Business problem

Most agent prototypes start as a prompt and a few function calls. That is useful for exploration, but it is not enough for real work.

A production-style system needs:

- state
- traces
- model call records
- controlled actions
- human review points
- quality checks
- cost and latency visibility

## Product wedge

This starter kit turns scattered agent ideas into one coherent system shape:

- runtime
- gateway
- review flow
- trace view
- eval loop
- deployment notes

The practical message is simple: agent work should be observable, reviewable, and measurable.

## Demo story

A user starts a task. The system creates a run, records steps, calls a model, uses context, optionally proposes an external action, waits for review when needed, and records an eval result.

## Hiring signal

This project demonstrates architecture thinking. It shows the ability to design the surrounding system that makes AI agents useful beyond a demo.
