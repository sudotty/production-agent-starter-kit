# Production Agent Starter Kit

A production-style starter kit for building, running, evaluating, and governing AI agents with RAG, MCP tools, human approval, tracing, and regression tests.

This repository is not intended to be another chatbot demo. It is a practical learning and interview project for engineers who want to understand how AI agents move from prototype to production.

## Why this project exists

Most AI agent demos fail at the same boundary: they can answer, but they are not reliable enough to act.

A production agent needs more than an LLM call:

- context construction
- RAG and memory retrieval
- tool calling and MCP integration
- permission checks and audit logs
- human approval for sensitive actions
- traceable execution
- evaluation and regression tests
- deployment and configuration discipline

## MVP target

Build the smallest useful production-agent skeleton:

```text
agent run -> step trace -> model call -> optional retrieval -> optional external action -> review point -> eval result
```

The first demo should prove that every action is visible, every decision is traceable, and every version can be compared against a small eval set.

## Prioritized roadmap

| Priority | Workstream | Outcome |
|---|---|---|
| P0 / MVP | Architecture and data model | The system has clear boundaries, state, and storage objects |
| P0 / MVP | Run and step tracking | A user can inspect what the agent did |
| P0 / MVP | Model gateway | Model calls are structured, measurable, and replaceable |
| P1 | Human review flow | Sensitive actions can pause and resume |
| P1 | Trace viewer | Failures become visible instead of hidden |
| P1 | Eval runner | New versions can be compared against baseline runs |
| P2 | Interview package | The project becomes easy to explain in remote interviews |

## Modules

| Module | Purpose |
|---|---|
| Agent Runtime | Run/step/state model for multi-step agents |
| Model Gateway | Unified model calls, structured outputs, token/cost tracking |
| RAG Service | Document ingestion, hybrid retrieval, reranking, citations |
| MCP Tool Gateway | Tool registry, schema validation, permissions, audit logs |
| Human Approval | Pause/resume execution for sensitive actions |
| Eval System | Baseline/candidate comparison and release confidence |
| Observability | Trace viewer for steps, model calls, retrieval, and external actions |

## Planned stack

- Frontend: Next.js / React / Tailwind
- Backend: Spring Boot or FastAPI
- Worker: Python + LangGraph-style state machine
- Database: PostgreSQL + pgvector or MySQL + Qdrant
- Queue: Redis or NATS
- Deployment: Docker Compose first

## Success criteria

1. Run a multi-step agent task.
2. Show every step in a trace.
3. Pause for human review before sensitive actions.
4. Compare two agent versions on an eval set.
5. Explain why a run failed.
6. Start locally with clear documentation.

## Interview value

This project is designed to demonstrate backend maturity, agent runtime design, tool safety, eval-driven development, and clear remote-friendly technical writing.

## Status

Planning and scaffolding. Issues are used as the implementation roadmap.
