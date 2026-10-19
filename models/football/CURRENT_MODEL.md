# Football v2 — Current Model Authority

## ACTIVE STACK

This file describes only the current production path.

Prospective G4 research uses `procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md`:
negative, mixed and evidence-limited findings are distinct. Native evidence
diagnostics and production-scope checks apply without changing C thresholds.

- **Official and only active model:** Football C.
- **Retired models:** C2, C3 and C4.
- Historical C2/C3/C4 receipts, boards and accounting rows remain immutable
  and may be read for audit only. They never participate in new /rank, /xi,
  /live, accounting or publication.
- **Active source/rank stages:** Football V4 only.
- **Active operational store:** Google Sheets `Football v2 — Active Operations` (`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`).
- **User P/L authority:** Actual Bets — Current only.

The active command surface is:

- /sweep -> models/football/stages_v4/SWEEP.md
- /rank -> models/football/stages_v4/RANK.md
- /xi and /xi exception -> models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md
- /live -> the same Football C assessment with current live state
- /audit -> models/football/prompts/04_NORMAL_CHAT_AUDIT.md
- /audit deep -> models/football/prompts/04_WORK_POST_SLATE_AUDIT.md (internal escalation target)
- /report -> models/football/prompts/06_NORMAL_CHAT_REPORT.md

### Conversation/runtime routing

- **Normal chat:** `/sweep`, `/xi`, `/xi exception`, `/live`, `/audit`, `/report`.
- **ChatGPT Work:** `/rank`; `/audit deep` only after normal `/audit` emits `DEEP AUDIT REQUIRED`.

Conversation type is an operational surface, not model authority. Football C and
the native V4/runtime receipts remain authoritative regardless of chat surface.
For `/xi`, normal chat gathers evidence but official ACT/WAIT/PASS is owned by
`engine/core.py` + `engine/adapter.py` + `engine/xi_portable.py`. When
local execution is unavailable, normal chat must use the on-demand GitHub XI
runtime bridge and consume its persisted result in the same turn. Local Python
absence by itself is **not** grounds for ANALYSIS_ONLY. ANALYSIS_ONLY remains the
last-resort state only when the deterministic runtime and backend are genuinely
unavailable or return a concrete failure.


Retired V1-V3 source/checkpoint/ZIP machinery and retired model policies are
not production dependencies.

## Production sequence

SOURCE DATE SURFACES -> V4 GOALS-FIRST INTAKE -> V4_SWEEP_READY ->
ORIGINAL-SOURCE REPLAY + FRESH FULL-COHORT STATUS -> FOOTBALL C BOARD ->
ONE GOOGLE SHEETS READBACK -> /xi FOOTBALL C -> OPTIONAL OBSERVED-QUOTE
EVALUATION OR STRICT C PRICE DECISION -> ONE DECISION READBACK/PUBLICATION
GATE -> LIVE/AUDIT

There is no active shadow model and no model-voting/consensus layer.

## /sweep — V4 goals-first intake

**Conversation surface: NORMAL CHAT.**

Authority: stages_v4/SWEEP.md plus the V4 source/intake modules.
Normal chat acquires the requested window once, performs targeted goal-history
research directly, and emits the same native V4 source/receipt contract consumed
by Work `/rank`. Work acquisition/orchestration is fallback infrastructure,
not the default sweep route.

A sweep with actionable upstream research still pending after a genuine
tool/provider failure is a checkpoint, not a completed handoff. Normal source
acquisition, bounded history research, native V4 execution and durable
rank-handoff persistence are one backend unit and must not be exposed as
separate user Resume steps. Preserve the source snapshot and resume only the
unresolved queue after a real interruption. If a partial verified subset is
handed to rank, both stages must label it PARTIAL and preserve the exact upstream
pending count.


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

Research completion and persistence verification are separate. New rank receipts
freeze all eligible dispositions and reusable factual C input. Unfinished
research stays in an ordered resume queue; bare evidence-missing labels cannot
establish completed research. `V4_RANK_PARTIAL_PERSISTENCE_VERIFIED` verifies the
assessed board while explicitly retaining unresolved work. Repeated `/rank` on
the same source epoch resumes its native checkpoint and reuses completed facts.
No predictive C thresholds or sweep admission rules change through this repair.

### Ranking calibration

C ranks certificate robustness and depth first. For C G3, a structure with both
MEDIUM burden-completion quality and MEDIUM continuation is capped at
CONDITIONAL even when the frozen Step-0 rate signal is strong. Within equal
robustness/depth, current continuation and completion are compared before raw
historical goal-rate strength.

This prevents a Hearts-style medium-completion G3 from taking rank priority
solely because its historical goal signal is stronger than a current higher-
completion certificate.

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

## Upper-tail evidence transferability

C distinguishes **confidence** from **transferability**.

Evidence can be confidently observed yet still be a poor predictor of the
current goal-four-plus tail when it is materially driven by weak-opposition,
domestic/cup, red-card or otherwise distorted contexts.

Whenever `independent_upper_tail=true`, current C research must freeze:

- `upper_tail_transferability = LOW / MEDIUM / HIGH`;
- a non-empty `upper_tail_transferability_basis`.

Deterministic effect:

- LOW -> G4/G5/G6 cannot be funded;
- MEDIUM -> G4+ may be funded but certificate robustness is capped at
  CONDITIONAL;
- HIGH -> normal G4+ robustness rules apply.

This is not a league penalty. Comparable current senior mechanisms can remain
HIGH in any competition. Raw goal rates cannot upgrade transferability and
later match outcomes never rewrite it.

### G4 completion reliability

Transferability alone does not certify the fourth goal. C now distinguishes a
self-funded/strong-route completion from a fourth goal that depends on a more
fragile opponent reply.

For G4:

- a STRONG carrier path must have HIGH route reliability, unless both scoring
  routes are independently STRONG with HIGH independent-route quality;
- a reply-dependent TWO_SIDED/MIXED path with only one STRONG route requires
  HIGH failure resistance;
- two independently STRONG routes may retain G4 with MEDIUM failure resistance.

This preserves genuine City/Villa/Brighton/Lech and two-strong-route shapes
while preventing a broad high-goal history from upgrading a fragile 3+1/2+2
completion path.

C now freezes a second structured field for G4+:
`upper_tail_comparable_context_signal` = SUPPORTIVE / MIXED / SUPPRESSIVE /
UNAVAILABLE, with a factual basis.

Evidence hierarchy is prospective and ordered:

1. same competition / continental context;
2. closely comparable senior opponent/competition strength;
3. domestic/cup history as corroboration only.

If the closest available context is SUPPRESSIVE, effective upper-tail
transferability is forced to LOW even when domestic scoring rates and the raw
transferability grade are HIGH. MIXED caps it at MEDIUM. This prevents
less-comparable domestic blowouts from overriding a contradictory continental
sample.

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

**Conversation surface: NORMAL CHAT; deterministic runtime remains decision authority.**

Authority: prompts/02_NORMAL_CHAT_XI_ODDS.md,
procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md, engine/core.py,
engine/adapter.py and engine/xi_portable.py.

Every /xi:

1. completes Football C assessment without requiring odds;
2. executes the deterministic runtime directly when callable, otherwise through
   `xi_runtime_backend.py` via the request/result GitHub bridge;
3. if the user supplied an observed screenshot, evaluates exactly that quote
   through adapter.evaluate_observed_quote();
4. if a genuinely executable current prematch quote exists, uses
   adapter.run_decision();
5. persists/readbacks once when persistence is required.

The backend bridge is transport only. It does not create a second policy, fetch
replacement odds, or loosen Football C.

There is no second screenshot-specific ACT/WAIT/PASS policy and no second model
whose result can override or dilute C.

### Screenshot/market disagreement

Use only the user-supplied quote when that is the declared evidence source.

A ranked fixture also carries its frozen board certificate into `/xi`. A
higher screenshot burden can never authorize an upgrade by itself.

If the observed market burden materially exceeds C's certified burden, the
disagreement triggers one independent football-evidence recheck. That recheck
may produce a higher current certificate only through one of three explicit
paths:

- genuinely changed football evidence:
  `VERIFIED_NEW_FOOTBALL_EVIDENCE`;
- previously incomplete G4 research:
  `VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH`;
- a source-backed correction where rank had marked G4 complete-rejected but the
  same prospective evidence was misclassified/underweighted:
  `VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION`.

The third path must name the reclassified G4 fields and verify upper-tail
transferability plus comparable context with non-market evidence. The market
remains only the trigger and never creates G3/G4/G5/G6.

Do not fetch a replacement quote.

### Fragile WATCH WAIT activation

A WATCH certificate can remain visible for research when it is FRAGILE, but a
reachable price does not by itself convert that fragile thesis into WAIT. C
requires the current WATCH assessment to revalidate to at least CONDITIONAL
before WAIT is emitted. FOCUS retains the normal reachability and football-veto
rules.

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

**Conversation surface: NORMAL CHAT; deterministic Football C assessment remains authority.**

Started fixtures use the same Football C football assessment with current
score/minute/material events.

After kickoff:

- continue football assessment;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/WAIT/PASS retrospectively;
- a live quote is comparison evidence only unless a separate live execution
  policy explicitly authorizes it.

## Persistence and accounting

`models/football/google_sheets/ACTIVE_STORE_ROUTING.json` is the machine-readable routing authority.

For new operations:

- persist only active Football C model outputs;
- retired C2/C3/C4 fields may remain in historical Airtable rows for immutable audit only; all new C persistence uses Google Sheets;
- WATCH creates no model bet;
- Unresolved WAIT creates no model bet;
- only a strict direct C BET or a user-confirmed reached WAIT may enter model
  accounting;
- Actual Bets — Current is the only authority for physical user P/L.

## Website projection

The private Google Sheets workbook is not exposed to the public website.

After a verified rank persistence change or verified Website Pick change,
refresh the public-safe projection using
`models/football/google_sheets/public_projection.py` and update
`acchtt/football-v2/pages/data/board-feed.json`.

Only Daily Coverage Ledger and Website Picks are valid projection inputs.
Decision States, Actual Bets, engine-result JSON and generic payload JSON must
never be published. Website tier mapping FOLLOW→FOCUS, RESERVE→WATCHLIST and
STOP→PASS remains display-only.

The projection is a view of already-verified Sheets state. It cannot authorize
a model decision or physical exposure.

## Deterministic runtime

The active /xi runner is thin. It imports core.py and adapter.py directly.
No duplicate embedded model source and no pair/consensus wrapper is part of
normal execution.

The old board_pair_cli.py, decision_pair_cli.py and C2 challenger documents may
remain solely for frozen historical audit/regression. Active launchers,
routing, CI and production stages must not import or require them.

## /audit — lightweight diagnosis with automatic deep escalation

**Conversation surface: NORMAL CHAT by default.**

Routine `/audit` reads only the relevant frozen receipts/rows/evidence needed
for the incident or slate. It diagnoses screening, ranking, certificate,
WAIT/execution, availability/incentive and workflow failures without rewriting
history and without loading the whole repository by default.

The user does not need to decide whether a deep audit is required. Normal
`/audit` escalates only when it detects a structural implementation problem,
for example:

- the same defect pattern repeats across multiple fixtures/slates;
- authoritative Football C rules or launchers conflict;
- source/persistence/runtime integrity cannot be resolved from the relevant
  receipts alone;
- fixing the defect requires repository-wide inspection, code changes or
  regression tests.

When escalation is justified, normal `/audit` must end with
`DEEP AUDIT REQUIRED` and emit a compact handoff containing the affected
fixtures/receipts, frozen prospective evidence, defect class, suspected
rule/runtime area, what has already been ruled out, and the exact questions or
tests for Work. It must not duplicate a repo-wide investigation in normal chat.

`/audit deep` is the Work-only escalation target. It consumes that compact
handoff, performs the broader repository/regression investigation, and may patch
code only when the user has explicitly requested implementation.

## Audit invariant

All audit modes compare frozen prospective evidence with outcomes without
rewriting history. Retired-model history can be inspected, but only Football C
may produce a new production model judgment.
