# Football Model Rules v0.2.44 — Timeliness, Pre-Goal Trigger and Decision-First Delivery

**Effective date:** 2026-08-14  
**Status:** Active audit rule  
**Supersedes:** v0.2.43 only where its post-goal persistence logic was being misapplied to delay an already-qualified pre-goal total candidate. It does **not** weaken the mandatory post-goal reset.

## Trigger

Recent live reviews identified a repeated process problem: the model sometimes recognized a valid total-goal environment but waited for an additional event or confirmation interval before delivering the verdict. In Portland Timbers vs Club Tijuana, Over 3 @ 1.96 was visible around 61' at 1-1; the model delayed, Portland scored at 64', and the original state ceased to exist. The later 3-1 score shows the timing cost, but that result is not allowed to retroactively convert the missed state into a winning shadow.

The objective of this rule is prospective: reduce decision latency without weakening synchronization, settlement, style, or provider-quality controls.

## 1. Pre-goal states are decision-complete when the existing gates are complete

If the current synchronized state is **not** inside an unresolved post-goal or other material-event reset, a total candidate may be issued immediately once all applicable selection gates are satisfied.

Do **not** wait for a goal merely to obtain confirmation of a thesis that is already supported by the current state.

The v0.2.43 post-goal persistence requirement applies **after a goal has occurred**. It must not be imported backward into an otherwise stable pre-goal state.

## 2. Verdict-first delivery is mandatory

Once the gates resolve, deliver the decision before the long explanation.

Required order:

1. current synchronized state;
2. verdict line;
3. chosen line and odds if applicable;
4. only then the compact reasoning and invalidation condition.

Valid audit outputs remain:

- `SHADOW LEAN — DO NOT PLACE`;
- `BENCHMARK SHADOW — DO NOT PLACE`;
- `NO BET`;
- `NO BET — HOLD`.

Do not spend the decision window narrating every input before stating the verdict.

## 3. No confirmation tax

An additional snapshot is not automatically required when the current synchronized snapshot already contains:

- the exact score and minute;
- exact line, odds, and settlement scope;
- at least two independent forward-looking primary evidence channels;
- sufficient style/game-state context for the applicable arm;
- no unresolved material-event reset;
- an adjacent-line comparison where required;
- a candidate that is preferable to NO BET.

Require another observation only when persistence itself is materially unresolved, the provider feed is stale or contradictory, or a specific existing rule requires a second observation for that state.

## 4. Material-event race rule

A goal, red card, awarded penalty, material VAR event, major injury, or substitution/tactical cluster that occurs **before the verdict is delivered** invalidates the pending candidate.

Record it as:

`NOT COUNTED — STATE CHANGED BEFORE DELIVERY`

Then reprice from zero under the new state.

A candidate invalidated this way is neither a win nor a loss and must not enter shadow P/L.

## 5. Arm B fast-path for live totals

For the early-totals benchmark, a synchronized pre-goal state may produce an immediate benchmark shadow when all of the following hold:

1. exact total line and odds are visible and at least 1.70;
2. settlement scope is verified;
3. at least two independent forward-looking channels support the same goal-environment direction;
4. no reset is unresolved;
5. adjacent totals have been compared and the selected boundary is the best expression;
6. the adverse-branch test is passed;
7. the total remains preferable to NO BET after clock decay;
8. the total expresses the evidence more cleanly than a directional side when the side's decisive-event branch is ambiguous.

When these conditions are already met, do not wait for the next goal to validate the Over or Under thesis.

## 6. Post-goal discipline remains strict

After any goal, v0.2.43 remains fully active.

Before a **new** post-goal candidate, report:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:`
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence over a meaningful interval. v0.2.44 is not permission to skip that reset.

## 7. Quote synchronization remains mandatory

The candidate must be tied to the latest synchronized market snapshot. Existing v0.2.36 odds-drift tolerance remains unchanged. A line change, material state event, or stale timestamp requires repricing.

## 8. Timeliness audit fields

For each live assessment that approaches a decision boundary, classify the timing result as one of:

- `ON TIME — DELIVERED IN STATE`;
- `VALID HOLD — GATE INCOMPLETE`;
- `LATE — GATES WERE COMPLETE BUT VERDICT DELAYED`;
- `STATE-CHANGE RACE — NOT COUNTED`.

When a late or state-change-race case occurs, record what gate was actually unresolved, if any. If no gate was unresolved, classify it as a delivery-process failure rather than inventing a retrospective analytical reason.

## 9. No retrospective promotion

The Portland Timbers vs Club Tijuana Over 3 @ 1.96 example is a process lesson only. It is not a shadow selection because the verdict was not delivered before the state changed.

The same rule applies to all future reviews: a market that would have won is not a model win unless it was prospectively selected in the synchronized state.

## Operating principle

When the evidence is sufficient, decide now. When a material event changes the state, reset now. Do not confuse caution with accuracy, and do not use post-goal confirmation rules to delay a qualified pre-goal total.