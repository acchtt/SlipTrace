from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sweep_intake_evidence import classify_preflight, LEAGUE_CHANNEL_POLICY


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cheap strict XI + Asian-total preflight before Football Step0 Work queue"
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("candidates"), list):
            raise ValueError("candidates must be a list")
        intake_policy = data.get("intake_policy", "XI_MARKET_FIRST_V1")
        if intake_policy not in {"XI_MARKET_FIRST_V1", LEAGUE_CHANNEL_POLICY}:
            raise ValueError("unknown intake_policy")
        found = set()
        ready, excluded, pending = [], [], []
        for i, row in enumerate(data["candidates"]):
            if not isinstance(row, dict):
                raise ValueError(f"candidates[{i}] must be object")
            mid = row.get("match_id")
            if not isinstance(mid, str) or not mid.strip() or mid in found:
                raise ValueError(f"missing or duplicate canonical match_id at index {i}")
            found.add(mid)
            result = classify_preflight(row, intake_policy=intake_policy)
            record = {"match_id": mid, **result}
            if result["work_queue_eligible"]:
                ready.append(row)
            elif result["disposition"] == "PREFLIGHT_INCOMPLETE_NO_WORK":
                pending.append(record)
            else:
                excluded.append(record)
        report = {
            "ok": True,
            "policy": intake_policy,
            "raw_preflight_count": len(data["candidates"]),
            "verified_queue_candidates": len(ready),
            "operational_or_scope_excluded": len(excluded),
            "preflight_incomplete": len(pending),
            "ready_candidates": ready,
            "excluded": excluded,
            "pending": pending,
            "source_fixture_records_preserved": True,
        }
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
