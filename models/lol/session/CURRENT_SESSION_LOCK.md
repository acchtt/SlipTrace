# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Status:** `CLOSED — SERIES COMPLETE / 80-POSITION CHECKPOINT COMPLETE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Round 1 — Karmine Corp vs GIANTX — Bo5 Fearless Draft`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Actual exposure:** `0u`

## Final series

- G1: KC `12-8`, `40:40`.
- G2: GX `22-12`, `37:42`.
- G3: KC `14-1`, `26:27`.
- G4: KC `20-6`, `26:35`.
- Final: **Karmine Corp 3-1 GIANTX**.

No additional KC-GX position may be created under this lock.

## 80-position checkpoint

Verified Airtable cohort:
- `80 unique forced-choice positions`;
- `20 per family`;
- `20 maps`;
- `39W-41L / -1.49750u`;
- ROI `-7.4875%`;
- actual exposure `0u`.

By family:
- ML `5-15 / -2.44150u`;
- KH `10-10 / -0.31200u`;
- Duration `13-7 / +1.08650u`;
- TK `11-9 / +0.16950u`.

Checkpoint review:
`models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-05_80_POSITIONS.md`

Final series handoff:
`models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-09-05_KC_GX.md`

## Prospective only — Q3 if a future fresh lock activates it

Canonical `models/lol/CURRENT_MODEL.md` remains unchanged.

- ML: `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.
- ML floor 1.45 is an execution filter only and does not automatically force the dog; opposite side must independently win model-vs-price comparison. Any actual/non-shadow layer PASSES if no eligible positive-edge ML exists.
- KH: retain 70% cap, signed bins, both 10+ tails, `<5` ML alignment, and wide-line independence.
- Duration: formula/31m anchor unchanged; forced-choice Over branch becomes `DURATION_OVER_SHADOW_ONLY=YES`.
- TK: TK0 unchanged; split numeric suppression persistence into `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY`.
- Preferred next checkpoint if continued: `120 positions / 30 per family`.

## Fresh-lock requirement

Before any new LoL position:
1. identify the current series fresh;
2. build a fresh pre-series Gol.gg benchmark with same-series results excluded;
3. write a new Session Authority Lock;
4. if the fresh lock does not explicitly activate Q3, use canonical v1.3 only.

If no fresh active lock exists: `MODEL REBUILD IN PROGRESS — HOLD`.