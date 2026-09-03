# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** ACTIVE SERIES HANDOFF — PRE-GAME 1 / FRESH LOCKED BENCHMARK / NO POSITIONS YET  
**Session lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Series state

- KT Rolster vs Dplus KIA
- LCK 2026 Season Playoffs — Lower Bracket Round 2
- Bo5 Fearless Draft
- scheduled `2026-09-04 08:00 UTC / 15:00 UTC+7`
- no map in this series has started at handoff creation
- no KT-DK canonical Position exists yet
- Airtable untouched for this series until a locked map ends

## 2. Fresh frozen benchmark

Completed Gol.gg regular competitive windows only; no sportsbook price or prior playoff result in benchmark metrics.

Roster continuity:
- DK normal 70/30 current/previous
- KT one material starter change (Rounds 1-2 Aiming -> current Jiwoo), so 85/15 current/previous

Split scores:
- `B_current(DK)=+0.174447`
- `B_current(KT)=-1.458375`
- `B_previous(DK)=+0.412956`
- `B_previous(KT)=+0.503116`

Roster-adjusted raw blend:
- `B_raw(DK)=+0.246000`
- `B_raw(KT)=-1.164151`

Full peer-set re-standardization:
- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`

Frozen prior:
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_KT=21;B_CUR_DK=0.174447;B_CUR_KT=-1.458375;B_PREV_DK=0.412956;B_PREV_KT=0.503116;BLEND_DK=0.246000;BLEND_KT=-1.164151;B_DK=0.355702;B_KT=-1.465479;GAP_DK_KT=1.821180;K_DK=+2;K_KT=-2;ROSTER_ADJ_DK=NORMAL70_30;ROSTER_ADJ_KT=ONE_STARTER_85_15;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`

## 3. Frozen Total Kills baseline

Current Rounds 3-4 environments:
- DK `12.9 KPG + 13.0 DPG = 25.9`
- KT `12.0 KPG + 13.0 DPG = 25.0`

`TK0=25.45`.

## 4. Expected roster context

KT:
- Perfect TOP
- Cuzz JUNGLE
- Bdd MID
- Jiwoo ADC
- Effort SUPPORT

DK:
- Siwoo TOP
- Lucid JUNGLE
- ShowMaker MID
- Smash ADC
- Career SUPPORT

User-supplied final map roles override this context.

## 5. Q2 forced-choice controls

Exactly one canonical position per executable family after final draft + exact board:
- Moneyline
- Kill Handicap
- Duration
- Total Kills

Stake/exposure:
- `0.25u shadow` each
- `0u actual`
- 1.00u shadow total per fully executable map

Mandatory price-blind order:
1. full DIM;
2. ML P0 lock;
3. full signed KH margin distribution;
4. Duration `V/Q/H/T/F`;
5. full TK bins;
6. only then read price for model-vs-book selection.

Q2 quarantine:
- `D_DIAGNOSTIC_ONLY=YES`
- `D_PROBABILITY_CONTRIBUTION=0`
- forced-choice ML probability = `P0` only
- `KH_MODEL_PROB_CAP=70%` for execution-edge reporting/comparison; persist raw cover too
- KH bins must include numeric `10+` kill tails for both teams
- `<5` KH must align with selected ML; `±5.5+` may be independent
- Duration formula frozen; selected Over gets `OVER_BRANCH_WARNING=YES`
- TK bins require explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch
- `MODEL_EDGE` + `FORCED_NEG_EV=YES/NO` on every selected side
- ignore all displayed in-map state for prediction
- Airtable only at map end

## 6. Cohort state

Entering this series:
- `40 Positions / 10 per family`
- `17W-23L`
- `-2.0755u` shadow
- `0u actual`

Family state:
- ML `1-9 / -2.0805u`
- KH `4-6 / -0.6225u`
- Duration `7-3 / +0.7770u`
- TK `5-5 / -0.1495u`

Next preferred structural checkpoint:
- `80 total / 20 per family`
- 10 more fully recorded maps / 40 positions

## 7. Game 1 readiness

No Game 1 draft or market board is locked yet.

When final G1 roles + exact board arrive, return verdict first and fast:
`G1: ML / KH / Duration / Total Kills — 1.00u shadow total.`

Then only the shortest necessary DIM, raw/capped probabilities, and edge/forced-Neg-EV notes.
