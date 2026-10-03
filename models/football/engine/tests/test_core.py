import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from core import (  # noqa: E402
    Action,
    BoardState,
    C3PolicyAssessment,
    CarrierStrength,
    CompletionMode,
    DecisionContext,
    FollowLane,
    FundingSource,
    FundingState,
    Grade,
    H2HReviewStatus,
    MatchAssessment,
    PostXiResearchStatus,
    Quote,
    RouteStrength,
    SecondRouteRole,
    SelectionFloor,
    Settlement,
    ThesisState,
    XiStatus,
    c2_bridge_eligibility,
    c2_selection_floor,
    c3_board_state,
    c3_ranking_key,
    c3_shadow_lane,
    decide_c,
    decide_c2,
    decide_c3,
    follow_through_lane,
    rank_assessments,
    rank_assessments_c2,
    rank_assessments_c3,
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
        main_failure="no unresolved material failure",
        h2h_state="REVIEWED_NOT_MATERIAL",
        supported_line=2.5,
        carrier_self_fund=False,
        independent_upper_tail=False,
        failure_attacks_route=False,
        material_suppression=False,
    )
    base.update(overrides)
    return MatchAssessment(**base)


def c3_assessment(base=None, **overrides):
    data = dict(
        base=base or assessment(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
        ),
        second_route_role=SecondRouteRole.BURDEN_CONTRIBUTING,
        goal3_funding=FundingState.VERIFIED,
        goal3_funding_source=FundingSource.CARRIER,
        goal3_funding_basis="strong self-funded carrier has repeatable third-goal path",
        goal4_funding=FundingState.NOT_REQUIRED,
        goal4_funding_source=FundingSource.NONE,
        goal4_funding_basis="not required below O3.0",
        control_endpoint_risk=Grade.LOW,
        control_endpoint_basis="continued pressure remains supported after two goals",
        forced_chaos_verified=False,
    )
    data.update(overrides)
    return C3PolicyAssessment(**data)


def context(
    board_state=BoardState.FOCUS,
    thesis_state=ThesisState.PRESERVED,
    quote=None,
    **overrides,
):
    base = dict(
        board_state=board_state,
        thesis_state=thesis_state,
        quote=quote or Quote(2.5, 1.70),
        xi_status=XiStatus.CONFIRMED,
        post_xi_research_status=PostXiResearchStatus.FOUND,
        h2h_review_status=H2HReviewStatus.REVIEWED_USABLE,
        h2h_rechecked=True,
        completion_rechecked=True,
        top_ranked_focus=False,
        primary_mechanism_intact=True,
        wait_reachable=False,
        wait_requires_negative_info=False,
        material_veto=False,
    )
    base.update(overrides)
    return DecisionContext(**base)


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

    def test_c_and_c2_can_rank_same_evidence_differently(self):
        completion_first = assessment(
            match_id="completion_first",
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
        )
        route_first = assessment(
            match_id="route_first",
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
        )

        c_ranked = rank_assessments([route_first, completion_first])
        c2_ranked = rank_assessments_c2([route_first, completion_first])

        self.assertEqual(c_ranked[0].match_id, "completion_first")
        self.assertEqual(c2_ranked[0].match_id, "route_first")

    def test_c2_ranking_does_not_use_supported_line_as_rank_factor(self):
        high_line = assessment(match_id="z_high", supported_line=3.0)
        low_line = assessment(match_id="a_low", supported_line=2.5)
        ranked = rank_assessments_c2([low_line, high_line])

        # Equal C2 football factors fall through to stable match_id only.
        self.assertEqual(ranked[0].match_id, "z_high")


class C3BurdenFundingTests(unittest.TestCase):
    def test_two_routes_exchange_only_do_not_create_focus(self):
        a = c3_assessment(
            base=assessment(
                carrier=CarrierStrength.USABLE,
                carrier_self_fund=False,
                independent_upper_tail=False,
            ),
            second_route_role=SecondRouteRole.EXCHANGE_ONLY,
            goal3_funding=FundingState.PARTIAL,
            goal3_funding_source=FundingSource.SECOND_ROUTE,
            goal3_funding_basis="second route can produce exchange goal but third-goal proof is partial",
        )
        self.assertEqual(c3_board_state(a), BoardState.WATCH)

    def test_no_goal3_funding_is_pass_even_with_two_usable_routes(self):
        a = c3_assessment(
            base=assessment(
                carrier=CarrierStrength.USABLE,
                carrier_self_fund=False,
                independent_upper_tail=False,
            ),
            second_route_role=SecondRouteRole.EXCHANGE_ONLY,
            goal3_funding=FundingState.NONE,
            goal3_funding_source=FundingSource.NONE,
            goal3_funding_basis="no prospectively supported third-goal mechanism",
        )
        self.assertEqual(c3_board_state(a), BoardState.PASS)

    def test_verified_second_route_requires_burden_contributing_role(self):
        with self.assertRaisesRegex(ValueError, "burden-contributing"):
            c3_assessment(
                base=assessment(
                    carrier=CarrierStrength.USABLE,
                    carrier_self_fund=False,
                    independent_upper_tail=False,
                ),
                second_route_role=SecondRouteRole.EXCHANGE_ONLY,
                goal3_funding=FundingState.VERIFIED,
                goal3_funding_source=FundingSource.SECOND_ROUTE,
            )

    def test_carrier_led_verified_goal3_can_focus_with_weak_second_route(self):
        base = assessment(
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
        )
        a = c3_assessment(
            base=base,
            second_route_role=SecondRouteRole.NONE,
            goal3_funding=FundingState.VERIFIED,
            goal3_funding_source=FundingSource.CARRIER,
        )
        self.assertEqual(c3_board_state(a), BoardState.FOCUS)
        self.assertEqual(c3_shadow_lane(a, BoardState.FOCUS), FollowLane.FOLLOW)

    def test_o3_requires_goal4_funding(self):
        with self.assertRaisesRegex(ValueError, "goal4 funding cannot be NOT_REQUIRED"):
            c3_assessment(
                base=assessment(
                    supported_line=3.0,
                    carrier=CarrierStrength.STRONG,
                    carrier_self_fund=True,
                    independent_upper_tail=True,
                )
            )

    def test_medium_control_endpoint_caps_at_watch(self):
        a = c3_assessment(control_endpoint_risk=Grade.MEDIUM)
        self.assertEqual(c3_board_state(a), BoardState.WATCH)
        self.assertEqual(c3_shadow_lane(a, BoardState.WATCH), FollowLane.RESERVE)

    def test_c3_ranking_prioritizes_verified_funding_over_two_route_shape(self):
        verified_carrier = c3_assessment(
            base=assessment(
                match_id="carrier",
                away_route=RouteStrength.WEAK,
                carrier=CarrierStrength.STRONG,
                carrier_self_fund=True,
                independent_upper_tail=True,
            ),
            second_route_role=SecondRouteRole.NONE,
        )
        two_route_partial = c3_assessment(
            base=assessment(
                match_id="two_route",
                carrier=CarrierStrength.USABLE,
                carrier_self_fund=False,
                independent_upper_tail=False,
            ),
            second_route_role=SecondRouteRole.EXCHANGE_ONLY,
            goal3_funding=FundingState.PARTIAL,
            goal3_funding_source=FundingSource.SECOND_ROUTE,
        )
        ranked = rank_assessments_c3([two_route_partial, verified_carrier])
        self.assertEqual(ranked[0].base.match_id, "carrier")
        self.assertGreater(c3_ranking_key(verified_carrier), c3_ranking_key(two_route_partial))

    def test_c3_decision_requires_verified_funding_and_low_control(self):
        good = c3_assessment()
        bad = c3_assessment(control_endpoint_risk=Grade.MEDIUM)
        self.assertEqual(decide_c3(good, context()).action, Action.BET)
        self.assertEqual(decide_c3(bad, context()).action, Action.PASS)


class FootballCExecutionTests(unittest.TestCase):
    def test_normal_price_at_supported_line_bets(self):
        decision = decide_c(
            assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.70),
            ),
        )
        self.assertEqual(decision.action, Action.BET)

    def test_soft_zone_requires_top_focus(self):
        top = decide_c(
            assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=True,
            ),
        )
        not_top = decide_c(
            assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=False,
            ),
        )
        self.assertEqual(top.action, Action.BET)
        self.assertEqual(not_top.action, Action.PASS)

    def test_high_current_stall_risk_passes(self):
        decision = decide_c(
            assessment(burden_stall_risk=Grade.HIGH),
            context(),
        )
        self.assertEqual(decision.action, Action.PASS)

    def test_low_current_completion_passes(self):
        decision = decide_c(
            assessment(burden_completion_quality=Grade.LOW),
            context(),
        )
        self.assertEqual(decision.action, Action.PASS)

    def test_low_current_continuation_passes(self):
        decision = decide_c(
            assessment(continuation_quality=Grade.LOW),
            context(),
        )
        self.assertEqual(decision.action, Action.PASS)

    def test_broken_primary_mechanism_passes(self):
        decision = decide_c(
            assessment(),
            context(primary_mechanism_intact=False),
        )
        self.assertEqual(decision.action, Action.PASS)

    def test_above_burden_waits_only_when_healthy_and_reachable(self):
        healthy = decide_c(
            assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.75, 1.85),
                wait_reachable=True,
                wait_requires_negative_info=False,
            ),
        )
        stale = decide_c(
            assessment(),
            context(
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
        ctx = context(
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
        ctx = context(
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
