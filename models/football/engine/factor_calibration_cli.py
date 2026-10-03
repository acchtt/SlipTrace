from __future__ import annotations

import argparse
import json
from pathlib import Path

from factor_calibration import analyze, parse_observation


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze prospective Football C factor-calibration observations"
    )
    parser.add_argument("--input", required=True, help="JSON file containing an array of observations or {observations:[...]}")
    args = parser.parse_args()

    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    items = raw["observations"] if isinstance(raw, dict) else raw
    if not isinstance(items, list):
        raise ValueError("input must be an array or an object with observations array")
    observations = [parse_observation(item) for item in items]
    print(json.dumps(analyze(observations), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
