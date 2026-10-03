# Football Factor Calibration Bootstrap — 2026-10-03

**Status:** descriptive bootstrap only — zero production authority

## Purpose

Determine whether recent historical boards can be safely imported into the new Factor Calibration Observer without retrospectively manufacturing factor values.

## Activation chronology

- Burden-completion / continuation selector activation: commit `d68d773300ac25af406c3367e5fa6da2e8c2a411`, 2026-10-02 16:24 ICT.
- The 2 Oct 16:27–3 Oct 03:00 board was assessed at approximately 17:00 ICT, so the new burden-completion policy was active.
- Later 3 Oct boards were also produced under the new policy.

## Bootstrap eligibility result

**Fully eligible observations for complete factor-vector ablation: 0.**

This is intentional, not a data failure.

### Sep 30 / Oct 1 boards

These boards preserve the older route/carrier/chance/failure vector, but they predate the burden-completion selector.

Do not backfill:
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk.

They remain useful historical background for old-factor questions only and carry zero evidence for the new completion-factor weights.

### 2 Oct 16:27–3 Oct 03:00 board

The board was frozen after the selector activation and the durable report preserves rank/lane/support plus several qualitative completion judgments.

However, the durable report and current coverage persistence do not expose the complete exact machine factor vector for every fixture (route reliability, independent-route quality, chance quality, failure resistance, XI robustness, evidence confidence, burden protection and all new completion fields together).

Reconstructing those missing values from prose after results are known would violate hindsight integrity.

Therefore no full-vector calibration row is retroactively manufactured.

### 3 Oct boards

The current Daily Coverage persistence preserves completion mode/quality, continuation and stall fields for some newer rows, while the human board reports preserve additional reasoning.

The full exact observer vector still was not prospectively written into one immutable calibration record before outcome.

Therefore these boards are not imported as fully eligible observations.

## Existing hypotheses retained as hypotheses only

These are not factor-weight conclusions:

1. `continuation x stall risk`: HIGH continuation can be too optimistic when ordinary 2-0 / 1-1 control remains live.
2. `second-route strength x carrier`: historical selection sometimes preferred balanced two-route shapes over stronger self-funded carrier paths; the burden-completion patch already addresses the structural version of this issue.
3. `supported burden x completion`: O2.75/O3.0 needs explicit third/fourth-goal funding, not merely general attacking quality.
4. `failure resistance x completion`: a high-quality scoring route may still be a poor priority if its dominant failure mode directly creates a common stall endpoint.

All remain:

`CALIBRATION SIGNAL — OBSERVE ONLY`

## Clean start

The first board frozen after the Factor Calibration Observer activation commit is Observation Board 1.

For every ranked fixture on that board, Step 1 writes the complete immutable factor vector to Airtable before outcome.

After FT, `/audit` appends outcome labels and runs bucket/ablation diagnostics.

Do not change Football C factor ordering until the prospective thresholds in `FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md` are met.
