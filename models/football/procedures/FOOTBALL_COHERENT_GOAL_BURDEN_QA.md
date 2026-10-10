# Football C/C2 — coordinated ranking, goal-tail and Asian-total QA pass

**Date:** 2026-10-11. **Scope:** new prospective boards only; Football C official, C2 shadow, no C3/C4 revival. Ref: re-audit `models/football/qa/2026-10-11_FULL_MODEL_REAUDIT.md`.

## Coordinated changes

**1. Correct operationally useful C board ranking.** For official C `adapter.run_board()`, sort by declared FOCUS/WATCH/PASS before the pre-existing `ranking_key` inside each state. Prevent mechanical O2.0 WATCH first when stronger FOCUS fixtures have larger yet not-fully-funded totals. Keep score evidence, qualitative supported burden, all within-state funding rankings, same-kickoff allocation (<=2 FOLLOW), global lane capacity and C2's independently frozen ranking unaffected. `xi_portable.py` is regenerated from the changed adapter with source Git blob SHA verified; run pinned self-check. No retroactive overwrite of last October 10 board or past rank ledgers. New official ranking policy: `FOOTBALL_C_FOCUS_FIRST_BURDEN_COMPLETION`.

**2. Establish an explicitly reproducible independent goal distribution research baseline, not a sports-betting oracle.** `goal_total_probabilities.py` ingests 6–30 publicly sourced *home games* for the upcoming home side and 6–30 *away games* for the upcoming away side, each with actual final GF/GA, individual identity and historical kickoff proof. It computes:

- Home goal intensity = (home team's home GF/game + visitor's away conceded/game) / 2.
- Away goal intensity = (visitor's away GF/game + home team's home conceded/game) / 2.
- With *independent Poisson* assumptions, total goals is Poisson with mean sum of those intensities. Return P(goals >= 3), >= 4, >= 5 and the full count distribution to 24.

These are **assumptions**, not validated football probabilities. Venue/game samples have no competition-strength, xG, league-baseline, opponent or squad adjustments. Sparse match samples cannot support reliable actual Asian market value. Do **not** assign the resulting rates to Football C, pretend a book's 3.5 total equals a goal mean, or copy C's forecast into C2's independent challenger.

**3. Audit actual quotes with quarter-line payoffs.** The probability module accepts optional source-verified actual prematch Asian Over quotes no older than 120 seconds; no quote -> no price conclusion. For each quote, it reports exact win/half-win/push/half-loss/loss settlement by goal count and a *model-conditional unit-profit estimate*. It has `positive_ev_established=false`, `bet_authorized=false` regardless of sign. A positive mathematical output is not calibrated EV or an action. The paired, unmodified Step2 `step2_price_aware_shadow.py` still independently compares each C/C2 gate against genuine supported quotes and does not manufacture unoffered lines.

**4. Validate before changing thresholds.** Run `goal_total_probabilities.py --mode holdout` on **independently recorded pre-KO estimates** whose 3+/4+/5+ probabilities were committed before kickoff; merge only actual final totals observed postmatch. Require at least 100 unique prospectively frozen fixtures before even declaring minimum review sample; show Brier scores, mean predicted and observed rate per threshold. This is only the start: league/venue stratification, odds source reliability, independent C and C2 holdout, and real quote-conditional settlement are additionally needed for any production threshold proposal. Never optimize rules to October 10's reported early goals or the partly backfilled Airtable calibration sample.

## Commands / evidence

```bash
python models/football/engine/xi_portable.py self-check
python -m unittest discover -s models/football/engine/tests -v

python models/football/engine/goal_total_probabilities.py --mode estimate \
  --input pre_ko_team_history.json --output probability_research.json

python models/football/engine/goal_total_probabilities.py --mode holdout \
  --input sealed_prospective_predictions_with_later_ft.json \
  --output validation_report.json
```

Input `schema_version=football-goal-probability-experiment-v1`, `market_independent_inputs=true`, original match identity and source epoch, freeze/assessment/KO UTC times, `home` and `away` records with public HTTPS `source_url`, `observed_at_utc`, and **venue_matched_games** (unique `fixture_id`, `kickoff_utc`, `venue=HOME/AWAY`, actual `goals_for`, `goals_against`). `quotes` optional (up to 20) with `market_phase=PREMATCH`, `line`, `decimal_odds`, source and UTC observation. The field name `forecast_total` is deliberately not an input: estimation is based on historical actual goals, not another researcher-provided guess.

For holdout input use `schema_version=football-goal-probability-holdout-v1` and `sealed_matches[]` with match ID, pre-KO frozen time, kickoff time, result observation time, actual total goals and **previously frozen** P(>=3), P(>=4), P(>=5). The script checks chronology and duplicates but cannot cryptographically prove external provenance: the audit record must bind the actual original forecast hash and saved independent freeze evidence.

## Safety / unresolved

- Original C/C2 execution goal-three/four gates **unchanged**. No automatic BET, WAIT, greater supported total or higher exposure.
- No new official P/L or user Actual Bets. No frozen records rewritten.
- Fast /xi and early-live route unaffected. The probability module is optional research, not a new heavy or blocking XI stage.
- The 0/5 own-supported-line discrepancy remains an **explicit unresolved calibration issue**. Fixing ranking does not fix goal-3 funding; the probability experiment is infrastructure for out-of-sample testing, not proof to relax the rule.
- Future candidate-goal distribution must be validated before optimizing for 1–1 stalls, rapid 2–0 leads, late 3rd/4th goals and bookmaker value.
