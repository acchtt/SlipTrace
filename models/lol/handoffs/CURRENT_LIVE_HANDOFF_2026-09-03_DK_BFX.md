# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** ACTIVE SERIES HANDOFF — NO NEW POSITION RECORDED YET UNDER THIS LOCK  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Lock persistence commit:** `4d28d7665092b5e43afafa0af99d4f1e13c5d279`

## 1. Current series

- Dplus KIA (DK) vs BNK FearX (BFX)
- LCK 2026 Season Playoffs
- Lower Bracket Round 1
- 2026-09-03
- scheduled 08:00 UTC / 15:00 UTC+7
- Bo5 Fearless Draft

The series was identified fresh from Riot LoL Esports schedule plus Games of Legends / gol.gg playoff match list.

The session lock was established after the scheduled series start. Same-series score/map state is intentionally not imported into the prediction baseline. Do not create any retroactive Position for a map that started or completed before the lock existed.

## 2. Frozen pre-series benchmark

Source windows:
- current: completed `LCK 2026 Rounds 3-4`;
- previous: completed `LCK 2026 Rounds 1-2`;
- 10-team LCK peer set;
- normal 70/30 current/previous blend;
- sportsbook prices, playoff outcomes and today's DK-BFX results excluded.

Final benchmark:
- `B_current(DK)=+0.174447`
- `B_current(BFX)=+0.278708`
- `B_previous(DK)=+0.412956`
- `B_previous(BFX)=-0.624751`
- `B_raw(DK)=+0.246000`
- `B_raw(BFX)=+0.007670`
- `B(DK)=+0.334587`
- `B(BFX)=+0.010432`
- `GAP(DK-BFX)=+0.324155 SD`

Frozen prior:
- `DK K=0 / P0=50%`
- `BFX K=0 / P0=50%`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`

## 3. Expected roster context

DK:
- Siwoo TOP
- Lucid JUNGLE
- ShowMaker MID
- Smash ADC
- Career SUPPORT

BFX:
- Clear TOP
- Raptor JUNGLE
- VicLa MID
- Taeyoon ADC
- Kellin SUPPORT

Final user-supplied draft/roles override public roster context when different.

## 4. Execution mode

Standing mode is `POSTDRAFT-ONLY / FORCED-CHOICE`:
- prediction inputs: frozen benchmark + final draft/mechanisms + supplied board;
- ignore displayed match clock and all in-map kills/gold/objectives/structures;
- enabled families: Moneyline / Kill Handicap / Duration / Total Kills;
- exactly one canonical Position per executable family per map;
- evaluate alternate lines but select only one canonical line per family;
- PASS disabled for executable binary markets;
- if both sides are negative EV, select the less-negative side;
- tag every selection with `MODEL_EDGE` and `FORCED_NEG_EV=YES/NO`;
- 0.25u shadow per family / 0u actual;
- no chase/rescue/martingale/averaging down/stake escalation.

### Kill-handicap portfolio rule

- absolute handicap below 5 kills: selected KH team must align with selected ML team;
- `±5.5` or wider: KH may be independent;
- prospective only.

## 5. Post-audit DIM discipline

Before any map verdict:
1. resolve exact roles;
2. persist full DIM rows: `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP`;
3. certify `D=+1/-1` only if at least two independent mechanism advantages survive adversarial failure-path review;
4. otherwise use `D=0 / EVEN-STYLE-DEPENDENT`;
5. KH must have full signed final kill-margin bins summing to 100% before price;
6. Duration must lock `V/Q/H/T` and `F` before line/price;
7. Total Kills must have full kill-total bins summing to 100% before price;
8. no structural coefficient change before the 40-position checkpoint unless an implementation bug is found.

## 6. Family baselines

Moneyline:
`P(A)=clamp(P0(A)+4.5*D pp,15%,85%)` with both teams starting from P0 50%.

Kill Handicap:
full signed margin distribution required before line/price; apply portfolio rule after ML side selection.

Duration:
use v1.1 draft-only core at t=0; lock F before line/price.

Total Kills current-window environment:
- BFX: 16.1 KPG + 14.8 DPG = 30.9
- DK: 12.9 KPG + 13.0 DPG = 25.9
- frozen `TK0=28.4` kills

## 7. Forced-choice cohort entering DK-BFX

- `28 canonical Positions`
- `7 per family`
- `13W-15L`
- shadow P/L `-0.9980u`
- actual exposure `0u`

By family:
- ML `1-6 / -1.3305u`
- KH `3-4 / -0.3475u`
- Duration `4-3 / +0.0795u`
- Total Kills `5-2 / +0.6005u`

Next checkpoint:
- `40 positions / 10 per family`
- `3 more maps / 12 positions` needed.

## 8. Next-map workflow

When the user supplies a final DK-BFX draft + exact board:
1. immediately lock the full price-blind DIM and all family projections;
2. first user-visible line: `[Map]: ML / KH / Duration / Total Kills — 1.00u shadow.`;
3. then only concise mechanism/probability/distribution notes plus `MODEL_EDGE` and `FORCED_NEG_EV`;
4. do not delay the verdict for Airtable;
5. Airtable writes occur only at map end, when the map and all canonical Positions are settled together;
6. run the full micro-audit and update the cohort afterward.

No new Position exists under this handoff until a post-lock final draft + board is supplied.
