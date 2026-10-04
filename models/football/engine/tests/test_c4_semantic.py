import copy
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from c4_semantic import C4ContractError, compile_board  # noqa: E402


def a(state, basis=None):
    return {
        "state": state,
        "basis": basis or f"prospective evidence basis for {state.lower()}",
    }


def side(
    *,
    creation="VERIFIED",
    access="VERIFIED",
    service="VERIFIED",
    leakage="PARTIAL",
    personnel="INTACT",
    suppression="NONE",
    multigoal="VERIFIED",
):
    return {
        "creation_repeatability": a(creation),
        "dangerous_access": a(access),
        "service_finishing_continuity": a(service),
        "matched_opponent_leakage": a(leakage),
        "personnel_integrity": a(personnel),
        "route_suppression": a(suppression),
        "multi_goal_repeatability": a(multigoal),
    }


def match(match_id="alpha", **overrides):
    row = {
        "match_id": match_id,
        "common_evidence_basis": "single frozen Step-1 research epoch",
        "home": side(),
        "away": side(
            creation="VERIFIED",
            access="PARTIAL",
            service="VERIFIED",
            leakage="PARTIAL",
            multigoal="PARTIAL",
        ),
        "mechanism_evidence_coverage": a("COMPLETE"),
        "team_news_coverage": a("COMPLETE"),
        "competition_context_coverage": a("COMPLETE"),
        "continuation_after_first_goal": a("VERIFIED"),
        "lead_control_tendency": a("NONE"),
        "draw_utility": a("NOT_APPLICABLE"),
        "mechanism_failure": a("NONE"),
        "match_suppression": a("NONE"),
        "upper_tail_repeatability": a("VERIFIED"),
    }
    row.update(overrides)
    return row


def payload(*rows):
    return {
        "schema_version": "football-c4-semantic-v1",
        "stage": "board",
        "matches": list(rows),
    }


class C4StructuredEvidenceTests(unittest.TestCase):
    def test_strong_route_carrier_and_goal4_focus(self):
        result = compile_board(payload(match()))
        row = result["matches"][0]
        self.assertEqual(row["c4_home_route"], "STRONG")
        self.assertEqual(row["c4_away_route"], "STRONG")
        self.assertEqual(row["c4_carrier"], "STRONG")
        self.assertEqual(row["c4_goal3_funding"], "VERIFIED")
        self.assertEqual(row["c4_goal4_funding"], "VERIFIED")
        self.assertEqual(row["c4_supported_line"], 3.0)
        self.assertEqual(row["c4_state"], "C4-FOCUS")

    def test_damaged_route_cannot_be_strong_or_usable(self):
        row = match()
        row["home"] = side(personnel="DAMAGED")
        result = compile_board(payload(row))
        self.assertEqual(result["matches"][0]["c4_home_route"], "WEAK")

    def test_partial_goal3_maps_to_o2(self):
        row = match()
        row["home"] = side(
            creation="VERIFIED",
            access="PARTIAL",
            service="PARTIAL",
            leakage="NONE",
            multigoal="PARTIAL",
        )
        row["away"] = side(
            creation="PARTIAL",
            access="VERIFIED",
            service="PARTIAL",
            leakage="NONE",
            multigoal="NONE",
        )
        row["continuation_after_first_goal"] = a("PARTIAL")
        row["upper_tail_repeatability"] = a("NONE")
        result = compile_board(payload(row))
        out = result["matches"][0]
        self.assertEqual(out["c4_goal3_funding"], "PARTIAL")
        self.assertEqual(out["c4_supported_line"], 2.0)
        self.assertEqual(out["c4_state"], "C4-WATCH")

    def test_verified_suppression_forces_pass(self):
        row = match()
        row["match_suppression"] = a("VERIFIED")
        result = compile_board(payload(row))
        out = result["matches"][0]
        self.assertTrue(out["c4_material_suppression"])
        self.assertEqual(out["c4_failure_resistance"], "LOW")
        self.assertEqual(out["c4_state"], "C4-PASS")

    def test_missing_anchor_basis_fails_closed(self):
        row = match()
        row["home"]["dangerous_access"] = {"state": "VERIFIED", "basis": ""}
        with self.assertRaisesRegex(C4ContractError, "home.dangerous_access.basis"):
            compile_board(payload(row))

    def test_missing_common_basis_fails_closed(self):
        row = match()
        row["common_evidence_basis"] = ""
        with self.assertRaisesRegex(C4ContractError, "common_evidence_basis"):
            compile_board(payload(row))

    def test_exact_key_tie_uses_match_id_ascending(self):
        first = match("zeta")
        second = match("alpha")
        result = compile_board(payload(first, second))
        self.assertEqual(
            [row["match_id"] for row in result["matches"]],
            ["alpha", "zeta"],
        )

    def test_input_order_cannot_change_ranking(self):
        a_row = match("a")
        b_row = match("b")
        one = compile_board(payload(a_row, b_row))
        two = compile_board(payload(copy.deepcopy(b_row), copy.deepcopy(a_row)))
        self.assertEqual(
            [row["match_id"] for row in one["matches"]],
            [row["match_id"] for row in two["matches"]],
        )


if __name__ == "__main__":
    unittest.main()
