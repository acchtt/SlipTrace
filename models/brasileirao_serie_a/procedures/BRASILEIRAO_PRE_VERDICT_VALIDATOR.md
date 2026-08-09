# BRAZILIAN SERIE A PRE-VERDICT VALIDATOR

Mandatory before any positive child-model selection.

## Result semantics

- `PASS`: all mandatory gates satisfied; candidate may become `SHADOW LEAN — DO NOT PLACE`.
- `HOLD`: thesis plausible but required state unresolved/stale; output `NO BET — HOLD`.
- `FAIL`: mandatory gate contradicted/violated; output `NO BET`.

No candidate may be promoted around HOLD or FAIL.

## Gate 1 — synchronized state

Verify current match identity, score, minute/phase, material events, candidate line/odds and settlement scope. Any assumed current state = HOLD.

## Gate 2 — reset epoch

Check goals, penalties, red cards, injuries, substitution clusters, halftime, tactical changes and material weather/pitch changes. After a reset, old regime/direction does not carry forward. Insufficient post-reset evidence = HOLD with Goal Environment `Unresolved`.

## Gate 3 — competition and result utility

Confirm this is a Brazilian Serie A league match. Apply table/result utility when relevant: win, draw, margin/goal-difference, relegation/title/continental-place incentives and conservation. Do not convert motivation narrative into edge without a probability mechanism.

## Gate 4 — lineup, rest, travel and congestion

Verify known lineup/availability information and assess rest-day asymmetry, midweek continental/cup involvement, rotation and material travel/climate burden. If a candidate depends on one of these and evidence is unresolved, HOLD.

## Gate 5 — xG/xGOT role

Set xG Role to `Secondary Only`, `Not Used`, or `Violation`. If removing xG/xGOT collapses the thesis, result = FAIL.

## Gate 6 — independent primary evidence

For live candidates identify at least two independent primary forward-looking channels, subject to stricter inherited rules. Possession, raw shots, SOT, xG and xGOT alone cannot satisfy the minimum.

## Gate 7 — persistence and regime consistency

Directional switches, favorite fades and goal-environment changes require persistent comparable evidence. One event cannot establish a regime. Contradiction or retrospective rewriting = HOLD/FAIL.

## Gate 8 — favorite, margin and underdog controls

For favorite handicaps, establish margin capacity separately from win probability.

For protected underdogs against material favorites, require affirmative defensive margin suppression and run the favorite-first-goal branch. Attacking threat, formation labels and nominal protection do not suffice.

## Gate 9 — Brazilian Serie A prior integrity

Any league prior used must be based on a clearly identified child calibration source or reliable historical Serie A data. If sample quality is inadequate, widen uncertainty. Do not import a generic football prior as though it were Serie A-specific.

## Gate 10 — market-family scan

Reassess all available major families relevant to the state, at minimum sides/AH, moneyline/DNB where relevant and totals. Compare the candidate against the best alternative expression. Incomplete scan = HOLD.

## Gate 11 — settlement and event budget

Verify exact settlement, minimum odds >=1.70, quarter-line outcomes and live full-match versus remaining-match scope. For totals, calculate the remaining event budget from the current score. Any unresolved settlement issue = HOLD/FAIL.

## Gate 12 — Airtable write lock and output mode

Before a positive verdict, write the Decision States record in base `appsqiBbCMEKKLqgG` and require `Validator Result = PASS`. Then create the Shadow Bets record.

Positive output is only `SHADOW LEAN — DO NOT PLACE`, simulated 0.25u. Official execution is disabled.

If Airtable is unavailable, output `NO BET — HOLD — decision-state validation unavailable`.

## Compact response behavior

Keep user-facing live responses brief and decision-first. Always include `Assessment period: ...`. On HOLD/FAIL, state only the decisive unresolved/failed gate and the concrete unlock condition.
