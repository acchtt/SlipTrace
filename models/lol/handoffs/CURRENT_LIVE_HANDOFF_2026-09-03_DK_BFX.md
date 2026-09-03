# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** SERIES COMPLETE — GAME 5 SETTLED — 40-POSITION CHECKPOINT COMPLETE  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7` — CLOSED/HISTORICAL  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`

## Final series

- Dplus KIA vs BNK FearX — LCK 2026 Season Playoffs Lower Bracket Round 1.
- Final series score: **DK 3-2 BFX**.
- G1-G2 had no prospective canonical Positions in this chat.
- G3: DK win `13-12`, `31:57`.
- G4: DK win `16-6`, `22:43`.
- G5: user-designated final DK win `16-6`, `24:42`.

No additional DK-BFX Position may be created.

## Game 5 settlement

Locked canonical G5 Positions:
- BFX ML @1.866 — LOSS `-0.2500u`
- BFX +3.5 @1.770 — LOSS `-0.2500u`
- Under 32 @1.958 — WIN `+0.2395u`
- Over 27.5 kills @1.756 — LOSS `-0.2500u`

G5 result: `1W-3L / -0.5105u`.

Airtable map + all four G5 Positions were written at map end.

## Forced-choice cohort at checkpoint

Exactly `40 unique settled Positions / 10 per family`:
- overall `17W-23L`;
- shadow P/L `-2.0755u`;
- shadow stake `10.00u`;
- ROI `-20.755%`;
- actual exposure `0u`.

By family:
- Moneyline `1-9 / -2.0805u`;
- Kill Handicap `4-6 / -0.6225u`;
- Duration `7-3 / +0.7770u`;
- Total Kills `5-5 / -0.1495u`.

## 40-position audit decision

Canonical LoL v1.3 remains unchanged.

Audit authority:
`models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-03_40_POSITIONS.md`

Prospective next forced-choice block, only if a fresh lock explicitly activates it:
- full DIM remains mandatory;
- `D` remains recorded but `D_PROBABILITY_CONTRIBUTION=0` for forced-choice ML; use frozen `P0` only;
- `D_DIAGNOSTIC_ONLY=YES`;
- KH `<5` must align with ML; `±5.5+` may remain independent;
- full KH signed margin bins required; use `KH_MODEL_PROB_CAP=70%` for execution-edge reporting/comparison;
- Duration formula remains frozen; diagnostic `OVER_BRANCH_WARNING=YES` when draft-only Over is selected;
- TK remains structurally unchanged but must persist explicit numeric `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` mass;
- next preferred structural checkpoint: `80 Positions / 20 per family`.

## Next-session requirement

Before any new Position:
1. identify the new current match fresh;
2. build a fresh pre-series Gol.gg benchmark;
3. create a fresh Session Authority Lock;
4. never reuse this completed DK-BFX lock.
