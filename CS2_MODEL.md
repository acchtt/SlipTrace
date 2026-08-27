# SlipTrace CS2 Shadow Model

Effective: 2026-08-27
Current version: **v1.4**

Purpose: define the durable CS2 decision model used for shadow testing. Official placed wagers remain separate from this model and are not written to `ledger.json` unless the user explicitly confirms a real wager and authorizes the ledger write.

## Operating window

1. Build and preserve a **pre-veto baseline** before map picks are known.
2. A counted **pre-pistol shadow selection** may be issued after the complete BO3 veto/map order is known and before round 1 begins, using the user's actual available odds.
3. Starting with **v1.3**, a counted **live shadow selection** may also be issued after play has started when the current game state and the user's current live odds are both captured before entry.
4. Pre-pistol and live shadow bets must be tagged separately in Airtable so their performance can be audited independently.
5. Nothing may be retroactively promoted into a counted shadow bet. Historical live calls made before v1.3 remain analysis-only.
6. Airtable `SlipTrace CS2 Decision Control` is the audit layer for pre-veto forecasts, counted shadow bets, and post-match reviews.

## Live shadow protocol

Live shadow bets are permitted only when the state is sufficiently well-defined to recompute the price independently.

Preferred checkpoints:
- **after round 12 / halftime of a map**;
- **between maps** after the previous map is final;
- another live checkpoint only when an exact score, current map, map order and current sportsbook prices are captured clearly enough to avoid stale-state ambiguity.

At a live checkpoint, use:
- current map and exact score;
- completed and upcoming side assignment where relevant;
- remaining map order;
- pre-veto and pre-pistol map probabilities as priors, not anchors;
- current economy / loss-bonus / timeout context when reliably visible or supplied;
- current live market price from the user's sportsbook.

Recompute both **current-map win probability** and **BO3 series probability** from the live state. Do not simply rescale the pre-match series probability.

A live shadow position should normally require:
- model edge of roughly **4 percentage points or more** versus implied probability;
- positive EV of roughly **6% or more** per unit;
- confidence of at least **6.5/10**;
- a thesis based on more than the current score alone.

These are guardrails, not automatic triggers. PASS remains preferred when the apparent edge depends on uncertain economy information, a stale price, or one unsustainable round-level signal.

### Live staking and exposure

- Pre-pistol shadow default: **1.0u**.
- Live shadow default: **0.5u** because state estimates are noisier and prices move quickly.
- A live shadow may use **1.0u** only when the edge is unusually strong and the state is clearly captured.
- Default maximum total shadow exposure on one BO3 is **2.0u** across pre-pistol and live positions combined.
- A live add-on must have an independent edge; do not add merely because an existing shadow bet is losing.

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

For each map in the final BO3, estimate both teams' win probability independently. Do not infer a map win merely because a team selected that map.

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

## v1.2 calibration changes

Introduced after the full 2026-08-20 EWC review: MOUZ-GamerLegion, FURIA-Aurora, NAVI-Legacy, Falcons-The MongolZ, FaZe-Vitality, B8-Spirit and G2-FURIA.

### 6. Market-disagreement sanity check

A large gap between the independent model and a strong, liquid market must be treated as a warning signal rather than automatic value.

If the model differs from the market by **15 percentage points or more** on series win probability, require at least two strong independent reasons beyond the veto before approving a shadow bet. Examples:
- material roster/availability information not yet reflected in price;
- large current-lineup form advantage against comparable opponents;
- substantial map-pool mismatch across at least two maps;
- reliable tactical or role mismatch supported by current data.

Without that support, shrink the estimate toward the market or pass. The FaZe 47% estimate versus Vitality at 3.70 is the reference failure.

### 7. Map-quality over map-ownership

For every picked map, record:
- pick ownership;
- current-lineup win quality on that map;
- opponent quality faced in those results;
- favorite's steal probability on that map.

The key variable is **map win probability**, not who picked it. B8-Spirit is the positive reference case; Falcons-MongolZ is the negative reference case.

### 8. Strong-veto swing threshold

A post-veto move of only 1-3 percentage points is appropriate when the veto largely matches expectations.

When the underdog receives both:
- a genuinely high-confidence first map, and
- a favorable or low-sample decider for the favorite,

a **larger 8-15 point swing** is allowed and may cross 50/50. NAVI-Legacy is the reference failure for under-adjustment.

### 9. Conservative edge preference

Prefer modest, explainable edges with strong structural support over spectacular theoretical edges that depend on uncertain assumptions.

Priority order during shadow testing:
1. map handicap where one-map cover probability is independently strong;
2. Over/Under 2.5 where map-specific probabilities support the series shape;
3. match winner with moderate edge and stable priors;
4. longshot match winner only when the market-disagreement sanity check is satisfied.

### 10. Prediction and price are separate outputs

Always produce both:
- the most likely series result / exact-score lean;
- the best available betting decision.

A correct prediction may still be a pass if the price is too short. Spirit 2-0 at 1.20 ML is the reference positive example.

### 11. Veto update discipline

Do not reward or penalize a surprising team pick mechanically. A surprising pick can imply prepared anti-stratting. G2 choosing Ancient versus FURIA is the reference example: weak historical numbers alone were not enough to treat Ancient as a free FURIA map.

## v1.3 calibration changes

Introduced on 2026-08-22 to extend the shadow test into live markets while preserving clean auditability.

### 12. Live-state re-pricing

At permitted live checkpoints, treat the score and side state as new evidence and rebuild the map/series probability. The pre-pistol model is a prior only.

A halftime lead can be misleading if the leading side has already played the easier side of a strongly side-biased map, or if the opponent has a materially stronger upcoming side. Conversely, a close halftime score can strongly favor the team moving onto its better side.

### 13. No retrospective live selection

A live selection counts only when the exact state and offered odds were observed **before** the subsequent rounds/outcome. Do not score a price that was merely discussed after the state changed.

### 14. Separate live performance audit

Track live shadow W/L, units and ROI separately from pre-pistol shadow results as well as in the combined test record. This prevents a profitable pre-pistol process from masking poor live entries, or vice versa.

## v1.4 calibration changes

Introduced on 2026-08-27 after two similar underdog map-handicap failures: Legacy +1.5 vs Spirit and paiN +1.5 vs FURIA. M80-NAVI is the counterexample used to avoid overcorrecting against all underdogs.

### 15. Handicap-market disagreement sanity check

Apply a dedicated market sanity check to BO3 map handicaps, not only series ML.

If the model differs from the market by roughly **8 percentage points or more** on underdog +1.5 cover probability, or by roughly **10 percentage points or more** on favorite 2-0 probability, require at least two independent structural reasons before approving the handicap. At least one reason must be current-lineup map-quality evidence against comparable opposition, not merely veto ownership or a small-sample win rate.

If that evidence is absent, shrink toward the market or PASS. Legacy +1.5 vs Spirit and paiN +1.5 vs FURIA are the reference failures.

### 16. Elite-favorite map-steal proof standard

Against a stable elite/top-tier favorite, do not price an underdog above 50% to take at least one map merely because:
- the underdog receives its preferred pick;
- the favorite chooses a volatile or low-sample map;
- the decider appears playable;
- recent underdog map form comes mostly from weaker opposition.

To justify an aggressive +1.5 position, require evidence that the underdog has at least one genuinely strong map-win route against **multiple comparable top-tier opponents**, or two independent maps that each project competitively after explicitly pricing the favorite's steal chance.

For the underdog's own pick, a model probability above roughly **55%** should normally require demonstrated current-lineup quality against strong opposition rather than pick ownership alone.

### 17. Favorite-stability modifier

Do not apply the elite-favorite restraint blindly. First classify the favorite's current map floor.

When the favorite is unstable — weak recent map conversion, lineup disruption, repeated losses on its own picks, or a shallow current-map sample — an underdog may still receive a large veto upgrade if it has two independent routes. NAVI-M80 is the reference counterexample: M80 had a deliberate comfort pick plus a genuinely playable decider against a NAVI side with an unstable current map floor.

When the favorite is stable and elite across multiple maps, raise its steal probability on the underdog's pick and its independent 2-0 term before considering +1.5 value.

## Market rules

For every candidate market calculate:
- offered decimal odds;
- implied probability = 1 / odds;
- model probability;
- fair odds = 1 / model probability;
- edge in percentage points = model probability - implied probability;
- expected value per 1u = model probability * (odds - 1) - (1 - model probability).

Prefer NO BET when the model edge is weak or depends mainly on uncertain veto or live-state assumptions. During the test phase, avoid forcing action merely to increase sample size.

For a longshot ML, explicitly state whether the market-disagreement sanity check passed.

## Review discipline

After each settled series, preserve:
- final score;
- whether the series winner thesis was correct;
- whether the selected market won;
- whether the veto interpretation was correct independently of outcome;
- for live positions, the exact entry state and whether the live re-pricing logic was correct independently of result;
- primary model error;
- calibration change, if any.

Do not rewrite historical forecasts after results are known.
