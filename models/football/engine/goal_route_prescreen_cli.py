#!/usr/bin/env python3
"""CLI for a bounded whole-queue football screen before Step1 deep research."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from goal_route_prescreen import GoalPrescreenError, run_prescreen


def main() -> int:
    parser = argparse.ArgumentParser(description="Prospective A/B goal-route research priority screen")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = run_prescreen(payload)
        serialized = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
        if args.output:
            Path(args.output).write_text(serialized + "\n", encoding="utf-8")
        else:
            print(serialized)
        return 0
    except (OSError, ValueError, TypeError, json.JSONDecodeError, GoalPrescreenError) as exc:
        print(json.dumps({"ok": False, "status": "GOAL_PRESCREEN_INVALID",
                          "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
