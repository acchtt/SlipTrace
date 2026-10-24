# Rapid Wien — Austria Lustenau ranking/intake omission flag

**Date flagged:** 2026-10-25 ICT  
**Fixture:** Rapid Wien — Austria Lustenau  
**Competition:** Austria Bundesliga  
**Kickoff:** 2026-10-25 00:30 ICT  
**Flag class:** RANKING_INTAKE_FALSE_NEGATIVE / MISSED_FIXTURE_CONTROL  
**Severity:** HIGH diagnostic  
**Selection authority:** ZERO  
**Backfill prohibited:** YES

## Trigger

The fixture was supplied by the user at approximately 2' live, score 0-0, with a confirmed-lineup screenshot.

The active Daily Coverage Ledger was checked during the /xi preflight and no Rapid Wien — Austria Lustenau row was found. Therefore no sealed ranked FOCUS authority existed for normal prematch /xi execution, and the request correctly transitioned to /live rather than recreating a missed prematch action.

## Why this is flagged

Current football evidence at the time of review indicated a materially credible G3 / three-goal route:

- Rapid's attacking XI retained its primary current scoring structure;
- Rapid had strong recent scoring/home control;
- Austria Lustenau entered with repeated defensive leakage;
- the main caution was upper-tail continuation, not the third-goal route itself.

The football-only review therefore considered O2.50 territory substantially credible, with O2.75 only as a possible settlement-aware extension if the normal execution-strength checks had cleared before kickoff. G4/O3.50 was not certified.

This does **not** record a missed bet or retroactive ACT. It records a coverage/ranking omission for prospective QA.

## Audit use

Include this fixture in the next selection-inversion / intake-recall audit and determine exactly where it disappeared:

1. source/date-surface acquisition;
2. league/fixture eligibility;
3. goal-screen admission;
4. bounded low-priority/control research;
5. rank research/persistence;
6. workload allocation versus true board state.

Compare the frozen pre-kickoff evidence available to the pipeline only. Do not use the eventual final score to promote, demote or tune thresholds.

## Required audit label

`MISSED_FIXTURE_CONTROL_RAPID_WIEN_AUSTRIA_LUSTENAU_20261025`
