#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = {
    "models/football/CURRENT_MODEL.md": [
        "Active official model:** Football **C**",
        "fresh post-XI public-web football research mandatory",
        "H2H mandatory when usable",
    ],
    "models/football/production/FOOTBALL_C.md": [
        "one mandatory fresh fixture-specific public-web football research pass",
        "Market-history/odds lookup does not satisfy the football-research requirement",
        "H2H is mandatory context when usable",
        "PRICE DECAY != THESIS DECAY",
    ],
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md": [
        "MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH",
        "Odds/history lookup does **not** satisfy the football-research gate.",
        "perform/recheck relevant H2H/matchup context",
    ],
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md": [
        "TARGET REACHED + THESIS STILL HEALTHY?",
        "C-WAIT CANCELLED — THESIS DECAY",
    ],
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md": [
        "mandatory post-XI football research compliance",
        "Historical Football A audits must remain version-faithful.",
    ],
}

failures = []
for file_name, needles in REQUIRED.items():
    path = Path(file_name)
    if not path.exists():
        failures.append(f"{file_name}: missing file")
        continue
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            failures.append(f"{file_name}: missing invariant: {needle}")

if failures:
    print("WORKFLOW REGRESSION — FOOTBALL C PRODUCTION INVARIANT MISSING")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — Football C production research/H2H/decay invariants are present.")
