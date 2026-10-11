"""Prospective fast-sweep bounded runtime (existing V1 leases unchanged)."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from sweep_checkpoint import (  # noqa: E402
    CHECKPOINT_VERSION,
    FAST_FINISH_POLICY,
    FAST_FINISH_MAX_ELAPSED_MINUTES,
    FAST_FINISH_V2_POLICY,
    FAST_FINISH_V2_MAX_ELAPSED_MINUTES,
    FAST_FINISH_V2_VERIFICATION_BLOCKS_PER_INVOCATION,
    advance_after_chunk,
    expire_fast_finish_deadline,
    select_verification_chunk,
    validate_checkpoint,
)


ANCHOR = "2026-10-12T00:00:00Z"


def payload(*, phase="TARGETED_VERIFICATION", pending=None):
    return {
        "checkpoint_version": CHECKPOINT_VERSION,
        "run_id": "SWEEP-20261012-0700-20261012-1200",
        "phase": phase,
        "chunk_number": 1,
        "source_acquisition_state": "UNTRIED" if phase == "SOURCE_ACQUISITION" else "ACQUIRED",
        "source_payload_hash": "frozen-diagnostic-seed",
        "source_scope": "BOUNDED_PRODUCTION_DISCOVERY",
        "verification_policy": FAST_FINISH_V2_POLICY,
        "verification_attempt_counts": {},
        "terminal_unresolved_verification_blocks": [],
        "pending_verification_blocks": list(pending or []),
        "retry_queue": [],
        "completed_verification_blocks": [],
        "requested_window": {
            "start_utc": ANCHOR, "end_utc": "2026-10-12T05:00:00Z",
        },
        "discovery_seed_manifest": {"sources": [{"family": "A"}, {"family": "B"}]},
    }


class FastBudgetV2Tests(unittest.TestCase):
    def test_existing_v1_keeps_original_sixty_minutes(self):
        p = payload(pending=["women"])
        p["verification_policy"] = FAST_FINISH_POLICY
        self.assertEqual(FAST_FINISH_MAX_ELAPSED_MINUTES, 60)
        within = expire_fast_finish_deadline(p, now="2026-10-12T00:16:00Z")
        self.assertEqual(within["deadline_status"], "WITHIN_BUDGET")
        self.assertEqual(within["deadline_minutes"], 60)

    def test_new_acquisition_stage_expires_by_three_minutes(self):
        p = payload(phase="SOURCE_ACQUISITION")
        self.assertEqual(FAST_FINISH_V2_MAX_ELAPSED_MINUTES, 15)
        within = expire_fast_finish_deadline(p, now="2026-10-12T00:02:59Z")
        self.assertEqual(within["deadline_status"], "WITHIN_BUDGET")
        expired = expire_fast_finish_deadline(p, now="2026-10-12T00:03:00Z")
        self.assertEqual(expired["deadline_status"], "BLOCKED_TIME_BUDGET_UNVERIFIED")
        self.assertEqual(expired["phase"], "SOURCE_ACQUISITION")
        self.assertTrue(expired["terminal_budget_locked"])
        self.assertIn("SOURCE_OR_DISCOVERY_NOT_RECONCILED",
                      expired["terminal_unresolved_verification_blocks"])
        self.assertFalse(expired["work_ready"])
        validate_checkpoint(expired)

    def test_discovery_stops_by_five_minutes_even_without_pending(self):
        p = payload(phase="DISCOVERY_CLASSIFICATION")
        expired = expire_fast_finish_deadline(p, now="2026-10-12T00:05:00Z")
        self.assertEqual(expired["deadline_status"], "BLOCKED_TIME_BUDGET_UNVERIFIED")
        self.assertIn("FULL_SOURCE_FIXTURE_INVENTORY_NOT_VERIFIED",
                      expired["terminal_unresolved_verification_blocks"])
        self.assertEqual(expired["discovery_seed_manifest"], p["discovery_seed_manifest"])

    def test_targeted_verification_stops_by_twelve_minutes(self):
        p = payload(pending=["WOMENS_SCOPE", "INVENTORY_PROOF"],)
        within = expire_fast_finish_deadline(p, now="2026-10-12T00:11:59Z")
        self.assertEqual(within["deadline_status"], "WITHIN_BUDGET")
        expired = expire_fast_finish_deadline(p, now="2026-10-12T00:12:00Z")
        self.assertEqual(expired["phase"], "RECONCILIATION")
        self.assertEqual(expired["pending_verification_blocks"], [])
        self.assertEqual(expired["terminal_unresolved_verification_blocks"][:2],
                         ["WOMENS_SCOPE", "INVENTORY_PROOF"])
        self.assertTrue(expired["terminal_budget_locked"])
        self.assertFalse(expired["actionable_complete"])
        again = expire_fast_finish_deadline(expired, now="2026-10-12T00:13:00Z")
        self.assertEqual(again["terminal_unresolved_verification_blocks"],
                         expired["terminal_unresolved_verification_blocks"])

    def test_no_pending_is_not_proof_of_global_completeness(self):
        p = payload(phase="RECONCILIATION")
        status = expire_fast_finish_deadline(p, now="2026-10-12T00:15:00Z")
        self.assertEqual(status["deadline_status"], "BLOCKED_TIME_BUDGET_UNVERIFIED")
        self.assertIn("GLOBAL_SENIOR_WOMENS_TOPFLIGHT_AISCORE_SCOPE_ATTESTATION",
                      status["terminal_unresolved_verification_blocks"])

    def test_packaging_can_finish_without_external_calls_after_verified_reconciliation(self):
        p = payload(phase="PACKAGING")
        p.update({
            "reconciliation_complete": True,
            "required_competition_blocks_complete": True,
            "women_top_flight_global_confirmed": True,
            "final_source_fixture_inventory_hash": "sha256-verified-full",
        })
        result = expire_fast_finish_deadline(p, now="2026-10-12T00:16:00Z")
        self.assertEqual(result["deadline_status"], "PACKAGE_VERIFIED_OFFLINE_ONLY")
        self.assertFalse(result["external_lookup_allowed"])
        p["women_top_flight_global_confirmed"] = False
        blocked = expire_fast_finish_deadline(p, now="2026-10-12T00:16:00Z")
        self.assertEqual(blocked["deadline_status"], "BLOCKED_TIME_BUDGET_UNVERIFIED")

    def test_fast_v2_limits_to_eight_logical_blocks_one_attempt_each(self):
        p = payload(pending=[f"block-{i}" for i in range(20)])
        selection = select_verification_chunk(p)
        self.assertEqual(len(selection.selected_blocks),
                         FAST_FINISH_V2_VERIFICATION_BLOCKS_PER_INVOCATION)
        self.assertEqual(len(selection.remaining_blocks), 12)
        after = advance_after_chunk(p, completed_blocks=[], retry_blocks=["block-0"])
        self.assertIn("block-0", after["terminal_unresolved_verification_blocks"])
        self.assertNotIn("block-0", after["pending_verification_blocks"])
        self.assertEqual(after["verification_attempt_counts"]["block-0"], 1)

    def test_cli_select_requires_clock_and_stops_expired_research(self):
        p = payload(pending=["women"])
        with tempfile.TemporaryDirectory() as root:
            path = pathlib.Path(root) / "cursor.json"
            path.write_text(json.dumps(p))
            cli = ENGINE / "sweep_checkpoint_cli.py"
            cmd = [sys.executable, str(cli), "select", "--input", str(path)]
            missing = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(missing.returncode, 2)
            self.assertIn("requires --now", missing.stderr)
            expired = subprocess.run(cmd + ["--now", "2026-10-12T00:13:00Z"],
                                     capture_output=True, text=True)
            self.assertEqual(expired.returncode, 2)
            self.assertIn("PERSIST DEADLINE RECEIPT", expired.stderr)
            self.assertIn("BLOCKED_TIME_BUDGET_UNVERIFIED", expired.stderr)
            within = subprocess.run(cmd + ["--now", "2026-10-12T00:01:00Z"],
                                    capture_output=True, text=True)
            self.assertEqual(within.returncode, 0, within.stderr)


if __name__ == "__main__":
    unittest.main()
