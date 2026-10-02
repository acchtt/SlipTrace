import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from core import (  # noqa: E402
    Action,
    BoardState,
    CarrierStrength,
    CompletionMode,
    DecisionContext,
    FollowLane,
    Grade,
    MatchAssessment,
    Quote,
    RouteStrength,
    SelectionFloor,
    Settlement,
    ThesisState,
    c2_bridge_eligibility,
    c2_selection_floor,
    decide_c,
    decide_c2,
    follow_through_lane,
    rank_assessments,
    settle_over,
)


def assessment(**overrides):
    base = dict(
        match_id="alpha",
        home_route=RouteStrength.STRONG,
        away_route=RouteStrength.USABLE,
        carrier=CarrierStrength.USABLE,
        route_reliability=Grade.HIGH,
        independent_route_quality=Grade.HIGH,
        chance_quality=Grade.HIGH,
        failure_resistance=Grade.HIGH,
        xi_robustness=Grade.HIGH,
        evidence_confidence=Grade.HIGH,
        burden_protection=Grade.HIGH,
        completion_mode=CompletionMode.TWO_SIDED,
        burden_completion_quality=Grade.HIGH,
        continuation_quality=Grade.HIGH,
        opponent_leakage=Grade.MEDIUM,
        burden_stall_risk=Grade.LOW,
        supported_line=2.5,
    )
    base.update(overrides)
    return MatchAssessment(**base)


class FollowThroughTests(unittest.TestCase):
    def test_strong_two_route_high_resistance_is_follow(self):
        lane = follow_through_lane(
            assessment(carrier=CarrierStrength.STRONG),
            BoardState.FOCUS,
        )
        self.assertEqual(lane, FollowLane.FOLLOW)

    def test_medium_resistance_high_protection_is_reserve(self):
        lane = follow_through_lane(
            assessment(
                carrier=CarrierStrength.STRONG,
                failure_resistance=Grade.MEDIUM,
            ),
            BoardState.FOCUS,
        )
        self.assertEqual(lane, FollowLane.RESERVE)

    def test_weak_second_route_stops_routine_followthrough(self):
        lane = follow_through_lane(
            assessment(
                carrier=CarrierStrength.STRONG,
                away_route=RouteStrength.WEAK,
            ),
            BoardState.FOCUS,
        )
        self.assertEqual(lane, FollowLane.STOP)

    def test_carrier_led_weak_second_route_can_follow(self):
        lane = follow_through_lane(
            assessment(
                away_route=RouteStrength.WEAK,
                carrier=CarrierStrength.STRONG,
                completion_mode=CompletionMode.CARRIER_LED,
                carrier_self_fund=True,
                independent_upper_tail=True,
                opponent_leakage=Grade.HIGH,
                independent_route_quality=Grade.MEDIUM,
            ),
            BoardState.FOCUS,
        )
        self.assertEqual(lane, FollowLane.FOLLOW)

    def test_high_stall_risk_blocks_follow(self):
        lane = follow_through_lane(
            assessment(
                carrier=CarrierStrength.STRONG,
                burden_stall_risk=Grade.HIGH,
            ),
            BoardState.FOCUS,
        )
        self.assertEqual(lane, FollowLane.STOP)

    def test_watch_never_auto_follows(self):
        lane = follow_through_lane(
            assessment(),
            BoardState.WATCH,
        )
        self.assertEqual(lane, FollowLane.STOP)


class SelectionFloorTests(unittest.TestCase):
    def test_two_route_floor_clears(self):
        state, reasons = c2_selection_floor(assessment())
        self.assertEqual(state, SelectionFloor.CLEAR)
        self.assertEqual(reasons, ())

    def test_material_failure_forces_fail(self):
        state, _ = c2_selection_floor(
            assessment(failure_attacks_route=True)
        )
        self.assertEqual(state, SelectionFloor.FAIL)

    def test_strong_carrier_can_clear_with_weak_second_route(self):
        state, _ = c2_selection_floor(
            assessment(
                away_route=RouteStrength.WEAK,
                carrier=CarrierStrength.STRONG,
                carrier_self_fund=True,
                independent_upper_tail=True,
            )
        )
        self.assertEqual(state, SelectionFloor.CLEAR)


class RankingTests(unittest.TestCase):
    def test_declared_quality_order_is_deterministic(self):
        strong = assessment(match_id="strong")
        weak = assessment(
            match_id="weak",
            route_reliability=Grade.MEDIUM,
        )
        ranked = rank_assessments([weak, strong])
        self.assertEqual([x.match_id for x in ranked], ["strong", "weak"])


class FootballCExecutionTests(unittest.TestCase):
    def test_normal_price_at_supported_line_bets(self):
        decision = decide_c(
            assessment(),
            DecisionContext(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.70),
            ),
        )
        self.assertEqual(decision.action, Action.BET)

    def test_soft_zone_requires_top_focus(self):
        top = decide_c(
            assessment(),
            DecisionContext(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=True,
            ),
        )
        not_top = decide_c(
            assessment(),
            DecisionContext(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=False,
            ),
        )
        self.assertEqual(top.action, Action.BET)
        self.assertEqual(not_top.action, Action.PASS)

    def test_above_burden_waits_only_when_healthy_and_reachable(self):
        healthy = decide_c(
            assessment(),
            DecisionContext(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.75, 1.85),
                wait_reachable=True,
                wait_requires_negative_info=False,
            ),
        )
        stale = decide_c(
            assessment(),
            DecisionContext(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.75, 1.85),
                wait_reachable=True,
                wait_requires_negative_info=True,
            ),
        )
        self.assertEqual(healthy.action, Action.WAIT)
        self.assertEqual(stale.action, Action.PASS)


class C2BridgeTests(unittest.TestCase):
    def test_focus_bridge_clears_only_with_independent_proof(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            independent_upper_tail=True,
        )
        ctx = DecisionContext(
            BoardState.FOCUS,
            ThesisState.PRESERVED,
            Quote(2.75, 1.72),
        )
        ok, reasons = c2_bridge_eligibility(a, ctx)
        self.assertTrue(ok, reasons)
        decision = decide_c2(a, ctx)
        self.assertEqual(decision.action, Action.BET)
        self.assertTrue(decision.bridge_used)

    def test_bridge_never_uses_market_as_upper_tail_proof(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            independent_upper_tail=False,
        )
        ctx = DecisionContext(
            BoardState.FOCUS,
            ThesisState.PRESERVED,
            Quote(2.75, 2.10),
        )
        ok, reasons = c2_bridge_eligibility(a, ctx)
        self.assertFalse(ok)
        self.assertIn(
            "independent non-market upper-tail proof missing",
            reasons,
        )


class SettlementTests(unittest.TestCase):
    def test_o225_two_goals_is_half_loss(self):
        result, pnl = settle_over(2.25, 2, 1.90)
        self.assertEqual(result, Settlement.HALF_LOSS)
        self.assertAlmostEqual(pnl, -0.5)

    def test_o275_three_goals_is_half_win(self):
        result, pnl = settle_over(2.75, 3, 1.90)
        self.assertEqual(result, Settlement.HALF_WIN)
        self.assertAlmostEqual(pnl, 0.45)

    def test_o3_three_goals_pushes(self):
        result, pnl = settle_over(3.0, 3, 1.90)
        self.assertEqual(result, Settlement.PUSH)
        self.assertAlmostEqual(pnl, 0.0)


if __name__ == "__main__":
    unittest.main()
