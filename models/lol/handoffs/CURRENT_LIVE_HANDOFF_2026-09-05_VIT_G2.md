# Current Live Handoff — Team Vitality vs G2 Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 3 TARGET / NO POSITIONS YET  
**Session lock:** `LOL-2026-09-05-V13-LEC-VIT-G2-DRAFTONLY-FORCEDCHOICE-Q2-1903-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Team Vitality vs G2 Esports — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.
- User explicitly requested the current match be locked for **Game 3**.
- G1/G2 occurred before this lock and are same-series history only; do not create retroactive positions.
- Same-series results do not update `K/P0/TK0`; prior maps may inform only Fearless champion availability where structurally needed.
- Await final G3 draft/roles + exact sportsbook board before any Position.
- Airtable untouched for this series so far.

## Frozen benchmark

Fresh pre-series Gol.gg construction from completed LEC 2026 Summer regular season + LEC 2026 Spring regular season, excluding current playoff maps and sportsbook price:
- `B(G2)=+1.000135`
- `B(VIT)=+0.917530`
- `GAP(G2-VIT)=+0.082605 SD`
- `G2 K=0 / P0=50%`
- `VIT K=0 / P0=50%`
- `TK0=29.25`

Roster continuity:
- G2 normal `70/30` Summer/Spring;
- VIT `85/15` because FIESTA replaced Humanoid at MID.

## Q2 execution controls

- Exactly one canonical selection per family: ML / KH / Duration / TK.
- `0.25u shadow` each / `0u actual`.
- ML uses frozen `P0` only; full DIM persists but `D_DIAGNOSTIC_ONLY=YES` and `D_PROBABILITY_CONTRIBUTION=0`.
- KH: full signed margin bins, both 10+ tails, execution probability capped at 70%; `<5` line must align with ML; `±5.5+` may diverge.
- Duration: frozen 31m-anchor formula, persist `V/Q/H/T/F`; selected Over gets `OVER_BRANCH_WARNING=YES`.
- TK: persist full bins and explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` mass.
- Price is not causal evidence; if both binary sides are negative EV choose the less-negative side and tag it.
- Airtable write only at map end.

## Cohort entering VIT-G2

- `60 Positions / 15 per family`
- `31W-29L / -0.53825u`
- ML `4-11 / -2.01775u`
- KH `7-8 / -0.45225u`
- Duration `11-4 / +1.43075u`
- TK `9-6 / +0.50100u`
- actual exposure `0u`

Preferred next checkpoint: `80 total Positions / 20 per family` — 5 more fully recorded maps.

## Game 3 workflow

1. Receive final G3 draft in role order TOP/JG/MID/ADC/SUP plus exact board.
2. Complete full price-blind DIM and all four family projections.
3. Select exactly one ML/KH/Duration/TK side.
4. User-visible verdict first and fast.
5. Do not use displayed live state for prediction.
6. Settle and write Airtable only after final map result.
