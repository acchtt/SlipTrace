# Current Live Handoff — Team Vitality vs G2 Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 3 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-LEC-VIT-G2-DRAFTONLY-FORCEDCHOICE-Q2-1903-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Team Vitality vs G2 Esports — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.
- G1/G2 occurred before this lock and remain same-series history only; no retroactive positions.
- G3 final draft + exact board were supplied prospectively; four canonical positions are locked.
- Same-series results do not update `K/P0/TK0`; prior maps may inform only Fearless champion availability where structurally needed.
- Airtable remains untouched until G3 ends.

## Frozen benchmark

- `B(G2)=+1.000135`
- `B(VIT)=+0.917530`
- `GAP(G2-VIT)=+0.082605 SD`
- `G2 K=0 / P0=50%`
- `VIT K=0 / P0=50%`
- `TK0=29.25`

## Game 3 final draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

G2 blue: `Olaf / Pantheon / LeBlanc / Xayah / Rakan`  
VIT red: `Trundle / Cho'Gath / Hwei / Lucian / Milio`

## Game 3 source-truth board

- ML: G2 `1.446` / VIT `2.640`
- Duration `33.0`: Over `2.047` / Under `1.719`
- Total Kills `26.5`: Over `1.832` / Under `1.889`
- KH: G2 `-6.5 @1.876` / VIT `+6.5 @1.862`

## Game 3 price-blind DIM

G2 mechanisms:
- PKM: Pantheon point-and-click/global access -> LeBlanc/Rakan collapse -> Xayah follow-up, with Olaf running through disrupted front lines.
- SKM: Olaf side pressure and Pantheon semi-global reinforcement create side-to-center collapse while LeBlanc/Rakan threaten fog picks.

VIT mechanisms:
- PKM: Trundle pillar / Cho'Gath knock-up-silence / Hwei control layers stop or isolate first contact -> Lucian damage -> Milio reset and spacing.
- SKM: double-frontline objective/choke occupation with Hwei ranged zone and Milio range support lets VIT deny G2's preferred entry before turning onto the committing diver.

DIM rows:
- TAM: VIT advantage; Cho/Hwei/Milio provide multiple independent answers to Pantheon/Rakan/Olaf/LeBlanc commitment.
- OSG: VIT slight; pillar + Cho/Hwei zone + Milio range support make choke entry costly.
- DAU: mixed; G2 has excellent target access but VIT has stronger layered denial and sustained front-to-back structure.
- SLI: G2 slight theoretical Olaf/Pantheon side-collapse route, but VIT can answer rotations with Trundle/Cho front occupation and Hwei wave control.
- FNF: VIT advantage from reliable double-frontline occupancy; G2 relies more on successful first contact.
- CAS: mixed; G2 can cascade rapidly from one pick, while VIT can convert denied engage into objective control.
- ETS: effectively even from the frozen benchmark.
- AFP: VIT retains two distinct surviving routes after adversarial denial — anti-dive front-to-back and ranged objective/choke control — while G2's routes more often require successful forward commitment.

Diagnostic result: `D=+1 VIT`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 3 locked forced-choice card

### Moneyline
Frozen Q2 probabilities: G2 `50%` / VIT `50%`.

- G2 @1.446 -> implied `69.16%` -> edge `-19.16pp`
- VIT @2.640 -> implied `37.88%` -> edge `+12.12pp`

Canonical ML: **VIT ML @2.640**  
`MODEL_EDGE=+12.12pp`  
`FORCED_NEG_EV=NO`

### Kill Handicap
Absolute line is `6.5`, so KH may be evaluated independently of ML under the portfolio rule.

Pre-price signed margin bins:
- G2 wins by 10+: `16%`
- G2 wins by 7-9: `8%`
- G2 wins by 1-6: `26%`
- VIT wins by 1-6: `25%`
- VIT wins by 7-9: `9%`
- VIT wins by 10+: `16%`

Each side retains `50%` win mass, consistent with frozen P0.  
VIT +6.5 raw cover = `76%`; Q2 capped execution probability = `70%`.  
VIT +6.5 @1.862 -> implied `53.71%` -> edge `+16.29pp`.

Canonical KH: **VIT +6.5 @1.862**  
`MODEL_EDGE=+16.29pp`  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=+1` — G2 has direct Pantheon/Rakan pick-to-fight acceleration and both sides can convert won contact quickly.
- `Q=0` — no reliable pre-map compulsory-cycle delay or acceleration edge.
- `H=0` — ordinary terminal-path depth.
- `T=+1` — VIT's Cho/Hwei/Milio reset/zone package can extend failed G2 commits and prevent immediate terminal conversion.
- `F=30.25m`.

At line 33.0:
- Under model `69.25%`
- Under @1.719 implied `58.17%`
- `MODEL_EDGE=+11.08pp`

Canonical Duration: **Under 33 @1.719**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=NO`

### Total Kills
Frozen `TK0=29.25`.

Price-blind bins:
- `<20`: `8%`
- `20-24`: `11%`
- `25-26`: `15%`
- `27-31`: `28%`
- `32-36`: `21%`
- `37+`: `17%`

Over 26.5 model = `66%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `17%` of scenario mass, concentrated below 27 kills. The upper branch remains substantial because G2 has repeatable dive/collapse while VIT has enough peel and return damage to generate two-sided contact rather than purely suppressing fights.

Over 26.5 @1.832 -> implied `54.59%` -> edge `+11.41pp`.

Canonical TK: **Over 26.5 @1.832**  
`FORCED_NEG_EV=NO`

## Game 3 execution lock

1. **VIT ML @2.640** — `0.25u shadow`
2. **VIT +6.5 @1.862** — `0.25u shadow`
3. **Under 33 @1.719** — `0.25u shadow`
4. **Over 26.5 @1.832** — `0.25u shadow`

Total: `1.00u shadow / 0u actual`.

Do not update predictions from displayed live state. Await final G3 result, then write map + four canonical Positions to Airtable and run map micro-audit.

## Cohort entering G3

- `60 Positions / 15 per family`
- `31W-29L / -0.53825u`
- ML `4-11 / -2.01775u`
- KH `7-8 / -0.45225u`
- Duration `11-4 / +1.43075u`
- TK `9-6 / +0.50100u`
- actual exposure `0u`

Preferred next checkpoint remains `80 total / 20 per family`.