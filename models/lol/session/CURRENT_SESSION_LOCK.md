# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-05-V13-LEC-VIT-G2-DRAFTONLY-FORCEDCHOICE-Q2-1903-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Round 1 — Team Vitality vs G2 Esports — Bo5 Fearless Draft`  
**Target map at activation:** `Game 3`  
**Supersedes:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7` (closed historical lock)  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q2`  
**Execution mode:** `POSTDRAFT-ONLY INPUTS / FORCE ONE SIDE PER OFFERED MARKET / IGNORE DISPLAYED LIVE STATE FOR PREDICTION`  
**Circuit breaker / actual exposure:** `CLEAR / 0u actual`  
**Default shadow stake:** `0.25u per family`

## Authority and overlay

Load `models/lol/CURRENT_MODEL.md` and the complete v1.3 stack from authority commit `6018e7706772554d6318c1af4a9548ca4f25cd95`. Canonical `CURRENT_MODEL.md` remains unchanged. This lock explicitly re-activates the experimental forced-choice Q2 overlay prospectively for this series.

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
- if both sides are negative EV, select the less-negative side and tag `FORCED_NEG_EV=YES`;
- Airtable writes occur only at map end;
- no retroactive position creation;
- no chasing, rescue, martingale, averaging down, or stake escalation.

### Q2 Moneyline quarantine
- full DIM remains mandatory: `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP`;
- persist `D=+1/0/-1` under the adversarial two-independent-mechanism rule;
- `D_DIAGNOSTIC_ONLY=YES`;
- `D_PROBABILITY_CONTRIBUTION=0`;
- forced-choice ML probability uses frozen `P0` only.

### Q2 Kill Handicap
- full signed margin bins before price;
- explicit numeric mass in both teams' 10+ kill tails;
- `KH_MODEL_PROB_CAP=70%` for execution edge reporting;
- absolute handicap `<5` kills => selected KH team must align with selected ML team;
- `±5.5` or wider may be independent.

### Q2 Duration
- v1.1 formula and `31.0m` anchor remain frozen;
- persist draft-only `V/Q/H/T/F` before price;
- selected Over => `OVER_BRANCH_WARNING=YES` diagnostically.

### Q2 Total Kills
- frozen series `TK0` below;
- persist full pre-price bins;
- explicitly persist numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch separately from clean-cascade/two-sided-brawl mass.

## Fresh series identification

Current LEC match at lock time resolves to:
- Team Vitality (`VIT`) vs G2 Esports (`G2`);
- LEC 2026 Summer Playoffs;
- Upper Bracket Round 1;
- Bo5 Fearless Draft;
- date `2026-09-05`;
- user-designated target map at activation: `Game 3`.

Public match pages list VIT vs G2 as the first Sep 5 LEC Summer Playoffs Bo5. G1/G2 are same-series history and are not benchmark inputs. No G1/G2 positions are created under this new lock.

## Expected current lineups

G2:
- BrokenBlade — TOP
- SkewMond — JUNGLE
- Caps — MID
- Hans Sama — ADC
- Labrov — SUPPORT

VIT:
- Naak Nako — TOP
- Lyncas — JUNGLE
- FIESTA — MID
- Carzzy — ADC
- Fleshy — SUPPORT

User-supplied final map roles/draft override saved context if contradictory.

## Fresh pre-series Gol.gg benchmark

Primary source: Games of Legends / gol.gg completed **LEC 2026 Summer Season** regular-season team table, with **LEC 2026 Spring Season** as the previous comparable split. Current-series playoff maps and sportsbook prices are excluded.

Formula per authority:
`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`.

Target-team current Summer inputs:
- G2: `21 games`, WinRate `66.7%`, GDM `+122`, GD@15 `+645`, Towers `8.1-5.0`, DRA% `50.9`, NASH% `71.4`;
- VIT: `22 games`, WinRate `63.6%`, GDM `+121`, GD@15 `+416`, Towers `7.1-4.7`, DRA% `62.5`, NASH% `72.7`.

Previous Spring inputs:
- G2: WinRate `71.4%`, GDM `+143`, GD@15 `+575`, Towers `8.2-4.6`, DRA% `54.0`, NASH% `77.5`;
- VIT: WinRate `70.8%`, GDM `+162`, GD@15 `+980`, Towers `7.7-5.0`, DRA% `57.0`, NASH% `61.5`.

League-relative split scores:
- `B_current(G2)=+0.838442`;
- `B_current(VIT)=+0.777186`;
- `B_previous(G2)=+1.099925`;
- `B_previous(VIT)=+1.202211`.

Roster continuity:
- G2 retains the same five from Spring to Summer => normal `70/30` current/previous;
- VIT changed MID from Humanoid to FIESTA => one material starter change => `85/15` current/previous.

Peer-set continuity adjustments used for final re-standardization:
- normal `70/30`: G2, KC, MKOI, NAVI;
- one-change `85/15`: FNC, SHFT, SK, TH, VIT;
- current-only due two material changes: GX.

Blended raw target scores:
- `B_raw(G2)=+0.916887`;
- `B_raw(VIT)=+0.840940`.

After re-standardizing the full 10-team blended LEC peer set:
- `B(G2)=+1.000135`;
- `B(VIT)=+0.917530`;
- `GAP(G2-VIT)=+0.082605 SD`.

Frozen strength prior:
- `G2 K=0 / P0=50%`;
- `VIT K=0 / P0=50%`.

Compact record:
`TEAM_BENCH[LEAGUE=LEC2026;CURRENT=SUMMER_SEASON;PREVIOUS=SPRING_SEASON;G_G2=21;G_VIT=22;B_CUR_G2=0.838442;B_CUR_VIT=0.777186;B_PREV_G2=1.099925;B_PREV_VIT=1.202211;BLEND_G2=0.916887;BLEND_VIT=0.840940;B_G2=1.000135;B_VIT=0.917530;GAP_G2_VIT=0.082605;K_G2=0;K_VIT=0;ROSTER_ADJ_G2=NORMAL70_30;ROSTER_ADJ_VIT=ONE_CHANGE85_15;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## Frozen Total Kills baseline

Current Summer regular-season total-kill environments:
- G2 = `16.5 kills/game + 13.0 deaths/game = 29.5`;
- VIT = `16.0 kills/game + 13.0 deaths/game = 29.0`.

Both samples exceed 15 games, so no previous-split TK blend is required.

`TK0=(29.5+29.0)/2=29.25 kills`.

## Same-series information boundary

- G1/G2 results do not update `K/P0/TK0`;
- current-series prices do not alter benchmark or price-blind projections;
- prior maps may matter only for structurally required Fearless champion availability;
- final G3 draft/roles + exact board are the only prediction inputs for the next forced-choice card;
- displayed G3 in-map clock/kills/gold/objectives are ignored for draft-only prediction.

## Cohort state entering this lock

Carried from closed GEN-HLE lock:
- `60 Positions / 15 per family`;
- overall `31W-29L / -0.53825u`;
- ML `4-11 / -2.01775u`;
- KH `7-8 / -0.45225u`;
- Duration `11-4 / +1.43075u`;
- TK `9-6 / +0.50100u`;
- actual exposure `0u`.

Preferred next structural checkpoint remains `80 total / 20 per family`, requiring `5` additional fully recorded maps / `20` positions.

## Game 3 readiness

No VIT-G2 G3 position exists yet. Await final G3 draft/roles + exact board. If either is missing: `HOLD — NEED FINAL DRAFT + EXACT BOARD`.
