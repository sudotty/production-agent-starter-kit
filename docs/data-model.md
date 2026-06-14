# Data Model

## Core tables

### agent_runs

| Field | Purpose |
|---|---|
| id | Run id |
| title | Short task title |
| input | Original user task |
| status | created, running, waiting, completed, failed |
| started_at | Start time |
| finished_at | End time |

### agent_steps

| Field | Purpose |
|---|---|
| id | Step id |
| run_id | Parent run |
| step_index | Order in timeline |
| step_type | plan, model, context, tool, review, final |
| summary | Short explanation |
| payload | Structured details |
| status | pending, completed, failed |

### model_calls

| Field | Purpose |
|---|---|
| id | Model call id |
| run_id | Parent run |
| step_id | Parent step |
| provider | Model provider |
| model | Model name |
| input_summary | Short input summary |
| output | Structured output |
| latency_ms | Runtime time |
| token_count | Optional token count |

### review_points

| Field | Purpose |
|---|---|
| id | Review id |
| run_id | Parent run |
| step_id | Parent step |
| reason | Why a human should check this step |
| decision | pending, accepted, rejected, changed |
| note | Reviewer note |

### quality_notes

| Field | Purpose |
|---|---|
| id | Note id |
| run_id | Parent run |
| score | Optional simple score |
| summary | Human-readable quality note |
| created_at | Created time |

## MVP rule

Every important step should be a record. The UI should be able to reconstruct the run from stored records alone.
