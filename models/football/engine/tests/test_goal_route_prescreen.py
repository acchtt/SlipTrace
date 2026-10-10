import copy
import pathlib
import sys
import unittest
from datetime import datetime, timedelta, timezone

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))
from goal_route_prescreen import GoalPrescreenError, run_prescreen, verified_research_order
from capacity_replenishment import CapacityReplenishmentError, next_replenishment_wave, COMPACT_POLICY

NOW = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)
NOW_ISO = NOW.isoformat()
HASH = "fnv1a32-example-20261010"


def recent(gf=0, ga=0):
    return [{
        "kickoff_utc": (NOW - timedelta(days=i + 1)).isoformat(),
        "goals_for": gf,
        "goals_against": ga,
    } for i in range(5)]


def football_evidence(high=False):
    return {
        "home": {"source_url": "https://scores.example.org/team-home",
                 "observed_at_utc": NOW_ISO, "recent": recent(3, 1) if high else recent()},
        "away": {"source_url": "https://scores.example.org/team-away",
                 "observed_at_utc": NOW_ISO, "recent": recent(2, 1) if high else recent()},
    }


def candidates(count=30):
    return [{
        "match_id": f"m{i}",
        "queue_rank": i,
        "operational_grade": "A" if i <= 20 else "B",
        "fixture_status": "PREMATCH_CONFIRMED",
        "kickoff_utc": (NOW + timedelta(hours=4)).isoformat(),
        "football_evidence": football_evidence(i == 13),
    } for i in range(1, count + 1)]


def request(rows=None):
    return {
        "schema_version": "football-goal-route-prescreen-v1",
        "run_id": "SWEEP-20261010-EXAMPLE",
        "source_payload_hash": HASH,
        "screen_at_utc": NOW_ISO,
        "candidates": rows if rows is not None else candidates(),
    }


def queue(rows):
    return [{
        "match_id": c["match_id"],
        "queue_rank": c["queue_rank"],
        "operational_grade": c["operational_grade"],
        "disposition": "ADMITTED_TO_C" if c["queue_rank"] <= 8
                       else "OPERATIONAL_CAPACITY_DEFERRED",
        "fixture_status": c["fixture_status"],
    } for c in rows]


class FullQueuePrescreenTests(unittest.TestCase):
    def test_goal_rich_rank_13_is_in_first_deep_research_wave(self):
        out = run_prescreen(request())
        self.assertEqual(out["full_ab_count"], 30)
        self.assertEqual(out["quantified_count"], 30)
        self.assertEqual(out["initial_original_step0_ranks"][0], 13)
        self.assertIn("m13", out["initial_promoted_from_step0_deferred"])
        self.assertEqual(out["initial_research_match_ids"][0], "m13")
        row = next(r for r in out["manifest"]["original_rows"] if r["match_id"] == "m13")
        self.assertEqual(row["queue_rank"], 13)
        self.assertEqual(row["screen_status"], "QUANTIFIED")

    def test_unknown_evidence_is_not_false_negative(self):
        rows = candidates(12)
        for c in rows:
            c.pop("football_evidence")
        out = run_prescreen(request(rows))
        self.assertEqual(out["quantified_count"], 0)
        self.assertEqual(out["evidence_limited_count"], 12)
        self.assertEqual(out["initial_original_step0_ranks"], list(range(1, 9)))
        self.assertTrue(all(r["priority_score"] is None for r in out["manifest"]["original_rows"]))

    def test_started_match_is_closed_not_retrospectively_scored(self):
        rows = candidates()
        rows[12]["fixture_status"] = "STARTED"
        rows[12]["kickoff_utc"] = (NOW - timedelta(minutes=4)).isoformat()
        out = run_prescreen(request(rows))
        self.assertNotIn("m13", out["initial_research_match_ids"])
        self.assertEqual(out["closed_count"], 1)

    def test_prematch_label_after_kickoff_not_researchable(self):
        rows = candidates(10)
        rows[1]["kickoff_utc"] = (NOW - timedelta(minutes=2)).isoformat()
        out = run_prescreen(request(rows))
        self.assertNotIn("m2", out["manifest"]["ordered_eligible_match_ids"])

    def test_no_future_results_leak_into_screen(self):
        rows = candidates()
        rows[12]["football_evidence"]["home"]["recent"][0]["kickoff_utc"] = (
            NOW + timedelta(minutes=1)
        ).isoformat()
        with self.assertRaisesRegex(GoalPrescreenError, "not provably finished"):
            run_prescreen(request(rows))

    def test_no_bookmaker_or_postmatch_outcomes_in_screen(self):
        for field, value in (("odds", 1.9), ("final_score", "3-3"),
                             ("pnl", 1.0), ("c_result", "BET"),
                             ("bookmaker_total", 3.5)):
            with self.subTest(field=field):
                rows = candidates(10)
                rows[0][field] = value
                with self.assertRaisesRegex(GoalPrescreenError, "forbidden"):
                    run_prescreen(request(rows))

    def test_future_or_stale_source_rejected(self):
        for shift in (timedelta(minutes=1), -timedelta(days=9)):
            with self.subTest(shift=shift):
                rows = candidates(9)
                rows[0]["football_evidence"]["home"]["observed_at_utc"] = (NOW + shift).isoformat()
                with self.assertRaisesRegex(GoalPrescreenError, "stale or from future"):
                    run_prescreen(request(rows))

    def test_duplicate_or_missing_original_queue_rank_rejected(self):
        rows = candidates(11)
        rows[3]["queue_rank"] = 13
        with self.assertRaisesRegex(GoalPrescreenError, "contiguous"):
            run_prescreen(request(rows))

    def test_imminent_kickoff_gets_time_priority(self):
        rows = candidates()
        rows[0]["kickoff_utc"] = (NOW + timedelta(minutes=45)).isoformat()
        out = run_prescreen(request(rows))
        self.assertEqual(out["initial_research_match_ids"][0], "m1")
        self.assertEqual(out["initial_research_match_ids"][1], "m13")

    def test_different_source_hash_cannot_reuse_priority(self):
        rows = candidates()
        out = run_prescreen(request(rows))
        with self.assertRaisesRegex(GoalPrescreenError, "source"):
            verified_research_order(out["manifest"], queue(rows), "different_hash")

    def test_tampered_priority_manifest_fails(self):
        rows = candidates()
        manifest = run_prescreen(request(rows))["manifest"]
        manifest["ordered_eligible_match_ids"].reverse()
        with self.assertRaisesRegex(GoalPrescreenError, "fingerprint"):
            verified_research_order(manifest, queue(rows), HASH)


class WholeQueueDeepResearchTests(unittest.TestCase):
    def setUp(self):
        self.rows = candidates()
        self.screen = run_prescreen(request(self.rows))

    def payload(self):
        return {
            "budget_policy": COMPACT_POLICY,
            "research_schedule_policy": "GOAL_FIRST_STEP1_RESEARCH_V1",
            "source_payload_hash": HASH,
            "research_priority_manifest": self.screen["manifest"],
            "research_at_utc": (NOW + timedelta(minutes=5)).isoformat(),
            "researched_match_ids": self.screen["initial_research_match_ids"],
            "follow_count": 0,
            "reserve_count": 0,
            "candidates": queue(self.rows),
        }

    def test_followup_can_include_unresearched_original_step0_admitted(self):
        out = next_replenishment_wave(self.payload())
        self.assertEqual(out["status"], "REPLENISHMENT_REQUIRED")
        self.assertEqual(len(out["selected_match_ids"]), 4)
        self.assertIn("m8", out["selected_match_ids"])
        self.assertNotIn("m13", out["selected_match_ids"])
        self.assertEqual(out["research_schedule_policy"], "GOAL_FIRST_STEP1_RESEARCH_V1")

    def test_priority_binding_rejects_missing_or_foreign_queue_member(self):
        p = self.payload()
        p["candidates"].pop()
        with self.assertRaisesRegex(CapacityReplenishmentError, "incomplete"):
            next_replenishment_wave(p)

    def test_screen_epoch_requires_refresh(self):
        p = self.payload()
        p["research_at_utc"] = (NOW + timedelta(hours=4)).isoformat()
        with self.assertRaisesRegex(CapacityReplenishmentError, "RESCREEN_REQUIRED"):
            next_replenishment_wave(p)

    def test_prospective_recheck_skips_expired_high_priority(self):
        p = self.payload()
        # rank 8 is normally next in queue but cannot be researched after KO.
        p["candidates"][7]["fixture_status"] = "STARTED"
        out = next_replenishment_wave(p)
        self.assertNotIn("m8", out["selected_match_ids"])
        self.assertIn("m8", [r["match_id"] for r in out["closed_deferred"]])

    def test_original_legacy_rank_order_remains_unchanged(self):
        p = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0, "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 9)],
            "candidates": queue(self.rows),
        }
        out = next_replenishment_wave(p)
        self.assertEqual(out["selected_queue_ranks"], [9, 10, 11, 12])
        self.assertEqual(out["research_schedule_policy"], "FROZEN_STEP0_RANK")


if __name__ == "__main__":
    unittest.main()
