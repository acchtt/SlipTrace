# LoL v1.3 Frozen Validation Protocol — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.3 — Hierarchy Moneyline + Duration Core

## 1. Epoch transition

The user explicitly authorized the v1.3 Moneyline hierarchy repair during Game 3, effective prospectively from the next game after Game 3 ended.

The repair reduces the persistent team-strength weight and increases draft weight so the intended hierarchy is:

`strength prior < draft correction < accumulated live evidence`.

Game 3 remains v1.2 historical evidence and is not rescored as v1.3.

v1.3 began prospectively with:

- `ML_SAMPLE_N=0` accepted v1.3 Positions;
- Duration sample carrying forward independently.

On 2026-08-30, after TH vs MKOI Game 2, the user explicitly authorized two prospective execution/calibration repairs:
1. price cannot create the bet; selected-side causal thesis `C>0` is required;
2. team-strength `K` is to be constructed from a reproducible Gol.gg league-relative benchmark rather than loose subjective tiering.

Earlier accepted positions remain historical under the rules active at their entry time.

---

## 2. Frozen v1.3 Moneyline core

Do not change during initial validation without new explicit authorization:

- `K=-2..+2` constructed by `LOL_V1.3_TEAM_BENCHMARK_GOLGG_2026-08-30.md`;
- `P0=50%+5*K pp`;
- `D=-1/0/+1`;
- `R/X/O/T=-2..+2`;
- mechanism `INTACT / WEAKENING / BROKEN / REPLACED`;
- `D_eff=D / 0.5D / 0`;
- `C=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`;
- `S=C`;
- `P=clamp(P0+3*S pp,15%,85%)`;
- raw implied `1/odds`;
- ML edge >=+5.0pp;
- minimum odds 1.60;
- probability locked before price evidence.

### Frozen team benchmark

Primary data source: gol.gg same-league/tournament team tables, frozen pre-series.

Split benchmark:

`B_split = 0.30*z(WinRate) + 0.30*z(GDM) + 0.20*z(GD@15) + 0.10*z(TowerDiff/Game) + 0.05*z(DRA%) + 0.05*z(NASH%)`

Current/previous split weighting by current games:
- 15+: 70/30;
- 8-14: 55/45;
- under 8: 40/60;
subject to the active roster-continuity adjustment.

Re-standardize blended peer scores. Pairwise final benchmark gap maps to K:
- `<0.50 SD`: K=0;
- `0.50-<1.25 SD`: K=±1;
- `>=1.25 SD`: K=±2.

No sportsbook price and no same-series result may enter benchmark construction.

Metrics, weights, blending rules, roster adjustment and K thresholds are frozen for the initial benchmark-validation epoch.

### Frozen causal thesis gate

- selected-side `C>0` is required for TAKE CANDIDATE;
- selected side must have a coherent, currently reachable draft/live win mechanism;
- `K/P0` alone cannot satisfy the thesis gate;
- if `C<=0`, `PASS` even when numerical model-vs-book edge exceeds +5.0pp;
- price may validate value only after a non-price causal thesis exists; price cannot create the bet.

Record `TEAM_BENCH[...]`, `K/P0`, `C`, and all live state variables for every accepted ML Position.

---

## 3. Duration core

Duration remains unchanged from v1.1/v1.2:

- neutral anchor 31.0m;
- `R0=max(5,31-t)`;
- `V/Q/H/T=-2..+2`;
- `ER=max(2,R0-1.5V+Q+H+0.75T)`;
- `F=t+ER`;
- `P(OVER)=clamp(50%+7*(F-L) pp,15%,85%)`;
- Duration edge >=+7.5pp;
- minimum odds 1.60;
- F locked before line/price evidence.

---

## 4. Shared execution freeze

- live only;
- Moneyline + Duration active;
- KH/TK retired;
- synchronized executable evidence required;
- position-blind reassessment;
- shadow stake 0.25u unless lock changes it;
- actual exposure 0u;
- exact user confirmation before accepted Position;
- material state change expires candidate;
- no chasing/rescue/martingale/averaging down/stake escalation;
- no retroactive accepted Position creation.

---

## 5. Review cadence

Per family:

- 10 accepted Positions: diagnostic only;
- 20: minimum architecture review;
- 30: preferred full calibration review.

For ML, explicitly review:
- benchmark tier accuracy and whether K=±2 is being assigned at the right frequency;
- whether `K` remains light enough in P0;
- whether draft/live layers dominate at appropriate evidence strength;
- whether causal thesis gate prevents price-only contrarian entries without suppressing genuinely supported opportunities.

Do not retune after one upset.

---

## 6. Error taxonomy

Only:

- `DRAFT READ ERROR`
- `LIVE STATE ERROR`
- `PROBABILITY/CALIBRATION ERROR`
- `PRICE/EXECUTION ERROR`

Incorrect benchmark/tier construction or hierarchy/weight calibration is `PROBABILITY/CALIBRATION ERROR`.

Sportsbook contamination or issuance of a price-only candidate without positive causal thesis is `PRICE/EXECUTION ERROR` plus governance review.

---

## 7. Future changes

Material analytical changes normally require repeated causal failure across independent accepted positions, persistent calibration bias, a clear mechanical defect, or explicit user-authorized redesign.

Historical v0.x/v1.0/v1.1/v1.2 records remain unchanged. Previously accepted v1.3 Positions also remain historical under the rules active at their entry time; do not retroactively invalidate them.
