#!/usr/bin/env python3
"""End-to-end CLI smoke for the active /xi portable C+C2 runtime.

This runs an entirely synthetic, pre-outcome evidence epoch. It never creates a
Website Pick, changes a live decision, or counts toward prospective model QA.
"""
from __future__ import annotations

import copy
import json
import hashlib
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[3]
BUNDLE = ROOT / "models/football/engine/xi_portable.py"
HANDOFF = ROOT / "models/football/engine/xi_source_handoff.py"
TESTS = ROOT / "models/football/engine/tests"
sys.path.insert(0, str(TESTS))

from test_adapter import pair_payload  # noqa: E402
from test_step2_reconcile import payload as reconciliation_payload  # noqa: E402
from test_model_bet_accounting import row as accounting_row  # noqa: E402


def command(*args: str) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(BUNDLE), *args],
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
            f"portable CLI failed to emit JSON: rc={proc.returncode} "
            f"stdout={proc.stdout[-600:]!r} stderr={proc.stderr[-600:]!r}"
        ) from exc
    return proc.returncode, result


def write(path: Path, value: dict) -> str:
    path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")
    return str(path)


def expect_contract_failure(args: tuple[str, ...], fragment: str) -> None:
    code, result = command(*args)
    assert code != 0, f"invalid payload unexpectedly succeeded: {args}"
    assert result.get("status") == "XI ENGINE CONTRACT REJECTED", result
    assert result.get("failure_class") == "PAYLOAD_OR_MODEL_CONTRACT", result
    assert fragment in result.get("error", ""), result


def main() -> None:
    code, self_check = command("self-check")
    assert code == 0 and self_check.get("ok") is True, self_check
    assert self_check.get("active_models") == ["c", "c2"], self_check
    assert self_check.get("status") == "XI PORTABLE RUNTIME: PASS", self_check

    with TemporaryDirectory(prefix="xi-portable-e2e-") as directory:
        global BUNDLE
        temp = Path(directory)
        source_bytes = BUNDLE.read_bytes()
        sha = hashlib.sha1(
            b"blob " + str(len(source_bytes)).encode("ascii") + b"\0" + source_bytes
        ).hexdigest()
        checkout_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, cwd=ROOT
        ).strip()
        staged = temp / "xi_portable.py"
        handoff_command = [
            sys.executable, str(HANDOFF), "--revision", checkout_sha,
            "--blob-sha", sha, "--output", str(staged),
        ]
        staged_run = subprocess.run(
            handoff_command, input=source_bytes,
            capture_output=True, timeout=35, check=False,
        )
        assert staged_run.returncode == 0, staged_run.stderr.decode()[-800:]
        receipt = json.loads(staged_run.stdout)
        assert receipt["status"] == "XI SOURCE HANDOFF: PASS", receipt
        assert receipt["source_blob_sha"] == sha, receipt
        assert staged.read_bytes() == source_bytes

        # Corrupted transit bytes cannot replace a previously validated engine.
        corrupted = bytearray(source_bytes)
        corrupted[100] ^= 1
        bad_run = subprocess.run(
            handoff_command, input=bytes(corrupted),
            capture_output=True, timeout=35, check=False,
        )
        assert bad_run.returncode != 0, bad_run.stdout
        bad_receipt = json.loads(bad_run.stderr)
        assert bad_receipt["status"] == "XI SOURCE HANDOFF: FAIL", bad_receipt
        assert "source blob mismatch" in bad_receipt["error"], bad_receipt
        assert staged.read_bytes() == source_bytes

        # Subsequent C+C2 pair, reconciliation and accounting use staged bytes.
        BUNDLE = staged
        c = pair_payload("c")
        c2 = pair_payload("c2")
        c_file = write(temp / "c.json", c)
        c2_file = write(temp / "c2.json", c2)
        pair_args = ("pair", "--c", c_file, "--c2", c2_file)

        code, result = command(*pair_args)
        assert code == 0 and result.get("ok") is True, result
        assert result.get("engine_execution_status") == "EXECUTED_C_C2_PAIR", result
        assert result.get("models_executed") == ["c", "c2"], result
        assert set(result.get("results", {})) == {"c", "c2"}, result
        # Repeatability: the same frozen inputs must return exactly the same pair.
        repeated_code, repeated = command(*pair_args)
        assert repeated_code == 0 and repeated == result, (result, repeated)

        invalid_epoch = copy.deepcopy(c2)
        invalid_epoch["match"]["common_evidence_basis"] = (
            "different synthetic factual evidence epoch"
        )
        invalid_file = write(temp / "different-epoch.json", invalid_epoch)
        expect_contract_failure(
            ("pair", "--c", c_file, "--c2", invalid_file),
            "same frozen common evidence epoch",
        )

        # Remove the same common field from BOTH sides, avoiding an earlier
        # epoch-mismatch rejection and reaching the evidence-completeness gate.
        missing_research_c = copy.deepcopy(c)
        missing_research_c2 = copy.deepcopy(c2)
        missing_research_c["context"].pop("post_xi_research_note")
        missing_research_c2["context"].pop("post_xi_research_note")
        missing_c_file = write(temp / "missing-research-c.json", missing_research_c)
        missing_c2_file = write(temp / "missing-research-c2.json", missing_research_c2)
        expect_contract_failure(
            ("pair", "--c", missing_c_file, "--c2", missing_c2_file),
            "post_xi_research_note",
        )

        invalid_model = copy.deepcopy(c2)
        invalid_model["model"] = "c3"
        retired_file = write(temp / "retired-model.json", invalid_model)
        expect_contract_failure(
            ("pair", "--c", c_file, "--c2", retired_file),
            "expected model=c2",
        )

        reconciliation = write(
            temp / "reconcile.json", reconciliation_payload()
        )
        code, reconciled = command("reconcile", "--input", reconciliation)
        assert code == 0 and reconciled.get("all_due_accounted") is True, reconciled
        assert reconciled.get("step2_reconciliation_status") == "PASS", reconciled

        accounting = write(
            temp / "accounting.json",
            {
                "match_id": "synthetic-no-exposure",
                "total_goals": 3,
                "models": [
                    accounting_row("c", "C-WATCH", 2.5),
                    accounting_row("c2", "C2-WATCH", 2.25),
                ],
            },
        )
        code, accounted = command("accounting", "--input", accounting)
        assert code == 0 and accounted.get("roster") == "ACTIVE_C_C2", accounted
        assert {row["model"] for row in accounted["models"]} == {"c", "c2"}
        assert not any(
            row.get("creates_website_pick", False)
            for row in accounted["models"]
            if row["model"] == "c2"
        ), accounted

    print(
        "PASS — standalone XI portable CLI: self-check, atomic C+C2 pair, "
        "determinism, 3 contract rejections, reconciliation, active accounting."
    )


if __name__ == "__main__":
    main()
