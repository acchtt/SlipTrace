# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Round 1 — Karmine Corp vs GIANTX — Bo5 Fearless Draft`  
**Target map at activation:** `Game 1`  
**Supersedes:** `LOL-2026-09-05-V13-LEC-VIT-G2-DRAFTONLY-FORCEDCHOICE-Q2-1903-UTC7` (closed historical lock)  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q2`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / FORCE ONE SIDE PER OFFERED MARKET / IGNORE DISPLAYED LIVE STATE FOR PREDICTION`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u per family`

## Authority and overlay

Load `models/lol/CURRENT_MODEL.md` and the complete v1.3 stack from authority commit `6018e7706772554d6318c1af4a9548ca4f25cd95`. Canonical `CURRENT_MODEL.md` remains unchanged. This lock explicitly activates the experimental forced-choice Q2 overlay prospectively for KC-GX.

Enabled forced-choice families:
- Moneyline;
- Kill Handicap;
- Duration;
- Total Kills.

Execution controls:
- exactly one canonical side/line per executable family;
- `0.25u shadow / 0u actual` per family;
- supplied final draft + exact board is standing authorization for the four shadow positions;
- price is used only after price-blind projections are locked;
- if both sides are negative EV, select the less-negative eligible side and tag `FORCED_NEG_EV=YES`;
- Airtable writes occur only at map end;
- no retroactive position creation;
- no chasing, rescue, martingale, averaging down, or stake escalation.

## User-directed Moneyline price-floor override — ACTIVE prospectively

The user explicitly stated on activation: `moneyline under 1.45 is not worth taking`.

Therefore for this lock and subsequent forced-choice maps unless revoked:
- selected Moneyline odds must be `>=1.45`;
- an ML side quoted below `1.45` is execution-ineligible even if it is the benchmark favorite;
- the price floor does not alter `K`, `P0`, DIM, or model probability;
- if the opposite ML side is offered at `>=1.45`, evaluate/select it under the forced-choice side-comparison rule;
- never create a sub-1.45 canonical ML position merely to satisfy forced-choice bookkeeping.

## Q2 checkpoint quarantine — ACTIVE

### Moneyline
- full `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP` DIM mandatory and persisted;
- certify `D=+1/0/-1` under adversarial two-independent-mechanism rule;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- forced-choice ML probability uses frozen `P0` only.

### Kill Handicap
- full signed margin bins before price;
- explicit numeric mass in both teams' 10+ kill tails;
- `KH_MODEL_PROB_CAP=70%` for execution edge reporting;
- absolute handicap `<5` kills => selected KH team must align with selected ML team;
- `±5.5` or wider may be independent.

### Duration
- v1.1 formula and `31.0m` anchor remain frozen;
- persist draft-only `V/Q/H/T/F` before price;
- selected Over => `OVER_BRANCH_WARNING=YES` diagnostically.

### Total Kills
- frozen series `TK0` below;
- persist full pre-price bins;
- explicitly persist numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch separately from clean-cascade/two-sided-brawl mass.

## Series identification / timing note

Current target is Karmine Corp (`KC`) vs GIANTX (`GX`), LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

A prior prep handoff carried a public scheduled time of `15:00 UTC / 22:00 UTC+7`, but the user has now supplied an executable Game 1 live board and final draft at approximately `19:50 UTC+7`. User-supplied current-match evidence overrides the stale prep timing for activation purposes. No live in-map state is used in prediction.

## Expected current lineups

KC:
- Canna — TOP
- Yike — JUNGLE
- Kyeahoo — MID
- Caliste — ADC
- Busio — SUPPORT

GX:
- Oscarinin — TOP
- Isma — JUNGLE
- Jackies — MID
- Flakked — ADC
- Jun — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Frozen KC vs GX Gol.gg benchmark

Primary source: completed `LEC 2026 Summer Season` team table, with completed `LEC 2026 Spring Season` as previous comparable split where continuity permits. Sportsbook price and current-series results are excluded.

- `B_current(KC)=+1.802032`
- `B_current(GX)=-0.224502`
- `B_previous(KC)=+0.766645`
- `B_previous(GX)=-0.282555` descriptive only
- KC roster continuity: normal `70/30`
- GX roster continuity: current-only due two material starter changes
- `B_raw(KC)=+1.491416`
- `B_raw(GX)=-0.224502`
- after full-peer re-standardization: `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`

Frozen prior:
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`

Compact record:
`TEAM_BENCH[LEAGUE=LEC2026;CURRENT=SUMMER_SEASON;PREVIOUS=SPRING_SEASON;G_KC=20;G_GX=24;B_CUR_KC=1.802032;B_CUR_GX=-0.224502;B_PREV_KC=0.766645;B_PREV_GX=-0.282555;BLEND_KC=1.491416;BLEND_GX=-0.224502;B_KC=1.625030;B_GX=-0.241316;GAP_KC_GX=1.866346;K_KC=+2;K_GX=-2;ROSTER_ADJ_KC=NORMAL70_30;ROSTER_ADJ_GX=CURRENT_ONLY_TWO_CHANGES;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current Summer environments:
- KC = `30.8` total kills/game environment;
- GX = `26.2` total kills/game environment.

`TK0=(30.8+26.2)/2=28.50 kills`.

## Cohort entering KC-GX

- `64 Positions / 16 per family`
- overall `33W-31L / -0.64300u`
- ML `4-12 / -2.26775u`
- KH `8-8 / -0.23675u`
- Duration `12-4 / +1.61050u`
- TK `9-7 / +0.25100u`
- actual exposure `0u`

Preferred next checkpoint: `80 total / 20 per family` — 4 more fully recorded maps / 16 positions.

## Game 1 activation state

Final G1 draft and exact board have been supplied prospectively. Four canonical positions are locked in the current live handoff. Airtable remains untouched until G1 ends.
