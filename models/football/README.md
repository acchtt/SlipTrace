# Football Model

This directory contains the files required to operate the current **Football v0.2.47** workflow, with the clean original v0.2.47 rules restored from Git history.

## Active files

- `CURRENT_MODEL.md` — active version, load order, and current operating layer.
- `rules/MODEL_RULES_FOOTBALL_V0.2.47.md` — clean original v0.2.47 rule source restored from the Aug 16, 2026 history.
- `procedures/FOOTBALL_BETTING_PROCEDURE.md` — daily slate, XI, odds, live, and settlement workflow.
- `airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md` — current decision-state logging contract.

## Shadow candidate

- `rules/MODEL_RULES_FOOTBALL_V0.2.48-SHADOW.md` — forward-test candidate only; never part of official P/L unless explicitly promoted.

## Archive

- `archive/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md` — archived consolidated/restored-core variant. It is retained for provenance only and must not be loaded into official decisions.

Historical incremental rule files, old audit/shadow procedures, dated handoffs, benchmarks, and process-review documents remain available through Git history rather than the active load order.

## Principle

Use the clean original v0.2.47 source as the base rule file, `CURRENT_MODEL.md` plus the procedure as the current operating layer, and one decision-state control plane. Do not silently reintroduce the archived `-R` variant or reconstruct the active workflow by stacking unrelated historical rules.
