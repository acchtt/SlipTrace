# Football Model QA — production re-audit, October 11, 2026

**Version audited:** SlipTrace `85459b3a654afe87c9d1cd902286a74df4acaab6` (C production + independent C2 shadow only). Airtable `Daily Coverage Ledger`, `Decision States`, `Factor Calibration Observations` and `Actual Bets — Current`. No edits to frozen match judgments, markets, retrospective exposure or actual wagers.

## Executive verdict — structural selection/execution misalignment confirmed

The engine code is deterministic but **its football ranking state, supported Asian line, goal-funding proof and bookmaker decision are not aligned**. Existing improvements to Step0 scope (#110/#111), operational lanes (#109), early live (#108) and the quote-aware shadow comparator (#113) do not calibrate this model.

### Finding 1 — C rank can invert predictive FOCUS/WATCH state (CRITICAL)

`core.ranking_key()` starts with `int(clearing_goal_funded(a))`. The funding function automatically passes every supported line <=O2.0. It is not conditioned on the declared C `board_state`. `adapter.run_board()` sorts by this key *before* assigning FOCUS/WATCH/PASS and then allocates FOLLOW/RESERVE by resulting order.

On `B-20261010-2200-20261011-0600`, official C ranked:
- #1 Lille–Le Havre: **WATCH**, O2.0;
- #2 Manchester United–Tottenham: **WATCH**, O2.0;
- #3–#7: five **FOCUS**, supported O2.75–O3.0.

Thus the two WATCH positions precede all five FOCUS (10 cross-state inversion pairs). Independently, C2 ranked five FOCUS positions #1–#5 and the two WATCH #6–#7, so **C2 has zero such inversion pairs** in this board. This is not a semantic error in Python ordering; it is a concrete **model policy design conflict** if ranks are intended to prioritize FOCUS matches for coverage. Do not silently reorder historical ranks.

### Finding 2 — 0/5 own-supported-line funding, C and C2 (CRITICAL)

Exact frozen model-specific factors imply that *none* of the five C-FOCUS/FOLLOW fixtures would pass C's own `clearing_goal_funded` at its supported line. None of their C2-FOCUS counterparts would pass C2's independently frozen own-line funding logic either. Their forecast/market comparisons are:

| Fixture | C supported | C2 supported | Advisory central forecast | Observed Step1 bookmaker centre |
|---|---:|---:|---:|---:|
| Fortuna–Twente | O2.75 | O3.0 | 3.10 | 3.50 |
| Inter–Parma | O2.75 | O3.0 | 3.30 | 3.25 |
| Barcelona–Getafe | O2.75 | O3.0 | 3.40 | 3.75 |
| Leipzig–Frankfurt | O3.0 | O3.25 | 3.40 | 3.75 |
| Feyenoord–AZ | O3.0 | O3.25 | 3.70 | 3.50 |

C owns a `carrier_self_fund=false`, `continuation_quality=MEDIUM` combination on all five. C2 has `failure_resistance=MEDIUM` on all five, which prevents its O3.0+ quality gate (and Barcelona is independently borderline on C2 selection). These are **funding-readiness contradictions**, not evidence that an O3.25 was profitable at quoted odds.

The latest `follow_funding_readiness_qa.py` (PR #112) is read-only, but unless its independent frozen input is collected and invoked, the board does **not** automatically disclose this fact. This QA pass therefore adds `model_reaudit.py` to reconcile actual *paired engine board outputs* with the existing frozen-funding report, alert on cross-state inversions and 0/N funding, without modifying official decisions.

### Finding 3 — endogenous scoring forecast is not a calibrated goal distribution (HIGH)

`goal_burden_forecast.py` accepts researcher-supplied `home/away low/central/high` scenarios and checks source/prematch chronology. It does **not** estimate independent home/away scoring rates or a Poisson/negative-binomial model from a validated dataset. `declared_total` is arithmetic, not evidence of calibrated P(T>=3), P(T>=4), or positive Asian-line EV. Thus Inter's 3.30 forecast against the bookmaker 3.25 does not imply an executable advantage.

The new `step2_price_aware_shadow.py` correctly refuses to infer an EV from those forecasts; its shadow funding hypotheses have not been validated prospectively. Replacing boolean clearance tests with a bookmaker-derived mean would introduce leakage, not fix prediction.

### Finding 4 — actual quoted market above supported burden becomes terminal PASS (HIGH)

`decide_c()` and `decide_c2()` first test funding at `min(actual quote, frozen support)`. A failure returns PASS before considering whether other real price/line alternatives exist. C only supports an above-burden WAIT if `wait_reachable` is genuinely true; it cannot trade above frozen support. C2's narrow +0.25/+0.50 bridge also requires upper-tail/fourth-goal funding. The new shadow comparator observes quote-level alternatives, but is not a production trading policy and cannot invent a low-priced O2.75 when the real market is O3.25. Model selection has been found strong on a few fast-home scoring examples, yet no valid price-aware EV has been established.

### Finding 5 — exploratory historical factor signal: weak calibration coverage (HIGH)

Airtable `Factor Calibration Observations` contained 79 rows, 73 marked eligible, 57 unique fixtures after using the earliest record for each normalized fixture name + kickoff, with 51 possessing all C-factor dimensions. These are **historical, partly untimed/backfilled, selection-biased** records, not matched prospective model/quote trials.

Across all 57 eligible unique, supported line O2.25 appeared 21 times (10 eventually >=3 goals, 6 exactly 2, 5 <=1); O2.5 14 times (8 >=3), O2.0 17 times (8 >=3, 4 exactly 2); O2.75 only 3 cases (1 >=3). The richer 51-record C factor group shows:
- continuation HIGH: 5 cases, 4 reached >=3 and 4 reached >=4;
- continuation MEDIUM: 25 cases, 12 reached >=3 and 7 reached >=4;
- continuation LOW: 21 cases, 11 reached >=3 and 4 reached >=4.

These numbers are **exploratory outcome descriptions**. Very small/highly selective strata, missing independent C2 factor freezes, historical model revisions and **no matched executable odds** prohibit profitable-policy claims, confidence statements or immediate threshold changes. Notice O2.75 has only three historical fixtures: it cannot reliably calibrate third-/fourth-goal odds.

### Finding 6 — early-score successes do not establish high-total settlement (MODERATE)

Inter–Parma 2–0 around minute19 (exact goal times not attested); Leipzig–Frankfurt 2–0 at 08:17; Barcelona–Getafe 1–0 at 04:22. They justify separating **first/second-goal prediction** from **third/fourth/fifth-goal continuation**. No official C user BET was recorded for these cases, and quoted lines became obsolete after scoring. The reset-era `Actual Bets — Current` remains two confirmed historical user slips, total net -16,000 VND.

## Immediate remediation order

1. For **every new** frozen C+C2 board, compute non-blocking QA: C and C2 cross-state ranking inversions, zero-funded own-supported FOCUS lines, forecast-versus-market gap, actual offered quote coverage. Flag without delaying Step2 or inventing C/C2 actions.
2. Separately compare `C_STATE_FIRST_RANK` and existing `C_FUNDING_FIRST_RANK` as a shadow sort across future boards. A state-first production change may improve FOCUS queue order but needs a specific reviewed policy approval and regression/fairness analysis; do not silently rewrite original C ranked history.
3. Quantify 2-, 3-, 4- and 5-goal model predictions with independently timed source-backed football data and calibrated out-of-sample probabilities. Evaluate correct quarter-line push/half-win/half-loss EV at actual prices. The present numeric Step1 forecast is insufficient.
4. Trial narrower, independent C/C2 goal-three/four funding hypotheses on **prospective** matching XI/quote epochs; include adverse 0–0, 1–1 and 2–0/3–0 control endings. Never infer actual profit from an unmatched support line.
5. Preserve immediate /xi and fast-live handoff. No new background research loop or fail-closed QA gate. **Do not auto-relax official C or shadow C2 thresholds** based only on three early goal events.

### Execution and scope

This PR is a **model re-audit instrument and report**, not the threshold repair. It adds `model_reaudit.py` (requiring the true `run_board` C+C2 results plus same-board output of `follow_funding_readiness_qa.py`). Mismatched fixtures, wrong source board or fabricated funding fields fail audit; genuine FOCUS/WATCH inversions and 0/N own-line funding become advisory warnings. No source schedule/board/odds/exposure is rewritten.
