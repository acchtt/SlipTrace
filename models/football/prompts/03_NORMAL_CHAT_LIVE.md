# 03 — Normal Chat: Football C Official Live + C2/C3 Shadow Wait

**Command alias:** `/live`

Read:
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`

Football C is official. C2 and C3 are shadow-only.

## Common live evidence

For a supplied live fixture, freeze one current live state:
- score/minute;
- goals/cards/injuries/substitutions or other material event changes when known;
- material tactical/mechanism changes supported by concrete event/news evidence;
- current quote;
- current tournament/aggregate/table state when applicable;
- whether a draw is acceptable;
- whether extra time/direct penalties are reachable;
- whether goal difference/margin still matters;
- which side is genuinely forced to chase.

Use this same live state for C, C2 and C3 when a corresponding predeclared shadow WAIT exists.

### No live-stat gate

Assess the live match **regardless of provider live stats**.

Do not require, request, or use as a mandatory execution/cancellation gate:
- shots / shots on target;
- xG / xGOT;
- big chances;
- dangerous attacks;
- possession;
- corners;
- box entries / final-third entries;
- pressure / momentum widgets;
- any derived live-stat feed.

These feeds are too inconsistent across providers and may miss goals that arise from isolated transitions, set pieces, penalties, long shots, errors or deflections.

The absence of positive live telemetry is **not negative evidence**.

A live assessment may proceed from the current score, minute, executable line/odds, the frozen prematch/XI thesis, and concrete material events. If a user supplies live stats, do not let them upgrade, downgrade, approve or cancel the decision by themselves.

## Football C official WAIT resolution

Retrieve the exact official C-WAIT plan and its already-created assumed exposure.

The live workflow may change the current football recommendation, but it does **not** rewrite WAIT accounting by itself. Under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`, the default exposure remains target line @ minimum odds until the user provides a matching actual bet or explicitly says the line never reached.

Core rule:

`TARGET REACHED + PREMATCH/XI THESIS NOT MATERIALLY INVALIDATED?`

A target number alone never authorizes C-BET, but **positive live-stat confirmation is not required**.

Clock/price decay without a goal is not thesis decay by itself.

Cancel only when concrete football information materially attacks the frozen mechanism, such as a red card against the carrier, key attacking injury/substitution, verified tactical/mechanism change, or changed tournament incentive.

A goal/red card/major injury/material mechanism change invalidates the old quote and creates a new epoch.

For tournament/cup fixtures, every new epoch must recompute incentive before resolving the Over. A level score does **not** imply continued chase if parity can lead directly to penalties, protect an aggregate/table objective, or otherwise remain strategically acceptable.

For an applicable tournament fixture, explicitly output the current incentive epoch:
- score + aggregate/table state;
- home incentive;
- away incentive;
- draw/penalty/extra-time consequence;
- margin/tiebreak relevance;
- incentive effect;
- side genuinely forced to chase.

If this recomputation is missing:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE EPOCH MISSING`

If it exists but qualification/tiebreak/margin/simultaneous-result consequences remain LIMITED/UNKNOWN:

`LIVE DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

Do not issue a normal live C/C2/C3 action from any unresolved state. A user-declared exception may authorize reassessment of the fixture but does **not** waive the requirement to resolve the current incentive epoch first.

Official C may produce:
- `C-BET — <line> @ <odds>`
- `C-WAIT — TARGET NOT YET READY`
- `C-WAIT CANCELLED — THESIS DECAY`
- `C-PASS — NEW EPOCH INVALIDATES PLAN`

Persist official material live state.

If a live C-BET recommendation occurs from a prior C-WAIT, do not automatically replace the existing WAIT assumed-exposure line/odds. Reconcile the Website Pick to actual line/odds/stake only when the user supplies the corresponding bet.

If the user explicitly says the WAIT target line never reached, mark the operational C-WAIT exposure `WAIT_NOT_REACHED / USER_DECLARED_NOT_REACHED`, Result=`VOID`, P/L=0, and remove the WAIT layer from C model-accounting.

If the frozen C board state was C-WATCH, retain the independent C-WATCH accounting bet at C supported line @1.65, 1u. Do not erase WATCH accounting merely because the later WAIT target never reached.

## Football C2 shadow WAIT resolution

If a predeclared C2-WAIT exists, resolve it separately using the same common live evidence and its own target/cancellation conditions. Do not require live-stat confirmation.

Its audit accounting remains a shadow assumed bet at the frozen WAIT target/minimum odds unless the user explicitly states that target line never reached. If that occurs and the frozen C2 board state was C2-WATCH, remove only the WAIT layer and retain C2-WATCH accounting at C2 supported line @1.65, 1u.

C2 may produce:
- `C2-BET — SHADOW`
- `C2-WAIT — SHADOW`
- `C2-WAIT CANCELLED — THESIS DECAY — SHADOW`
- `C2-PASS — NEW EPOCH — SHADOW`

C2 may never create Website Pick or real exposure.

## Football C3 shadow WAIT resolution

If a predeclared C3-WAIT exists on a fixture already in the normal live workflow, resolve it from the same live epoch. Do not require live-stat confirmation.

Its audit accounting remains a shadow assumed bet at the frozen WAIT target/minimum odds unless the user explicitly states that target line never reached. If that occurs and the frozen C3 board state was C3-WATCH, remove only the WAIT layer and retain C3-WATCH accounting at C3 supported line @1.65, 1u.

Recheck:
- required clearing-goal funding;
- funding source integrity;
- control-endpoint risk;
- primary funding mechanism;
- tournament incentive epoch when applicable.

C3 may produce:
- `C3-BET — SHADOW`
- `C3-WAIT — SHADOW`
- `C3-WAIT CANCELLED — FUNDING DECAY — SHADOW`
- `C3-PASS — NEW EPOCH — SHADOW`

Do not start C3-only live monitoring for a fixture Football C is not otherwise following.

## Mandatory three-track visibility

For every material live match, visibly report:
- `OFFICIAL C: ...`
- `SHADOW C2: ...`
- `SHADOW C3: ...`

If a shadow track has no valid prospective frozen state/plan, show:
- `SHADOW C2: UNAVAILABLE — NO PROSPECTIVE C2 FREEZE`; or
- `SHADOW C3: UNAVAILABLE — BOARD PREDATES C3 / NO PROSPECTIVE C3 FREEZE`; or
- the applicable `COMPARISON INCOMPLETE` reason.

Never omit a shadow row just because the handoff is stale or the match is already live.

Do not ask the user for live-stat screenshots before assessing. Score/minute/odds plus the preserved football thesis are sufficient unless a separate integrity gate (for example tournament incentive) is unresolved.

## Output

Report official C first, then C2 and C3 shadow comparisons when they exist.

When a WAIT resolution changes accounting precedence, also report the resulting accounting basis for that model (`DIRECT_BET / WAIT_ASSUMED / WATCH_ASSUMED / shadow equivalents / NONE`).

Never allow a C2/C3 live state to overwrite or substitute for the official C live plan.
