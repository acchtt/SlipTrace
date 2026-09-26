#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = {
    "models/football/CURRENT_MODEL.md": [
        "MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md",
        "POST-XI FOOTBALL WEB-RESEARCH GATE — ACTIVE",
        "Verdict-first must never be interpreted as research-skipped.",
    ],
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md": [
        "Mandatory post-XI football web-research gate",
        "POST-XI RESEARCH = FOUND",
        "MANDATORY POST-XI FOOTBALL WEB RESEARCH",
        "Odds/history lookup does **not** satisfy the football-research gate.",
    ],
    "models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md": [
        "Mandatory post-XI football web research",
        "POST-XI RESEARCH = FOUND",
        "MANDATORY POST-XI FOOTBALL WEB RESEARCH",
        "Verdict-first must never become research-skipped.",
    ],
    "models/football/procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md": [
        "Step 2 XI+odds has an additional mandatory post-XI football web-research gate",
        "This is separate from the market-history watch",
    ],
    "models/football/procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md": [
        "WORKFLOW REGRESSION — POST-XI RESEARCH GATE MISSING/OPTIONAL",
        "market-history lookup is treated as satisfying the post-XI football research gate",
    ],
    "models/football/prompts/README.md": [
        "mandatory fresh post-XI football web research",
        "run the mandatory post-XI football web-research gate",
    ],
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md": [
        "Step-2 post-XI research compliance audit",
        "POST-XI RESEARCH COMPLIANCE ERROR",
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
    print("WORKFLOW REGRESSION — POST-XI RESEARCH GATE MISSING/OPTIONAL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — post-XI football web-research gate is present in all canonical workflow surfaces.")
