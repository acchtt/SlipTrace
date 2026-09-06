# Current Live Handoff — Invictus Gaming vs Team WE — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — PRE-G1 / NO POSITIONS YET  
**Session lock:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Invictus Gaming vs Team WE — LPL 2026 Split 3 Playoffs Lower Bracket Quarterfinal 1, Bo5 Fearless Draft. Scheduled start `2026-09-06 13:00 UTC+7`.

- No map has been entered under this lock.
- No IG-WE Position exists yet.
- Airtable is untouched for this series.
- Same-series results must not alter frozen `K/P0/TK0`; prior maps may affect only Fearless champion availability.

## Frozen benchmark

- `B(IG)=+0.797272`
- `B(WE)=-0.938274`
- `GAP(IG-WE)=+1.735546 SD`
- `IG K=+2 / P0=60%`
- `WE K=-2 / P0=40%`
- `TK0=33.40`

Expected lineups:
- IG: TheShy / Wei / Rookie / Assum / Meiko
- WE: Cube / Monki / Karis / About / Erha

Roster adjustments used in the frozen benchmark:
- IG current-only due at least three material Split 2 -> Split 3 starter changes;
- WE normal 70/30 blend with lineup continuity.

## Pre-series market board — context only / excluded from benchmark

User supplied a readable sportsbook screenshot pre-G1. The book UI labels the event `LPL 2026 Grand Finals`; independent schedule sources identify this IG-WE match as the LPL Split 3 Playoffs Lower Bracket Quarterfinal 1, so the active series scope remains unchanged.

Captured series markets:
- Series winner: `IG 1.475 / WE 2.616`;
- IG -1.5 maps: `IG 2.057 / WE +1.5 1.712`;
- WE -1.5 maps: `IG +1.5 1.254 / WE 3.663`;
- IG -2.5 maps: `IG 4.158 / WE +2.5 1.205`;
- WE -2.5 maps: `IG +2.5 1.070 / WE 7.376`;
- Total maps 3.5: `Over 1.329 / Under 3.145`;
- Total maps 4.5: `Over 2.496 / Under 1.493`;
- Exact score: `IG 3-0 3.889 / WE 3-0 6.406 / IG 3-1 3.677 / WE 3-1 5.555 / IG 3-2 3.952 / WE 3-2 5.050`.

Governance:
- these series prices are NOT inputs to `B/K/P0/TK0`;
- no series-market Position is created;
- do not use pre-series odds as causal evidence for any map pick;
- map positions still require final draft + exact Game market board.

## Q3 overlay

- ML: `D_DIAGNOSTIC_ONLY=YES`, `D_PROBABILITY_CONTRIBUTION=0`; frozen P0 only.
- ML floor `1.45` is an execution filter only; it does not automatically force the dog.
- KH: 70% probability cap, signed margin bins, numeric 10+ tails; `<5` must align with ML; `±5.5+` may be independent.
- Duration: frozen v1.1 formula and 31.0m anchor; Over has `OVER_BRANCH_WARNING=YES` and `DURATION_OVER_SHADOW_ONLY=YES`.
- TK: persist both `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` numeric branches.
- Four-family validation remains `0.25u shadow each / 0u actual`.
- Airtable writes only at map end; no retroactive positions.

## Cohort entering series

- `80 positions / 20 per family`
- `39W-41L / -1.49750u`
- ML `5-15 / -2.44150u`
- KH `10-10 / -0.31200u`
- Duration `13-7 / +1.08650u`
- TK `11-9 / +0.16950u`

Next preferred structural checkpoint: `120 positions / 30 per family`.

## Next action

**READY FOR GAME 1 FINAL DRAFT + EXACT BOARD.**

Do not create any Position from schedule/market alone.