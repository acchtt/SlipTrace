"""Observed screenshot quote uses canonical Football C policy only."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ENGINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

from test_football_assessment_pair import football
from xi_assessment_reconcile import (
    STATUS_COLUMN,
    XIAssessmentReadbackError,
    verify_football_assessment,
)

CAPTURE = "2026-10-11T05:05:00+00:00"


def snapshot(c, *, line=2.5, odds=1.70, captured=CAPTURE, **changes):
    obj = {
        "evidence_mode": "USER_SCREENSHOT_ONLY",
        "source": "USER_SCREENSHOT",
        "capture_reference": "user-attachment-screenshot-1",
        "match_id": c["match"]["match_id"],
        "bookmaker": "User-displayed bookmaker",
        "quote": {"line": line, "odds": odds},
        "observed_at_utc": captured,
        "fixture_status": c["context"]["fixture_status"],
        "score": c["context"]["score"],
        "match_minute": c["context"]["match_minute"],
    }
    obj.update(changes)
    return obj


def complete_market_disagreement_recheck(payload, *, fields=None):
    payload["context"].update(
        market_disagreement_recheck_status="COMPLETED",
        market_disagreement_recheck_basis=(
            "Current football evidence was rechecked against the higher "
            "screenshot burden and the deterministic certificate was rerun."
        ),
        market_disagreement_recheck_fields=(
            fields
            if fields is not None
            else [
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            ]
        ),
        market_disagreement_recheck_evidence_refs=[
            "source-backed-current-football-recheck-1"
        ],
    )
    return payload


def wait_ready(payload, *, top=False):
    payload["match"].update(
        carrier="STRONG",
        carrier_self_fund=True,
        carrier_self_fund_basis=(
            "Strong current carrier independently funds the frozen protected burden."
        ),
        independent_upper_tail=True,
        independent_upper_tail_basis=(
            "Separate current non-market upper-tail route is verified."
        ),
    )
    payload["context"].update(
        thesis_state="PRESERVED",
        primary_mechanism_intact=True,
        material_veto=False,
        material_event_since_frozen="NONE_VERIFIED",
        wait_reachable=True,
        wait_reachability_basis=(
            "clean clock decay to the model's frozen burden is reachable "
            "without requiring a negative football event"
        ),
        wait_requires_negative_info=False,
        wait_negative_info_basis="no negative information required",
        top_ranked_focus=top,
    )
    return payload


def run_xi(c=None, shot=None):
    c = c or football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
    shot = shot if shot is not None else snapshot(c)
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        cp = root / "c.json"
        sp = root / "shot.json"
        cp.write_text(json.dumps(c), encoding="utf-8")
        sp.write_text(json.dumps(shot), encoding="utf-8")
        proc = subprocess.run(
            [
                sys.executable,
                str(ENGINE / "xi_portable.py"),
                "xi",
                "--c",
                str(cp),
                "--screenshot-quote",
                str(sp),
            ],
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if proc.returncode:
            raise AssertionError(proc.stderr)
        return json.loads(proc.stdout)


class ScreenshotOnlyXIRegression(unittest.TestCase):
    def test_exact_screenshot_quote_is_preserved(self):
        out = run_xi()
        self.assertEqual(out["xi_mode"], "FOOTBALL_AND_OBSERVED_QUOTE")
        price = out["price_check"]
        self.assertTrue(price["ok"])
        self.assertEqual(price["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertEqual(price["evidence"]["quote"], {"line": 2.5, "odds": 1.7})
        self.assertEqual(
            price["evidence"]["capture_reference"],
            "user-attachment-screenshot-1",
        )
        self.assertFalse(price["execution_authorized"])
        self.assertFalse(price["bet_authorized"])
        self.assertIn("model", price)
        self.assertNotIn("models", price)

    def test_no_external_or_replacement_quote(self):
        out = run_xi()
        evidence = out["price_check"]["evidence"]
        self.assertEqual(evidence["external_price_searches"], 0)
        self.assertEqual(evidence["replacement_quotes"], 0)
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_missing_capture_time_is_not_retimed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=None))
        price = out["price_check"]
        self.assertIsNone(price["evidence"]["observed_at_utc"])
        self.assertIsNone(price["evidence"]["observation_age_seconds"])
        self.assertIn("SCREENSHOT_CAPTURE_TIME_UNKNOWN", price["limitations"])

    def test_live_screenshot_never_recreates_prematch_action(self):
        c = football("c")
        out = run_xi(c, snapshot(c))
        price = out["price_check"]
        self.assertEqual(price["evidence"]["score"], "1-0")
        self.assertEqual(price["evidence"]["match_minute"], 5)
        self.assertEqual(
            price["model"]["conditional_action"],
            "LIVE_PRICE_BURDEN_COMPARISON_ONLY",
        )
        self.assertFalse(price["execution_authorized"])

    def test_invalid_screenshot_blocks_price_only_not_football(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, match_id="wrong-id"))
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
        self.assertEqual(out["price_check"]["status"], "OBSERVED_QUOTE_INVALID")
        self.assertEqual(
            out["engine_execution_status"],
            "EXECUTED_C_FOOTBALL_ONLY",
        )
        self.assertEqual(out["model"], "c")
        self.assertEqual(out["result"]["model"], "c")

    def test_wait_comes_from_explicit_reachability(self):
        c = complete_market_disagreement_recheck(
            wait_ready(
                football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
            )
        )
        out = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        verdict = out["price_check"]["model"]
        self.assertEqual(verdict["conditional_action"], "WAIT")
        self.assertEqual(verdict["wait_target_line"], 3.5)
        self.assertEqual(verdict["wait_min_odds"], 1.65)
        self.assertTrue(verdict["wait_reachable"])

    def test_material_market_disagreement_blocks_until_rechecked(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        first = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        price = first["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertTrue(price["quote_research_required"])
        self.assertEqual(
            price["model"]["conditional_action"],
            "MARKET_DISAGREEMENT_RECHECK_REQUIRED",
        )
        self.assertFalse(price["model"]["market_disagreement_recheck_completed"])

        complete_market_disagreement_recheck(c)
        second = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        self.assertEqual(second["price_check"]["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertFalse(second["price_check"]["quote_research_required"])
        self.assertTrue(
            second["price_check"]["model"]["market_disagreement_recheck_completed"]
        )
        self.assertIn(
            second["price_check"]["model"]["conditional_action"],
            {"ACT", "WAIT", "PASS"},
        )

    def test_g4_disagreement_requires_upper_tail_and_comparable_context_fields(self):
        c = complete_market_disagreement_recheck(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None),
            fields=["upper_tail_transferability"],
        )
        out = run_xi(c, snapshot(c, line=5.0, odds=1.72))
        price = out["price_check"]
        self.assertEqual(price["status"], "MARKET_DISAGREEMENT_RECHECK_REQUIRED")
        self.assertIn(
            "upper_tail_comparable_context_signal",
            price["model"]["market_disagreement_recheck_missing_fields"],
        )

    def test_quarter_goal_disagreement_does_not_trigger_material_recheck(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        baseline = run_xi(c, snapshot(c, line=2.5, odds=1.70))
        supported = baseline["price_check"]["model"]["supported_line"]
        self.assertIsNotNone(supported)
        out = run_xi(c, snapshot(c, line=supported + 0.25, odds=1.70))
        self.assertEqual(out["price_check"]["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_unestablished_wait_is_not_invented(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c, snapshot(c, line=3.25, odds=1.72))
        self.assertNotEqual(
            out["price_check"]["model"]["conditional_action"],
            "WAIT",
        )

    def test_observed_quote_persists_in_normal_line_odds_fields(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, line=2.75, odds=1.71))
        readback = {
            "spreadsheet_id": "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM",
            "sheet_name": "Decision States",
            "row_key": "XI-SCREENSHOT-EXAMPLE",
            "assessment_id": "XI-SCREENSHOT-EXAMPLE",
            "match_id": out["result"]["match_id"],
            "readback_method": "INDEPENDENT_GOOGLE_SHEETS_REFETCH",
            "xi_status_column": STATUS_COLUMN,
            "xi_assessment_execution_status":
                "EXECUTED_C_FOOTBALL_AND_PRICE",
            "engine_c_result": out["result"],
            "evaluated_line": 2.75,
            "evaluated_odds": 1.71,
        }
        verified = verify_football_assessment(out, readback)
        self.assertTrue(verified["football_c_verified"])
        self.assertTrue(verified["observed_quote_readback_verified"])
        self.assertFalse(verified["actual_bet_created"])

        bad = dict(readback)
        bad["evaluated_odds"] = 1.91
        with self.assertRaisesRegex(
            XIAssessmentReadbackError,
            "evaluated line/odds",
        ):
            verify_football_assessment(out, bad)


if __name__ == "__main__":
    unittest.main()
