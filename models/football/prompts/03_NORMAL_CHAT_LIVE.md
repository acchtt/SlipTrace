# 03 — Normal Chat: Football C Official Live + C2/C3 Shadow Wait

**Command alias:** `/live`

Read:
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`

Football C is official. C2 and C3 are shadow-only.

## Common live evidence

For a supplied live fixture, freeze one current live state:
- score/minute;
- cards/injuries;
- material tactical/mechanism changes;
- current quote;
- attacking-quality indicators relevant to the original thesis;
- current tournament/aggregate/table state when applicable;
- whether a draw is acceptable;
- whether extra time/direct penalties are reachable;
- whether goal difference/margin still matters;
- which side is genuinely forced to chase.

Use this same live state for C, C2 and C3 when a corresponding predeclared shadow WAIT exists.

## Football C official WAIT resolution

Retrieve the exact official C-WAIT plan.

Core rule:

`TARGET REACHED + THESIS STILL HEALTHY?`

A target number alone never authorizes C-BET.

If price improved because the attack has gone stale:

`C-WAIT CANCELLED — THESIS DECAY`

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

Persist official material state. If C-BET occurs, reconcile Website Pick.

## Football C2 shadow WAIT resolution

If a predeclared C2-WAIT exists, resolve it separately using the same common live evidence and its own target/cancellation conditions.

C2 may produce:
- `C2-BET — SHADOW`
- `C2-WAIT — SHADOW`
- `C2-WAIT CANCELLED — THESIS DECAY — SHADOW`
- `C2-PASS — NEW EPOCH — SHADOW`

C2 may never create Website Pick or real exposure.

## Football C3 shadow WAIT resolution

If a predeclared C3-WAIT exists on a fixture already in the normal live workflow, resolve it from the same live epoch.

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

## Output

Report official C first, then C2 and C3 shadow comparisons when they exist.

Never allow a C2/C3 live state to overwrite or substitute for the official C live plan.
