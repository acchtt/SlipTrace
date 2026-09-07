# Football Model

This directory contains the files required to operate the current **Football v0.2.47 CLEAN official + v0.2.48-SHADOW** workflow.

## Active files

- `CURRENT_MODEL.md` — active versions, load order, coverage directive, and operating state.
- `procedures/FOOTBALL_COVERAGE_CONTROLLER.md` — mandatory full-slate reconciliation and screen-every-fixture controller shared by both models.
- `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` — clean original v0.2.47 rule source restored from Aug 16, 2026 Git history.
- `rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md` — forward-test candidate; parallel only, never official P/L unless explicitly promoted.
- `procedures/FOOTBALL_BETTING_PROCEDURE.md` — PRE, XI, market, dual-model verdict, live, settlement, and audit workflow.
- `airtable/FOOTBALL_COVERAGE_AIRTABLE.md` — Daily Coverage Ledger contract.
- `airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md` — official/shadow decision-state logging contract.

## Coverage control plane

The active workflow no longer begins by selecting a few `credible candidates`.

It now requires:

`RECONCILED FIXTURE UNIVERSE → ELIGIBILITY → SCREEN EVERY ELIGIBLE FIXTURE → FOCUS/WATCHLIST/PASS → XI RERANK → MARKET → TWO MODEL OUTCOMES`

Daily coverage is persisted to Airtable `Daily Coverage Ledger` so FOCUS/WATCHLIST matches cannot silently disappear when the visible board is shortened or when the user later asks `what's next?`.

The user-facing board may remain concise. The internal screened universe must reconcile completely.

## Model tracks

### Official

Football **v0.2.47 CLEAN**

- can issue official LOCK/HOLD/PASS;
- official locks enter Website Picks and official P/L.

### Shadow

Football **v0.2.48-SHADOW**

- uses the same fixture universe, PRE evidence, XI, and market snapshot;
- can issue SHADOW LOCK/HOLD/PASS;
- never enters official P/L unless explicitly promoted.

## Archive

- `archive/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md` — archived consolidated/restored-core variant. Retained for provenance only; never load it into active decisions.

Historical incremental rule files, old audit/shadow procedures, dated handoffs, benchmarks, and process-review documents remain available through Git history rather than the active load order.

## Principle

**Coverage first, selection second. Every eligible fixture gets a disposition. Shorten the display, not the screened universe. Persist FOCUS and WATCHLIST. Keep clean v0.2.47 official and v0.2.48 shadow separate.**