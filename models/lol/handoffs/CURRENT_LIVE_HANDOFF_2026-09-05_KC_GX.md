# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — G1/G2/G3 SETTLED / KC LEADS 2-1 / GAME 4 POSITIONS LOCKED  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

- G1 final: **KC won 12-8 in 40:40**.
- G2 final: **GX won 22-12 in 37:42**.
- G3 final: **KC won 14-1 in 26:27**.
- Series score entering G4: **KC 2-1 GX**.
- G1/G2/G3 map records and all 12 canonical positions are written to Airtable.
- Same-series results do not update frozen `K/P0/TK0`; prior maps may inform only Fearless champion availability.
- User-directed ML floor remains active as last explicitly stated: selected Moneyline must be `>=1.45`.
- G4 final draft + exact board were supplied prospectively; four canonical positions are locked below.
- Airtable remains untouched for G4 until the map ends.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Cohort entering Game 4

- `76 Positions / 19 per family`
- overall `38W-38L / -0.98225u`
- ML `5-14 / -2.19150u`
- KH `10-9 / -0.06200u`
- Duration `13-6 / +1.33650u`
- TK `10-9 / -0.06525u`
- actual exposure `0u`

G4 settlement reaches the planned `80 positions / 20 per family` structural checkpoint.

## Game 4 final draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

KC blue: `Rumble / Pantheon / Sylas / Varus / Vel'Koz`  
GX red: `Ornn / Xin Zhao / Syndra / Kalista / Renata Glasc`

## Game 4 source-truth board

- ML: KC `1.299` / GX `3.327`
- Duration `32.0`: Over `1.978` / Under `1.771`
- Total Kills `25.5`: Over `1.939` / Under `1.787`
- KH: KC `-8.5 @1.864` / GX `+8.5 @1.874`

Displayed live-state labels are ignored for prediction under postdraft-only mode.

## Game 4 price-blind DIM

KC mechanisms:
- PKM: Pantheon deterministic access -> Sylas follow-through -> Rumble Equalizer and Varus/Vel'Koz ranged conversion.
- SKM: Varus + Vel'Koz poke with Rumble objective-zone control can win space before Pantheon/Sylas commit, giving KC a distinct ranged setup route.

GX mechanisms:
- PKM: Ornn or Syndra first control -> Xin Zhao/Kalista collapse, with Renata extending or reversing the exchange.
- SKM: Ornn/Xin front line plus Syndra zone and Renata anti-dive can absorb KC's first entry and turn a denied engage into a counter-engage/front-to-back win.

DIM rows:
- TAM: GX slight — Ornn/Xin/Renata provide stronger denial and reset against KC's forward commit.
- OSG: KC advantage — Rumble/Varus/Vel'Koz offer superior long-range choke control and pre-fight damage.
- DAU: KC slight — Pantheon gives cleaner deterministic first access, though GX has multiple counter-starts.
- SLI: even — neither composition owns a robust independent split-push route.
- FNF: GX advantage — Ornn/Xin front line plus Renata/Kalista/Syndra is more stable in straight front-to-back fights.
- CAS: mixed — KC can cascade from a successful Pantheon/Rumble opening; GX can cascade from Renata/Ornn counter-engage.
- ETS: KC benchmark advantage remains contextual only.
- AFP: both sides retain two independent mechanisms after adversarial denial; no side clears the full certification threshold.

Diagnostic result: `D=0 / EVEN-STYLE-DEPENDENT`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 4 locked forced-choice card

### Moneyline
Frozen Q2 probabilities: KC `60%` / GX `40%`.

- KC @1.299 -> implied `76.98%` -> raw model edge `-16.98pp`; additionally execution-ineligible under ML floor `<1.45`.
- GX @3.327 -> implied `30.06%` -> `MODEL_EDGE=+9.94pp`.

GX is selected because the frozen model still prices it above the market implied probability, not merely because KC is below the floor.

Canonical ML: **GX ML @3.327**  
`ML_PRICE_FLOOR=1.45`  
`FORCED_NEG_EV=NO`

### Kill Handicap
Absolute line is `8.5`, so KH may be evaluated independently of ML.

Pre-price signed margin bins:
- KC wins by 10+: `27%`
- KC wins by exactly 9: `5%`
- KC wins by 5-8: `14%`
- KC wins by 1-4: `14%`
- GX wins by 1-4: `15%`
- GX wins by 5-8: `11%`
- GX wins by exactly 9: `4%`
- GX wins by 10+: `10%`

Total KC win mass = `60%`; GX win mass = `40%`.  
GX +8.5 raw cover = `68%`; below the Q2 70% execution cap.  
GX +8.5 @1.874 -> implied `53.36%` -> `MODEL_EDGE=+14.64pp`.

Canonical KH: **GX +8.5 @1.874**  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=+1` — both sides have direct initiation and explosive conversion once contact is created.
- `Q=+1` — KC's Rumble/Varus/Vel'Koz zone and GX's Ornn/Syndra/Renata objective control can force additional setup cycles rather than automatic first-contact endings.
- `H=+1` — Renata reset/counter-engage plus Ornn durability gives GX a credible non-terminal fight branch; KC can also disengage through range after partial contact.
- `T=+1` — Ornn scaling and strong late front-to-back structure preserve extension risk despite KC's midgame acceleration.
- `F=32.25m`.

At line 32.0:
- Over model `51.75%`
- Over @1.978 implied `50.56%`
- `MODEL_EDGE=+1.19pp`

Canonical Duration: **Over 32 @1.978**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=YES`

Note: the initial flash verdict said Under 32 before the full V/Q/H/T pass was completed. The completed price-blind duration audit supersedes that flash line; **Over 32 is the only canonical Duration position**.

### Total Kills
Frozen `TK0=28.50`.

Price-blind bins:
- `<20`: `9%`
- `20-25`: `26%`
- `26-30`: `27%`
- `31-35`: `21%`
- `36-40`: `11%`
- `41+`: `6%`

Over 25.5 model = `65%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `22%` of scenario mass, concentrated at 25 or fewer kills. The Over branch remains larger because both drafts contain deterministic engage/counter-engage and multiple damage sources that can create return kills and repeated objective fights.

Over 25.5 @1.939 -> implied `51.57%` -> `MODEL_EDGE=+13.43pp`.

Canonical TK: **Over 25.5 @1.939**  
`FORCED_NEG_EV=NO`

## Game 4 execution lock

1. **GX ML @3.327** — `0.25u shadow`
2. **GX +8.5 @1.874** — `0.25u shadow`
3. **Over 32 @1.978** — `0.25u shadow`
4. **Over 25.5 @1.939** — `0.25u shadow`

Total G4: `1.00u shadow / 0u actual`.

Do not update predictions from displayed live score/state. Await final G4 result, then write G4 map + four canonical positions to Airtable. G4 settlement reaches the 80-position checkpoint and must trigger the checkpoint audit before any new structural overlay change.