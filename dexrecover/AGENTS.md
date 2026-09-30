# AGENTS.md — DexRecover

## Product boundary

DexRecover only works on runtime DEX recovery for owned or explicitly authorized Android targets.

Do not expand the project into a general Android reverse-engineering framework.

## The three questions

Every change should help answer one of these:

1. What DEX appeared at runtime?
2. Is that DEX structurally and semantically useful?
3. What controlled experiment should improve the next capture?

If it does not answer one of those questions, it likely belongs elsewhere.

## Preferred loop

`capture → validate → compare → score → decide whether to recapture`

## Evidence rules

- DEX identity is SHA-256, not filename.
- Keep capture labels and timestamps.
- Do not equate valid DEX magic with complete recovery.
- Preserve failed/incomplete captures when they explain a recovery gap.
- Prefer before/after event captures over periodic blind dumping.

## Handoff boundary

If evidence indicates that meaningful behavior is primarily native-only or implemented in a custom native VM, report a native-analysis handoff. Do not add Ghidra/native analysis into DexRecover to chase the target.

## Authorization

Work only on applications the user owns or is explicitly authorized to test, or on lawful lab/CTF/research samples.
