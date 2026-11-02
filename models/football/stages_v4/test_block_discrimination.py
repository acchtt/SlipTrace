import unittest

from block_discrimination import POLICY, comparison_blocks, review_block


def raw(mid, kickoff):
    return {
        "match_id": mid,
        "kickoff_ict": kickoff,
    }


def compiled(mid, rank, state="FOCUS"):
    return {
        "match_id": mid,
        "rank": rank,
        "board_state": state,
        "operational_viability_grade": "A",
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
            raw("a", "2026-11-02T21:30:00+07:00"),
            raw("b", "2026-11-02T22:00:00+07:00"),
            raw("c", "2026-11-02T22:30:00+07:00"),
        ]
        outs = [
            compiled("a", 1),
            compiled("b", 2, "WATCH"),
            compiled("c", 3),
        ]
        blocks = comparison_blocks(raws, outs)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["candidate_match_ids"], ["a", "b", "c"])

    def test_distant_candidates_split(self):
        raws = [
            raw("a", "2026-11-02T20:00:00+07:00"),
            raw("b", "2026-11-02T22:00:00+07:00"),
        ]
        outs = [compiled("a", 1), compiled("b", 2)]
        self.assertEqual(comparison_blocks(raws, outs), [])

    def test_missing_comparison_is_pending(self):
        raws = [
            raw("a", "2026-11-02T21:30:00+07:00"),
            raw("b", "2026-11-02T22:00:00+07:00"),
        ]
        outs = [compiled("a", 1), compiled("b", 2)]
        block = comparison_blocks(raws, outs)[0]
        review = review_block(block)
        self.assertEqual(review["status"], "PENDING")
        self.assertFalse(review["engine_reconciled"])

    def test_complete_comparison_must_match_engine_relative_order(self):
        raws = [
            raw("a", "2026-11-02T21:30:00+07:00"),
            raw("b", "2026-11-02T22:00:00+07:00"),
        ]
        outs = [compiled("a", 3), compiled("b", 7)]
        block = comparison_blocks(raws, outs)[0]
        block_id = block["block_id"]
        ids = block["candidate_match_ids"]
        raws[0]["block_comparison"] = proof(block_id, ids, 1)
        raws[1]["block_comparison"] = proof(block_id, ids, 2)
        block = comparison_blocks(raws, outs)[0]
        review = review_block(block)
        self.assertEqual(review["status"], "COMPLETE")
        self.assertTrue(review["engine_reconciled"])
        self.assertEqual(review["declared_order"], ["a", "b"])

    def test_disagreement_requires_grade_reconciliation_not_override(self):
        raws = [
            raw("a", "2026-11-02T21:30:00+07:00"),
            raw("b", "2026-11-02T22:00:00+07:00"),
        ]
        outs = [compiled("a", 1), compiled("b", 2)]
        first = comparison_blocks(raws, outs)[0]
        raws[0]["block_comparison"] = proof(first["block_id"], first["candidate_match_ids"], 2)
        raws[1]["block_comparison"] = proof(first["block_id"], first["candidate_match_ids"], 1)
        review = review_block(comparison_blocks(raws, outs)[0])
        self.assertEqual(review["status"], "PENDING")
        self.assertFalse(review["engine_reconciled"])
        self.assertIn(
            "declared_block_order_must_reconcile_with_engine_inputs",
            review["missing_by_match_id"]["a"],
        )


if __name__ == "__main__":
    unittest.main()
