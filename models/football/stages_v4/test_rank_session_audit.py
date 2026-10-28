"""Regression tests for deadline accounting and rank-to-rank continuity."""
import unittest
from rank_session_audit import prematch_opportunity, rank_transitions


class PrematchDeadlineTests(unittest.TestCase):
    def setUp(self):
        self.queue = {
            "early": {"kickoff_utc": "2026-10-26T13:30:00+00:00"},
            "retained": {"kickoff_utc": "2026-10-26T17:00:00+00:00"},
            "open": {"kickoff_utc": "2026-10-26T19:00:00+00:00"},
        }

    def test_closed_candidate_without_prematch_assessment_is_not_covered(self):
        prior = {
            "rank_at_utc": "2026-10-26T10:45:00+00:00",
            "frozen_model_input": {"matches": [{"match_id": "retained"}]},
        }
        got = prematch_opportunity(
            self.queue, now="2026-10-26T15:09:22+00:00",
            current_ids=set(), previous_rank=prior,
        )
        self.assertEqual(got["never_assessed_before_kickoff_count"], 1)
        self.assertEqual(got["ever_prematch_assessed_count"], 1)
        self.assertEqual(got["open_unassessed_count"], 1)
        states = {r["match_id"]: r for r in got["manifest"]}
        self.assertEqual(states["early"]["deadline_state"], "PREMATCH_RESEARCH_MISSED")
        self.assertEqual(states["retained"]["deadline_state"], "PREMATCH_C_ASSESSED")
        self.assertEqual(got["priority_open_match_ids"], ["open"])

    def test_later_timestamp_cannot_backfill_closed_fixture(self):
        prior = {
            "rank_at_utc": "2026-10-26T17:01:00+00:00",
            "frozen_model_input": {"matches": [{"match_id": "retained"}]},
        }
        got = prematch_opportunity(
            self.queue, now="2026-10-26T18:00:00+00:00",
            current_ids=set(), previous_rank=prior,
        )
        self.assertIn(
            "retained", [r["match_id"] for r in got["manifest"]
                         if r["deadline_state"] == "PREMATCH_RESEARCH_MISSED"]
        )

    def test_first_timestamp_remains_frozen_across_resumes(self):
        original = prematch_opportunity(
            self.queue, now="2026-10-26T12:00:00+00:00",
            current_ids={"early", "retained"}, previous_rank=None,
        )
        prior = {
            "prematch_opportunity_manifest": original["manifest"],
            "rank_at_utc": "2026-10-26T12:00:00+00:00",
        }
        resumed = prematch_opportunity(
            self.queue, now="2026-10-26T16:00:00+00:00",
            current_ids=set(), previous_rank=prior,
        )
        early = next(x for x in resumed["manifest"] if x["match_id"] == "early")
        self.assertEqual(early["first_C_assessed_at_utc"], "2026-10-26T12:00:00+00:00")
        self.assertEqual(resumed["never_assessed_before_kickoff_count"], 0)


class RerankTransitionTests(unittest.TestCase):
    def test_rizespor_demoted_and_geylang_closed_are_preserved(self):
        previous = {"research_assessment": {"matches": [
            {"match_id": "rize", "follow_lane": "FOLLOW", "supported_line": 2.5, "rank": 1},
            {"match_id": "gey", "follow_lane": "FOLLOW", "supported_line": 2.5, "rank": 2},
        ]}}
        current = [
            {"match_id": "rize", "follow_lane": "RESERVE", "supported_line": 2.5, "rank": 4},
            {"match_id": "new", "follow_lane": "FOLLOW", "supported_line": 3.5, "rank": 2},
        ]
        rows = rank_transitions(current, previous_rank=previous, coverage_manifest=[
            {"match_id": "gey", "disposition": "STATUS_EXCLUDED"},
            {"match_id": "rize", "disposition": "C_ASSESSED"},
        ])
        m = {x["match_id"]: x for x in rows}
        self.assertEqual(m["rize"]["transition"], "DEMOTED")
        self.assertTrue(m["rize"]["prior_follow_history_preserved"])
        self.assertEqual(m["gey"]["transition"], "CLOSED")
        self.assertTrue(m["gey"]["prior_follow_history_preserved"])
        self.assertEqual(m["new"]["transition"], "NEW")


if __name__ == "__main__":
    unittest.main()
