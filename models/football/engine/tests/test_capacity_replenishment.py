import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from capacity_replenishment import (  # noqa: E402
    CapacityReplenishmentError,
    COMPACT_POLICY,
    next_replenishment_wave,
    select_initial_work_wave,
)


def row(match_id, rank, status="PREMATCH_CONFIRMED", disposition="OPERATIONAL_CAPACITY_DEFERRED", grade="A"):
    return {
        "match_id": match_id,
        "queue_rank": rank,
        "operational_grade": grade,
        "fixture_status": status,
        "disposition": disposition,
    }


class CapacityReplenishmentTests(unittest.TestCase):
    def test_selects_lowest_queue_ranks_for_vacancies(self):
        result = next_replenishment_wave(
            {
                "follow_count": 2,
                "reserve_count": 1,
                "candidates": [
                    row("late", 20),
                    row("first", 16),
                    row("second", 17),
                    row("third", 18),
                    row("fourth", 19),
                    row("fifth", 21),
                    row("sixth", 22),
                    row("seventh", 23),
                    row("eighth", 24),
                ],
            }
        )
        self.assertEqual(result["vacancies"], 7)
        self.assertEqual(
            result["selected_queue_ranks"],
            [16, 17, 18, 19, 20, 21, 22],
        )

    def test_full_active_capacity_selects_none(self):
        result = next_replenishment_wave(
            {
                "follow_count": 6,
                "reserve_count": 4,
                "candidates": [row("x", 16)],
            }
        )
        self.assertEqual(result["status"], "ACTIVE_LANE_CAPACITY_FULL")
        self.assertEqual(result["selected_match_ids"], [])

    def test_started_candidate_is_skipped_without_jumping_order_bug(self):
        result = next_replenishment_wave(
            {
                "follow_count": 5,
                "reserve_count": 3,
                "candidates": [
                    row("started", 16, status="STARTED"),
                    row("next", 17),
                    row("after", 18),
                ],
            }
        )
        self.assertEqual(result["selected_match_ids"], ["next", "after"])
        self.assertEqual(result["closed_deferred"][0]["match_id"], "started")

    def test_duplicate_queue_rank_fails(self):
        with self.assertRaisesRegex(
            CapacityReplenishmentError,
            "duplicate Step0 Capacity Queue Rank",
        ):
            next_replenishment_wave(
                {
                    "follow_count": 0,
                    "reserve_count": 0,
                    "candidates": [row("a", 16), row("b", 16)],
                }
            )

    def test_non_ab_candidate_fails(self):
        with self.assertRaisesRegex(
            CapacityReplenishmentError,
            "capacity queue accepts A/B only",
        ):
            next_replenishment_wave(
                {
                    "follow_count": 0,
                    "reserve_count": 0,
                    "candidates": [row("bad", 16, grade="C")],
                }
            )


class CompactCapacityTests(unittest.TestCase):
    def test_compact_initial_wave_eight_and_full_queue_retained(self):
        queue = [row(f"m{i}", i) for i in range(1, 20)]
        result = select_initial_work_wave(queue, budget_policy=COMPACT_POLICY)
        self.assertEqual(result["admitted_queue_ranks"], list(range(1, 9)))
        self.assertEqual(result["deferred_queue_ranks"], list(range(9, 20)))
        self.assertEqual(result["full_queue_count"], 19)

    def test_legacy_initial_wave_is_fifteen(self):
        result = select_initial_work_wave([row(f"m{i}", i) for i in range(1, 18)])
        self.assertEqual(result["admitted_queue_ranks"], list(range(1, 16)))
        self.assertEqual(result["deferred_queue_ranks"], [16, 17])

    def test_compact_stops_at_four_active(self):
        result = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 2,
            "reserve_count": 2,
            "researched_match_ids": [f"m{i}" for i in range(1, 9)],
            "candidates": [row(f"m{i}", i, disposition=("ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED")) for i in range(1, 20)],
        })
        self.assertEqual(result["status"], "COMPACT_ACTIVE_TARGET_SATISFIED")
        self.assertEqual(result["selected_match_ids"], [])

    def test_four_reserves_zero_follow_does_not_stop_at_nine(self):
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 4,
            "researched_match_ids": [f"m{i}" for i in range(1, 10)],
            "candidates": [
                row(f"m{i}", i, disposition=(
                    "ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED"
                )) for i in range(1, 31)
            ],
        })
        self.assertEqual(out["status"], "REPLENISHMENT_REQUIRED")
        self.assertEqual(out["selected_queue_ranks"], [10, 11, 12])
        self.assertFalse(out["compact_follow_target_met"])

    def test_one_follow_three_reserves_still_satisfies_four_active(self):
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 1,
            "reserve_count": 3,
            "researched_match_ids": [f"m{i}" for i in range(1, 9)],
            "candidates": [row(f"m{i}", i) for i in range(1, 20)],
        })
        self.assertEqual(out["status"], "COMPACT_ACTIVE_TARGET_SATISFIED")
        self.assertEqual(out["selected_queue_ranks"], [])
        self.assertTrue(out["compact_follow_target_met"])

    def test_reserve_only_after_twelve_requires_verified_adaptive_time(self):
        base = [row(f"m{i}", i) for i in range(1, 31)]
        p = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 4,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": base,
        }
        without_time = next_replenishment_wave(p)
        self.assertEqual(without_time["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")
        self.assertEqual(without_time["selected_match_ids"], [])
        p["adaptive_research"] = {
            "enabled": True,
            "available_research_minutes": 110,
            "next_candidate_kickoff_minutes": 150,
        }
        with_time = next_replenishment_wave(p)
        self.assertEqual(with_time["status"], "REPLENISHMENT_REQUIRED")
        self.assertEqual(with_time["selected_queue_ranks"], [13])
        self.assertEqual(with_time["research_budget_limit"], 20)

    def test_compact_refills_four_when_no_active(self):
        result = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 9)],
            "candidates": [row(f"m{i}", i, disposition=("ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED")) for i in range(1, 20)],
        })
        self.assertEqual(result["selected_queue_ranks"], [9, 10, 11, 12])
        self.assertEqual(result["research_budget_remaining"], 4)

    def test_compact_budget_exhaustion_is_not_unbounded_replenishment(self):
        result = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": [row(f"m{i}", i, disposition=("ADMITTED_TO_C" if i <= 12 else "OPERATIONAL_CAPACITY_DEFERRED")) for i in range(1, 20)],
        })
        self.assertEqual(result["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")
        self.assertEqual(result["selected_match_ids"], [])

    def test_compact_rejects_missing_history_and_duplicates(self):
        data = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "candidates": [row(f"m{i}", i) for i in range(1, 12)],
        }
        with self.assertRaisesRegex(CapacityReplenishmentError, "researched_match_ids"):
            next_replenishment_wave(data)
        data["researched_match_ids"] = ["m1", "m1"]
        with self.assertRaisesRegex(CapacityReplenishmentError, "duplicate"):
            next_replenishment_wave(data)
        data["researched_match_ids"] = ["unknown"]
        with self.assertRaisesRegex(CapacityReplenishmentError, "missing from frozen queue"):
            next_replenishment_wave(data)

    def test_initial_wave_rejects_noncontiguous_rank(self):
        with self.assertRaisesRegex(CapacityReplenishmentError, "contiguous"):
            select_initial_work_wave([row("a", 1), row("b", 3)], budget_policy=COMPACT_POLICY)

    def test_underfilled_large_board_extends_beyond_rank_twelve_in_original_order(self):
        base = [row(f"m{i}", i, disposition=("ADMITTED_TO_C" if i <= 8 else "OPERATIONAL_CAPACITY_DEFERRED")) for i in range(1, 28)]
        epoch = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 1,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": base,
            "adaptive_research": {
                "enabled": True,
                "available_research_minutes": 110,
                "next_candidate_kickoff_minutes": 150,
            },
        }
        first = next_replenishment_wave(epoch)
        self.assertEqual(first["research_budget_limit"], 20)
        self.assertEqual(first["adaptive_budget_reason"], "ADAPTIVE_TIME_VERIFIED")
        self.assertEqual(first["selected_queue_ranks"], [13])
        epoch["researched_match_ids"] += first["selected_match_ids"]
        second = next_replenishment_wave(epoch)
        self.assertEqual(second["selected_queue_ranks"], [14])
        self.assertEqual(second["research_budget_remaining"], 7)

    def test_partial_standard_wave_cannot_cross_twelve_even_with_adaptive_time(self):
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 11)],
            "candidates": [row(f"m{i}", i) for i in range(1, 23)],
            "adaptive_research": {
                "enabled": True,
                "available_research_minutes": 240,
                "next_candidate_kickoff_minutes": 300,
            },
        })
        self.assertEqual(out["selected_queue_ranks"], [11, 12])
        self.assertEqual(out["research_budget_limit"], 20)

    def test_no_adaptive_data_preserves_twelve_limit(self):
        queue = [row(f"m{i}", i) for i in range(1, 22)]
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": queue,
        })
        self.assertEqual(out["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")
        self.assertEqual(out["research_budget_limit"], 12)
        self.assertEqual(out["selected_match_ids"], [])

    def test_early_kickoff_or_no_research_time_blocks_extension(self):
        queue = [row(f"m{i}", i) for i in range(1, 22)]
        for budget, until in ((100, 30), (0, 140), (50, 39)):
            with self.subTest(budget=budget, until=until):
                out = next_replenishment_wave({
                    "budget_policy": COMPACT_POLICY,
                    "follow_count": 0,
                    "reserve_count": 0,
                    "researched_match_ids": [f"m{i}" for i in range(1, 13)],
                    "candidates": queue,
                    "adaptive_research": {
                        "enabled": True,
                        "available_research_minutes": budget,
                        "next_candidate_kickoff_minutes": until,
                    },
                })
                self.assertEqual(out["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")
                self.assertEqual(out["research_budget_limit"], 12)

    def test_adaptive_never_exceeds_twenty_even_with_many_matches(self):
        queue = [row(f"m{i}", i) for i in range(1, 31)]
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 21)],
            "candidates": queue,
            "adaptive_research": {
                "enabled": True,
                "available_research_minutes": 300,
                "next_candidate_kickoff_minutes": 400,
            },
        })
        self.assertEqual(out["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")
        self.assertEqual(out["research_budget_limit"], 20)

    def test_four_active_lanes_prevent_adaptive_overresearch(self):
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 2,
            "reserve_count": 2,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": [row(f"m{i}", i) for i in range(1, 24)],
            "adaptive_research": {
                "enabled": True,
                "available_research_minutes": 180,
                "next_candidate_kickoff_minutes": 300,
            },
        })
        self.assertEqual(out["status"], "COMPACT_ACTIVE_TARGET_SATISFIED")
        self.assertEqual(out["selected_match_ids"], [])

    def test_adaptive_skips_started_but_never_reranks_by_goal_potential(self):
        queue = [row(f"m{i}", i, status=("STARTED" if i == 13 else "PREMATCH_CONFIRMED")) for i in range(1, 24)]
        out = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": queue,
            "adaptive_research": {
                "enabled": True,
                "available_research_minutes": 48,
                "next_candidate_kickoff_minutes": 110,
            },
        })
        self.assertEqual(out["selected_queue_ranks"], [14])
        self.assertIn("m13", [x["match_id"] for x in out["closed_deferred"]])

    def test_adaptive_kickoff_rechecked_for_each_next_candidate(self):
        queue = [row(f"m{i}", i) for i in range(1, 22)]
        payload = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": queue,
            "adaptive_research": {
                "enabled": True, "available_research_minutes": 80,
                "next_candidate_kickoff_minutes": 110,
            },
        }
        first = next_replenishment_wave(payload)
        self.assertEqual(first["selected_queue_ranks"], [13])
        payload["researched_match_ids"].append("m13")
        # Even with ample research time, rank 14's earlier kickoff closes
        # the adaptive window; do not skip ahead to cherry-pick rank 15.
        payload["adaptive_research"]["next_candidate_kickoff_minutes"] = 28
        second = next_replenishment_wave(payload)
        self.assertEqual(second["selected_match_ids"], [])
        self.assertEqual(second["status"], "COMPACT_RESEARCH_BUDGET_EXHAUSTED")

    def test_adaptive_payload_requires_real_time_evidence_shape(self):
        base = {
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 0,
            "researched_match_ids": [f"m{i}" for i in range(1, 13)],
            "candidates": [row(f"m{i}", i) for i in range(1, 20)],
        }
        for option in (True, {"enabled": True}, {
            "enabled": True, "available_research_minutes": True,
            "next_candidate_kickoff_minutes": 120,
        }):
            with self.subTest(option=option):
                with self.assertRaises(CapacityReplenishmentError):
                    next_replenishment_wave({**base, "adaptive_research": option})

    def test_compact_researched_candidate_is_not_reselected(self):
        result = next_replenishment_wave({
            "budget_policy": COMPACT_POLICY,
            "follow_count": 0,
            "reserve_count": 1,
            "researched_match_ids": ["m1"],
            "candidates": [row(f"m{i}", i) for i in range(1, 8)],
        })
        self.assertEqual(result["selected_queue_ranks"], [2, 3, 4, 5])




if __name__ == "__main__":
    unittest.main()
