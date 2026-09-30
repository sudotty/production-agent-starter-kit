import unittest

from traceforge.planner import ExperimentCandidate, Outcome, entropy, rank_experiments


class PlannerTests(unittest.TestCase):
    def test_entropy(self):
        self.assertAlmostEqual(entropy([0.5, 0.5]), 1.0, places=6)

    def test_informative_experiment_ranks_first(self):
        prior = [0.5, 0.5]
        useful = ExperimentCandidate(
            "useful",
            1.0,
            [
                Outcome("a", 0.5, [0.95, 0.05]),
                Outcome("b", 0.5, [0.05, 0.95]),
            ],
        )
        weak = ExperimentCandidate(
            "weak",
            1.0,
            [
                Outcome("a", 0.5, [0.55, 0.45]),
                Outcome("b", 0.5, [0.45, 0.55]),
            ],
        )
        ranked = rank_experiments(prior, [weak, useful])
        self.assertEqual(ranked[0][0], "useful")


if __name__ == "__main__":
    unittest.main()
