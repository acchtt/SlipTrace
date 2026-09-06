# Current Live Handoff — G2 Esports vs Karmine Corp — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — PRE-G1 / NO POSITIONS YET  
**Session lock:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u EACH / 0u ACTUAL`

## Match

G2 Esports vs Karmine Corp — LEC 2026 Summer Playoffs Upper Bracket Final, Bo5 Fearless Draft.

- Scheduled: `2026-09-06 15:00 UTC / 22:00 UTC+7`.
- Current target: `Game 1`.
- No G2-KC Position exists yet.
- Airtable remains untouched until an explicitly supplied map final.

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

Primary current peer set: completed `LEC 2026 Summer Season`; previous comparable split: completed `LEC 2026 Spring Season`. This reconstruction excludes Sep 5 playoff results and all sportsbook/current-map information.

Roster continuity:
- G2: `NORMAL70_30`.
- KC: `NORMAL70_30`.

Established peer-wide continuity mapping for the completed Summer peer set is preserved for re-standardization: normal `70/30` G2/KC/MKOI/NAVI; one-change `85/15` FNC/SHFT/SK/TH/VIT; GX current-only.

Target split scores under the active benchmark formula:
- `B_current(G2)=+0.838442`
- `B_previous(G2)=+1.099925`
- `B_raw(G2)=+0.916887`
- `B(G2)=+1.000135`
- `B_current(KC)=+1.802032`
- `B_previous(KC)=+0.766645`
- `B_raw(KC)=+1.491416`
- `B(KC)=+1.625030`

Pairwise:
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
- `ML_PRICE_FLOOR=1.45` is execution eligibility only and never transfers probability/edge to the opposite side;
- shadow forced-choice may still record the less-negative eligible side with `FORCED_NEG_EV=YES` if necessary;
- actual/non-shadow layer PASSES if no eligible positive-edge ML exists.

### Kill Handicap
- full signed margin bins before price;
- explicit numeric 10+ tails for both teams;
- `KH_MODEL_PROB_CAP=70%` for reporting;
- absolute handicap `<5` must align with selected ML team;
- `±5.5` or wider may be independent.

### Duration
- v1.1 formula and `31.0m` neutral anchor unchanged;
- persist `V/Q/H/T/F` before price;
- selected Over => `OVER_BRANCH_WARNING=YES` and `DURATION_OVER_SHADOW_ONLY=YES`;
- Under remains eligible under normal model-vs-price comparison.

### Total Kills
- frozen `TK0=30.15`;
- persist full pre-price bins;
- separately persist numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` branches.

Execution controls:
- exactly one canonical ML/KH/Duration/TK shadow selection per fully supplied map under forced-choice validation;
- `0.25u shadow each / 1.00u total / 0u actual`;
- Airtable only at map end;
- no retroactive positions;
- displayed live state is ignored for draft-only prediction.

## Cohort entering G2-KC

- `96 settled positions / 24 per family / 24 settled maps`
- overall `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

Preferred next structural checkpoint: `120 settled positions / 30 per family`.

## Historical outstanding state

- T1-DK G3 is settled; T1 leads that series 2-1. No T1-DK G4 Position existed at this target switch.
- IG-WE G4 remains prospectively locked but unsettled in its own historical handoff. Switching the current target does not cancel it.

## Next action

**AWAIT G2-KC GAME 1 FINAL DRAFT + EXACT BOARD.**