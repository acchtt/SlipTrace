# Football v2 — Current Model Authority

## ACTIVE STACK

This file describes only the current production path.

- **Official and only active model:** Football C.
- **Retired models:** C2, C3 and C4.
- Historical C2/C3/C4 receipts, boards and accounting rows remain immutable
  and may be read for audit only. They never participate in new /rank, /xi,
  /live, accounting or publication.
- **Active source/rank stages:** Football V4 only.
- **Active Airtable model base:** appbzxqXYf0lKfD4P.
- **User P/L authority:** Actual Bets — Current only.

The active command surface is:

- /sweep -> models/football/stages_v4/SWEEP.md
- /rank -> models/football/stages_v4/RANK.md
- /xi and /xi exception -> models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md
- /live -> the same Football C assessment with current live state
- /audit -> models/football/prompts/04_WORK_POST_SLATE_AUDIT.md
- /report -> models/football/prompts/06_NORMAL_CHAT_REPORT.md

Retired V1-V3 source/checkpoint/ZIP machinery and retired model policies are
not production dependencies.

## Production sequence

SOURCE DATE SURFACES -> V4 GOALS-FIRST INTAKE -> V4_SWEEP_READY ->
ORIGINAL-SOURCE REPLAY + FRESH FULL-COHORT STATUS -> FOOTBALL C BOARD ->
ONE AIRTABLE READBACK -> /xi FOOTBALL C -> OPTIONAL OBSERVED-QUOTE
EVALUATION OR STRICT C PRICE DECISION -> ONE DECISION READBACK/PUBLICATION
GATE -> LIVE/AUDIT

There is no active shadow model and no model-voting/consensus layer.

## /sweep — V4 goals-first intake

Authority: stages_v4/SWEEP.md plus the V4 source/intake modules.

The sweep must acquire complete provider date surfaces before filtering, apply
the standing league/user exclusions, and use source-backed goal evidence to
admit GOAL_PRIORITY fixtures. Intake never requires odds or lineups.

The high-rate alternate research path is active alongside the original
route-composite path. Both are research admission only; neither creates a goal
certificate, supported burden or bet.

## /rank — Football C only

Authority: stages_v4/RANK.md and stages_v4/stage.py.

Before C board execution:

1. load the native V4 sweep receipt and unchanged original source;
2. replay the original source;
3. refresh kickoff/status for the full eligible cohort;
4. remove already-started/source-changed fixtures explicitly;
5. research the complete eligible cohort in goal-first order;
6. freeze the Football C evidence fields;
7. execute the deterministic C board once;
8. persist exact C result JSON plus C board/rank/lane fields;
9. independently refetch once and verify.

### Ranking order

The active C ranking key is:

1. certificate robustness;
2. highest funded certificate G6 > G5 > G4 > G3 > none;
3. endpoint/control risk;
4. frozen V4 quantitative goal signal;
5. remaining C football-mechanism quality.

Compiled burden magnitude itself is not a ranking bonus. A fragile G4/G5 does
not automatically outrank a robust or conditional G3.

## Football C supported-burden compiler

Production supported burden is compiled from explicit goal certificates:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50
- no G3 -> no certified burden

Asian .75 lines require the next certificate for a full win.

G3 may be funded by the explicit C carrier, two-route, distributed or
matchup-leakage mechanisms. Market prices cannot manufacture certificates.

The research-declared supported line remains audit metadata only.

## Availability / evidence symmetry

Availability may downgrade a certificate only when it attacks an identified
scoring mechanism after alternative creators/scorers, opponent independent
routes and defensive-rotation leakage are checked.

Domestic/cup/red-card inflated scorelines must not be promoted merely because
raw 3+/4+ rates are high. Current route reliability, chance quality, failure
resistance and evidence confidence remain independently required by the C
certificate/robustness rules.

The UCL reconciliation is calibration evidence, not a league-specific boost.
There is no automatic UCL or Norway adjustment.

## /xi — one C assessment and one price policy

Authority: prompts/02_NORMAL_CHAT_XI_ODDS.md,
procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md, engine/core.py,
engine/adapter.py and engine/xi_portable.py.

Every /xi:

1. completes Football C assessment without requiring odds;
2. if the user supplied an observed screenshot, evaluates exactly that quote
   through adapter.evaluate_observed_quote();
3. if a genuinely executable current prematch quote exists, uses
   adapter.run_decision();
4. persists/readbacks once when persistence is required.

There is no second screenshot-specific ACT/WAIT/PASS policy and no second model
whose result can override or dilute C.

### Screenshot/market disagreement

Use only the user-supplied quote when that is the declared evidence source.
Do not fetch a replacement quote.

If the observed market burden materially exceeds C's certified burden, the
disagreement may trigger one football-evidence recheck. It never enters the
ranking key and never creates G3/G4/G5/G6.

### WAIT

WAIT requires:

- wait_reachable=true;
- a non-empty football/market reachability basis;
- wait_requires_negative_info=false;
- intact current football thesis;
- no material veto.

A lone screenshot does not prove same-line odds will improve. Near kickoff,
do not manufacture a micro-WAIT from a speculative price drift.

The normal minimum price is 1.65. The supported-line 1.60 soft zone is allowed
only by the C core where the already-funded burden has the required independent
football corroboration. Unsupported higher burdens do not inherit that zone.

## /live

Started fixtures use the same Football C football assessment with current
score/minute/material events.

After kickoff:

- continue football assessment;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/WAIT/PASS retrospectively;
- a live quote is comparison evidence only unless a separate live execution
  policy explicitly authorizes it.

## Persistence and accounting

ACTIVE_MODEL_ROUTING.json is the machine-readable routing authority.

For new operations:

- persist only active Football C model outputs;
- retired C2/C3/C4 fields may remain in Airtable for immutable historical rows
  but are not required or written for new C decisions;
- WATCH creates no model bet;
- Unresolved WAIT creates no model bet;
- only a strict direct C BET or a user-confirmed reached WAIT may enter model
  accounting;
- Actual Bets — Current is the only authority for physical user P/L.

## Deterministic runtime

The active /xi runner is thin. It imports core.py and adapter.py directly.
No duplicate embedded model source and no pair/consensus wrapper is part of
normal execution.

The old board_pair_cli.py, decision_pair_cli.py and C2 challenger documents may
remain solely for frozen historical audit/regression. Active launchers,
routing, CI and production stages must not import or require them.

## Audit invariant

/audit compares frozen prospective evidence with outcomes without rewriting
history. Retired-model history can be inspected, but only Football C may
produce a new production model judgment.
