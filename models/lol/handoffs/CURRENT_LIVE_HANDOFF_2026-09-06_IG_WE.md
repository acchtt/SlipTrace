# Current Live Handoff — Invictus Gaming vs Team WE — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — G1 UNSETTLED / G2 LOCKED / AWAIT FINALS  
**Session lock:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Invictus Gaming vs Team WE — LPL 2026 Split 3 Playoffs Lower Bracket Quarterfinal 1, Bo5 Fearless Draft.

- G1 has four prospective canonical shadow selections locked below but remains unsettled because the user has not supplied explicit final-result evidence.
- G2 now has four prospective canonical shadow selections locked below.
- Do not infer or retroactively settle G1 merely because a G2 board now exists.
- Airtable remains untouched until explicit map-end evidence is supplied for each map.
- Same-series results must not alter frozen `K/P0/TK0`; prior maps may affect only Fearless champion availability.

## Frozen benchmark

- `B(IG)=+0.797272`
- `B(WE)=-0.938274`
- `GAP(IG-WE)=+1.735546 SD`
- `IG K=+2 / P0=60%`
- `WE K=-2 / P0=40%`
- `TK0=33.40`

Expected lineups:
- IG: TheShy / Wei / Rookie / Assum / Meiko
- WE: Cube / Monki / Karis / About / Erha

Roster adjustments used in the frozen benchmark:
- IG current-only due at least three material Split 2 -> Split 3 starter changes;
- WE normal 70/30 blend with lineup continuity.

## Pre-series market board — context only / excluded from benchmark

User supplied a readable sportsbook screenshot pre-G1. Captured series winner `IG 1.475 / WE 2.616` plus map handicaps/totals/exact score. These prices are context only and are NOT inputs to `B/K/P0/TK0`; no series-market Position was created.

## Q3 overlay

- ML: `D_DIAGNOSTIC_ONLY=YES`, `D_PROBABILITY_CONTRIBUTION=0`; frozen P0 only.
- ML floor `1.45` is an execution filter only; it does not automatically force the dog.
- KH: 70% probability cap, signed margin bins, numeric 10+ tails; `<5` must align with ML; `±5.5+` may be independent.
- Duration: frozen v1.1 formula and 31.0m anchor; Over has `OVER_BRANCH_WARNING=YES` and `DURATION_OVER_SHADOW_ONLY=YES`.
- TK: persist both `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` numeric branches.
- Four-family validation remains `0.25u shadow each / 0u actual`.
- Airtable writes only at map end; no retroactive positions.

## Game 1 — canonical prospective lock

Final draft supplied by user:
- IG blue: `Gwen / Nocturne / Syndra / Yunara / Lulu`
- WE red: `K'Sante / Lee Sin / Ryze / Caitlyn / Bard`

Exact board:
- ML: `IG 1.693 / WE 2.085`
- Duration 32: `Over 2.030 / Under 1.731`
- Total Kills 31.5: `Over 2.120 / Under 1.671`
- Total Kills 30.5: `Over 1.895 / Under 1.843`
- Total Kills 29.5: `Over 1.714 / Under 2.054`
- KH: `IG -4.5 1.861 / WE +4.5 1.859`

Canonical four-family card:
1. `IG ML @1.693`
2. `IG -4.5 kills @1.861`
3. `Over 32 minutes @2.030`
4. `Over 31.5 total kills @2.120`

Shadow stake: `0.25u each / 1.00u total`; actual exposure `0u`.

### G1 price-blind analytical lock

Moneyline:
- frozen P0 `IG 60% / WE 40%`;
- full DIM diagnostic `D=+1 IG`, but `D_PROBABILITY_CONTRIBUTION=0`;
- selected ML model `IG 60%`; book implied `59.07%`; edge `+0.93pp`; `FORCED_NEG_EV=NO`.

Kill Handicap:
- `<5` portfolio rule requires alignment with selected IG ML;
- signed IG-minus-WE margin bins: `WE 10+ 12% / WE 5-9 11% / WE 1-4 17% / IG 1-4 18% / IG 5-9 20% / IG 10+ 22%`;
- IG -4.5 raw cover `42%`; implied `53.73%`; edge `-11.73pp`; `FORCED_NEG_EV=YES`.

Duration:
- draft-only `V=0 / Q=+1 / H=+1 / T=+1`; `F=33.75m`;
- Over 32 model `62.25%`; implied `49.26%`; edge `+12.99pp`;
- `OVER_BRANCH_WARNING=YES`; `DURATION_OVER_SHADOW_ONLY=YES`.

Total Kills:
- bins `<20 7% / 20-24 11% / 25-29 20% / 30-34 24% / 35-39 20% / 40+ 18%`;
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION=18%`;
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY=12%`;
- Over 31.5 model approximately `52.5%`; implied `47.17%`; edge approximately `+5.33pp`.

## Game 2 — canonical prospective lock

Final draft supplied by user:
- WE blue: `Galio / Wukong / Akali / Lucian / Milio`
- IG red: `Rumble / Naafiri / Orianna / Xayah / Rakan`

Exact board:
- ML: `IG 1.598 / WE 2.250`
- Duration 31: `Over 1.947 / Under 1.797`
- Total Kills 30.5: `Over 1.771 / Under 1.977`
- KH: `IG -5.5 1.769 / WE +5.5 1.961`

Canonical four-family card:
1. `IG ML @1.598`
2. `WE +5.5 kills @1.961`
3. `Under 31 minutes @1.797`
4. `Over 30.5 total kills @1.771`

Shadow stake: `0.25u each / 1.00u total`; actual exposure `0u`.

### G2 price-blind analytical lock

Moneyline:
- frozen P0 `IG 60% / WE 40%`;
- full DIM diagnostic `D=+1 IG`, but `D_PROBABILITY_CONTRIBUTION=0`;
- IG mechanisms: Rumble/Rakan/Naafiri initiation layered into Orianna AoE with Xayah self-peel; secondary route is Rumble zone control plus Xayah/Orianna front-to-back around objectives;
- WE mechanisms: Galio/Wukong/Akali multi-angle dive with Lucian follow-up; secondary route is Wukong/Galio first contact enabling Akali side access;
- IG model `60%`; implied `62.58%`; edge `-2.58pp`;
- WE model `40%`; implied `44.44%`; edge `-4.44pp`;
- forced-choice selects less-negative eligible side `IG`; `FORCED_NEG_EV=YES`; any actual/non-shadow layer would PASS because neither side has positive edge.

Kill Handicap:
- line is wide (`±5.5`), so independent side selection is allowed;
- signed IG-minus-WE margin bins before price: `WE 10+ 11% / WE 5-9 12% / WE 1-4 17% / IG 1-4 18% / IG 5-9 21% / IG 10+ 21%`;
- WE +5.5 raw cover approximately `62%`; cap not binding;
- implied `50.99%`; edge approximately `+11.01pp`; `FORCED_NEG_EV=NO`.

Duration:
- draft-only `V=+1 / Q=0 / H=0 / T=0`;
- `F=29.50m` from 31.0m anchor;
- Under 31 model `60.50%`; implied `55.65%`; edge `+4.85pp`;
- `OVER_BRANCH_WARNING=NO`; `FORCED_NEG_EV=NO` for validation bookkeeping (below canonical live execution edge gate, but this is the forced-choice shadow overlay).

Total Kills:
- frozen `TK0=33.40`;
- pre-price bins: `<20 5% / 20-24 9% / 25-30 22% / 31-35 28% / 36-40 20% / 41+ 16%`;
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION=18%`;
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY=8%`;
- Over 30.5 model `64%`; implied `56.47%`; edge `+7.53pp`; `FORCED_NEG_EV=NO`.

## Cohort entering series

- `80 positions / 20 per family`
- `39W-41L / -1.49750u`
- ML `5-15 / -2.44150u`
- KH `10-10 / -0.31200u`
- Duration `13-7 / +1.08650u`
- TK `11-9 / +0.16950u`

Next preferred structural checkpoint: `120 positions / 30 per family`.

## Next action

**AWAIT EXPLICIT G1/G2 FINAL RESULT EVIDENCE.**

Do not write Airtable until each map end is explicitly supplied.