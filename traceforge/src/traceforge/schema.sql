PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS missions (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  authorization_note TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS targets (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  kind TEXT NOT NULL,
  identifier TEXT NOT NULL,
  sha256 TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS artifacts (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  target_id INTEGER REFERENCES targets(id) ON DELETE SET NULL,
  kind TEXT NOT NULL,
  path TEXT,
  sha256 TEXT,
  provenance TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS observations (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  target_id INTEGER REFERENCES targets(id) ON DELETE SET NULL,
  source TEXT NOT NULL,
  event_time TEXT,
  summary TEXT NOT NULL,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS entities (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  entity_type TEXT NOT NULL,
  canonical_name TEXT NOT NULL,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS relations (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  src_entity_id INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  relation_type TEXT NOT NULL,
  dst_entity_id INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
  confidence REAL NOT NULL DEFAULT 1.0,
  evidence_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS claims (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  kind TEXT NOT NULL CHECK(kind IN ('fact','hypothesis')),
  statement TEXT NOT NULL,
  confidence REAL NOT NULL CHECK(confidence >= 0 AND confidence <= 1),
  status TEXT NOT NULL DEFAULT 'open',
  evidence_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS hypotheses (
  id INTEGER PRIMARY KEY,
  claim_id INTEGER NOT NULL REFERENCES claims(id) ON DELETE CASCADE,
  prior REAL NOT NULL CHECK(prior >= 0 AND prior <= 1),
  posterior REAL CHECK(posterior >= 0 AND posterior <= 1),
  falsification_condition TEXT
);

CREATE TABLE IF NOT EXISTS experiments (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  hypothesis_id INTEGER REFERENCES hypotheses(id) ON DELETE SET NULL,
  name TEXT NOT NULL,
  question TEXT NOT NULL,
  action TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'planned',
  expected_information_gain REAL,
  expected_cost REAL NOT NULL DEFAULT 1.0,
  reversible INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS runs (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  experiment_id INTEGER REFERENCES experiments(id) ON DELETE SET NULL,
  tool_id INTEGER REFERENCES tools(id) ON DELETE SET NULL,
  started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ended_at TEXT,
  exit_status TEXT,
  stdout_artifact_id INTEGER REFERENCES artifacts(id) ON DELETE SET NULL,
  stderr_artifact_id INTEGER REFERENCES artifacts(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS failures (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  run_id INTEGER REFERENCES runs(id) ON DELETE SET NULL,
  failure_type TEXT NOT NULL,
  summary TEXT NOT NULL,
  retryable INTEGER NOT NULL DEFAULT 0,
  evidence_json TEXT NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS decisions (
  id INTEGER PRIMARY KEY,
  mission_id INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  decision TEXT NOT NULL,
  rationale TEXT NOT NULL,
  evidence_json TEXT NOT NULL DEFAULT '[]',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tools (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  version TEXT,
  provenance TEXT,
  sha256 TEXT,
  trust_state TEXT NOT NULL DEFAULT 'unverified'
);

CREATE TABLE IF NOT EXISTS capabilities (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  risk_class TEXT NOT NULL DEFAULT 'observe',
  description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tool_capabilities (
  tool_id INTEGER NOT NULL REFERENCES tools(id) ON DELETE CASCADE,
  capability_id INTEGER NOT NULL REFERENCES capabilities(id) ON DELETE CASCADE,
  PRIMARY KEY(tool_id, capability_id)
);

CREATE INDEX IF NOT EXISTS idx_obs_mission_time ON observations(mission_id, event_time);
CREATE INDEX IF NOT EXISTS idx_claims_mission_kind ON claims(mission_id, kind);
CREATE INDEX IF NOT EXISTS idx_entities_mission_type ON entities(mission_id, entity_type);
