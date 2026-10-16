from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from control_plane import (
    ControlPlaneError,
    ROOT,
    SCHEMA,
    _load_request,
    _repo_file,
)


class ControlPlaneTests(unittest.TestCase):
    def test_repo_file_rejects_absolute_and_escape_paths(self):
        with self.assertRaisesRegex(ControlPlaneError, "repository-relative"):
            _repo_file(str(ROOT / "models/football/CURRENT_MODEL.md"), "path")
        with self.assertRaisesRegex(ControlPlaneError, "escapes the repository"):
            _repo_file("../outside.json", "path")

    def test_repo_file_accepts_real_repository_file(self):
        resolved = _repo_file(
            "models/football/CURRENT_MODEL.md",
            "path",
        )
        self.assertTrue(resolved.is_file())
        self.assertEqual(resolved.name, "CURRENT_MODEL.md")

    def test_request_schema_and_operation_are_bound(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            request_path = Path(folder) / "request.json"
            request_path.write_text(
                json.dumps(
                    {
                        "schema_version": SCHEMA,
                        "operation": "rank",
                        "paths": {},
                    }
                ),
                encoding="utf-8",
            )
            request = _load_request(request_path, "rank")
            self.assertEqual(request["operation"], "rank")
            with self.assertRaisesRegex(ControlPlaneError, "does not match"):
                _load_request(request_path, "sweep")

    def test_unknown_schema_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            request_path = Path(folder) / "request.json"
            request_path.write_text(
                json.dumps(
                    {
                        "schema_version": "wrong",
                        "operation": "rank",
                        "paths": {},
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ControlPlaneError, "schema_version"):
                _load_request(request_path, "rank")


if __name__ == "__main__":
    unittest.main()
