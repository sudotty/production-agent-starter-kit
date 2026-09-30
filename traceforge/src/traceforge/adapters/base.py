from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(slots=True)
class AdapterResult:
    ok: bool
    observations: list[dict[str, Any]] = field(default_factory=list)
    artifacts: list[dict[str, Any]] = field(default_factory=list)
    raw_ref: str | None = None
    error: str | None = None


class ToolAdapter(Protocol):
    name: str
    capabilities: frozenset[str]

    def healthcheck(self) -> dict[str, Any]:
        ...

    def run(self, action: str, **kwargs: Any) -> AdapterResult:
        ...
