import unittest

from traceforge.differential import RuntimeSnapshot, compare_snapshots


class DifferentialTests(unittest.TestCase):
    def test_added_runtime_signals(self):
        before = RuntimeSnapshot(
            "before",
            dex_hashes={"dex-a"},
            classes={"A"},
            endpoints={"https://api.example.test/a"},
        )
        after = RuntimeSnapshot(
            "after",
            dex_hashes={"dex-a", "dex-b"},
            classes={"A", "Checkout"},
            endpoints={
                "https://api.example.test/a",
                "https://api.example.test/pay",
            },
        )
        delta = compare_snapshots(before, after)
        self.assertEqual(delta.dex.added, {"dex-b"})
        self.assertEqual(delta.classes.added, {"Checkout"})
        self.assertEqual(delta.signal_count, 3)


if __name__ == "__main__":
    unittest.main()
