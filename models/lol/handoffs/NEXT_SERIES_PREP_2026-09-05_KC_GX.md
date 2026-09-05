# Next Series Prep — Karmine Corp vs GIANTX — 2026-09-05

**Status:** PREPPED — NOT YET ACTIVE SESSION LOCK  
**Target:** `LEC 2026 Summer Playoffs — Upper Bracket Round 1 — Karmine Corp vs GIANTX — Bo5 Fearless Draft`  
**Scheduled:** `2026-09-05 15:00 UTC / 22:00 UTC+7`  
**Authority to activate:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Intended overlay if activated:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Fresh series identification

The next scheduled LEC playoff series after VIT-G2 is Karmine Corp (`KC`) vs GIANTX (`GX`), scheduled Sep 5 at 15:00 UTC. It is the second upper-bracket Round 1 Bo5 of the opening playoff day.

No sportsbook price, same-series map result, or current-map state is used in the benchmark below.

## Expected current lineups

Karmine Corp:
- Canna — TOP
- Yike — JUNGLE
- Kyeahoo — MID
- Caliste — ADC
- Busio — SUPPORT

GIANTX:
- Oscarinin — TOP
- Isma — JUNGLE
- Jackies — MID
- Flakked — ADC
- Jun — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Roster continuity

KC retained the same primary five from LEC 2026 Spring to Summer, so normal `70/30 current/previous` weighting applies.

GX changed at least two material starters from Spring to Summer:
- TOP: Lot -> Oscarinin
- ADC: Noah -> Flakked

Therefore the previous split is descriptive only and GX is benchmarked `CURRENT_ONLY` under the active roster-continuity rule.

For full-peer re-standardization, retain the continuity mapping already established for the same completed LEC Summer peer set:
- normal `70/30`: G2, KC, MKOI, NAVI;
- one-change `85/15`: FNC, SHFT, SK, TH, VIT;
- current-only: GX.

## Fresh pre-series Gol.gg benchmark

Primary source: Games of Legends / gol.gg completed `LEC 2026 Summer Season` team table, with completed `LEC 2026 Spring Season` as the previous comparable split where roster continuity permits.

Formula:
`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`.

### Current Summer target inputs

KC — 20 games:
- WinRate `90.0%`
- GDM `+277`
- GD@15 `+1361`
- Towers `8.7-3.9`
- DRA% `61.9`
- NASH% `75.0`
- `B_current(KC)=+1.802032`

GX — 24 games:
- WinRate `54.2%`
- GDM `-39`
- GD@15 `-756`
- Towers `5.8-6.1`
- DRA% `44.0`
- NASH% `46.9`
- `B_current(GX)=-0.224502`

### Previous Spring target inputs

KC:
- WinRate `65.2%`
- GDM `+139`
- GD@15 `+7`
- Towers `7.2-5.0`
- DRA% `63.2`
- NASH% `64.1`
- `B_previous(KC)=+0.766645`

GX:
- WinRate `50.0%`
- GDM `-70`
- GD@15 `-270`
- Towers `5.5-6.5`
- DRA% `48.9`
- NASH% `36.8`
- `B_previous(GX)=-0.282555` (descriptive only; not blended due two material starter changes)

### Blended raw scores

- `B_raw(KC)=0.70*(1.802032)+0.30*(0.766645)=+1.491416`
- `B_raw(GX)=B_current(GX)=-0.224502`

After re-standardizing the full 10-team blended LEC peer set under the continuity mapping above:
- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`

Frozen pre-series strength prior if activated:
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`

Compact record:
`TEAM_BENCH[LEAGUE=LEC2026;CURRENT=SUMMER_SEASON;PREVIOUS=SPRING_SEASON;G_KC=20;G_GX=24;B_CUR_KC=1.802032;B_CUR_GX=-0.224502;B_PREV_KC=0.766645;B_PREV_GX=-0.282555;BLEND_KC=1.491416;BLEND_GX=-0.224502;B_KC=1.625030;B_GX=-0.241316;GAP_KC_GX=1.866346;K_KC=+2;K_GX=-2;ROSTER_ADJ_KC=NORMAL70_30;ROSTER_ADJ_GX=CURRENT_ONLY_TWO_CHANGES;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline if activated

Current Summer total-kill environments:
- KC = `19.1 kills/game + 11.7 deaths/game = 30.8`
- GX = `13.2 kills/game + 13.0 deaths/game = 26.2`

Both current samples exceed 15 games, so no previous split is required for TK.

`TK0=(30.8+26.2)/2=28.50 kills`.

## Q2 overlay to carry forward on activation

Moneyline:
- full DIM mandatory;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- ML probability uses frozen `P0` only.

Kill Handicap:
- full signed margin bins before price;
- numeric 10+ tails for both sides;
- `KH_MODEL_PROB_CAP=70%`;
- `<5` must align with selected ML team; `±5.5+` may diverge.

Duration:
- frozen v1.1 31m-anchor formula;
- persist `V/Q/H/T/F`;
- selected Over => `OVER_BRANCH_WARNING=YES`.

Total Kills:
- frozen `TK0=28.50`;
- full pre-price bins;
- explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch.

Execution:
- exactly one canonical ML/KH/Duration/TK side per fully supplied map;
- `0.25u shadow` each / `0u actual`;
- Airtable only at map end;
- no retroactive positions.

## Cohort entering KC-GX

- `64 Positions / 16 per family`
- overall `33W-31L / -0.64300u`
- ML `4-12 / -2.26775u`
- KH `8-8 / -0.23675u`
- Duration `12-4 / +1.61050u`
- TK `9-7 / +0.25100u`
- actual exposure `0u`

Preferred next checkpoint: `80 total / 20 per family` — 4 more fully recorded maps / 16 positions.

## Activation requirement

This file is prep state only. `CURRENT_SESSION_LOCK.md` remains closed until KC-GX is explicitly activated as the current target.

Before the first KC-GX position:
1. verify the series is current and roster context has not materially changed;
2. write a fresh active Session Authority Lock for KC-GX pointing to authority commit `6018e7706772554d6318c1af4a9548ca4f25cd95`;
3. load this prep handoff last;
4. await final current-map draft/roles + exact board.

Until activation: `MODEL REBUILD IN PROGRESS — HOLD`.