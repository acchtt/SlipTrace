# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 4 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- G1 had no prospective canonical Position in this chat; no retroactive G1 Positions.
- G2 settled: GEN won `34-27` in `45:43`; card `1-3 / -0.4935u`; Airtable written.
- G3 settled: GEN won `26-9` in `31:20`; card `2-2 / -0.09675u`; Airtable written.
- Entering G4, visible series score is GEN `2-1` HLE.
- G4 final draft + exact board were supplied prospectively; four canonical forced-choice Positions are locked.
- Same-series results do not update `K/P0/TK0`; only Fearless champion availability may carry forward.
- No Airtable write until G4 ends.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`

## Game 4 draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

GEN blue: `Varus / Vi / Vex / Miss Fortune / Neeko`  
HLE red: `Nasus / Naafiri / Sylas / Kalista / Renata Glasc`

## Game 4 source-truth board

- ML: GEN `1.786` / HLE `1.959`
- Duration `32.0`: Over `1.903` / Under `1.836`
- Total Kills `30.5`: Over `1.816` / Under `1.925`
- KH: GEN `-3.5 @1.861` / HLE `+3.5 @1.876`

Displayed in-map clock/state is ignored for prediction under postdraft-only mode.

## Game 4 price-blind DIM

GEN mechanisms:
- PKM: Vi point-and-click access -> Vex/Neeko layered control -> Miss Fortune channel, with Varus adding ranged lock/poke before or after contact.
- SKM: Varus/Vex/Neeko catch from range or fog -> Vi follow-through -> MF zone/cleanup; GEN can create contact without relying on one exact flank.

HLE mechanisms:
- PKM: Naafiri/Sylas dive and collapse onto a marked carry -> Kalista continuation, with Renata bailout/turn support and Nasus front pressure.
- SKM: Nasus side pressure / Wither-based front disruption -> forced rotations -> Naafiri/Sylas collapse while Kalista/Renata hold the four-man unit.

DIM rows:
- TAM: GEN advantage. Vex fear directly punishes Naafiri/Sylas dash commitment; Vi/Neeko provide reliable counter-lock, while HLE Renata can answer one committed GEN engage but cannot generically stop GEN's ranged catch plus follow-up.
- OSG: GEN advantage from Varus range, Neeko fog threat, Vi target access and MF choke punishment.
- DAU: GEN advantage; HLE's melee-heavy access must cross Vex/Varus/Neeko zones before Kalista can freely sustain damage.
- SLI: HLE slight theoretical Nasus route, but not certified independent because GEN has ranged pressure plus Vi/Neeko rotation catch and HLE's four-man unit can be forced.
- FNF: GEN does not need a classic tank because Vi creates deterministic first contact and the rest of the draft damages from controlled range/chokes. HLE's shorter-range melee stack has the higher access burden.
- CAS: GEN advantage; after an ordinary won contact, Vi/Neeko/Vex catch plus MF/Varus zone can make the next entry materially harder for HLE.
- ETS: benchmark modestly favors GEN; used only as execution-confidence context, not to set D mechanically.
- AFP: HLE's Renata turn can deny the first GEN all-in, but GEN retains a distinct ranged catch/zone route. HLE's alternative side route is not sufficiently independent against GEN rotation catch.

Diagnostic result: `D=+1 GEN`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 4 locked forced-choice card

### Moneyline
Q2 frozen probabilities: GEN `55%` / HLE `45%`.

- GEN @1.786 -> implied `55.99%` -> `MODEL_EDGE=-0.99pp`
- HLE @1.959 -> implied `51.05%` -> edge `-6.05pp`

Canonical ML: **GEN ML @1.786**  
`FORCED_NEG_EV=YES`

### Kill Handicap
Absolute line is `<5`, therefore KH must align with selected GEN ML.

Pre-price signed margin bins:
- GEN wins by 10+: `20%`
- GEN wins by 5-9: `19%`
- GEN wins by exactly 4: `5%`
- GEN wins by 1-3: `11%`
- HLE wins by 1-3: `16%`
- HLE wins by 4-9: `18%`
- HLE wins by 10+: `11%`

Total GEN win mass = `55%`, consistent with frozen ML P0.  
GEN -3.5 raw cover = `44%`; capped execution probability = `44%`.  
GEN -3.5 @1.861 -> implied `53.73%` -> `MODEL_EDGE=-9.73pp`.

Canonical KH: **GEN -3.5 @1.861**  
`FORCED_NEG_EV=YES`  
Selection is forced by the user-directed `<5 => ML-aligned` portfolio rule.

### Duration
Draft-only scores:
- `V=+1` — both sides possess decisive commit tools; GEN in particular has a short pick-to-wombo conversion path.
- `Q=0` — no reliable pre-map compulsory spacing edge.
- `H=0` — ordinary terminal path depth.
- `T=0` — HLE Renata/Nasus/Sylas can extend failed commits, offsetting further acceleration credit.
- `F=29.50m`.

At line 32.0:
- Under model `67.50%`
- Under @1.836 implied `54.47%`
- `MODEL_EDGE=+13.03pp`

Canonical Duration: **Under 32 @1.836**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=NO`

### Total Kills
Frozen `TK0=26.95`.

Price-blind bins:
- `<20`: `5%`
- `20-24`: `10%`
- `25-30`: `27%`
- `31-35`: `29%`
- `36-40`: `18%`
- `41+`: `11%`

Over 30.5 model = `58%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `17%` of scenario mass, concentrated below 31 kills. The upper branch remains large because both drafts have repeatable dive/catch and continuation rather than clean disengage.

Over 30.5 @1.816 -> implied `55.07%` -> `MODEL_EDGE=+2.93pp`.

Canonical TK: **Over 30.5 @1.816**  
`FORCED_NEG_EV=NO`

## Game 4 execution lock

Four canonical Positions are prospectively locked from the supplied final draft + exact board:
1. **GEN ML @1.786** — `0.25u shadow`
2. **GEN -3.5 @1.861** — `0.25u shadow`
3. **Under 32 @1.836** — `0.25u shadow`
4. **Over 30.5 @1.816** — `0.25u shadow`

Total: `1.00u shadow / 0u actual`.

Do not update predictions from live score/state. Await final G4 result, then write map + four Positions to Airtable and run map micro-audit.

## Cohort entering G4

- `56 Positions / 14 per family`
- `27W-29L / -1.36300u`
- ML `3-11 / -2.21425u`
- KH `6-8 / -0.66750u`
- Duration `10-4 / +1.22175u`
- TK `8-6 / +0.29700u`
- actual exposure `0u`

Preferred next structural checkpoint remains `80 total / 20 per family`.
