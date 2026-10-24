# Football v2 — Current Model Authority

## ACTIVE STACK

This file describes only the current production path.

### Authority hierarchy

When two repository texts appear to disagree, use this order:

1. executable contracts in `engine/core.py`, `engine/adapter.py` and V4
   `stage.py`;
2. this file for active model/routing/data boundaries;
3. `production/FOOTBALL_C.md` for Football C semantic rules;
4. the canonical stage launcher for the command being executed;
5. procedure documents only when an authority above explicitly imports them.

Historical/retired documents never override an active layer. Do not merge two
conflicting rules by applying both.


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
For `/xi`, normal chat gathers evidence but official ACT/BOOK/PASS is owned by
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
unresolved queue after a real interruption. An upstream PARTIAL sweep is not
rankable: `/rank` must fail closed and return the exact pending identities to
the same sweep checkpoint.


The sweep must acquire complete provider date surfaces before filtering, apply
the standing league/user exclusions, and use source-backed goal evidence to
admit GOAL_PRIORITY fixtures. **Latvian domestic leagues are excluded from
production intake from 2026-10-20 onward** because of user-declared
inconsistency; preserve them in the source ledger as
`USER_LATVIA_LEAGUE_EXCLUSION` and do not research/rank them. Latvian clubs in
continental competitions remain eligible through the normal tournament path.
Intake never requires odds or lineups.

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

Research completion and persistence verification are separate. Only after the
upstream sweep is COMPLETE may rank checkpoint its own C/G4 research. New rank
receipts freeze all eligible dispositions and reusable factual C input.
Unfinished rank research stays in an ordered resume queue; bare
evidence-missing labels cannot establish completed research.
`V4_RANK_PARTIAL_PERSISTENCE_VERIFIED` refers only to that downstream rank
research state and never authorizes a PARTIAL upstream sweep. Repeated `/rank`
on the same complete source epoch resumes its native checkpoint and reuses
completed facts.

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

The active champion C ranking key is now execution-structure first:

1. current G3 execution-floor authorization;
2. funded G3 mechanism strength (self-funded carrier > two-route > leakage >
   distributed-only);
3. burden-normalized clearability;
4. certificate robustness;
5. highest funded certificate G6 > G5 > G4 > G3 > none;
6. endpoint/control risk;
7. frozen V4 quantitative goal signal;
8. remaining C football-mechanism quality.

This prevents a broadly-MEDIUM distributed G3 from outranking a stronger
self-funded carrier merely because evidence documentation is HIGH or recent
score rates are stronger. Evidence confidence is a sourcing-quality field and
does not count as the genuinely HIGH predictive dimension required to promote
active C execution robustness.

Compiled burden magnitude itself is not a ranking bonus. Deeper certificates
remain important, but certificate depth no longer wins before current mechanism
strength and clearability.

## Football C supported-burden compiler

Production supported burden is compiled from explicit goal certificates:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50
- no G3 -> no certified burden

Asian .75 lines require the next certificate for a full-win **certificate**.

The protected certificate is not the same thing as the maximum bookable Asian
line. Active C has a separate settlement-aware G3 execution extension for
C-FOCUS only:

- O2.75 BOOK floor 1.85;
- O3.00 BOOK floor 1.90;
- no G3-only O3.25 BOOK;
- O3.50 still requires funded G4.

BOOK does not upgrade the certificate and creates no model exposure until fill
confirmation.

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

**Presentation rule:** internal C-WATCH is displayed as REVIEW_ONLY metadata.
The final /xi headline is always ACT, BOOK or PASS (or an explicit blocker such
as RANK_RECEIPT_REQUIRED / MARKET_DISAGREEMENT_RECHECK_REQUIRED), never WATCH.


**Conversation surface: NORMAL CHAT; deterministic runtime remains decision authority.**

Authority: prompts/02_NORMAL_CHAT_XI_ODDS.md,
procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md, engine/core.py,
engine/adapter.py and engine/xi_portable.py.

Every /xi:

1. resolves shared authority first: normal fixtures require the newest verified
   rank package and exact FOCUS row; only explicit `/xi exception` may use
   EXCEPTION authority;
2. completes Football C assessment without requiring odds;
3. executes the deterministic runtime directly when callable, otherwise through
   `xi_runtime_backend.py` via the request/result GitHub bridge;
4. if the user supplied an observed screenshot, evaluates exactly that quote
   through adapter.evaluate_observed_quote();
5. if a genuinely executable current prematch quote exists, uses
   adapter.run_decision();
6. persists/readbacks once when persistence is required.

Both direct `xi_portable.py` and the GitHub backend call
`engine/xi_authority.py`. A free-standing routine Football C payload is
invalid and fails closed with `RANK_RECEIPT_REQUIRED`.

The backend bridge is transport only. It does not create a second policy, fetch
replacement odds, or loosen Football C.

There is no second screenshot-specific ACT/BOOK/PASS policy and no second model
whose result can override or dilute C.

### Screenshot/market disagreement

Use only the user-supplied quote when that is the declared evidence source.

A ranked fixture also carries its frozen board certificate into `/xi`. A
higher screenshot burden can never authorize an upgrade by itself.

If the observed market burden materially exceeds C's certified burden, the
disagreement triggers one independent football-evidence recheck before a final
priced verdict. A bounded settlement-aware G3 BOOK target is not an
observed-burden ACT and does not require that recheck to fund G4 merely because
the current market is higher. After the recheck, C may BOOK within its bounded
G3 extension or PASS; ACT at the observed burden still requires funding. A
higher current certificate may arise only through one of three explicit paths:

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

### REVIEW_ONLY and conditional BOOK

`C-WATCH` remains an internal frozen research classification for audit
compatibility. User-facing surfaces render it as **REVIEW_ONLY**. It is not a
post-/xi verdict and does not authorize routine Step 2.

Active Football C has three user-facing prematch price actions:

- **ACT** — accept the current quote;
- **BOOK** — place/record an exact conditional target; zero exposure until an
  independently confirmed fill;
- **PASS** — no acceptable current or conditional entry.

Legacy WAIT fields remain only as internal reachability evidence and historical
compatibility. When the old price-only WAIT conditions are valid, active C emits
BOOK instead. BOOK remains ROBUST-only. A FRAGILE REVIEW_ONLY exception may
retain a direct O2.50 ACT only when G3 itself is already funded, the current
G3 execution-floor checks clear, and endpoint-control pressure is not HIGH;
FRAGILE never receives upper-tail or BOOK authority.

For an unsupported higher observed burden, a conditional target may move down to
the certified burden only across one **0.25-goal** Asian-total step. A gap of
**0.50+** cannot manufacture a far-lower target. The normal minimum remains
1.65, with the existing supported-line 1.60 soft zone where deterministic C
corroboration permits it.

## /live

**Conversation surface: NORMAL CHAT; deterministic Football C assessment remains authority.**

Started fixtures use the same Football C football assessment with current
score/minute/material events.

After kickoff:

- continue football assessment;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/BOOK/PASS retrospectively;
- a live quote is comparison evidence only unless a separate live execution
  policy explicitly authorizes it.

## Persistence and accounting

`models/football/google_sheets/ACTIVE_STORE_ROUTING.json` is the machine-readable routing authority.

For new operations:

- persist only active Football C model outputs;
- retired C2/C3/C4 fields may remain in historical Airtable rows for immutable audit only; all new C persistence uses Google Sheets;
- internal WATCH/REVIEW_ONLY creates no model bet;
- active C does not issue a user-facing WAIT; historical WAIT records remain
  immutable audit/accounting history;
- a BOOK order creates no exposure when issued; any later fill must be
  independently confirmed before reconciliation;
- only a strict direct C BET/ACT or a confirmed booked-order fill may enter new
  model accounting;
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
