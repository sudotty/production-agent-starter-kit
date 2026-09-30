from __future__ import annotations

import hashlib
import struct
from pathlib import Path

from .models import DexArtifact


DEX_PREFIX = b"dex\n"
CDEX_PREFIX = b"cdex"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inspect_dex(path: str | Path) -> DexArtifact:
    p = Path(path)
    size = p.stat().st_size
    sha = sha256_file(p)

    with p.open("rb") as f:
        header = f.read(112)

    magic_bytes = header[:8]
    magic = magic_bytes.decode("latin1", errors="replace")
    version: str | None = None
    header_file_size: int | None = None

    if len(header) < 40:
        return DexArtifact(
            str(p), sha, size, magic, None, None, False, "file too small for DEX header"
        )

    if magic_bytes.startswith(DEX_PREFIX) and magic_bytes[-1:] == b"\x00":
        try:
            version = magic_bytes[4:7].decode("ascii")
        except UnicodeDecodeError:
            version = None
    elif magic_bytes.startswith(CDEX_PREFIX):
        try:
            version = magic_bytes[4:7].decode("ascii")
        except UnicodeDecodeError:
            version = None
    else:
        return DexArtifact(
            str(p), sha, size, magic, None, None, False, "unrecognized DEX/CDEX magic"
        )

    header_file_size = struct.unpack_from("<I", header, 32)[0]
    header_size = struct.unpack_from("<I", header, 36)[0]

    if magic_bytes.startswith(DEX_PREFIX):
        header_ok = header_size == 0x70
    else:
        # Compact DEX headers vary from standard DEX. Keep v0.1 validation
        # conservative: reject impossible sizes without pretending to fully
        # validate every CompactDex header revision.
        header_ok = 0x70 <= header_size <= size

    if not header_ok:
        return DexArtifact(
            str(p),
            sha,
            size,
            magic,
            version,
            header_file_size,
            False,
            f"unexpected header_size=0x{header_size:x}",
        )

    if header_file_size <= 0 or header_file_size > size:
        return DexArtifact(
            str(p),
            sha,
            size,
            magic,
            version,
            header_file_size,
            False,
            "header file_size exceeds captured file size",
        )

    return DexArtifact(
        str(p), sha, size, magic, version, header_file_size, True, None
    )
