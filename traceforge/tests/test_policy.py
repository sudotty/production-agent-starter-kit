import unittest

from traceforge.policy import PolicyError, PolicyProfile, RiskClass, authorize_capability


class PolicyTests(unittest.TestCase):
    def test_observation_allowed(self):
        authorize_capability(
            "apk.inspect",
            RiskClass.OBSERVE,
            profile=PolicyProfile(),
            authorization_note="owned synthetic test",
        )

    def test_mutation_blocked_by_default(self):
        with self.assertRaises(PolicyError):
            authorize_capability(
                "runtime.modify",
                RiskClass.MUTATE,
                profile=PolicyProfile(),
                authorization_note="owned synthetic test",
            )


if __name__ == "__main__":
    unittest.main()
