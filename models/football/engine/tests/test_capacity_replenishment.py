import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from capacity_replenishment import (  # noqa: E402
    CapacityReplenishmentError,
    next_replenishment_wave,
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


if __name__ == "__main__":
    unittest.main()
