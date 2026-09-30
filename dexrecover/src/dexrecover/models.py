from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class DexArtifact:
    path: str
    sha256: str
    size: int
    magic: str
    version: str | None
    header_file_size: int | None
    structurally_valid: bool
    reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class CaptureManifest:
    label: str
    artifacts: list[DexArtifact] = field(default_factory=list)

    @property
    def unique_hashes(self) -> set[str]:
        return {a.sha256 for a in self.artifacts}

    @property
    def valid_hashes(self) -> set[str]:
        return {a.sha256 for a in self.artifacts if a.structurally_valid}

    def to_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "artifact_count": len(self.artifacts),
            "unique_count": len(self.unique_hashes),
            "valid_count": len(self.valid_hashes),
            "artifacts": [a.to_dict() for a in self.artifacts],
        }
