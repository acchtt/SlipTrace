#!/usr/bin/env python3
"""Validate and stage an exact GitHub-sourced XI bundle from stdin.

No network access, third-party dependencies, model-rule changes, or live data.
The source bytes arrive from an upstream authenticated/connected GitHub fetch.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

MAX_SOURCE_BYTES = 2_000_000
HEX_SHA = re.compile(r"^[0-9a-f]{40}$")


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    ).hexdigest()


def stage_source(
    data: bytes, destination: Path, *, revision: str, expected_blob_sha: str
) -> dict:
    """Promote a self-checked, SHA-verified temporary source atomically."""
    if not HEX_SHA.fullmatch(revision) or not HEX_SHA.fullmatch(expected_blob_sha):
        raise ValueError("revision and expected blob SHA must be full lowercase 40-hex Git SHAs")
    if not data:
        raise ValueError("empty source stream")
    if len(data) > MAX_SOURCE_BYTES:
        raise ValueError("source stream exceeds maximum allowed size")
    actual = git_blob_sha(data)
    if actual != expected_blob_sha:
        raise ValueError(
            f"source blob mismatch: expected={expected_blob_sha} actual={actual}"
        )
    data.decode("utf-8")  # Fail before writing a non-text/corrupt source.
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=".xi-stage-", suffix=".py",
            dir=destination.parent, delete=False
        ) as source_file:
            temporary = Path(source_file.name)
            source_file.write(data)

        run = subprocess.run(
            [sys.executable, str(temporary), "self-check"],
            capture_output=True, text=True, timeout=30, check=False,
        )
        try:
            report = json.loads(run.stdout)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"portable self-check emitted non-JSON output (exit={run.returncode}): "
                f"{run.stderr[-400:]}"
            ) from exc
        if (
            run.returncode != 0
            or report.get("ok") is not True
            or report.get("status") != "XI PORTABLE RUNTIME: PASS"
            or report.get("active_models") != ["c", "c2"]
        ):
            raise ValueError(
                f"portable self-check rejected staged bytes (exit={run.returncode}): "
                f"{json.dumps(report, sort_keys=True)[:600]}"
            )
        os.replace(temporary, destination)
        temporary = None
        return {
            "ok": True,
            "status": "XI SOURCE HANDOFF: PASS",
            "repository_revision": revision,
            "source_blob_sha": actual,
            "source_bytes": len(data),
            "python_version": report.get("python_version"),
            "active_models": ["c", "c2"],
            "bundle_self_check": "PASS",
        }
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Stage connected-GitHub source bytes into a verified local XI runtime"
    )
    parser.add_argument("--revision", required=True, help="Exact current main commit SHA")
    parser.add_argument("--blob-sha", required=True, help="Git blob SHA from fetch_file")
    parser.add_argument("--output", required=True, help="Local xi_portable.py destination")
    args = parser.parse_args()
    try:
        source = sys.stdin.buffer.read(MAX_SOURCE_BYTES + 1)
        result = stage_source(
            source, Path(args.output),
            revision=args.revision, expected_blob_sha=args.blob_sha,
        )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({
            "ok": False,
            "status": "XI SOURCE HANDOFF: FAIL",
            "failure_class": "SOURCE_TRANSFER_OR_SELF_CHECK",
            "error": f"{type(exc).__name__}: {exc}",
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
