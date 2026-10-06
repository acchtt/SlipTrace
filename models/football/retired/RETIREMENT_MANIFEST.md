# Retired Football Model Artifacts

**Status:** HISTORICAL SOURCE ONLY  
**Effective retirement:** 2026-10-06  
**Current production roster:** Football C official + Football C2 shadow

This directory documents the boundary between current production code and preserved historical C3/C4 artifacts.

## Current rule

C3 and C4 must not participate in a new/current:
- /rank board;
- /xi decision;
- /live action;
- Website Pick;
- active model-accounting payload;
- forward model-comparison metric.

"All models" means the active roster: C + C2.

## Preserved historical artifacts

The following repository surfaces may remain because they describe or preserve old prospective work:

- `models/football/challengers/football-c3/**`
- `models/football/challengers/football-c4/**`
- `models/football/airtable/FOOTBALL_C3_AIRTABLE.md`
- `models/football/airtable/FOOTBALL_C4_AIRTABLE.md`
- `models/football/engine/board_triplet_cli.py`
- `models/football/engine/decision_triplet_cli.py`
- `models/football/engine/c4_semantic.py`
- `models/football/engine/c4_semantic_cli.py`
- `models/football/engine/c4_schema.json`
- historical C3/C4 tests and dated QA artifacts
- historical Airtable C3/C4 columns and frozen records
- Git history from the period in which those challengers were active.

These files are not current runtime dependencies.

## Active production files must not depend on retired models

Current active surfaces must be C+C2-only:
- `CURRENT_MODEL.md`
- `prompts/01_WORK_DAILY_SWEEP.md`
- `prompts/02_NORMAL_CHAT_XI_ODDS.md`
- `prompts/03_NORMAL_CHAT_LIVE.md`
- `prompts/04_WORK_POST_SLATE_AUDIT.md`
- `prompts/06_NORMAL_CHAT_REPORT.md`
- `prompts/COMMAND_ALIASES.md`
- `engine/core.py`
- `engine/adapter.py`
- `engine/schema.json`
- `engine/runtime_probe.py`
- `engine/xi_portable.py`
- current runtime/bootstrap/reconciliation/accounting procedures.

A current runtime/launcher must fail QA if it reintroduces:
- model=c3 or model=c4;
- triplet execution as a current requirement;
- C4 compilation as a current rank requirement;
- C3/C4 current persistence/accounting requirements.

## Historical audit fidelity

Do not delete or rewrite prospectively frozen historical C3/C4 data.

Historical retired-model settlement is allowed only when:
1. the historical row was genuinely frozen before outcome;
2. the model's own line/action/accounting state exists;
3. no missing state is reconstructed from FT/current information.

Use explicit historical accounting mode where supported.

## Executability

Preserved retired engine scripts are archival source, not supported current executables. Their exact original dependencies are preserved by Git history.

Do not modify active C/C2 code to make a retired script executable.

If an old C3/C4 result must be investigated, prefer the frozen persisted output and the original Git revision over replaying it against the current engine.

## Deletion policy

Retired artifacts may be physically deleted later if:
- all required historical audit information is safely persisted elsewhere; and
- no user workflow relies on repository-local historical source inspection.

Until then, preservation does not imply authority.
