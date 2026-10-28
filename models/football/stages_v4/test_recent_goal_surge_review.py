"""Prospective Gamba-style goal-signal false negative replay, research-only.

Frozen 28-Oct 09:20 UTC source must replay under the legacy screen; a future
kickoff with the *same* historical form may enter C research as GOAL_REVIEW.
"""
import copy
import unittest
from discovery_goal_gate import screen_discovery


def fixture(home_scores, away_scores, *, observed):
    days = [24, 21, 17, 13, 9, 7, 5, 3, 2, 1]
    def team(scores, side):
        return {
            "source_url": "https://example.org/" + side,
            "observed_at_utc": observed,
            "recent": [
                {
                    "kickoff_utc": f"2026-10-{days[i]:02d}T05:00:00Z",
                    "goals_for": gf,
                    "goals_against": ga,
                }
                for i, (gf, ga) in enumerate(scores)
            ],
        }
    return {
        "match_id": "gamba-test",
        "kickoff_utc": "2026-10-29T10:00:00+00:00",
        "home": "Control A",
        "away": "Control B",
        "football_evidence": {
            "home": team(home_scores, "home"),
            "away": team(away_scores, "away"),
        },
    }


# Same 10 home / 8 away scores preserved in the sealed 28-Oct source.
GAMBA = [(2,2),(2,1),(2,2),(3,1),(0,2),(5,0),(0,1),(4,1),(0,2),(0,2)]
BURIRAM = [(2,3),(1,0),(0,1),(3,2),(1,0),(1,1),(1,1),(3,1)]
KASHIMA = [(2,3),(2,2),(2,0),(1,0),(2,0),(3,1),(3,3),(7,1),(1,2),(0,1)]
POHANG = [(2,2),(0,0),(0,2),(0,3),(2,1),(1,3),(2,2),(0,0),(0,2),(0,0)]


class RecentGoalReviewBoundary(unittest.TestCase):
    def screen(self, fixt, at):
        return screen_discovery(
            run_id="V4-TEST-GAMBA",
            source_payload_hash="a" * 64,
            at_utc=at,
            fixture=fixt,
        )

    def test_gamba_legacy_before_effective_remains_watch_with_original_fingerprint(self):
        row = fixture(GAMBA, BURIRAM, observed="2026-10-28T09:20:00Z")
        got = self.screen(row, "2026-10-28T09:20:33Z")
        self.assertEqual(got["status"], "WATCH_GOAL_SIGNAL")
        self.assertEqual(got["priority_score"], 47)
        self.assertEqual(got["mean_over_two_rate"], 0.4875)
        self.assertEqual(got["carrier_route"], 1.4625)
        self.assertNotIn("recency_research_review", got)

    def test_same_prior_form_qualifies_for_future_research_not_bet(self):
        row = fixture(GAMBA, BURIRAM, observed="2026-10-28T10:04:00Z")
        got = self.screen(row, "2026-10-28T10:06:00Z")
        self.assertEqual(got["status"], "DISCOVERY_GOAL_REVIEW")
        self.assertEqual(got["reason"], "SOURCE_BACKED_RECENT_G3_FORM_REVIEW")
        self.assertEqual(got["qualification_path"],
                         "RECENT_4_MATCH_2PLUS_CARRIER_SECOND_ROUTE_REVIEW")
        evidence = got["recency_research_review"]
        self.assertFalse(evidence["production_certificate_authority"])
        self.assertEqual(evidence["recent_four"]["home"]["total_3plus_count"], 4)
        self.assertEqual(evidence["recent_four"]["away"]["total_3plus_count"], 2)

    def test_kashima_existing_borderline_review_remains_review(self):
        row = fixture(KASHIMA, POHANG, observed="2026-10-28T10:04:00Z")
        got = self.screen(row, "2026-10-28T10:06:00Z")
        self.assertEqual(got["status"], "DISCOVERY_GOAL_REVIEW")
        self.assertEqual(got["qualification_path"], "NEAR_CUTOFF_CARRIER_SECONDARY_REVIEW")
        self.assertNotIn("recency_research_review", got)

    def test_started_match_never_reopened_at_new_effective_epoch(self):
        row = fixture(GAMBA, BURIRAM, observed="2026-10-28T10:04:00Z")
        row["kickoff_utc"] = "2026-10-28T10:00:00Z"
        got = self.screen(row, "2026-10-28T10:06:00Z")
        self.assertEqual(got["status"], "WATCH_GOAL_SIGNAL")

    def test_recent_one_sided_goal_facts_not_enough(self):
        row = fixture(GAMBA, [(0,0),(1,0),(0,1),(1,1)], observed="2026-10-28T10:04:00Z")
        got = self.screen(row, "2026-10-28T10:06:00Z")
        self.assertEqual(got["status"], "WATCH_GOAL_SIGNAL")


if __name__ == "__main__":
    unittest.main()
