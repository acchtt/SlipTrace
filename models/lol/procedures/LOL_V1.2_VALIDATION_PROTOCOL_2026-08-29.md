# LoL v1.2 Frozen Validation Protocol — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.2 — Strength-Prior Moneyline + Duration Core

## 1. Epoch transition

The user explicitly authorized an immediate Moneyline patch on 2026-08-29 after the v1.1 workflow exposed a clear mechanical defect: the ML probability engine had no persistent team-strength prior and therefore forced materially different teams to begin from a neutral 50% baseline.

This qualifies under the v1.1 change rule allowing repair of a clear mechanical implementation/architecture defect with explicit user authorization.

v1.1 closes prospectively with:

- `ML_SAMPLE_N=0` accepted v1.1 Positions;
- `DURATION_SAMPLE_N=0` accepted Positions.

The two Game 1 retroactive user-designated Airtable ledger entries remain outside validation and do not count.

v1.2 begins:

- `ML_SAMPLE_N=0`;
- `DURATION_SAMPLE_N=0`.

Duration analytics are unchanged; the zero count simply carries forward because no accepted Duration Position existed.

---

# 2. Active validation families

Count accepted Positions separately:

- `ML_SAMPLE_N`
- `DURATION_SAMPLE_N`

Only user-confirmed executable live Positions count.

Do not count HOLD, PASS, unconfirmed candidates, retroactive ledger-only entries, historical v0.x/v1.0/v1.1 Positions, Kill Handicap or Total Kills.

---

# 3. Frozen v1.2 Moneyline core

During the initial v1.2 ML sample do not change without another explicit analytical authorization:

- team-strength tier `K=-2..+2`;
- `P0=50%+10*K pp`;
- `K` must use pre-series non-price evidence and remain series-frozen absent genuine roster/availability change;
- `D=-1/0/+1`;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff` treatment;
- `S=1.0*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `P=clamp(P0+3*S pp,15%,85%)`;
- raw implied `1/odds`;
- ML edge requirement `+5.0pp`;
- minimum odds `1.60`;
- probability locked before offered price is used as evidence.

`K` calibration is a new v1.2 component. Record it on every accepted ML Position.

---

# 4. Frozen Duration core — unchanged

Carry forward unchanged from v1.1:

- neutral anchor `31.0 minutes`;
- `R0(t)=max(5.0,31.0-t)`;
- `V/Q/H/T=-2..+2`;
- `ER=max(2.0,R0-1.5*V+1.0*Q+1.0*H+0.75*T)`;
- `F=t+ER`;
- `P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`;
- `P(UNDER)=100%-P(OVER)` with clear settlement semantics;
- raw implied `1/odds`;
- Duration edge requirement `+7.5pp`;
- minimum odds `1.60`;
- `F` locked before line/odds are used as evidence.

---

# 5. Shared execution freeze

Remain frozen:

- live betting only;
- active families = Moneyline + Duration;
- KH/TK retired;
- synchronized evidence;
- executable market;
- position-blind reassessment;
- default shadow stake `0.25u`;
- actual exposure `0u`;
- exact user line confirmation before Position creation;
- material state change expires candidate;
- no chasing/rescue/martingale/averaging down/stake escalation;
- no retroactive accepted Position creation.

---

# 6. Review cadence

Per family:

- 10 accepted Positions: diagnostic checkpoint only;
- 20: minimum architecture review;
- 30: preferred full calibration review.

For ML, review `K` assignment calibration separately from live-state calibration. Do not tune `K` after one upset or one favorite win.

---

# 7. Error taxonomy

Primary taxonomy only:

- `DRAFT READ ERROR`
- `LIVE STATE ERROR`
- `PROBABILITY/CALIBRATION ERROR`
- `PRICE/EXECUTION ERROR`

For v1.2 ML:

- wrong team-strength tier/baseline despite adequate pre-series evidence -> `PROBABILITY/CALIBRATION ERROR`;
- contaminating `K` with sportsbook price or same-series hindsight -> `PRICE/EXECUTION ERROR` plus governance review;
- wrong draft mechanism -> `DRAFT READ ERROR`;
- wrong `R/X/O/T` or mechanism contradiction -> `LIVE STATE ERROR`.

---

# 8. Evidence threshold for future change

A material analytical change should normally require one of:

1. at least 3 independent accepted Positions in the same family across at least 2 series/matchups with the same causal failure;
2. persistent calibration bias across at least 10 accepted Positions/probability band;
3. a clear mechanical defect;
4. explicit user-authorized analytical redesign with a documented new epoch.

One ordinary result is not enough.

---

# 9. ML review metrics

For accepted ML Positions record:

- `K` and `P0`;
- draft `D` and mechanism state;
- `R/X/O/T`;
- final model probability;
- raw implied probability;
- quoted edge;
- result;
- Brier score;
- shadow P/L.

At review points calculate calibration by `K` tier when sample size permits, as well as broad final probability bands.

---

# 10. Historical integrity

Do not relabel Game 1 or Game 2 of T1–BFX as v1.2. They were assessed under v1.1 and remain historical v1.1 evidence.

v1.2 activates prospectively from the fresh authority lock. Earlier results may be cited only as defect-discovery/audit context, not as accepted v1.2 validation observations.
