"""End-to-end offline Step0 -> Step1 /rank bridge. No fake provider/Airtable calls."""
import copy
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from sweep_rank_pipeline import (
    SweepRankError, prepare, seal, execute_rank, publish_rank,
)
from test_step0_package_cli import scenario
from test_board_pair import c_row, c2_row, payload as model_payload


def preview_run():
    return {
        "schema_version": "football-sweep-rank-v3",
        "run_id": "SWEEP-20261011-2255-20261012-0300",
        "run_status": "RUNNING",
        "source_acquisition_state": "ACQUIRED",
        "source_payload_hash": "fnv1a32-test-seed",
        "at_utc": "2026-10-11T16:00:00Z",
        "window_start_utc": "2026-10-11T15:55:00Z",
        "window_end_utc": "2026-10-11T20:00:00Z",
        "coverage_blockers": ["SOURCE_VISIBLE_COMPETITION_UNVERIFIED"],
        "candidates": [{
            "match_id": f"canonical-m{i}",
            "step0_capacity_queue_rank": i,
            "operational_viability_grade": "B",
            "final_step0_disposition": (
                "ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED"
            ),
            "fixture_kickoff_utc": "2026-10-11T18:30:00Z",
            "fixture_status": "PREMATCH_CONFIRMED",
            "fixture_source_url": "https://provider.example.org/football/fixture",
            "country": "Italy",
            "competition_name": "Serie A",
        } for i in range(1, 13)],
    }


def real_zip_bundle(root):
    handoff, run_proof = scenario()
    paths = {
        "handoff": root / "STEP0_HANDOFF.json",
        "proof": root / "run_proof.json",
        "text": root / "AISCORE_FIXTURES_TEST.txt",
        "zip": root / "AISCORE_FIXTURES_TEST.zip",
    }
    paths["handoff"].write_text(json.dumps(handoff))
    paths["proof"].write_text(json.dumps(run_proof))
    paths["text"].write_text("FINAL verified Step0 historical test handoff")
    sealed = seal(paths["handoff"], paths["proof"], paths["text"], paths["zip"])
    complete_run = {
        "run_id": handoff["run_id"],
        "run_status": "COMPLETE",
        "source_payload_hash": handoff["source_payload_hash"],
        "official_zip_sha256": sealed["zip_sha256"],
    }
    cr, c2r = c_row(), c2_row()
    for r in (cr, c2r):
        r["match_id"] = "m1"
        r["kickoff_ict"] = "2026-10-10T07:00:00+07:00"
    unranked = {f"m{i}": "RESEARCH_BUDGET_EXHAUSTED" for i in range(2, 11)}
    return handoff, sealed, complete_run, model_payload("c", cr), model_payload("c2", c2r), unranked


def storage_receipt(execution):
    q = execution["execution"]
    c = q["board_pair"]["results"]["c"]["matches"][0]
    c2 = q["board_pair"]["results"]["c2"]["matches"][0]
    return {
        "schema_version": "football-step1-readback-v1",
        "run_id": q["run_id"],
        "source_payload_hash": q["source_payload_hash"],
        "active_base_id": "appbzxqXYf0lKfD4P",
        "readback_method": "INDEPENDENT_AIRTABLE_REFETCH",
        "readback_at_utc": "2026-10-09T13:00:00Z",
        "frozen_ab_queue": copy.deepcopy(q["frozen_ab_queue"]),
        "board_pair": copy.deepcopy(q["board_pair"]),
        "sweep_run_readback": {
            "run_id": q["run_id"],
            "source_payload_hash": q["source_payload_hash"],
            "run_status": "COMPLETE",
        },
        "readback_rows": [{
            "match_id": "m1",
            "coverage_id": q["run_id"] + "|m1",
            "step0_capacity_queue_rank": 1,
            "c_rank": c["rank"],
            "c_board_state": "C-" + c["board_state"],
            "c_supported_line": c["supported_line"],
            "follow_lane": c["follow_lane"],
            "c2_rank": c2["rank"],
            "c2_board_state": "C2-" + c2["board_state"],
            "c2_supported_line": c2["supported_line"],
        }],
        "unranked_reasons": dict(q["unranked_reasons"]),
        "terminal_status": {
            "complete": True, "blocked": False,
            "ranked_eligible_count": 1,
            "follow_count": q["counts"]["FOLLOW"],
            "reserve_count": q["counts"]["RESERVE"],
            "stop_count": q["counts"]["STOP"],
        },
    }


class SweepRankPipelineTests(unittest.TestCase):
    def test_early_research_queue_without_promoting_sweep_to_complete(self):
        result = prepare(preview_run())
        self.assertEqual(result["status"], "FOOTBALL_RESEARCH_PREPARED_UNOFFICIAL")
        self.assertEqual(result["source_backed_queue_count"], 12)
        self.assertEqual(len(result["initial_wave"]), 8)
        self.assertEqual(len(result["standard_research_order"]), 12)
        self.assertTrue(result["coverage_blockers"])
        self.assertFalse(result["official_rank_authorized"])
        self.assertTrue(result["no_bet"])

    def test_prepare_rejects_ambiguous_or_expired_or_unverified_fixtures(self):
        p = preview_run()
        p["run_status"] = "BLOCKED"
        with self.assertRaisesRegex(SweepRankError, "RUNNING"):
            prepare(p)
        p = preview_run()
        p["candidates"][0]["match_id"] = "DISCOVERY-hash"
        with self.assertRaisesRegex(SweepRankError, "canonical unique"):
            prepare(p)
        p = preview_run()
        p["candidates"][0]["fixture_source_url"] = ""
        with self.assertRaisesRegex(SweepRankError, "source URL"):
            prepare(p)
        p = preview_run()
        p["candidates"][0]["fixture_kickoff_utc"] = "2026-10-10T18:30:00Z"
        with self.assertRaisesRegex(SweepRankError, "outside frozen"):
            prepare(p)
        p = preview_run()
        p["candidates"][9]["step0_capacity_queue_rank"] = 12
        with self.assertRaisesRegex(SweepRankError, "queue rank"):
            prepare(p)

    def test_one_pipeline_real_zip_c2_pair_and_publication_readback(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            _, sealed, sweep, c, c2, unranked = real_zip_bundle(root)
            self.assertTrue((root / "AISCORE_FIXTURES_TEST.zip").exists())
            self.assertEqual(sealed["status"], "STEP0_OFFICIAL_ZIP_VERIFIED")
            ranked = execute_rank(root / "AISCORE_FIXTURES_TEST.zip",
                                  sealed["zip_sha256"], sweep, c, c2, unranked,
                                  at_utc="2026-10-09T12:00:00Z")
            self.assertEqual(ranked["status"], "C_C2_EXECUTED_AWAITING_INDEPENDENT_AIRTABLE_READBACK")
            self.assertEqual(ranked["models_executed"], ["c", "c2"])
            self.assertFalse(ranked["official_publication_authorized"])
            receipt = storage_receipt(ranked)
            confirmed = publish_rank(ranked, receipt)
            self.assertEqual(confirmed["status"], "C_C2_RANKED_READBACK_VERIFIED")
            self.assertEqual(confirmed["ranked_count"], 1)
            self.assertFalse(confirmed["website_published"])

    def test_missing_sweep_readback_and_wrong_zip_sha_are_terminal(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            _, sealed, sweep, c, c2, unranked = real_zip_bundle(root)
            archive = root / "AISCORE_FIXTURES_TEST.zip"
            with self.assertRaisesRegex(SweepRankError, "SHA256 mismatch"):
                execute_rank(archive, "f" * 64, sweep, c, c2, unranked,
                             at_utc="2026-10-09T12:00:00Z")
            sweep["run_status"] = "RUNNING"
            with self.assertRaisesRegex(SweepRankError, "COMPLETE readback"):
                execute_rank(archive, sealed["zip_sha256"], sweep, c, c2, unranked,
                             at_utc="2026-10-09T12:00:00Z")

    def test_retroactive_rank_and_unranked_missing_block(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            _, sealed, sweep, c, c2, unranked = real_zip_bundle(root)
            archive = root / "AISCORE_FIXTURES_TEST.zip"
            with self.assertRaisesRegex(SweepRankError, "retrospective"):
                execute_rank(archive, sealed["zip_sha256"], sweep, c, c2, unranked,
                             at_utc="2026-10-11T12:00:00Z")
            unranked.pop("m2")
            with self.assertRaisesRegex(SweepRankError, "reason required"):
                execute_rank(archive, sealed["zip_sha256"], sweep, c, c2, unranked,
                             at_utc="2026-10-09T12:00:00Z")

    def test_c2_drift_and_false_airtable_readback_block_publication(self):
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            _, sealed, sweep, c, c2, unranked = real_zip_bundle(root)
            archive = root / "AISCORE_FIXTURES_TEST.zip"
            c2["matches"][0]["chance_quality"] = "LOW"
            with self.assertRaisesRegex(ValueError, "COMMON EVIDENCE DRIFT"):
                execute_rank(archive, sealed["zip_sha256"], sweep, c, c2, unranked,
                             at_utc="2026-10-09T12:00:00Z")
            c2["matches"][0]["chance_quality"] = c["matches"][0]["chance_quality"]
            result = execute_rank(archive, sealed["zip_sha256"], sweep, c, c2, unranked,
                                  at_utc="2026-10-09T12:00:00Z")
            receipt = storage_receipt(result)
            receipt["readback_rows"][0]["c_rank"] = 15
            with self.assertRaises(ValueError):
                publish_rank(result, receipt)
            receipt = storage_receipt(result)
            receipt["board_pair"]["results"]["c"]["matches"][0]["rank"] = 20
            with self.assertRaisesRegex(SweepRankError, "same executed"):
                publish_rank(result, receipt)


if __name__ == "__main__":
    unittest.main()
