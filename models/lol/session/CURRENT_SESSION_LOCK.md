# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Final — G2 Esports vs Karmine Corp — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 15:00 UTC / 22:00 UTC+7`  
**Activation:** `2026-09-06 18:59 UTC+7`, before the scheduled series start.  
**Current target:** `Game 1`  
**Supersedes as current target only:** `LOL-2026-09-06-V13-LCK-T1-DK-DRAFTONLY-FORCEDCHOICE-Q3-1704-UTC7`; T1-DK G3 is settled and no T1-DK G4 Position existed at the switch.  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q3`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / 0.25u EACH / 0u ACTUAL`

## Authority boundary

Canonical `models/lol/CURRENT_MODEL.md` remains unchanged. This lock activates the experimental Q3 forced-choice validation overlay prospectively for G2-KC beginning with Game 1.

No sportsbook price, Sep 5 playoff result, same-series result, or current-map state is used in the frozen benchmark below. Same-series outcomes never update `B/K/P0/TK0`; prior maps may affect only Fearless champion availability.

## Expected current lineups

G2 Esports:
- BrokenBlade — TOP
- SkewMond — JUNGLE
- Caps — MID
- Hans Sama — ADC
- Labrov — SUPPORT

Karmine Corp:
- Canna — TOP
- Yike — JUNGLE
- kyeahoo — MID
- Caliste — ADC
- Busio — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Fresh frozen pre-series Gol.gg benchmark

Primary current peer set: completed `LEC 2026 Summer Season`; previous comparable split: completed `LEC 2026 Spring Season`.

Roster continuity:
- G2: `NORMAL70_30`.
- KC: `NORMAL70_30`.

Target split scores under the active benchmark formula:
- `B_current(G2)=+0.838442`
- `B_previous(G2)=+1.099925`
- `B_raw(G2)=+0.916887`
- `B(G2)=+1.000135`
- `B_current(KC)=+1.802032`
- `B_previous(KC)=+0.766645`
- `B_raw(KC)=+1.491416`
- `B(KC)=+1.625030`

Pairwise frozen prior:
- `GAP(KC-G2)=+0.624895 SD`
- `KC K=+1 / P0=55%`
- `G2 K=-1 / P0=45%`

Compact record:
`TEAM_BENCH[LEAGUE=LEC2026;CURRENT=SUMMER_SEASON;PREVIOUS=SPRING_SEASON;B_CUR_G2=0.838442;B_PREV_G2=1.099925;BLEND_G2=0.916887;B_G2=1.000135;B_CUR_KC=1.802032;B_PREV_KC=0.766645;BLEND_KC=1.491416;B_KC=1.625030;GAP_KC_G2=0.624895;K_KC=+1;K_G2=-1;ROSTER_ADJ_G2=NORMAL70_30;ROSTER_ADJ_KC=NORMAL70_30;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current Summer environments:
- G2: `16.5 kills + 13.0 deaths = 29.5`.
- KC: `19.1 kills + 11.7 deaths = 30.8`.

`TK0=(29.5+30.8)/2=30.15 kills`.

## Q3 validation overlay — ACTIVE

### Moneyline
- full DIM mandatory and persisted;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- forced-choice ML probability uses frozen `P0` only;
- `ML_PRICE_FLOOR=1.45` is execution eligibility only and does not transfer probability/edge to the opposite side;
- a dog above 1.45 may be selected only if it independently wins the model-vs-price comparison;
- shadow forced-choice bookkeeping may record the less-negative eligible side with `FORCED_NEG_EV=YES` if required;
- actual/non-shadow execution PASSES if no eligible positive-edge ML exists.

### Kill Handicap
- full signed margin bins before price;
- explicit numeric 10+ clean-cascade tails for both sides;
- `KH_MODEL_PROB_CAP=70%` for reporting;
- absolute handicap `<5` => selected KH team must align with selected ML team;
- `±5.5` or wider may be independent.

### Duration
- v1.1 formula and `31.0m` neutral anchor unchanged;
- persist `V/Q/H/T/F` before price;
- selected Over => `OVER_BRANCH_WARNING=YES` and `DURATION_OVER_SHADOW_ONLY=YES`;
- Under remains eligible under the normal model-vs-price test.

### Total Kills
- frozen `TK0=30.15`;
- persist full pre-price bins;
- separately persist numeric:
  1. `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION`;
  2. `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY`.

Execution controls:
- exactly one canonical ML/KH/Duration/TK shadow selection per fully supplied map under validation;
- `0.25u shadow each / 1.00u total / 0u actual`;
- final draft + exact board supplied before material state change is standing authorization for the four shadow positions;
- Airtable writes only at map end;
- no retroactive positions;
- displayed live state is ignored for draft-only prediction.

## Settled cohort entering G2-KC

- `96 positions / 24 per family / 24 settled maps`
- `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

Preferred structural checkpoint: `120 settled positions / 30 per family`.

## Historical outstanding state

- T1-DK G3 is settled; T1 leads 2-1. No T1-DK G4 Position existed when this lock became current.
- IG-WE G4 remains prospectively locked but unsettled in its own historical handoff; this current-target switch does not cancel it.

## Activation state

No G2-KC Position exists yet. Airtable is untouched for G2-KC.

## Next action

**AWAIT G2-KC GAME 1 FINAL DRAFT + EXACT BOARD.**