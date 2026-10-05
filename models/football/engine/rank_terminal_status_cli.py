from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rank_terminal_status import RankTerminalStatusError, rank_terminal_status


def main() -> int:
    parser = argparse.ArgumentParser(description="Football /rank terminal status")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        out = {"ok": True, **rank_terminal_status(payload)}
    except (OSError, json.JSONDecodeError, RankTerminalStatusError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2

    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
