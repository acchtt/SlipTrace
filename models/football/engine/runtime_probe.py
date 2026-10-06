from __future__ import annotations

import argparse
import importlib
import json
import py_compile
import sys
from pathlib import Path
from typing import Any


MIN_PYTHON = (3, 10)

STAGE_FILES = {
    "rank": (
        "models/football/engine/cli.py",
        "models/football/engine/adapter.py",
        "models/football/engine/core.py",
        "models/football/engine/competition_reliability.py",
        "models/football/engine/schema.json",
        "models/football/engine/board_pair_cli.py",
        "models/football/engine/capacity_replenishment.py",
        "models/football/engine/capacity_replenishment_cli.py",
        "models/football/engine/rank_terminal_status.py",
        "models/football/engine/rank_terminal_status_cli.py",
        "models/football/engine/repaired_handoff_normalize.py",
        "models/football/engine/model_bet_accounting.py",
        "models/football/engine/model_bet_accounting_cli.py",
        "models/football/engine/runtime_probe.py",
    ),
    "xi": (
        "models/football/engine/cli.py",
        "models/football/engine/adapter.py",
        "models/football/engine/core.py",
        "models/football/engine/competition_reliability.py",
        "models/football/engine/schema.json",
        "models/football/engine/xi_portable.py",
        "models/football/engine/model_bet_accounting.py",
        "models/football/engine/decision_pair_cli.py",
        "models/football/engine/step2_reconcile_cli.py",
        "models/football/engine/runtime_probe.py",
    ),
    "audit": (
        "models/football/engine/cli.py",
        "models/football/engine/adapter.py",
        "models/football/engine/core.py",
        "models/football/engine/competition_reliability.py",
        "models/football/engine/schema.json",
        "models/football/engine/factor_calibration.py",
        "models/football/engine/factor_calibration_cli.py",
        "models/football/engine/model_bet_accounting.py",
        "models/football/engine/model_bet_accounting_cli.py",
        "models/football/engine/runtime_probe.py",
    ),
}

STAGE_IMPORTS = {
    "rank": (
        "core",
        "competition_reliability",
        "adapter",
        "board_pair_cli",
        "model_bet_accounting",
        "model_bet_accounting_cli",
        "rank_terminal_status",
        "rank_terminal_status_cli",
    ),
    "xi": (
        "core",
        "competition_reliability",
        "adapter",
        "decision_pair_cli",
        "step2_reconcile_cli",
        "model_bet_accounting",
    ),
    "audit": (
        "core",
        "competition_reliability",
        "adapter",
        "factor_calibration",
        "factor_calibration_cli",
        "model_bet_accounting",
        "model_bet_accounting_cli",
    ),
}


class RuntimeProbeError(RuntimeError):
    pass


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def required_files(stage: str) -> tuple[str, ...]:
    try:
        return STAGE_FILES[stage]
    except KeyError as exc:
        raise RuntimeProbeError(
            f"stage must be one of {sorted(STAGE_FILES)}, got {stage!r}"
        ) from exc


def _parse_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as handle:
        json.load(handle)


def probe_stage(stage: str, root: Path | None = None) -> dict[str, Any]:
    root = root or repo_root()
    files = required_files(stage)

    result: dict[str, Any] = {
        "stage": stage,
        "python_version": ".".join(map(str, sys.version_info[:3])),
        "python_ok": sys.version_info[:2] >= MIN_PYTHON,
        "root": str(root),
        "required_files": list(files),
        "missing_files": [],
        "compile_errors": [],
        "json_errors": [],
        "import_errors": [],
    }

    if not result["python_ok"]:
        raise RuntimeProbeError(
            f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required, "
            f"got {result['python_version']}"
        )

    for rel in files:
        path = root / rel
        if not path.exists():
            result["missing_files"].append(rel)
            continue

        try:
            if path.suffix == ".py":
                py_compile.compile(str(path), doraise=True)
            elif path.suffix == ".json":
                _parse_json(path)
        except Exception as exc:  # exact setup diagnostic
            bucket = "compile_errors" if path.suffix == ".py" else "json_errors"
            result[bucket].append(f"{rel}: {exc}")

    if result["missing_files"] or result["compile_errors"] or result["json_errors"]:
        result["ok"] = False
        return result

    engine_dir = root / "models/football/engine"
    inserted = False
    if str(engine_dir) not in sys.path:
        sys.path.insert(0, str(engine_dir))
        inserted = True

    try:
        for name in STAGE_IMPORTS[stage]:
            try:
                importlib.import_module(name)
            except Exception as exc:
                result["import_errors"].append(f"{name}: {exc}")
    finally:
        if inserted:
            try:
                sys.path.remove(str(engine_dir))
            except ValueError:
                pass

    result["ok"] = not result["import_errors"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify the local Football runtime source for an execution stage"
    )
    parser.add_argument("--stage", required=True, choices=tuple(STAGE_FILES))
    args = parser.parse_args()

    try:
        result = probe_stage(args.stage)
    except RuntimeProbeError as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "stage": args.stage,
                    "status": "RUNTIME SOURCE PROBE: FAIL",
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 2

    result["status"] = (
        "RUNTIME SOURCE PROBE: PASS"
        if result["ok"]
        else "RUNTIME SOURCE PROBE: FAIL"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
