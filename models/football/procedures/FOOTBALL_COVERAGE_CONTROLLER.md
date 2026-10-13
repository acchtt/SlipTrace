# Historical coverage controller — retired

## Status

The former Step0 coverage controller, actionable_complete/work_ready state,
capacity/replenishment rules, repaired handoffs and frozen PRE Work board are
V1–V3 history.

They are not part of current Football V4.

## Current coverage authority

Use:

- models/football/stages_v4/SWEEP.md
- models/football/stages_v4/source_completeness.py
- models/football/stages_v4/league_registry.py
- models/football/stages_v4/goals_first_intake.py
- models/football/stages_v4/stage.py

Current V4 coverage flow:

COMPLETE PROVIDER DATE SURFACES
-> SOURCE-VISIBLE FIXTURE UNION
-> EXCLUSIONS / REGISTRY / DISCOVERY
-> GOAL-HISTORY SCREEN
-> GOAL_PRIORITY + visible pending/watch/excluded ledger
-> V4_SWEEP_READY

There is no active:

- work_ready;
- actionable_complete;
- capacity/replenishment queue;
- fixed first-eight board;
- repaired ZIP handoff;
- second Work structural screen;
- frozen PRE FOCUS/WATCHLIST/PASS board produced by this controller.

C/C2 board state is produced later by current V4 /rank.

## Historical audit

Old records may be reconstructed with the exact historical revision and
historical fields that existed at the time. Never project those controls onto a
current V4 run and never require current /sweep or /rank to satisfy them.
