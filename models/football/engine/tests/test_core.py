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
    H2HReviewStatus,
    MatchAssessment,
    PostXiResearchStatus,
    Quote,
    RouteStrength,
    SelectionFloor,
    Settlement,
    Step2Authorization,
    ThesisState,
    XiStatus,
    c2_bridge_eligibility,
    c2_clearing_goal_funded,
    c2_selection_floor,
    clearing_goal_funded,
    decide_c,
    decide_c2,
    follow_through_lane,
    rank_assessments,
    rank_assessments_c2,
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
        common_evidence_basis="shared current football evidence supports the frozen route and quality grades",
        completion_mode=CompletionMode.TWO_SIDED,
        burden_completion_quality=Grade.HIGH,
        continuation_quality=Grade.HIGH,
        opponent_leakage=Grade.MEDIUM,
        burden_stall_risk=Grade.LOW,
        main_failure="no unresolved material failure",
        h2h_state="REVIEWED_NOT_MATERIAL",
        h2h_effect="NOT_MATERIAL",
        h2h_transferability="VERIFIED",
        h2h_current_corroboration="NOT_APPLICABLE",
        h2h_material_effect=False,
        h2h_basis="reviewed matchup history with no material transferable suppressive mechanism",
        supported_line=2.5,
        supported_line_basis="O2.5 is the highest supported burden without an optimistic tail",
        carrier_self_fund=False,
        carrier_self_fund_basis="usable carrier but not independently self-funding the protected burden",
        independent_upper_tail=False,
        independent_upper_tail_basis="no separate non-market upper-tail path frozen",
        failure_attacks_route=False,
        failure_attacks_route_basis="main failure does not directly remove the current scoring route",
        material_suppression=False,
        material_suppression_basis="no current material suppression trigger present",
    )
    base.update(overrides)
    return MatchAssessment(**base)


def context(
    board_state=BoardState.FOCUS,
    thesis_state=ThesisState.PRESERVED,
    quote=None,
    **overrides,
):
    base = dict(
        board_state=board_state,
        official_follow_lane=FollowLane.FOLLOW,
        step2_authorization=Step2Authorization.ROUTINE_FOLLOW,
        thesis_state=thesis_state,
        thesis_state_basis="current XI/research preserves the frozen scoring thesis",
        quote=quote or Quote(2.5, 1.70),
        xi_status=XiStatus.CONFIRMED,
        post_xi_research_status=PostXiResearchStatus.FOUND,
        h2h_review_status=H2HReviewStatus.REVIEWED_USABLE,
        h2h_rechecked=True,
        h2h_basis="reviewed against current mechanism evidence",
        top_ranked_focus=False,
        primary_mechanism_intact=True,
        primary_mechanism_basis="confirmed XI preserves the primary mechanism",
        wait_reachable=False,
        wait_reachability_basis="no protected target is expected to become executable before kickoff",
        wait_requires_negative_info=False,
        wait_negative_info_basis="no proposed wait depends on adverse football information",
        material_veto=False,
        material_veto_basis="no current material veto condition is present",
    )
    base.update(overrides)
    return DecisionContext(**base)


class FollowThroughTests(unittest.TestCase):
    def test_o225_full_win_still_needs_goal3_but_o20_push_protects(self):
        a = assessment(
            supported_line=2.25,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertFalse(clearing_goal_funded(a))
        self.assertTrue(clearing_goal_funded(a, selected_line=2.0))

    def test_focus_supported_high_goal_totals_are_not_stopped(self):
        for line in (2.0, 2.25, 2.75, 3.0, 3.25, 3.5, 4.0, 4.5):
            with self.subTest(line=line):
                a = assessment(
                    carrier=CarrierStrength.STRONG,
                    supported_line=line,
                    carrier_self_fund=False,
                    independent_upper_tail=False,
                )
                self.assertEqual(
                    follow_through_lane(a, BoardState.FOCUS), FollowLane.FOLLOW
                )

    def test_unfunded_goal3_does_not_block_step2_research(self):
        a = assessment(
            supported_line=2.75,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.STRONG,
            completion_mode=CompletionMode.CARRIER_LED,
            carrier_self_fund=True,
            independent_upper_tail=False,
            opponent_leakage=Grade.HIGH,
        )
        self.assertFalse(clearing_goal_funded(a))
        self.assertEqual(follow_through_lane(a, BoardState.FOCUS), FollowLane.FOLLOW)

    def test_unfunded_goal4_does_not_block_step2_research(self):
        a = assessment(
            supported_line=3.0,
            carrier=CarrierStrength.STRONG,
            independent_upper_tail=False,
        )
        self.assertFalse(clearing_goal_funded(a))
        self.assertEqual(follow_through_lane(a, BoardState.FOCUS), FollowLane.FOLLOW)

    def test_predictive_failure_factors_do_not_become_lane_vetoes(self):
        for overrides in (
            {"burden_stall_risk": Grade.HIGH},
            {"failure_resistance": Grade.LOW},
            {"route_reliability": Grade.LOW},
            {"chance_quality": Grade.LOW},
            {"away_route": RouteStrength.WEAK},
            {"material_suppression": True},
            {"failure_attacks_route": True},
            {"burden_completion_quality": Grade.LOW},
        ):
            with self.subTest(overrides=overrides):
                self.assertEqual(
                    follow_through_lane(assessment(**overrides), BoardState.FOCUS),
                    FollowLane.FOLLOW,
                )

    def test_non_focus_never_auto_follows(self):
        for state in (BoardState.WATCH, BoardState.PASS):
            with self.subTest(state=state):
                self.assertEqual(
                    follow_through_lane(assessment(), state), FollowLane.STOP
                )


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

    def test_c_ranking_prioritizes_clearing_goal_funding(self):
        funded = assessment(
            match_id="funded",
            supported_line=2.75,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            continuation_quality=Grade.MEDIUM,
        )
        unfunded = assessment(
            match_id="unfunded",
            supported_line=2.75,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=False,
            independent_upper_tail=False,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.LOW,
        )
        ranked = rank_assessments([unfunded, funded])
        self.assertEqual(ranked[0].match_id, "funded")

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


class FootballCExecutionTests(unittest.TestCase):
    def test_kashima_style_unfunded_exception_passes_o25_and_o225(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=True,
        )
        for line, odds in ((2.5, 1.96), (2.25, 1.89)):
            with self.subTest(line=line):
                ctx = context(
                    official_follow_lane=FollowLane.RESERVE,
                    step2_authorization=Step2Authorization.USER_EXCEPTION,
                    quote=Quote(line, odds),
                )
                result = decide_c(a, ctx)
                self.assertEqual(result.action, Action.PASS)
                self.assertIn("clearing-goal funding", result.reason)

    def test_strong_carrier_retains_legitimate_bet(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            completion_mode=CompletionMode.CARRIER_LED,
            away_route=RouteStrength.WEAK,
            continuation_quality=Grade.MEDIUM,
            burden_completion_quality=Grade.MEDIUM,
        )
        self.assertEqual(decide_c(a, context()).action, Action.BET)

    def test_unfunded_c_wait_is_not_assumed_model_exposure(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
        )
        ctx = context(
            quote=Quote(2.75, 1.85),
            wait_reachable=True,
            wait_requires_negative_info=False,
        )
        self.assertEqual(decide_c(a, ctx).action, Action.PASS)

    def test_routine_follow_rejects_stop_lane(self):
        with self.assertRaisesRegex(
            ValueError,
            "STEP2 AUTHORIZATION/LANE MISMATCH",
        ):
            decide_c(
                assessment(),
                context(official_follow_lane=FollowLane.STOP),
            )

    def test_stop_lane_is_allowed_only_by_user_exception(self):
        decision = decide_c(
            assessment(),
            context(
                official_follow_lane=FollowLane.STOP,
                step2_authorization=Step2Authorization.USER_EXCEPTION,
            ),
        )
        self.assertEqual(decision.action, Action.BET)

    def test_reserve_activation_requires_reserve_lane(self):
        decision = decide_c(
            assessment(),
            context(
                official_follow_lane=FollowLane.RESERVE,
                step2_authorization=Step2Authorization.RESERVE_ACTIVATED,
            ),
        )
        self.assertEqual(decision.action, Action.BET)

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
    def test_c2_uses_own_route_quality_not_c_completion(self):
        unfunded = assessment(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=False,
            independent_upper_tail=True,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
        )
        self.assertFalse(c2_clearing_goal_funded(unfunded, 2.5))
        self.assertEqual(
            decide_c2(unfunded, context(
                step2_authorization=Step2Authorization.USER_EXCEPTION,
                quote=Quote(2.5, 1.96),
            )).action,
            Action.PASS,
        )
        funded = assessment(
            independent_upper_tail=True,
            burden_completion_quality=Grade.LOW,
            continuation_quality=Grade.LOW,
        )
        self.assertTrue(c2_clearing_goal_funded(funded, 2.5))
        self.assertEqual(decide_c2(funded, context()).action, Action.BET)

    def test_c2_requires_fourth_goal_at_o30(self):
        a = assessment(
            independent_upper_tail=True,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
        )
        self.assertTrue(c2_clearing_goal_funded(a, 2.75))
        self.assertFalse(c2_clearing_goal_funded(a, 3.0))
        self.assertFalse(c2_clearing_goal_funded(a, 3.25))

    def test_c2_bridge_does_not_bypass_fourth_goal_proof(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            independent_upper_tail=True,
            supported_line=2.75,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
        )
        ok, reasons = c2_bridge_eligibility(a, context(quote=Quote(3.0, 1.90)))
        self.assertFalse(ok)
        self.assertIn("C2 clearing-goal funding missing at bridge line", reasons)

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
