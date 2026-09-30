# dex-validation

## Goal

Validate recovered DEX artifacts and estimate semantic usefulness.

## Inputs

DEX artifact references + optional runtime class inventory.

## Outputs

Parse result, class/package/method metrics, Recovery Score inputs.

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

A valid DEX file is not equivalent to complete semantic recovery.

Use only on owned or explicitly authorized targets.
