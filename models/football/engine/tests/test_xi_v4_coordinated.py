"""Regression for simplified V4 /xi authority and football-first execution."""
from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ENGINE = HERE.parent
STAGES = ENGINE.parent / "stages_v4"
sys.path.insert(0, str(ENGINE))
sys.path.insert(0, str(STAGES))

from decision_pair_cli import run_football_pair
from stage import rank as v4_rank, sweep as v4_sweep, verify_rank as v4_verify_rank
from step2_queue_guard import Step2QueueError, freeze_queue
from test_adapter import pair_payload
from test_board_pair import c2_row, c_row, payload as board_payload
from test_football_assessment_pair import football
from xi_assessment_reconcile import (
    STATUS_FIELD_ID,
    XIAssessmentReadbackError,
    verify_football_assessment,
)


def digest(value):
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def native_v4_case(*, include_closed_unranked=False):
    run = "V4-20261012-1300"

    def fx(mid, ko):
        games = [
            {
                "kickoff_utc": f"2026-09-{d:02d}T12:00:00Z",
                "goals_for": gf,
                "goals_against": ga,
            }
            for d, (gf, ga) in zip(
                (1, 8, 15, 22), ((3, 2), (2, 1), (4, 1), (2, 2))
            )
        ]
        return {
            "match_id": mid,
            "country": "England",
            "competition": "Premier League",
            "competition_kind": "DOMESTIC_LEAGUE",
            "home": "Home " + mid,
            "away": "Away " + mid,
            "kickoff_utc": ko,
            "fixture_status": "PREMATCH_CONFIRMED",
            "source_url": "https://sports.example.org/fixture/" + mid,
            "observed_at_utc": "2026-10-12T12:59:00Z",
            "football_evidence": {
                side: {
                    "source_url": f"https://results.example.org/{mid}/{side}",
                    "observed_at_utc": "2026-10-12T12:58:00Z",
                    "recent": copy.deepcopy(games),
                }
                for side in ("home", "away")
            },
        }

    fixtures = [fx("fixture-1", "2026-10-12T14:00:00Z")]
    if include_closed_unranked:
        fixtures.append(fx("fixture-2", "2026-10-12T14:30:00Z"))

    original_source = {
        "schema_version": "football-stages-v4",
        "run_id": run,
        "window_start_utc": "2026-10-12T12:50:00Z",
        "window_end_utc": "2026-10-12T16:00:00Z",
        "source_family": "provider-test",
        "source_url": "https://sports.example.org/window",
        "source_observed_at_utc": "2026-10-12T12:59:00Z",
        "fixtures": fixtures,
    }
    sweep = v4_sweep(original_source, now="2026-10-12T13:00:00Z")

    cbase, c2base = c_row(), c2_row()
    c2base["c2_opponent_leakage"] = "HIGH"
    c2base["c2_opponent_leakage_basis"] = (
        "Independent current opponent-specific leakage evidence"
    )
    for row in (cbase, c2base):
        row["match_id"] = "fixture-1"
        row["kickoff_ict"] = "2026-10-12T21:00:00+07:00"
    cin, c2in = board_payload("c", cbase), board_payload("c2", c2base)

    status_refresh = {
        "schema_version": "football-v4-rank-status-refresh-v1",
        "run_id": run,
        "sweep_integrity_sha256": sweep["integrity_sha256"],
        "checked_at_utc": "2026-10-12T13:05:00Z",
        "matches": [
            {
                "match_id": q["match_id"],
                "kickoff_utc": q["kickoff_utc"],
                "fixture_status": (
                    "STARTED"
                    if include_closed_unranked and q["match_id"] == "fixture-2"
                    else "PREMATCH_CONFIRMED"
                ),
                "source_url": q["source_url"],
                "observed_at_utc": "2026-10-12T13:05:00Z",
            }
            for q in sweep["eligible_queue"]
        ],
    }
    unranked = (
        {"fixture-2": "PREMATCH_WINDOW_CLOSED"}
        if include_closed_unranked
        else {}
    )
    rank = v4_rank(
        sweep,
        cin,
        c2in,
        unranked,
        now="2026-10-12T13:05:00Z",
        original_source=original_source,
        status_refresh=status_refresh,
    )
    cr = rank["board_pair"]["results"]["c"]["matches"][0]
    c2r = rank["board_pair"]["results"]["c2"]["matches"][0]
    readback = {
        "active_base_id": "appbzxqXYf0lKfD4P",
        "method": "INDEPENDENT_AIRTABLE_REFETCH",
        "run_id": run,
        "rank_integrity_sha256": rank["integrity_sha256"],
        "sweep_integrity_sha256": rank["sweep_integrity_sha256"],
        "readback_at_utc": "2026-10-12T13:06:00Z",
        "ranked_rows": [
            {
                "match_id": "fixture-1",
                "coverage_id": run + "|fixture-1",
                "follow_lane": cr["follow_lane"],
                "c_rank": cr["rank"],
                "c_board_state": "C-" + cr["board_state"],
                "c_supported_line": cr["supported_line"],
                "c2_rank": c2r["rank"],
                "c2_board_state": "C2-" + c2r["board_state"],
                "c2_supported_line": c2r["supported_line"],
                "step1_engine_c_result": json.dumps(cr, sort_keys=True),
                "step1_engine_c_result_field_id": "fldhUWNoyXzXfQJ3C",
                "step1_engine_c2_result": json.dumps(c2r, sort_keys=True),
                "step1_engine_c2_result_field_id": "fldq0n2tDlS58goAm",
            }
        ],
    }
    verified = v4_verify_rank(readback, rank)
    row = {
        "match_id": "fixture-1",
        "coverage_id": run + "|fixture-1",
        "kickoff_utc": "2026-10-12T14:00:00Z",
        "kickoff_ict": "2026-10-12T21:00:00+07:00",
        "official_follow_lane": cr["follow_lane"],
        "xi_window_open": True,
        "xi_window_basis": "verified current XI window",
        "c_board_state": "C-" + cr["board_state"],
        "c2_shadow_state": "C2-" + c2r["board_state"],
        "c_supported_line": cr["supported_line"],
        "c2_supported_line": c2r["supported_line"],
    }
    return {
        "schema_version": "football-step2-queue-v2",
        "session_id": "XI-V4-TEST",
        "mode": "V4_ROUTINE",
        "board": [row],
        "user_exceptions": [],
        "activated_reserves": [],
        "v4_rank_receipt": rank,
        "v4_persistence_receipt": verified,
    }


def call_xi(fc, fs, pc=None, ps=None):
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        files = {}
        for name, data in (("fc", fc), ("fs", fs), ("pc", pc), ("ps", ps)):
            if data is None:
                continue
            path = root / (name + ".json")
            path.write_text(json.dumps(data), encoding="utf-8")
            files[name] = str(path)
        args = [
            sys.executable,
            str(ENGINE / "xi_portable.py"),
            "xi",
            "--c",
            files["fc"],
            "--c2",
            files["fs"],
        ]
        if "pc" in files:
            args += ["--price-c", files["pc"], "--price-c2", files["ps"]]
        return subprocess.run(
            args, text=True, capture_output=True, timeout=20, check=False
        )


class V4QueueBridgeTests(unittest.TestCase):
    def test_verified_rank_chain_authorizes_routine_follow(self):
        actual = freeze_queue(native_v4_case())
        self.assertEqual(actual["source_run_id"], "V4-20261012-1300")
        self.assertEqual(actual["due_count"], 1)
        self.assertEqual(
            actual["due"][0]["step2_authorization"], "ROUTINE_FOLLOW"
        )
        self.assertTrue(actual["model_evidence_sha256"])

    def test_step2_does_not_require_original_source_or_status_payload_again(self):
        case = native_v4_case()
        self.assertNotIn("v4_original_source", case)
        self.assertNotIn("v4_status_refresh", case)
        self.assertNotIn("v4_sweep_receipt", case)
        self.assertEqual(freeze_queue(case)["due_count"], 1)

    def test_full_status_refresh_can_have_legitimately_unranked_started_fixture(self):
        actual = freeze_queue(native_v4_case(include_closed_unranked=True))
        self.assertEqual(actual["due_count"], 1)
        self.assertEqual(actual["due"][0]["match_id"], "fixture-1")

    def test_rank_or_persistence_proof_cannot_be_removed(self):
        for target, field in (
            ("v4_rank_receipt", "source_replayed"),
            ("v4_rank_receipt", "current_fixture_status_checked"),
            ("v4_persistence_receipt", "source_replayed"),
            ("v4_persistence_receipt", "current_fixture_status_checked"),
            ("v4_persistence_receipt", "model_evidence_readback_verified"),
            ("v4_persistence_receipt", "model_evidence_sha256"),
        ):
            with self.subTest(target=target, field=field):
                case = native_v4_case()
                case[target].pop(field)
                if target == "v4_rank_receipt":
                    case[target]["integrity_sha256"] = digest({
                        k: v
                        for k, v in case[target].items()
                        if k != "integrity_sha256"
                    })
                    case["v4_persistence_receipt"]["rank_sha256"] = (
                        case[target]["integrity_sha256"]
                    )
                with self.assertRaises(Step2QueueError):
                    freeze_queue(case)

    def test_persisted_model_evidence_digest_cannot_drift(self):
        case = native_v4_case()
        case["v4_persistence_receipt"]["model_evidence_sha256"] = "0" * 64
        with self.assertRaisesRegex(Step2QueueError, "model evidence"):
            freeze_queue(case)

    def test_board_lane_or_line_cannot_be_forged(self):
        for field, value in (
            ("official_follow_lane", "STOP"),
            ("c2_supported_line", 3.0),
        ):
            with self.subTest(field=field):
                case = native_v4_case()
                case["board"][0][field] = value
                with self.assertRaises(Step2QueueError):
                    freeze_queue(case)

    def test_exception_authorized_without_board(self):
        case = {
            "schema_version": "football-step2-queue-v2",
            "session_id": "TEST-EXCEPTION",
            "mode": "EXCEPTION_ONLY",
            "board": [],
            "activated_reserves": [],
            "user_exceptions": [
                {
                    "match_id": "new-exception",
                    "user_authorization_reference":
                        "user explicitly requested /xi exception",
                }
            ],
        }
        result = freeze_queue(case)
        self.assertEqual(result["due_count"], 1)
        self.assertEqual(
            result["due"][0]["step2_authorization"], "USER_EXCEPTION"
        )


class FootballFirstExecutionTests(unittest.TestCase):
    def test_no_quote_prematch_started_and_halftime(self):
        for state, minute, score in (
            ("PREMATCH_CONFIRMED", None, None),
            ("STARTED", 3, "0-0"),
            ("STARTED", 17, "1-0"),
            ("HALFTIME", 45, "2-1"),
        ):
            with self.subTest(state=state):
                proc = call_xi(
                    football("c", status=state, minute=minute, score=score),
                    football("c2", status=state, minute=minute, score=score),
                )
                self.assertEqual(proc.returncode, 0, proc.stderr[-500:])
                out = json.loads(proc.stdout)
                self.assertEqual(
                    out["engine_execution_status"],
                    "EXECUTED_C_C2_FOOTBALL_ONLY",
                )
                self.assertFalse(out["model_bets_created"])

    def test_failed_strict_price_never_erases_football(self):
        fc = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        fs = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        pc, ps = pair_payload("c"), pair_payload("c2")
        for item in (pc, ps):
            item["evidence_epoch_id"] = fc["evidence_epoch_id"]
            item["context"]["quote_revalidated"] = False
        proc = call_xi(fc, fs, pc, ps)
        self.assertEqual(proc.returncode, 0, proc.stderr[-900:])
        out = json.loads(proc.stdout)
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
        self.assertEqual(
            out["price_check"]["status"], "EXECUTABLE_PRICE_NOT_AUTHORIZED"
        )
        self.assertEqual(set(out["results"]), {"c", "c2"})

    def test_real_prematch_strict_quote_checked_same_command(self):
        fc = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        fs = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        pc, ps = pair_payload("c"), pair_payload("c2")
        for item in (pc, ps):
            item["evidence_epoch_id"] = fc["evidence_epoch_id"]
            item["match"]["match_id"] = fc["match"]["match_id"]
        proc = call_xi(fc, fs, pc, ps)
        self.assertEqual(proc.returncode, 0, proc.stderr[-900:])
        out = json.loads(proc.stdout)
        self.assertEqual(
            out["xi_mode"], "FOOTBALL_AND_EXECUTABLE_PRICE_CHECK"
        )
        self.assertTrue(out["price_check"]["ok"])
        self.assertEqual(
            out["price_check"]["receipt"]["engine_execution_status"],
            "EXECUTED_C_C2_PAIR",
        )

    def test_started_fixture_closes_strict_prematch_price_path(self):
        fc = football("c", status="STARTED", minute=4, score="0-0")
        fs = football("c2", status="STARTED", minute=4, score="0-0")
        pc, ps = pair_payload("c"), pair_payload("c2")
        for item in (pc, ps):
            item["evidence_epoch_id"] = fc["evidence_epoch_id"]
            item["match"]["match_id"] = fc["match"]["match_id"]
        proc = call_xi(fc, fs, pc, ps)
        self.assertEqual(proc.returncode, 0, proc.stderr[-900:])
        out = json.loads(proc.stdout)
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
        self.assertIn("started fixture", out["price_check"]["reason"])


class XIStoredFootballStatusTests(unittest.TestCase):
    def test_one_readback_status_for_unpriced_or_successful_price(self):
        pair = run_football_pair(football("c"), football("c2"))
        for price, expected in (
            (None, "EXECUTED_C_C2_FOOTBALL_ONLY"),
            (
                {
                    "ok": False,
                    "status": "EXECUTABLE_PRICE_NOT_AUTHORIZED",
                },
                "EXECUTED_C_C2_FOOTBALL_ONLY",
            ),
            (
                {
                    "ok": True,
                    "status": "OBSERVED_QUOTE_EVALUATED",
                    "evidence": {"quote": {"line": 2.5, "odds": 1.7}},
                },
                "EXECUTED_C_C2_FOOTBALL_AND_PRICE",
            ),
        ):
            with self.subTest(expected=expected):
                receipt = {"ok": True, **pair}
                if price is not None:
                    receipt["price_check"] = price
                readback = {
                    "base_id": "appbzxqXYf0lKfD4P",
                    "record_id": "rec1234567890ABCDE",
                    "assessment_id": "XI-C2-EXAMPLE",
                    "match_id": pair["results"]["c"]["match_id"],
                    "readback_method": "INDEPENDENT_AIRTABLE_REFETCH",
                    "xi_status_field_id": STATUS_FIELD_ID,
                    "xi_assessment_execution_status": expected,
                    "engine_c_result": json.dumps(pair["results"]["c"]),
                    "engine_c2_result": pair["results"]["c2"],
                }
                if price and price.get("ok"):
                    readback["evaluated_line"] = 2.5
                    readback["evaluated_odds"] = 1.7
                result = verify_football_assessment(receipt, readback)
                self.assertTrue(result["football_pair_verified"])
                self.assertFalse(result["actual_bet_created"])

                tampered = copy.deepcopy(readback)
                tampered["xi_assessment_execution_status"] = (
                    "ENGINE_FAILED_AFTER_ATTEMPT"
                )
                with self.assertRaisesRegex(
                    XIAssessmentReadbackError, "status"
                ):
                    verify_football_assessment(receipt, tampered)


if __name__ == "__main__":
    unittest.main()
