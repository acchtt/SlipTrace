import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from sweep_checkpoint import (  # noqa: E402
    CHECKPOINT_VERSION,
    MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK,
    SweepCheckpointError,
    advance_after_chunk,
    select_verification_chunk,
    validate_checkpoint,
)


def checkpoint(pending=None, retry=None, completed=None):
    return {
        "checkpoint_version": CHECKPOINT_VERSION,
        "run_id": "SWEEP-TEST",
        "phase": "TARGETED_VERIFICATION",
        "chunk_number": 2,
        "source_acquisition_state": "ACQUIRED",
        "source_payload_hash": "abc123",
        "pending_verification_blocks": pending or [],
        "retry_queue": retry or [],
        "completed_verification_blocks": completed or [],
        "last_completed_block": None,
    }


class SweepCheckpointTests(unittest.TestCase):
    def test_selects_at_most_six_blocks(self):
        pending = [f"block-{i}" for i in range(10)]
        result = select_verification_chunk(checkpoint(pending=pending))
        self.assertEqual(
            len(result.selected_blocks),
            MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK,
        )
        self.assertEqual(list(result.selected_blocks), pending[:6])
        self.assertEqual(list(result.remaining_blocks), pending[6:])

    def test_retry_blocks_are_prioritized_on_resume(self):
        result = select_verification_chunk(
            checkpoint(pending=["new-1", "new-2"], retry=["retry-1"])
        )
        self.assertEqual(result.selected_blocks[0], "retry-1")

    def test_acquired_checkpoint_requires_payload_hash(self):
        p = checkpoint(["a"])
        p["source_payload_hash"] = ""
        with self.assertRaises(SweepCheckpointError):
            validate_checkpoint(p)

    def test_completed_block_cannot_remain_pending(self):
        p = checkpoint(["a"], completed=["a"])
        with self.assertRaises(SweepCheckpointError):
            validate_checkpoint(p)

    def test_advance_moves_retry_to_front_and_increments_chunk(self):
        p = checkpoint(["a", "b", "c"])
        out = advance_after_chunk(
            p,
            completed_blocks=["a"],
            retry_blocks=["b"],
        )
        self.assertEqual(out["chunk_number"], 3)
        self.assertEqual(out["pending_verification_blocks"], ["b", "c"])
        self.assertEqual(out["last_completed_block"], "a")

    def test_advance_to_reconciliation_when_queue_empty(self):
        p = checkpoint(["a"])
        out = advance_after_chunk(p, completed_blocks=["a"])
        self.assertEqual(out["phase"], "RECONCILIATION")
        self.assertEqual(out["pending_verification_count"], 0)

    def test_non_targeted_phase_cannot_select(self):
        p = checkpoint(["a"])
        p["phase"] = "PACKAGING"
        with self.assertRaises(SweepCheckpointError):
            select_verification_chunk(p)


if __name__ == "__main__":
    unittest.main()
