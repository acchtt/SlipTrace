PRAGMA foreign_keys = ON;
CREATE TABLE boards (id TEXT PRIMARY KEY, created_at TEXT NOT NULL, title TEXT NOT NULL, context TEXT NOT NULL, model_sha TEXT NOT NULL);
CREATE TABLE matches (id TEXT PRIMARY KEY, board_id TEXT NOT NULL REFERENCES boards(id), frozen TEXT NOT NULL, event_id INTEGER, UNIQUE(board_id, event_id));
CREATE TABLE evidence (id TEXT PRIMARY KEY, match_id TEXT NOT NULL REFERENCES matches(id), kind TEXT NOT NULL, created_at TEXT NOT NULL, payload TEXT NOT NULL);
CREATE INDEX evidence_match ON evidence(match_id, kind, created_at);
CREATE TABLE assessments (id TEXT PRIMARY KEY, match_id TEXT NOT NULL REFERENCES matches(id), created_at TEXT NOT NULL, payload TEXT NOT NULL, airtable_id TEXT);
CREATE INDEX assessment_match ON assessments(match_id, created_at);
CREATE UNIQUE INDEX one_verdict_per_image ON assessments(match_id, json_extract(payload, '$.oddsEvidenceId')) WHERE json_extract(payload, '$.oddsEvidenceId') IS NOT NULL;
