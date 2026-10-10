#!/usr/bin/env python3
"""Pure scope preflight, no fixture-level searches or odds predictions."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from sweep_competition_scope import screen_competitions

def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    args=p.parse_args()
    try:
        x=json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(x,dict) or not isinstance(x.get("competitions"),list):
            raise ValueError("competitions must be a list")
        print(json.dumps(screen_competitions(x["competitions"]),indent=2,sort_keys=True))
        return 0
    except (OSError,ValueError,json.JSONDecodeError) as e:
        print(json.dumps({"ok":False,"reason":str(e)}),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
