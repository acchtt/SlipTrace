# Model Rules — J1 League v0.1

## Status

Initial child-model rules for J1-specific calibration. These rules sit on top of the frozen SlipTrace Football v0.2.41 process skeleton.

## Scope

Only J1 League matches enter the calibration population. Other Japanese or continental competitions are contextual only unless explicitly separated into another dataset.

## Operating mode

- Shadow calibration only.
- Positive output: `SHADOW LEAN — DO NOT PLACE`.
- Other outputs: `NO BET — HOLD` or `NO BET`.
- 1u = 1,000,000 VND.
- Minimum odds = 1.70.
- Qualified shadow = exactly 0.25u simulated.
- No official real-money recommendation until explicitly activated after review.

## Universal controls inherited unchanged

Use the frozen parent for synchronization, reset handling, evidence hierarchy, xG/xGOT restrictions, correlated-evidence control, persistence, market scan, settlement, one-best-expression, favorite/underdog gates and pre-verdict validation.

## J1-specific calibration priorities

Do not assume generic football priors when J1 evidence becomes available. Estimate and update:
- home-field effect by club/venue where sample permits;
- home/away goal distributions;
- handicap-band win/push/cover rates;
- favorite 2+ margin frequency;
- draw/clean-sheet rates;
- totals by closing line;
- 1H/2H and late-goal rates;
- goal hazard by minute and score state;
- promoted-team behavior;
- rest/travel asymmetry;
- heat/humidity/weather effects;
- rotation and congestion from Emperor's Cup, J.League Cup and AFC commitments;
- lineup/goalkeeper effects;
- market movement and CLV.

## Prematch evidence

For each team independently assess:
- opponent-adjusted attack and defense;
- relevant home/away splits;
- chance quality and box access;
- transition attack/defense;
- set pieces;
- goalkeeper and centre-back stability;
- confirmed/expected lineup quality;
- bench depth;
- tactical matchup;
- rest/travel/congestion;
- weather/heat if material.

Recent results support but do not define the thesis. H2H is low weight.

## Win versus margin

Never translate stronger team directly into deep negative handicap. Explicitly separate win probability, draw probability, one-goal win probability and 2+ margin probability.

For protected underdogs, attacking threat is separate from defensive margin suppression. Handicap protection itself is not evidence.

## Live model

Every goal, penalty, red card, major injury, substitution cluster, halftime, tactical shift or material weather/pitch change creates a new reset epoch. Set goal environment to `Unresolved` until post-reset evidence establishes Closed, Neutral or Open.

One dangerous event does not establish persistence.

## Evidence

Primary forward-looking channels include box/central access, big chances, dangerous transitions/cutbacks, high-value shot locations, persistent box touches, set-piece pressure, defensive degradation and tempo/persistence.

Possession, raw shots and SOT without location/quality context are supporting only. xG/xGOT are secondary diagnostics and cannot independently create a bet.

Counterfactual: if xG/xGOT disappeared, the thesis must still exist.

## J1 context rule

Travel, heat/humidity and congestion can modify priors only when verified and materially asymmetric. Do not use generic 'Japan heat' or 'long travel' narratives without actual context.

## Market scan

At each material assessment independently compare available major market families: AH/sides, ML/DNB where available and totals; team totals/corners only when sufficiently supported. Do not anchor to the first market shown.

## Dataset and review

Record NO BET assessments as well as selections. After losses, distinguish normal variance from application/enforcement, calibration, margin, favorite/underdog bias, xG misuse, reset/persistence, lineup, tactical, settlement, market selection, travel/congestion and weather/heat errors.

Do not add a new rule from a single result unless an existing safety control is demonstrably missing.
