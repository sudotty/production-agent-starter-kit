from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RecoverySignals:
    valid_dex_ratio: float
    unique_dex_ratio: float
    method_body_ratio: float
    business_package_ratio: float
    runtime_class_coverage: float

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be between 0 and 1")


WEIGHTS = {
    "valid_dex_ratio": 0.10,
    "unique_dex_ratio": 0.05,
    "method_body_ratio": 0.35,
    "business_package_ratio": 0.20,
    "runtime_class_coverage": 0.30,
}


def recovery_score(signals: RecoverySignals) -> float:
    """Estimate whether a DEX capture is useful, not merely present."""
    signals.validate()
    value = sum(getattr(signals, key) * weight for key, weight in WEIGHTS.items())
    return max(0.0, min(1.0, value))
