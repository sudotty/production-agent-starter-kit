import json
import struct
import tempfile
import unittest
from pathlib import Path

from dexrecover.capture import save_manifest, scan_capture
from dexrecover.compare import compare_manifest_dicts
from dexrecover.dex import inspect_dex
from dexrecover.score import RecoverySignals, recovery_score
from dexrecover.strategy import RecoveryState, recommend_next_step


def write_fake_dex(path: Path, version: bytes = b"035") -> None:
    data = bytearray(0x70)
    data[0:8] = b"dex\n" + version + b"\x00"
    struct.pack_into("<I", data, 32, len(data))
    struct.pack_into("<I", data, 36, 0x70)
    path.write_bytes(data)


class DexRecoverTests(unittest.TestCase):
    def test_inspect_valid_dex(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "classes.dex"
            write_fake_dex(path)
            artifact = inspect_dex(path)
            self.assertTrue(artifact.structurally_valid)
            self.assertEqual(artifact.version, "035")

    def test_scan_deduplicates_by_hash(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_fake_dex(root / "classes.dex")
            (root / "copy.dex").write_bytes((root / "classes.dex").read_bytes())
            manifest = scan_capture(root, label="capture")
            self.assertEqual(len(manifest.artifacts), 2)
            self.assertEqual(len(manifest.unique_hashes), 1)

    def test_diff_finds_new_dex(self):
        before = {"artifacts": [{"sha256": "a"}]}
        after = {"artifacts": [{"sha256": "a"}, {"sha256": "b"}]}
        delta = compare_manifest_dicts(before, after)
        self.assertEqual(delta.added_hashes, {"b"})

    def test_recovery_score_weights_semantics(self):
        low = RecoverySignals(1.0, 1.0, 0.1, 0.2, 0.2)
        high = RecoverySignals(1.0, 1.0, 0.9, 0.9, 0.9)
        self.assertGreater(recovery_score(high), recovery_score(low))

    def test_native_heavy_handoff(self):
        state = RecoveryState(True, True, 0.9, 0.9, native_heavy=True)
        self.assertTrue(recommend_next_step(state).startswith("handoff-native"))

    def test_manifest_is_json_serializable(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_fake_dex(root / "classes.dex")
            manifest = scan_capture(root)
            out = root / "manifest.json"
            save_manifest(manifest, out)
            parsed = json.loads(out.read_text())
            self.assertEqual(parsed["valid_count"], 1)


if __name__ == "__main__":
    unittest.main()
