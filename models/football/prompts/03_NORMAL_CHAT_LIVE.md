# /live — current-state Football C assessment

> **Work conversation role — LIVE ONLY.** This conversation is dedicated to
> Football C in-play reassessment using current match state and frozen
> prematch evidence. Load this launcher from current SlipTrace main.
> Do not silently perform /sweep, /rank, prematch /xi, or /audit in this
> conversation. Preserve live-versus-prematch authorization boundaries.
> If the user explicitly changes stages, load that stage's canonical launcher.
> This is the SlipTrace production route, not FOM.


Football C is the only active model.

/live uses the same football-assessment runtime as /xi with:

- actual current score;
- match minute;
- verified goals/reds/injuries/substitutions;
- current tournament/game-state changes;
- frozen prematch/xi thesis as context.

Provider live stats are not required.

There is no active step2_fixture_transition state machine. Current facts are
frozen directly into the new Football C assessment epoch.

After kickoff:

- assess the current football state;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/WAIT/PASS;
- do not request a new bookmaker quote merely because the game started;
- a user-supplied live quote returns
  LIVE_PRICE_BURDEN_COMPARISON_ONLY unless a separate live-execution policy
  explicitly authorizes action.

C2/C3/C4 models are retired and do not run in /live.
