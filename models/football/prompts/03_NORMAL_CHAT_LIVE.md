# 03 — Normal Chat: Football C Live / WAIT Resolution

Read `models/football/CURRENT_MODEL.md` and `models/football/production/FOOTBALL_C.md`.

Football C is the active official model.

Normal live use is to resolve a **predeclared C-WAIT**. Do not create opportunistic new live candidates unless the user explicitly asks for a fresh exceptional reassessment.

## Resolve a WAIT

Retrieve the exact predeclared plan:
- target line;
- minimum odds;
- original supported burden;
- original routes/carrier/failure mode;
- cancellation conditions;
- required thesis-health evidence.

Then verify the current score, minute, cards/injuries/material tactical changes and current quote.

Core rule:

`TARGET REACHED + THESIS STILL HEALTHY?`

A target number alone never authorizes C-BET.

For scoreless Over waits, no-goal/no-red-card alone is insufficient. Require current evidence that the original scoring mechanism is functioning: credible high-value chances, dangerous box/central entries, threatening keeper work/quality SOT, productive dangerous transitions, or another predeclared mechanism.

If price improved because attack quality has gone stale:

`C-WAIT CANCELLED — THESIS DECAY`

If a goal/red card/major injury/material mechanism change occurred, invalidate the old quote and reassess the new epoch. Never mechanically carry the old quote.

## Output

First line must be one of:
- `C-BET — <line> @ <odds>`
- `C-WAIT — TARGET NOT YET READY`
- `C-WAIT CANCELLED — THESIS DECAY`
- `C-PASS — NEW EPOCH INVALIDATES PLAN`

Then give the shortest football reason needed.

## Persistence

Persist the material live state to Decision States under model `Football C`.

If C-BET occurs, also create/reconcile the Website Pick. Actual bet slip remains physical execution truth.
