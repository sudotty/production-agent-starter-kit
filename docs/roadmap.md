# Roadmap

## Phase 1: System shape

- Define the product boundary and interview story.
- Design frontend, backend API, worker, database, queue, model gateway, tool gateway, and eval layer.
- Create schemas for agent runs, steps, model calls, external actions, approval requests, and eval runs.

## Phase 2: Agent runtime

- Implement run creation and step recording.
- Add state transitions for planning, retrieval, action, approval wait, verification, success, and failure.
- Add max steps, timeout, retry policy, and cost budget.

## Phase 3: Production boundary

- Add tool gateway interface.
- Add approval gate for risky actions.
- Add trace viewer data model.
- Add audit logs.

## Phase 4: Eval and release gate

- Create eval dataset and runner.
- Implement baseline vs candidate comparison.
- Add failure taxonomy and release recommendation.

## Phase 5: Interview package

- Add screenshots and demo data.
- Record a 3-minute English demo.
- Write system design notes, trade-offs, and resume bullets.
