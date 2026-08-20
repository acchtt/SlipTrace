# SlipTrace CS2 Shadow Model

Effective: 2026-08-20
Current version: **v1.1**

Purpose: define the durable pre-match CS2 decision model used for shadow testing. Official placed wagers remain separate from this model and are not written to `ledger.json` unless the user explicitly confirms a real wager and authorizes the ledger write.

## Operating window

1. Build and preserve a **pre-veto baseline** before map picks are known.
2. Issue counted shadow selections only **after the complete BO3 veto/map order is known and before round 1 begins**, using the user's actual available odds.
3. Live prices after the first round starts are analysis-only and must not be retroactively counted as shadow bets.
4. Airtable `SlipTrace CS2 Decision Control` is the audit layer for pre-veto forecasts, counted shadow bets, and post-match reviews.

## Probability framework

Start from series-strength priors, then update for:
- current five-man lineup quality and sample size;
- recent LAN form and opponent quality;
- star/entry/AWP differential;
- map-pool depth and veto flexibility;
- expected first-pick strength;
- expected decider strength;
- direct matchup evidence, downweighted when lineups differ materially;
- bookmaker price only after the independent model probability is established.

## v1.1 calibration changes

Introduced after Falcons 2-0 The MongolZ and Legacy 2-0 NAVI at EWC 2026.

### 1. Underdog-pick restraint

Do **not** automatically treat an underdog receiving a preferred map as sufficient evidence for +1.5 maps or Over 2.5.

Before upgrading an underdog map-cover probability, explicitly estimate the favorite's probability of winning the underdog's pick. Increase the sweep probability when:
- the favorite has an elite cross-map team-strength advantage;
- the favorite's current five is materially stronger in individual quality;
- the underdog's preferred-map edge is based on a small or soft-opposition sample;
- the favorite has demonstrated recent wins on the opponent's preferred map or has strong tactical flexibility.

A split-looking veto is not, by itself, evidence of a three-map series.

### 2. Two-of-three veto swing

Apply a larger post-veto probability shift when the underdog receives **two structurally favorable maps** among the three: one strong pick plus a favorable/low-sample decider.

Do not stay anchored to the pre-veto favorite. If two maps move materially toward the underdog, a favorite may move from clear favorite to near coin flip or underdog.

### 3. Decider uncertainty penalty

A low-sample or frequently-banned decider for the favorite carries a stronger uncertainty penalty than in v1.0. Cache and other newly reintroduced/low-sample maps require especially conservative assumptions.

### 4. Favorite sweep term

For top-tier favorites, model P(2-0) separately instead of deriving it mechanically from series win probability. A strong favorite can have meaningful 2-0 equity even when the opponent has a credible map pick.

### 5. Lineup continuity weighting

Downweight old H2H and old map records when either team has changed two or more players or the current five has a small map sample. Current-lineup LAN evidence has priority over long-run team-name history.

## Market rules

For every candidate market calculate:
- offered decimal odds;
- implied probability = 1 / odds;
- model probability;
- fair odds = 1 / model probability;
- edge in percentage points = model probability - implied probability;
- expected value per 1u = model probability * (odds - 1) - (1 - model probability).

Prefer NO BET when the model edge is weak or depends mainly on uncertain veto assumptions. During the test phase, avoid forcing action merely to increase sample size.

## Review discipline

After each settled series, preserve:
- final score;
- whether the series winner thesis was correct;
- whether the selected market won;
- whether the veto interpretation was correct independently of outcome;
- primary model error;
- calibration change, if any.

Do not rewrite historical forecasts after results are known.
