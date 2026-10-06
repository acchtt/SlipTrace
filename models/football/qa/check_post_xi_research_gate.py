#!/usr/bin/env python3
"""Production invariant check for the active Football C + C2 roster.

Historical C3/C4 files may remain for audit history, but no active launcher or
runtime contract may require them for a new production decision.
"""
from pathlib import Path
import sys

REQUIRED = {
    "models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md": [
        "Football C3 and Football C4 are retired",
        "C + C2",
        "C+C2 EXCEPTION INCOMPLETE",
        "python xi_portable.py pair --c <c.json> --c2 <c2.json>",
    ],
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md": [
        "RESEARCHABLE_SENIOR_PRODUCTION",
        "Operational viability gate",
        "Competition reliability memory",
        "WOMEN TOP-FLIGHT COVERAGE GAP",
        "Command alias:** `/sweep`",
    ],
    "models/football/prompts/01_WORK_DAILY_SWEEP.md": [
        "Football C official board",
        "Football C2 shadow board",
        "clearing-goal funding",
        "maximum routine `FOLLOW = 6`",
        "maximum retained `RESERVE = 4`",
        "board_pair_cli.py --c <c.json> --c2 <c2.json>",
        "EXECUTED_C_C2_BOARDS",
        "Command alias:** `/rank`",
    ],
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md": [
        "ACTIVE ROSTER OVERRIDE",
        "pair --c <c.json> --c2 <c2.json>",
        "Only Football C may create official exposure.",
        "Engine execution is **mandatory**",
        "Command alias:** `/xi`",
    ],
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md": [
        "ACTIVE ROSTER",
        "C2 may never create Website Pick or real exposure.",
        "Command alias:** `/live`",
    ],
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md": [
        "ACTIVE ROSTER",
        "Audit hindsight integrity",
        "Command alias:** `/audit`",
    ],
    "models/football/engine/adapter.py": [
        "model not in {\"c\", \"c2\"}",
        "C3/C4 are retired",
        "MAX_FOLLOW = 6",
        "MAX_RESERVE = 4",
        "MAX_FOLLOW_PER_KICKOFF = 2",
        "def run_decision",
    ],
    "models/football/engine/xi_portable.py": [
        "def run_pair_files",
        'description="Portable Football /xi C+C2 deterministic runtime"',
        'sub.add_parser("pair")',
        '"EXECUTED_C_C2_PAIR"',
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

FORBIDDEN_ACTIVE = {
    "models/football/CURRENT_MODEL.md": [
        "xi_portable.py triplet",
        "board_triplet_cli.py --c",
        "Shadow challengers:** Football **C2**, Football **C3**",
    ],
    "models/football/prompts/01_WORK_DAILY_SWEEP.md": [
        "board_triplet_cli.py",
        "c4_semantic_cli.py",
        "C3 shadow board",
        "C4 Step-1 shadow",
    ],
    "models/football/prompts/COMMAND_ALIASES.md": [
        "C2/C3/C4 Step-1 shadow board workflow",
        "C3 Step-2 shadow action",
        "C4 prospectively frozen Step-1 snapshot",
    ],
}

for file_name, needles in FORBIDDEN_ACTIVE.items():
    path = Path(file_name)
    if not path.exists():
        failures.append(f"{file_name}: missing file")
        continue
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle in text:
            failures.append(f"{file_name}: retired active-path invariant present: {needle}")

# Runtime boundary is authoritative: retired models may remain as historical
# source modules, but run_board must reject them.
adapter = Path("models/football/engine/adapter.py").read_text(encoding="utf-8")
if 'model not in {"c", "c2"}' not in adapter:
    failures.append("adapter.py: active board model set is not C+C2 only")

if failures:
    print("WORKFLOW REGRESSION — ACTIVE C+C2 PRODUCTION INVARIANT MISSING")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active production roster is Football C official + C2 shadow.")
