# Football Chat Operating Protocol

**Status:** ACTIVE  
**Canonical model entry point:** `models/football/CURRENT_MODEL.md`

This file is intentionally small. It must not duplicate version-specific rules from the model stack.

## Authority order

1. `models/football/CURRENT_MODEL.md`
2. The active procedures/rules referenced by its canonical load order
3. Frozen Work PRE persisted to the Daily Coverage Ledger
4. Airtable Decision States for later XI/market/live assessments
5. User-supplied current XI, odds, and live-state evidence

For current work, load `CURRENT_MODEL.md` first. Do not reconstruct the active model from old handoffs, backups, Git history, or memory.

## Workflow

- Sweep / discovery: use the current sweep and time-integrity procedures referenced by `CURRENT_MODEL.md`.
- PRE / Step 1: `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`
- XI + odds / Step 2: `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`
- QA / promotion: `models/football/procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md`
- Launchers and resumable handoffs: `handoffs/football/`

Frozen historical PRE remains immutable. Current execution decisions and actual exposure must be persisted separately.

If this protocol conflicts with `CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.
