import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from coverage_manifest import (  # noqa: E402
    CoverageManifestError,
    MANIFEST_VERSION,
    validate_required_competition_manifest,
)


def payload(status="CHECKED_NO_IN_WINDOW_FIXTURES", fixtures=None):
    if fixtures is None:
        fixtures = []
    return {
        "required_competition_manifest_version": MANIFEST_VERSION,
        "required_competition_blocks": [
            {
                "block_id": "NED_EERSTE_DIVISIE",
                "status": status,
                "fixture_count": len(fixtures),
                "fixtures": fixtures,
                "note": "explicit protected-block check",
            }
        ],
    }


class RequiredCoverageManifestTests(unittest.TestCase):
    def test_no_fixture_window_can_pass_when_explicitly_checked(self):
        result = validate_required_competition_manifest(payload())
        self.assertTrue(result["required_blocks_complete"])

    def test_checked_fixtures_require_complete_disposition(self):
        row = {
            "match_id": "ned-1",
            "match": "Vitesse - NAC Breda",
            "kickoff_ict": "2026-10-03T21:30:00+07:00",
            "disposition": "ADMITTED_TO_C",
        }
        result = validate_required_competition_manifest(
            payload("CHECKED_WITH_FIXTURES", [row])
        )
        self.assertTrue(result["required_blocks_complete"])

    def test_missing_eerste_block_fails_closed(self):
        bad = {
            "required_competition_manifest_version": MANIFEST_VERSION,
            "required_competition_blocks": [],
        }
        with self.assertRaisesRegex(
            CoverageManifestError,
            "REQUIRED COMPETITION COVERAGE GAP",
        ):
            validate_required_competition_manifest(bad)

    def test_source_blocked_fails_closed(self):
        with self.assertRaisesRegex(CoverageManifestError, "SOURCE_BLOCKED"):
            validate_required_competition_manifest(
                payload("SOURCE_BLOCKED")
            )

    def test_count_mismatch_fails_closed(self):
        bad = payload()
        bad["required_competition_blocks"][0]["fixture_count"] = 1
        with self.assertRaisesRegex(CoverageManifestError, "fixture_count"):
            validate_required_competition_manifest(bad)

    def test_missing_disposition_fails_closed(self):
        row = {
            "match_id": "ned-1",
            "match": "Vitesse - NAC Breda",
            "kickoff_ict": "2026-10-03T21:30:00+07:00",
        }
        with self.assertRaisesRegex(CoverageManifestError, "invalid disposition"):
            validate_required_competition_manifest(
                payload("CHECKED_WITH_FIXTURES", [row])
            )


if __name__ == "__main__":
    unittest.main()
