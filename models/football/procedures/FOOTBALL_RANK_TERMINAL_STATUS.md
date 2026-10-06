# Football Rank Terminal Status

**Status:** ACTIVE STEP-1 TERMINAL-STATE CONTROL  
**Applies to:** `/rank` after Step-1 research/replenishment  
**Predictive effect:** none

## Purpose

Prevent a legitimate empty or zero-FOLLOW board from being mislabeled as a blocked ranking run.

A fixture-level quarantine such as `INCENTIVE-INCOMPLETE` is not a board-level failure when the quarantine was applied prospectively, the fixture received no model state/rank/line/lane, and the remaining ranked universe is complete.

## Status precedence

Use this order:

1. **Board/process integrity failure** -> `RANK BLOCKED`.
2. **Deferred prematch A/B candidates remain while FOLLOW+RESERVE < 10** -> `RANK CONTINUES — REPLENISHMENT REQUIRED`.
3. **Ranked eligible universe is empty after legitimate quarantines/closed fixtures and queue is exhausted** -> `RANK COMPLETE — NO RANKED ELIGIBLE FIXTURES`.
4. **Ranked universe exists but FOLLOW=0** -> `RANK COMPLETE — 0 FOLLOW`.
5. **FOLLOW>0** -> `RANK COMPLETE`.

## What may produce RANK BLOCKED

Only board/process failures, for example:
- invalid/incomplete Step-0 handoff;
- required competition coverage failure;
- women's coverage/reconciliation failure;
- unresolved ranked fixture that was incorrectly allowed into the ranked universe;
- deterministic board reconciliation failure;
- other explicit fail-closed integrity faults.

Do **not** use `RANK BLOCKED` merely because:
- FOLLOW count is zero;
- the ranked universe is empty;
- one or more fixtures are prospectively `INCENTIVE-INCOMPLETE`;
- every completed model assessment is STOP/PASS;
- there are no deferred candidates left.

## Incentive quarantine

For a valid `INCENTIVE-INCOMPLETE` fixture:
- no C/C2 state;
- no rank;
- no supported line;
- no lane;
- no WATCH/WAIT accounting;
- it does not count toward active lane capacity;
- it remains visible in the quarantine/hold table.

If deferred prematch A/B candidates exist, the vacancy participates in normal capacity replenishment.

If none exist, the board may validly finish with zero ranked fixtures and zero FOLLOW.

## User-facing output

Never write `/rank blocked — no FOLLOW candidates`.

Use:
- `/rank complete — 0 FOLLOW` when ranked fixtures exist;
- `/rank complete — no ranked eligible fixtures` when all candidates were legitimately quarantined/closed and the queue is exhausted;
- `/rank blocked — <integrity reason>` only for a true board/process failure.

When the board has quarantines, report them separately after the terminal status.
