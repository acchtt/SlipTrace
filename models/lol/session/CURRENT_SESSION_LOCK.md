# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LCK-T1-DK-DRAFTONLY-FORCEDCHOICE-Q3-1704-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 3 — T1 vs Dplus KIA — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 17:00 KST / 15:00 UTC+7`  
**Activation time:** `2026-09-06 17:04 UTC+7`  
**Target map at activation:** `Game 3`  
**Series state at activation:** `T1 1-1 Dplus KIA` from current schedule/live listing; G1/G2 are historical context only and receive no retroactive Positions.  
**Supersedes as current target:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7` (IG-WE G4 remains prospectively locked but unsettled in its historical handoff; not cancelled).  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q3`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / FOUR-FAMILY SHADOW VALIDATION / IGNORE DISPLAYED LIVE STATE FOR PREDICTION`  
**Default shadow stake:** `0.25u per family`  
**Actual exposure:** `0u`

## Authority boundary

Load `models/lol/CURRENT_MODEL.md` and the complete v1.3 stack from authority commit `979c955667d63e913cb7eb2ecff915fc1f83920b`. Canonical `CURRENT_MODEL.md` remains unchanged. This lock explicitly activates the experimental Q3 draft-only forced-choice overlay prospectively for T1-DK beginning with Game 3.

No T1-DK G1/G2 Position may be created. Same-series G1/G2 results are excluded from `B/K/P0/TK0`; they may affect only Fearless champion availability.

## Q3 validation overlay — ACTIVE

### Moneyline
- full draft DIM mandatory and persisted;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- forced-choice ML probability uses frozen `P0` only;
- `ML_PRICE_FLOOR=1.45` is an execution-eligibility filter only and does not transfer probability/edge to the opposite side;
- a dog above 1.45 may be selected only if it independently wins the model-vs-price side comparison;
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

T1:
- Doran — TOP
- Oner — JUNGLE
- Faker — MID
- Peyz — ADC
- Keria — SUPPORT

Dplus KIA:
- Siwoo — TOP
- Lucid — JUNGLE
- ShowMaker — MID
- Smash — ADC
- Career — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Fresh frozen pre-series Gol.gg benchmark

Benchmark reconstruction is frozen to information available before T1-DK Game 1 and excludes this series' G1/G2 outcomes. Primary current peer set: completed `LCK 2026 Rounds 3-4`. Previous comparable split: `LCK 2026 Rounds 1-2`. Both teams use the established LCK normal `70/30` continuity treatment.

Current split target inputs:
- DK: `20 games / 55.0% WR / GDM +25 / GD@15 -694 / TowerDiff +1.1 / DRA 54.4% / NASH 61.1% / kills 12.9 / deaths 13.0`;
- T1: `19 games / 42.1% WR / GDM +5 / GD@15 +222 / TowerDiff -0.4 / DRA 50.3% / NASH 50.9% / kills 13.4 / deaths 13.5`.

Previous split target inputs:
- DK: `42 games / 57.1% WR / GDM +64 / GD@15 +619 / TowerDiff +1.2 / DRA 48.8% / NASH 49.1%`;
- T1: `40 games / 75.0% WR / GDM +139 / GD@15 +674 / TowerDiff +2.5 / DRA 53.9% / NASH 54.2%`.

League-relative split scores under the active benchmark formula:
- `B_current(DK)=+0.174447`
- `B_previous(DK)=+0.412956`
- `B_current(T1)=-0.177983`
- `B_previous(T1)=+0.902156`

70/30 raw blends:
- `B_raw(DK)=+0.246000`
- `B_raw(T1)=+0.146058`

After peer-wide blended-score re-standardization:
- `B(DK)=+0.334587`
- `B(T1)=+0.198656`
- `GAP(DK-T1)=+0.135931 SD`

Frozen Moneyline prior:
- `DK K=0 / P0=50%`
- `T1 K=0 / P0=50%`

Compact benchmark record:
`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=ROUNDS3-4;PREVIOUS=ROUNDS1-2;G_DK=20;G_T1=19;B_CUR_DK=0.174447;B_CUR_T1=-0.177983;B_PREV_DK=0.412956;B_PREV_T1=0.902156;BLEND_DK=0.246000;BLEND_T1=0.146058;B_DK=0.334587;B_T1=0.198656;GAP_DK_T1=0.135931;K_DK=0;K_T1=0;ROSTER_ADJ_DK=NORMAL70_30;ROSTER_ADJ_T1=NORMAL70_30;PRICE_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current Rounds 3-4 environments:
- DK: `12.9 kills + 13.0 deaths = 25.9`
- T1: `13.4 kills + 13.5 deaths = 26.9`

`TK0=(25.9+26.9)/2=26.40 kills`.

## Cohort entering T1-DK

Settled cohort before any T1-DK Position:
- `92 settled positions / 23 per family / 23 settled maps`
- overall `46W-46L / -1.38275u`
- ML `7-16 / -2.35500u`
- KH `13-10 / +0.34850u`
- Duration `14-9 / +0.77725u`
- TK `12-11 / -0.15350u`
- actual exposure `0u`

Outstanding historical prospective exposure in the shadow ledger:
- IG-WE G4 has `4` already-locked but unsettled shadow Positions; preserve them in the IG-WE handoff and settle only on explicit final evidence.

Preferred next structural checkpoint remains `120 settled positions / 30 per family`.

## Activation state

No T1-DK Position exists yet. Airtable is untouched for T1-DK. Await **Game 3 final draft + exact board** before any canonical shadow Position is created.