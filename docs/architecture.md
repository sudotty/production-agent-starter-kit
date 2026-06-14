# Architecture

## Goal

Build a reference runtime for production-style AI agents. The project should show run state, step timeline, model output, review point, and quality note.

## System boundary

The first version should be a clear skeleton, not a full platform. It should demonstrate how the surrounding system makes an agent inspectable.

## Components

| Component | Responsibility |
|---|---|
| Web UI | Run list, run detail, step timeline, model panel, review panel, quality panel |
| Runtime API | Create runs, append steps, return status and timeline |
| Agent worker | Executes a simple state machine for one task |
| Model gateway | Calls model provider and records structured output, tokens, and latency |
| Context service | Provides small context records or retrieval results |
| Tool boundary | Records proposed external actions without deep integration first |
| Review module | Pauses a step for human check when needed |
| Eval module | Stores a simple quality note or comparison result |
| Storage | Runs, steps, model calls, context records, review records, quality notes |

## MVP flow

```text
Create run
  -> append planning step
  -> call model
  -> attach context
  -> create review point
  -> finalize output
  -> store quality note
```

## Recommended first stack

- Frontend: React / Next.js / Tailwind
- Backend: FastAPI or Spring Boot
- Worker: simple state machine first
- Database: SQLite or PostgreSQL
- Queue: optional until long-running steps exist

## Design principle

A production-style agent is not only an answer. It is a sequence of states and decisions that can be inspected after the run.
