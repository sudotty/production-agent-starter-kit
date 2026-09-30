from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CaptureDelta:
    added_hashes: set[str]
    removed_hashes: set[str]
    unchanged_hashes: set[str]

    def to_dict(self) -> dict:
        return {
            "added_hashes": sorted(self.added_hashes),
            "removed_hashes": sorted(self.removed_hashes),
            "unchanged_hashes": sorted(self.unchanged_hashes),
            "added_count": len(self.added_hashes),
            "removed_count": len(self.removed_hashes),
            "unchanged_count": len(self.unchanged_hashes),
        }


def compare_manifest_dicts(before: dict, after: dict) -> CaptureDelta:
    before_hashes = {a["sha256"] for a in before.get("artifacts", [])}
    after_hashes = {a["sha256"] for a in after.get("artifacts", [])}
    return CaptureDelta(
        added_hashes=after_hashes - before_hashes,
        removed_hashes=before_hashes - after_hashes,
        unchanged_hashes=before_hashes & after_hashes,
    )
