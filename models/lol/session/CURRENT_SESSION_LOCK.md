# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LPL 2026 Split 3 Playoffs — Lower Bracket Quarterfinal 1 — Invictus Gaming vs Team WE — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 13:00 UTC+7`  
**Target map at activation:** `Game 1`  
**Supersedes:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7` (closed historical lock)  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q3`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / FOUR-FAMILY SHADOW VALIDATION / IGNORE DISPLAYED LIVE STATE FOR PREDICTION`  
**Default shadow stake:** `0.25u per family`  
**Actual exposure:** `0u`

## Authority boundary

Load `models/lol/CURRENT_MODEL.md` and the complete v1.3 stack from authority commit `979c955667d63e913cb7eb2ecff915fc1f83920b`. Canonical `CURRENT_MODEL.md` remains unchanged. This lock explicitly activates the experimental Q3 draft-only forced-choice overlay prospectively for IG-WE.

Enabled validation families:
- Moneyline;
- Kill Handicap;
- Duration;
- Total Kills.

Controls:
- exactly one canonical shadow selection per offered family when the forced-choice validation protocol requires a record;
- `0.25u shadow / 0u actual` per family;
- final draft + exact board supplied before material state change is standing authorization for the four shadow positions;
- price is analytical evidence only after price-blind projections are locked;
- Airtable writes only at map end;
- no retroactive position creation;
- no chasing, rescue, martingale, averaging down, or stake escalation;
- same-series results never update frozen `K/P0/TK0`; prior maps may inform only Fearless champion availability.

## Q3 validation overlay — ACTIVE

### Moneyline
- full draft DIM remains mandatory and persisted;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- forced-choice ML probability uses frozen `P0` only;
- `ML_PRICE_FLOOR=1.45` is an execution-eligibility filter only and does not transfer probability/edge to the opposite side;
- a dog above 1.45 may be selected only if it independently wins the model-vs-price comparison;
- shadow forced-choice bookkeeping may still record the less-negative eligible side with `FORCED_NEG_EV=YES` if necessary;
- any non-shadow/actual execution layer must PASS if no eligible positive-edge ML exists.

### Kill Handicap
- full signed margin bins before price;
- explicit numeric mass in both teams' 10+ kill tails;
- `KH_MODEL_PROB_CAP=70%` for execution-edge reporting;
- absolute handicap `<5` => selected KH team must align with selected ML team;
- `±5.5` or wider may be independent.

### Duration
- v1.1 formula and `31.0m` neutral anchor unchanged;
- persist draft-only `V/Q/H/T/F` before price;
- selected Over => `OVER_BRANCH_WARNING=YES`;
- `DURATION_OVER_SHADOW_ONLY=YES`: Over may be logged for validation but is not an approved positive execution signal; Under remains eligible under the normal model-vs-price test.

### Total Kills
- frozen series `TK0` below;
- persist full pre-price bins;
- separately persist numeric branches for:
  1. `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION`;
  2. `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY`.

## Expected current lineups

IG:
- TheShy — TOP
- Wei — JUNGLE
- Rookie — MID
- Assum — ADC
- Meiko — SUPPORT

WE:
- Cube — TOP
- Monki — JUNGLE
- Karis — MID
- About — ADC
- Erha — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Frozen pre-series Gol.gg benchmark

Primary current peer set: completed `LPL 2026 Split 3` team table before IG-WE Game 1. Previous comparable split: `LPL 2026 Split 2`, used only where roster continuity permits. Sportsbook price, current-series results, and current-map state are excluded.

Target current split inputs:
- IG: `15 games / 60.0% WR / GDM +102 / GD@15 +615 / TowerDiff +2.6 / DRA 65.7% / NASH 71.1%`;
- WE: `33 games / 48.5% WR / GDM -67 / GD@15 -815 / TowerDiff -0.6 / DRA 46.9% / NASH 47.9%`.

Roster continuity:
- IG: `CURRENT_ONLY` — at least three material Split 2 -> Split 3 starter changes; current sample is 15 games;
- WE: `NORMAL70_30` — same core five across Split 2 and Split 3.

After peer-wide continuity-adjusted blending and re-standardization:
- `B(IG)=+0.797272`
- `B(WE)=-0.938274`
- `GAP(IG-WE)=+1.735546 SD`

Frozen prior:
- `IG K=+2 / P0=60%`
- `WE K=-2 / P0=40%`

Compact benchmark record:
`TEAM_BENCH[LEAGUE=LPL2026;CURRENT=SPLIT3;PREVIOUS=SPLIT2;G_IG=15;G_WE=33;B_CUR_IG=0.769250;B_CUR_WE=-0.398881;B_PREV_IG=-0.375925;B_PREV_WE=-2.134560;BLEND_IG=0.769250;BLEND_WE=-0.919585;B_IG=0.797272;B_WE=-0.938274;GAP_IG_WE=1.735546;K_IG=+2;K_WE=-2;ROSTER_ADJ_IG=CURRENT_ONLY_3PLUS_CHANGES;ROSTER_ADJ_WE=NORMAL70_30;PRICE_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current Split 3 environments:
- IG: `18.0 kills + 15.9 deaths = 33.9 total-kill environment`;
- WE: `14.8 kills + 18.1 deaths = 32.9 total-kill environment`.

`TK0=(33.9+32.9)/2=33.40 kills`.

## Cohort entering IG-WE

- `80 positions / 20 per family / 20 maps`
- overall `39W-41L / -1.49750u`
- ML `5-15 / -2.44150u`
- KH `10-10 / -0.31200u`
- Duration `13-7 / +1.08650u`
- TK `11-9 / +0.16950u`
- actual exposure `0u`

Preferred next structural checkpoint: `120 positions / 30 per family` = 10 additional fully recorded maps / 40 positions.

## Activation state

No IG-WE position exists yet. Airtable is untouched for this series. Await Game 1 final draft + exact board before any canonical shadow position is created.