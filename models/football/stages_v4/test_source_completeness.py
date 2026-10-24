"""Prospective sweep rebuild: date-surface completeness must fail closed."""
from __future__ import annotations

import copy
import pathlib
import sys
import unittest

DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(DIR))

from source_completeness import (
    CONTRACT,
    SourceCompletenessError,
    required_surface_keys,
    validate_source_completeness,
)
from stage import StageError, sweep


NOW = "2026-10-12T18:05:00Z"
START = "2026-10-12T18:10:00Z"
END = "2026-10-12T20:00:00Z"
KO = "2026-10-12T19:00:00Z"
MATCH = "aiscore-fixture-1"


def source():
    fixture = {
        "match_id": MATCH,
        "country": "Finland",
        "competition": "Finnish Veikkausliiga",
        "competition_kind": "DOMESTIC_LEAGUE",
        "home": "AC Oulu",
        "away": "HJK Helsinki",
        "kickoff_utc": KO,
        "fixture_status": "PREMATCH_CONFIRMED",
        "source_url": "https://sports.example.org/match/aiscore-fixture-1",
        "observed_at_utc": "2026-10-12T18:04:00Z",
    }
    keys = required_surface_keys(START, END)
    surfaces = []
    for key in keys:
        surfaces.append({
            "surface_key": key,
            "source_url": "https://sports.example.org/football/date/" + key.split(":", 1)[1],
            "observed_at_utc": "2026-10-12T18:04:00Z",
            "provider_page_count": 1,
            "pages_fetched": [1],
            "pagination_complete": True,
            "provider_senior_fixture_count": 1,
            "provider_senior_competition_block_count": 1,
            "extracted_fixture_ids": [MATCH],
            "competition_blocks": [{
                "country": "Finland",
                "competition": "Finnish Veikkausliiga",
                "provider_fixture_count": 1,
                "extracted_fixture_ids": [MATCH],
            }],
        })
    return {
        "schema_version": "football-stages-v4",
        "run_id": "V4-20261013-0105-0300-S2",
        "window_start_utc": START,
        "window_end_utc": END,
        "source_family": "Fixture Provider One",
        "source_url": "https://sports.example.org/football/date",
        "source_observed_at_utc": "2026-10-12T18:04:00Z",
        "fixtures": [fixture],
        "source_completeness_manifest": {
            "schema_version": "football-v4-source-completeness-v2",
            "acquisition_mode": CONTRACT,
            "league_query_mode": "DATE_SURFACE_ONLY",
            "registry_prefilter_applied": False,
            "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS",
            "extraction_complete": True,
            "provider_family": "Fixture Provider One",
            "window_start_utc": START,
            "window_end_utc": END,
            "checked_at_utc": "2026-10-12T18:04:00Z",
            "required_surface_keys": keys,
            "date_surfaces": surfaces,
            "terminal_sentinel": {
                "interval_start_utc": START,
                "interval_end_utc": END,
                "checked_at_utc": "2026-10-12T18:04:30Z",
                "independent_refetch": True,
                "source_urls": ["https://sports.example.org/football/date"],
                "provider_senior_fixture_count": 1,
                "extracted_fixture_ids": [MATCH],
                "complete": True,
            },
        },
    }


class SourceCompletenessContractTests(unittest.TestCase):
    def test_valid_complete_date_surface_manifest(self):
        proof = validate_source_completeness(source(), now=NOW)
        self.assertEqual(proof["source_completeness_contract"], CONTRACT)
        self.assertEqual(proof["provider_senior_fixture_union_count"], 1)
        self.assertFalse(proof["registry_prefilter_applied"])
        self.assertEqual(proof["league_query_mode"], "DATE_SURFACE_ONLY")

    def test_new_source_requires_independent_priority_verification(self):
        item = source()
        item["source_observed_at_utc"] = "2026-10-21T00:00:00Z"
        with self.assertRaisesRegex(SourceCompletenessError, "SWEEP_COMPLETENESS_BLOCKED"):
            validate_source_completeness(item, now=NOW)
        item["priority_completeness_verification"] = {
            "status": "PRIORITY_COMPLETENESS_VERIFIED",
            "timezone_contract": "ISO_8601_EXPLICIT_UTC",
            "validator_family": "Independent Provider",
        }
        proof = validate_source_completeness(item, now=NOW)
        self.assertTrue(proof["priority_completeness_verified"])

    def test_missing_required_ict_or_utc_surface_fails(self):
        item = source()
        item["source_completeness_manifest"]["date_surfaces"].pop()
        with self.assertRaisesRegex(SourceCompletenessError, "missing required surfaces"):
            validate_source_completeness(item, now=NOW)

    def test_registry_prefilter_or_league_query_discovery_fails(self):
        item = source()
        item["source_completeness_manifest"]["registry_prefilter_applied"] = True
        with self.assertRaisesRegex(SourceCompletenessError, "REGISTRY_PREFILTER"):
            validate_source_completeness(item, now=NOW)
        item = source()
        item["source_completeness_manifest"]["league_query_mode"] = "REGISTERED_LEAGUES_ONLY"
        with self.assertRaisesRegex(SourceCompletenessError, "LEAGUE_BY_LEAGUE"):
            validate_source_completeness(item, now=NOW)

    def test_unexhausted_pagination_fails(self):
        item = source()
        surface = item["source_completeness_manifest"]["date_surfaces"][0]
        surface["provider_page_count"] = 2
        with self.assertRaisesRegex(SourceCompletenessError, "pages_fetched"):
            validate_source_completeness(item, now=NOW)

    def test_provider_fixture_and_block_counts_must_reconcile(self):
        item = source()
        item["source_completeness_manifest"]["date_surfaces"][0]["provider_senior_fixture_count"] = 2
        with self.assertRaisesRegex(SourceCompletenessError, "provider fixture count"):
            validate_source_completeness(item, now=NOW)
        item = source()
        item["source_completeness_manifest"]["date_surfaces"][0]["provider_senior_competition_block_count"] = 2
        with self.assertRaisesRegex(SourceCompletenessError, "block count"):
            validate_source_completeness(item, now=NOW)

    def test_registered_competition_block_cannot_silently_drop_fixture(self):
        item = source()
        surface = item["source_completeness_manifest"]["date_surfaces"][0]
        surface["provider_senior_fixture_count"] = 2
        surface["extracted_fixture_ids"].append("radomiak-motor")
        block = surface["competition_blocks"][0]
        block["provider_fixture_count"] = 2
        block["extracted_fixture_ids"].append("radomiak-motor")
        with self.assertRaisesRegex(SourceCompletenessError, "FIXTURE_UNION_MISMATCH"):
            validate_source_completeness(item, now=NOW)

    def test_surface_fixture_union_must_equal_source_fixture_set(self):
        item = source()
        item["fixtures"] = []
        with self.assertRaisesRegex(SourceCompletenessError, "FIXTURE_UNION_MISMATCH"):
            validate_source_completeness(item, now=NOW)

    def test_terminal_sentinel_must_follow_main_surface_observation(self):
        item = source()
        item["source_completeness_manifest"]["terminal_sentinel"]["checked_at_utc"] = "2026-10-12T18:03:00Z"
        with self.assertRaisesRegex(SourceCompletenessError, "PRECEDES_MAIN_DATE_SURFACE"):
            validate_source_completeness(item, now=NOW)

    def test_terminal_sentinel_includes_fixture_exactly_at_requested_end(self):
        item = source()
        item["fixtures"][0]["kickoff_utc"] = END
        proof = validate_source_completeness(
            item, now=NOW, inclusive_end=True
        )
        self.assertEqual(proof["terminal_fixture_count"], 1)
        self.assertTrue(proof["window_end_inclusive"])

    def test_terminal_sentinel_is_independent_and_exact(self):
        item = source()
        item["source_completeness_manifest"]["terminal_sentinel"]["extracted_fixture_ids"] = []
        item["source_completeness_manifest"]["terminal_sentinel"]["provider_senior_fixture_count"] = 0
        with self.assertRaisesRegex(SourceCompletenessError, "SENTINEL_RECONCILIATION"):
            validate_source_completeness(item, now=NOW)
        item = source()
        item["source_completeness_manifest"]["terminal_sentinel"]["independent_refetch"] = False
        with self.assertRaisesRegex(SourceCompletenessError, "INDEPENDENT_REFETCH"):
            validate_source_completeness(item, now=NOW)

    def test_post_rebuild_stage_refuses_partial_snapshot(self):
        item = source()
        del item["source_completeness_manifest"]
        with self.assertRaisesRegex(StageError, "SOURCE_COMPLETENESS_REQUIRED"):
            sweep(item, now=NOW)

    def test_post_rebuild_stage_emits_completeness_receipt(self):
        out = sweep(source(), now=NOW)
        self.assertEqual(out["status"], "V4_SWEEP_READY")
        self.assertEqual(out["source_completeness_contract"], CONTRACT)
        self.assertEqual(out["source_completeness"]["provider_senior_fixture_union_count"], 1)
        self.assertEqual(out["source_ledger"][0]["registry_lane"], "ROUTINE")
        self.assertEqual(out["source_ledger"][0]["competition"], "Finnish Veikkausliiga")


if __name__ == "__main__":
    unittest.main()
