import hashlib
import json
import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from step0_handoff_cli import Step0HandoffError, validate_step0_handoff
from step1_fixture_intake_cli import Step1FixtureIntakeError, validate_step1_fixture_evidence
from test_step0_handoff_cli import bounded_payload
from test_step1_fixture_intake import sample


class CoordinatedIntegrityTests(unittest.TestCase):
    def test_current_run_cannot_downgrade_to_legacy(self):
        payload = bounded_payload()
        payload["run_id"] = "SWEEP-20261011-2023-20261012-0300"
        payload.pop("source_scope")
        with self.assertRaisesRegex(Step0HandoffError, "cannot omit source_scope"):
            validate_step0_handoff(payload)

    def test_future_inventory_digest_must_bind_full_fixture_list(self):
        payload = bounded_payload()
        payload["run_id"] = "SWEEP-20261012-0001-20261012-0300"
        payload["production_universe_count"] = 1
        payload["verified_fixture_inventory"] = [{
            "match_id": "m1",
            "fixture_kickoff_utc": "2026-10-10T00:00:00Z",
            "source_url": "https://league.example.org/fixture/m1",
        }]
        payload["source_payload_hash_basis"] = "VERIFIED_FULL_FIXTURE_INVENTORY_SHA256"
        payload["source_payload_hash"] = "source-seed-only"
        payload["verified_fixture_inventory_sha256"] = "source-seed-only"
        with self.assertRaisesRegex(Step0HandoffError, "SHA256 mismatch"):
            validate_step0_handoff(payload)
        digest = hashlib.sha256(json.dumps(payload["verified_fixture_inventory"],
            sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()
        payload["source_payload_hash"] = digest
        payload["verified_fixture_inventory_sha256"] = digest
        self.assertEqual(validate_step0_handoff(payload)["admitted_count"], 1)
        payload["verified_fixture_inventory"][0]["match_id"] = "DISCOVERY-1234"
        with self.assertRaisesRegex(Step0HandoffError, "provisional/duplicate"):
            validate_step0_handoff(payload)

    def test_unpriced_rank_research_remains_football_only(self):
        payload = sample()
        payload["evidence_mode"] = "FOOTBALL_ONLY"
        for key in list(payload["researched_fixture"]):
            if key.startswith("asian_total_"):
                del payload["researched_fixture"][key]
        result = validate_step1_fixture_evidence(payload)
        self.assertTrue(result["model_execution_authorized"])
        self.assertFalse(result["verified_match_specific_market"])
        self.assertFalse(result["quote_required_for_football_research"])
        self.assertEqual(result["pricing_status"], "UNOBSERVED_NOT_REQUIRED_FOR_FOOTBALL")
        payload["researched_fixture"]["xi_home_channel_source_url"] = ""
        with self.assertRaisesRegex(Step1FixtureIntakeError, "XI_HOME_PUBLISHING"):
            validate_step1_fixture_evidence(payload)

    def test_partial_odds_cannot_hide_in_unpriced_mode(self):
        payload = sample()
        payload["evidence_mode"] = "FOOTBALL_ONLY"
        with self.assertRaisesRegex(Step1FixtureIntakeError, "require PRICED_OBSERVED"):
            validate_step1_fixture_evidence(payload)


if __name__ == "__main__":
    unittest.main()
