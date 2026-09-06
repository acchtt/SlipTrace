# Current Live Handoff — G2 Esports vs Karmine Corp — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — G1/G2 PROSPECTIVELY LOCKED / UNSETTLED  
**Session lock:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u EACH / 0u ACTUAL`

## Match

G2 Esports vs Karmine Corp — LEC 2026 Summer Playoffs Upper Bracket Final, Bo5 Fearless Draft.

Frozen pre-series benchmark remains unchanged:
- `B(G2)=+1.000135`
- `B(KC)=+1.625030`
- `GAP(KC-G2)=+0.624895 SD`
- `KC K=+1 / P0=55%`
- `G2 K=-1 / P0=45%`
- `TK0=30.15 kills`

Same-series outcomes do not update `B/K/P0/TK0`; prior maps may affect only Fearless champion availability. Draft `D` is diagnostic-only and contributes 0pp to ML probability.

## Game 1 — PROSPECTIVE / UNSETTLED

Draft:
- KC blue: Jayce / Vi / Ahri / Caitlyn / Bard
- G2: K'Sante / Xin Zhao / Viktor / Ezreal / Karma

Board:
- ML G2 `1.831` / KC `1.908`
- Duration 33: Over `1.923` / Under `1.817`
- Total Kills 27.5: Over `1.999` / Under `1.739`
- KH G2 -3.5 `1.915` / KC +3.5 `1.825`

Canonical card:
- `KC ML @1.908`
- `KC +3.5 @1.825`
- `Under 33 @1.817`
- `Under 27.5 @1.739`
- `0.25u each / 1.00u total shadow / 0u actual`

Diagnostic draft: `D=+1 KC`, `D_PROBABILITY_CONTRIBUTION=0`.

## Game 2 — PROSPECTIVE / UNSETTLED

Draft:
- G2 blue: Camille / Jarvan IV / Galio / Yunara / Lulu
- KC: Olaf / Lee Sin / Orianna / Lucian / Milio

Board:
- ML G2 `1.901` / KC `1.838`
- Duration 33: Over `2.007` / Under `1.748`
- Total Kills 27.5: Over `1.897` / Under `1.825`
- KH G2 -3.5 `1.906` / KC +3.5 `1.832`

Canonical card:
- `KC ML @1.838`
- `KC +3.5 @1.832`
- `Under 33 @1.748`
- `Over 27.5 @1.897`
- `0.25u each / 1.00u total shadow / 0u actual`

G2 draft mechanisms:
1. Jarvan IV + Galio primary force with Camille/Yunara follow-through.
2. Camille side assignment with Galio reinforcement creates a separate collapse route.

KC draft mechanisms:
1. Lee Sin/Orianna access into Lucian burst while Olaf disrupts the back line.
2. Lucian-Milio ranged pressure with Olaf side/front pressure.

Full DIM diagnostic resolves `D=+1 G2`; this is diagnostic only and adds `0pp` to ML probability.

G2 signed margin bins used for KH, expressed from G2 perspective:
- G2 by 10+: `13%`
- G2 by 4-9: `18%`
- G2 by 1-3: `14%`
- KC by 1-3: `15%`
- KC by 4-9: `19%`
- KC by 10+: `21%`

Thus KC +3.5 raw cover = `69%`, below the Q3 70% cap. Explicit 10+ clean-cascade tails: G2 `13%`, KC `21%`.

Duration pre-price state:
`V=0 / Q=0 / H=0 / T=-1 / F=30.25m`.
At line 33: Under model `69.25%`.

TK pre-price bins:
- `<20`: `8%`
- `20-24`: `11%`
- `25-27`: `16%`
- `28-32`: `27%`
- `33-37`: `21%`
- `38+`: `17%`

Over 27.5 model = `65%`.
Suppression scenario masses persisted separately:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 17%`
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY = 8%`

Price comparison:
- KC ML model `55%` vs implied `54.41%` => `+0.59pp`, `FORCED_NEG_EV=NO`
- KC +3.5 model `69%` vs implied `54.59%` => `+14.41pp`
- Under 33 model `69.25%` vs implied `57.21%` => `+12.04pp`
- Over 27.5 model `65%` vs implied `52.71%` => `+12.29pp`

## Cohort entering G2-KC

- `96 settled positions / 24 per family / 24 settled maps`
- overall `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

No G2-KC Airtable write occurs until explicit map-end final evidence. G1 and G2 remain unsettled.

## Next action

**AWAIT EXPLICIT G1/G2 FINAL EVIDENCE OR NEXT FULLY SUPPLIED MAP DRAFT + BOARD.**