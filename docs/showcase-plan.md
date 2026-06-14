# Showcase Plan

## Product form

A reference console for a production-style AI agent runtime. The project should show the surrounding system: runs, steps, models, tools, review points, metrics, and notes.

## MVP screens

1. Run list: all tasks with status and duration.
2. Run detail: input, output, steps, and notes.
3. Step timeline: model call, context use, action proposal, review step, final result.
4. Model call panel: provider, structured output, tokens, latency.
5. Review panel: what needs human review and why.
6. Eval panel: simple baseline result.

## Demo flow

1. Start one task.
2. Show run creation.
3. Show each step in the timeline.
4. Show a structured model output.
5. Show one review point.
6. Show final output and eval note.

## Good demo points

- The runtime has state.
- Each step is inspectable.
- Model calls are measurable.
- Human review is part of the system.
- The demo connects architecture, product, and evaluation.

## First-version boundary

Do not build a full platform first. Build one clear runtime path and make it easy to inspect.
