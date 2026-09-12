# 01 — Work High Daily Sweep

Read the **upstream/default-branch** `models/football/CURRENT_MODEL.md` from `acchtt/SlipTrace` first and treat it as the version authority. Follow the current official load order and the stage-relevant procedures/rules it declares. Never infer the active model version from this file or from a locally cached repository copy.

## Upstream authority preflight

Before any football research:

1. read upstream `CURRENT_MODEL.md` once;
2. if a local/cached copy disagrees with upstream, **upstream wins immediately**;
3. do not spend Work usage investigating, diffing, or trying to rehabilitate the stale local cache;
4. load only the current upstream stage-relevant files and continue.

A stale local model is a cache fault, not a reason to run on old rules.

Use the attached `AISCORE_FIXTURES_YYYY-MM-DD.txt` as the already-reconciled, **scope-pruned Work handoff** produced by Step 0. Do not rebuild the raw fixture universe.

## HARD PRE-FLIGHT GATE — NO DEEP RESEARCH BEFORE PASS

Validate the handoff **before any match research or broad web search**.

The handoff must explicitly show all of the following:

- `source = AiScore`;
- requested ICT window/slate is present and coherent;
- `complete = true`;
- reconciliation/count invariant passed;
- terminal AiScore interval/date traversal passed;
- scope/registry audit passed;
- no schedule-integrity unresolved fixture appears in the Work fixture array;
- coverage skeleton publication is not marked failed;
- admitted fixture count matches the actual Work fixture array.

If **any** required item is false, missing, contradictory, provisional, or says traversal is incomplete, **STOP IMMEDIATELY**.

Return only a compact failure such as:

`HANDOFF INCOMPLETE — RERUN NORMAL CHAT STEP 0`

or, where appropriate:

`HANDOFF SCOPE FAULT — RERUN NORMAL CHAT STEP 0`

Do **not**:

- research the confirmed subset;
- publish a provisional Work board;
- search the web for omitted fixtures;
- traverse AiScore yourself;
- try to backfill the missing universe;
- create PRE grades for any fixture;
- touch Decision States or Website Picks.

An incomplete Step-0 universe is a **hard Work stop**, not permission to continue with `Reconciled = false`.

## Hard Work-usage boundary

Step 0 Normal Chat owns fixture discovery, scope filtering, cheap league admission, and coverage skeleton publication.

Therefore Work must **not**:
- traverse AiScore date pages again;
- run a second fixture sweep;
- search for fixtures omitted from the handoff;
- reconsider low-goal/Finnish/conditional-no-pass/model-quality exclusions;
- fetch opening odds, prematch odds, confirmed XI, or current bookmaker prices;
- spend deep-research usage on matches that Step 0 already filtered out.

Only after the hard pre-flight gate passes, treat the admitted fixture array as the complete Work research universe for that run.

The handoff should already have removed model-quality exclusions, low-goal domestic leagues, Finnish domestic leagues, and conditional-league fixtures that failed/no-data'd the cheap admission gate. **Do not reintroduce those fixtures and do not spend deep research usage reconsidering them.**

Process every fixture that survived into the valid Work handoff with full deep structural research under the current model. Produce and rank the current PRE states, then freeze the PRE artifact and batch-publish the exact frozen state to Airtable Daily Coverage Ledger `tblcl1UAyMqZT6Ub0` in base `appWyZJjitSBATXAU`.

This stage is price/XI/market-history blind. Do not use downstream Decision States or Website Picks. Do not run opening-odds watch, confirmed-XI review, live, settlement, post-slate audit, or shadow comparison work here.

If the current model contains a later post-XI goal-environment/regime gate, preserve the structural evidence needed for it but do not classify that later regime during PRE unless `CURRENT_MODEL.md` explicitly moves the gate earlier.

Reconcile the complete **Work-admitted** universe once at the end. Publishing is a copy/upsert, not a second structural screen. If Airtable differs from the frozen Work artifact, preserve the Work artifact and report a persistence sync fault.

## Final response

If pre-flight fails, stop with the applicable handoff failure code and **zero fixtures researched**.

If pre-flight passes, return: current official model version, number of Work-admitted fixtures processed, PRE counts, ranked FOCUS/WATCHLIST, Airtable publish PASS/FAIL, reconciliation PASS/FAIL.