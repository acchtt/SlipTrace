# 01 — Work High Daily Sweep

Read `models/football/CURRENT_MODEL.md` first and treat it as the version authority. Follow the current official load order and the stage-relevant procedures/rules it declares. Never infer the active model version from this file.

Use the attached `AISCORE_FIXTURES_YYYY-MM-DD.txt` as the already-reconciled AiScore universe. Validate its source, ICT window, completeness flag, count consistency, and time/identity consistency. Do not rebuild the fixture universe.

Process every actionable fixture with full deep structural research under the current model. Produce and rank the current PRE states, then freeze the PRE artifact and batch-publish the exact frozen state to Airtable Daily Coverage Ledger `tblcl1UAyMqZT6Ub0` in base `appWyZJjitSBATXAU`.

This stage is price/XI blind. Do not use downstream Decision States or Website Picks. Do not run live, settlement, post-slate audit, or shadow comparison work here.

If the current model contains a later post-XI goal-environment/regime gate, preserve the structural evidence needed for it but do not classify that later regime during PRE unless `CURRENT_MODEL.md` explicitly moves the gate earlier.

Reconcile the complete actionable universe once at the end. Publishing is a copy/upsert, not a second structural screen. If Airtable differs from the frozen Work artifact, preserve the Work artifact and report a persistence sync fault.

Final response: current official model version, PRE counts, ranked FOCUS/WATCHLIST, Airtable publish PASS/FAIL, reconciliation PASS/FAIL.