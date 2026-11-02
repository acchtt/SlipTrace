import unittest

from selection_discrimination import (
    POLICY,
    requires_borderline_recheck,
    review_borderline_recheck,
)


def raw():
    return {
        "match_id": "candidate",
        "material_suppression": False,
        "failure_attacks_route": False,
        "home_route": "STRONG",
        "away_route": "USABLE",
        "carrier": "USABLE",
        "route_reliability": "MEDIUM",
        "chance_quality": "MEDIUM",
        "failure_resistance": "MEDIUM",
        "burden_protection": "MEDIUM",
        "burden_completion_quality": "MEDIUM",
        "continuation_quality": "MEDIUM",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "MEDIUM",
    }


def compiled(state="WATCH"):
    return {
        "match_id": "candidate",
        "board_state": state,
        "operational_viability_grade": "A",
    }


class SelectionDiscriminationTests(unittest.TestCase):
    def test_strong_plus_usable_all_medium_watch_requires_recheck(self):
        self.assertTrue(requires_borderline_recheck(raw(), compiled()))

    def test_grade_b_strong_route_watch_also_requires_recheck(self):
        row = raw()
        out = compiled()
        out["operational_viability_grade"] = "B"
        self.assertTrue(requires_borderline_recheck(row, out))

    def test_focus_never_enters_borderline_negative_recheck(self):
        self.assertFalse(requires_borderline_recheck(raw(), compiled("FOCUS")))

    def test_two_merely_usable_routes_do_not_trigger_this_narrow_gate(self):
        row = raw()
        row["home_route"] = "USABLE"
        self.assertFalse(requires_borderline_recheck(row, compiled()))

    def test_low_axis_is_not_laundered_into_borderline_gate(self):
        row = raw()
        row["chance_quality"] = "LOW"
        self.assertFalse(requires_borderline_recheck(row, compiled()))

    def test_hard_veto_does_not_trigger_research_rescue(self):
        row = raw()
        row["material_suppression"] = True
        self.assertFalse(requires_borderline_recheck(row, compiled()))

    def test_missing_recheck_is_pending(self):
        result = review_borderline_recheck(raw(), compiled())
        self.assertEqual(result["status"], "PENDING")
        self.assertIn("selection_recheck", result["missing_fields"])
        self.assertTrue(result["no_automatic_promotion"])

    def test_substantive_source_backed_recheck_completes(self):
        row = raw()
        row["selection_recheck"] = {
            "contract": POLICY,
            "completed": True,
            "market_independent": True,
            "evidence_refs": [
                "https://club.example/match-preview",
                "https://league.example/team-news",
            ],
            "missing_goal3_requirement": (
                "No independently verified carrier self-fund or HIGH reply-quality "
                "fact remains after the second pass."
            ),
            "resolution": "CONFIRMED_REVIEW_ONLY",
            "conclusions": {
                "primary_goal3_path": (
                    "The primary side retains a strong current scoring route, but "
                    "the evidence does not independently establish three goals alone."
                ),
                "reply_or_independent_completion": (
                    "The opponent reply remains usable through current starters, "
                    "without enough distinct evidence to upgrade reply reliability."
                ),
                "stall_0_0_1_1_2_0": (
                    "A 1-1 or 2-0 stop remains materially credible because neither "
                    "side has verified continuation beyond the second goal."
                ),
                "continuation_after_second_goal": (
                    "Continuation after goal two is supported only at MEDIUM by "
                    "current comparable matches and available attacking replacements."
                ),
                "principal_failure": (
                    "The main failure is a strong primary route producing twice while "
                    "the usable reply fails to convert its limited current chances."
                ),
                "grade_reconciliation": (
                    "The second pass found no source-backed reason to lift completion, "
                    "continuation, route reliability or chance creation above MEDIUM."
                ),
            },
        }
        result = review_borderline_recheck(row, compiled())
        self.assertEqual(result["status"], "COMPLETE")
        self.assertEqual(result["resolution"], "CONFIRMED_REVIEW_ONLY")
        self.assertEqual(result["evidence_ref_count"], 2)


if __name__ == "__main__":
    unittest.main()
