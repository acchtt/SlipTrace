# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** SERIES COMPLETE — KC 3-1 GX / 80-POSITION CHECKPOINT COMPLETE  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7` — CLOSED  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE Q2 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Final series

Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

- G1: KC won `12-8` in `40:40`.
- G2: GX won `22-12` in `37:42`.
- G3: KC won `14-1` in `26:27`.
- G4: KC won `20-6` in `26:35`.
- Final series: **Karmine Corp 3-1 GIANTX**.

All four maps and all 16 canonical KC-GX positions are written to Airtable.

## Game 4 final settlement

Draft:
- KC blue: `Rumble / Pantheon / Sylas / Varus / Vel'Koz`
- GX red: `Ornn / Xin Zhao / Syndra / Kalista / Renata Glasc`

Board:
- ML: KC `1.299` / GX `3.327`
- Duration `32.0`: Over `1.978` / Under `1.771`
- TK `25.5`: Over `1.939` / Under `1.787`
- KH: KC `-8.5 @1.864` / GX `+8.5 @1.874`

Canonical G4 card:
1. GX ML @3.327 — LOSS — `-0.25000u`
2. GX +8.5 @1.874 — LOSS — `-0.25000u`
3. Over 32 @1.978 — LOSS — `-0.25000u`
4. Over 25.5 @1.939 — WIN — `+0.23475u`

**G4: `1-3 / -0.51525u`.**

## 80-position checkpoint

Verified canonical cohort:
- `80 Positions / 20 per family / 20 maps`
- `39W-41L`
- `-1.49750u`
- ROI `-7.4875%`
- actual exposure `0u`

By family:
- ML `5-15 / -2.44150u`
- KH `10-10 / -0.31200u`
- Duration `13-7 / +1.08650u`
- TK `11-9 / +0.16950u`

Positions 41-80 under Q2 were `22-18 / +0.57800u`.

Full review:
`models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-05_80_POSITIONS.md`

## Prospective Q3 conclusions — only under a future fresh lock

Canonical `CURRENT_MODEL.md` remains unchanged.

If another draft-only forced-choice validation block is explicitly activated:
- ML: keep `D_DIAGNOSTIC_ONLY=YES` and `D_PROBABILITY_CONTRIBUTION=0`.
- ML floor: `1.45` is an execution filter only; it never automatically forces the dog. Opposite side must independently win model-vs-price comparison. Any actual layer PASSES when no eligible positive-edge ML exists.
- KH: keep 70% probability cap, signed margin bins, both 10+ tails, `<5` ML alignment, and wide-line independence.
- Duration: formula/31m anchor unchanged; Over branch becomes `DURATION_OVER_SHADOW_ONLY=YES` in the forced-choice experiment; Under remains normally eligible.
- TK: TK0 unchanged; separately persist `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` branches.

Preferred next structural checkpoint if continued: `120 positions / 30 per family`.

No additional KC-GX position may be created. A new match requires fresh identification, fresh pre-series benchmark, and a new Session Authority Lock.