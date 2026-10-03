# Football Factor Calibration Observer

**Status:** PROSPECTIVE DIAGNOSTIC OBSERVER — ZERO PRODUCTION AUTHORITY  
**Parent:** Football C production  
**Purpose:** detect persistent over-weighting / under-weighting of frozen Football C factors without changing historical grades after FT.

## 1. Core rule

This observer answers:

> When Football C ranks two otherwise viable fixtures differently, which frozen factors repeatedly improve or damage out-of-sample selection quality?

It does **not** answer:

> Which factor should be changed because the last losing match looked wrong after FT?

No predictive rule changes are allowed from a single result.

## 2. Eligible observations

A factor-calibration observation is eligible only when:

- the Football C board was frozen before kickoff;
- the factor values being tested existed prospectively in that frozen state;
- fixture identity and supported line are preserved;
- FT result is known;
- the fixture was not subsequently re-graded from outcome knowledge.

Historical boards may contribute only the factors they actually froze at the time.

Do **not** backfill:
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- carrier self-fund;
- independent upper tail;
- failure/suppression flags

when those values were not prospectively frozen for that board.

Such a fixture may remain useful for older-factor diagnostics but is `INELIGIBLE` for any missing new factor.

## 3. Frozen factor vector

Where prospectively available, preserve:

- C board state;
- C rank;
- FOLLOW / RESERVE / STOP;
- supported line;
- home route;
- away route;
- carrier strength;
- carrier self-fund;
- independent upper tail;
- route reliability;
- independent route quality;
- chance quality;
- failure resistance;
- XI robustness;
- evidence confidence;
- burden protection;
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- failure attacks route;
- material suppression.

Never edit this vector after FT.

## 4. Observed labels

After FT, add only outcome labels:

- total goals;
- frozen-support settlement = WIN / HALF_WIN / PUSH / HALF_LOSS / LOSS;
- completion materialized = YES / NO / UNKNOWN;
- continuation materialized = YES / NO / UNKNOWN;
- carrier self-fund materialized = YES / NO / UNKNOWN / NOT_APPLICABLE;
- opponent route materialized = YES / NO / UNKNOWN / NOT_APPLICABLE;
- stall endpoint observed = YES / NO / UNKNOWN;
- same-kickoff priority inversion = YES / NO / UNKNOWN.

These are observations, not retrospective factor grades.

## 5. Diagnostic contribution trace

The observer computes a **trace score** solely to expose which factors the current model is implicitly favoring.

The trace score is deliberately simple and non-authoritative:

- burden completion: HIGH +2, MEDIUM +1, LOW +0;
- continuation: HIGH +2, MEDIUM +1, LOW +0;
- stall risk: LOW +2, MEDIUM +0, HIGH -2;
- carrier self-fund: true +1;
- independent upper tail: true +1;
- independent second route: weaker route STRONG +1, USABLE +0.5, WEAK +0;
- failure attacks route: true -1;
- material suppression: true -1.

The trace score:
- does not replace Football C's lexicographic ranking;
- does not decide C-PASS/WATCH/FOCUS;
- does not decide FOLLOW/RESERVE/STOP;
- does not alter supported line;
- does not authorize BET/WAIT;
- does not create Website Picks.

Its only purpose is to make implicit factor emphasis inspectable.

## 6. Calibration diagnostics

Run these separately.

### A. Factor bucket performance

For each frozen factor level, report:
- eligible N;
- support-clear rate;
- support-fail rate;
- average goals minus supported line;
- continuation-materialization rate where applicable;
- stall-endpoint rate where applicable.

Never compare a factor with fewer than 5 eligible observations as a stable signal.

### B. Same-kickoff priority inversion

For exact same-kickoff groups, compare the frozen ordering against outcomes.

Flag only when:
- a higher-ranked fixture failed its frozen support; and
- a lower-ranked otherwise eligible fixture cleared its frozen support.

This is a **priority inversion observation**, not proof that the lower-ranked fixture should have been selected.

### C. Ablation replay

Using the same prospectively frozen vectors, recompute ranking with one diagnostic factor omitted.

For each factor:
- count rank changes;
- count same-kickoff top-choice changes;
- compare support settlement of original versus ablated top choice.

Ablation is diagnostic only. It cannot rewrite the historical board.

### D. Conflict matrix

Track interactions rather than only single factors:

- continuation x stall risk;
- carrier self-fund x supported burden;
- second-route strength x carrier strength;
- completion quality x supported burden;
- failure resistance x completion quality.

This is mandatory because a factor may look good alone but fail in a specific interaction.

## 7. Overweight / underweight candidate rules

A factor becomes an `OVERWEIGHT CANDIDATE` only when, over a prospective eligible sample:

- N >= 20 overall for that factor family;
- at least 5 observations in the relevant level/bucket;
- it repeatedly causes priority inversions or negative ablation delta;
- the pattern appears across at least 3 separate boards;
- no single competition contributes more than 40% of the evidence;
- the result is not explained by a known process/integrity fault.

A factor becomes an `UNDERWEIGHT CANDIDATE` under the mirror condition:
- removing/lowering it worsens selection;
- or promoting its influence would have repeatedly improved same-kickoff ordering using only frozen information.

Until these thresholds are met:
`CALIBRATION SIGNAL — OBSERVE ONLY`

## 8. Production-change boundary

Do not modify Football C directly from the observer.

If a stable candidate emerges:
1. write the exact prospective rule change;
2. freeze it into a new challenger/version;
3. run paired prospective boards against Football C;
4. promote only after the predeclared comparison threshold is met.

No silent coefficient tuning inside Football C.

## 9. Airtable persistence

Use `Factor Calibration Observations`.

One row per fixture per frozen board.

The row stores:
- immutable frozen vector;
- post-FT observed labels;
- trace score;
- eligibility / contamination reason;
- board identity.

Audit may append outcome fields after FT but must never alter frozen factor columns.

## 10. Current bootstrap boundary

The observer activates at the merge commit that introduces this procedure.

Earlier boards may be imported only when:
- the exact frozen factor exists in the historical artifact;
- no retrospective inference is required.

New burden-completion fields must never be backfilled onto older boards that did not freeze them.

Bootstrap evidence is descriptive and carries zero authority to change Football C.
