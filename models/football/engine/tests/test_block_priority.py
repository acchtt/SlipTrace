import pathlib
import sys
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from block_priority import (  # noqa: E402
    BlockPriorityError,
    block_priority_key,
    rank_block,
)
from block_runtime import BlockRuntimeError, run_block  # noqa: E402
from xi_authority import RankAuthorityError, _validate_assessment_depth  # noqa: E402
from test_board_pair import c_row  # noqa: E402


def raw(
    mid,
    *,
    activation="MEDIUM",
    leakage="MEDIUM",
    continuation="MEDIUM",
    chance="HIGH",
    completion="HIGH",
    route="STRONG",
    other_route="USABLE",
    over3=0.45,
    over2=0.65,
    signal=65,
    stall="MEDIUM",
):
    return {
        "match_id": mid,
        "home_route": route,
        "away_route": other_route,
        "route_reliability": "HIGH",
        "chance_quality": chance,
        "burden_completion_quality": completion,
        "continuation_quality": continuation,
        "opponent_leakage": leakage,
        "burden_stall_risk": stall,
        "material_suppression": False,
        "failure_attacks_route": False,
        "goal_signal_mean_over_three_rate": over3,
        "goal_signal_mean_over_two_rate": over2,
        "goal_signal_priority_score": signal,
        "activation_quality": activation,
        "activation_basis": (
            "Frozen prematch current attacking structure and opponent opening "
            "patterns support this activation grade without using market prices."
        ),
        "activation_evidence_refs": [
            "https://club.example/current-attack",
            "https://league.example/current-defence",
        ],
        "independent_upper_tail": False,
        "upper_tail_transferability": "MEDIUM",
    }


def compiled(
    mid,
    *,
    global_rank=1,
    state="FOCUS",
    goal3=True,
    goal4=False,
    tail="MIXED",
    endpoint="MODERATE",
    clearability=50,
    execution="CONDITIONAL",
    mechanism="DISTRIBUTED",
    current_verified=False,
):
    return {
        "match_id": mid,
        "rank": global_rank,
        "board_state": state,
        "goal3_funded": goal3,
        "goal4_funded": goal4,
        "goal5_funded": False,
        "goal6_funded": False,
        "credible_tail_state": tail,
        "g3_endpoint_control_pressure": endpoint,
        "follow_clearability_score": clearability,
        "execution_strength": execution,
        "goal3_mechanism_class": mechanism,
        "g3_current_structure_verified": current_verified,
        "operational_viability_grade": "A",
    }


class BlockPriorityTests(unittest.TestCase):
    def test_high_activation_leakage_tail_beats_lower_tail_carrier(self):
        carrier = raw(
            "carrier",
            activation="MEDIUM",
            leakage="MEDIUM",
            continuation="MEDIUM",
            over3=0.45,
            over2=0.60,
            signal=62,
        )
        volatile = raw(
            "volatile",
            activation="HIGH",
            leakage="HIGH",
            continuation="HIGH",
            over3=0.70,
            over2=0.88,
            signal=82,
        )
        carrier_c = compiled(
            "carrier",
            global_rank=1,
            tail="REJECTED",
            clearability=58,
            execution="ROBUST",
            mechanism="CARRIER",
        )
        volatile_c = compiled(
            "volatile",
            global_rank=9,
            goal4=True,
            tail="FUNDED",
            endpoint="NONE",
            clearability=52,
            execution="CONDITIONAL",
            mechanism="LEAKAGE",
        )

        ranked = rank_block(
            [carrier, volatile],
            [carrier_c, volatile_c],
        )
        self.assertEqual(ranked[0]["match_id"], "volatile")
        self.assertEqual(ranked[1]["match_id"], "carrier")

    def test_global_rank_has_no_block_selection_authority(self):
        a = raw("a", activation="HIGH", leakage="HIGH", continuation="HIGH")
        b = raw("b", activation="MEDIUM", leakage="MEDIUM", continuation="MEDIUM")
        outs = [
            compiled("a", global_rank=99, mechanism="LEAKAGE"),
            compiled("b", global_rank=1, mechanism="CARRIER"),
        ]
        self.assertEqual(rank_block([a, b], outs)[0]["match_id"], "a")

    def test_positive_carrier_control_survives_when_earlier_axes_tie(self):
        carrier = raw("carrier", activation="HIGH", leakage="HIGH", continuation="HIGH")
        leakage = raw("leakage", activation="HIGH", leakage="HIGH", continuation="HIGH")
        carrier_c = compiled(
            "carrier", mechanism="CARRIER", endpoint="NONE", clearability=55
        )
        leakage_c = compiled(
            "leakage", mechanism="LEAKAGE", endpoint="NONE", clearability=55
        )
        self.assertEqual(
            rank_block([leakage, carrier], [leakage_c, carrier_c])[0]["match_id"],
            "carrier",
        )

    def test_fake_chaos_cannot_beat_viable_funded_candidate(self):
        fake = raw(
            "fake",
            activation="HIGH",
            leakage="HIGH",
            continuation="HIGH",
            chance="LOW",
            over3=0.80,
            over2=0.90,
            signal=90,
        )
        good = raw(
            "good",
            activation="MEDIUM",
            leakage="MEDIUM",
            continuation="MEDIUM",
            chance="MEDIUM",
            completion="MEDIUM",
            over3=0.40,
            over2=0.60,
            signal=55,
        )
        fake_c = compiled(
            "fake", state="WATCH", goal3=False, mechanism="NONE", clearability=70
        )
        good_c = compiled(
            "good", state="FOCUS", goal3=True, mechanism="DISTRIBUTED", clearability=40
        )
        self.assertEqual(
            rank_block([fake, good], [fake_c, good_c])[0]["match_id"],
            "good",
        )

    def test_activation_is_required_and_source_backed(self):
        row = raw("thin")
        row.pop("activation_evidence_refs")
        with self.assertRaisesRegex(BlockPriorityError, "activation_evidence_refs"):
            block_priority_key(row, compiled("thin"))

    def test_outcome_or_price_fields_are_forbidden(self):
        row = raw("bad")
        row["final_score"] = "4-3"
        with self.assertRaisesRegex(BlockPriorityError, "forbids outcome/price"):
            block_priority_key(row, compiled("bad"))

    def test_key_places_mechanism_after_activation_and_tail(self):
        carrier = raw("carrier", activation="MEDIUM")
        better = raw("better", activation="HIGH")
        self.assertGreater(
            block_priority_key(
                better,
                compiled("better", mechanism="DISTRIBUTED"),
            ),
            block_priority_key(
                carrier,
                compiled("carrier", mechanism="CARRIER"),
            ),
        )


class BlockRuntimeTests(unittest.TestCase):
    def _engine_row(self, mid, activation):
        row = c_row()
        row["match_id"] = mid
        row["activation_quality"] = activation
        row["activation_basis"] = (
            "Two frozen prematch football sources establish how quickly the "
            "current scoring and leakage mechanisms can open this fixture."
        )
        row["activation_evidence_refs"] = [
            "https://example.com/current-attack",
            "https://example.org/current-leakage",
        ]
        return row

    def test_runtime_is_football_only_and_never_publishes_action(self):
        result = run_block({
            "schema_version": "football-block-runtime-v1",
            "model": "c",
            "matches": [
                self._engine_row("block-a", "HIGH"),
                self._engine_row("block-b", "MEDIUM"),
            ],
        })
        self.assertFalse(result["priced_publication_authorized"])
        self.assertEqual(
            result["publication_status"],
            "FOOTBALL_ASSESSMENT_ONLY_PRICED_DECISION_NOT_PERSISTED",
        )
        self.assertTrue(all(row["priced_action"] is None for row in result["matches"]))

    def test_runtime_rejects_price_input(self):
        with self.assertRaisesRegex(BlockRuntimeError, "football-only"):
            run_block({
                "schema_version": "football-block-runtime-v1",
                "model": "c",
                "quote": {"line": 3.0, "odds": 1.95},
                "matches": [
                    self._engine_row("block-a", "HIGH"),
                    self._engine_row("block-b", "MEDIUM"),
                ],
            })


class AssessmentDepthV2Tests(unittest.TestCase):
    def _payload(self, when, contract, *, activation=True):
        refs = [
            "https://club.example/current-attack",
            "https://league.example/current-defence",
        ]
        checks = {
            "primary_scoring_route": "Current primary scoring route is source-backed and intact.",
            "secondary_reply_route": "Current reply route is independently checked and source-backed.",
            "carrier_capacity": "Carrier capacity is assessed from current prematch football evidence.",
            "current_chance_creation": "Current chance creation is assessed from recent comparable football.",
            "goal3_mechanism": "The explicit third-goal mechanism is frozen before any price comparison.",
            "goal4_mechanism": "The fourth-goal mechanism is independently funded or explicitly rejected.",
            "stall_0_0": "The zero-zero stall route is explicitly assessed from current structure.",
            "stall_1_1": "The one-one stall route is explicitly assessed from current structure.",
            "continuation_2_0": "Continuation from a two-goal lead is explicitly assessed prospectively.",
            "opponent_leakage": "Opponent leakage is frozen from current matchup-specific football evidence.",
            "named_failure_mechanism": "The principal named failure mechanism is frozen before publication.",
            "availability_replacements": "Current availability and replacement quality are independently checked.",
            "h2h_transferability": "Head-to-head evidence is checked for current transferability before use.",
            "tournament_incentive": "Tournament format and incentive state are resolved prospectively.",
            "match_context": "Rivalry rest travel and fatigue context are checked prospectively.",
            "supported_burden_basis": "Supported burden basis is separated from bookmaker price information.",
        }
        match = {"match_id": "depth-v2"}
        if activation:
            match.update(
                activation_quality="HIGH",
                activation_basis=(
                    "Current attack availability, early chance creation and opponent "
                    "opening patterns jointly support a high activation grade."
                ),
                activation_evidence_refs=refs,
            )
        return {
            "evidence_epoch_id": "DEPTH-V2-EPOCH",
            "context": {"assessment_at_utc": when},
            "match": match,
            "assessment_depth": {
                "contract": contract,
                "completed": True,
                "market_independent": True,
                "evidence_epoch_id": "DEPTH-V2-EPOCH",
                "assessed_at_utc": when,
                "evidence_refs": refs,
                "checks": checks,
            },
        }

    def test_v1_remains_valid_for_pre_v2_frozen_epoch(self):
        trace = _validate_assessment_depth(
            self._payload(
                "2026-11-03T12:00:00+00:00",
                "ASSESSMENT_DEPTH_V1",
                activation=False,
            )
        )
        self.assertEqual(trace["contract"], "ASSESSMENT_DEPTH_V1")
        self.assertIsNone(trace["activation"])

    def test_v2_requires_activation_evidence(self):
        with self.assertRaisesRegex(RankAuthorityError, "activation_quality"):
            _validate_assessment_depth(
                self._payload(
                    "2026-11-04T01:00:00+00:00",
                    "ASSESSMENT_DEPTH_V2",
                    activation=False,
                )
            )

    def test_v2_activation_is_selection_only(self):
        trace = _validate_assessment_depth(
            self._payload(
                "2026-11-04T01:00:00+00:00",
                "ASSESSMENT_DEPTH_V2",
            )
        )
        self.assertEqual(trace["contract"], "ASSESSMENT_DEPTH_V2")
        self.assertTrue(trace["activation"]["block_selection_only"])
        self.assertFalse(trace["activation"]["certificate_authority"])
        self.assertFalse(trace["activation"]["price_execution_authority"])


if __name__ == "__main__":
    unittest.main()
