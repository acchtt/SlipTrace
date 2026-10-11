"""Regression for V2 source-scoped handoff / women's parity / Work ZIP."""
import copy
import json
import pathlib
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from step0_handoff_cli import Step0HandoffError, validate_step0_handoff
from step0_package_cli import package as create_package
from test_step0_package_cli import scenario

WINDOW = {
    "start_utc": "2026-10-11T15:00:00Z",
    "end_utc": "2026-10-11T20:00:00Z",
}


def ready_v2():
    p, run = scenario()
    p["run_id"] = "SWEEP-20261011-2200-20261012-0300"
    p["verification_policy"] = "FAST_FINISH_V2"
    p["requested_window"] = dict(WINDOW)
    p["women_coverage_scope"] = "BOUNDED_DISCOVERED_BLOCKS"
    p["women_top_flight_seed_fixture_ids"] = []
    p["women_top_flight_source_checks"] = [
        {
            "source_family": "WOMENS_LEAGUE_OFFICIAL",
            "source_url": "https://league.example.org/womens/fixtures",
            "checked_at_utc": "2026-10-11T15:06:00Z",
            "status": "OPENED_WINDOW_VERIFIED",
            "scope": "SENIOR_WOMENS_TOPFLIGHT",
            "requested_window": dict(WINDOW),
            "visible_fixture_ids": [],
        },
        {
            "source_family": "INDEPENDENT_WOMENS_PROVIDER",
            "source_url": "https://provider.example.org/womens/fixtures",
            "checked_at_utc": "2026-10-11T15:07:00Z",
            "status": "OPENED_WINDOW_VERIFIED",
            "scope": "SENIOR_WOMENS_TOPFLIGHT",
            "requested_window": dict(WINDOW),
            "visible_fixture_ids": [],
        },
    ]
    p["women_top_flight_disposition_manifest"] = []
    for field in (
        "women_top_flight_raw_count",
        "women_top_flight_admitted_count",
        "women_top_flight_capacity_deferred_count",
        "women_top_flight_operational_excluded_count",
        "women_top_flight_researchability_excluded_count",
        "women_top_flight_unresolved_count",
    ):
        p[field] = 0
    run["run_id"] = p["run_id"]
    return p, run


class FastV2HandoffTests(unittest.TestCase):
    def test_bounded_two_family_negative_womens_checks_can_export_without_global_claim(self):
        p, run = ready_v2()
        for consumer in ("rank", "export"):
            out = validate_step0_handoff(p, consumer=consumer)
            self.assertEqual(out["step0_handoff_validation_status"], "PASS")
        self.assertFalse(p["global_raw_exact"])
        self.assertEqual(p["source_scope"], "BOUNDED_PRODUCTION_DISCOVERY")

    def test_missing_womens_source_proof_blocks_real_handoff(self):
        p, _ = ready_v2()
        p.pop("women_top_flight_source_checks")
        with self.assertRaisesRegex(Step0HandoffError, "two independent"):
            validate_step0_handoff(p)

    def test_unverified_womens_global_completeness_cannot_be_claimed(self):
        p, _ = ready_v2()
        p["women_coverage_scope"] = "GLOBAL_AISCORE_COMPLETE"
        with self.assertRaisesRegex(Step0HandoffError, "BOUNDED_DISCOVERED_BLOCKS"):
            validate_step0_handoff(p)

    def test_source_surfaced_womens_fixture_cannot_disappear(self):
        p, _ = ready_v2()
        p["women_top_flight_source_checks"][0]["visible_fixture_ids"] = ["canonical-w1"]
        with self.assertRaisesRegex(Step0HandoffError, "surface"):
            validate_step0_handoff(p)

    def test_womens_source_fixture_can_be_included_with_real_disposition(self):
        p, _ = ready_v2()
        p["women_top_flight_source_checks"][0]["visible_fixture_ids"] = ["canonical-w1"]
        p["women_top_flight_seed_fixture_ids"] = ["canonical-w1"]
        p["women_top_flight_disposition_manifest"] = [{
            "match_id": "canonical-w1",
            "competition_name": "Women's Senior Top Flight",
            "kickoff_ict": "2026-10-12T02:30:00+07:00",
            "disposition": "RESEARCHABILITY_EXCLUDED",
        }]
        p["women_top_flight_raw_count"] = 1
        p["women_top_flight_researchability_excluded_count"] = 1
        out = validate_step0_handoff(p)
        self.assertEqual(out["step0_handoff_validation_status"], "PASS")
        p["women_top_flight_researchability_excluded_count"] = 0
        with self.assertRaisesRegex(Step0HandoffError, "counter mismatch"):
            validate_step0_handoff(p)

    def test_unresolved_source_or_legacy_zip_protection_still_blocks(self):
        p, _ = ready_v2()
        p["terminal_unresolved_verification_blocks"] = ["LATE_FIXTURE_SOURCE"]
        with self.assertRaisesRegex(Step0HandoffError, "FAST FINISH UNRESOLVED"):
            validate_step0_handoff(p)

    def test_v2_actual_packager_retains_readback_admission_proof(self):
        p, run = ready_v2()
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            handoff = root / "STEP0_HANDOFF.json"
            text = root / "AISCORE_FIXTURES_TEST.txt"
            proof = root / "sweep_run_proof.json"
            output = root / "AISCORE_FIXTURES_TEST.zip"
            handoff.write_text(json.dumps(p))
            proof.write_text(json.dumps(run))
            text.write_text("SOURCE-RECONCILED BOUNDED HANDOFF")
            out = create_package(handoff, text, proof, output)
            self.assertEqual(out["status"], "STEP0 WORK ZIP VALIDATED")
            output.unlink()
            run["admitted_dispositions"]["m1"] = "UNRESOLVED"
            proof.write_text(json.dumps(run))
            with self.assertRaisesRegex(Step0HandoffError, "still provisional"):
                create_package(handoff, text, proof, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
