# Retired Football Model Artifacts

**Status:** HISTORICAL SOURCE ONLY  
**Effective retirement:** 2026-10-06  
**Current production roster:** Football C official + Football C2 shadow

This document defines the boundary between current production code and retired C3/C4 history.

## Current rule

C3 and C4 must not participate in a new/current:
- /rank board;
- /xi decision;
- /live action;
- Website Pick;
- active model-accounting payload;
- forward model-comparison metric.

"All models" means the active roster: C + C2.

## Preserved historical records/specifications

The following may remain in the repository because they document old prospective work:

- `models/football/challengers/football-c3/**`
- `models/football/challengers/football-c4/**`
- `models/football/airtable/FOOTBALL_C3_AIRTABLE.md`
- `models/football/airtable/FOOTBALL_C4_AIRTABLE.md`
- dated historical QA/audit artifacts;
- historical Airtable C3/C4 columns and frozen records;
- Git history from the period in which those challengers were active.

These surfaces are documentation/history only. They are not current runtime dependencies.

## Removed executable artifacts

The active repository no longer carries the old executable C3/C4 surfaces:

- `models/football/engine/board_triplet_cli.py`
- `models/football/engine/decision_triplet_cli.py`
- `models/football/engine/c4_semantic.py`
- `models/football/engine/c4_semantic_cli.py`
- `models/football/engine/c4_schema.json`
- the active C4 semantic test suite.

Their exact source remains recoverable from Git history at the revisions where they were active.

Do not restore these files merely to replay a historical result against today's engine.

## Active production files must not depend on retired models

Current active surfaces must be C+C2-only:
- `CURRENT_MODEL.md`
- current launchers and command aliases;
- `engine/core.py`
- `engine/adapter.py`
- `engine/schema.json`
- `engine/runtime_probe.py`
- `engine/xi_portable.py`
- current bootstrap/reconciliation/accounting procedures.

The active engine must not expose:
- C3 policy classes/functions;
- C3 schema model choices/fields;
- model=c3/model=c4 execution;
- triplet execution;
- C4 rank compilation.

## Historical audit fidelity

Do not delete or rewrite prospectively frozen historical C3/C4 data.

Historical retired-model settlement is allowed only when:
1. the historical row was genuinely frozen before outcome;
2. the model's own line/action/accounting basis exists;
3. no missing state is reconstructed from FT/current information.

Use explicit historical accounting mode where supported.

## Historical executability

Current production code is not required to execute retired models.

If an old C3/C4 result must be investigated:
- use the frozen persisted result first;
- use the original Git revision if code inspection is required;
- never transplant retired code back into current production to manufacture missing output.

## CI rule

Production QA must fail if a current launcher/runtime/schema reintroduces retired-model execution semantics.

Historical documentation may mention C3/C4 when clearly labeled historical/retired.
