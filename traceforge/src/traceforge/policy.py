from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class RiskClass(IntEnum):
    OBSERVE = 10
    MUTATE = 20
    DESTRUCTIVE = 30


@dataclass(frozen=True, slots=True)
class PolicyProfile:
    name: str = "observation-first"
    max_risk: RiskClass = RiskClass.OBSERVE
    require_authorization_note: bool = True


class PolicyError(RuntimeError):
    pass


def authorize_capability(
    capability: str,
    risk: RiskClass,
    *,
    profile: PolicyProfile,
    authorization_note: str,
) -> None:
    if profile.require_authorization_note and not authorization_note.strip():
        raise PolicyError("mission authorization note is required")
    if risk > profile.max_risk:
        raise PolicyError(
            f"capability {capability!r} has risk={risk.name.lower()}, "
            f"above profile maximum {profile.max_risk.name.lower()}"
        )
