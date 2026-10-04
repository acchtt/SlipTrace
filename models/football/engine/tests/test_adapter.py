import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from adapter import ContractError, run_audit_record, run_board, run_decision  # noqa: E402
from decision_triplet_cli import run_triplet  # noqa: E402


def match(match_id="m1", **overrides):
    row = {
        "match_id": match_id,
        "kickoff_ict": "2026-10-02T01:45:00+07:00",
        "operational_viability_grade": "A",
        "raw_operational_viability_grade": "A",
        "competition_reliability_state": "UNPROVEN",
        "competition_reliability_reason": "fewer than 3 countable observations",
        "competition_reliability_manual_override": "NONE",
        "demoted_probation": False,
        "xi_expected": "YES",
        "market_observability": "HIGH",
        "team_news_observability": "HIGH",
        "operational_viability_reason": "reliable XI/news and executable totals expected",
        "home_route": "STRONG",
        "away_route": "USABLE",
        "carrier": "USABLE",
        "route_reliability": "HIGH",
        "independent_route_quality": "HIGH",
        "chance_quality": "HIGH",
        "failure_resistance": "HIGH",
        "xi_robustness": "MEDIUM",
        "evidence_confidence": "HIGH",
        "burden_protection": "HIGH",
        "completion_mode": "TWO_SIDED",
        "burden_completion_quality": "HIGH",
        "continuation_quality": "HIGH",
        "opponent_leakage": "MEDIUM",
        "burden_stall_risk": "LOW",
        "main_failure": "no unresolved material failure",
        "h2h_state": "REVIEWED_NOT_MATERIAL",
        "supported_line": 2.5,
        "carrier_self_fund": False,
        "independent_upper_tail": False,
        "failure_attacks_route": False,
        "material_suppression": False,
        "tournament_incentive_required": False,
        "tournament_format_status": "NOT_APPLICABLE",
        "competition_stage": "NOT_APPLICABLE",
        "competition_format": "NOT_APPLICABLE",
        "draw_resolution": "NOT_APPLICABLE",
        "aggregate_state": "NOT_APPLICABLE",
        "qualification_state": "NOT_APPLICABLE",
        "simultaneous_results_status": "NOT_APPLICABLE",
        "simultaneous_results_note": "NOT_APPLICABLE",
        "home_incentive": "NOT_APPLICABLE",
        "away_incentive": "NOT_APPLICABLE",
        "tiebreak_margin_relevance": "NOT_APPLICABLE",
        "incentive_effect": "NOT_APPLICABLE",
        "board_state": "C2-FOCUS",
        "c3_second_route_role": "BURDEN_CONTRIBUTING",
        "c3_goal3_funding": "VERIFIED",
        "c3_goal3_funding_source": "CARRIER",
        "c3_goal3_funding_basis": "strong self-funded carrier can fund goal three",
        "c3_goal4_funding": "NOT_REQUIRED",
        "c3_goal4_funding_source": "NONE",
        "c3_goal4_funding_basis": "not required below O3.0",
        "c3_control_endpoint_risk": "LOW",
        "c3_control_endpoint_basis": "continued pressure remains supported beyond two goals",
        "c3_forced_chaos_verified": False,
    }
    row.update(overrides)
    return row


def decision_context(**overrides):
    row = {
        "board_state": "C-FOCUS",
        "thesis_state": "PRESERVED",
        "quote": {"line": 2.5, "odds": 1.70},
        "xi_status": "CONFIRMED",
        "post_xi_research_status": "FOUND",
        "market_history_status": "FOUND",
        "market_history_movement": "STABLE",
        "market_history_conflict_recheck": "NOT_REQUIRED",
        "market_history_note": "open O2.5 -> pre-XI O2.5 -> current O2.5",
        "h2h_review_status": "REVIEWED_USABLE",
        "h2h_rechecked": True,
        "completion_rechecked": True,
        "top_ranked_focus": False,
        "primary_mechanism_intact": True,
        "wait_reachable": False,
        "wait_requires_negative_info": False,
        "material_veto": False,
        "tournament_incentive_rechecked": False,
        "tournament_incentive_recheck_status": "NOT_APPLICABLE",
    }
    row.update(overrides)
    return row


def triplet_payload(model):
    state = {
        "c": "C-FOCUS",
        "c2": "C2-FOCUS",
        "c3": "C3-FOCUS",
    }[model]
    return {
        "schema_version": "football-engine-v1",
        "stage": "decision",
        "model": model,
        "match": match(
            board_state=state,
            carrier="STRONG",
            carrier_self_fund=True,
            independent_upper_tail=True,
        ),
        "context": decision_context(board_state=state),
    }


class DecisionTripletRunnerTests(unittest.TestCase):
    def test_triplet_executes_all_three_models(self):
        result = run_triplet(
            triplet_payload("c"),
            triplet_payload("c2"),
            triplet_payload("c3"),
        )
        self.assertEqual(result["engine_execution_status"], "EXECUTED_ALL_THREE")
        self.assertEqual(result["models_executed"], ["c", "c2", "c3"])
        self.assertEqual(set(result["results"]), {"c", "c2", "c3"})

    def test_triplet_rejects_model_mismatch(self):
        wrong = triplet_payload("c2")
        with self.assertRaisesRegex(ContractError, "expected model=c"):
            run_triplet(
                wrong,
                triplet_payload("c2"),
                triplet_payload("c3"),
            )

    def test_triplet_rejects_non_decision_stage(self):
        wrong = triplet_payload("c3")
        wrong["stage"] = "board"
        with self.assertRaisesRegex(ContractError, "must use stage=decision"):
            run_triplet(
                triplet_payload("c"),
                triplet_payload("c2"),
                wrong,
            )


class BoardContractTests(unittest.TestCase):
    def test_board_is_ranked_and_floor_is_computed(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c2",
                "matches": [
                    match("weak", route_reliability="MEDIUM"),
                    match("strong"),
                ],
            }
        )
        self.assertEqual(result["matches"][0]["match_id"], "strong")
        self.assertEqual(
            result["matches"][0]["selection_floor"],
            "CLEAR",
        )
        self.assertEqual(
            result["ranking_policy"],
            "FOOTBALL_C2_FROZEN_ROUTE_QUALITY",
        )

    def test_missing_operational_gate_fails(self):
        row = match()
        row.pop("operational_viability_grade")
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_low_observability_fixture_is_blocked(self):
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — LOW OPERATIONAL OBSERVABILITY",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [
                        match(
                            operational_viability_grade="C",
                            raw_operational_viability_grade="C",
                            xi_expected="NO",
                            market_observability="LOW",
                            team_news_observability="LOW",
                        )
                    ],
                }
            )

    def test_grade_a_requires_expected_xi(self):
        with self.assertRaisesRegex(
            ContractError,
            "operational grade A requires xi_expected=YES",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [match(xi_expected="UNCERTAIN")],
                }
            )

    def test_grade_b_is_capped_at_reserve(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        operational_viability_grade="B",
                        raw_operational_viability_grade="B",
                        xi_expected="UNCERTAIN",
                        market_observability="MEDIUM",
                        carrier="STRONG",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["follow_lane"], "RESERVE")
        self.assertEqual(result["follow_count"], 0)
        self.assertEqual(result["reserve_count"], 1)

    def test_caution_caps_raw_a_to_b(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        operational_viability_grade="B",
                        raw_operational_viability_grade="A",
                        competition_reliability_state="CAUTION",
                        competition_reliability_reason="XI usable rate below 75%",
                        carrier="STRONG",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["operational_viability_grade"], "B")
        self.assertEqual(result["matches"][0]["follow_lane"], "RESERVE")

    def test_caution_a_bypass_is_blocked(self):
        with self.assertRaisesRegex(
            ContractError,
            "COMPETITION RELIABILITY CAP BYPASS",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [
                        match(
                            operational_viability_grade="A",
                            raw_operational_viability_grade="A",
                            competition_reliability_state="CAUTION",
                            competition_reliability_reason="market usable rate below 75%",
                        )
                    ],
                }
            )

    def test_demoted_probation_raw_a_may_enter_as_b(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        operational_viability_grade="B",
                        raw_operational_viability_grade="A",
                        competition_reliability_state="DEMOTED",
                        competition_reliability_reason="three consecutive critical failures",
                        demoted_probation=True,
                        carrier="STRONG",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["follow_lane"], "RESERVE")
        self.assertTrue(result["matches"][0]["demoted_probation"])

    def test_demoted_probation_cannot_rescue_raw_b(self):
        with self.assertRaisesRegex(
            ContractError,
            "COMPETITION RELIABILITY CAP BYPASS",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [
                        match(
                            operational_viability_grade="B",
                            raw_operational_viability_grade="B",
                            competition_reliability_state="DEMOTED",
                            competition_reliability_reason="three consecutive critical failures",
                            demoted_probation=True,
                        )
                    ],
                }
            )

    def test_carrier_led_weak_second_route_can_follow(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        home_route="STRONG",
                        away_route="WEAK",
                        carrier="STRONG",
                        completion_mode="CARRIER_LED",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                        opponent_leakage="HIGH",
                        independent_route_quality="MEDIUM",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["follow_lane"], "FOLLOW")

    def test_high_stall_risk_blocks_two_sided_follow(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        carrier="STRONG",
                        burden_stall_risk="HIGH",
                        board_state="C-FOCUS",
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["follow_lane"], "STOP")

    def test_c2_does_not_inherit_c_burden_completion_ranking(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c2",
                "matches": [
                    match(
                        "completion_first",
                        burden_completion_quality="HIGH",
                        continuation_quality="HIGH",
                        route_reliability="MEDIUM",
                        independent_route_quality="MEDIUM",
                    ),
                    match(
                        "route_first",
                        burden_completion_quality="MEDIUM",
                        continuation_quality="MEDIUM",
                        route_reliability="HIGH",
                        independent_route_quality="HIGH",
                    ),
                ],
            }
        )
        self.assertEqual(result["matches"][0]["match_id"], "route_first")

    def test_c2_equal_quality_is_not_ranked_by_lower_supported_line(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c2",
                "matches": [
                    match("z_high", supported_line=3.0),
                    match("a_low", supported_line=2.5),
                ],
            }
        )
        self.assertEqual(result["matches"][0]["match_id"], "z_high")

    def test_c_board_reports_burden_completion_ranking_policy(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [match(carrier="STRONG", board_state="C-FOCUS")],
            }
        )
        self.assertEqual(
            result["ranking_policy"],
            "FOOTBALL_C_BURDEN_COMPLETION",
        )

    def test_same_kickoff_follow_is_capped_at_two_best_candidates(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [
                    match(
                        "high_burden",
                        carrier="STRONG",
                        supported_line=3.0,
                        board_state="C-FOCUS",
                    ),
                    match(
                        "mid_burden",
                        carrier="STRONG",
                        supported_line=2.75,
                        board_state="C-FOCUS",
                    ),
                    match(
                        "low_burden",
                        carrier="STRONG",
                        supported_line=2.5,
                        board_state="C-FOCUS",
                    ),
                ],
            }
        )
        lanes = {row["match_id"]: row["follow_lane"] for row in result["matches"]}
        self.assertEqual(lanes["low_burden"], "FOLLOW")
        self.assertEqual(lanes["mid_burden"], "FOLLOW")
        self.assertEqual(lanes["high_burden"], "RESERVE")
        self.assertEqual(result["max_follow_per_exact_kickoff"], 2)

    def test_high_completion_carrier_path_cannot_be_c_pass(self):
        with self.assertRaisesRegex(
            ContractError,
            "C-PASS CONTRADICTION",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [
                        match(
                            home_route="STRONG",
                            away_route="WEAK",
                            carrier="STRONG",
                            completion_mode="CARRIER_LED",
                            carrier_self_fund=True,
                            independent_upper_tail=True,
                            opponent_leakage="HIGH",
                            board_state="C-PASS",
                        )
                    ],
                }
            )

    def test_missing_tournament_gate_fails(self):
        row = match()
        row.pop("tournament_incentive_required")
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_required_tournament_block_must_not_be_na(self):
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [match(tournament_incentive_required=True)],
                }
            )

    def test_limited_tournament_block_is_blocked(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="LIMITED",
            competition_stage="GROUP D ROUND 6",
            competition_format="GROUP",
            draw_resolution="90-minute group result",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="UNKNOWN",
            simultaneous_results_status="UNKNOWN",
            simultaneous_results_note="qualification and tiebreak impact unresolved",
            home_incentive="UNKNOWN",
            away_incentive="UNKNOWN",
            tiebreak_margin_relevance="UNKNOWN",
            incentive_effect="UNKNOWN",
        )
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_verified_format_with_unknown_tiebreak_is_blocked(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="GROUP D ROUND 6",
            competition_format="GROUP",
            draw_resolution="90-minute group result",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="top two advance; current exact need verified",
            simultaneous_results_status="VERIFIED",
            simultaneous_results_note="other group match impact checked",
            home_incentive="WIN_PREFERRED",
            away_incentive="MUST_WIN",
            tiebreak_margin_relevance="UNKNOWN",
            incentive_effect="MIXED",
        )
        with self.assertRaisesRegex(
            ContractError,
            "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c",
                    "matches": [row],
                }
            )

    def test_complete_tournament_block_passes(self):
        row = match(
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="GROUP FINAL ROUND",
            competition_format="GROUP",
            draw_resolution="draw qualifies home",
            aggregate_state="NOT A TWO-LEG TIE",
            qualification_state="home qualifies with draw; away must win",
            simultaneous_results_status="VERIFIED",
            simultaneous_results_note="simultaneous group result impact checked",
            home_incentive="DRAW_ACCEPTABLE",
            away_incentive="MUST_WIN",
            tiebreak_margin_relevance="YES",
            incentive_effect="MIXED",
        )
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [row],
            }
        )
        self.assertTrue(result["matches"][0]["tournament_incentive_required"])
        self.assertEqual(result["matches"][0]["incentive_effect"], "MIXED")

    def test_bad_schema_fails(self):
        with self.assertRaises(ContractError):
            run_board(
                {
                    "schema_version": "wrong",
                    "stage": "board",
                    "model": "c",
                    "matches": [match()],
                }
            )


class C3IsolationTests(unittest.TestCase):
    C3_KEYS = (
        "c3_second_route_role",
        "c3_goal3_funding",
        "c3_goal3_funding_source",
        "c3_goal3_funding_basis",
        "c3_goal4_funding",
        "c3_goal4_funding_source",
        "c3_goal4_funding_basis",
        "c3_control_endpoint_risk",
        "c3_control_endpoint_basis",
        "c3_forced_chaos_verified",
    )

    def without_c3(self, row):
        row = dict(row)
        for key in self.C3_KEYS:
            row.pop(key, None)
        return row

    def test_c_board_does_not_require_c3_fields(self):
        row = self.without_c3(match(carrier="STRONG", board_state="C-FOCUS"))
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [row],
            }
        )
        self.assertEqual(result["model"], "c")

    def test_c2_board_does_not_require_c3_fields(self):
        row = self.without_c3(match(board_state="C2-FOCUS"))
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c2",
                "matches": [row],
            }
        )
        self.assertEqual(result["model"], "c2")

    def test_changing_c3_fields_cannot_change_c_ranking(self):
        a1 = match("a", carrier="STRONG", board_state="C-FOCUS")
        b1 = match("b", carrier="STRONG", board_state="C-FOCUS")
        first = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [a1, b1],
            }
        )
        a2 = dict(a1)
        b2 = dict(b1)
        a2["c3_second_route_role"] = "NONE"
        a2["c3_goal3_funding"] = "NONE"
        a2["c3_goal3_funding_source"] = "NONE"
        b2["c3_second_route_role"] = "BURDEN_CONTRIBUTING"
        b2["c3_control_endpoint_risk"] = "HIGH"
        second = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c",
                "matches": [a2, b2],
            }
        )
        self.assertEqual(
            [(x["match_id"], x["ranking_key"]) for x in first["matches"]],
            [(x["match_id"], x["ranking_key"]) for x in second["matches"]],
        )


class C3ContractTests(unittest.TestCase):
    def test_c3_board_ignores_two_route_label_without_goal3_funding(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c3",
                "matches": [
                    match(
                        "two_route",
                        carrier="USABLE",
                        carrier_self_fund=False,
                        independent_upper_tail=False,
                        c3_second_route_role="EXCHANGE_ONLY",
                        c3_goal3_funding="NONE",
                        c3_goal3_funding_source="NONE",
                        c3_goal3_funding_basis="both can score once but no third-goal mechanism",
                    )
                ],
            }
        )
        row = result["matches"][0]
        self.assertEqual(row["board_state"], "C3-PASS")
        self.assertEqual(row["c3_shadow_lane"], "STOP")
        self.assertEqual(
            result["ranking_policy"],
            "FOOTBALL_C3_CLEARING_GOAL_FUNDING",
        )
        self.assertNotIn("completion_mode", row)

    def test_c3_carrier_led_goal3_can_focus_without_second_route(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c3",
                "matches": [
                    match(
                        "carrier",
                        away_route="WEAK",
                        carrier="STRONG",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                        c3_second_route_role="NONE",
                        c3_goal3_funding="VERIFIED",
                        c3_goal3_funding_source="CARRIER",
                    )
                ],
            }
        )
        row = result["matches"][0]
        self.assertEqual(row["board_state"], "C3-FOCUS")
        self.assertEqual(row["c3_shadow_lane"], "FOLLOW")

    def test_c3_b_grade_is_capped_at_reserve(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c3",
                "matches": [
                    match(
                        "c3_b",
                        operational_viability_grade="B",
                        raw_operational_viability_grade="B",
                        xi_expected="UNCERTAIN",
                        market_observability="MEDIUM",
                        carrier="STRONG",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                    )
                ],
            }
        )
        self.assertEqual(result["matches"][0]["board_state"], "C3-FOCUS")
        self.assertEqual(result["matches"][0]["c3_shadow_lane"], "RESERVE")
        self.assertEqual(result["c3_shadow_follow_count"], 0)
        self.assertEqual(result["c3_shadow_reserve_count"], 1)

    def test_c3_same_kickoff_follow_is_capped_at_two(self):
        result = run_board(
            {
                "schema_version": "football-engine-v1",
                "stage": "board",
                "model": "c3",
                "matches": [
                    match(
                        "a",
                        carrier="STRONG",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                    ),
                    match(
                        "b",
                        carrier="STRONG",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                    ),
                    match(
                        "c",
                        carrier="STRONG",
                        carrier_self_fund=True,
                        independent_upper_tail=True,
                    ),
                ],
            }
        )
        lanes = [row["c3_shadow_lane"] for row in result["matches"]]
        self.assertEqual(lanes.count("FOLLOW"), 2)
        self.assertEqual(lanes.count("RESERVE"), 1)
        self.assertEqual(result["c3_max_follow_per_exact_kickoff"], 2)

    def test_c3_missing_policy_field_fails_closed(self):
        row = match()
        row.pop("c3_goal3_funding")
        with self.assertRaisesRegex(ContractError, "missing required field: c3_goal3_funding"):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c3",
                    "matches": [row],
                }
            )

    def test_c3_o3_requires_goal4_funding(self):
        with self.assertRaisesRegex(ValueError, "goal4 funding cannot be NOT_REQUIRED"):
            run_board(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "board",
                    "model": "c3",
                    "matches": [
                        match(
                            supported_line=3.0,
                            carrier="STRONG",
                            carrier_self_fund=True,
                            independent_upper_tail=True,
                        )
                    ],
                }
            )

    def test_c3_decision_requires_focus_verified_funding_and_low_control(self):
        good = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c3",
                "match": match(
                    board_state="C3-FOCUS",
                    carrier="STRONG",
                    carrier_self_fund=True,
                    independent_upper_tail=True,
                ),
                "context": decision_context(board_state="C3-FOCUS"),
            }
        )
        self.assertEqual(good["action"], "BET")

        blocked = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c3",
                "match": match(
                    board_state="C3-WATCH",
                    carrier="STRONG",
                    carrier_self_fund=True,
                    independent_upper_tail=True,
                    c3_control_endpoint_risk="MEDIUM",
                ),
                "context": decision_context(board_state="C3-WATCH"),
            }
        )
        self.assertEqual(blocked["action"], "PASS")


class AuditRecordContractTests(unittest.TestCase):
    def audit_record(self, **overrides):
        payload = {
            "schema_version": "football-engine-v1",
            "stage": "audit_record",
            "match_id": "fiorentina-sassuolo",
            "model_version": "Football C",
            "frozen": {
                "c_board_state": "C-FOCUS",
                "follow_lane": "FOLLOW",
                "supported_line": 2.5,
                "completion_mode": "TWO_SIDED",
                "burden_completion_quality": "HIGH",
                "continuation_quality": "HIGH",
                "opponent_leakage": "MEDIUM",
                "burden_stall_risk": "LOW",
                "c_action": "C-BET",
                "quote_line": 2.5,
                "quote_odds": 1.80,
            },
            "observed": {
                "ht_score": "2-0",
                "ft_score": "2-0",
                "settlement": "LOSS",
                "completion_materialized": "NO",
                "continuation_materialized": "NO",
                "carrier_self_fund_materialized": "UNKNOWN",
                "opponent_route_materialized": "NO",
            },
            "diagnosis": {
                "tags": ["MODEL_FALSE_POSITIVE"],
                "pre_freeze_evidence_miss": False,
                "pre_freeze_evidence_note": None,
                "retrospective_hypothesis_only": True,
            },
            "pnl_status": {
                "official_c_exposure": True,
                "official_c_model_pnl": -1.0,
                "user_executed": False,
                "user_pnl": None,
                "c2_shadow_only": False,
            },
        }
        for key, value in overrides.items():
            if key in {"frozen", "observed", "diagnosis", "pnl_status"}:
                payload[key].update(value)
            else:
                payload[key] = value
        return payload

    def test_canonical_hindsight_safe_record_passes(self):
        result = run_audit_record(self.audit_record())
        self.assertEqual(result["frozen"]["continuation_quality"], "HIGH")
        self.assertFalse(result["pnl_status"]["user_executed"])
        self.assertEqual(result["pnl_status"]["official_c_model_pnl"], -1.0)

    def test_compound_grade_is_rejected(self):
        with self.assertRaisesRegex(ContractError, "continuation_quality"):
            run_audit_record(
                self.audit_record(
                    frozen={"continuation_quality": "MEDIUM-HIGH"}
                )
            )

    def test_pre_freeze_miss_requires_contemporaneous_note(self):
        with self.assertRaisesRegex(
            ContractError,
            "pre_freeze_evidence_note is required",
        ):
            run_audit_record(
                self.audit_record(
                    diagnosis={
                        "pre_freeze_evidence_miss": True,
                        "pre_freeze_evidence_note": None,
                        "retrospective_hypothesis_only": False,
                    }
                )
            )

    def test_no_official_exposure_cannot_have_model_pnl(self):
        with self.assertRaisesRegex(
            ContractError,
            "official_c_model_pnl must be null",
        ):
            run_audit_record(
                self.audit_record(
                    observed={"settlement": "NO_OFFICIAL_EXPOSURE"},
                    pnl_status={
                        "official_c_exposure": False,
                        "official_c_model_pnl": -1.0,
                    },
                )
            )

    def test_published_model_exposure_does_not_require_user_bet(self):
        result = run_audit_record(
            self.audit_record(
                pnl_status={
                    "official_c_exposure": True,
                    "official_c_model_pnl": -1.0,
                    "user_executed": False,
                    "user_pnl": None,
                }
            )
        )
        self.assertTrue(result["pnl_status"]["official_c_exposure"])
        self.assertFalse(result["pnl_status"]["user_executed"])

    def test_user_pnl_requires_user_execution(self):
        with self.assertRaisesRegex(
            ContractError,
            "user_pnl must be null when user_executed=false",
        ):
            run_audit_record(
                self.audit_record(
                    pnl_status={
                        "user_executed": False,
                        "user_pnl": -1.0,
                    }
                )
            )


class DecisionContractTests(unittest.TestCase):
    def test_c_decision_is_computed_from_structured_input(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(board_state="C-FOCUS"),
                "context": decision_context(top_ranked_focus=True),
            }
        )
        self.assertEqual(result["action"], "BET")

    def test_missing_xi_status_fails_closed(self):
        ctx = decision_context()
        ctx.pop("xi_status")
        with self.assertRaisesRegex(ContractError, "missing required field: xi_status"):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": ctx,
                }
            )

    def test_unavailable_xi_blocks_decision(self):
        with self.assertRaisesRegex(
            ContractError,
            "DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": decision_context(xi_status="UNAVAILABLE"),
                }
            )

    def test_missing_post_xi_research_status_fails_closed(self):
        ctx = decision_context()
        ctx.pop("post_xi_research_status")
        with self.assertRaisesRegex(
            ContractError,
            "missing required field: post_xi_research_status",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": ctx,
                }
            )

    def test_missing_market_history_status_fails_closed(self):
        ctx = decision_context()
        ctx.pop("market_history_status")
        with self.assertRaisesRegex(
            ContractError,
            "missing required field: market_history_status",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": ctx,
                }
            )

    def test_unavailable_market_history_must_be_unclear(self):
        with self.assertRaisesRegex(
            ContractError,
            "UNAVAILABLE_ATTEMPTED market history requires movement=UNCLEAR",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": decision_context(
                        market_history_status="UNAVAILABLE_ATTEMPTED",
                        market_history_movement="STABLE",
                        market_history_note="history source unavailable after targeted attempt",
                    ),
                }
            )

    def test_unavailable_market_history_can_continue_after_attempt(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(board_state="C-FOCUS"),
                "context": decision_context(
                    market_history_status="UNAVAILABLE_ATTEMPTED",
                    market_history_movement="UNCLEAR",
                    market_history_conflict_recheck="LIMITED",
                    market_history_note="targeted history search attempted; no reliable snapshots found",
                ),
            }
        )
        self.assertEqual(result["market_history_status"], "UNAVAILABLE_ATTEMPTED")
        self.assertEqual(result["market_history_movement"], "UNCLEAR")

    def test_h2h_recheck_missing_blocks_decision(self):
        with self.assertRaisesRegex(
            ContractError,
            "DECISION BLOCKED — H2H RECHECK MISSING",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": decision_context(h2h_rechecked=False),
                }
            )

    def test_completion_recheck_missing_blocks_decision(self):
        with self.assertRaisesRegex(
            ContractError,
            "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": decision_context(completion_rechecked=False),
                }
            )

    def test_missing_suppression_boolean_fails_closed(self):
        row = match(board_state="C-FOCUS")
        row.pop("material_suppression")
        with self.assertRaisesRegex(
            ContractError,
            "missing required field: material_suppression",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": decision_context(),
                }
            )

    def test_missing_failure_attack_boolean_fails_closed(self):
        row = match(board_state="C-FOCUS")
        row.pop("failure_attacks_route")
        with self.assertRaisesRegex(
            ContractError,
            "missing required field: failure_attacks_route",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": decision_context(),
                }
            )

    def test_missing_primary_mechanism_flag_fails_closed(self):
        ctx = decision_context()
        ctx.pop("primary_mechanism_intact")
        with self.assertRaisesRegex(
            ContractError,
            "missing required field: primary_mechanism_intact",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": match(board_state="C-FOCUS"),
                    "context": ctx,
                }
            )

    def test_high_current_stall_risk_cannot_bet(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(
                    board_state="C-FOCUS",
                    burden_stall_risk="HIGH",
                ),
                "context": decision_context(),
            }
        )
        self.assertEqual(result["action"], "PASS")

    def test_low_current_completion_cannot_bet(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(
                    board_state="C-FOCUS",
                    burden_completion_quality="LOW",
                ),
                "context": decision_context(),
            }
        )
        self.assertEqual(result["action"], "PASS")

    def test_low_current_continuation_cannot_bet(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": match(
                    board_state="C-FOCUS",
                    continuation_quality="LOW",
                ),
                "context": decision_context(),
            }
        )
        self.assertEqual(result["action"], "PASS")

    def test_tournament_decision_requires_recheck(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            qualification_state="winner on aggregate advances",
            simultaneous_results_status="NOT_APPLICABLE",
            simultaneous_results_note="no simultaneous result affects this tie",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        with self.assertRaises(ContractError):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": decision_context(
                        tournament_incentive_rechecked=False,
                        tournament_incentive_recheck_status="VERIFIED",
                    ),
                }
            )

    def test_tournament_decision_limited_recheck_is_blocked(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            qualification_state="winner on aggregate advances",
            simultaneous_results_status="NOT_APPLICABLE",
            simultaneous_results_note="no simultaneous result affects this tie",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        with self.assertRaisesRegex(
            ContractError,
            "DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED",
        ):
            run_decision(
                {
                    "schema_version": "football-engine-v1",
                    "stage": "decision",
                    "model": "c",
                    "match": row,
                    "context": decision_context(
                        tournament_incentive_rechecked=True,
                        tournament_incentive_recheck_status="LIMITED",
                    ),
                }
            )

    def test_tournament_decision_with_recheck_passes(self):
        row = match(
            board_state="C-FOCUS",
            tournament_incentive_required=True,
            tournament_format_status="VERIFIED",
            competition_stage="KNOCKOUT",
            competition_format="TWO_LEG",
            draw_resolution="extra time if aggregate level",
            aggregate_state="home trails by one",
            home_incentive="MUST_WIN",
            away_incentive="PROTECT_AGGREGATE",
            tiebreak_margin_relevance="NO",
            incentive_effect="MIXED",
        )
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c",
                "match": row,
                "context": decision_context(
                    tournament_incentive_rechecked=True,
                    tournament_incentive_recheck_status="VERIFIED",
                ),
            }
        )
        self.assertTrue(result["tournament_incentive_rechecked"])

    def test_c2_floor_blocks_weak_protected_line(self):
        result = run_decision(
            {
                "schema_version": "football-engine-v1",
                "stage": "decision",
                "model": "c2",
                "match": match(
                    home_route="USABLE",
                    away_route="WEAK",
                    carrier="USABLE",
                ),
                "context": decision_context(
                    board_state="C2-WATCH",
                    quote={"line": 2.0, "odds": 1.90},
                ),
            }
        )
        self.assertEqual(result["action"], "PASS")
        self.assertNotEqual(result["selection_floor"], "CLEAR")


if __name__ == "__main__":
    unittest.main()
