#!/usr/bin/env python3
"""Small end-to-end smoke for the active thin /xi C+C2 runner."""

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
    assert checked.get("active_models") == ["c", "c2"], checked
    assert checked.get("runtime_mode") == "THIN_SHARED_MODULES", checked

    with TemporaryDirectory(prefix="xi-runtime-e2e-") as directory:
        root = Path(directory)

        c, c2 = pair_payload("c"), pair_payload("c2")
        c_file = write(root / "c.json", c)
        c2_file = write(root / "c2.json", c2)
        args = ("pair", "--c", c_file, "--c2", c2_file)
        code, first = command(*args)
        assert code == 0 and first.get("engine_execution_status") == "EXECUTED_C_C2_PAIR", first
        code, repeated = command(*args)
        assert code == 0 and repeated == first, (first, repeated)

        bad = copy.deepcopy(c2)
        bad["model"] = "c3"
        bad_file = write(root / "retired.json", bad)
        code, rejected = command("pair", "--c", c_file, "--c2", bad_file)
        assert code != 0, rejected
        assert rejected.get("status") == "XI ENGINE CONTRACT REJECTED", rejected

        fc = write(
            root / "fc.json",
            football("c", status="PREMATCH_CONFIRMED", minute=None, score=None),
        )
        fc2 = write(
            root / "fc2.json",
            football("c2", status="PREMATCH_CONFIRMED", minute=None, score=None),
        )
        code, assessed = command("xi", "--c", fc, "--c2", fc2)
        assert code == 0, assessed
        assert assessed.get("xi_mode") == "FOOTBALL_ASSESSMENT", assessed
        assert assessed.get("engine_execution_status") == "EXECUTED_C_C2_FOOTBALL_ONLY", assessed

    print(
        "PASS — thin /xi runner: self-check, deterministic strict pair, "
        "retired-model rejection and quote-free C+C2 assessment."
    )


if __name__ == "__main__":
    main()
