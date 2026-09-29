# Football Chat Operating Protocol

**Status:** ACTIVE  
**Canonical model entry point:** `models/football/CURRENT_MODEL.md`  
**Current official model:** Football C

## Authority order

1. `models/football/CURRENT_MODEL.md`
2. `models/football/production/FOOTBALL_C.md`
3. current stage launcher under `models/football/prompts/`
4. frozen Football C board state in Daily Coverage Ledger
5. Football C Decision States
6. user-supplied current XI/odds/live evidence
7. user bet slip for physical execution truth

Do not load Football A's rule stack into a new Football C decision.

Historical decisions remain governed by the model/version that actually produced them.

## Workflow

- Step 0: AiScore handoff
- Step 1: integrated C board
- Step 2: integrated XI + fresh web research + H2H + odds decision
- Live: predeclared WAIT resolution
- Audit: version-faithful settlement/process audit

Frozen historical states remain immutable.

If this protocol conflicts with `CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.
