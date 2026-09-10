# 01 — Work High Daily Sweep

Read `models/football/CURRENT_MODEL.md` first and treat it as the version authority. Follow the current official load order and the stage-relevant procedures/rules it declares. Never infer the active model version from this file.

Use the attached `AISCORE_FIXTURES_YYYY-MM-DD.txt` as the already-reconciled, **scope-pruned Work handoff** produced by Step 0. Validate its source, ICT window, completeness flag, count consistency, time/identity consistency, and scope metadata. Do not rebuild the raw fixture universe.

The handoff should already have removed model-quality exclusions, low-goal domestic leagues, Finnish domestic leagues, and conditional-league fixtures that failed/no-data'd the cheap admission gate. **Do not reintroduce those fixtures and do not spend deep research usage reconsidering them.**

Process every fixture that actually survived into the Work handoff with full deep structural research under the current model. Produce and rank the current PRE states, then freeze the PRE artifact and batch-publish the exact frozen state to Airtable Daily Coverage Ledger `tblcl1UAyMqZT6Ub0` in base `appWyZJjitSBATXAU`.

This stage is price/XI blind. Do not use downstream Decision States or Website Picks. Do not run live, settlement, post-slate audit, or shadow comparison work here.

If the current model contains a later post-XI goal-environment/regime gate, preserve the structural evidence needed for it but do not classify that later regime during PRE unless `CURRENT_MODEL.md` explicitly moves the gate earlier.

Reconcile the complete **Work-admitted** universe once at the end. Publishing is a copy/upsert, not a second structural screen. If Airtable differs from the frozen Work artifact, preserve the Work artifact and report a persistence sync fault.

If the Step-0 handoff is missing its scope/registry audit or appears to contain excluded/conditional-no-pass leagues, stop and report `HANDOFF SCOPE FAULT` rather than consuming Work usage on those matches.

Final response: current official model version, number of Work-admitted fixtures processed, PRE counts, ranked FOCUS/WATCHLIST, Airtable publish PASS/FAIL, reconciliation PASS/FAIL.