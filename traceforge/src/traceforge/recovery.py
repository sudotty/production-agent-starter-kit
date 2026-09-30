from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True, slots=True)
class RecoveryMetrics:
    class_coverage: float
    method_body_coverage: float
    package_coverage: float
    entrypoint_coverage: float
    semantic_density: float
    native_dependency: float

    def validate(self) -> None:
        for name, value in asdict(self).items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1, got {value}")


DEFAULT_WEIGHTS = {
    "class_coverage": 0.18,
    "method_body_coverage": 0.25,
    "package_coverage": 0.16,
    "entrypoint_coverage": 0.16,
    "semantic_density": 0.15,
    "native_dependency": 0.10,
}


def recovery_score(
    metrics: RecoveryMetrics,
    weights: dict[str, float] | None = None,
) -> float:
    """Return semantic recovery score in [0, 1].

    File acquisition and semantic recovery are deliberately separate. A dumped
    DEX can score poorly when method bodies are missing or meaningful behavior
    remains native-only.
    """
    metrics.validate()
    w = dict(DEFAULT_WEIGHTS)
    if weights:
        w.update(weights)

    positive = (
        metrics.class_coverage * w["class_coverage"]
        + metrics.method_body_coverage * w["method_body_coverage"]
        + metrics.package_coverage * w["package_coverage"]
        + metrics.entrypoint_coverage * w["entrypoint_coverage"]
        + metrics.semantic_density * w["semantic_density"]
    )
    penalty = metrics.native_dependency * w["native_dependency"]
    denominator = sum(v for k, v in w.items() if k != "native_dependency")
    score = (positive / denominator) - penalty
    return max(0.0, min(1.0, score))
