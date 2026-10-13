# /live — current-state C + C2 football assessment

**Command alias:** /live

/live uses the same football-assessment runtime as /xi.

## Inputs

Use the actual current:

- fixture status;
- score;
- match minute;
- red cards/goals/other material events;
- current route/mechanism state;
- current tournament/incentive state when relevant.

Do not require live bookmaker odds to complete football analysis.

## Execution

Run independent C official + C2 shadow stage=football_assessment payloads at
the same current evidence epoch.

A started fixture is still assessable. Do not discard the football result
because kickoff passed.

There is no active step2_fixture_transition state machine.

## Price

If the user supplies a live screenshot, use its exact displayed line/odds as
current comparison evidence only. Do not search replacement odds.

A live observed quote must not recreate a prematch ACT/WAIT/PASS. The active
runner returns LIVE_PRICE_BURDEN_COMPARISON_ONLY for started fixtures.

No live bet is authorized unless a separately implemented/current live
execution policy explicitly supports it.

## Output

Give the current football read first for C and C2, then:

- current score/minute;
- whether the thesis/mechanism remains intact;
- supported frozen burdens for context;
- material rechecks;
- optional live burden comparison if a screenshot was supplied.

Never retroactively claim a prematch bet.
