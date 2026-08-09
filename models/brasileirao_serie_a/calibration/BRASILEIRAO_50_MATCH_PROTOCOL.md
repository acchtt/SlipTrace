# Brazilian Serie A — 50-Match Calibration Protocol

## Objective

Build a clean initial league-specific sample before making strong performance claims or enabling official execution.

Target: **50 completed assessed Brazilian Serie A matches**.

This is a match sample, not a bet quota. NO BET and HOLD matches count when they were materially assessed and recorded.

## Inclusion criteria

Include only Campeonato Brasileiro Serie A league fixtures.

Exclude from the calibration population:

- Copa do Brasil;
- Copa Libertadores;
- Copa Sudamericana;
- state championships;
- Serie B or lower divisions;
- friendlies;
- reserve/youth matches;
- international fixtures.

Excluded competitions may be referenced only for fatigue, lineup, travel or tactical context.

## Required match-level record

For each assessed league match record, where obtainable:

- date, season and round;
- home/away teams;
- promoted-team flags;
- home/away rest days;
- midweek continental involvement flags;
- closing home Asian handicap and odds;
- closing total and over odds;
- halftime and fulltime score;
- goals and red cards;
- number of material model assessments;
- whether a shadow selection occurred;
- whether closing-line data was captured;
- travel/climate/congestion notes;
- calibration notes.

## Decision-state sample

Record material prematch and live assessment states, including NO BET and NO BET — HOLD, not only selections.

This is necessary to measure filtering quality and avoid selection-only hindsight.

## Shadow-bet sample

A shadow selection enters the Shadow Bets table only after the hard validator PASS and Decision States write.

Track:

- exact line and odds;
- 0.25u simulated stake;
- entry score/minute;
- settlement result;
- simulated P/L;
- closing line/odds where available;
- CLV notes;
- process validity independent of outcome;
- error classification.

## Review buckets

After sufficient observations, evaluate by:

- market family;
- favorite versus underdog;
- handicap depth;
- home versus away side;
- odds band;
- prematch versus live;
- entry-minute bucket;
- score state;
- promoted-team subset;
- rest-day differential;
- midweek continental involvement;
- heavy travel/congestion subset;
- model version.

## Metrics

Track at minimum:

- number of assessed matches;
- number and rate of shadow selections;
- win/half-win/push/half-loss/loss counts;
- simulated ROI and P/L;
- average odds;
- closing-line value where available;
- results and process validity by bucket;
- NO BET/HOLD frequency;
- recurring fail/hold reasons.

Do not use raw win rate alone as proof of edge.

## Model-change discipline

A single loss does not justify a new rule.

Before any version change, document:

1. observed problem;
2. number of supporting observations;
3. whether existing rules were missing or merely misapplied;
4. proposed correction;
5. overfitting risk;
6. expected affected market/state subset.

## Initial activation threshold

At 50 completed assessed matches, run a formal review. Do not automatically enable real-money recommendations. Official execution requires explicit user approval after reviewing process validity, calibration stability, CLV and sample composition.
