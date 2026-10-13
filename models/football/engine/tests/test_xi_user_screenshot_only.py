"""Observed screenshot quote uses canonical C/C2 policy, never execution authority."""
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
    STATUS_FIELD_ID,
    XIAssessmentReadbackError,
    verify_football_assessment,
)


CAPTURE = "2026-10-11T05:05:00+00:00"
OLDER = "2026-10-11T05:04:00+00:00"


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


def wait_ready(payload, *, top=False):
    payload["context"].update(
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


def run_xi(c=None, c2=None, shot=None):
    c = c or football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
    c2 = c2 or football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
    shot = shot if shot is not None else snapshot(c)
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        paths = {}
        for name, doc in {"c": c, "c2": c2, "shot": shot}.items():
            file = root / (name + ".json")
            file.write_text(json.dumps(doc), encoding="utf-8")
            paths[name] = str(file)
        proc = subprocess.run(
            [
                sys.executable,
                str(ENGINE / "xi_portable.py"),
                "xi",
                "--c",
                paths["c"],
                "--c2",
                paths["c2"],
                "--screenshot-quote",
                paths["shot"],
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
    def test_01_exact_screenshot_quote_is_preserved(self):
        out = run_xi()
        self.assertEqual(out["xi_mode"], "FOOTBALL_AND_OBSERVED_QUOTE")
        price = out["price_check"]
        self.assertTrue(price["ok"])
        self.assertEqual(price["status"], "OBSERVED_QUOTE_EVALUATED")
        self.assertEqual(price["evidence"]["quote"], {"line": 2.5, "odds": 1.7})
        self.assertEqual(price["evidence"]["bookmaker"], "User-displayed bookmaker")
        self.assertEqual(
            price["evidence"]["capture_reference"],
            "user-attachment-screenshot-1",
        )
        self.assertFalse(price["execution_authorized"])
        self.assertFalse(price["bet_authorized"])

    def test_02_no_external_or_replacement_quote(self):
        out = run_xi()
        evidence = out["price_check"]["evidence"]
        self.assertEqual(evidence["external_price_searches"], 0)
        self.assertEqual(evidence["replacement_quotes"], 0)
        self.assertFalse(out["price_check"]["quote_research_required"])

    def test_03_missing_capture_time_is_not_retimed(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, captured=None))
        price = out["price_check"]
        self.assertIsNone(price["evidence"]["observed_at_utc"])
        self.assertIsNone(price["evidence"]["observation_age_seconds"])
        self.assertIn("SCREENSHOT_CAPTURE_TIME_UNKNOWN", price["limitations"])
        self.assertFalse(price["execution_authorized"])

    def test_04_live_screenshot_never_recreates_prematch_action(self):
        c, c2 = football("c"), football("c2")
        out = run_xi(c, c2, snapshot(c))
        price = out["price_check"]
        self.assertEqual(price["evidence"]["score"], "1-0")
        self.assertEqual(price["evidence"]["match_minute"], 5)
        for model in ("c", "c2"):
            self.assertEqual(
                price["models"][model]["conditional_action"],
                "LIVE_PRICE_BURDEN_COMPARISON_ONLY",
            )
        self.assertFalse(price["execution_authorized"])

    def test_05_invalid_screenshot_blocks_price_only_not_football(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, match_id="wrong-id"))
        self.assertEqual(out["xi_mode"], "FOOTBALL_ASSESSMENT")
        self.assertEqual(out["price_check"]["status"], "OBSERVED_QUOTE_INVALID")
        self.assertEqual(
            out["engine_execution_status"], "EXECUTED_C_C2_FOOTBALL_ONLY"
        )
        self.assertEqual(set(out["results"]), {"c", "c2"})

    def test_06_open_offer_flag_never_makes_screenshot_executable(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(
            c=c,
            shot=snapshot(c, open_offer_verified_in_screenshot=True),
        )
        self.assertFalse(out["price_check"]["execution_authorized"])
        self.assertFalse(out["price_check"]["bet_authorized"])

    def test_07_independent_c2_supported_burden_is_preserved(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2 = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2["match"]["supported_line"] = 3.0
        out = run_xi(c, c2, snapshot(c, line=2.75, captured=OLDER))
        self.assertEqual(out["price_check"]["models"]["c"]["supported_line"], 2.5)
        self.assertEqual(out["price_check"]["models"]["c2"]["supported_line"], 3.0)
        self.assertEqual(
            out["price_check"]["models"]["c2"]["snapshot_line_relation"],
            "BELOW_SUPPORTED_BURDEN",
        )

    def test_08_wait_comes_from_explicit_reachability_not_wrapper_gap(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        c2 = wait_ready(
            football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        out = run_xi(c, c2, snapshot(c, line=3.25, odds=1.72))
        for model in ("c", "c2"):
            verdict = out["price_check"]["models"][model]
            self.assertEqual(verdict["conditional_action"], "WAIT")
            self.assertEqual(verdict["wait_target_line"], 2.5)
            self.assertEqual(verdict["wait_min_odds"], 1.65)
            self.assertTrue(verdict["wait_reachable"])
        self.assertFalse(out["price_check"]["execution_authorized"])

    def test_09_unestablished_wait_does_not_get_invented(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        c2 = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c, c2, snapshot(c, line=3.25, odds=1.72))
        for model in ("c", "c2"):
            self.assertNotEqual(
                out["price_check"]["models"][model]["conditional_action"],
                "WAIT",
            )

    def test_10_negative_information_wait_is_not_healthy(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        c2 = wait_ready(
            football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        )
        for payload in (c, c2):
            payload["context"]["wait_requires_negative_info"] = True
            payload["context"]["wait_negative_info_basis"] = (
                "would need route deterioration to become cheap enough"
            )
        out = run_xi(c, c2, snapshot(c, line=3.25, odds=1.72))
        for model in ("c", "c2"):
            self.assertNotEqual(
                out["price_check"]["models"][model]["conditional_action"],
                "WAIT",
            )

    def test_11_top_focus_soft_zone_uses_core_160_rule(self):
        c = wait_ready(
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None),
            top=True,
        )
        c2 = wait_ready(
            football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None),
            top=True,
        )
        out = run_xi(c, c2, snapshot(c, line=2.5, odds=1.62))
        for model in ("c", "c2"):
            self.assertEqual(
                out["price_check"]["models"][model]["conditional_action"],
                "ACT",
            )

    def test_12_observed_quote_persists_in_normal_line_odds_fields(self):
        c = football("c", status="PREMATCH_CONFIRMED", minute=None, score=None)
        out = run_xi(c=c, shot=snapshot(c, line=2.75, odds=1.71))
        readback = {
            "base_id": "appbzxqXYf0lKfD4P",
            "record_id": "rec1234567890ABCDE",
            "assessment_id": "XI-SCREENSHOT-EXAMPLE",
            "match_id": out["results"]["c"]["match_id"],
            "readback_method": "INDEPENDENT_AIRTABLE_REFETCH",
            "xi_status_field_id": STATUS_FIELD_ID,
            "xi_assessment_execution_status":
                "EXECUTED_C_C2_FOOTBALL_AND_PRICE",
            "engine_c_result": out["results"]["c"],
            "engine_c2_result": out["results"]["c2"],
            "evaluated_line": 2.75,
            "evaluated_odds": 1.71,
        }
        verified = verify_football_assessment(out, readback)
        self.assertTrue(verified["football_pair_verified"])
        self.assertTrue(verified["observed_quote_readback_verified"])
        self.assertFalse(verified["actual_bet_created"])

        bad = dict(readback)
        bad["evaluated_odds"] = 1.91
        with self.assertRaisesRegex(
            XIAssessmentReadbackError, "evaluated line/odds"
        ):
            verify_football_assessment(out, bad)


if __name__ == "__main__":
    unittest.main()
