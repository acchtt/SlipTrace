# SlipTrace Eredivisie v0.1

**Status:** Initial league-specialized extension  
**Mode:** Shadow calibration only  
**Parent:** Current SlipTrace football model resolved dynamically from `models/football/CURRENT_MODEL.md`

## 1. Purpose

Eredivisie v0.1 does not create a new football betting philosophy. It adds an Eredivisie-specific probability and calibration layer to the active SlipTrace football process.

The parent football model remains authoritative for decision logic. The Eredivisie layer may alter league priors, distributions and calibration inputs when sufficient league-only evidence exists, but it may not relax or bypass any active parent gate.

## 2. Inherited controls — unchanged

The following remain parent-model controls and are not redefined by Eredivisie v0.1:

- synchronized match identity, score, minute/phase, material events, line, odds and settlement scope;
- reset epochs after goals, penalties, red cards, major injuries, tactical changes, substitution clusters, halftime and material weather/pitch changes;
- post-reset `Goal Environment = Unresolved` until fresh evidence establishes the new regime;
- competition-format verification and propagation into regulation-win, draw, margin, loss-avoidance, conservation and other relevant utility;
- decomposition of win probability, draw probability and margin probability;
- lineup/personnel analysis, goalkeeper and centre-back stability, bench quality and tactical matchup;
- opponent-adjusted team-strength decomposition;
- evidence hierarchy and correlated-evidence control;
- xG/xGOT as secondary evidence only;
- the counterfactual that a thesis must survive removal of xG/xGOT;
- directional persistence, candidate-switch and one-event binary-market controls;
- favourite-fade, deep-favourite and protected-underdog gates;
- full independent market-family scan and one-best-expression discipline;
- exact Asian-handicap and quarter-total settlement;
- exact remaining event-budget analysis for goal and corner unders;
- minimum-price, execution-freshness and accepted-odds drift rules;
- hard pre-verdict validator;
- mandatory Airtable Decision States write lock;
- official accounting authority of `/ledger.json` when ledger writes are authorized.

If a future parent football rule conflicts with this extension on a process/control issue, the parent rule controls. Eredivisie v0.1 controls only league-specific calibration matters unless explicitly superseded by a later Eredivisie version.

## 3. Eredivisie-only calibration universe

Only matches verified as Netherlands Eredivisie belong in the statistical calibration dataset.

Do not automatically include:

- KNVB Cup;
- UEFA Champions League, Europa League or Conference League;
- friendlies;
- Eerste Divisie;
- reserve or youth football;
- international matches;
- any other competition merely because an Eredivisie club participates.

Non-Eredivisie matches may be used as contextual evidence for current personnel, tactical shape, fatigue, rotation or availability when relevant. Their match statistics do not enter Eredivisie league priors unless a later rule explicitly creates and validates a cross-competition adjustment.

Competition membership must be stored explicitly. Ambiguous competition or phase metadata is a data-quality failure, not an invitation to infer inclusion.

## 4. Initial calibration state

At v0.1 creation, numeric Eredivisie priors are `UNINITIALIZED`.

Do not insert generic-football numeric priors merely to fill the league layer. Until sufficient Eredivisie-only evidence is available, use the parent model's disciplined uncertainty handling and mark league-specific calibration fields as unavailable or provisional.

The first purpose of v0.1 is to collect clean league-only observations, not to force premature precision.

## 5. Eredivisie calibration components

The league layer should eventually maintain versioned estimates for the following, always with sample size, season/window and uncertainty metadata:

### 5.1 League scoring and venue distributions

- home-team goals distribution;
- away-team goals distribution;
- total-goals distribution;
- home-field effect;
- first-half scoring;
- second-half scoring;
- late-goal frequency;
- goal hazard by minute or time band;
- 0-0 at 15, 20, 30 and halftime outcome distributions;
- 1-0 and 0-1 score-state outcome distributions;
- comeback and equalizer rates.

### 5.2 Market-conditioned margin distributions

- closing Asian-handicap distribution;
- favourite result by closing handicap band;
- favourite win-by-exactly-one rate;
- favourite 2+ margin rate;
- protected-underdog cover/protection rate by exact line;
- draw rate by market-strength band;
- total-goal outcome by closing total line;
- closing-line movement and direction.

A strong favourite prior must never collapse win and margin into one probability. The league layer must preserve separate branches for win, draw, exactly-one-goal margin and 2+ margin.

### 5.3 Team and personnel effects

- opponent-adjusted attack;
- opponent-adjusted defence;
- home/away splits;
- scoring and conceding distributions;
- high-value chance creation;
- box/central access;
- set-piece attack and defence;
- transition attack and defence;
- goalkeeper effects;
- centre-back stability;
- lineup strength;
- bench/substitution strength;
- tactical matchup markers;
- promoted-team performance.

Raw recent results remain supporting evidence rather than the model. Relevant competitive H2H is preview-only and low weight unless personnel, tactical and incentive comparability are independently established.

### 5.4 Live-state effects

- scoring hazard by minute and score state;
- scoring after first goal;
- favourite/underdog behaviour after taking the lead or falling behind;
- red-card effects separated by team strength, score state and minute;
- substitution-cluster effects;
- late defensive degradation;
- persistence following 0-0 checkpoints;
- comeback, equalizer and second-goal branches.

These are calibration inputs only. A live recommendation must still pass the parent reset, persistence and primary-evidence gates from the current synchronized state.

## 6. Prematch workflow

Before considering a shadow wager, verify:

- exact teams;
- date;
- Netherlands Eredivisie competition membership;
- venue and home/away designation;
- confirmed or explicitly classified expected lineups;
- injuries/suspensions;
- current market and exact settlement scope;
- current Asian handicap;
- current goal total.

Evaluate both teams independently using the decomposed parent workflow. At minimum assess:

- opponent-adjusted attack and defence;
- relevant home/away scoring and conceding profiles;
- high-value chance creation and suppression;
- box access;
- set pieces;
- transition attack and defence;
- goalkeeper quality;
- centre-back stability;
- lineup strength and bench strength;
- tactical matchup;
- first-goal branches.

Recent relevant home/away form and relevant H2H belong in the prematch preview, but neither may replace the decomposed assessment.

## 7. Favourite and protected-underdog calibration

The Eredivisie layer must estimate the league-specific distribution behind a favourite's expected margin, but it does not weaken the parent protected-underdog controls.

For material/deep favourites, explicitly separate:

- favourite win probability;
- draw probability;
- favourite exactly-one-goal-win probability;
- favourite 2+ goal probability;
- underdog scoring probability;
- underdog adverse-state resistance.

A protected underdog requires affirmative evidence that the offered favourite margin is overstated. The parent requirement for at least two independent margin-suppression channels and a passing favourite-first-goal branch remains mandatory when applicable.

Handicap protection itself, defensive formation labels, generic counterattack narratives, possession stories and friendly H2H are not margin-suppression evidence.

## 8. Live workflow

Follow the parent state machine without modification.

Every material event creates a new reset epoch. The prior Open/Neutral/Closed state does not survive automatically.

After a reset:

1. set `Goal Environment = Unresolved`;
2. expire stale directional evidence;
3. collect fresh synchronized post-reset evidence;
4. require persistence appropriate to the parent rules before reclassifying the regime or switching direction.

One high-value event can reveal danger or trigger a reset. It cannot by itself establish a persistent attacking regime.

Strong primary channels include central/box access, clear chances, dangerous transitions/cutbacks, repeated high-value shot locations, persistent opposition-box touches, sustained set-piece pressure, verified defensive degradation, tactical overloads and tempo/persistence.

Possession, pass counts, raw shots and shots on target without shot-quality context remain lower-value or contextual evidence. xG/xGOT remain secondary only.

## 9. Market scan and one-best-expression

Every material prematch or live assessment independently scans the available major market families.

At minimum compare:

- Asian handicap / sides;
- DNB or moneyline where relevant;
- totals.

Evaluate team totals and corners when sufficiently supported and settlement-verifiable. Other displayed markets may be assessed only when reliable inputs exist.

Do not anchor to the market first supplied by the user. Rejecting one side does not confirm the opposite side.

At each decision point, choose no more than one best expression.

## 10. Settlement and event budgets

Before any shadow selection, apply the parent exact-settlement rules.

For Asian handicaps and quarter lines, understand all full-win, half-win, push, half-loss and full-loss branches.

For live Asian handicaps, distinguish full-match score from remaining-match settlement when applicable.

For totals, explicitly calculate the number of additional goals required for each settlement branch. The remaining event budget must be compared with time, score state, chase utility, substitutions, fatigue, routes to goal and stoppage-time exposure.

## 11. Shadow-only execution mode

Eredivisie v0.1 is shadow-only even if the parent football circuit breaker is later cleared.

A validator-qualified selection must be labeled:

`SHADOW LEAN — DO NOT PLACE`

Default simulated stake is exactly 0.25u. At project creation, 1u = 1,000,000 VND, therefore 0.25u = 250,000 VND.

Minimum accepted odds are inherited dynamically from the parent model; at project creation the minimum is 1.70.

Do not vary simulated stake according to subjective confidence.

A `PASS` is not sufficient unless the corresponding core Airtable Decision States record exists. If the parent football circuit breaker is active, also follow its Circuit Breaker record requirements. The separate 50-match Eredivisie calibration sample is not the same thing as the parent's four-match circuit breaker.

## 12. Required assessment record

Every material assessment, including `NO BET` and `NO BET — HOLD`, must enter the Eredivisie calibration dataset.

The record must preserve at least:

- match and season;
- home and away teams;
- score and minute;
- assessment period;
- reset epoch;
- market, candidate, line and odds;
- goal environment;
- evidence channels;
- xG role;
- favourite/underdog status;
- validator result;
- fail/hold reasons;
- verdict;
- eventual result;
- closing line and price information when available;
- simulated P/L when a shadow selection exists;
- process validity.

Do not record only selections. Excluding NO BET decisions would create selection bias and make calibration review unreliable.

## 13. Probability output discipline

League probabilities may be produced only when supported by the current data and model state.

When support is weak:

- use intervals or qualitative calibration state rather than false precision;
- record sample size and applicable cohort;
- widen uncertainty for sparse promoted-team, handicap-band, score-state or personnel cells;
- do not manufacture a precise number from generic football intuition.

No numeric Eredivisie prior becomes active merely because it was calculated once. It must be versioned, documented and reviewed under the calibration protocol.

## 14. Model changes and review discipline

Do not create a new Eredivisie rule because one shadow selection loses.

For every proposed correction first classify whether the failure was:

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
- data/universe classification error.

Ask first: was a rule missing, or did the process fail to apply an existing rule?

Add or alter a rule only when the evidence supports a real missing control or durable calibration error rather than hindsight.

## 15. Response format

Keep live reassessments compact and decision-first.

Every material Eredivisie assessment begins with exactly one of:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET — HOLD`
- `NO BET`

Then include:

`Assessment period: ...`

Prematch previews include recent relevant home/away form and relevant H2H. Ordinary live reassessments do not repeat those sections unless specifically requested.

Never invent current score, minute, lineup, event, line or odds. Fresh user evidence overrides stale match-state assumptions.

## 16. v0.1 governing principle

**Same SlipTrace decision process; narrower league-specific calibration.**
