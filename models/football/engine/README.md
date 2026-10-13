# Football engine — active runtime

## Active production modules

- core.py — C/C2 deterministic football and quote policy.
- adapter.py — structured board, football-assessment, observed-quote and strict
  decision adapters.
- board_pair_cli.py — paired C/C2 Step-1 board execution.
- decision_pair_cli.py — paired C/C2 football/strict decision execution.
- xi_portable.py — thin user-facing /xi runner over the shared modules.
- step2_queue_guard.py — verifies the sealed V4 rank+persistence chain and due
  routine/exception authorization.
- xi_assessment_reconcile.py — one Decision State assessment readback.
- step2_publication_guard.py — final strict-pair readback/freshness gate.
- model_bet_accounting.py — actual-terms-only model accounting; no synthetic
  WATCH or unresolved WAIT exposure.

V4 /sweep and /rank live under models/football/stages_v4/. Source-provider diagnostics live under stages_v4/tools/, not the model engine.

## /xi

Quote-free football:

python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json

Observed user screenshot:

python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json --screenshot-quote screenshot.json

Strict executable current price:

python models/football/engine/xi_portable.py xi --c c_football.json --c2 c2_football.json --price-c c_price.json --price-c2 c2_price.json

The observed quote and strict price paths use the same core C/C2 quote policy.
Only the strict path can gain execution authority.

## WAIT

WAIT requires explicit reachability evidence in the current model context.
There is no wrapper-only fixed gap rule.

WATCH and unresolved WAIT create no model exposure.

## Retired/dormant source

Older Step0/V1-V3 checkpoint, repaired-handoff, compact-capacity, legacy rank
reconciliation, session-wide Step2 reconciliation, source-handoff/embedded
portable and kickoff-transition modules are historical only.

They are not imported by active launchers or production CI. Git history is the
audit authority for those implementations.

Experimental goal probability/price-shadow tools are QA/trials only and cannot
authorize C/C2 actions.
