# Football V4 goals-first research screen

The screen schedules football research; it is not a Football C prediction,
board state or betting decision.

Active implementation:

- discovery_goal_gate.py
- goals_first_intake.py

There is no second legacy prescreen pass.

## Admission

The original route-composite path and the high-rate alternate path are
league-neutral, price-blind and prematch-only.

A qualifying screen permits the fixture to reach research/rank. It does not
create G3/G4/G5/G6, supported burden, FOCUS or a bet.

A WATCH_GOAL_SIGNAL outcome is an intake/research result, never Football C
PASS.

Competition/league identity may control registry inclusion/researchability but
must not manufacture the goal signal.
