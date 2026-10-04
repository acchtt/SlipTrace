#!/usr/bin/env python3
"""Fail CI when the generated /xi portable runtime is stale or unloadable."""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
BUNDLE = ROOT / "models/football/engine/xi_portable.py"


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
    ).hexdigest()


spec = importlib.util.spec_from_file_location("xi_portable_guarded", BUNDLE)
if spec is None or spec.loader is None:
    raise SystemExit("XI PORTABLE QA FAIL — unable to load bundle spec")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

failures: list[str] = []

for rel, expected in module.SOURCE_BLOB_SHA.items():
    path = ROOT / rel
    if not path.exists():
        failures.append(f"missing source: {rel}")
        continue
    actual = git_blob_sha(path)
    if actual != expected:
        failures.append(
            f"stale embedded source: {rel} expected={expected} actual={actual}"
        )

result = module.self_check()
if not result.get("ok"):
    failures.append(f"self-check failed: {result}")

if failures:
    print("XI PORTABLE QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — XI portable runtime is source-fresh and self-loads successfully.")
