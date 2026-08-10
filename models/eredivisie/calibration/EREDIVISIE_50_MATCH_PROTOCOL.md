# Eredivisie 50-Match Calibration Protocol

## Objective

Build the first clean, auditable Eredivisie-only sample without contaminating it with other competitions or selection-only bias.

The target is **50 completed Eredivisie matches with properly recorded model assessments**, not 50 bets.

## Sampling rule

Record every Eredivisie match materially assessed by the model from v0.1 activation onward, including:

- SHADOW selections;
- NO BET — HOLD;
- NO BET.

Do not discard matches because no bet was found. If the user selectively brings only certain fixtures, mark the sample as `user-selected` in notes rather than pretending it is schedule-complete.

## Match-level minimum record

For each match capture when available:

- date, season, round;
- home and away teams;
- promoted-team flags;
- closing home Asian handicap and representative odds;
- closing total and representative Over odds;
- halftime score;
- full-time score;
- red-card state;
- count of material assessments;
- whether a shadow selection occurred;
- whether closing-line data were captured.

## Assessment-level minimum record

Every material decision state should include:

- assessment ID;
- model version;
- exact score/minute;
- assessment period;
- reset epoch;
- candidate market/line/odds;
- goal environment;
- synchronized/reset state;
- competition utility status;
- xG role;
- primary evidence channels and count;
- favourite/underdog gate;
- directional persistence;
- major-market scan;
- settlement verification;
- validator result;
- fail/HOLD reason;
- evidence summary.

## Shadow-selection record

For every qualified shadow selection capture:

- exact selection, line, odds;
- entry minute and score;
- simulated 0.25u stake;
- settlement result and simulated P/L;
- closing line/odds when obtainable;
- CLV notes;
- process validity independent of the result;
- error classification and review notes.

## Checkpoints

At 10, 20, 30, 40 and 50 completed matches, produce a calibration review.

Minimum review dimensions:

- total assessed matches;
- number of shadow selections;
- NO BET/HOLD rate;
- shadow W/HW/P/HL/L distribution;
- simulated P/L and ROI;
- average odds;
- closing-line value coverage and direction;
- AH vs ML/DNB vs totals vs derivatives;
- favourites vs underdogs;
- handicap depth bands;
- home vs away selections;
- prematch vs live;
- score-state and entry-minute buckets;
- promoted-team subset;
- model-version split;
- process-valid versus process-invalid outcomes.

Do not interpret raw win rate without odds and settlement context.

## Rule-change discipline

Critical enforcement bugs may be fixed immediately if an existing rule was clearly violated.

Calibration changes should normally require repeated evidence rather than one outcome. Before changing the model, state:

1. observed problem;
2. supporting sample;
3. whether it is missing-rule or application/enforcement;
4. proposed correction;
5. overfitting risk;
6. exact versioned change.

## Active enforcement calibration — 2026-08-10

This is an **application/enforcement correction under existing protected-line rules**, not a new Eredivisie prior and not a model-version change.

Observed problem from the 2026-08-09 Sunday Over comparison: the model correctly identified raw goal-environment rankings, but in PEC Zwolle–Ajax and sc Heerenveen–FC Twente it moved the prematch watch from a short protected Over 2.5 to Over 3.5 largely because Over 2.5 was below the 1.70 minimum-odds floor. That improperly used the odds floor as a reason to worsen the settlement line.

Effective immediately during v0.1 calibration:

- **Minimum odds is a veto, not a line-selection instruction.** If the natural protected total is below 1.70, do not move automatically to a higher total merely to clear the floor.
- **Preserve the protected line.** A worse line such as Over 2.75, Over 3.0 or Over 3.5 must independently justify its own event budget, probability and settlement-weighted value.
- **Separate raw Over likelihood from executable Over value.** A match may rank first for expected goals while still producing no eligible shadow candidate.
- **Market shortness is prior evidence, not an independent scoring channel.** Short Over 2.5 or BTTS prices may inform the baseline but cannot by themselves establish bilateral scoring or a three-/four-goal route.
- **Bilateral labels require bilateral support.** Calling an Over environment two-sided requires an independent scoring route for each team. A one-team-driven high total is still possible, but the favourite must independently support the required multi-goal event budget.
- **Do not outcome-fit the correction.** A final score landing Over or Under does not retroactively validate or invalidate the prematch ranking. Grade the process using information available at decision time.
- **Live repricing remains independent.** If later state changes create a lower, protected total with fresh forward-looking evidence, validate that new line on its own reset epoch rather than carrying the prematch Over thesis forward.

Review this enforcement correction at the 10-match checkpoint. Escalate to an Eredivisie-specific structural rule only if repeated calibration evidence shows a league-specific pattern beyond the already inherited protected-line principle.

## Priors to estimate as sample grows

Prioritize:

- home-field scoring/margin effect;
- favourite cover and 2+ margin rates by closing AH band;
- underdog resistance/cover rates by AH band;
- closing total outcome distribution;
- 0-0 at 15/20/30/HT branch outcomes;
- 1-0 and 0-1 state continuation/comeback rates;
- second-half and late-goal rates;
- promoted-team behaviour;
- red-card branches;
- market movement/CLV.

Do not overfit advanced feature interactions before the base sample supports them.

## End-of-50 review

At 50 completed assessed matches:

- freeze the v0.1 dataset snapshot;
- audit missing/low-quality records;
- summarize process-valid shadow performance;
- compare shadow prices against closing market where available;
- identify stable league-specific priors versus unresolved features;
- recommend whether to continue shadow mode, revise to v0.2, or consider a later official-execution review.

Official execution remains disabled unless the user explicitly enables it after review.
