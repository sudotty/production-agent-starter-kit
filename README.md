# Production Agent Starter Kit

A reference starter kit for production-style AI agents: run state, step timeline, model gateway, context use, external actions, human review, and quality notes.

This repository is not intended to be another chatbot demo. It is a practical learning and interview project for engineers who want to understand how AI agents move from prototype to reliable system design.

## Why this project exists

Most AI agent demos fail at the same boundary: they can answer, but the surrounding system is not visible enough to trust.

A production-style agent needs more than an LLM call:

- task state
- context construction
- model call records
- tool or external action boundaries
- human review for sensitive steps
- step-by-step traces
- quality checks
- deployment and configuration discipline

## Product shape

The product should feel like a reference console for inspecting one agent run from start to finish.

Core screens:

| Screen | What it shows |
|---|---|
| Run List | Tasks, status, duration, model, and result |
| Run Detail | Input, final output, status, and notes |
| Step Timeline | Context use, model call, action proposal, review step, final note |
| Model Panel | Provider, structured output, tokens, latency |
| Review Panel | What needs human attention and why |
| Quality Panel | Simple comparison note or eval result |

## MVP target

Build the smallest useful production-agent skeleton:

```text
run list -> run detail -> step timeline -> model output -> review point -> final note
```

The first demo should prove that every important step is visible and easy to inspect.

## Prioritized roadmap

| Priority | Workstream | Outcome |
|---|---|---|
| P0 / MVP | Architecture and data model | The system has clear boundaries, state, and storage objects |
| P0 / MVP | Run and step tracking | A user can inspect what the agent did |
| P0 / MVP | Model gateway | Model calls are structured, measurable, and replaceable |
| P0 / MVP | Showcase path | One demo path from run list to final note |
| P1 | Human review flow | Sensitive steps can pause and resume |
| P1 | Trace viewer | Weak or failed runs become visible instead of hidden |
| P1 | Eval runner | New versions can be compared against baseline runs |
| P2 | Interview package | The project becomes easy to explain in remote interviews |

## Repository documents

- [Business Context](docs/business-context.md)
- [Roadmap](docs/roadmap.md)
- [Showcase Plan](docs/showcase-plan.md)
- [Design Gallery](docs/design-gallery.md)

## Planned stack

- Frontend: Next.js / React / Tailwind
- Backend: Spring Boot or FastAPI
- Worker: Python state machine
- Database: PostgreSQL or MySQL first
- Queue: Redis or NATS when async execution is needed
- Deployment: Docker Compose first

## Demo narrative

1. Start one sample task.
2. Open the run detail page.
3. Inspect the step timeline.
4. Open the model output panel.
5. Show one human review point.
6. Show the final note and quality result.

## What this project demonstrates

- Backend architecture for stateful AI agents.
- Clear separation between runtime, model gateway, tool layer, and evaluation.
- Observability and reviewability as first-class product concerns.
- Practical judgment about where to keep a human in the loop.
- Strong fit for AI platform, AgentOps, and backend AI engineering roles.

## Status

Planning and scaffolding. Issues are used as the implementation roadmap. The next build target is the P0 MVP showcase path.
