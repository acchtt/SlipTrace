# 00 — Normal Chat: AiScore Broad Senior Intake

**Use in:** Normal Chat, high reasoning.

Read upstream `models/football/CURRENT_MODEL.md` first.

Football C is the active official model.

## Purpose

Build a trustworthy **BROAD SENIOR** AiScore universe for the requested window, apply only hard identity/scope exclusions, and send every remaining reasonable senior first-team fixture to Football C.

Step 0 must not pre-rank football quality and must not recreate the old Football A narrow-core league allowlist.

Operational principle:

`NORMALIZE WINDOW -> DISCOVER COMPLETE SENIOR BLOCKS -> PRESERVE AISCORE IDENTITY/TIME -> APPLY HARD EXCLUSIONS ONLY -> VERIFY ADMITTED TIMES -> PACKAGE ALL SURVIVING SENIOR FIXTURES -> FOOTBALL C SCREENS THEM`

Measure the whole funnel:

`RAW SENIOR -> HARD EXCLUDED -> ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS -> C-BET/C-WAIT`

## Default mode

Default:
`BROAD_SENIOR_PRODUCTION`

Do not use the legacy `FAST_PRODUCTION / NARROW_CORE` allowlist behavior.

A prior sweep may be reused only if it was itself completed under BROAD_SENIOR_PRODUCTION for a window fully covering the request. A narrow-core run cannot prove broad-senior completeness.

## Source authority

AiScore is the fixture-discovery authority. Other sources may research a known AiScore fixture later, but may not add fixtures to the production universe.

## Time integrity

Resolve the requested ICT/UTC boundaries once and follow `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

Before packaging, every admitted fixture must have an authoritative zoned AiScore time from explicit Match Info UTC, an AiScore epoch/zoned ISO timestamp, or an explicit offset. Convert exactly once to Asia/Ho_Chi_Minh and prove it lies inside the requested window.

Do not guess timezone from geography or treat a bare display clock as UTC.

## Broad senior discovery — mandatory

Inspect every AiScore competition block visible on the touched date surfaces and account for every potentially reasonable senior first-team fixture in-window.

Do not restrict discovery to PRIORITY/NORMAL registry entries.

Normally admit to Football C:
- senior top divisions;
- professional senior lower divisions;
- senior international qualifiers/tournaments;
- senior continental club competitions;
- senior national FA cups;
- senior league/professional cups;
- senior women's first-team competitions when identity/data are usable;
- other reasonable senior first-team fixtures.

A fixture being unfamiliar, historically low-scoring, outside a legacy registry, or previously CONDITIONAL is not enough to remove it at Step 0. Those are Football C screening questions.

## Hard exclusions only

Exclude before Football C only when clearly outside production scope or unsafe to identify:

- youth/Uxx-only competitions;
- academy/junior competitions;
- reserve/B/development-only competitions;
- amateur or clearly semi-professional micro competitions with unreliable identity/data;
- regional/state/provincial competitions outside the intended senior professional universe;
- school/university/military/company competitions;
- friendlies/exhibitions unless explicitly requested;
- cancelled/postponed/abandoned/already-finished fixtures for an upcoming sweep;
- unresolved fixture/home-away identity;
- unresolved authoritative kickoff time;
- duplicate identities.

### Professional reserve-brand exception

If a reserve/Jong/U21-branded side is an official participant in a normal professional senior league, do not exclude solely because of the team name. Treat the competition as the scope authority.

## No longer Step-0 exclusions

Do not exclude solely because a fixture is:
- from a legacy LOW-GOAL league;
- from a legacy HARD-EXCLUDE country;
- from Finland or Japan;
- from a professional lower division;
- from a senior cup previously considered small;
- from a legacy CONDITIONAL league;
- unfamiliar or absent from a priority list.

If it is a reasonable senior first-team fixture with usable identity, send it to Football C.

## Completeness

Production completeness means every potentially reasonable senior first-team block in the requested window has been accounted for.

A visible senior block skipped because it is not in a registry makes the handoff incomplete.

For cross-midnight/early-morning windows, independently inspect the terminal ICT date and UTC date containing the end boundary.

`terminal_interval_ict = max(window_start_ict, window_end_ict - 6h) -> window_end_ict`

Record `terminal_scan_complete=true|false`. Never infer terminal completeness from the latest kickoff already found.

Every visibly surfaced senior cup/continental block must be accounted for. No legacy "main cups only" filter.

## Persistence skeleton

Use the existing football Airtable coverage contract.

For every discovered in-window fixture preserve enough to distinguish:
- `ADMITTED_TO_C`
- `HARD_EXCLUDED`
- `UNRESOLVED`

For admitted fixtures preserve Match, Competition, AiScore identity, verified UTC/ICT kickoff, time provenance, status, and `BROAD_SENIOR_PRODUCTION` in notes.

Do not populate Football C rank/routes/burden here. Step 1 owns football-quality screening.

## Work-readiness gate

Package only when:
- `complete=true`
- `actionable_complete=true`
- `work_ready=true`
- every touched senior block is accounted for
- terminal scan is complete
- every admitted fixture has resolved identity/time
- every admitted fixture lies inside the ICT window
- admitted count matches the handoff array
- no legacy registry/narrow-core filter removed a reasonable senior fixture

If not:

`HANDOFF INCOMPLETE — BROAD SENIOR COVERAGE GAP`

## ZIP handoff

Create one canonical UTF-8 `AISCORE_FIXTURES_*.txt` at ZIP root and attach only the ZIP normally.

Required handoff metadata:
- `model=Football C`
- `sweep_scope_mode=BROAD_SENIOR_PRODUCTION`
- requested ICT/UTC window
- listing dates checked
- terminal interval/listing dates
- `terminal_scan_complete=true`
- `complete=true`
- `actionable_complete=true`
- `work_ready=true`
- `raw_senior_count`
- `hard_excluded_count`
- `admitted_to_c_count`
- hard-exclusion reason counts
- all admitted fixtures with AiScore identity, competition, source kickoff, verified UTC/ICT and time provenance

Do not include only "interesting" matches. This is the complete C-eligible senior universe.

## Step-0 boundary

Step 0 does not research scoring mechanisms, judge Over quality, assign C-PASS/WATCH/FOCUS, choose supported burden, rank fixtures, inspect confirmed XI, fetch bookmaker odds, create Decision States, or issue betting decisions.

Football C Step 1 owns all football-quality screening.

## Output

Return:

`BROAD SENIOR HANDOFF COMPLETE`

with requested window, raw senior count, hard-excluded count, admitted-to-C count, unresolved count, and ZIP filename.

If incomplete, report the blocker and do not send a partial production handoff.
