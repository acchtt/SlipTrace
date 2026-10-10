# C/C2 goal-burden QA: October 10 research and matched-gate calibration

**Status:** research/QA implemented; production decision thresholds unchanged.
**Canonical production:** Football C official; Football C2 shadow only.
**Rule version:** exact current `core.py` compared with PR #92's
pre-2026-10-09 C O2.25 exemption and a C2 quality-floor-only sensitivity.
**No revised odds, bets, winners, retroactive actions or P/L authorized.**

## A. Step-1 forecast gap closed prospectively

The current `core.MatchAssessment` and deterministic C/C2 decisions
receive subjective route and quality labels plus independent protected
supported lines; they do **not** independently output a numerical expected
goal total for each team. A protected O2.0 is **not** the prediction
"the game will finish with 2.0 goals."

For new research epochs the **advisory** `goal_burden_forecast.py`
accepts evidenced home/away central+uncertainty goal contributions before
market comparison, computes their arithmetic total, and records the
third/fourth-goal mechanisms and failure pathways. Missing information is
`EVIDENCE_LIMITED`, with **no invented expectation**. A major bookmaker
market-centre gap (>=0.75 goals) becomes `RECHECK_REQUIRED`, not a forced
C/C2 rejection or quote-based goal forecast adjustment.

**Calibration caveat:** Until a new prospective sample is settled and
evaluated out of sample, these numbers are a traceable researcher scenario,
not calibrated xG/Poisson/probability estimates. Do not expose the output as
a validated expected-goals model or substitute it for C/C2 clearing-goal
funding or a current bookmaker quote. The advisory output must not delay
the existing `/xi` decision window.

## B. Historical C sensitivity — actual frozen-factor memory sample

**Source:** Airtable `Factor Calibration Observations`
(`tblz2s2KR4BRyAaVo`), read 2026-10-10; earliest persisted
`createdTime` record per normalized fixture-name + kickoff-UTC identity,
then the exact original C-factor fields. No current final score is used
to construct a frozen C policy input.

- 79 total observation records.
- 73 marked calibration eligible.
- 16 repeated fixture/KO rows removed: 57 unique, of which **51**
  have the complete frozen C-factor dimensions needed for gate comparison.
- 6 incomplete factor snapshots excluded from the gate sensitivity.
- Among 51 complete C snapshots, **18** have supported line O2.25.
- At O2.25 the pre-PR #92 C goal-funding rule admitted the funding
  burden mechanically (`line < 2.5`); the current rule requires
  third-goal funding.
- Current goal-funding test **passes 1/18** O2.25 snapshots and
  **blocks 17/18**, versus pre-PR #92 passing 18/18.
- Among **17 additionally blocked**, observed FT goals are:
  **8 fixtures with >=3 goals** (O2.25 would fully win),
  **5 fixtures with exactly 2** (half-loss),
  **4 fixtures with <=1** (loss).

Other frozen-line groups in the 51 complete snapshots:
O2.0 (17), O2.5 (12), O2.75 (2), O1.5 (1), O1.75 (1).
The isolated PR #92 historical C funding ablation creates **zero**
incremental gate disagreements in those other groups.

**Interpretation:** PR #92 greatly narrowed the O2.25 funding pathway.
In this exploratory retrospective sample, the extra rejections included
both high- and low-scoring outcomes. This is **not** evidence that the
17 cases were tradable; a goal-rule gate pass is not C-BET, and no
contemporaneous executable price, verified same-epoch XI, source-timed
Step-2 receipt, or confirmed exposure is supplied by this factor table.

**Sampling limitations:** These are historical C frozen-factor records
with some untimed/backfilled observations, overlapping competitions and
selection/supported-line concentrations; first persisted does not
necessarily mean independently attested earliest pre-kickoff frozen state.
The retrospective endpoint is an outcome *label*, not an input. Selection
and league biases cannot be removed from these aggregate counts.
No model performance or return-confidence claim should be made.

## C. C2 matched evidence is missing, do not manufacture it

The Airtable calibration table only supplies C frozen factors.
A C2 supported line or inferred C2 result is not an independent prospective
C2 snapshot. The October 9 retrospective audit also reported **no
confirmatory post-fix paired C+C2 settlement window**.

The new `goal_gate_shadow_audit.py` requires separately frozen model C
and model C2 factor inputs, same fixture and same `evidence_epoch_id`,
and valid pre-kickoff frozen timestamps for a *verified matched pair*.
It compares C with its pre-PR #92 gate and C2 with a
`SELECTION_FLOOR_WITHOUT_EXTRA_GOAL_GATE` diagnostic comparator.

This returns **goal-gate eligibility only**. It cannot silently convert
a frozen C2 supported line into a BET, a shadow return, a historical win,
or physical P/L. Untimed historical snapshots never count as verified
prospective C+C2 pairs.

## D. Prospective experiment / go-no-go

1. Continue publishing the existing C + C2 official/shadow decision pair
   from the exact same source/quote/XI epoch. Keep all true production
   thresholds and publication guard unchanged.
2. Save before kickoff for **both** models: numerical football-first
   home/away contribution or EVIDENCE_LIMITED, supported line,
   route/funding factors, quote/market history, current C/C2 actions,
   decision-delivery timestamp, and the actual source revision.
3. Apply shadow gate ablation to **identical frozen inputs**, never
   after seeing the FT result. The market odds are *separate* from the
   goal burden forecast. Track decision opportunity coverage/latency,
   qualified direct exposures, missed windows, and actual user slips.
4. Reconcile FT only after all frozen versions are sealed: quarter-line
   outcomes for hypothetical protected totals, actual C model exposure,
   C2 shadow counterfactual separately, actual user-bet P/L separately.
5. Evaluate goal forecasts with prospective mean absolute error and
   calibration by total-goal bins, broken out by competition and market
   centre where sample size permits. Avoid refitting to these 51 historical
   cases. Do not relax C/C2 on the basis of 8 hypothetical clears.
6. Propose a **separate** reviewed policy change only if a prospective
   sample establishes incremental quality, price-aware EV and safety of
   the alternative; until then mark `OBSERVE_ONLY`.

**Immediate priority:** real paired Step-2 decisions and timed forecasts,
not another veto, slower WAIT, or a wholesale removal of goal-three checks.
