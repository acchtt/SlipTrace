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
