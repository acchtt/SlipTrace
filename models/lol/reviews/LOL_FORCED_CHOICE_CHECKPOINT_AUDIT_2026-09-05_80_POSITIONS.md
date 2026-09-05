# LoL Draft-Only Forced-Choice Checkpoint Audit — 80 Positions — 2026-09-05

**Status:** CHECKPOINT COMPLETE — CANONICAL v1.3 UNCHANGED / Q3 VALIDATION RULES DEFINED

## 1. Scope and ledger integrity

This review covers exactly:
- `80 unique settled forced-choice Positions`;
- `20 samples per market family`;
- `20 fully recorded maps`;
- `0.25u shadow per Position`;
- `0u actual exposure`.

Airtable was re-read at checkpoint. The standard filter `Entry Evidence contains FORCED-CHOICE` initially returned `76` records because the four corrected KT-DK G4 records had been rewritten under a `CORRECTED BOARD TRANSCRIPTION` prefix and had lost the cohort tag. Those four records were verified by canonical map id, retagged in place as `FORCED-CHOICE Q2. CORRECTED BOARD TRANSCRIPTION`, and the same Airtable filter now returns exactly `80` records. No selection/result/P&L value changed during this tag repair.

## 2. Overall result

- Settled Positions: `80`
- Wins / Losses: `39-41`
- Shadow stake: `20.00u`
- Shadow P/L: `-1.49750u`
- ROI on shadow stake: `-7.4875%`
- Actual exposure: `0u`

### By family

| Family | W-L | P/L | Stake | ROI |
|---|---:|---:|---:|---:|
| Moneyline | `5-15` | `-2.44150u` | `5.00u` | `-48.83%` |
| Kill Handicap | `10-10` | `-0.31200u` | `5.00u` | `-6.24%` |
| Duration | `13-7` | `+1.08650u` | `5.00u` | `+21.73%` |
| Total Kills | `11-9` | `+0.16950u` | `5.00u` | `+3.39%` |
| **Total** | **39-41** | **-1.49750u** | **20.00u** | **-7.4875%** |

The experiment remains negative overall, but the loss is still entirely concentrated in Moneyline. KH is close to flat, Duration remains materially positive, and TK has crossed slightly positive.

## 3. First 40 vs second 40

40-position checkpoint:
- `17-23 / -2.07550u`.

Positions 41-80 under the Q2 quarantine:
- `22-18 / +0.57800u`.

Incremental by family:
- ML: `4-6 / -0.36100u`
- KH: `6-4 / +0.31050u`
- Duration: `6-4 / +0.30950u`
- TK: `6-4 / +0.31900u`

The Q2 block is therefore materially better than the first 40. The main improvement is that three non-ML families were all profitable and Moneyline moved from catastrophic to modestly negative.

## 4. Moneyline audit — keep draft probability quarantined

### Q2 P0-only performance

After the 40-position checkpoint, forced-choice ML probability used frozen `P0` only and `D` contributed `0pp`.

Across ML positions 11-20:
- overall: `4-6 / -0.36100u`;
- model-positive P0-vs-price selections: `3-4 / -0.05750u`;
- forced/negative-edge selections: `1-2 / -0.30350u`.

This is a major improvement from the first block, where the model-positive ML subset was `0-5`. The remaining Q2 loss is concentrated in forced negative-edge selections rather than a clear failure of the P0-positive subset.

### Diagnostic D direction

Second 10-map block nonzero diagnostic D:
- KT-DK G3: leaned KT -> wrong;
- GEN-HLE G3: `D=+1 HLE` -> wrong;
- GEN-HLE G4: `D=+1 GEN` -> correct;
- VIT-G2 G3: `D=+1 VIT` -> wrong.

Second block nonzero D: `1/4` correct (`25%`).

Combined 20-map cohort:
- nonzero D observations: `12`;
- correct direction: `2`;
- wrong direction: `10`;
- observed directional accuracy: `16.7%`.

Decision: **keep `D_PROBABILITY_CONTRIBUTION=0` and `D_DIAGNOSTIC_ONLY=YES`.** The 80-position sample still does not justify reintroducing a positive draft coefficient into forced-choice ML probability.

### ML price-floor semantics — clarified prospectively

The user introduced `ML_PRICE_FLOOR=1.45` with the intent that sub-1.45 Moneylines are not worth taking.

Prospective Q3 interpretation:
- the floor is an **execution-eligibility filter only**;
- it does not alter `K`, `P0`, DIM, or any model probability;
- it does not transfer probability/edge to the opposite side;
- a dog above 1.45 may be selected only if it independently wins the model-vs-price side comparison;
- for the forced-choice **shadow** experiment, one ML side may still be recorded and tagged `FORCED_NEG_EV` when necessary;
- for any non-shadow/actual execution layer, PASS is mandatory if no eligible ML has positive edge.

This clarification does not retroactively change KC-GX G1-G4. GX was independently model-positive versus its market price on all four maps.

## 5. Kill Handicap audit — Q2 cap helped; retain

Overall KH:
- `10-10 / -0.31200u`.

Second block:
- `6-4 / +0.31050u`.

The 70% execution-probability cap and explicit 10+ tails reduced the unsupported confidence seen in the first 40. Severe plus-handicap failures still occurred — notably HLE +3.5 by 17 kills and GX +8.5 by 13 and 14 kills — but the family improved to positive P/L in the Q2 block.

Decision for Q3:
- retain `KH_MODEL_PROB_CAP=70%`;
- retain full signed margin bins before price;
- retain explicit numeric 10+ clean-cascade mass for both teams;
- retain `<5 => ML-aligned` portfolio rule;
- retain `±5.5+` independence;
- no fitted variance/tail coefficient change at 20 samples.

## 6. Duration audit — profitable, but Over branch remains structurally weak

Overall Duration:
- `13-7 / +1.08650u`.

Directional split across all 20 Duration positions:
- Under selections: `12-2`;
- Over selections: `1-5`.

Approximate branch P/L:
- Under: `+2.11050u`;
- Over: `-1.02400u`.

The Over warning added at 40 positions correctly identified a persistent asymmetry, and the next 10 maps did not resolve it. KC-GX G3 and G4 both produced short one-sided closes after the full Duration pass selected Over.

Decision for Q3:
- keep the v1.1 formula and 31.0m neutral anchor unchanged;
- keep `V/Q/H/T/F` persistence unchanged;
- keep `OVER_BRANCH_WARNING=YES`;
- escalate the forced-choice experimental Over branch to `DURATION_OVER_SHADOW_ONLY=YES` — it may be logged for validation, but it is not an approved positive execution signal;
- Under branch remains eligible under the normal model-vs-price test;
- do not refit coefficients from 20 samples.

This restriction is overlay-only and does not silently rewrite canonical v1.3 live/selective Duration authority.

## 7. Total Kills audit — near-flat to slightly positive; branch taxonomy needs one refinement

Overall TK:
- `11-9 / +0.16950u`.

Second block:
- `6-4 / +0.31900u`.

The explicit return-kill-suppression branch helped identify short one-sided misses, but KC-GX G1 exposed a different failure mode: a `40:40` game with only `20` total kills. That is not a fast-close event; it is a low-contact extended game.

Decision for Q3:
- keep TK0 construction unchanged;
- keep full pre-price kill bins;
- split the suppression taxonomy into two separately persisted numeric branches:
  1. `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION`;
  2. `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY`;
- do not change TK0 or fit new coefficients at this checkpoint.

## 8. Data/process audit

Positive process findings:
- no retroactive positions were created;
- same-series results did not alter frozen benchmark P0/TK0;
- all positions remained `0.25u shadow / 0u actual`;
- Airtable writes occurred at map end;
- source-truth board corrections were handled in place rather than duplicated.

Implementation issue found and repaired:
- four corrected KT-DK G4 positions lost the `FORCED-CHOICE` cohort tag after the board-transcription correction;
- tags were restored without changing selection, result, odds, or P/L;
- canonical Airtable filter now returns exactly `80` records.

## 9. Canonical model boundary

`models/lol/CURRENT_MODEL.md` remains canonical LoL v1.3 authority and is **unchanged** by this review.

The draft-only forced-choice cohort remains an experimental lock-scoped overlay. The Q3 decisions above apply only if a future fresh Session Authority Lock explicitly activates another validation block.

## 10. Next cadence

Current checkpoint:
- `80 positions / 20 per family / 20 maps`.

Preferred next structural checkpoint if the experiment continues:
- `120 positions / 30 per family`;
- `10 additional fully recorded maps / 40 positions`.

Earlier review remains appropriate only for a clear implementation/data-integrity bug.

## 11. KC-GX series closure

Final tracked series:
- G1 KC won `12-8` in `40:40`;
- G2 GX won `22-12` in `37:42`;
- G3 KC won `14-1` in `26:27`;
- G4 KC won `20-6` in `26:35`;
- final series: **Karmine Corp 3-1 GIANTX**.

G4 locked card settlement:
- GX ML @3.327 — LOSS `-0.25000u`;
- GX +8.5 @1.874 — LOSS `-0.25000u`;
- Over 32 @1.978 — LOSS `-0.25000u`;
- Over 25.5 @1.939 — WIN `+0.23475u`.

G4: `1-3 / -0.51525u`.

No additional KC-GX position may be created under this lock.

## Bottom line

At 80 positions the experiment is still negative (`-1.49750u`), but Q2 materially improved the second half (`+0.57800u`). The evidence supports **keeping D quarantined from ML probability**, retaining the **70% KH cap**, preserving the **Duration formula while quarantining Over as shadow-only**, and keeping TK unchanged except for splitting fast-close suppression from low-contact extended-game suppression. The 1.45 ML floor is clarified as an execution filter, not a reason to automatically take the dog.
