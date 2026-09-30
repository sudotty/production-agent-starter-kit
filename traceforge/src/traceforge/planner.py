from __future__ import annotations

import math
from dataclasses import dataclass, field


def entropy(probabilities: list[float]) -> float:
    total = sum(probabilities)
    if total <= 0:
        return 0.0
    normalized = [p / total for p in probabilities if p > 0]
    return -sum(p * math.log2(p) for p in normalized)


@dataclass(slots=True)
class Outcome:
    name: str
    probability: float
    posterior: list[float]


@dataclass(slots=True)
class ExperimentCandidate:
    name: str
    cost: float
    outcomes: list[Outcome] = field(default_factory=list)


def expected_information_gain(prior: list[float], candidate: ExperimentCandidate) -> float:
    """Expected entropy reduction for a candidate experiment."""
    before = entropy(prior)
    expected_after = 0.0
    probability_mass = sum(o.probability for o in candidate.outcomes)
    if probability_mass <= 0:
        return 0.0

    for outcome in candidate.outcomes:
        p = outcome.probability / probability_mass
        expected_after += p * entropy(outcome.posterior)
    return max(0.0, before - expected_after)


def rank_experiments(
    prior: list[float],
    candidates: list[ExperimentCandidate],
) -> list[tuple[str, float, float]]:
    """Rank experiments by information gain per unit cost.

    Returns tuples of (name, expected_information_gain, utility).
    """
    ranked: list[tuple[str, float, float]] = []
    for candidate in candidates:
        ig = expected_information_gain(prior, candidate)
        utility = ig / max(candidate.cost, 1e-9)
        ranked.append((candidate.name, ig, utility))
    return sorted(ranked, key=lambda row: row[2], reverse=True)
