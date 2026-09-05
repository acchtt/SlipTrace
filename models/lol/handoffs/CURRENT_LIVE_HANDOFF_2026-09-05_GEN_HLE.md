# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 3 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- G1 had no prospective canonical Position in this chat; no retroactive G1 Positions.
- G2 settled: GEN won `34-27` in `45:43`; G2 card `1-3 / -0.4935u`; Airtable written.
- G3 final draft + exact board supplied prospectively; four canonical forced-choice Positions are locked.
- No Airtable write until G3 ends.
- Same-series results do not update `K/P0/TK0`; only Fearless champion availability may carry forward.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`

## Game 3 draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT, following the user's established list convention.

HLE blue: `Camille / Pantheon / Ahri / Ziggs / Pyke`  
GEN red: `Gwen / Aatrox / Akali / Ashe / Seraphine`

## Game 3 source-truth board

- ML: GEN `1.703` / HLE `2.069`
- Duration `32.0`: Over `1.803` / Under `1.939`
- Total Kills `27.5`: Over `1.674` / Under `2.114`
- KH: GEN `-3.5 @1.816` / HLE `+3.5 @1.924`

## Game 3 price-blind DIM

HLE mechanisms:
- PKM: Pantheon/Ahri/Pyke pick -> Camille lockdown/collapse -> Ziggs ranged follow-up and structure conversion.
- SKM: Camille side pressure + Pantheon semi-global reinforcement while Ziggs/Ahri/Pyke hold or create objective-entry space.

GEN mechanisms:
- PKM: Ashe arrow / Seraphine catch -> Aatrox/Akali/Gwen multi-angle melee continuation.
- SKM: Gwen side-lane pressure while Ashe/Seraphine form a four-man catch/kite shell and Akali threatens backline access.

DIM rows:
- TAM: mixed; Seraphine/Ashe can punish direct HLE commitment, but do not generically suppress Pantheon/Camille/Pyke multi-angle pick chains; HLE has no universal answer to GEN sustained melee continuation either.
- OSG: HLE advantage from Ahri/Pyke vision-entry threat, Pantheon reinforcement and Ziggs pre-contact zone/structure pressure.
- DAU: mixed; HLE gains safer pre-contact/ranged damage through Ziggs while GEN has stronger sustained melee damage if it reaches stable contact.
- SLI: HLE slight; Camille side route is strengthened by Pantheon reinforcement, although Gwen remains a real direct lane answer.
- FNF: HLE's limited traditional frontline is not a major penalty because its primary identity is pick/collapse/siege rather than long front-to-back occupancy.
- CAS: HLE slight; Pyke execute/chase plus Ziggs conversion can turn one ordinary pick into repeat control, but GEN retains return-fight damage and is not certified as cascade-fragile.
- ETS: GEN benchmark strength is modestly higher; team strength does not alter the mechanical draft sign.
- AFP: HLE retains two distinct routes after denial of the first — pick/global collapse and side-pressure/structure conversion — while GEN must more often obtain clean contact to unlock its melee damage.

Diagnostic result: `D=+1 HLE`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 3 locked forced-choice card

### Moneyline
Q2 frozen probabilities: GEN `55%` / HLE `45%`.

- GEN @1.703 -> implied `58.72%` -> edge `-3.72pp`
- HLE @2.069 -> implied `48.33%` -> edge `-3.33pp`

Canonical ML: **HLE ML @2.069**  
`MODEL_EDGE=-3.33pp`  
`FORCED_NEG_EV=YES`

### Kill Handicap
Absolute line is `<5`, so KH must align with selected HLE ML.

Pre-price signed margin bins:
- HLE wins by 10+: `10%`
- HLE wins by 5-9: `12%`
- HLE wins by 1-4: `23%`
- GEN wins by 1-3: `18%`
- GEN wins by 4-9: `22%`
- GEN wins by 10+: `15%`

HLE win mass remains `45%`, consistent with frozen Q2 ML probability.  
HLE +3.5 raw cover = `63%`; capped execution probability = `63%`.  
HLE +3.5 @1.924 -> implied `51.98%` -> edge `+11.02pp`.

Canonical KH: **HLE +3.5 @1.924**  
`MODEL_EDGE=+11.02pp`  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=+1` — HLE has credible pick-to-Ziggs structure conversion.
- `Q=0` — no reliable pre-map compulsory-cycle spacing edge.
- `H=0` — do not double-count Ziggs structure compression already credited in V.
- `T=0` — HLE acceleration is balanced by GEN's Seraphine/Ashe defensive reset and scaling tools.
- `F=29.50m`.

At line 32.0:
- Under model `67.50%`
- Under @1.939 implied `51.57%`
- `MODEL_EDGE=+15.93pp`

Canonical Duration: **Under 32 @1.939**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=NO`

### Total Kills
Frozen `TK0=26.95`.

Price-blind bins:
- `<20`: `6%`
- `20-24`: `14%`
- `25-27`: `18%`
- `28-32`: `29%`
- `33-37`: `19%`
- `38+`: `14%`

Over 27.5 model = `62%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `18%` of scenario mass, concentrated below 28 kills. A separate high-contact/two-sided-brawl branch is large because both drafts contain repeatable catch, dive and chase access.

Over 27.5 @1.674 -> implied `59.74%` -> `MODEL_EDGE=+2.26pp`.

Canonical TK: **Over 27.5 @1.674**  
`FORCED_NEG_EV=NO`

## Game 3 execution lock

Four canonical positions are prospectively locked from the supplied final draft + exact board:
1. **HLE ML @2.069** — `0.25u shadow`
2. **HLE +3.5 @1.924** — `0.25u shadow`
3. **Under 32 @1.939** — `0.25u shadow`
4. **Over 27.5 @1.674** — `0.25u shadow`

Total: `1.00u shadow / 0u actual`.

Do not update predictions from live state. Await final G3 result, then write map + four Positions to Airtable and run map micro-audit.

## Cohort entering G3

- `52 Positions / 13 per family`
- `25W-27L / -1.26625u`
- ML `3-10 / -1.96425u`
- KH `6-7 / -0.41750u`
- Duration `9-4 / +0.98700u`
- TK `7-6 / +0.12850u`
- actual exposure `0u`

Preferred next structural checkpoint remains `80 total / 20 per family`.
