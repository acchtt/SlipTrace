# Current Live Handoff — Invictus Gaming vs Team WE — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — G1/G2/G3 SETTLED / IG LEADS 2-1 / G4 LOCKED / AWAIT FINAL  
**Session lock:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Frozen series authority

- `B(IG)=+0.797272`
- `B(WE)=-0.938274`
- `GAP(IG-WE)=+1.735546 SD`
- `IG K=+2 / P0=60%`
- `WE K=-2 / P0=40%`
- `TK0=33.40`
- same-series results never update `K/P0/TK0`; prior maps may affect only Fearless champion availability.

Q3 overlay remains active:
- ML: `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; forced-choice ML probability uses P0 only; ML floor 1.45 is execution eligibility only.
- KH: signed margin bins, explicit 10+ tails, 70% cap; `<5` aligns with ML; `±5.5+` may be independent.
- Duration: v1.1 formula / 31.0m anchor unchanged; Over is warning + shadow-only; Under remains eligible under normal comparison.
- TK: persist separate `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` branches.
- Airtable writes only at map end; no retroactive positions; actual exposure `0u`.

## Settled series state through G3

### Game 1 — SETTLED
- IG win `18-7`, `23:27`, total kills `25`.
- Card: IG ML W `+0.17325u`; IG -4.5 W `+0.21525u`; Over 32 L `-0.25u`; Over 31.5 kills L `-0.25u`.
- G1: `2-2 / -0.11150u`.

### Game 2 — SETTLED
- WE win `16-7`, `31:30`, total kills `23`.
- Card: IG ML L `-0.25u`; WE +5.5 W `+0.24025u`; Under 31 L `-0.25u`; Over 30.5 kills L `-0.25u`.
- G2: `1-3 / -0.50975u`.

### Game 3 — SETTLED
- IG win despite WE leading kills `22-18`, duration `33:42`, total kills `40`.
- Card: IG ML W `+0.16325u`; WE +5.5 W `+0.20500u`; Over 31 W `+0.19075u`; Over 29.5 kills W `+0.17700u`.
- G3: `4-0 / +0.73600u`.

Series score: **IG 2-1 WE**.
IG-WE tracked block through G3: `7W-5L / +0.11475u`.

## Game 4 — canonical prospective lock

Final draft supplied by user:
- IG blue: `Kled / Qiyana / Viktor / Kalista / Alistar`
- WE red: `Olaf / Pantheon / Annie / Sivir / Karma`

Exact board:
- ML: `IG 1.616 / WE 2.215`
- Duration 32: `Over 2.086 / Under 1.692`
- Total Kills 31.5: `Over 1.929 / Under 1.812`
- KH: `IG -4.5 1.864 / WE +4.5 1.855`

Canonical four-family card:
1. `IG ML @1.616`
2. `IG -4.5 kills @1.864`
3. `Under 32 minutes @1.692`
4. `Over 31.5 total kills @1.929`

Shadow stake: `0.25u each / 1.00u total`; actual exposure `0u`.

### G4 price-blind analytical lock

Moneyline:
- frozen P0 `IG 60% / WE 40%`;
- diagnostic DIM `D=+1 IG`, but `D_PROBABILITY_CONTRIBUTION=0`;
- IG primary mechanism: Kled/Alistar force first contact into Qiyana terrain burst with Viktor/Kalista cleanup;
- IG secondary mechanism: Kalista objective tempo plus Kled side pressure gives Qiyana/Viktor favorable compulsory-fight geometry;
- WE primary counter-route: Pantheon/Annie point-click start into Olaf access and Sivir follow-up, amplified by Karma speed/shields;
- WE secondary route: Sivir/Karma wave control plus Pantheon cross-map punish if IG splits setup poorly;
- adversarial pass: IG retains at least two independent mechanisms, but WE's direct point-click access keeps the draft from being a large edge;
- IG model `60%`; implied `61.88%`; edge `-1.88pp`;
- WE model `40%`; implied `45.15%`; edge `-5.15pp`;
- forced-choice selects the less-negative eligible side `IG`; `FORCED_NEG_EV=YES`; any actual/non-shadow layer would PASS.

Kill Handicap:
- line is `<5`, therefore selected KH team must align with selected IG ML;
- signed IG-minus-WE margin bins before price: `WE 10+ 13% / WE 5-9 11% / WE 1-4 16% / IG 1-4 17% / IG 5-9 20% / IG 10+ 23%`;
- IG -4.5 raw cover `43%`; cap not binding;
- implied `53.65%`; edge `-10.65pp`; `FORCED_NEG_EV=YES`.

Duration:
- draft-only `V=+1 / Q=0 / H=+1 / T=-1`;
- `F=29.75m` from 31.0m anchor;
- Under 32 model `65.75%`; implied `59.10%`; edge `+6.65pp`;
- selected branch is Under, so `OVER_BRANCH_WARNING=NO`; `DURATION_OVER_SHADOW_ONLY` not applicable;
- `FORCED_NEG_EV=NO` for validation bookkeeping.

Total Kills:
- frozen `TK0=33.40`;
- pre-price bins: `<20 4% / 20-24 8% / 25-29 14% / 30-34 25% / 35-39 24% / 40+ 25%`;
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION=17%`;
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY=5%`;
- Over 31.5 model approximately `64%`; implied `51.84%`; edge approximately `+12.16pp`; `FORCED_NEG_EV=NO`.

## Cohort entering G4

- `92 positions / 23 per family / 23 maps`
- overall `46W-46L / -1.38275u`
- ML `7-16 / -2.35500u`
- KH `13-10 / +0.34850u`
- Duration `14-9 / +0.77725u`
- TK `12-11 / -0.15350u`

Next preferred structural checkpoint remains `120 positions / 30 per family`.

## Next action

**AWAIT G4 FINAL RESULT.**

Do not write Airtable until map end.