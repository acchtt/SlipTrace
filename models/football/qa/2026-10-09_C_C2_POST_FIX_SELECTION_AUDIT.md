# Football C + C2 — historical selection calibration checkpoint

**Audit date:** 2026-10-09 ICT  
**Official model:** C; **challenger:** C2 shadow  
**Nature:** retrospective diagnostic based on prospectively frozen football factors, NOT a new prediction, model-promotion trial, or verified user return.  
**Effective source:** Airtable `Factor Calibration Observations` and historical `Decision States`/`Website Picks`. No original frozen factors or exposures changed.

## 1. Freeze-safe sample

- 73 calibration rows retrieved; 67 prospectively eligible; 6 excluded.
- 16 repeated assessments removed by fixture + kickoff identity; **51 unique fixtures** remain, with one earliest frozen row per fixture.
- 5 distinct board IDs in the deduplicated sample (the larger raw sample had repeated board receipts).
- 42 STOP, 7 RESERVE, 2 FOLLOW. STOP results are **hypothetical frozen-supported-line counterfactuals**, never actual bets.
- All 51 have a full-time goal total and frozen supported-line settlement.
- **Observed completion materialized** and **observed continuation materialized** are not populated for these 51 distinct fixtures. Do not infer them from the final score; leave UNKNOWN pending reliable event-level evidence.
- Existing `Stall Endpoint Observed` = YES for 15/51 is a **coarse FT endpoint proxy**; it is not an independent classification of tactical 0-0/1-1/2-0 stalling.

## 2. Completion-mode cross-check (fixture unique)

| Frozen mode | N | Frozen-line full wins | Two or fewer FT goals | Average FT goals | Most concentrated competition |
|---|---:|---:|---:|---:|---:|
| TWO_SIDED | 22 | 8 | 14 | 2.32 | 27% |
| CARRIER_LED | 9 | 7 | 2 | 3.44 | **56%** |
| MIXED | 11 | 6 | 5 | 3.64 | 18% |
| NONE | 9 | 6 | 3 | 2.78 | 33% |

A lower frequency of two-goal endpoints in CARRIER_LED is a **candidate signal**, not a calibrated lift. It is only N=9, exceeds the 40% concentration guard, and uses different league/line mixtures. The 8/22 vs 7/9 full-win counts must **not** be represented as expected betting ROI.

## 3. Quality and stall conflict

- Frozen completion HIGH: N=9, 7 full wins, 2 at <=2 FT goals; MEDIUM: N=28, 12 full wins, 16 at <=2 goals; LOW: N=14, 8 full wins, 6 at <=2 goals.
- Frozen stall HIGH: N=24, 13 full wins, 11 at <=2 goals; MEDIUM: N=25, 13 full wins, 12 at <=2 goals; LOW: N=2, 1 full win.
- HIGH stall and MEDIUM stall have essentially indistinguishable *unadjusted* <=2 goal frequencies here. That is **not** proof that stall risk is useless: line, ranking/STOP selection, competition and freeze grade distributions differ. LOW stall has only two examples.
- O2.0 and O2.25 carry different settlement at two goals, so simply counting FT <=2 cannot replace actual protected-line settlement.

## 4. Non-STOP selection surface

- Nine distinct followed/reserved fixtures only: 6 frozen-line full wins, 2 losses, 1 half-loss.
- This is too small for a model-specific performance estimate, and it excludes many cases where a frozen STOP would have cleared.
- Do not promote a C2 challenger from this table; the factor ledger stores a frozen C perspective and lacks complete independent prospective C2 verdicts, executable prices and same-epoch settlements.

## 5. Historical case study vs prospective validation

The Sep 12/20 and Oct 9 Japanese league inversion cases and Oct 8 UAE Cup C2-only exposures are useful *discovery* cases, not confirmatory proof after the Oct 9 code change. C2's historical one-sided winners and C's two-goal stalls must not be backfilled as outcomes of the new funding gate.

**No prospective post-fix C/C2 paired settlement window is available yet.** It begins only with decisions frozen after the Oct 9 merge and accompanied by:
- independent C and C2 supported burdens;
- complete current C/C2 pair runtime receipt;
- actual event/quote evidence epoch, current source revision and delivery time;
- Decision State read-back and prepublication guard result;
- outcome settlement, including non-exposures;
- separation of model DIRECT BET, assumed WAIT, shadow exposure and confirmed user bet.

## 6. Decision

- Keep C official, C2 shadow; retain current third-goal safeguards.
- Do not relax the FORCED_CHAOS pathway or add O4.0+ funding expansion from this historical sample.
- Do not alter threshold weights or retroactively rescore HIGH/MEDIUM/LOW from FT.
- First process fix: make the new Step-2 prepublication guard mandatory, with epoch+publication-key persistence for new decisions only.
- Next model comparison: matched C/C2 same-evidence prospective decisions, with full-win/half-win/push/half-loss/loss and exposure-rate deltas, **including passes and misses**.
- For observation labels, consult match timelines and source evidence. When absent, explicitly report UNKNOWN rather than fabricate a mechanism.

**Status:** ANALYZED — OBSERVE ONLY; no promotion or model-threshold change justified.
