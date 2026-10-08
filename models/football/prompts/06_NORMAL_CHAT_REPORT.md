# 06 — Normal Chat: Football Report

**Command alias:** `/report`  
**Current roster:** Football C official + Football C2 shadow.

Read `models/football/CURRENT_MODEL.md` and current persisted state first.

This launcher is read-only. It summarizes already-existing football state and must not silently rerun Step 0, Step 1, Step 2, live assessment, or predictive ranking.

## Current report scope

When relevant, report:
- current board/window;
- Step-0 funnel/capacity state;
- Football C official state/rank/line/lane;
- Football C2 shadow state/rank/line;
- current C+C2 Step-2 actions;
- Website Pick / official C exposure state;
- C/C2 model-accounting state;
- current WAIT plans;
- runtime/persistence blockers;
- upcoming kickoff/status after factual revalidation when requested.

C3/C4 are retired. Do not show them as current tracks or counters.

Historical C3/C4 data may appear only in an explicitly historical audit/report when:
- the record was genuinely prospectively frozen during that model's active era; and
- the historical comparison is relevant to the user's requested scope.

## `/report current board`

Show the latest frozen:
- board window;
- C official ranking/state/line;
- FOLLOW / RESERVE / STOP lane;
- C2 shadow ranking/state/line;
- replenishment state;
- pair-reconciliation status;
- persistence/runtime status.

Do not rerank.

## `/report latest decisions`

Show latest material Decision States:
- C Action;
- C supported line;
- C2 Shadow Action;
- C2 supported line;
- engine C+C2 pair status;
- official Website Pick state;
- WAIT target/min odds when relevant;
- active accounting result.

Do not reconstruct missing C2 from C.

## `/report next matches`

Daily Coverage is frozen history, not proof a fixture is still upcoming.

Revalidate only the factual schedule/status necessary for the report:
- correct ICT kickoff;
- remove LIVE/HT/FT/postponed/cancelled fixtures from upcoming;
- annotate material schedule corrections.

This factual refresh does not authorize reranking/reassessment.

## WAIT display

Show C/C2 WAIT plans using each model's own:
- target line;
- minimum odds;
- accounting basis;
- current known resolution.

Do not label a WAIT "not reached" unless the user explicitly said so.

C official model-accounting and actual user execution remain separate.

## Accounting

Current forward accounting is C+C2 only.

For WATCH:
`WATCH_ASSUMED O<supported line> @1.65 1u`
with the shadow equivalent for C2.

For WAIT:
use that model's frozen target/min odds.

Historical retired-model accounting belongs only in an explicitly historical appendix using frozen historical rows.

### Actual user profit

Use Airtable `Actual Bets — Current` (`tblF0MSRTuqCWlL8s`) as the canonical source for current actual-user P/L from the 2026-10-08 reset onward.

Unless the user explicitly asks for historical combined reporting:
- sum `Profit VND` only from this table;
- turnover is the sum of `Stake VND` from this table;
- ROI is total profit / total stake for this table;
- do not infer actual bets from Website Picks, Decision States, C/C2 model accounting, WATCH/WAIT records, or shadow exposure.

## Boundaries

`/report` must not:
- create a new sweep;
- repair Step 0;
- rerank;
- reassess XI;
- execute a new live decision;
- manufacture a new model verdict;
- backfill C2/C3/C4 after outcome.

If the user asks for new predictive work, route to the corresponding launcher.
