import unittest

from traceforge.recovery import RecoveryMetrics, recovery_score


class RecoveryScoreTests(unittest.TestCase):
    def test_score_is_bounded(self):
        metrics = RecoveryMetrics(1, 1, 1, 1, 1, 0)
        self.assertEqual(recovery_score(metrics), 1.0)

    def test_native_dependency_penalizes_score(self):
        clean = RecoveryMetrics(0.8, 0.8, 0.8, 0.8, 0.8, 0.0)
        native = RecoveryMetrics(0.8, 0.8, 0.8, 0.8, 0.8, 1.0)
        self.assertGreater(recovery_score(clean), recovery_score(native))

    def test_invalid_metric_rejected(self):
        with self.assertRaises(ValueError):
            recovery_score(RecoveryMetrics(1.1, 1, 1, 1, 1, 0))


if __name__ == "__main__":
    unittest.main()
