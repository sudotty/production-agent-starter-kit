from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RecoveryState:
    found_dex: bool
    structurally_valid: bool
    method_body_ratio: float | None = None
    runtime_class_coverage: float | None = None
    native_heavy: bool = False


def recommend_next_step(state: RecoveryState) -> str:
    """Return a deliberately narrow next step for authorized DEX recovery."""
    if state.native_heavy:
        return "handoff-native: target appears native-heavy; DexRecover scope ends here"

    if not state.found_dex:
        return "recapture-runtime: exercise target code paths and retry runtime DEX acquisition"

    if not state.structurally_valid:
        return "recapture-runtime: captured artifact is incomplete or structurally invalid"

    if state.method_body_ratio is not None and state.method_body_ratio < 0.5:
        return "validate-methods: DEX exists but method-body recovery appears incomplete"

    if (
        state.runtime_class_coverage is not None
        and state.runtime_class_coverage < 0.7
    ):
        return "compare-runtime-classes: recovered DEX misses a significant runtime class set"

    return "recovery-sufficient: continue normal decompilation/analysis outside DexRecover"
