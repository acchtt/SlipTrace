# J1 League 50-Match Calibration Protocol

## Objective
Build the first league-specific J1 sample without selection bias or contamination from other competitions.

## Sample definition
Target: **50 completed J1 League matches that received at least one material model assessment**. The target is assessed matches, not bets. NO BET matches count if they were properly assessed and recorded.

Do not include J2, J3, Emperor's Cup, J.League Cup, AFC competition, friendlies, reserve/youth or national-team matches in the J1 sample.

## Required match record
For each sampled match capture, where available:
- date, season, round;
- home/away teams and promoted status;
- relevant rest days and midweek cup/AFC context;
- closing home AH and odds;
- closing total and over odds;
- HT/FT score and goals;
- red cards;
- number of material assessments;
- whether a qualified shadow selection occurred;
- whether closing-line data was captured;
- travel/weather/congestion notes;
- calibration notes.

## Assessment record
Every material prematch/live assessment must have a Decision States entry. Record NO BET/HOLD/FAIL states as well as PASS states.

## Shadow record
Only validator-PASS candidates enter Shadow Bets. Default simulated stake is exactly 0.25u. Record entry state, result, simulated P/L, closing line/odds when available, CLV notes, process validity and error classification.

## Minimum analyses after sample growth
Track at least:
- hit/push/half-win/half-loss rates;
- ROI and simulated P/L;
- average odds;
- CLV proxy when captured;
- market family;
- handicap/total band;
- favorite vs underdog;
- home vs away;
- prematch vs live;
- entry-minute buckets;
- score-state buckets;
- promoted-team subset;
- rest/congestion subset;
- heat/weather subset when material;
- model version.

## J1 priors to estimate
As the sample grows, estimate cautiously:
- home-field effect;
- goal and draw distributions;
- favorite one-goal vs 2+ margin rates;
- protected-underdog cover rates;
- totals by closing line;
- 1H/2H and late-goal behavior;
- red-card response;
- score-state hazard;
- travel/rest/congestion modifiers;
- summer heat/humidity effects;
- promoted-team performance.

## Overfitting control
Do not promote a league-wide rule from one match. Before changing the active child rules, distinguish:
1. missing rule;
2. failure to apply an existing rule;
3. calibration error;
4. normal variance.

Document sample support and the risk of overfitting for every proposed rule change.

## Review points
Perform structured reviews at approximately 10, 25 and 50 completed assessed matches. Early reviews are diagnostic; they do not justify strong profitability claims.

## Activation rule
Reaching 50 matches does not automatically enable official betting. After the 50-match review, official execution remains disabled until the user explicitly approves activation and any required model-version change is documented.
