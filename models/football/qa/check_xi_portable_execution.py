#!/usr/bin/env python3
"""End-to-end smoke for the active thin single-C /xi runner."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "models/football/engine/xi_portable.py"
TESTS = ROOT / "models/football/engine/tests"
sys.path.insert(0, str(TESTS))

from test_adapter import pair_payload  # noqa: E402
from test_football_assessment_pair import football  # noqa: E402
from test_xi_user_screenshot_only import exception_authority  # noqa: E402

def command(*args: str) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(RUNNER), *args],
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )
    output = proc.stdout if proc.returncode == 0 else proc.stderr
    try:
        result = json.loads(output)
    except json.JSONDecodeError as exc:
        raise AssertionError(
            f"/xi runner did not emit JSON: rc={proc.returncode} "
            f"stdout={proc.stdout[-500:]!r} stderr={proc.stderr[-500:]!r}"
        ) from exc
    return proc.returncode, result

def write(path: Path, value: dict) -> str:
    path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")
    return str(path)

def main() -> None:
    code, checked = command("self-check")
    assert code == 0 and checked.get("ok") is True, checked
    assert checked.get("active_models") == ["c"], checked
    assert checked.get("retired_models") == ["c2", "c3", "c4"], checked

    with TemporaryDirectory(prefix="xi-runtime-e2e-") as directory:
        root = Path(directory)

        decision = pair_payload("c")
        decision_file = write(root / "decision-c.json", decision)
        frozen = dict(decision["match"])
        ranked_authority = write(root / "ranked-decision-authority.json", {
            "mode": "RANKED",
            "match_id": frozen["match_id"],
            "verified_rank_package": {
                "status": "V4_RANK_PERSISTENCE_VERIFIED",
                "native_rank": {
                    "run_id": "V4-qa-ranked-decision",
                    "integrity_sha256": "qa-ranked-decision-hash",
                    "board": {
                        "matches": [{
                            "match_id": frozen["match_id"],
                            "rank": 1,
                            "board_state": "FOCUS",
                            "supported_line": 2.5,
                        }]
                    },
                    "frozen_model_input": {"matches": [frozen]},
                },
            },
            "material_evidence_updates": [],
        })
        code, first = command(
            "decision", "--c", decision_file, "--authority", ranked_authority
        )
        assert code == 0, first
        assert first.get("engine_execution_status") == "EXECUTED_C_DECISION", first

        direct_decision_authority = write(root / "decision-exception-authority.json", {
            "mode": "EXCEPTION",
            "exception_reference": "qa-direct-decision-exception",
            "user_requested_exception": True,
        })
        code, blocked_decision = command(
            "decision", "--c", decision_file, "--authority", direct_decision_authority
        )
        assert code != 0, blocked_decision
        assert blocked_decision.get("status") == "EXCEPTION_RESEARCH_REQUIRED", blocked_decision

        retired = football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None)
        retired_file = write(root / "retired-c2.json", retired)
        code, rejected = command("football", "--c", retired_file)
        assert code != 0, rejected
        assert rejected.get("status") == "XI ENGINE CONTRACT REJECTED", rejected

        football_input = football(
            "c", status="PREMATCH_CONFIRMED", minute=None, score=None
        )
        authority_file = write(
            root / "authority.json",
            exception_authority(
                football_input,
                reference="qa-explicit-exception",
            ),
        )
        football_file = write(root / "football-c.json", football_input)
        code, missing_authority = command("xi", "--c", football_file)
        assert code != 0, missing_authority
        assert missing_authority.get("status") == "RANK_RECEIPT_REQUIRED", missing_authority

        code, assessed = command(
            "xi", "--c", football_file, "--authority", authority_file
        )
        assert code == 0, assessed
        assert assessed.get("xi_mode") == "FOOTBALL_ASSESSMENT", assessed
        assert assessed.get("engine_execution_status") == "EXECUTED_C_FOOTBALL_ONLY", assessed
        assert assessed.get("model") == "c", assessed

    print(
        "PASS — single-C /xi runner: self-check, shared authority fail-closed, "
        "ranked strict C decision, decision-stage exception replay block, retired-C2 rejection and quote-free C assessment."
    )

if __name__ == "__main__":
    main()
