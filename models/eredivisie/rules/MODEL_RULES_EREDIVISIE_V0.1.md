# MODEL RULES — EREDIVISIE v0.1

**Status:** Active  
**Parent methodology:** SlipTrace Football v0.2.41 frozen at `dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`

## 1. Scope

This model applies only to Dutch Eredivisie matches. Non-Eredivisie matches must not enter Eredivisie calibration aggregates.

## 2. Architecture

Use two layers:

1. **Frozen SlipTrace football core** — state synchronization, reset logic, evidence hierarchy, market/settlement logic, persistence, margin controls, validation and record discipline.
2. **Eredivisie calibration layer** — league-specific priors, distributions and empirical adjustments.

The calibration layer may refine probability formation but may never bypass the core controls.

## 3. Independent model lineage

Eredivisie v0.1 is a true fork. Later changes to the general football model are not inherited automatically. Any upstream merge requires an explicit Eredivisie version change.

## 4. Shadow-only startup

Initial execution mode is shadow calibration only.

Allowed verdicts:

- `SHADOW LEAN — DO NOT PLACE`
- `NO BET — HOLD`
- `NO BET`

No official real-money recommendation until the user explicitly enables it after calibration review.

Qualified shadow stake = exactly 0.25u simulated. 1u = 1,000,000 VND. Minimum accepted odds = 1.70.

## 5. Win versus margin separation

Always distinguish:

- win probability;
- draw probability;
- exactly-one-goal win probability;
- 2+ goal margin probability;
- loss probability.

Do not promote a deep favourite handicap from team-strength superiority alone.

## 6. Underdog handicap separation

Underdog attacking threat and underdog defensive margin resistance are separate propositions.

A protected underdog candidate must not pass merely because it creates chances, has a defensive formation, receives a large handicap, or offers an attractive price.

For material/deep favourite situations, explicitly test:

- favourite repeated high-value creation and 2+ margin capability;
- underdog box/goalkeeper/transition resistance;
- underdog adverse-state behaviour;
- underdog credible scoring route;
- favourite-first-goal branch.

## 7. xG/xGOT enforcement

xG and xGOT are secondary diagnostics only. Apply the counterfactual:

> If xG/xGOT disappeared, would the primary thesis still stand?

If no, validation fails.

Possession, raw shots and SOT alone also cannot establish an executable thesis.

## 8. Live reset and persistence

Goals, penalties, red cards, halftime, substitution clusters, major injuries, tactical changes and material weather/pitch changes create a new reset epoch.

After reset, set the goal environment to `Unresolved` until fresh evidence establishes the new state. A single event cannot establish persistence or retroactively relabel the prior regime.

## 9. Major-market scan

Every material assessment must independently compare all available major market families, at minimum:

- sides/Asian handicap;
- moneyline/DNB when available;
- totals.

Team totals and corners may be included when data and settlement are sufficiently reliable.

Choose one best expression only.

## 10. Eredivisie-specific priors to learn

Build and maintain league-specific evidence for:

- home-field effect;
- home/away scoring and conceding distributions;
- closing AH performance by favourite band;
- 2+ goal margin rates by handicap band;
- underdog cover/resistance rates;
- totals by closing total band;
- 0-0 state outcomes at 15/20/30/HT;
- 1-0 and 0-1 state branches;
- first-half/second-half goal rates;
- goal hazard by minute;
- comeback and late-goal rates;
- promoted-team behaviour;
- red-card effects;
- lineup/goalkeeper effects;
- market movement and closing-line value.

Do not claim a stable Eredivisie prior until sample quality supports it. Early in v0.1, widen uncertainty rather than invent precision.

## 11. Record all assessed matches

Record material NO BET and HOLD assessments as well as shadow selections. Do not evaluate the model only on selected bets.

## 12. Error classification before rule changes

Before adding a rule after a bad result, classify the issue as one or more of:

- application/enforcement;
- calibration;
- margin;
- favourite bias;
- underdog bias;
- xG misuse;
- reset violation;
- persistence violation;
- lineup;
- tactical;
- settlement;
- market selection;
- execution;
- normal variance.

Single-match hindsight is not sufficient justification for a new structural rule.

## 13. Response discipline

Every material analysis starts with the verdict and includes `Assessment period: ...`.

Prematch previews may include recent relevant home/away form and recent relevant H2H with low weight. Ordinary live reassessments should not repeat those sections.

Never assume a current score, minute, lineup, event, line or odds without fresh evidence.
