from __future__ import annotations

import json
from pathlib import Path

from .dex import inspect_dex
from .models import CaptureManifest


def scan_capture(directory: str | Path, *, label: str | None = None) -> CaptureManifest:
    root = Path(directory)
    if not root.exists() or not root.is_dir():
        raise ValueError(f"capture directory does not exist: {root}")

    candidates = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in {".dex", ".cdex"}
    )
    artifacts = [inspect_dex(p) for p in candidates]
    return CaptureManifest(label=label or root.name, artifacts=artifacts)


def save_manifest(manifest: CaptureManifest, output: str | Path) -> None:
    Path(output).write_text(
        json.dumps(manifest.to_dict(), indent=2, sort_keys=True),
        encoding="utf-8",
    )


def load_manifest(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
