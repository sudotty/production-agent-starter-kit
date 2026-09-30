import tempfile
import unittest
from pathlib import Path

from traceforge.db import MissionStore


class MissionStoreTests(unittest.TestCase):
    def test_create_mission_target_and_observation(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "mission.db"
            with MissionStore(path) as store:
                mission_id = store.create_mission("lab", "owned test application")
                target_id = store.add_target(
                    mission_id,
                    kind="apk",
                    identifier="sample.apk",
                    sha256="00" * 32,
                )
                obs_id = store.add_observation(
                    mission_id,
                    target_id=target_id,
                    source="unit-test",
                    summary="artifact registered",
                )
                self.assertGreater(mission_id, 0)
                self.assertGreater(target_id, 0)
                self.assertGreater(obs_id, 0)

    def test_authorization_note_required(self):
        with tempfile.TemporaryDirectory() as td:
            with MissionStore(Path(td) / "mission.db") as store:
                with self.assertRaises(ValueError):
                    store.create_mission("lab", "")


if __name__ == "__main__":
    unittest.main()
