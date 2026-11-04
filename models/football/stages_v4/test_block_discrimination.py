import unittest

from block_discrimination import POLICY, comparison_blocks, review_block


def raw(
    mid,
    kickoff,
    *,
    activation="MEDIUM",
    leakage="MEDIUM",
    continuation="MEDIUM",
    chance="HIGH",
    completion="HIGH",
):
    return {
        "match_id": mid,
        "kickoff_ict": kickoff,
        "home_route": "STRONG",
        "away_route": "USABLE",
        "route_reliability": "HIGH",
        "chance_quality": chance,
        "burden_completion_quality": completion,
        "continuation_quality": continuation,
        "opponent_leakage": leakage,
        "burden_stall_risk": "MEDIUM",
        "material_suppression": False,
        "failure_attacks_route": False,
        "goal_signal_mean_over_three_rate": 0.45,
        "goal_signal_mean_over_two_rate": 0.65,
        "goal_signal_priority_score": 65,
        "independent_upper_tail": False,
        "upper_tail_transferability": "MEDIUM",
        "activation_quality": activation,
        "activation_basis": (
            "Current prematch attack and defensive opening evidence supports "
            "the frozen activation grade without using bookmaker information."
        ),
        "activation_evidence_refs": [
            "https://club.example/current-football",
            "https://league.example/current-football",
        ],
    }


def compiled(
    mid,
    rank,
    state="FOCUS",
    *,
    mechanism="DISTRIBUTED",
    tail="MIXED",
    goal4=False,
):
    return {
        "match_id": mid,
        "rank": rank,
        "board_state": state,
        "operational_viability_grade": "A",
        "goal3_funded": state == "FOCUS",
        "goal4_funded": goal4,
        "goal5_funded": False,
        "goal6_funded": False,
        "credible_tail_state": tail,
        "g3_endpoint_control_pressure": "MODERATE",
        "follow_clearability_score": 50,
        "execution_strength": "CONDITIONAL",
        "goal3_mechanism_class": mechanism,
        "g3_current_structure_verified": False,
    }


def proof(block_id, ids, rank):
    common = (
        "Source-backed current football comparison establishes a distinct edge "
        "rather than relying on league prestige or bookmaker information."
    )
    return {
        "contract": POLICY,
        "completed": True,
        "market_independent": True,
        "block_id": block_id,
        "candidate_match_ids": ids,
        "same_depth_completed": True,
        "block_rank": rank,
        "evidence_refs": [
            "https://club.example/current-football",
            "https://league.example/current-football",
        ],
        "g3_strength_basis": common,
        "g4_strength_basis": common,
        "carrier_self_funding_basis": common,
        "reply_dependence_basis": common,
        "endpoint_exposure_basis": common,
        "continuation_basis": common,
        "tournament_incentive_basis": common,
        "supported_burden_basis": common,
        "beats_next_basis": common,
    }


class BlockDiscriminationTests(unittest.TestCase):
    def test_nearby_focus_and_watch_form_one_block(self):
        raws = [
            raw("a", "2026-11-04T21:30:00+07:00"),
            raw("b", "2026-11-04T22:00:00+07:00"),
            raw("c", "2026-11-04T22:30:00+07:00"),
        ]
        outs = [
            compiled("a", 1),
            compiled("b", 2, "WATCH"),
            compiled("c", 3),
        ]
        outs[1]["operational_viability_grade"] = "B"
        blocks = comparison_blocks(raws, outs)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["candidate_match_ids"], ["a", "b", "c"])

    def test_distant_candidates_split(self):
        raws = [
            raw("a", "2026-11-04T20:00:00+07:00"),
            raw("b", "2026-11-04T22:00:00+07:00"),
        ]
        outs = [compiled("a", 1), compiled("b", 2)]
        self.assertEqual(comparison_blocks(raws, outs), [])

    def test_missing_comparison_is_pending(self):
        raws = [
            raw("a", "2026-11-04T21:30:00+07:00"),
            raw("b", "2026-11-04T22:00:00+07:00"),
        ]
        outs = [compiled("a", 1), compiled("b", 2)]
        block = comparison_blocks(raws, outs)[0]
        review = review_block(block)
        self.assertEqual(review["status"], "PENDING")
        self.assertTrue(review["block_priority_order"])
        self.assertFalse(review["block_priority_reconciled"])

    def test_complete_comparison_matches_block_priority_not_global_rank(self):
        raws = [
            raw(
                "a",
                "2026-11-04T21:30:00+07:00",
                activation="HIGH",
                leakage="HIGH",
                continuation="HIGH",
            ),
            raw(
                "b",
                "2026-11-04T22:00:00+07:00",
                activation="MEDIUM",
                leakage="MEDIUM",
                continuation="MEDIUM",
            ),
        ]
        # Secondary global /rank says b > a.
        outs = [
            compiled("a", 7, mechanism="LEAKAGE", tail="FUNDED", goal4=True),
            compiled("b", 1, mechanism="CARRIER", tail="REJECTED"),
        ]
        block = comparison_blocks(raws, outs)[0]
        block_id = block["block_id"]
        ids = block["candidate_match_ids"]
        raws[0]["block_comparison"] = proof(block_id, ids, 1)
        raws[1]["block_comparison"] = proof(block_id, ids, 2)
        review = review_block(comparison_blocks(raws, outs)[0])

        self.assertEqual(review["status"], "COMPLETE")
        self.assertTrue(review["block_priority_reconciled"])
        self.assertEqual(review["declared_order"], ["a", "b"])
        self.assertEqual(review["block_priority_order"], ["a", "b"])
        self.assertEqual(review["engine_order"], ["b", "a"])
        self.assertFalse(review["engine_reconciliation_required"])
        self.assertFalse(review["global_rank_is_selection_authority"])

    def test_declared_disagreement_with_block_priority_is_pending(self):
        raws = [
            raw(
                "a",
                "2026-11-04T21:30:00+07:00",
                activation="HIGH",
                leakage="HIGH",
                continuation="HIGH",
            ),
            raw("b", "2026-11-04T22:00:00+07:00"),
        ]
        outs = [compiled("a", 2), compiled("b", 1, mechanism="CARRIER")]
        first = comparison_blocks(raws, outs)[0]
        # Deliberately reverse the BLOCK_PRIORITY_V1 order.
        raws[0]["block_comparison"] = proof(first["block_id"], first["candidate_match_ids"], 2)
        raws[1]["block_comparison"] = proof(first["block_id"], first["candidate_match_ids"], 1)
        review = review_block(comparison_blocks(raws, outs)[0])
        self.assertEqual(review["status"], "PENDING")
        self.assertFalse(review["block_priority_reconciled"])
        self.assertIn(
            "declared_block_order_must_reconcile_with_block_priority_v1",
            review["missing_by_match_id"]["a"],
        )

    def test_missing_activation_evidence_is_pending(self):
        raws = [
            raw("a", "2026-11-04T21:30:00+07:00"),
            raw("b", "2026-11-04T22:00:00+07:00"),
        ]
        raws[1].pop("activation_evidence_refs")
        outs = [compiled("a", 1), compiled("b", 2)]
        first = comparison_blocks(raws, outs)[0]
        ids = first["candidate_match_ids"]
        raws[0]["block_comparison"] = proof(first["block_id"], ids, 1)
        raws[1]["block_comparison"] = proof(first["block_id"], ids, 2)
        review = review_block(comparison_blocks(raws, outs)[0])
        self.assertEqual(review["status"], "PENDING")
        self.assertIsNotNone(review["block_priority_error"])
        self.assertIn("block_priority_v1_input", review["missing_by_match_id"]["b"])


if __name__ == "__main__":
    unittest.main()
