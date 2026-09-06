# Current Live Handoff — T1 vs Dplus KIA — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — SERIES 1-1 / TARGET G3 / NO T1-DK POSITIONS YET  
**Session lock:** `LOL-2026-09-06-V13-LCK-T1-DK-DRAFTONLY-FORCEDCHOICE-Q3-1704-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

T1 vs Dplus KIA — LCK 2026 Season Playoffs Lower Bracket Round 3, Bo5 Fearless Draft.

At activation, current schedule/live evidence showed **T1 1-1 Dplus KIA**. The lock starts prospectively at **Game 3**.

- No G1/G2 Position exists and none may be created retroactively.
- G1/G2 same-series results do not alter frozen `K/P0/TK0`; they may affect only Fearless champion availability.
- No T1-DK Airtable record exists yet.

Expected lineups:
- T1: Doran / Oner / Faker / Peyz / Keria
- DK: Siwoo / Lucid / ShowMaker / Smash / Career

## Fresh frozen benchmark

Current peer set: `LCK 2026 Rounds 3-4`; previous comparable split: `LCK 2026 Rounds 1-2`; same-series maps excluded.

- `B_current(DK)=+0.174447`
- `B_previous(DK)=+0.412956`
- `B_current(T1)=-0.177983`
- `B_previous(T1)=+0.902156`
- 70/30 raw blend: DK `+0.246000`, T1 `+0.146058`
- peer-wide re-standardized `B(DK)=+0.334587`
- peer-wide re-standardized `B(T1)=+0.198656`
- `GAP(DK-T1)=+0.135931 SD`

Frozen prior:
- `DK K=0 / P0=50%`
- `T1 K=0 / P0=50%`

Frozen TK baseline:
- DK current environment `25.9`
- T1 current environment `26.9`
- `TK0=26.40`

## Q3 overlay

- ML: full DIM persisted; `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; P0-only forced-choice probability.
- ML floor `1.45` is execution eligibility only; it never automatically forces the opposite side.
- KH: 70% cap, signed margin bins, explicit 10+ tails; `<5` must align with ML; `±5.5+` may be independent.
- Duration: v1.1 / 31.0m anchor unchanged; Over has warning and `DURATION_OVER_SHADOW_ONLY=YES`.
- TK: separately persist fast-close return-kill suppression and low-contact extended-game suppression.
- Exactly one canonical shadow selection per offered family; `0.25u each / 0u actual`.
- Airtable only at map end; no retroactive positions.

## Cohort entering T1-DK

- `92 settled positions / 23 per family / 23 settled maps`
- `46W-46L / -1.38275u`
- ML `7-16 / -2.35500u`
- KH `13-10 / +0.34850u`
- Duration `14-9 / +0.77725u`
- TK `12-11 / -0.15350u`

Historical outstanding item:
- IG-WE G4 has four prospectively locked but unsettled shadow Positions. They remain preserved in `models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-09-06_IG_WE.md` and are not cancelled by this switch.

## Next action

**READY FOR T1-DK GAME 3 FINAL DRAFT + EXACT BOARD.**