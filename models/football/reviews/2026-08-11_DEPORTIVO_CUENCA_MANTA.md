# Deportivo Cuenca vs Manta — Shadow Review

Date: 2026-08-11
Model at decision: Football v0.2.41
Circuit-breaker selection: CB3
Selection: Deportivo Cuenca -0.5 @2.45, simulated 0.25u
Entry state: 61:05, score 1-1
Final score: Deportivo Cuenca 1-2 Manta
Settlement: Lost, -0.25u simulated P/L

## Decision-state evidence

At the entry snapshot Cuenca led the aggregate process by 1.72-0.11 xG, 19-6 shots, 7-2 shots on target, 17-7 opposition-box touches, 6-1 corners and 63-37 possession.

The selection promoted the directional conclusion that Cuenca were more likely to score the next decisive goal into a Cuenca -0.5 full-match side bet.

## Process error

The primary error was not that Cuenca had no attacking edge. The error was choosing a directional side expression when the same evidence more directly supported continued event generation.

Cuenca's pressure created two distinct possibilities: Cuenca could score, but their aggressive posture also preserved transition space for Manta. Manta had already scored once despite weak aggregate creation, so their counter/transition route could not be treated as negligible merely because aggregate xG was low.

The side bet required Cuenca to score the winner and then avoid conceding. A live total could benefit from a goal by either team. Therefore the side expression carried more directional dependence than the underlying evidence justified.

At the synchronized sportsbook snapshot:

- Over 2.5 @1.59 was below the 1.70 minimum and was ineligible.
- Over 2.75 @1.88 was eligible and had a materially better settlement relationship to the observed match state: exactly one further goal produced a half-win; two or more further goals produced a full win.
- Cuenca -0.5 @2.45 required a Cuenca win and lost on both a draw and a Manta win.

Correct process comparison: Over 2.75 @1.88 should have ranked above Cuenca -0.5 @2.45 once Manta's live transition route was acknowledged.

## Non-hindsight lesson

When one team has sustained attacking dominance but the opponent has already demonstrated a credible scoring or transition route, the model must distinguish **directional superiority** from **event-generation superiority**.

The evidence can strongly imply another goal without strongly implying which team scores it.

Before promoting a live side in this state, compare it explicitly with the best eligible one-goal-over / quarter-goal-over expression. The side may pass only if the evidence contains an additional independent channel that makes the dominant team's scoring route materially stronger than the opponent's transition/scoring route after accounting for settlement and price.

This review motivates Football v0.2.42.