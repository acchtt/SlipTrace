# MODEL RULES — BRAZILIAN SERIE A v0.1

## Status

Initial independent child model. Shadow calibration only.

## 1. Scope

Only Campeonato Brasileiro Serie A league matches may produce child-model assessments or enter the core calibration sample.

Other competitions may inform fatigue, rotation, availability or tactical context, but must not be pooled directly into league priors.

## 2. Core methodology inheritance

Apply the frozen SlipTrace Football v0.2.41 process at ref `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`, then apply this file as the child-specific layer.

## 3. League-specific probability layer

Before any candidate, use Brazilian Serie A-specific priors when available for:

- home/away attack and defense;
- expected scoring distribution;
- draw rate;
- favorite win and margin distribution by handicap band;
- underdog protection by handicap band;
- score-state and minute effects;
- promoted-team performance;
- rest/travel/congestion effects;
- red-card and late-goal behavior;
- closing-line behavior.

When child-specific sample size is inadequate, widen uncertainty rather than importing a strong generic prior.

## 4. Travel/rest/congestion module

For every prematch assessment, explicitly check:

- days of rest for both teams;
- whether either team played continental or domestic cup football midweek;
- rotation and travel burden;
- long-distance travel or materially different climate/venue conditions when relevant;
- likely substitution depth after congestion.

These variables count only when they change expected performance or variance. Narrative mention without probability impact is prohibited.

## 5. Win versus margin

Maintain separate views of:

- win probability;
- draw probability;
- one-goal win probability;
- 2+ goal win probability;
- loss probability.

A strong win thesis does not automatically qualify a deep negative handicap.

## 6. Protected-underdog control

An underdog handicap requires affirmative defensive margin-suppression evidence, not merely attacking threat or a seemingly generous line.

Against a material favorite, test:

- favorite repeated high-value creation and multi-goal capability;
- underdog box and transition defense;
- goalkeeper/center-back stability;
- adverse-state resistance after conceding first;
- credible underdog scoring route that can restore handicap protection;
- rest/travel/congestion asymmetry that materially reduces favorite margin capacity, if applicable.

Formation labels, possession, isolated close losses and handicap size itself do not satisfy the gate.

## 7. xG/xGOT

xG and xGOT remain secondary-only diagnostics.

Counterfactual test: if xG/xGOT were removed, the primary thesis must still stand. Otherwise validator result = FAIL.

## 8. Live state machine

A goal, penalty, red card, major injury, substitution cluster, halftime, tactical change or material weather/pitch change creates a new reset epoch.

Post-reset goal environment begins `Unresolved` until fresh evidence establishes Closed/Neutral/Open. One event cannot establish persistence.

## 9. Primary evidence minimum

For live selections, require at least two independent forward-looking primary channels unless a stricter inherited rule applies.

Valid channels include:

- central/box access;
- big chances;
- dangerous transitions/cutbacks;
- sustained set-piece pressure;
- defensive degradation;
- repeatable shot-location quality;
- persistent territory/box touches;
- tempo/persistence;
- scoring/conceding profile;
- lineup/availability;
- validated Serie A prior;
- rest/travel/congestion effect when independently material.

Possession, raw shots, SOT and xG/xGOT cannot alone satisfy the minimum.

## 10. Market scan and one-best-expression

Every material assessment scans available major families at minimum:

- Asian handicap/sides;
- moneyline/DNB where relevant;
- totals.

Team totals/corners may be added when sufficiently supported.

Issue at most one new positive selection per assessment point.

## 11. Settlement

Exact Asian handicap, quarter-line and total settlement must be understood before promotion. For live markets verify whether settlement is full-match or remaining-match.

Minimum accepted odds = 1.70.

## 12. Calibration mode

Positive output: `SHADOW LEAN — DO NOT PLACE`.

Simulated stake: exactly 0.25u.

1u = 1,000,000 VND.

No official real-money recommendation until the user explicitly activates execution after calibration review.

## 13. Error review

After outcomes, separate process validity from result. Before adding a new rule, classify whether the problem was:

- application/enforcement;
- calibration;
- margin;
- favorite/underdog bias;
- xG misuse;
- reset/persistence;
- lineup/tactical;
- settlement/market selection;
- travel/congestion;
- execution;
- normal variance.

Do not create hindsight rules from a single loss.
