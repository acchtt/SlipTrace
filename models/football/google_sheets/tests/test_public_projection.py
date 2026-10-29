import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "google_sheets"))

from public_projection import ProjectionError, build_projection


class PublicProjectionTests(unittest.TestCase):
    def test_safe_coverage_and_pick_projection(self):
        out = build_projection(
            [{
                "Coverage ID": "RUN|m1",
                "Run ID": "RUN",
                "Slate Date": "2026-10-15",
                "Match": "Home – Away",
                "Competition": "League",
                "Kickoff ICT": "2026-10-15T20:00:00+07:00",
                "Eligibility": "ELIGIBLE",
                "Operational Grade": "A",
                "C Board State": "C-FOCUS",
                "C Rank": 1,
                "C Supported Line": "3,5",
                "C Follow Lane": "FOLLOW",
                "Step1 Engine C Result": '{"private":"must not leak"}',
                "Payload JSON": '{"secret":"must not leak"}',
            }],
            [{
                "Publication Key": "PUB-1",
                "Match": "Home – Away",
                "Competition": "League",
                "Kickoff ICT": "2026-10-15T20:00:00+07:00",
                "C Action": "C-BET",
                "Line": 3.25,
                "Odds": 1.82,
                "Published At UTC": "2026-10-15T12:00:00Z",
                "Payload JSON": '{"secret":"must not leak"}',
            }],
            generated_at="2026-10-15T12:01:00Z",
        )
        self.assertEqual(out["sourceStore"], "GOOGLE_SHEETS")
        self.assertEqual(out["schedule"][0]["tier"], "FOCUS")
        self.assertTrue(out["schedule"][0]["isSelected"])
        self.assertEqual(out["schedule"][0]["priorityState"], "FOCUS")
        self.assertEqual(out["schedule"][0]["cSupportedLine"], 3.5)
        self.assertEqual(out["picks"][0]["pickId"], "PUB-1")
        raw = str(out)
        self.assertNotIn("Step1 Engine C Result", raw)
        self.assertNotIn("Payload JSON", raw)
        self.assertNotIn("private", raw)
        self.assertNotIn("secret", raw)

    def test_lane_mapping_is_display_only(self):
        rows = []
        for index, lane in enumerate(
            ("FOLLOW", "RESERVE", "FOCUS_UNFOLLOWED", "STOP"), start=1
        ):
            rows.append({
                "Coverage ID": f"RUN|m{index}",
                "Run ID": "RUN",
                "Match": f"H{index} – A{index}",
                "Kickoff ICT": f"2026-10-15T2{index}:00:00+07:00",
                "C Follow Lane": lane,
                "C Board State": "C-WATCH",
                "C Rank": index,
                "C Supported Line": 2.5,
            })
        out = build_projection(rows, [], generated_at="2026-10-15T12:01:00Z")
        by_lane = {row["followLane"]: row["tier"] for row in out["schedule"]}
        self.assertEqual(by_lane, {
            "FOLLOW": "FOCUS",
            "RESERVE": "WATCHLIST",
            "FOCUS_UNFOLLOWED": "WATCHLIST",
            "STOP": "PASS",
        })
        by_lane = {
            row["followLane"]: row["priorityState"] for row in out["schedule"]
        }
        self.assertEqual(by_lane, {
            "FOLLOW": "FOCUS",
            "RESERVE": "RESERVE",
            "FOCUS_UNFOLLOWED": "RESERVE",
            "STOP": "PASS",
        })

    def test_public_selected_priority_fails_closed_above_eight(self):
        rows = [{
            "Coverage ID": f"RUN|m{index}",
            "Run ID": "RUN",
            "Match": f"H{index} – A{index}",
            "Kickoff ICT": f"2026-10-15T{10 + index:02d}:00:00+07:00",
            "C Follow Lane": "FOLLOW",
            "C Rank": index,
        } for index in range(1, 10)]
        with self.assertRaisesRegex(ProjectionError, "exceeds max 8"):
            build_projection(rows, [])

    def test_selection_is_frozen_before_kickoff_display_sort(self):
        rows = [
            {
                "Coverage ID": "RUN|rank1",
                "Run ID": "RUN",
                "Match": "Later best",
                "Kickoff ICT": "2026-10-15T22:00:00+07:00",
                "C Follow Lane": "FOLLOW",
                "C Rank": 1,
            },
            {
                "Coverage ID": "RUN|rank2",
                "Run ID": "RUN",
                "Match": "Earlier second",
                "Kickoff ICT": "2026-10-15T20:00:00+07:00",
                "C Follow Lane": "FOLLOW",
                "C Rank": 2,
            },
        ]
        out = build_projection(rows, [])
        self.assertEqual(
            [row["id"] for row in out["schedule"]],
            ["RUN|rank2", "RUN|rank1"],
        )
        self.assertEqual(out["selectedCountByBoard"], {"RUN": 2})

    def test_missing_identity_fails_closed_by_omission(self):
        out = build_projection([{
            "Run ID": "RUN",
            "Match": "Home – Away",
            "Kickoff ICT": "2026-10-15T20:00:00+07:00",
            "C Follow Lane": "FOLLOW",
        }], [])
        self.assertEqual(out["schedule"], [])


if __name__ == "__main__":
    unittest.main()
