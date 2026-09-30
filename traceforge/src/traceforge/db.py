from __future__ import annotations

import json
import sqlite3
from importlib.resources import files
from pathlib import Path


class MissionStore:
    def __init__(self, path: str | Path = "mission.db") -> None:
        self.path = Path(path)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")

    def init_schema(self) -> None:
        schema = files("traceforge").joinpath("schema.sql").read_text(encoding="utf-8")
        self.conn.executescript(schema)
        self.conn.commit()

    def create_mission(self, name: str, authorization_note: str) -> int:
        if not authorization_note.strip():
            raise ValueError("authorization_note is required")
        cur = self.conn.execute(
            "INSERT INTO missions(name, authorization_note) VALUES (?, ?)",
            (name, authorization_note),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def add_target(
        self,
        mission_id: int,
        *,
        kind: str,
        identifier: str,
        sha256: str | None = None,
        metadata: dict | None = None,
    ) -> int:
        cur = self.conn.execute(
            """INSERT INTO targets(mission_id, kind, identifier, sha256, metadata_json)
               VALUES (?, ?, ?, ?, ?)""",
            (mission_id, kind, identifier, sha256, json.dumps(metadata or {}, sort_keys=True)),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def add_observation(
        self,
        mission_id: int,
        *,
        source: str,
        summary: str,
        target_id: int | None = None,
        payload: dict | None = None,
        event_time: str | None = None,
    ) -> int:
        cur = self.conn.execute(
            """INSERT INTO observations(
                 mission_id, target_id, source, event_time, summary, payload_json
               ) VALUES (?, ?, ?, ?, ?, ?)""",
            (
                mission_id,
                target_id,
                source,
                event_time,
                summary,
                json.dumps(payload or {}, sort_keys=True),
            ),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "MissionStore":
        self.init_schema()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
