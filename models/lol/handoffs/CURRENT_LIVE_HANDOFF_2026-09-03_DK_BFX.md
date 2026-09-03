# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** ACTIVE SERIES HANDOFF — GAME 3 PREP READY / NO NEW POSITION RECORDED YET UNDER THIS LOCK  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Lock persistence commit:** `4d28d7665092b5e43afafa0af99d4f1e13c5d279`

## 1. Current series

- Dplus KIA (DK) vs BNK FearX (BFX)
- LCK 2026 Season Playoffs
- Lower Bracket Round 1
- 2026-09-03
- Bo5 Fearless Draft
- Games 1 and 2 are complete; Game 3 is the next eligible map for this chat workflow.

The session lock was established after the scheduled series start. Same-series outcomes are quarantined from the benchmark and must not update K/P0.

Neither Game 1 nor Game 2 had a final draft + exact board supplied to this chat for forced-choice execution. Therefore no retroactive Position may be created for either map and Airtable remains untouched for them in this workflow.

## 2. Frozen pre-series benchmark

Final benchmark remains unchanged:
- `B(DK)=+0.334587`
- `B(BFX)=+0.010432`
- `GAP(DK-BFX)=+0.324155 SD`
- `DK K=0 / P0=50%`
- `BFX K=0 / P0=50%`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`

Same-series results may be used only where structurally required by Fearless Draft champion availability, never as strength or probability evidence.

## 3. Expected roster context

DK: Siwoo / Lucid / ShowMaker / Smash / Career.  
BFX: Clear / Raptor / VicLa / Taeyoon / Kellin.

Final user-supplied Game 3 draft/roles override public roster context if different.

## 4. Execution mode

Standing mode is `POSTDRAFT-ONLY / FORCED-CHOICE`:
- inputs: frozen benchmark + final Game 3 draft/mechanisms + supplied Game 3 board;
- ignore displayed match clock and all in-map kills/gold/objectives/structures;
- families: Moneyline / Kill Handicap / Duration / Total Kills;
- exactly one canonical Position per executable family;
- alternate lines may be evaluated but only one canonical line per family is selected;
- PASS disabled for executable binary markets;
- if both sides are negative EV, select the less-negative side;
- tag every selection `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO`;
- `0.25u shadow per family / 0u actual`;
- no chase/rescue/martingale/averaging down/stake escalation.

Kill Handicap portfolio rule:
- absolute handicap below 5 kills: KH team must align with selected ML team;
- `±5.5` or wider: KH may be independent.

## 5. Game 3 post-audit DIM discipline

Before the Game 3 verdict:
1. resolve exact roles;
2. complete `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP`;
3. certify `D=+1/-1` only if at least two independent mechanism advantages survive adversarial failure-path review;
4. otherwise use `D=0 / EVEN-STYLE-DEPENDENT`;
5. KH: full signed final kill-margin distribution summing to 100% before price;
6. Duration: lock `V/Q/H/T` and `F` before line/price;
7. Total Kills: full kill-total distribution summing to 100% before price;
8. no structural coefficient change before the 40-position checkpoint unless an implementation bug is identified.

## 6. Family baselines for Game 3

Moneyline:
`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)`, with both teams starting from `50%`.

Kill Handicap:
full signed margin distribution before line/price, then apply the portfolio-coherence rule.

Duration:
use v1.1 draft-only core at `t=0`; lock `F` before line/price.

Total Kills:
- BFX current-window environment `30.9`;
- DK current-window environment `25.9`;
- frozen `TK0=28.4 kills`.

## 7. Forced-choice cohort entering Game 3

Because G1-G2 were not recorded in this workflow, cohort state is unchanged:
- `28 canonical Positions / 7 per family`;
- `13W-15L`;
- shadow P/L `-0.9980u`;
- actual exposure `0u`.

By family:
- ML `1-6 / -1.3305u`;
- KH `3-4 / -0.3475u`;
- Duration `4-3 / +0.0795u`;
- Total Kills `5-2 / +0.6005u`.

Next checkpoint remains:
- `40 positions / 10 per family`;
- `3 fully recorded maps / 12 positions` needed.

## 8. Game 3 workflow

When the user supplies the final Game 3 draft + exact board:
1. lock the full price-blind DIM and all four family projections;
2. first user-visible line immediately: `G3: ML / KH / Duration / Total Kills — 1.00u shadow.`;
3. follow with only concise mechanism/probability/distribution notes and `MODEL_EDGE` / `FORCED_NEG_EV`;
4. do not delay the verdict for persistence;
5. Airtable write only at Game 3 end, settling the map and four canonical Positions together;
6. run the full micro-audit and update the cohort afterward.

No Game 3 Position exists until a final Game 3 draft + exact board is supplied.