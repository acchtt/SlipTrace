# 03 — Normal Chat: Football C Official Live + C2 Shadow Wait

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired for new/current execution.

**Command alias:** `/live`

Read:
- `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`

Football C is official. C2 is shadow-only. C2 may never create Website Pick or real exposure.

## 1. Eligibility

Use this launcher when:
- a frozen C-WAIT reaches live state;
- a frozen C2 shadow WAIT exists and needs shadow resolution;
- a prematch Step-2 fixture has already started and was rerouted to live;
- the user explicitly requests a live exception.

Do not manufacture a C2 live state if no prospective/current C2 basis exists. A live exception does not authorize retrospective C2 reconstruction from later evidence.

### Automatic early-live takeover from /xi

**Started is not assessment blocked.** A normal /xi assessment can transition
directly into this launcher in the **same response** as soon as current
status says STARTED, without waiting for a second /live command. Invoke
`step2_fixture_transition.py` at the exact verified kickoff/current
timestamp. `EARLY_LIVE_FAST_PATH` covers the first 15 minutes;
`STANDARD_LIVE` covers later play, and **both allow assessment**.
The distinction is urgency only. A match 2, 9 or 16 minutes old is
not automatically PASS or NO BET because it started.

Carry forward the genuinely frozen, independent C and C2 research,
but freeze a **new live epoch** and verify current score/minute, any
goal/red card or material lineup/tactical change, and the live market
when available. At 0-0 with no material change, make a short check of
the existing scoring thesis rather than running the entire Step-1
research pipeline again. After any meaningful event, recompute
goal burden/continuation and relevant tournament incentives.

**Two levels of result:**
1. Immediately deliver the **football assessment** (scoring mechanism,
   whether C/C2's frozen theses survive, a goal-burden view and specific
   reason) even when live quote is unavailable. Clearly label
   `LIVE ASSESSMENT — QUOTE REQUIRED / NO EXECUTABLE BET` if applicable.
2. Only recommend a live official C action after verified **current
   in-play** totals and odds, current fixture/score/event integrity and
   any required C/C2 live engine and persistence/publication checks.
   A C2 apparent action is shadow-only. Never turn a late snapshot
   into a prematch recommendation or claim a bet was placed.

An exact-prematch Step-2 engine rejection of STARTED remains a valid
protection; it must **trigger this handoff**, not terminate the user's
requested football assessment. Never claim an authorized C/C2 action
if the relevant deterministic live decision path was not run.

## 2. Common live evidence

Freeze one current live epoch for both active models:
- score and minute;
- current executable total/odds;
- goals, cards, injuries, substitutions and other material events when known;
- verified tactical/mechanism changes;
- current tournament/aggregate/table state when applicable;
- draw utility;
- margin/GD/tiebreak relevance;
- which side is actually forced to chase.

A goal, red card, major injury, or material mechanism change creates a new epoch and invalidates the prior quote.

## 3. No live-stat gate

Assess the live match **regardless of provider live stats**.

Do not require or request as an execution prerequisite:
- shots / shots on target;
- xG / xGOT;
- big chances;
- dangerous attacks;
- possession;
- corners;
- box/final-third entries;
- momentum/pressure widgets.

positive live-stat confirmation is not required. The absence of positive telemetry is not negative evidence.

If the user supplies live stats, they may provide context, but they cannot by themselves approve, upgrade, downgrade, or cancel the decision.

The live assessment may proceed from score/minute, current quote, frozen prematch/XI thesis, and concrete material events.

## 4. Tournament incentive — every material live epoch

For a tournament/cup/qualification fixture, recompute:
- score + aggregate/table state;
- home incentive;
- away incentive;
- draw/extra-time/penalty consequence;
- margin/tiebreak relevance;
- simultaneous-result effects when relevant;
- side genuinely forced to chase;
- current incentive effect.

If the recomputation is missing:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE EPOCH MISSING`

If the material state remains LIMITED/UNKNOWN:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

A user exception does not waive this integrity gate.

## 5. Football C official WAIT/live resolution

Retrieve the exact frozen C plan and its accounting state.

Core question:

`TARGET REACHED + PREMATCH/XI THESIS NOT MATERIALLY INVALIDATED?`

A target number alone never authorizes C-BET.

Clock/price decay without a goal is not thesis decay by itself.

Cancel or pass only when concrete current football information materially attacks the frozen mechanism, including:
- red card against the carrier;
- key attacking injury/substitution;
- verified tactical/mechanism deterioration;
- tournament incentive turning suppressive;
- current clearing-goal funding no longer credible.

Possible official outputs:
- `C-BET — <line> @ <odds>`
- `C-WAIT — TARGET NOT YET READY`
- `C-WAIT CANCELLED — THESIS DECAY`
- `C-PASS — NEW EPOCH INVALIDATES PLAN`

## 6. Football C2 shadow resolution

Use the same common live epoch, but apply C2's own frozen route-quality/supported-burden policy.

Possible shadow outputs:
- `C2-BET — <line> @ <odds> — SHADOW`
- `C2-WAIT — SHADOW`
- `C2-WAIT CANCELLED — SHADOW`
- `C2-PASS — SHADOW`

Do not copy C's line or action into C2.

C2 never creates a Website Pick or official exposure.

## 7. WAIT accounting integrity

Under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`, the frozen model-accounting state is not silently rewritten by later live observation.

For Football C:
- WAIT_ASSUMED remains the model exposure convention unless the user supplies a matching actual bet or explicitly says the target was not reached.
- a later recommendation change does not erase the already frozen accounting entry.

For C2:
- shadow WAIT accounting follows its own frozen supported target;
- it remains shadow-only.

User execution truth and model accounting remain separate.

## 8. Persistence

Persist material live changes without overwriting the frozen prematch/XI record:
- live epoch time;
- score/minute;
- current quote;
- material events;
- tournament-incentive state when applicable;
- C live action;
- C2 shadow live action;
- thesis/mechanism cancellation basis where relevant;
- user-declared target-not-reached or actual execution facts.

Do not create new C3/C4 current fields or actions.

## 9. User-facing output

Show:
- Match / score / minute
- Current line / odds
- C frozen plan
- C current official action + reason
- C2 frozen plan if available
- C2 current shadow action + reason
- tournament-incentive epoch when applicable
- exact blocker when unresolved
- accounting/user-execution distinction when relevant

Do not delay the verdict waiting for live-stat screenshots.
