#!/usr/bin/env python3
"""Production invariant check for the active Football C + C2 roster.

Historical C3/C4 files may remain for audit history, but no active launcher or
runtime contract may require them for a new production decision.
"""
from pathlib import Path
import sys

REQUIRED = {
    "models/football/CURRENT_MODEL.md": [
        "ACTIVE NEW STAGES",
        "models/football/stages_v4/SWEEP.md",
        "models/football/stages_v4/RANK.md",
        "Historical V3 coordinator — non-authoritative",
        "Football C is official; Football C2 is the only shadow challenger",
    ],
    "models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md": [
        "Football C3 and Football C4 are retired",
        "C + C2",
        "C+C2 EXCEPTION INCOMPLETE",
        "python xi_portable.py xi --c <c_football.json> --c2 <c2_football.json>",
        "EXECUTED_C_C2_FOOTBALL_ONLY",
    ],
    "models/football/prompts/sweep.md": [
        "canonical V4 redirect",
        "models/football/stages_v4/SWEEP.md",
        "Retired V1–V3",
    ],
    "models/football/prompts/rank.md": [
        "canonical V4 redirect",
        "models/football/stages_v4/RANK.md",
        "--source",
        "--status-refresh",
    ],
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md": [
        "ACTIVE ROSTER OVERRIDE",
        "xi_portable.py xi --c c_football.json --c2 c2_football.json",
        "USER_SCREENSHOT_ONLY",
        "Command alias:** `/xi`",
    ],
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md": [
        "ACTIVE ROSTER",
        "live_price_action_engine_status=NOT_IMPLEMENTED_V4",
        "Command alias:** `/live`",
    ],
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md": [
        "ACTIVE ROSTER",
        "For **current V4**, check only:",
        "For **historical V1–V3** records",
        "Command alias:** `/audit`",
    ],
    "models/football/stages_v4/stage.py": [
        "V4_SOURCE_REPLAY_REQUIRED",
        "V4_STATUS_REFRESH_INCOMPLETE",
        '"source_replayed": True',
        '"current_fixture_status_checked": True',
    ],
    "models/football/engine/xi_v4_queue.py": [
        "v4_original_source",
        "v4_status_refresh",
        "original_source_sha256",
        "status_refresh_sha256",
        "source_replayed",
        "current_fixture_status_checked",
    ],
    "models/football/engine/step2_queue_guard.py": [
        "v4_provenance_chain_verified",
        "v4_original_source_sha256",
        "v4_status_refresh_sha256",
    ],
    "models/football/engine/adapter.py": [
        'model not in {"c", "c2"}',
        "C3/C4 are retired",
        "MAX_FOLLOW = 6",
        "MAX_RESERVE = 4",
        "MAX_FOLLOW_PER_KICKOFF = 2",
        "def run_decision",
    ],
    "models/football/engine/xi_portable.py": [
        "def run_pair_files",
        'sub.add_parser("xi")',
        '"EXECUTED_C_C2_FOOTBALL_ONLY"',
        "SCREENSHOT_CANNOT_INDEPENDENTLY_PROVE_EXECUTABLE_OFFER",
    ],
    "models/football/retired/RETIREMENT_MANIFEST.md": [
        "Current production roster:** Football C official + Football C2 shadow",
        "Do not delete or rewrite prospectively frozen historical C3/C4 data.",
        "Active production files must not depend on retired models",
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
        "- `/sweep` -> `00_NORMAL_CHAT_AISCORE_FETCH.md`",
        "- `/rank` -> `01_WORK_DAILY_SWEEP.md`",
        "## Unified /sweep and /rank V3",
    ],
    "models/football/engine/runtime_probe.py": [
        '"models/football/engine/capacity_replenishment.py"',
        '"models/football/engine/repaired_handoff_normalize.py"',
        '"models/football/engine/step0_handoff_cli.py"',
    ],
    "models/football/engine/step2_queue_guard.py": [
        'result["v4_source_attested"] = True',
    ],
    "models/football/prompts/COMMAND_ALIASES.md": [
        "C2/C3/C4 Step-1 shadow board workflow",
        "C3 Step-2 shadow action",
        "C4 prospectively frozen Step-1 snapshot",
    ],
    "models/football/engine/core.py": [
        "class C3PolicyAssessment",
        "def c3_ranking_key",
        "def decide_c3",
        "FundingState",
        "FundingSource",
    ],
    "models/football/engine/adapter.py": [
        "def parse_c3_policy",
        "rank_assessments_c3",
        "c3_board_state",
        "decide_c3",
    ],
    "models/football/engine/schema.json": [
        "\"c3\"",
        "\"C3-PASS\"",
        "\"c3_funding_rechecked\"",
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

# Runtime boundary is authoritative. Retired source may remain only in
# explicitly historical/retired files; active core/adapter/schema stay C+C2-only.
adapter = Path("models/football/engine/adapter.py").read_text(encoding="utf-8")
if 'model not in {"c", "c2"}' not in adapter:
    failures.append("adapter.py: active board model set is not C+C2 only")

if failures:
    print("WORKFLOW REGRESSION — ACTIVE C+C2 PRODUCTION INVARIANT MISSING")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active production roster is Football C official + C2 shadow.")
