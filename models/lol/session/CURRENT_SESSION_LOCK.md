# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Status:** `CLOSED — SERIES COMPLETE / 40-POSITION CHECKPOINT COMPLETE`  
**Scope:** `LCK 2026 Season Playoffs — Lower Bracket Round 1 — Dplus KIA vs BNK FearX — Bo5 Fearless Draft`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Actual exposure:** `0u`

## Closure

- Final series score: **Dplus KIA 3-2 BNK FearX**.
- No additional Position may be created under this lock.
- G3-G5 canonical forced-choice Positions are fully settled and written to Airtable.
- The forced-choice cohort reached exactly `40 Positions / 10 per family`.

Checkpoint state:
- overall `17W-23L / -2.0755u`;
- ML `1-9 / -2.0805u`;
- KH `4-6 / -0.6225u`;
- Duration `7-3 / +0.7770u`;
- TK `5-5 / -0.1495u`;
- actual exposure `0u`.

Full checkpoint audit:
`models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-03_40_POSITIONS.md`

Final series handoff:
`models/lol/handoffs/CURRENT_LIVE_HANDOFF_2026-09-03_DK_BFX.md`

## Prospective next forced-choice validation block

These controls are **not active under this closed lock**. A future fresh Session Authority Lock must explicitly activate them:

- canonical `CURRENT_MODEL.md` / LoL v1.3 remains unchanged;
- full DIM still required and persisted;
- forced-choice ML: `D_DIAGNOSTIC_ONLY=YES`, `D_PROBABILITY_CONTRIBUTION=0`, probability uses frozen `P0` only;
- KH `<5` must align with selected ML; `±5.5` or wider may remain independent;
- KH full signed-margin bins required and `KH_MODEL_PROB_CAP=70%` used for execution-edge reporting/comparison;
- Duration formula remains frozen; add diagnostic `OVER_BRANCH_WARNING` for selected draft-only Overs;
- TK framework remains frozen; explicit numeric one-sided fast-close / return-kill-suppression branch required;
- preferred next structural checkpoint: `80 total Positions / 20 per family`.

## Mandatory next-session behavior

Before any new LoL Position:
1. bootstrap from `models/lol/CURRENT_MODEL.md` and `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
2. observe that this lock is CLOSED and do not reuse it;
3. identify the current match fresh;
4. build a fresh price-independent Gol.gg benchmark;
5. create a fresh Session Authority Lock for that match;
6. load the newest applicable handoff last.

If no fresh lock exists: `MODEL REBUILD IN PROGRESS — HOLD`.
