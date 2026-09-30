# report

## Goal

Produce an auditable research report from mission state.

## Inputs

Mission DB, evidence graph, decisions, failures and Recovery Score.

## Outputs

Scope, methods, facts, hypotheses, evidence, limitations and next experiments.

## Workflow

1. Read current mission state before acting.
2. State the uncertainty or hypothesis this Skill addresses.
3. Prefer the lowest-risk observation that can discriminate among hypotheses.
4. Execute through a typed adapter when available.
5. Persist artifacts/observations/failures.
6. Verify important claims independently when practical.
7. Update confidence and recommend the next experiment only if uncertainty remains.

## Evidence rule

Every durable claim produced from this Skill must retain provenance to the run,
artifact or observation that supports it.

## Boundary

Separate observed facts, interpretations and unresolved hypotheses.

Use only on owned or explicitly authorized targets.
