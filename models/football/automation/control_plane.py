from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

SCHEMA = "football-actions-control-v1"
OPERATIONS = {"health", "sweep", "rank", "verify-rank", "xi-self-check"}
ROOT = Path(__file__).resolve().parents[3]


class ControlPlaneError(ValueError):
    pass


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _repo_file(value: Any, field: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ControlPlaneError(f"{field} must be a non-empty repository-relative path")
    rel = Path(value)
    if rel.is_absolute():
        raise ControlPlaneError(f"{field} must be repository-relative")
    resolved = (ROOT / rel).resolve()
    root = ROOT.resolve()
    if resolved != root and root not in resolved.parents:
        raise ControlPlaneError(f"{field} escapes the repository")
    if not resolved.is_file():
        raise ControlPlaneError(f"{field} not found: {value}")
    return resolved


def _run(args: list[str]) -> str:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        detail = "\n".join(x for x in (proc.stdout.strip(), proc.stderr.strip()) if x)
        raise ControlPlaneError(
            f"command failed ({proc.returncode}): {' '.join(args)}"
            + (f"\n{detail}" if detail else "")
        )
    return proc.stdout.strip()


def _load_request(path: Path, expected_operation: str) -> dict[str, Any]:
    try:
        request = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ControlPlaneError(f"request JSON unreadable: {exc}") from exc
    if not isinstance(request, dict):
        raise ControlPlaneError("request must be a JSON object")
    if request.get("schema_version") != SCHEMA:
        raise ControlPlaneError(f"request schema_version must be {SCHEMA}")
    if request.get("operation") != expected_operation:
        raise ControlPlaneError(
            f"request operation {request.get('operation')!r} does not match "
            f"requested operation {expected_operation!r}"
        )
    paths = request.get("paths")
    if not isinstance(paths, dict):
        raise ControlPlaneError("request paths must be an object")
    return request


def _receipt_summary(operation: str, receipt: dict[str, Any]) -> dict[str, Any]:
    base: dict[str, Any] = {
        "schema_version": SCHEMA,
        "status": "CONTROL_PLANE_OK",
        "operation": operation,
        "git_sha": os.environ.get("GITHUB_SHA"),
    }
    if operation == "sweep":
        base.update(
            run_id=receipt.get("run_id"),
            receipt_status=receipt.get("status"),
            fixture_count=receipt.get("fixture_count"),
            eligible_count=receipt.get("eligible_count"),
            goal_review_count=receipt.get("goal_review_count"),
            pending_discovery_count=receipt.get("pending_discovery_count"),
        )
    elif operation == "rank":
        board = receipt.get("board") if isinstance(receipt.get("board"), dict) else {}
        base.update(
            run_id=receipt.get("run_id"),
            receipt_status=receipt.get("status"),
            assessed_count=receipt.get("assessed_count"),
            ranked_count=receipt.get("ranked_count"),
            watch_count=receipt.get("watch_count"),
            pass_count=receipt.get("pass_count"),
            follow_count=board.get("follow_count"),
            reserve_count=board.get("reserve_count"),
            stop_count=board.get("stop_count"),
            board_admission_policy=receipt.get("board_admission_policy"),
        )
    elif operation == "verify-rank":
        base.update(
            run_id=receipt.get("run_id"),
            receipt_status=receipt.get("status"),
            ranked_count=receipt.get("ranked_count"),
            model_evidence_readback_verified=receipt.get(
                "model_evidence_readback_verified"
            ),
        )
    return base


def _stage_script() -> str:
    return str(ROOT / "models/football/stages_v4/stage.py")


def execute(operation: str, request_path: Path | None, output_dir: Path) -> dict[str, Any]:
    if operation not in OPERATIONS:
        raise ControlPlaneError(f"unsupported operation: {operation}")

    output_dir.mkdir(parents=True, exist_ok=True)

    if operation == "health":
        _run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "models/football/stages_v4",
                "-p",
                "test_*.py",
                "-v",
            ]
        )
        _run([sys.executable, "models/football/automation/test_control_plane.py"])
        _run([sys.executable, "models/football/qa/check_authority_consistency.py"])
        _run([sys.executable, "models/football/qa/check_runtime_execution_contract.py"])
        _run([sys.executable, "models/football/engine/xi_portable.py", "self-check"])
        summary = {
            "schema_version": SCHEMA,
            "status": "CONTROL_PLANE_OK",
            "operation": "health",
            "git_sha": os.environ.get("GITHUB_SHA"),
            "v4_stage_tests": "PASS",
            "authority_consistency": "PASS",
            "runtime_contract": "PASS",
            "xi_runtime": "PASS",
            "paid_ai_api_used": False,
        }
        _write_json(output_dir / "summary.json", summary)
        return summary

    if operation == "xi-self-check":
        _run([sys.executable, "models/football/engine/xi_portable.py", "self-check"])
        summary = {
            "schema_version": SCHEMA,
            "status": "CONTROL_PLANE_OK",
            "operation": operation,
            "git_sha": os.environ.get("GITHUB_SHA"),
            "xi_runtime": "PASS",
            "paid_ai_api_used": False,
        }
        _write_json(output_dir / "summary.json", summary)
        return summary

    if request_path is None:
        raise ControlPlaneError(f"{operation} requires --request")
    request = _load_request(request_path, operation)
    paths = request["paths"]

    if operation == "sweep":
        source = _repo_file(paths.get("source"), "paths.source")
        receipt_path = output_dir / "v4_sweep_ready.json"
        _run(
            [
                sys.executable,
                _stage_script(),
                "--output",
                str(receipt_path),
                "sweep",
                "--source",
                str(source),
            ]
        )
    elif operation == "rank":
        required = {
            key: _repo_file(paths.get(key), f"paths.{key}")
            for key in ("sweep", "source", "status_refresh", "c", "unranked")
        }
        receipt_path = output_dir / "v4_rank.json"
        _run(
            [
                sys.executable,
                _stage_script(),
                "--output",
                str(receipt_path),
                "rank",
                "--sweep",
                str(required["sweep"]),
                "--source",
                str(required["source"]),
                "--status-refresh",
                str(required["status_refresh"]),
                "--c",
                str(required["c"]),
                "--unranked",
                str(required["unranked"]),
            ]
        )
    else:
        required = {
            key: _repo_file(paths.get(key), f"paths.{key}")
            for key in ("rank", "readback")
        }
        receipt_path = output_dir / "v4_rank_verified.json"
        _run(
            [
                sys.executable,
                _stage_script(),
                "--output",
                str(receipt_path),
                "verify",
                "--rank",
                str(required["rank"]),
                "--readback",
                str(required["readback"]),
            ]
        )

    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ControlPlaneError(f"stage receipt unreadable: {exc}") from exc
    if not isinstance(receipt, dict):
        raise ControlPlaneError("stage receipt must be a JSON object")

    summary = _receipt_summary(operation, receipt)
    summary["paid_ai_api_used"] = False
    _write_json(output_dir / "summary.json", summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Free GitHub Actions control plane for Football v2 deterministic stages"
    )
    parser.add_argument("--operation", required=True, choices=sorted(OPERATIONS))
    parser.add_argument("--request", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("football-action-output"))
    args = parser.parse_args()

    try:
        summary = execute(args.operation, args.request, args.output_dir)
        print(json.dumps(summary, sort_keys=True))
        return 0
    except (ControlPlaneError, OSError, ValueError, KeyError, TypeError) as exc:
        failure = {
            "schema_version": SCHEMA,
            "status": "CONTROL_PLANE_BLOCKED",
            "operation": args.operation,
            "git_sha": os.environ.get("GITHUB_SHA"),
            "reason": str(exc),
            "paid_ai_api_used": False,
        }
        _write_json(args.output_dir / "summary.json", failure)
        print(json.dumps(failure, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
