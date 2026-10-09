import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from sweep_checkpoint import (  # noqa: E402
    CHECKPOINT_VERSION,
    MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK,
    FAST_FINISH_VERIFICATION_BLOCKS_PER_INVOCATION,
    FAST_FINISH_POLICY,
    SOURCE_RECOVERY_COOLDOWN_MINUTES,
    SweepCheckpointError,
    advance_after_chunk,
    mark_source_blocked,
    run_status_for_source_state,
    select_verification_chunk,
    source_retry_decision,
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


def blocked_checkpoint():
    return {
        "checkpoint_version": CHECKPOINT_VERSION,
        "run_id": "SWEEP-BLOCKED",
        "phase": "SOURCE_ACQUISITION",
        "chunk_number": 1,
        "source_acquisition_state": "SOURCE_BLOCKED",
        "source_payload_hash": None,
        "source_blocker_fingerprint": "fp-old",
        "source_last_attempt_at": "2026-10-06T10:00:00+07:00",
        "source_retry_not_before": "2026-10-06T10:30:00+07:00",
        "source_recovery_attempt_count": 1,
        "pending_verification_blocks": [],
        "retry_queue": [],
        "completed_verification_blocks": [],
        "last_completed_block": None,
    }


class SourceRunStatusMappingTests(unittest.TestCase):
    def test_source_state_maps_to_airtable_run_status(self):
        self.assertEqual(run_status_for_source_state("UNTRIED"), "RUNNING")
        self.assertEqual(run_status_for_source_state("ACQUIRED"), "RUNNING")
        self.assertEqual(run_status_for_source_state("SOURCE_BLOCKED"), "BLOCKED")

    def test_source_blocked_is_not_a_run_status_value(self):
        self.assertNotEqual(
            run_status_for_source_state("SOURCE_BLOCKED"),
            "SOURCE_BLOCKED",
        )



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

    def test_new_fast_finish_selects_24_blocks_in_one_invocation(self):
        p = checkpoint(pending=[f"block-{i}" for i in range(31)])
        p["verification_policy"] = FAST_FINISH_POLICY
        chunk = select_verification_chunk(p)
        self.assertEqual(len(chunk.selected_blocks), FAST_FINISH_VERIFICATION_BLOCKS_PER_INVOCATION)
        self.assertEqual(list(chunk.remaining_blocks), [f"block-{i}" for i in range(24, 31)])

    def test_fast_finish_has_finite_retries_not_infinite_resumes(self):
        p = checkpoint(pending=["protected"], retry=[])
        p["verification_policy"] = FAST_FINISH_POLICY
        first = advance_after_chunk(p, completed_blocks=[], retry_blocks=["protected"])
        self.assertEqual(first["pending_verification_blocks"], ["protected"])
        self.assertEqual(first["verification_attempt_counts"]["protected"], 1)
        second = advance_after_chunk(first, completed_blocks=[], retry_blocks=["protected"])
        self.assertEqual(second["phase"], "RECONCILIATION")
        self.assertEqual(second["terminal_unresolved_verification_blocks"], ["protected"])
        self.assertEqual(second["terminal_verification_status"], "BLOCKED_UNRESOLVED")
        self.assertEqual(second["pending_verification_count"], 0)
        with self.assertRaisesRegex(SweepCheckpointError, "unresolved verification blocks"):
            validate_checkpoint({**second, "phase": "COMPLETE"})

    def test_legacy_sweep_retries_remain_backward_compatible(self):
        p = checkpoint(pending=["protected"])
        first = advance_after_chunk(p, completed_blocks=[], retry_blocks=["protected"])
        second = advance_after_chunk(first, completed_blocks=[], retry_blocks=["protected"])
        self.assertEqual(second["pending_verification_blocks"], ["protected"])
        self.assertEqual(second["terminal_unresolved_verification_blocks"], [])

    def test_malformed_fast_attempt_metadata_is_rejected(self):
        p = checkpoint(pending=["a"])
        p["verification_policy"] = FAST_FINISH_POLICY
        p["verification_attempt_counts"] = {"a": -1}
        with self.assertRaisesRegex(SweepCheckpointError, "verification_attempt_counts"):
            validate_checkpoint(p)

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


class SourceRecoveryLeaseTests(unittest.TestCase):
    def test_unchanged_blocker_does_not_retry_inside_lease(self):
        out = source_retry_decision(
            blocked_checkpoint(),
            now="2026-10-06T10:15:00+07:00",
            current_blocker_fingerprint="fp-old",
        )
        self.assertFalse(out["should_retry"])
        self.assertEqual(out["reason"], "SOURCE_RECOVERY_LEASE_ACTIVE")

    def test_unchanged_blocker_retries_after_lease_expiry(self):
        out = source_retry_decision(
            blocked_checkpoint(),
            now="2026-10-06T10:31:00+07:00",
            current_blocker_fingerprint="fp-old",
        )
        self.assertTrue(out["should_retry"])
        self.assertEqual(out["reason"], "SOURCE_RECOVERY_LEASE_EXPIRED")

    def test_changed_fingerprint_retries_immediately(self):
        out = source_retry_decision(
            blocked_checkpoint(),
            now="2026-10-06T10:05:00+07:00",
            current_blocker_fingerprint="fp-new",
        )
        self.assertTrue(out["should_retry"])
        self.assertEqual(out["reason"], "BLOCKER_FINGERPRINT_CHANGED")

    def test_legacy_blocked_checkpoint_without_lease_retries_once(self):
        p = blocked_checkpoint()
        p.pop("source_retry_not_before")
        p.pop("source_last_attempt_at")
        out = source_retry_decision(
            p,
            now="2026-10-06T10:05:00+07:00",
            current_blocker_fingerprint="fp-old",
        )
        self.assertTrue(out["should_retry"])
        self.assertEqual(
            out["reason"], "LEGACY_BLOCKED_CHECKPOINT_NO_RETRY_LEASE"
        )

    def test_mark_source_blocked_creates_retry_lease(self):
        p = blocked_checkpoint()
        p["source_recovery_attempt_count"] = 2
        out = mark_source_blocked(
            p,
            blocker_fingerprint="fp-new",
            attempted_at="2026-10-06T14:25:00+07:00",
        )
        self.assertEqual(out["source_acquisition_state"], "SOURCE_BLOCKED")
        self.assertEqual(out["source_blocker_fingerprint"], "fp-new")
        self.assertEqual(out["source_recovery_attempt_count"], 3)
        self.assertEqual(
            out["source_retry_not_before"],
            "2026-10-06T14:55:00+07:00",
        )
        self.assertEqual(SOURCE_RECOVERY_COOLDOWN_MINUTES, 30)


    def test_real_legacy_source_blocked_cursor_without_chunk_is_recoverable(self):
        legacy = {
            "run_id": "SWEEP-20261006-1145-20261007-0300",
            "checkpoint_version": CHECKPOINT_VERSION,
            "phase": "SOURCE_ACQUISITION",
            "source_acquisition_state": "SOURCE_BLOCKED",
            "window_start_ict": "2026-10-06T11:45:55+07:00",
            "window_end_ict": "2026-10-07T03:00:00+07:00",
            "listing_dates": ["2026-10-06", "2026-10-07"],
            "blocker_fingerprint": {
                "source_acquisition_procedure_sha": "old-procedure",
                "failure_class": "NO_VALID_PROVIDER_DATE_ALL_MATCHES_CARRIER",
            },
        }
        out = source_retry_decision(
            legacy,
            now="2026-10-06T14:25:00+07:00",
            current_blocker_fingerprint="new-current-fingerprint",
        )
        self.assertTrue(out["should_retry"])
        self.assertEqual(
            out["reason"], "LEGACY_BLOCKED_CHECKPOINT_NO_FINGERPRINT"
        )

        migrated = mark_source_blocked(
            legacy,
            blocker_fingerprint="new-current-fingerprint",
            attempted_at="2026-10-06T14:25:00+07:00",
        )
        self.assertEqual(migrated["chunk_number"], 1)
        self.assertNotIn("blocker_fingerprint", migrated)
        self.assertEqual(
            migrated["source_blocker_fingerprint"],
            "new-current-fingerprint",
        )

    def test_retry_timestamp_requires_timezone(self):
        p = blocked_checkpoint()
        p["source_retry_not_before"] = "2026-10-06T10:30:00"
        with self.assertRaises(SweepCheckpointError):
            validate_checkpoint(p)


if __name__ == "__main__":
    unittest.main()
