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
    c2_distributed_goal3_funded,
    c2_goal5_funded,
    c2_low_burden_leakage_goal3_funded,
    c_effective_incentive_grades,
    c_distributed_goal3_funded,
    c_endpoint_control_pressure,
    c_execution_strength,
    c_direct_act_ceiling,
    c_goal4_funded,
    c_goal5_funded,
    certificate_robustness,
    certified_supported_burden,
    c2_selection_floor,
    clearing_goal_funded,
    low_burden_leakage_goal3_funded,
    market_line_funded,
    prospective_goal_funding,
    required_full_win_goal,
    tournament_incentive_profile,
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
        upper_tail_transferability=Grade.HIGH,
        upper_tail_transferability_basis=(
            "current comparable-opposition and mechanism evidence is independently "
            "transferable to the assessed matchup"
        ),
        upper_tail_comparable_context_signal="SUPPORTIVE",
        upper_tail_comparable_context_basis=(
            "same-competition or closely comparable senior evidence supports "
            "the current goal-four-plus mechanism"
        ),
        failure_attacks_route=False,
        failure_attacks_route_basis="main failure does not directly remove the current scoring route",
        material_suppression=False,
        material_suppression_basis="no current material suppression trigger present",
    )
    base.update(overrides)
    return MatchAssessment(**base)


def robust_g3_assessment(**overrides):
    """ROBUST G3 fixture with no G4 authority unless explicitly added."""

    base = dict(
        goal_signal_priority_score=70,
        goal_signal_mean_over_two_rate=0.75,
        goal_signal_mean_over_three_rate=0.50,
        goal_signal_low_draw_trap_rate=0.10,
    )
    base.update(overrides)
    return assessment(**base)


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
    def test_full_win_certificate_requires_goal3_even_at_o20(self):
        a = assessment(
            supported_line=2.25,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertFalse(clearing_goal_funded(a))
        self.assertFalse(clearing_goal_funded(a, selected_line=2.0))

    def test_o225_high_leakage_strong_route_can_fund_goal3_without_high_continuation(self):
        a = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(low_burden_leakage_goal3_funded(a))
        self.assertTrue(clearing_goal_funded(a))

    def test_high_leakage_strong_route_can_fund_goal3_in_clean_medium_shape(self):
        a = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(low_burden_leakage_goal3_funded(a))
        self.assertTrue(clearing_goal_funded(a))

    def test_leakage_goal3_funds_o250_but_not_o275_full_win(self):
        a = assessment(
            supported_line=2.5,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(low_burden_leakage_goal3_funded(a))
        self.assertTrue(clearing_goal_funded(a))
        self.assertFalse(clearing_goal_funded(a, selected_line=2.75))

    def test_o225_leakage_counterweight_requires_strong_route_and_completion(self):
        no_strong_route = assessment(
            supported_line=2.25,
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        low_completion = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            burden_completion_quality=Grade.LOW,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertFalse(low_burden_leakage_goal3_funded(no_strong_route))
        self.assertFalse(low_burden_leakage_goal3_funded(low_completion))

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

    def test_hearts_style_medium_completion_g3_does_not_outrank_mixed_context_g4(self):
        hearts = assessment(
            match_id="hearts_medium_g3",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=False,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            goal_signal_priority_score=61,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.4375,
            goal_signal_low_draw_trap_rate=0.125,
        )
        lech = assessment(
            match_id="lech_mixed_g4",
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "continental evidence has a control endpoint but current carrier remains transferable"
            ),
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            goal_signal_priority_score=60,
            goal_signal_mean_over_two_rate=0.65,
            goal_signal_mean_over_three_rate=0.45,
            goal_signal_low_draw_trap_rate=0.125,
        )
        self.assertEqual(certificate_robustness(hearts, "c"), 1)
        self.assertEqual(certificate_robustness(lech, "c"), 1)
        self.assertEqual(certified_supported_burden(hearts, "c"), 2.5)
        self.assertEqual(certified_supported_burden(lech, "c"), 3.5)
        self.assertEqual(
            rank_assessments([hearts, lech])[0].match_id,
            "lech_mixed_g4",
        )

    def test_c2_ranking_does_not_use_supported_line_as_rank_factor(self):
        high_line = assessment(match_id="z_high", supported_line=3.0)
        low_line = assessment(match_id="a_low", supported_line=2.5)
        ranked = rank_assessments_c2([low_line, high_line])

        # Equal C2 football factors fall through to stable match_id only.
        self.assertEqual(ranked[0].match_id, "z_high")


    def test_c_certificate_depth_precedes_old_lower_burden_preference(self):
        g4 = assessment(
            match_id="g4",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            burden_completion_quality=Grade.MEDIUM,
            goal_signal_priority_score=70,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.05,
        )
        g3 = assessment(
            match_id="g3",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            goal_signal_priority_score=70,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.05,
        )

        self.assertEqual(certified_supported_burden(g4, "c"), 3.5)
        self.assertEqual(certified_supported_burden(g3, "c"), 2.5)
        self.assertEqual(rank_assessments([g3, g4])[0].match_id, "g4")

    def test_robust_g3_can_outrank_fragile_g4(self):
        robust_g3 = assessment(
            match_id="robust_g3",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            goal_signal_priority_score=68,
            goal_signal_mean_over_two_rate=0.72,
            goal_signal_mean_over_three_rate=0.46,
            goal_signal_low_draw_trap_rate=0.05,
        )
        fragile_g4 = assessment(
            match_id="fragile_g4",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "comparable evidence supports G4 but retains a meaningful control endpoint"
            ),
            goal_signal_priority_score=60,
            goal_signal_mean_over_two_rate=0.55,
            goal_signal_mean_over_three_rate=0.30,
            goal_signal_low_draw_trap_rate=0.30,
        )

        self.assertEqual(certified_supported_burden(fragile_g4, "c"), 3.5)
        self.assertEqual(certified_supported_burden(robust_g3, "c"), 2.5)
        self.assertEqual(
            rank_assessments([fragile_g4, robust_g3])[0].match_id,
            "robust_g3",
        )

    def test_slovan_stuttgart_frozen_signal_beats_threshold_only_g3_shape(self):
        # Uses only the handoff's frozen prematch Step-0 Stuttgart metrics.
        stuttgart = assessment(
            match_id="slovan_stuttgart",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            route_reliability=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=66,
            goal_signal_mean_over_two_rate=0.7321,
            goal_signal_mean_over_three_rate=0.4732,
            goal_signal_low_draw_trap_rate=0.0625,
        )
        threshold_only = assessment(
            match_id="threshold_only",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            route_reliability=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=60,
            goal_signal_mean_over_two_rate=0.55,
            goal_signal_mean_over_three_rate=0.30,
            goal_signal_low_draw_trap_rate=0.0625,
        )

        self.assertEqual(certified_supported_burden(stuttgart, "c"), 2.5)
        self.assertEqual(certified_supported_burden(threshold_only, "c"), 2.5)
        self.assertEqual(
            rank_assessments([threshold_only, stuttgart])[0].match_id,
            "slovan_stuttgart",
        )

    def test_c2_certificate_depth_is_ranked_before_route_tiebreakers(self):
        g4 = assessment(
            match_id="c2_g4",
            independent_upper_tail=True,
            goal_signal_priority_score=70,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.05,
        )
        g3 = assessment(
            match_id="c2_g3",
            independent_upper_tail=False,
            goal_signal_priority_score=70,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.05,
        )

        self.assertEqual(certified_supported_burden(g4, "c2"), 3.5)
        self.assertEqual(certified_supported_burden(g3, "c2"), 2.5)
        self.assertEqual(rank_assessments_c2([g3, g4])[0].match_id, "c2_g4")

    def test_hardened_distributed_g3_demotes_high_stall_history_only_shape(self):
        stuttgart = assessment(
            match_id="slovan_stuttgart",
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            xi_robustness=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=66,
            goal_signal_mean_over_two_rate=0.7321,
            goal_signal_mean_over_three_rate=0.4732,
            goal_signal_low_draw_trap_rate=0.0625,
        )
        hodd = assessment(
            match_id="hodd_ranheim",
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            xi_robustness=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=True,
            independent_upper_tail=True,
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            goal_signal_priority_score=80,
            goal_signal_mean_over_two_rate=0.8125,
            goal_signal_mean_over_three_rate=0.6875,
            goal_signal_low_draw_trap_rate=0.0625,
        )
        sogndal = assessment(
            match_id="sogndal_odd",
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            xi_robustness=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=True,
            independent_upper_tail=False,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=68,
            goal_signal_mean_over_two_rate=0.6875,
            goal_signal_mean_over_three_rate=0.4375,
            goal_signal_low_draw_trap_rate=0.125,
        )
        bryne = assessment(
            match_id="bryne_raufoss",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            xi_robustness=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=63,
            goal_signal_mean_over_two_rate=0.6875,
            goal_signal_mean_over_three_rate=0.3125,
            goal_signal_low_draw_trap_rate=0.0,
        )
        stromsgodset = assessment(
            match_id="stromsgodset_kongsvinger",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            xi_robustness=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=True,
            independent_upper_tail=True,
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            goal_signal_priority_score=75,
            goal_signal_mean_over_two_rate=0.625,
            goal_signal_mean_over_three_rate=0.625,
            goal_signal_low_draw_trap_rate=0.125,
        )

        c_ranked = rank_assessments(
            [hodd, sogndal, bryne, stuttgart, stromsgodset]
        )
        self.assertEqual(
            [item.match_id for item in c_ranked],
            [
                "stromsgodset_kongsvinger",
                "hodd_ranheim",
                "bryne_raufoss",
                "sogndal_odd",
                "slovan_stuttgart",
            ],
        )

        c2_ranked = rank_assessments_c2(
            [hodd, sogndal, bryne, stuttgart, stromsgodset]
        )
        self.assertLess(
            [item.match_id for item in c2_ranked].index("slovan_stuttgart"),
            [item.match_id for item in c2_ranked].index("hodd_ranheim"),
        )
        self.assertLess(
            [item.match_id for item in c2_ranked].index("slovan_stuttgart"),
            [item.match_id for item in c2_ranked].index("sogndal_odd"),
        )
        self.assertLess(
            [item.match_id for item in c2_ranked].index("slovan_stuttgart"),
            [item.match_id for item in c2_ranked].index("bryne_raufoss"),
        )
        self.assertEqual(c2_ranked[0].match_id, "stromsgodset_kongsvinger")
    def test_rotation_is_not_suppressive_without_route_specific_failure(self):
        alternative_routes_intact = assessment(
            match_id="alternative_routes_intact",
            xi_robustness=Grade.LOW,
            failure_attacks_route=False,
            material_suppression=False,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            goal_signal_priority_score=70,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.50,
            goal_signal_low_draw_trap_rate=0.05,
        )
        superficially_safer = assessment(
            match_id="superficially_safer",
            xi_robustness=Grade.HIGH,
            failure_attacks_route=False,
            material_suppression=False,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            goal_signal_priority_score=61,
            goal_signal_mean_over_two_rate=0.65,
            goal_signal_mean_over_three_rate=0.38,
            goal_signal_low_draw_trap_rate=0.05,
        )
        route_attacked = assessment(
            match_id="route_attacked",
            xi_robustness=Grade.LOW,
            failure_attacks_route=True,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            goal_signal_priority_score=80,
            goal_signal_mean_over_two_rate=0.80,
            goal_signal_mean_over_three_rate=0.60,
            goal_signal_low_draw_trap_rate=0.00,
        )

        self.assertEqual(
            rank_assessments(
                [superficially_safer, alternative_routes_intact, route_attacked]
            )[0].match_id,
            "alternative_routes_intact",
        )
        self.assertEqual(
            rank_assessments_c2(
                [superficially_safer, alternative_routes_intact, route_attacked]
            )[0].match_id,
            "alternative_routes_intact",
        )


class FootballCExecutionTests(unittest.TestCase):
    def test_kashima_style_high_leakage_now_receives_goal3_certificate(self):
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
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertEqual(c_execution_strength(a), "FRAGILE")
        for line, odds in ((2.5, 1.96), (2.25, 1.89)):
            with self.subTest(line=line):
                ctx = context(
                    official_follow_lane=FollowLane.RESERVE,
                    step2_authorization=Step2Authorization.USER_EXCEPTION,
                    quote=Quote(line, odds),
                )
                result = decide_c(a, ctx)
                self.assertEqual(result.action, Action.PASS)
    def test_strong_carrier_retains_legitimate_bet_when_robust(self):
        a = robust_g3_assessment(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            completion_mode=CompletionMode.CARRIER_LED,
            away_route=RouteStrength.WEAK,
            continuation_quality=Grade.HIGH,
            burden_completion_quality=Grade.HIGH,
            burden_stall_risk=Grade.LOW,
        )
        self.assertEqual(c_execution_strength(a), "ROBUST")
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
            robust_g3_assessment(),
            context(
                official_follow_lane=FollowLane.STOP,
                step2_authorization=Step2Authorization.USER_EXCEPTION,
            ),
        )
        self.assertEqual(decision.action, Action.BET)
    def test_reserve_activation_requires_reserve_lane(self):
        decision = decide_c(
            robust_g3_assessment(),
            context(
                official_follow_lane=FollowLane.RESERVE,
                step2_authorization=Step2Authorization.RESERVE_ACTIVATED,
            ),
        )
        self.assertEqual(decision.action, Action.BET)
    def test_normal_price_at_supported_line_bets(self):
        decision = decide_c(
            robust_g3_assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.70),
            ),
        )
        self.assertEqual(c_execution_strength(robust_g3_assessment()), "ROBUST")
        self.assertEqual(decision.action, Action.BET)
    def test_soft_zone_requires_top_focus(self):
        a = robust_g3_assessment()
        top = decide_c(
            a,
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=True,
            ),
        )
        not_top = decide_c(
            a,
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.5, 1.62),
                top_ranked_focus=False,
            ),
        )
        self.assertEqual(top.action, Action.BET)
        self.assertEqual(not_top.action, Action.PASS)
    def test_o225_leakage_counterweight_no_longer_overrides_execution_strength(self):
        a = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(clearing_goal_funded(a, 2.25))
        self.assertEqual(c_execution_strength(a), "FRAGILE")
        self.assertEqual(
            decide_c(a, context(quote=Quote(2.25, 1.70))).action,
            Action.PASS,
        )
    def test_o250_same_leakage_shape_is_funded_but_not_execution_ready(self):
        a = assessment(
            supported_line=2.5,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.LOW,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.HIGH,
            chance_quality=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertEqual(c_execution_strength(a), "FRAGILE")
        self.assertEqual(
            decide_c(a, context(quote=Quote(2.5, 1.70))).action,
            Action.PASS,
        )
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

    def test_g3_o275_uses_book_order_not_decay_wait(self):
        decision = decide_c(
            robust_g3_assessment(),
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(2.75, 1.85),
                wait_reachable=True,
                wait_requires_negative_info=False,
            ),
        )
        self.assertEqual(decision.action, Action.BOOK)
        self.assertEqual(decision.book_target_line, 2.75)
        self.assertEqual(decision.book_min_odds, 1.85)
    def test_g3_o300_below_floor_is_pending_book_target(self):
        a = robust_g3_assessment(
            independent_upper_tail=True,
            failure_resistance=Grade.MEDIUM,
        )
        self.assertFalse(c_goal4_funded(a))
        decision = decide_c(
            a,
            context(
                BoardState.FOCUS,
                ThesisState.PRESERVED,
                Quote(3.0, 1.85),
                wait_reachable=True,
                wait_requires_negative_info=False,
            ),
        )
        self.assertEqual(decision.action, Action.BOOK)
        self.assertEqual(decision.book_target_line, 3.0)
        self.assertEqual(decision.book_min_odds, 1.90)
        self.assertTrue(decision.book_target_available)
        self.assertFalse(decision.current_price_clears_book_target)
        self.assertNotEqual(decision.action, Action.WAIT)
    def test_g3_only_o325_is_capped_at_o300_without_g4(self):
        a = robust_g3_assessment(
            independent_upper_tail=True,
            failure_resistance=Grade.MEDIUM,
        )
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertFalse(c_goal4_funded(a))
        decision = decide_c(a, context(quote=Quote(3.25, 2.00)))
        self.assertEqual(decision.action, Action.BOOK)
        self.assertEqual(decision.book_target_line, 3.0)
        self.assertEqual(decision.book_min_odds, 1.90)
    def test_g3_book_ceiling_never_authorizes_o350_without_g4(self):
        a = robust_g3_assessment()
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertFalse(c_goal4_funded(a))
        decision = decide_c(a, context(quote=Quote(3.5, 2.00)))
        self.assertEqual(decision.action, Action.BOOK)
        self.assertEqual(decision.book_target_line, 2.75)
        self.assertNotEqual(decision.action, Action.BET)
    def test_high_stall_g3_does_not_gain_book_extension(self):
        a = assessment(
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=False,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            goal_signal_priority_score=88,
            goal_signal_mean_over_two_rate=0.9167,
            goal_signal_mean_over_three_rate=0.6667,
            goal_signal_low_draw_trap_rate=0.0833,
        )
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        decision = decide_c(a, context(quote=Quote(3.25, 2.00)))
        self.assertEqual(decision.action, Action.PASS)

    def test_fragile_review_only_target_requires_conditional_or_better_revalidation(self):
        fragile = assessment(
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            goal_signal_priority_score=61,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.45,
            goal_signal_low_draw_trap_rate=0.125,
        )
        ctx = context(
            board_state=BoardState.WATCH,
            official_follow_lane=FollowLane.STOP,
            step2_authorization=Step2Authorization.USER_EXCEPTION,
            quote=Quote(2.75, 1.82),
            wait_reachable=True,
            wait_requires_negative_info=False,
        )
        self.assertEqual(c_execution_strength(fragile), "FRAGILE")
        self.assertEqual(decide_c(fragile, ctx).action, Action.PASS)

        conditional = assessment(
            **{
                **fragile.__dict__,
                "route_reliability": Grade.HIGH,
                "independent_route_quality": Grade.HIGH,
            }
        )
        self.assertEqual(c_execution_strength(conditional), "CONDITIONAL")
        self.assertEqual(c_endpoint_control_pressure(conditional), "HIGH")
        self.assertIsNone(c_direct_act_ceiling(conditional))
        self.assertEqual(decide_c(conditional, ctx).action, Action.PASS)
    def test_supported_line_is_anchor_when_frozen_goal5_tail_is_strong(self):
        a = assessment(
            supported_line=2.75,
            carrier=CarrierStrength.STRONG,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            burden_stall_risk=Grade.LOW,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
            goal_signal_priority_score=82,
            goal_signal_mean_over_two_rate=0.80,
            goal_signal_mean_over_three_rate=0.60,
            goal_signal_low_draw_trap_rate=0.05,
        )
        profile = prospective_goal_funding(a, "c")
        self.assertTrue(profile["goal4_funded"])
        self.assertTrue(profile["goal5_funded"])
        self.assertFalse(profile["goal6_funded"])
        self.assertEqual(profile["upper_tail_strength"], "STRONG")
        self.assertEqual(c_execution_strength(a), "ROBUST")
        self.assertTrue(market_line_funded(a, 4.0, "c"))
        self.assertTrue(market_line_funded(a, 4.5, "c"))
        self.assertFalse(market_line_funded(a, 4.75, "c"))
        self.assertEqual(certified_supported_burden(a, "c"), 4.5)
        self.assertEqual(
            decide_c(a, context(quote=Quote(4.0, 1.81))).action,
            Action.BET,
        )
    def test_kashiwa_style_o225_leakage_anchor_does_not_inherit_market_tail(self):
        a = assessment(
            supported_line=2.25,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.HIGH,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        self.assertTrue(market_line_funded(a, 2.25, "c"))
        self.assertTrue(market_line_funded(a, 2.5, "c"))
        self.assertFalse(market_line_funded(a, 2.75, "c"))
        self.assertFalse(market_line_funded(a, 4.0, "c"))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertEqual(c_execution_strength(a), "FRAGILE")
        result = decide_c(a, context(quote=Quote(4.0, 1.81)))
        self.assertEqual(result.action, Action.PASS)
    def test_strong_independent_distributed_g3_compiles_o250(self):
        a = assessment(
            supported_line=2.25,
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.LOW,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            goal_signal_priority_score=69,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.5625,
            goal_signal_low_draw_trap_rate=0.0625,
        )
        self.assertTrue(c_distributed_goal3_funded(a))
        self.assertTrue(c2_distributed_goal3_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertEqual(certified_supported_burden(a, "c2"), 2.5)
        self.assertEqual(c_execution_strength(a), "ROBUST")
        self.assertTrue(market_line_funded(a, 2.5, "c"))
        self.assertFalse(market_line_funded(a, 2.75, "c"))
        self.assertEqual(
            decide_c(a, context(quote=Quote(2.5, 1.70))).action,
            Action.BET,
        )
    def test_declared_line_does_not_change_compiled_burden(self):
        common = dict(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
        )
        low = assessment(supported_line=2.25, **common)
        high = assessment(supported_line=4.5, **common)
        self.assertEqual(certified_supported_burden(low, "c"), 2.5)
        self.assertEqual(certified_supported_burden(high, "c"), 2.5)

    def test_full_win_goal_requirement_handles_three_quarter_lines(self):
        self.assertEqual(required_full_win_goal(2.5), 3)
        self.assertEqual(required_full_win_goal(2.75), 4)
        self.assertEqual(required_full_win_goal(3.5), 4)
        self.assertEqual(required_full_win_goal(3.75), 5)
        self.assertEqual(required_full_win_goal(4.75), 6)


class UpperTailTransferabilityCalibrationTests(unittest.TestCase):
    def test_bodo_style_inflated_history_cannot_fund_g4(self):
        # Negative control uses only prospective warnings: the raw goal sample is
        # excellent, but the G4 tail depends materially on domestic/cup contexts
        # that are not comparable enough to carry into the current matchup.
        a = assessment(
            match_id="bodo_dortmund_negative_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.LOW,
            upper_tail_transferability_basis=(
                "upper-tail sample is materially inflated by domestic/cup and "
                "opponent-context evidence; current opponent has a credible "
                "one-goal control endpoint not resolved by that history"
            ),
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.HIGH,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            goal_signal_priority_score=88,
            goal_signal_mean_over_two_rate=0.875,
            goal_signal_mean_over_three_rate=0.625,
            goal_signal_low_draw_trap_rate=0.0,
        )
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertFalse(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertFalse(market_line_funded(a, 3.25, "c"))

    def test_lion_city_style_continental_suppression_overrides_domestic_tail(self):
        # Prospective control: domestic scoring may look explosive, but a
        # materially suppressive same-competition/continental sample takes
        # precedence for G4+. The live/current score is deliberately absent.
        a = assessment(
            match_id="lion_city_continental_negative_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_transferability_basis=(
                "domestic scoring and current attacking personnel would otherwise "
                "support a high upper-tail grade"
            ),
            upper_tail_comparable_context_signal="SUPPRESSIVE",
            upper_tail_comparable_context_basis=(
                "same-competition/continental matches available before kickoff "
                "consistently failed to clear the 2.5-goal threshold, so domestic "
                "blowouts cannot upgrade the fourth-goal tail"
            ),
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            goal_signal_priority_score=85,
            goal_signal_mean_over_two_rate=0.80,
            goal_signal_mean_over_three_rate=0.60,
            goal_signal_low_draw_trap_rate=0.05,
        )
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertFalse(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)
        self.assertEqual(certificate_robustness(a, "c"), 2)

    def test_mixed_comparable_context_caps_high_transferability_to_conditional(self):
        a = assessment(
            match_id="mixed_context_control",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_transferability_basis=(
                "current mechanisms support the upper tail"
            ),
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "same-competition/comparable senior evidence contains both "
                "high-tail and controlled low-tail matches"
            ),
            evidence_confidence=Grade.MEDIUM,
            goal_signal_priority_score=78,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.10,
        )
        self.assertTrue(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 3.5)
        self.assertEqual(certificate_robustness(a, "c"), 1)

    def test_galaxy_style_reply_dependent_g4_requires_stronger_failure_resistance(self):
        a = assessment(
            match_id="galaxy_portland_negative_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "recent high-scoring evidence is mixed with credible home-control endpoints"
            ),
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            goal_signal_priority_score=76,
            goal_signal_mean_over_two_rate=0.8125,
            goal_signal_mean_over_three_rate=0.5625,
            goal_signal_low_draw_trap_rate=0.125,
        )
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertFalse(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)

    def test_hodd_style_medium_carrier_cannot_promote_g3_evidence_to_g4(self):
        a = assessment(
            match_id="hodd_ranheim_negative_control",
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "same-level history contains both 3-2 and repeated 0-0/0-1 control endpoints"
            ),
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            goal_signal_priority_score=80,
            goal_signal_mean_over_two_rate=0.8125,
            goal_signal_mean_over_three_rate=0.6875,
            goal_signal_low_draw_trap_rate=0.0625,
        )
        self.assertTrue(clearing_goal_funded(a, 2.5))
        self.assertFalse(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 2.5)

    def test_two_strong_route_medium_reliability_control_keeps_g4(self):
        a = assessment(
            match_id="stromsgodset_kongsvinger_positive_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            upper_tail_comparable_context_basis=(
                "same-level evidence is mixed but both current scoring routes are independently strong"
            ),
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            goal_signal_priority_score=75,
            goal_signal_mean_over_two_rate=0.625,
            goal_signal_mean_over_three_rate=0.625,
            goal_signal_low_draw_trap_rate=0.125,
        )
        self.assertTrue(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 3.5)

    def test_city_psg_style_current_independent_routes_keep_g4(self):
        a = assessment(
            match_id="city_psg_positive_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_transferability_basis=(
                "XI-confirmed current scoring routes on both sides and repeated "
                "comparable-opposition chance creation independently support goal four"
            ),
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.HIGH,
            xi_robustness=Grade.MEDIUM,
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.LOW,
            goal_signal_priority_score=82,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.10,
        )
        self.assertTrue(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 3.5)
        self.assertEqual(certificate_robustness(a, "c"), 2)

    def test_villa_fener_style_transferable_carrier_tail_keeps_g4(self):
        a = assessment(
            match_id="villa_fener_positive_control",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_transferability_basis=(
                "current XI-confirmed carrier chance creation plus a separate usable "
                "opponent reply route support the fourth goal without relying on raw totals"
            ),
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.HIGH,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.LOW,
        )
        self.assertTrue(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 3.5)

    def test_medium_transferability_can_fund_g4_but_not_robust(self):
        a = assessment(
            match_id="mixed_transferability",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_transferability_basis=(
                "current mechanism is corroborated but some tail evidence comes from "
                "less-comparable contexts"
            ),
            evidence_confidence=Grade.MEDIUM,
            goal_signal_priority_score=78,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.10,
        )
        self.assertTrue(c_goal4_funded(a))
        self.assertEqual(certified_supported_burden(a, "c"), 3.5)
        self.assertEqual(certificate_robustness(a, "c"), 1)

    def test_low_transferability_high_raw_rates_rank_below_transferable_g4(self):
        negative = assessment(
            match_id="bodo_negative",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.LOW,
            upper_tail_transferability_basis=(
                "domestic/cup-heavy upper-tail evidence is not transferable enough"
            ),
            burden_stall_risk=Grade.MEDIUM,
            goal_signal_priority_score=90,
            goal_signal_mean_over_two_rate=0.875,
            goal_signal_mean_over_three_rate=0.625,
            goal_signal_low_draw_trap_rate=0.0,
        )
        positive = assessment(
            match_id="transferable_positive",
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            upper_tail_transferability=Grade.HIGH,
            upper_tail_transferability_basis=(
                "current comparable-opposition carrier and reply mechanisms are verified"
            ),
            evidence_confidence=Grade.MEDIUM,
            goal_signal_priority_score=72,
            goal_signal_mean_over_two_rate=0.70,
            goal_signal_mean_over_three_rate=0.50,
            goal_signal_low_draw_trap_rate=0.10,
        )
        self.assertEqual(certified_supported_burden(negative, "c"), 2.5)
        self.assertEqual(certified_supported_burden(positive, "c"), 3.5)
        self.assertEqual(
            rank_assessments([negative, positive])[0].match_id,
            "transferable_positive",
        )


class XiAssessmentCalibrationTests(unittest.TestCase):
    def test_history_only_usable_routes_no_longer_fund_c_distributed_g3(self):
        a = assessment(
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            goal_signal_priority_score=57,
            goal_signal_mean_over_two_rate=0.6875,
            goal_signal_mean_over_three_rate=0.50,
            goal_signal_low_draw_trap_rate=0.125,
        )
        self.assertFalse(c_distributed_goal3_funded(a))
        self.assertTrue(c2_distributed_goal3_funded(a))
        self.assertIsNone(certified_supported_burden(a, "c"))
        self.assertEqual(certified_supported_burden(a, "c2"), 2.5)
    def test_history_only_high_rate_o250_no_longer_acts_for_c(self):
        a = assessment(
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            goal_signal_priority_score=57,
            goal_signal_mean_over_two_rate=0.6875,
            goal_signal_mean_over_three_rate=0.50,
            goal_signal_low_draw_trap_rate=0.125,
        )
        ctx = context(
            board_state=BoardState.WATCH,
            step2_authorization=Step2Authorization.USER_EXCEPTION,
            quote=Quote(2.5, 1.63),
            wait_reachable=True,
            wait_reachability_basis="single pre-kickoff snapshot",
        )
        self.assertEqual(decide_c(a, ctx).action, Action.PASS)
        self.assertEqual(decide_c2(a, ctx).action, Action.BET)
    def test_soft_price_zone_never_funds_unsupported_higher_burden(self):
        a = assessment(
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            goal_signal_priority_score=57,
            goal_signal_mean_over_two_rate=0.6875,
            goal_signal_mean_over_three_rate=0.50,
            goal_signal_low_draw_trap_rate=0.125,
        )
        ctx = context(
            board_state=BoardState.WATCH,
            step2_authorization=Step2Authorization.USER_EXCEPTION,
            quote=Quote(2.75, 1.63),
            wait_reachable=True,
            wait_reachability_basis="supported O2.5 target may become available",
        )
        self.assertEqual(decide_c(a, ctx).action, Action.PASS)
        self.assertEqual(decide_c2(a, ctx).action, Action.WAIT)

    def test_galaxy_portland_shape_funds_c2_g4_without_all_high_grades(self):
        # Frozen prematch shape: strong+usable routes, HIGH route reliability
        # and independent-route quality, 81.25% 3+, 56.25% 4+, 12.5% trap.
        a = assessment(
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=True,
            goal_signal_priority_score=76,
            goal_signal_mean_over_two_rate=0.8125,
            goal_signal_mean_over_three_rate=0.5625,
            goal_signal_low_draw_trap_rate=0.125,
        )
        self.assertTrue(c2_clearing_goal_funded(a, 3.5))
        self.assertEqual(certified_supported_burden(a, "c2"), 3.5)
        self.assertEqual(
            decide_c2(
                a,
                context(
                    step2_authorization=Step2Authorization.USER_EXCEPTION,
                    quote=Quote(3.25, 1.72),
                ),
            ).action,
            Action.BET,
        )

    def test_weak_frozen_tail_does_not_gain_c2_g4_from_medium_grades(self):
        a = assessment(
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=True,
            goal_signal_priority_score=48,
            goal_signal_mean_over_two_rate=0.5625,
            goal_signal_mean_over_three_rate=0.3125,
            goal_signal_low_draw_trap_rate=0.1875,
        )
        self.assertFalse(c2_clearing_goal_funded(a, 3.0))
        self.assertEqual(certified_supported_burden(a, "c2"), 2.5)

    def test_strong_self_funded_carrier_can_support_c2_g4_with_medium_failure_grade(self):
        # Availability may reduce failure resistance from HIGH to MEDIUM without
        # erasing a separately evidenced strong carrier and independent tail.
        a = assessment(
            home_route=RouteStrength.USABLE,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.STRONG,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            carrier_self_fund=True,
            independent_upper_tail=True,
            goal_signal_priority_score=48,
            goal_signal_mean_over_two_rate=0.5625,
            goal_signal_mean_over_three_rate=0.3125,
            goal_signal_low_draw_trap_rate=0.1875,
        )
        self.assertTrue(c2_clearing_goal_funded(a, 3.25))
        self.assertEqual(certified_supported_burden(a, "c2"), 3.5)


class C2BridgeTests(unittest.TestCase):
    def test_sparse_shadow_probe_cannot_imply_leakage(self):
        from types import SimpleNamespace

        # Legacy synthetic route-quality probes do not provide a C2-owned
        # opponent leakage grade, basis or even a supported burden.
        sparse = SimpleNamespace(
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            route_reliability=Grade.HIGH,
        )
        self.assertFalse(c2_low_burden_leakage_goal3_funded(sparse))
        self.assertFalse(c2_low_burden_leakage_goal3_funded(sparse, 2.25))

    def test_o225_independently_evidenced_leakage_rescues_strong_route(self):
        a = assessment(
            supported_line=2.25,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=False,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            c2_opponent_leakage=Grade.HIGH,
            c2_opponent_leakage_basis="Independently researched current opponent defensive leakage against strong scoring routes",
        )
        self.assertTrue(c2_low_burden_leakage_goal3_funded(a))
        self.assertEqual(c2_selection_floor(a)[0], SelectionFloor.CLEAR)
        self.assertTrue(c2_clearing_goal_funded(a, 2.25))
        self.assertEqual(decide_c2(a, context(quote=Quote(2.25, 1.75))).action, Action.BET)
        # C has not inherited C2's independently researched leakage grade.
        self.assertFalse(low_burden_leakage_goal3_funded(a))

    def test_c2_o225_leakage_is_monotonic_with_positive_upper_tail(self):
        base = dict(
            supported_line=2.25,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.WEAK,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.MEDIUM,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.MEDIUM,
            burden_protection=Grade.MEDIUM,
            c2_opponent_leakage=Grade.HIGH,
            c2_opponent_leakage_basis="Independent opponent leakage evidence",
        )
        without_tail = assessment(**{**base, "independent_upper_tail": False})
        with_tail = assessment(**{**base, "independent_upper_tail": True})
        self.assertTrue(c2_low_burden_leakage_goal3_funded(without_tail))
        self.assertTrue(c2_low_burden_leakage_goal3_funded(with_tail))
        self.assertTrue(c2_clearing_goal_funded(without_tail, 2.25))
        self.assertTrue(c2_clearing_goal_funded(with_tail, 2.25))
        self.assertEqual(c2_selection_floor(without_tail)[0], SelectionFloor.CLEAR)
        self.assertEqual(c2_selection_floor(with_tail)[0], SelectionFloor.CLEAR)

    def test_c2_leakage_goal3_funds_o250_but_not_o275(self):
        a = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            independent_route_quality=Grade.MEDIUM,
            carrier_self_fund=False,
            independent_upper_tail=False,
            c2_opponent_leakage=Grade.HIGH,
            c2_opponent_leakage_basis="Verified opponent-specific leakage against strong attacking routes",
        )
        self.assertTrue(c2_low_burden_leakage_goal3_funded(a, 2.5))
        self.assertTrue(c2_clearing_goal_funded(a, 2.5))
        self.assertEqual(c2_selection_floor(a, 2.5)[0], SelectionFloor.CLEAR)
        for line in (2.75, 3.0):
            with self.subTest(line=line):
                self.assertFalse(c2_clearing_goal_funded(a, line))

    def test_c2_leakage_requires_current_independent_proof_and_quality(self):
        base = dict(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            carrier_self_fund=False,
            independent_upper_tail=False,
            independent_route_quality=Grade.MEDIUM,
            c2_opponent_leakage=Grade.HIGH,
            c2_opponent_leakage_basis="Recent opponent-specific defensive data supports repeat leakage",
        )
        for override in (
            {"c2_opponent_leakage": None, "c2_opponent_leakage_basis": None},
            {"c2_opponent_leakage": Grade.MEDIUM},
            {"route_reliability": Grade.MEDIUM},
            {"chance_quality": Grade.LOW},
            {"failure_resistance": Grade.LOW},
            {"independent_route_quality": Grade.LOW},
            {"home_route": RouteStrength.USABLE},
            {"material_suppression": True},
            {"failure_attacks_route": True},
        ):
            with self.subTest(override=override):
                a = assessment(**{**base, **override})
                self.assertFalse(c2_low_burden_leakage_goal3_funded(a))
                self.assertFalse(c2_clearing_goal_funded(a, 2.25))

    def test_c2_leakage_does_not_depend_on_c_stall_labels(self):
        base = assessment(
            supported_line=2.25,
            away_route=RouteStrength.WEAK,
            carrier_self_fund=False,
            independent_upper_tail=False,
            independent_route_quality=Grade.MEDIUM,
            c2_opponent_leakage=Grade.HIGH,
            c2_opponent_leakage_basis="C2 independently established HIGH recent opponent leakage",
        )
        self.assertTrue(c2_low_burden_leakage_goal3_funded(base))
        without_c = assessment(
            **{
                **base.__dict__,
                "completion_mode": None,
                "burden_completion_quality": None,
                "continuation_quality": None,
                "opponent_leakage": None,
                "burden_stall_risk": None,
            }
        )
        self.assertTrue(c2_clearing_goal_funded(without_c, 2.25))

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
        self.assertFalse(c2_clearing_goal_funded(a, 2.75))
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

    def test_compiler_makes_legacy_focus_bridge_unnecessary(self):
        a = assessment(
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
        )
        ctx = context(
            BoardState.FOCUS,
            ThesisState.PRESERVED,
            Quote(2.75, 1.72),
        )
        self.assertGreaterEqual(certified_supported_burden(a, "c2"), 2.75)
        decision = decide_c2(a, ctx)
        self.assertEqual(decision.action, Action.BET)
        self.assertFalse(decision.bridge_used)

    def test_c2_goal5_compiles_o450_burden_without_bridge(self):
        a = assessment(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
        )
        profile = prospective_goal_funding(a, "c2")
        self.assertTrue(profile["goal5_funded"])
        self.assertEqual(certified_supported_burden(a, "c2"), 4.5)
        self.assertTrue(market_line_funded(a, 4.0, "c2"))
        decision = decide_c2(a, context(quote=Quote(4.0, 1.81)))
        self.assertEqual(decision.action, Action.BET)
        self.assertFalse(decision.bridge_used)

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


class TournamentIncentiveModelTests(unittest.TestCase):
    def verified_tournament(self, effect="EXPANSIVE", **overrides):
        values = {
            "tournament_incentive_required": True,
            "tournament_incentive_resolution": "VERIFIED",
            "home_incentive": "MUST_WIN",
            "away_incentive": "WIN_PREFERRED",
            "tiebreak_margin_relevance": "YES",
            "incentive_effect": effect,
            "simultaneous_results_status": "VERIFIED",
        }
        values.update(overrides)
        return values

    def test_expansive_incentive_can_strengthen_existing_c_route(self):
        base = dict(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        neutral = assessment(**base)
        expansive = assessment(**{**base, **self.verified_tournament()})
        self.assertFalse(clearing_goal_funded(neutral, 2.75))
        self.assertFalse(clearing_goal_funded(expansive, 2.75))
        self.assertTrue(clearing_goal_funded(expansive, 2.5))
        continuation, stall = c_effective_incentive_grades(expansive)
        self.assertEqual(continuation, Grade.HIGH)
        self.assertEqual(stall, Grade.MEDIUM)
        self.assertEqual(
            tournament_incentive_profile(expansive)["tail_bias"],
            "EXPANSIVE",
        )

    def test_mixed_and_unresolved_incentive_cannot_manufacture_c_boost(self):
        base = dict(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.MEDIUM,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.HIGH,
            carrier_self_fund=False,
            independent_upper_tail=False,
        )
        mixed = assessment(**{
            **base,
            **self.verified_tournament(
                effect="MIXED",
                away_incentive="DRAW_ACCEPTABLE",
            ),
        })
        unresolved = assessment(**{
            **base,
            **self.verified_tournament(),
            "tournament_incentive_resolution": "INCENTIVE_RECHECK_REQUIRED",
        })
        self.assertFalse(clearing_goal_funded(mixed, 2.75))
        self.assertFalse(clearing_goal_funded(unresolved, 2.75))
        self.assertEqual(tournament_incentive_profile(mixed)["tail_bias"], "MIXED")
        self.assertEqual(
            tournament_incentive_profile(unresolved)["tail_bias"],
            "UNRESOLVED",
        )

    def test_suppressive_incentive_caps_c_goal5_tail(self):
        strong = dict(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            opponent_leakage=Grade.MEDIUM,
            burden_stall_risk=Grade.LOW,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
        )
        neutral = assessment(**strong)
        suppressive = assessment(**{
            **strong,
            **self.verified_tournament(
                effect="SUPPRESSIVE",
                home_incentive="DRAW_ACCEPTABLE",
                away_incentive="PROTECT_RESULT",
            ),
        })
        self.assertTrue(c_goal5_funded(neutral))
        self.assertFalse(c_goal5_funded(suppressive))
        continuation, stall = c_effective_incentive_grades(suppressive)
        self.assertEqual(continuation, Grade.MEDIUM)
        self.assertEqual(stall, Grade.MEDIUM)

    def test_expansive_incentive_can_clear_c2_fourth_goal_quality_gap(self):
        base = dict(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
        )
        neutral = assessment(**base)
        expansive = assessment(**{**base, **self.verified_tournament()})
        self.assertFalse(c2_clearing_goal_funded(neutral, 3.0))
        self.assertTrue(c2_clearing_goal_funded(expansive, 3.0))

    def test_suppressive_incentive_caps_c2_goal5_tail(self):
        strong = dict(
            supported_line=2.75,
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.HIGH,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.HIGH,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.HIGH,
        )
        neutral = assessment(**strong)
        suppressive = assessment(**{
            **strong,
            **self.verified_tournament(
                effect="SUPPRESSIVE",
                home_incentive="PROTECT_AGGREGATE",
                away_incentive="DRAW_ACCEPTABLE",
            ),
        })
        self.assertTrue(c2_goal5_funded(neutral))
        self.assertFalse(c2_goal5_funded(suppressive))



class CredibleBurdenProfileTests(unittest.TestCase):
    def test_villa_style_g3_can_be_near_funded_g4_without_certificate_upgrade(self):
        a = assessment(
            match_id="villa_style_near_g4",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=False,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.MIXED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.MEDIUM,
            burden_stall_risk=Grade.MEDIUM,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            goal_signal_priority_score=67,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.55,
            goal_signal_low_draw_trap_rate=0.10,
        )
        profile = prospective_goal_funding(a, "c")
        self.assertTrue(profile["goal3_funded"])
        self.assertFalse(profile["goal4_funded"])
        self.assertEqual(profile["certified_supported_burden"], 2.5)
        self.assertEqual(profile["credible_tail_state"], "NEAR_FUNDED")
        self.assertEqual(profile["credible_tail_target_goal"], 4)
        self.assertEqual(profile["credible_burden_band_low"], 2.75)
        self.assertEqual(profile["credible_burden_band_high"], 3.25)
        self.assertFalse(profile["credible_tail_execution_authority"])
        self.assertFalse(market_line_funded(a, 3.0, "c"))

    def test_betis_style_two_route_mixed_tail_is_not_promoted_to_near_funded(self):
        a = assessment(
            match_id="betis_style_mixed_g4",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.STRONG,
            carrier=CarrierStrength.USABLE,
            carrier_self_fund=False,
            independent_upper_tail=False,
            route_reliability=Grade.MEDIUM,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.TWO_SIDED,
            burden_completion_quality=Grade.HIGH,
            continuation_quality=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            goal_signal_priority_score=79,
            goal_signal_mean_over_two_rate=0.75,
            goal_signal_mean_over_three_rate=0.70,
            goal_signal_low_draw_trap_rate=0.05,
        )
        profile = prospective_goal_funding(a, "c")
        self.assertTrue(profile["goal3_funded"])
        self.assertFalse(profile["goal4_funded"])
        self.assertEqual(profile["certified_supported_burden"], 2.5)
        self.assertEqual(profile["credible_tail_state"], "MIXED")
        self.assertEqual(profile["credible_burden_band_low"], 2.5)
        self.assertEqual(profile["credible_burden_band_high"], 3.0)

    def test_madrid_style_g4_can_be_near_funded_g5_without_g5_authority(self):
        a = assessment(
            match_id="madrid_style_near_g5",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            goal_signal_priority_score=75,
            goal_signal_mean_over_two_rate=0.7889,
            goal_signal_mean_over_three_rate=0.6333,
            goal_signal_low_draw_trap_rate=0.0,
        )
        profile = prospective_goal_funding(a, "c")
        self.assertTrue(profile["goal4_funded"])
        self.assertFalse(profile["goal5_funded"])
        self.assertEqual(profile["certified_supported_burden"], 3.5)
        self.assertEqual(profile["credible_tail_state"], "NEAR_FUNDED")
        self.assertEqual(profile["credible_tail_target_goal"], 5)
        self.assertEqual(profile["credible_burden_band_low"], 3.75)
        self.assertEqual(profile["credible_burden_band_high"], 4.25)
        self.assertFalse(market_line_funded(a, 4.0, "c"))

    def test_brugge_style_funded_g4_with_weaker_tail_sample_stays_at_funded_band(self):
        a = assessment(
            match_id="brugge_style_funded_g4",
            home_route=RouteStrength.STRONG,
            away_route=RouteStrength.USABLE,
            carrier=CarrierStrength.STRONG,
            carrier_self_fund=True,
            independent_upper_tail=True,
            route_reliability=Grade.HIGH,
            independent_route_quality=Grade.MEDIUM,
            chance_quality=Grade.HIGH,
            failure_resistance=Grade.MEDIUM,
            evidence_confidence=Grade.HIGH,
            burden_protection=Grade.MEDIUM,
            completion_mode=CompletionMode.CARRIER_LED,
            burden_completion_quality=Grade.MEDIUM,
            continuation_quality=Grade.HIGH,
            burden_stall_risk=Grade.MEDIUM,
            upper_tail_transferability=Grade.MEDIUM,
            upper_tail_comparable_context_signal="MIXED",
            goal_signal_priority_score=60,
            goal_signal_mean_over_two_rate=0.70,
            goal_signal_mean_over_three_rate=0.40,
            goal_signal_low_draw_trap_rate=0.0,
        )
        profile = prospective_goal_funding(a, "c")
        self.assertTrue(profile["goal4_funded"])
        self.assertFalse(profile["goal5_funded"])
        self.assertEqual(profile["credible_tail_state"], "FUNDED")
        self.assertEqual(profile["credible_burden_band_low"], 3.5)
        self.assertEqual(profile["credible_burden_band_high"], 3.5)



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
