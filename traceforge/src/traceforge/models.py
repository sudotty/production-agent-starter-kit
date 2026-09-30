from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ClaimKind(str, Enum):
    FACT = "fact"
    HYPOTHESIS = "hypothesis"
    EXPERIMENT = "experiment"


class EvidencePolarity(str, Enum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    NEUTRAL = "neutral"


@dataclass(slots=True)
class Evidence:
    source: str
    artifact_ref: str | None = None
    observation: str = ""
    confidence: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Claim:
    kind: ClaimKind
    statement: str
    confidence: float
    scope: str = "target"
    evidence: list[Evidence] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Experiment:
    name: str
    question: str
    action: str
    expected_cost: float = 1.0
    reversible: bool = True
    required_capabilities: list[str] = field(default_factory=list)
    notes: str = ""
