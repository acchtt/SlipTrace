# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 1 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.
- G1 final draft + exact board were supplied prospectively; four canonical positions are locked.
- The user explicitly added a prospective Moneyline price floor: selected ML must be `>=1.45`; sub-1.45 ML is not worth taking and is execution-ineligible.
- Same-series results do not update `K/P0/TK0`; prior maps may inform only Fearless champion availability where structurally needed.
- Airtable remains untouched until G1 ends.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Game 1 final draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

KC blue: `Jayce / Jarvan IV / Anivia / Ashe / Seraphine`  
GX red: `Yorick / Skarner / Cassiopeia / Lucian / Milio`

## Game 1 source-truth board

- ML: KC `1.272` / GX `3.522`
- Duration `32.0`: Over `1.904` / Under `1.835`
- Total Kills `25.5`: Over `1.869` / Under `1.851`
- KH: KC `-8.5 @1.869` / GX `+8.5 @1.868`

Displayed live-state labels are ignored for prediction under postdraft-only mode.

## Game 1 price-blind DIM

KC mechanisms:
- PKM: Ashe arrow / Jarvan IV hard access -> Anivia wall-zone + Seraphine follow-up -> Jayce ranged damage and chase.
- SKM: Jayce/Anivia/Ashe/Seraphine ranged choke control can win space without immediate all-in, then Jarvan converts a displaced or slowed target.

GX mechanisms:
- PKM: Skarner displacement -> Cassiopeia control/DPS -> Lucian follow-up, with Milio extending range and stabilizing the first exchange.
- SKM: Yorick side-lane pressure forces rotation while Cassiopeia/Lucian/Milio/Skarner hold a defensible four-man shell and punish over-commitment.

DIM rows:
- TAM: mixed. KC has multiple catch layers, while GX has Skarner disruption, Cassiopeia anti-dash/zone control, and Milio reset tools.
- OSG: KC advantage from Jayce poke, Anivia wall/zone, Ashe arrow and Seraphine range in objective chokes.
- DAU: mixed. KC can start from long range, but GX's Skarner/Cassiopeia/Milio core is unusually good at punishing forced forward entry.
- SLI: GX advantage through Yorick side pressure; this is a genuinely separate macro route from GX's grouped anti-engage plan.
- FNF: GX slight in stable front-to-back occupancy through Skarner plus Cassiopeia, though KC can compensate with range and zone rather than a classic tank.
- CAS: mixed. KC can cascade from a successful arrow/Jarvan catch; GX can cascade from a denied engage into Yorick structure pressure or Skarner re-engage.
- ETS: KC benchmark advantage, used only as execution-confidence context and not to set D mechanically.
- AFP: both sides retain two independent mechanisms after adversarial denial; neither side clears the threshold for a certified draft-direction edge.

Diagnostic result: `D=0 / EVEN-STYLE-DEPENDENT`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 1 locked forced-choice card

### Moneyline
Frozen Q2 probabilities: KC `60%` / GX `40%`.

- KC @1.272 -> implied `78.62%` -> raw model edge `-18.62pp`; additionally **execution-ineligible** under user-directed ML floor `<1.45`.
- GX @3.522 -> implied `28.39%` -> `MODEL_EDGE=+11.61pp`.

Canonical ML: **GX ML @3.522**  
`ML_PRICE_FLOOR=1.45`  
`FORCED_NEG_EV=NO`

### Kill Handicap
Absolute line is `8.5`, so KH may be evaluated independently of ML.

Pre-price signed margin bins:
- KC wins by 10+: `24%`
- KC wins by exactly 9: `5%`
- KC wins by 5-8: `15%`
- KC wins by 1-4: `16%`
- GX wins by 1-4: `16%`
- GX wins by 5-8: `10%`
- GX wins by exactly 9: `4%`
- GX wins by 10+: `10%`

Total KC win mass = `60%`; GX win mass = `40%`, consistent with frozen P0.  
GX +8.5 raw cover = `71%`; Q2 capped execution probability = `70%`.  
GX +8.5 @1.868 -> implied `53.53%` -> `MODEL_EDGE=+16.47pp`.

Canonical KH: **GX +8.5 @1.868**  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=0` — both sides have initiation and conversion tools, but strong anti-engage/zone packages prevent clean acceleration credit.
- `Q=+1` — Anivia/Cassiopeia zone control and Yorick side pressure can force extra setup/rotation cycles around objectives.
- `H=+1` — both teams possess credible non-terminal reset/stall routes after a failed first conversion.
- `T=+1` — scaling control, side pressure and defensive spacing remain live rather than forcing an early terminal path.
- `F=33.75m`.

At line 32.0:
- Over model `62.25%`
- Over @1.904 implied `52.52%`
- `MODEL_EDGE=+9.73pp`

Canonical Duration: **Over 32 @1.904**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=YES`

### Total Kills
Frozen `TK0=28.50`.

Price-blind bins:
- `<20`: `8%`
- `20-24`: `15%`
- exactly `25`: `13%`
- `26-30`: `29%`
- `31-35`: `20%`
- `36+`: `15%`

Over 25.5 model = `64%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `18%` of scenario mass, concentrated at 25 or fewer kills. The upper branch remains larger because both comps have repeatable catch/re-engage plus enough defensive counterplay to create return kills rather than only clean one-way fights.

Over 25.5 @1.869 -> implied `53.50%` -> `MODEL_EDGE=+10.50pp`.

Canonical TK: **Over 25.5 @1.869**  
`FORCED_NEG_EV=NO`

## Game 1 execution lock

1. **GX ML @3.522** — `0.25u shadow`
2. **GX +8.5 @1.868** — `0.25u shadow`
3. **Over 32 @1.904** — `0.25u shadow`
4. **Over 25.5 @1.869** — `0.25u shadow`

Total: `1.00u shadow / 0u actual`.

Do not update predictions from displayed live score/state. Await final G1 result, then write map + four canonical positions to Airtable and run map micro-audit.

## Cohort entering Game 1

- `64 Positions / 16 per family`
- `33W-31L / -0.64300u`
- ML `4-12 / -2.26775u`
- KH `8-8 / -0.23675u`
- Duration `12-4 / +1.61050u`
- TK `9-7 / +0.25100u`
- actual exposure `0u`

Preferred next checkpoint remains `80 total / 20 per family`.