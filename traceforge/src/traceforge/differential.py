from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RuntimeSnapshot:
    label: str
    dex_hashes: set[str] = field(default_factory=set)
    so_hashes: set[str] = field(default_factory=set)
    classes: set[str] = field(default_factory=set)
    endpoints: set[str] = field(default_factory=set)
    files: set[str] = field(default_factory=set)


@dataclass(slots=True)
class SetDelta:
    added: set[str]
    removed: set[str]


@dataclass(slots=True)
class SnapshotDelta:
    before: str
    after: str
    dex: SetDelta
    so: SetDelta
    classes: SetDelta
    endpoints: SetDelta
    files: SetDelta

    @property
    def signal_count(self) -> int:
        groups = (self.dex, self.so, self.classes, self.endpoints, self.files)
        return sum(len(g.added) + len(g.removed) for g in groups)


def _delta(before: set[str], after: set[str]) -> SetDelta:
    return SetDelta(added=after - before, removed=before - after)


def compare_snapshots(before: RuntimeSnapshot, after: RuntimeSnapshot) -> SnapshotDelta:
    """Compare two controlled runtime snapshots.

    Traceforge intentionally keeps the primitive simple: adapters are responsible
    for normalization, while this layer computes deterministic changes.
    """
    return SnapshotDelta(
        before=before.label,
        after=after.label,
        dex=_delta(before.dex_hashes, after.dex_hashes),
        so=_delta(before.so_hashes, after.so_hashes),
        classes=_delta(before.classes, after.classes),
        endpoints=_delta(before.endpoints, after.endpoints),
        files=_delta(before.files, after.files),
    )
