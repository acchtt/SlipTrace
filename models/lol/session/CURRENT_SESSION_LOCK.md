# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LCK-T1-DK-DRAFTONLY-FORCEDCHOICE-Q3-1704-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 3 — T1 vs Dplus KIA — Bo5 Fearless Draft`  
**Activation:** prospective from Game 3 only; G1/G2 receive no retroactive Positions.  
**Current series state:** `T1 2-1 Dplus KIA` after settled Game 3.  
**Current target:** `Game 4`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q3`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / 0.25u EACH / 0u ACTUAL`

## Frozen authority

Same-series outcomes never update pre-series `B/K/P0/TK0`; prior maps may affect only Fearless champion availability.

Fresh pre-series Gol.gg benchmark frozen before Game 1:
- `B(DK)=+0.334587`
- `B(T1)=+0.198656`
- `GAP(DK-T1)=+0.135931 SD`
- `DK K=0 / P0=50%`
- `T1 K=0 / P0=50%`
- `TK0=26.40`

Q3 controls:
- ML: full DIM required; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; P0-only forced-choice probability; `ML_PRICE_FLOOR=1.45` execution eligibility only; actual layer PASS if no eligible positive edge.
- KH: signed margin bins + explicit 10+ tails; `KH_MODEL_PROB_CAP=70%`; `<5` aligns with selected ML side; `±5.5+` may be independent.
- Duration: v1.1 formula / 31.0m anchor unchanged; Over is `DURATION_OVER_SHADOW_ONLY=YES`; Under eligible normally.
- TK: persist numeric fast-close return-kill suppression and low-contact extended-game suppression branches.
- exactly one canonical shadow selection per offered family under validation; Airtable only at map end; no retroactive positions.

## Settled Game 3

Draft:
- DK blue: `Trundle / Pantheon / Viktor / Jhin / Rell`
- T1 red: `Olaf / Skarner / Locke / Sivir / Karma`

Locked card:
1. `DK ML @2.113`
2. `DK +4.5 @1.780`
3. `Under 33 @1.905`
4. `Over 27.5 kills @2.136`

Final:
- T1 win `30-13`
- `41:19`
- total kills `43`

Settlement: `1W-3L / -0.46600u`.

## Settled cohort after G3

- `96 positions / 24 per family / 24 maps`
- `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

Outstanding historical item: IG-WE G4 remains prospectively locked but unsettled in its own handoff; switching current target did not cancel it.

Preferred structural checkpoint: `120 settled positions / 30 per family`.

## Next action

**AWAIT T1-DK GAME 4 FINAL DRAFT + EXACT BOARD.**

No Game 4 Position exists yet.