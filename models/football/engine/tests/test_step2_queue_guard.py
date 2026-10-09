import copy
import pathlib
import sys
import unittest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE_DIR))

from step2_queue_guard import Step2QueueError, freeze_queue  # noqa: E402


def payload():
    def match(match_id, lane, window=True, **kwargs):
        return dict(
            match_id=match_id,
            kickoff_ict="2026-10-09T20:00:00+07:00",
            official_follow_lane=lane,
            xi_window_open=window,
            xi_window_basis="Explicit current-session fixture timing check",
            c_board_state="C-FOCUS" if lane != "STOP" else "C-WATCH",
            c2_shadow_state="C2-FOCUS",
            c_supported_line=2.5,
            c2_supported_line=2.25,
            c2_supported_line_basis="Independently frozen C2 burden",
            **kwargs,
        )
    return {
        "schema_version": "football-step2-queue-v1",
        "session_id": "S2-20261009-frozen-synthetic",
        "mode": "ROUTINE",
        "source_run": {
            "run_id": "SWEEP-20261009-1300-20261010-0300",
            "source_snapshot_id": "synthetic-frozen-source-manifest",
            "status": "COMPLETE",
            "packaging_complete": True,
            "work_ready": True,
        },
        "rank": {
            "status": "TERMINAL_COMPLETE",
            "board_pair_execution_status": "EXECUTED_C_C2_BOARDS",
            "common_evidence_reconciled": True,
            "board_snapshot_id": "synthetic-C+C2-frozen-pair",
        },
        "board": [
            match("follow-open", "FOLLOW"),
            match("follow-later", "FOLLOW", window=False),
            match("reserve-activated", "RESERVE", window=False),
            match("reserve-idle", "RESERVE"),
            match("stop-exception", "STOP"),
            match("stop-idle", "STOP"),
        ],
        "activated_reserves": [
            {"match_id": "reserve-activated", "activation_reference": "USER-RESERVE-1"},
        ],
        "user_exceptions": [
            {"match_id": "stop-exception", "user_authorization_reference": "USER-EXCEPTION-1"},
            {"match_id": "exception-outside-board", "user_authorization_reference": "USER-EXCEPTION-2"},
        ],
    }


class Step2QueueTests(unittest.TestCase):
    def test_frozen_due_set_uses_c_only_with_explicit_overrides(self):
        result = freeze_queue(payload())
        due = {x["match_id"]: x for x in result["due"]}
        self.assertEqual(set(due), {"follow-open", "reserve-activated", "stop-exception", "exception-outside-board"})
        self.assertEqual(due["follow-open"]["step2_authorization"], "ROUTINE_FOLLOW")
        self.assertEqual(due["reserve-activated"]["step2_authorization"], "RESERVE_ACTIVATED")
        self.assertEqual(due["exception-outside-board"]["official_follow_lane"], "STOP")
        self.assertEqual(result["user_exception_count"], 2)
        self.assertEqual(result["board_fixture_count"], 6)
        self.assertEqual(len(result["not_due"]), 3)

    def test_current_unfinished_sweep_cannot_authorize_routine_xi(self):
        row = payload()
        row["source_run"]["status"] = "RUNNING"
        with self.assertRaisesRegex(Step2QueueError, "SWEEP INCOMPLETE"):
            freeze_queue(row)

    def test_missing_work_ready_blocks(self):
        row = payload()
        row["source_run"]["work_ready"] = False
        with self.assertRaisesRegex(Step2QueueError, "STEP0 NOT WORK-READY"):
            freeze_queue(row)

    def test_missing_pair_execution_blocks(self):
        row = payload()
        row["rank"]["board_pair_execution_status"] = "ENGINE_NOT_RUN"
        with self.assertRaisesRegex(Step2QueueError, "C/C2 BOARD PAIR MISSING"):
            freeze_queue(row)

    def test_c2_frozen_line_required(self):
        row = payload()
        row["board"][0]["c2_supported_line"] = None
        with self.assertRaisesRegex(Step2QueueError, "c2_supported_line"):
            freeze_queue(row)

    def test_excluded_never_enters_rank_board(self):
        row = payload()
        row["board"][0]["eligibility"] = "EXCLUDED"
        with self.assertRaisesRegex(Step2QueueError, "EXCLUDED FIXTURE"):
            freeze_queue(row)

    def test_reserve_cannot_self_activate(self):
        row = payload()
        row["activated_reserves"][0]["match_id"] = "stop-idle"
        with self.assertRaisesRegex(Step2QueueError, "UNAUTHORIZED RESERVE"):
            freeze_queue(row)

    def test_duplicate_match_rejected(self):
        row = payload()
        row["board"].append(copy.deepcopy(row["board"][0]))
        with self.assertRaisesRegex(Step2QueueError, "DUPLICATE BOARD"):
            freeze_queue(row)

    def test_exception_only_does_not_need_finished_board(self):
        row = payload()
        row.update(mode="EXCEPTION_ONLY", board=[], activated_reserves=[])
        result = freeze_queue(row)
        self.assertEqual(result["due_count"], 2)
        self.assertTrue(all(x["step2_authorization"] == "USER_EXCEPTION" for x in result["due"]))
        self.assertIsNone(result["source_run_id"])

    def test_exception_only_must_not_smuggle_unverified_routine_rows(self):
        row = payload()
        row["mode"] = "EXCEPTION_ONLY"
        with self.assertRaisesRegex(Step2QueueError, "cannot import unverified board"):
            freeze_queue(row)

    def test_exception_reference_is_mandatory(self):
        row = payload()
        row["user_exceptions"][0]["user_authorization_reference"] = ""
        with self.assertRaisesRegex(Step2QueueError, "user_authorization_reference"):
            freeze_queue(row)


if __name__ == "__main__":
    unittest.main()
