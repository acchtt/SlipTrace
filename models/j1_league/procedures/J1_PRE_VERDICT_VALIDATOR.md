# J1 League Hard Pre-Verdict Validator

Run before every positive shadow selection. A candidate may become `SHADOW LEAN — DO NOT PLACE` only if all applicable gates pass and the Airtable Decision States record is successfully written.

## Gate 1 — Synchronized state
Verify exact match, competition, venue, home/away, current score, minute, current line and odds. Do not combine stale stats with fresh prices as one state.

## Gate 2 — Reset epoch
If a goal, penalty, red card, halftime, major injury, substitution cluster, tactical change or material weather/pitch event occurred, create a fresh epoch. Do not carry the prior regime through the reset.

## Gate 3 — Competition and utility
Confirm this is a J1 League match for calibration. Verify relevant result/margin utility. Do not silently mix cup or continental context into league priors.

## Gate 4 — xG/xGOT role
xG/xGOT must be `Secondary Only` or `Not Used`. If the thesis disappears without xG/xGOT, FAIL.

## Gate 5 — Independent primary evidence
When a live directional thesis requires evidence, require at least two genuinely independent primary forward-looking channels. Avoid double-counting correlated statistics such as xG + shots + SOT from the same events.

## Gate 6 — Persistence/regime consistency
One event cannot establish a persistent attacking regime. After reset, classify goal environment as `Unresolved` until sufficient new evidence exists.

## Gate 7 — favorite / margin / underdog validation
For favorite handicaps, establish margin capability separately from win probability. For protected underdogs, require affirmative defensive margin-suppression evidence and test the favorite-first-goal branch. Handicap protection, formation labels, possession and generic draw narratives are not sufficient.

## Gate 8 — J1 contextual modifiers
If rest, travel, heat/humidity, weather or cup/AFC congestion is material to the thesis, verify it and assess whether it is asymmetric. Generic contextual narratives cannot be the primary edge.

## Gate 9 — major-market scan
Independently scan the currently available major families: AH/sides, ML/DNB when available, totals, and other sufficiently supported markets. Do not anchor to the previously discussed candidate.

## Gate 10 — exact settlement / event budget
For AH and quarter lines, understand full win, half win, push, half loss and full loss. For live markets distinguish full-match from remaining-match settlement. For totals state the additional goals needed for each settlement branch.

## Gate 11 — output mode and price
Odds must be at least 1.70. Shadow mode only. One best expression per assessment point. Qualified simulated stake is exactly 0.25u.

## Gate 12 — Airtable write lock
Create/update the J1 `Decision States` record before promotion. `Validator Result` must be `PASS`. Then create the `Shadow Bets` record.

If Airtable is unavailable: `NO BET — HOLD — decision-state validation unavailable`.

## Outcomes

### PASS
Candidate may be output as `SHADOW LEAN — DO NOT PLACE` after the required writes.

### HOLD
Output `NO BET — HOLD` and state the exact evidence/price/state required to unlock reassessment.

### FAIL
Output `NO BET`. Do not promote the candidate around the validator.
