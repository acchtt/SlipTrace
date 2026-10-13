# Football V4 — goal-first research screen

## Status

Current V4 intake authority.

The active implementation is:

- models/football/stages_v4/discovery_goal_gate.py
- models/football/stages_v4/goals_first_intake.py
- models/football/stages_v4/cheap_sweep_filters.py
- models/football/stages_v4/stage.py

The former engine/goal_route_prescreen.py and its CLI are retired and are not
part of production.

## Purpose

Registration means a fixture is eligible for football research. It is not a
goal signal.

Every non-excluded competitive fixture must pass the same source-backed recent
goal-history screen before it can enter the V4 rank-eligible GOAL_PRIORITY
queue.

This screen schedules research only. It is not C/C2, not a goals forecast and
not a betting action.

## Evidence

For both teams use 4–10 verified completed competitive scorelines from
source-backed recent history.

The source must:

- be public HTTPS;
- be observed within the V4 freshness window for historical-form evidence;
- contain unique historical kickoff timestamps;
- contain results old enough to be provably final;
- stay inside the configured lookback.

If either side lacks enough valid history:

PENDING_GOAL_HISTORY

If supplied source history is malformed/stale/unverifiable:

PENDING_SOURCE_SCORING_EVIDENCE

Do not invent missing results.

## Equal goal-history screen

For each side derive:

- average goals scored;
- average goals conceded;
- 3+ total-goal frequency;
- 4+ total-goal frequency;
- <=2-goal stall frequency;
- 0-0 / 1-1 draw-trap frequency.

Derive the two matchup scoring routes from team scoring and opponent conceding
history, then compute the bounded evidence-only research priority used by
discovery_goal_gate.py.

Qualification requires all current V4 thresholds:

- priority score >= 60;
- mean 3+ total-goal rate >= 0.55;
- mean 0-0/1-1 draw-trap rate <= 0.35.

A qualifying row is:

DISCOVERY_GOAL_QUALIFIED

and, after registry/researchability gates, may become GOAL_PRIORITY.

A non-qualifying quantified row is:

WATCH_GOAL_SIGNAL

This is an intake/research result, never C/C2 PASS.

## League-neutral rule

The goal-history qualification itself does not add points because a competition
is Big Five, Dutch, famous, obscure or registered.

League/team research profiles in cheap_sweep_filters.py are workload priorities
only. They may decide which pending fixture is researched earlier, but they
cannot convert weak/missing goal evidence into GOAL_PRIORITY.

This prevents league prestige from substituting for current match evidence.

## Current research order

For already qualified GOAL_PRIORITY fixtures, stage.py builds one
football-v4-goal-research-manifest-v2 directly from the frozen V4 goal screen.

Order is driven by:

1. quantified goal priority;
2. cheap research-priority rank;
3. kickoff time;
4. stable match ID.

There is no second legacy prescreen pass.

## Draw-trap safeguard

Repeated 0-0 and 1-1 results directly weaken the qualification through the
draw-trap threshold. High BTTS counts cannot by themselves turn repeated 1-1
matches into a third-goal signal.

## Scope interaction

Explicit hard exclusions remain excluded even if recent results are high
scoring.

Current examples include:

- African domestic leagues/cups/women's domestic competitions;
- noncompetitive friendlies;
- standing domestic exclusions;
- generic unapproved youth competitions.

UEFA Youth League is the specific youth exception and still requires
fixture-specific goal evidence.

## Output integrity

Every source-visible fixture remains in the audit ledger.

A fixture not admitted to GOAL_PRIORITY must retain its real pending/watch/
excluded reason. Do not replace it with a model PASS.

The frozen V4 receipt binds:

- source ledger;
- eligible queue;
- goal screen per fixture;
- research order manifest;
- integrity SHA256.

Historical sealed V1 research manifests remain acceptable for their original
receipts, but new V4 sweeps emit the simplified V2 manifest.
