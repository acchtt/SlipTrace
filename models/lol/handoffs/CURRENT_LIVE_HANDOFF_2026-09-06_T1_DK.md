# Current Live Handoff — T1 vs Dplus KIA — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — SERIES 1-1 / G3 LOCKED / AWAIT FINAL  
**Session lock:** `LOL-2026-09-06-V13-LCK-T1-DK-DRAFTONLY-FORCEDCHOICE-Q3-1704-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Frozen series authority

T1 vs Dplus KIA — LCK 2026 Season Playoffs Lower Bracket Round 3, Bo5 Fearless Draft. Lock begins prospectively at Game 3 with series 1-1. G1/G2 receive no retroactive Positions and do not alter frozen `K/P0/TK0`.

Fresh pre-series benchmark:
- `B(DK)=+0.334587`
- `B(T1)=+0.198656`
- `GAP(DK-T1)=+0.135931 SD`
- `DK K=0 / P0=50%`
- `T1 K=0 / P0=50%`
- `TK0=26.40`

Q3 remains active: draft `D` diagnostic only / 0pp probability contribution; ML floor 1.45 execution-filter only; KH 70% cap and `<5` ML-alignment rule; Duration Over shadow-only; TK fast-close and low-contact suppression branches persisted; Airtable only at map end.

## Game 3 — canonical prospective lock

Final draft supplied by user:
- DK blue: `Trundle / Pantheon / Viktor / Jhin / Rell`
- T1 red: `Olaf / Skarner / Locke / Sivir / Karma`

Exact board:
- ML: `T1 1.675 / DK 2.113`
- Duration 33: `Over 1.834 / Under 1.905`
- Total Kills 27.5: `Over 2.136 / Under 1.660`
- KH: `T1 -4.5 1.967 / DK +4.5 1.780`

Canonical four-family card:
1. `DK ML @2.113`
2. `DK +4.5 kills @1.780`
3. `Under 33 minutes @1.905`
4. `Over 27.5 total kills @2.136`

Shadow stake: `0.25u each / 1.00u total`; actual exposure `0u`.

### G3 analytical lock

Moneyline:
- frozen P0 `DK 50% / T1 50%`;
- full DIM diagnostic `D=+1 DK`, but `D_PROBABILITY_CONTRIBUTION=0`;
- DK mechanism 1: Pantheon/Rell point-click/chain engage into Viktor zone and Jhin follow-up;
- DK mechanism 2: Trundle pillar/ult disrupts Olaf-Skarner front line and improves objective/corridor control;
- T1 counter-route 1: Skarner start plus Olaf access with Sivir/Karma speed can collapse DK backline;
- T1 counter-route 2: Sivir/Karma wave control and front-to-back durability can absorb first contact and reverse extended fights;
- adversarial pass leaves DK with two independent mechanisms but not enough to modify P0 under Q3;
- DK model `50.0%`; implied `47.33%`; edge `+2.67pp`; `FORCED_NEG_EV=NO`.

Kill Handicap:
- absolute line `<5`, so KH must align with selected DK ML;
- signed DK-minus-T1 margin bins before price: `T1 10+ 15% / T1 5-9 14% / T1 1-4 21% / DK 1-4 19% / DK 5-9 16% / DK 10+ 15%`;
- DK +4.5 raw cover `71%`; Q3 reporting cap => `70%`;
- implied `56.18%`; capped execution edge `+13.82pp`; `FORCED_NEG_EV=NO`.

Duration:
- draft-only `V=+1 / Q=0 / H=+1 / T=0`;
- `F=30.50m` from 31.0m anchor;
- Under 33 model approximately `63.5%`; implied `52.49%`; edge approximately `+11.01pp`;
- selected branch Under => `OVER_BRANCH_WARNING=NO`; `FORCED_NEG_EV=NO`.

Total Kills:
- frozen `TK0=26.40`;
- pre-price bins: `<20 10% / 20-24 16% / 25-27 18% / 28-32 28% / 33-37 18% / 38+ 10%`;
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION=16%`;
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY=8%`;
- Over 27.5 model `56%`; implied `46.82%`; edge `+9.18pp`; `FORCED_NEG_EV=NO`.

## Cohort entering G3

- `92 settled positions / 23 per family / 23 settled maps`
- `46W-46L / -1.38275u`
- ML `7-16 / -2.35500u`
- KH `13-10 / +0.34850u`
- Duration `14-9 / +0.77725u`
- TK `12-11 / -0.15350u`

Historical outstanding item: IG-WE G4 remains prospectively locked but unsettled in its own handoff and is not cancelled by this target switch.

## Next action

**AWAIT T1-DK GAME 3 FINAL RESULT.**

Do not write Airtable until map end.