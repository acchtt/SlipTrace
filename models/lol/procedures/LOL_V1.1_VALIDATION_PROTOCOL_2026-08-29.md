# LoL v1.1 Frozen Validation Protocol — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.1 — Moneyline + Duration Core

## 1. Epoch transition

The user explicitly authorized enabling Duration on 2026-08-29 while the v1.0 Moneyline-only validation sample still contained **0 confirmed Positions**.

This is a material market-scope/analytical extension, so the v1.0 Moneyline-only epoch closes at 0 Positions and a fresh v1.1 epoch begins. No results are silently mixed across analytical generations.

The v1.0 Moneyline formula itself is retained unchanged inside v1.1.

---

# 2. Active validation families

Count accepted Positions separately by family:

- `ML_SAMPLE_N`
- `DURATION_SAMPLE_N`

Only user-confirmed executable Positions count.

Do not count:

- HOLD;
- PASS;
- unconfirmed TAKE CANDIDATE;
- disappeared/moved lines never accepted;
- historical v0.x positions;
- Kill Handicap;
- Total Kills.

---

# 3. Frozen Moneyline core

The v1.0 Moneyline analytical module remains frozen unchanged:

- `D = -1/0/+1`;
- `R/X/O/T = -2..+2`;
- mechanism state `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff` treatment;
- `S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`;
- `P = clamp(50% + 3*S pp, 15%, 85%)`;
- raw implied `1/odds`;
- ML edge requirement `+5.0pp`;
- minimum odds `1.60`.

Adding Duration is not permission to alter ML weights after ordinary outcomes.

---

# 4. Frozen Duration core

During the initial Duration sample do not change without explicit user authorization:

- neutral final-duration anchor `31.0 minutes`;
- `R0(t) = max(5.0, 31.0 - t)`;
- variables `V/Q/H/T` and their `-2..+2` scales;
- `ER = max(2.0, R0 - 1.5*V + 1.0*Q + 1.0*H + 0.75*T)`;
- `F = t + ER`;
- `P(OVER) = clamp(50% + 7*(F-L) pp, 15%, 85%)`;
- `P(UNDER) = 100% - P(OVER)` subject to clear settlement rules;
- raw book implied probability `1/odds`;
- Duration edge requirement `+7.5pp`;
- minimum odds `1.60`;
- central `F` locked before line/odds are used as analytical evidence.

An ordinary Duration loss, a one-minute miss, or one missed opportunity does not change these items.

---

# 5. Shared execution freeze

Remain frozen unless explicitly changed by the user:

- live betting only;
- active families = Moneyline and Duration only;
- Kill Handicap and Total Kills retired;
- synchronized evidence required;
- executable market required;
- position-blind reassessment;
- default shadow stake `0.25u`;
- actual exposure `0u`;
- exact user line-existence confirmation before Position creation;
- no chasing/martingale/rescue/averaging down/stake escalation;
- historical prediction result and process validity remain separate.

---

# 6. Review cadence

Use the same cadence **per family**:

### 10 accepted Positions in a family

Diagnostic checkpoint only:

- W/L;
- average model probability;
- average raw implied probability;
- average quoted edge;
- Brier score where applicable;
- error-taxonomy counts;
- repeated causal patterns.

No architecture change by default.

### 20 accepted Positions in a family

Minimum architecture review point for that family.

### 30 accepted Positions in a family

Preferred first full calibration review for that family.

A family may be reviewed while the other remains frozen and under-sampled. Do not change ML merely because Duration miscalibrates, or vice versa.

---

# 7. Error taxonomy

Keep the same compact primary taxonomy:

- `DRAFT READ ERROR`
- `LIVE STATE ERROR`
- `PROBABILITY/CALIBRATION ERROR`
- `PRICE/EXECUTION ERROR`

For Duration:

- wrong `V/Q/H/T` or causal terminal interpretation -> `LIVE STATE ERROR`;
- reasonable state but bad 31-minute anchor, time weights, 7pp/min mapping or edge buffer -> `PROBABILITY/CALIBRATION ERROR`;
- wrong line, stale quote, settlement semantics, executability or confirmation -> `PRICE/EXECUTION ERROR`;
- draft/composition mechanism materially misread before live state -> `DRAFT READ ERROR` when that was the primary cause.

Do not create DOVC-style new error acronyms.

---

# 8. Evidence threshold for change

A material analytical change should normally require one of:

1. at least **3 independent accepted Positions** in the same family across at least **2 different series/matchups** showing the same causal failure;
2. a persistent calibration bias across at least **10 accepted Positions** or a sufficiently populated probability band;
3. a clear mechanical implementation defect.

A dramatic single miss is not enough.

---

# 9. Duration-specific review metrics

For accepted Duration Positions record when available:

- entry clock `t`;
- `V/Q/H/T`;
- central final estimate `F`;
- offered line `L`;
- selected Over/Under probability;
- raw implied probability;
- edge;
- final official/user-confirmed duration;
- absolute central-estimate error `|F - final duration|`;
- selected outcome;
- Brier score for selected side.

At review points calculate:

- mean/median absolute error of `F`;
- signed error `F - actual` to detect systematic over/under forecasting;
- Brier score;
- calibration by broad selected probability bands where sample permits;
- performance separately for Over and Under as a diagnostic, not as permission to create asymmetric rules after a few outcomes.

---

# 10. Moneyline review metrics

Continue the v1.0 metrics:

- W/L;
- Brier score;
- average model probability;
- average implied probability;
- average entry edge;
- broad probability-band calibration;
- shadow P/L as descriptive execution output.

---

# 11. Allowed changes during freeze

Without opening another analytical epoch, only:

1. governance/data-integrity repair;
2. factual context correction;
3. exact arithmetic/implementation typo repair that restores the written formula rather than changing it;
4. explicit user-authorized analytical change, in which case record a new calibration epoch if material.

---

# 12. Historical integrity

Do not rewrite or relabel v0.x or v1.0 records.

- v0.x remains historical/audit authority;
- v1.0 Moneyline-only epoch is preserved as a closed zero-Position epoch;
- new accepted Positions after v1.1 activation use `LoL v1.1 — Moneyline + Duration Core` as the active model generation;
- market family remains explicitly `Moneyline` or `Duration` in Airtable.

Kill Handicap and Total Kills remain retired.
