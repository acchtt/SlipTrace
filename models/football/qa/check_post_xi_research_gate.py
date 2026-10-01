#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = {
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md": [
        "RESEARCHABLE_SENIOR_PRODUCTION",
        "INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED",
        "Protected senior competition classes",
    ],
    "models/football/CURRENT_MODEL.md": [
        "Active official model:** Football **C**",
        "Shadow challenger:** Football **C2**",
        "COMMON FOOTBALL EVIDENCE FREEZE",
        "Football C's board is the only board that can feed official Step-2 exposure.",
        "models/football/engine/",
    ],
    "models/football/production/FOOTBALL_C.md": [
        "**Intake:** RESEARCHABLE_SENIOR_PRODUCTION",
        "INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED",
        "one mandatory fresh fixture-specific public-web football research pass",
        "Market-history/odds lookup does not satisfy the football-research requirement",
        "H2H is mandatory context when usable",
        "PRICE DECAY != THESIS DECAY",
    ],
    "models/football/prompts/01_WORK_DAILY_SWEEP.md": [
        "sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION",
        "Football C Official + C2 Shadow Board",
        "Common evidence freeze",
        "Football C official board",
        "Football C2 shadow board",
        "C2 shadow board never substitutes for C",
        "FOOTBALL_ENGINE_C_INPUT",
        "FOOTBALL_ENGINE_C2_INPUT",
        "Operational follow-through guard",
        "maximum routine `FOLLOW = 6`",
        "maximum retained `RESERVE = 4`",
    ],
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md": [
        "Football C Official + C2 Shadow XI/Odds",
        "MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH",
        "Odds/history lookup does **not** satisfy the football-research gate.",
        "Football C official action",
        "Follow-through lane authority",
        "`STOP` — do not run routine Step-2",
        "Football C2 shadow action",
        "Only Football C may create official exposure.",
        "FOOTBALL_ENGINE_C_DECISION_INPUT",
        "FOOTBALL_ENGINE_C2_DECISION_INPUT",
        "ENGINE DISAGREEMENT",
    ],
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md": [
        "Football C Official Live + C2 Shadow Wait",
        "TARGET REACHED + THESIS STILL HEALTHY?",
        "C-WAIT CANCELLED — THESIS DECAY",
        "C2 may never create Website Pick or real exposure.",
    ],
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md": [
        "C OFFICIAL BOARD -> FOLLOW/RESERVE/STOP -> C2 SHADOW BOARD",
        "mandatory post-XI football research",
        "Only C2 decisions produced **after the dual-track fix commit**",
        "Historical Football A/C1 audits remain version-faithful.",
        "FOLLOW/RESERVE/STOP allocation",
    ],
    "models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md": [
        "**Champion:** Football C",
        "Dual-track operational boundary",
        "C2 may not create Website Picks or real exposure.",
    ],
    "models/football/challengers/football-c2/TEST_PROTOCOL.md": [
        "**Champion:** Football C",
        "C-vs-C2",
        "Restart boundary",
    ],
    "models/football/engine/schema.json": [
        "football-engine-v1",
        "\"stage\"",
        "\"matches\"",
        "\"context\"",
    ],
    "models/football/trials/FOOTBALL_C_ELITE_UPPER_TAIL_OBSERVER_2026-10-01.md": [
        "PROSPECTIVE OBSERVER ONLY — NO PRODUCTION AUTHORITY",
        "ELITE_UPPER_TAIL_OBSERVER",
        "does not extend the C2 bridge",
    ],
    "models/football/engine/adapter.py": [
        "def run_board",
        "follow_through_lane",
        "MAX_FOLLOW = 6",
        "MAX_RESERVE = 4",
        "def run_decision",
        "SCHEMA_VERSION = \"football-engine-v1\"",
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
    print("WORKFLOW REGRESSION — FOOTBALL C/C2 DUAL-TRACK INVARIANT MISSING")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — Football C official / C2 shadow / engine dual-track invariants are present.")
