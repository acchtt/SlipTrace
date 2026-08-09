# Eredivisie 50-Match Calibration Protocol v0.1

**Status:** Initial shadow-calibration protocol  
**Target:** At least 50 properly assessed eligible Netherlands Eredivisie matches  
**Execution:** No real-money official bets

## 1. Objective

The first 50-match run is a calibration and process-validation sample, not a target of 50 wagers.

The run should determine whether the SlipTrace core process, when supplied with Eredivisie-only priors, is well calibrated across league-specific home/away scoring, draw, margin, total-goal and live score-state distributions.

Most matches may correctly produce `NO BET` or `NO BET — HOLD`.

The protocol must preserve those outcomes. Recording only successful-looking candidates would create selection bias and make model evaluation unreliable.

## 2. Match inclusion

Count unique matches, not assessments and not bets.

An eligible match must have:

- verified competition = Netherlands Eredivisie;
- verified home and away teams;
- verified date and venue/home-away designation;
- sufficient information for at least one proper assessment under the active parent model;
- a corresponding `Eredivisie Matches` record.

Exclude from the calibration universe:

- KNVB Cup;
- UEFA competitions;
- friendlies;
- Eerste Divisie;
- reserve/youth football;
- international matches;
- other competitions involving Eredivisie clubs.

If competition membership is ambiguous, do not count the match until verified.

## 3. Sampling discipline

Use a consecutive-observation principle rather than cherry-picking attractive betting fixtures.

The default v0.1 sample is the first 50 eligible Eredivisie matches assessed after project activation for which the required state can be verified.

A match may be skipped only for a documented operational reason, such as:

- competition identity cannot be verified;
- required market/state data are unavailable;
- match is abandoned or materially altered such that ordinary settlement is not comparable;
- duplicate record;
- another explicit data-integrity failure.

Every skip must be logged with the exclusion reason. Do not skip a match merely because no wager appears attractive.

## 4. Minimum assessment per match

Each counted match requires at least one properly logged prematch assessment unless the match enters the dataset as a pre-declared live-only observation with an explicit reason.

The prematch assessment must include:

- exact match identity and league verification;
- home/away designation;
- confirmed or classified expected lineups;
- injuries/suspensions when available;
- current Asian handicap and total;
- relevant home/away scoring and conceding profiles;
- independent team-strength decomposition for both teams;
- tactical/lineup matchup;
- win/draw/margin utility where relevant;
- complete major-market scan;
- validator result;
- final verdict.

Prematch previews include recent relevant home/away form and relevant competitive H2H at low weight.

## 5. Live-assessment coverage

The 50-match target does not require live coverage of every match. However, live observations must not be selected retroactively because the match became exciting or a price looked attractive.

When a match is designated for live monitoring, record that intention before or at the start of live coverage and follow the active parent assessment-period rules.

Preferred normal checkpoints, when reliable live data and markets are available, are:

- 20'–35' primary recommendation window;
- halftime–60' tactical repricing window;
- 65'–78' selective late window when conditions justify continued observation.

These are observation checkpoints, not mandatory wagering points.

Every material event still creates a reset epoch. Goals, penalties, red cards, major injuries, tactical changes, substitution clusters, halftime and material weather/pitch changes require fresh state handling under the parent model.

Do not carry a pre-reset Open/Neutral/Closed classification forward automatically.

## 6. Decision process at every material assessment

For each prematch assessment and material live reassessment:

1. synchronize match identity, score, minute/phase, events, line, odds and settlement scope;
2. establish/reset the current epoch;
3. verify competition format and result/margin utility when relevant;
4. evaluate both teams using independent forward-looking evidence;
5. keep xG/xGOT secondary only;
6. establish directional persistence when required;
7. apply favourite/deep-favourite/protected-underdog gates where relevant;
8. scan all major available market families independently;
9. compute exact settlement and event-budget branches;
10. choose one best expression or none;
11. create the parent `Decision States` record;
12. run the hard validator;
13. create the linked `Eredivisie Assessments` record;
14. output the verdict.

Validator semantics remain:

- `PASS` -> candidate may become `SHADOW LEAN — DO NOT PLACE`;
- `HOLD` -> `NO BET — HOLD` and state the exact unlock condition;
- `FAIL` -> `NO BET`.

No candidate may be promoted around the validator.

## 7. Shadow-selection rules

A qualified shadow selection is:

`SHADOW LEAN — DO NOT PLACE`

Rules:

- exactly 0.25u simulated stake;
- 1u inherits the parent unit definition; at v0.1 creation 1u = 1,000,000 VND;
- minimum odds inherit the parent minimum; at v0.1 creation minimum accepted odds = 1.70;
- do not scale stake with confidence;
- normally one best expression per assessment point;
- at most one designated primary shadow selection per match for match-level headline performance reporting, while additional material assessments still remain in the dataset as assessments;
- if the parent four-match football circuit breaker is still active, also satisfy its separate Circuit Breaker record requirements.

The 50-match calibration run does not automatically restore official betting after completion.

## 8. Information-leakage control

Assessment data must be frozen at the assessment timestamp.

Do not use later information to improve an earlier record, including:

- final score;
- closing line;
- later lineup changes;
- later injury information not known at entry;
- later tactical developments;
- post-match explanations.

Post-match fields are appended separately after the event.

A correct outcome produced by an invalid process remains process-invalid. A loss produced by a valid process remains process-valid unless review identifies an actual rule or calibration failure.

## 9. Post-match settlement

After the result is verified, update:

- eventual result;
- exact shadow-selection settlement;
- simulated P/L in units;
- closing line and closing prices when reliably available;
- process validity;
- failure classification when applicable;
- review notes.

Quarter-line settlement must preserve full-win, half-win, push, half-loss and full-loss distinctions.

Do not grade an Asian handicap from the final winner alone.

## 10. Closing-line value protocol

Track CLV without manufacturing comparability across different lines.

Use three layers:

### A. Same-line price CLV

When the exact entry line is still quoted at close, compare entry price with closing price on that same line.

Store the raw entry odds and same-line closing odds. A favorable move is one in which the market makes the selected side more expensive / lower decimal odds at close relative to entry, after confirming the same settlement line.

### B. Line CLV

When the handicap or total moves, record the quarter-goal movement in the direction of or against the selection.

Example categories should remain descriptive rather than forcing a synthetic probability conversion when no same-line close exists.

### C. CLV classification

Record:

- Favorable;
- Neutral;
- Adverse;
- Unavailable.

Do not collapse line movement and same-line price movement into one precise CLV score unless a later calibrated conversion is explicitly validated.

## 11. Required performance cuts

At review, analyze assessment and shadow-selection performance by at least:

- market family;
- favourite/underdog;
- handicap depth;
- home/away;
- prematch/live;
- entry minute or assessment period;
- score state;
- odds band;
- promoted-team involvement;
- parent football version;
- Eredivisie model version.

Also examine:

- validator PASS/HOLD/FAIL rates;
- NO BET rate;
- HOLD unlock quality;
- process-validity rate;
- CLV availability and direction;
- protected-underdog performance;
- deep-favourite margin calibration;
- total-goal event-budget performance.

Win rate alone is insufficient.

## 12. League-prior measurements

The first run should collect enough raw data to begin estimating, with uncertainty:

- home goals distribution;
- away goals distribution;
- home-field effect;
- draw rate;
- first-half and second-half scoring;
- late-goal frequency;
- 0-0 at 15/20/30/HT outcomes;
- 1-0 and 0-1 score-state outcomes;
- comeback rates;
- closing Asian handicap;
- favourite result by handicap band;
- favourite exactly-one and 2+ margin rates;
- underdog protection rate;
- totals by closing line;
- goal hazard by minute;
- promoted-team performance;
- red-card effects;
- goalkeeper/personnel effects when observable;
- substitution effects;
- closing-line movement.

Fifty matches are not enough to treat every subgroup as independently stable. Sparse cohorts must remain provisional and use wider uncertainty rather than false precision.

## 13. Review checkpoints

### After 10 counted matches

Perform a data-quality audit only:

- Are all matches correctly classified as Eredivisie?
- Are NO BET decisions being recorded?
- Are parent Decision States links present?
- Are closing fields being appended rather than overwriting entry data?
- Are reset epochs and assessment periods consistent?

Do not rewrite football betting rules because of short-run P/L.

### After 25 counted matches

Perform an interim calibration audit:

- distribution completeness;
- missing-data patterns;
- favourite/underdog balance;
- prematch/live coverage balance;
- market-family representation;
- early evidence of gross calibration drift.

Only fix clear data, application or enforcement defects. Do not promote fragile numerical priors merely because an early cell looks extreme.

### After at least 50 counted matches

Perform the formal v0.1 review.

For each major proposed change ask:

1. Was a parent/core rule missing?
2. Was an existing rule present but not applied?
3. Is the problem genuinely Eredivisie-specific calibration?
4. Is the evidence robust across multiple matches and relevant cohorts?
5. Would the proposed correction have been defensible before observing the outcomes that motivated it?

No official execution is enabled automatically at this checkpoint.

## 14. Failure taxonomy

Classify reviewed failures as one of:

- application/enforcement failure;
- probability calibration error;
- margin error;
- favourite bias;
- underdog bias;
- xG misuse;
- reset violation;
- persistence violation;
- lineup error;
- tactical error;
- settlement error;
- market-selection error;
- competition-universe/data error.

A losing wager does not itself identify the category. Review the pre-entry process.

## 15. Prior-promotion discipline

A derived Eredivisie statistic becomes an active prior only when:

- the source cohort is clearly defined;
- match count and effective sample are recorded;
- the estimate is not dominated by one team, one red-card cluster or one extreme score;
- home/away and closing-market context are understood where relevant;
- uncertainty is documented;
- activation is written into a versioned Eredivisie model/prior snapshot.

Until then, the estimate remains experimental.

Do not replace sparse league evidence with a generic football number without explicitly marking the fallback and its uncertainty.

## 16. Completion criteria

The initial calibration run is complete only when:

- at least 50 unique eligible Eredivisie matches have been properly assessed;
- every counted match has a match record;
- every material assessment has an Eredivisie assessment record;
- NO BET and HOLD outcomes are preserved;
- qualified shadow selections are settled;
- closing-line information is captured where available;
- process validity is reviewed;
- the formal 50-match report is completed.

Completion of the sample is evidence for review, not evidence that the model is automatically ready for real-money betting.

## 17. Governing principle

**Same SlipTrace decision process; narrower league-specific calibration.**
