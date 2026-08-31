# Football Model

This directory contains only the files required to operate the current **Football v0.2.47-R** workflow.

## Active files

- `CURRENT_MODEL.md` — active version, load order, and operating state.
- `rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md` — consolidated model rules.
- `procedures/FOOTBALL_BETTING_PROCEDURE.md` — daily slate, XI, odds, live, and settlement workflow.
- `airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md` — current decision-state logging contract.

Historical incremental rule files, old audit/shadow procedures, dated handoffs, benchmarks, and process-review documents are intentionally not part of the active directory. Git history is the archive.

## Principle

Use one canonical model, one operating procedure, and one decision-state control plane. Do not reconstruct the current workflow by stacking old model versions.