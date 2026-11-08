# /xi — Football C assessment

Apply `../procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md` and `../procedures/FOOTBALL_ASSESSMENT_DEPTH_AND_BLOCK_COMPARISON.md`. Use native result
diagnostics and scope labels. A research-required or scope-blocked result cannot
be replaced with a manually narrated ACT/BOOK/PASS. Complete mixed/rejected
G4 findings still receive the material-disagreement recheck; only source-backed
misclassification correction can revise a prior certificate. An out-of-scope
exception is labeled analysis and does not silently become production execution.

> **Normal chat role — XI ONLY.** This conversation is dedicated to
> Football C prematch /xi assessments (including explicit exceptions),
> screenshot-only quote comparisons, required football rechecks, and
> deterministic C verdicts. Load this launcher from current SlipTrace main.
> Do not independently run /sweep, /rank, /live, /audit, or redesign the model
> in this conversation. When an upstream receipt is missing or invalid,
> report the blocker rather than silently recreating it. If the user explicitly
> changes stages, load that stage's canonical launcher. This is the SlipTrace
> production route, not FOM.


Football C is the only active model. C2/C3/C4 are retired and never execute in
new /xi work.

## Runtime authority in normal chat

Normal chat is the evidence/interaction surface, not a second decision engine.
Official C ACT/BOOK/PASS must be produced by the current deterministic
runtime path in `engine/core.py`, `engine/adapter.py` and `engine/xi_portable.py`
when those components are callable. Conversational prose may explain the result
but may not override it.

If the runtime is not directly callable in normal chat, **do not immediately
fall back to ANALYSIS_ONLY**. Use the on-demand deterministic backend:

1. serialize the already-researched `c_football` payload and, when present,
   the exact `USER_SCREENSHOT_ONLY` quote into
   `models/football/engine/xi_runtime_requests/<request-id>.json`;
2. the request must use schema `football-c-xi-runtime-request-v2` and the
   filename stem must equal `request_id`;
3. wait for the `XI Football C deterministic runtime` workflow to persist
   `models/football/engine/xi_runtime_results/<request-id>.json`;
4. read that exact result and use it as the official runtime output for the
   current /xi turn.

The backend executes the same `xi_portable.py -> adapter.py -> core.py` path.
It performs no odds search and cannot replace the user's screenshot quote.

The user must not be asked to type `/resume` merely because local Python is
unavailable. Only when both direct runtime execution and the backend are
genuinely unavailable, or the backend itself returns a concrete runtime/tool
failure, may the response fall back to
`ANALYSIS_ONLY — NO OFFICIAL ENGINE VERDICT`. Surface the exact failure class;
never silently replace a missing runtime result with a free-form official action.


## Authority

Direct runtime when callable:

python models/football/engine/xi_portable.py xi --c c_football.json --authority xi_authority.json

Normal-chat backend when direct execution is unavailable:

`xi_runtime_requests/<request-id>.json`
→ `.github/workflows/xi-portable-artifact-transport.yml`
→ `xi_runtime_backend.py`
→ `xi_runtime_results/<request-id>.json`

A successful backend result is equivalent runtime execution, not conversational
analysis. It is **not yet publishable** as an official ACT/BOOK/PASS until the
runtime's `decision_state_persistence` row has been written to **Decision
States** and independently read back exactly. Runtime execution and publication
authority are separate states.

Optional:

- --screenshot-quote screenshot.json for exact user-supplied observed quote;
- --price-c c_decision.json only when a genuinely executable current prematch
  quote and all strict evidence already exist.

## Routine authority

For normal /xi, resolve authority in this order:

1. **BLOCK** — preferred primary authority after the 2026-11-04 block-first repair;
2. **RANKED** — legacy/secondary authority when no valid current block receipt exists;
3. **DIRECT** — exact user-selected one-off /xi when neither BLOCK nor RANKED exists;
4. **EXCEPTION** — only when the user explicitly requested `/xi exception`.

### BLOCK authority — primary

If the requested fixture was assessed through the current block workflow, do
not require /rank and do not convert it to /xi exception.

Locate the exact persisted pair:

- `models/football/engine/block_runtime_requests/<request-id>.json`;
- `models/football/engine/block_runtime_results/<request-id>.json`.

Build `authority.mode = BLOCK` with:

- the exact match ID;
- `verified_block_package.request` = the persisted block request;
- `verified_block_package.result` = the matching BLOCK_PRIORITY_V1 result;
- `material_evidence_updates` listing only genuinely changed current football
  fields since the frozen block assessment.

The shared authority contract verifies:

- `football-block-runtime-v1` on both sides;
- Football C + `BLOCK_PRIORITY_V1`;
- exact request/result SHA-256 integrity;
- the exact frozen candidate hash;
- its persisted block-priority rank/order;
- its block evidence epoch;
- prospective/outcome-free block execution; and
- current `ASSESSMENT_DEPTH_V2`.

The frozen block-selection fields
`activation_quality / activation_basis / activation_evidence_refs` are
authority-owned and cannot be silently rewritten during /xi. If current
football news materially changes ordinary Football C fields, declare those
fields in `material_evidence_updates`; the current Football C compiler then
reruns the certificate from the inherited block evidence plus those verified
updates.

BLOCK authority does not require a FOCUS row, FOLLOW lane, Slate Rank, Current
Rank or rank policy fingerprint. A candidate's block-priority rank is selection
metadata, not price authority.

### RANKED authority — secondary compatibility path

If no valid current persisted BLOCK_PRIORITY_V1 package exists, the existing
ranked path remains available for historically ranked/current secondary-board
fixtures.

Resolve the newest verified V4 rank package containing the fixture and require:

- `V4_RANK_PERSISTENCE_VERIFIED` or
  `V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`;
- the exact FOCUS board row;
- the matching frozen model-input row; and
- the active rank policy fingerprint/lock.

If the active ledger proves a fixture is ranked but the sealed package cannot
be loaded, return `RANK_RECEIPT_REQUIRED`. Do not convert that ranked fixture
to EXCEPTION.

If the ranked compatibility package is sealed under a different active Football
C policy revision, return `RANK_ENGINE_POLICY_DRIFT`; if it predates the
required slate lock, return `RANK_POLICY_LOCK_REQUIRED`. These are RANKED-mode
compatibility guards only and do not apply to a valid BLOCK authority package.

A ranked legacy `FOCUS_UNFOLLOWED` row remains valid only for an exact direct
user /xi request with `ranked_direct_request=true`, as before.

### DIRECT authority — exact one-off /xi fallback

If the user explicitly requests `/xi` for one exact fixture and neither a valid
BLOCK receipt nor a valid RANKED receipt exists, do not stop with
`XI_AUTHORITY_REQUIRED` and do not require a second command.

Perform a fresh full source-backed Football C assessment for that exact fixture,
including current XI/availability, both scoring routes, carrier/chance creation,
failure mechanisms, completion/continuation/stall, H2H materiality, tournament
format/incentive, match context, G4 research where applicable, and
ASSESSMENT_DEPTH_V2 activation evidence.

Then execute with `authority.mode = DIRECT` carrying
`user_requested_direct_xi = true`, a non-empty `direct_reference`, and the same
full fresh-research manifest used by the strict research validator.

DIRECT changes routing only. It does not weaken certificate, execution-strength,
screenshot-only, market-disagreement, persistence/readback, or publication
gates. It authorizes only the exact user-selected fixture.

### No-authority handling

A free-standing `c_football` payload is never enough for normal /xi.

If neither a valid block receipt nor a valid ranked receipt exists, an explicit
user /xi request must use DIRECT after the fresh full research pass above.
Return `XI_AUTHORITY_REQUIRED` only when there is no valid BLOCK/RANKED receipt
and no explicit exact user /xi request authorizing DIRECT.

The direct `xi_portable.py` path and the GitHub backend use this same
BLOCK/RANKED/DIRECT/EXCEPTION authority contract.

### Explicit exception research contract

An exception has no sealed ranked FOCUS evidence to inherit, so it must perform
a **fresh full Football C research pass before runtime**. Do not synthesize a
thin `c_football` payload from the screenshot, the prior chat conclusion, or a
WATCH/UNVERIFIED screening row.

The exception authority must carry `exception_research` with:

- `fresh_research_completed=true` and `market_independent=true`;
- a new `research_epoch_id` exactly matching `c_football.evidence_epoch_id`;
- `researched_at_utc` exactly matching the assessment epoch;
- the upstream state/reference (FOCUS/WATCH/PASS/UNVERIFIED/NOT_RANKED/OUT_OF_SCOPE);
- at least two football evidence references;
- explicit checked fields covering fixture/status, competition format + incentive,
  rivalry/rest/travel/fatigue context, both scoring routes, carrier/chance creation,
  replacements, failure mechanisms, completion/continuation/stall,
  upper-tail/comparable context, H2H materiality, and G4 research when G3 is funded.

A direct decision-stage exception is forbidden. Exception execution must begin
from the fresh football-assessment stage.

If the user challenges the first exception assessment as incomplete, stale or
half-baked, **invalidate that exception epoch immediately**. The reassessment
must use `revision=REASSESSMENT`, a new exception reference, a new evidence
epoch, the superseded reference/epoch, and a concrete challenge reason. Repeating
the same payload, sources or conclusion without rebuilding the football evidence
is not a reassessment and must fail closed with
`EXCEPTION_RESEARCH_REQUIRED`.

If the upstream state was WATCH/PASS and the fresh exception payload asserts
FOCUS, require an explicit source-backed state-change status, basis and changed
football fields. Exception authority never silently promotes WATCH/PASS to FOCUS.

Do not replay Step-1 source/status in Step 2.

## V3 post-audit evidence gate

For assessment epochs at or after 2026-11-05 08:15 UTC, /xi requires
`ASSESSMENT_DEPTH_V3`.

V3 carries forward the block's structured ignition and competition-structure
proof. If a legacy block receipt lacks those fields, current /xi research may
supply them as explicit material football updates; do not invent or silently
infer them. A HIGH activation label that fails the ignition gate is invalid.

If fresh G4 research finishes as `G4_RESEARCH_COMPLETE_REJECTED` (or legacy
complete-mixed normalized to rejection), the settlement-aware G3 extension is
capped at **O2.75**. O3.00/O3.25 may not be restored by generic NEAR_FUNDED
tail evidence after that explicit fourth-goal rejection. O3.50 still requires
funded G4.

## Football assessment

Freeze the current factual match state once. Start from the matching rank
receipt's frozen C input and source references. Reuse unchanged historical
results, mechanisms and context; research changed XI/availability/incentives,
current status and unresolved facts. Fresh post-XI football research remains
mandatory before final prematch C-BET. Do not repeat the entire rank research
or date-surface acquisition to confirm unchanged facts.

Research:

- routes/carrier/current chance creation;
- failure resistance and named failure mechanism;
- XI/availability where available;
- completion/continuation/stall/opponent leakage;
- upper-tail transferability when G4+ is part of the thesis;
- same-competition / comparable-context direction for that G4+ evidence;
- H2H only if materially transferable;
- tournament incentive where applicable;
- rivalry/derby context;
- rest/congestion and continental/intercontinental travel/recovery;
- verified fatigue evidence and its evidence-backed net effect;
- frozen V4 goal signal;
- whether availability actually attacks an identified scoring route.

For new production rows, checked-neutral context is distinct from not checked.
Do not assume derby = under or congestion = under. At /xi, newly verified
context is certificate-relevant football evidence and must be named in
material-evidence updates when it changes the frozen state.

Odds are not required.

### Credible burden diagnostic

Carry the frozen rank row's `credible_tail_state`,
`credible_tail_target_goal`, `credible_burden_band_low/high`, and
`credible_tail_basis` through /xi. These fields are computed from football
evidence only and are **diagnostic, not execution authority**.

Present the certified burden first. When useful, show the credible band beside
it so an O2.50 certificate with a near-funded fourth-goal tail is not narrated
as equivalent to an O2.50 certificate with a rejected tail. Never convert the
credible band into ACT/BOOK authorization and never upgrade it because the
bookmaker line is higher. ACT/BOOK/PASS remains governed by the certified
G3/G4/G5/G6 burden and existing settlement-aware BOOK policy.

Availability is symmetric: do not suppress the total merely because attacking
players are absent. Check replacements, opponent routes and defensive rotation.

## Execution-strength gate

Rank, FOCUS and FOLLOW are **workload/research priority only**. They never
create execution authority. Every current Football C assessment exposes a
separate `execution_strength` compiled from the funded certificate:

- **FRAGILE** — no upper-tail ACT and no BOOK. It may retain only the
  already-funded **O2.50 G3 floor** when the ordinary G3 completion, endpoint,
  reliability, chance, failure-resistance and protection checks clear. A
  distributed-only mechanism is ranked below stronger mechanisms, but is not
  blanket-vetoed from its funded O2.50 floor merely because its current grades
  are broad MEDIUM.
- **CONDITIONAL** — a funded O2.50 G3 certificate may ACT at O2.50 when the
  current G3 floor clears. The single canonical intermediate-burden profile may
  authorize O2.75 and, for a NEAR_FUNDED fourth-goal shape, O3.00. It cannot
  authorize O3.25.
- **ROBUST** — may ACT at or below the certified burden and uses the same
  canonical intermediate policy. O3.00 may also clear through independent
  transferable fourth-goal evidence. O3.25 is available only through the
  strict ROBUST gate because three goals is a half-loss: independent
  transferable tail plus HIGH continuation/reliability/chance/completion,
  at least MEDIUM failure resistance, and the tighter frozen tail-rate/trap
  controls.

The runtime also exposes `endpoint_control_pressure=NONE|MODERATE|HIGH`.
This is a market-independent control-risk diagnostic between ordinary caution
and the hard `material_suppression` veto. HIGH is now reserved for direct
hard-control evidence: HIGH effective stall, low-draw trap >=0.25, or
verified+corroborated suppressive H2H. Multiple MEDIUM grades or MIXED context
remain MODERATE cautions and do not combine into a synthetic hard veto.

A user-requested `/xi exception` bypasses rank-lane eligibility only. It does
**not** bypass execution strength, endpoint control, certificate funding, or the
ACT/BOOK gates.

For `DISTRIBUTED_G3`, frozen scoreline history is corroboration only. Two
merely USABLE routes with an all-MEDIUM current profile no longer combine into
G3 by themselves. The C certificate requires, among the existing protections,
failure resistance at least MEDIUM, stall no worse than MEDIUM, and either one
STRONG route or HIGH independent-route quality.

## Screenshot quote

A user screenshot is `USER_SCREENSHOT_ONLY` observed evidence. Extract every
line/price pair that is genuinely visible, evaluate that exact ladder, and
persist the selected visible line/odds in the normal evaluated line/odds fields
when readback is required. Choose the highest currently supported/executable
**visible** line for ACT. A rejected higher line cannot erase a lower supported
visible line.

The user's bookmaker also supports custom total lines/target odds. Therefore a
BOOK target may name a line that is **not visible** in the screenshot. That
target is not an observed quote and must never be reported as ACT or exposure
until the user independently selects it and confirms the actual fill.

- no replacement odds search;
- no inferred current price for a non-visible custom line;
- no re-timing;
- no new screenshot request merely because processing took time.

If the screenshot's lowest line is still above Football C's funded protected
G3 floor, the runtime includes `price_check.model.custom_line_review`.
`UNQUOTED_CUSTOM_LINE_REVIEW` is **not** an executable BOOK/ACT or a price;
`candidate_odds=null` and an independent actual quote is mandatory before
entry. `NO_FUNDED_CUSTOM_LINE` cannot be overridden by assuming a custom line.
For started-match exceptions the review is labeled
`STARTED_MATCH_CUSTOM_LINE_NOT_PREMATCH_EXECUTABLE`, never a late synthetic
prematch offer. Keep all visible quarter-lines separate: O2.75 at three total
goals half-wins, whereas O3.0 pushes. User screenshot evidence remains the sole
odds source.

The runtime calls `adapter.evaluate_visible_quote_ladder()`, which delegates
each exact quote to the same Football C policy used by strict execution.

If the screenshot burden materially exceeds C's certificate, the runtime
normally hard-gates the observed burden before ACT/BOOK/PASS at that burden.

A bounded **BOOK** is different because it does not accept the observed burden
or upgrade the certificate. The normal 0.50+ material-disagreement football
recheck still runs first. After it completes, a G3-only C-FOCUS row may publish a lower
settlement-aware target only when the football thesis itself clears the strict
BOOK-strength gate. Market disagreement never creates that eligibility:

- FRAGILE G3: no intermediate extension and no BOOK path;
- CONDITIONAL/ROBUST G3 may ACT O2.75 @1.85+ only through the deterministic
  intermediate-burden profile;
- O3.00 @1.90+ additionally requires a NEAR_FUNDED fourth-goal profile plus
  stronger carrier/independent structure;
- O3.25 is not generic G3 authority; it is available only through the strict
  ROBUST near-G4 intermediate gate at 2.00+;
- generic G3 BOOK may target only O2.75/O3.00 when its football-strength gate
  clears; the target does not need to appear in the visible ladder;
- O3.50 still requires funded G4.

The credible-burden diagnostic remains non-authoritative and cannot by itself
create an O3.00 target.

BOOK is a conditional target order and creates no model exposure until a fill is
independently confirmed.

Current material-disagreement threshold for accepting/upgrading the observed
burden remains: observed screenshot line >= compiled Football C burden + 0.50
goals.

The first runtime pass returns
`MARKET_DISAGREEMENT_RECHECK_REQUIRED` unless the current football payload
already contains a completed disagreement recheck.

When that state is returned, do not stop and do not issue a verdict. In the same
normal-chat /xi turn:

1. investigate the football reason for the disagreement using current factual
   evidence only;
2. carry the frozen board's `g4_research_status`;
3. for G4+ disagreement, explicitly verify carrier/distributed/reply completion,
   continuation after goal three, upper-tail transferability and comparable
   context;
4. record the researched certificate-relevant fields and source/evidence refs;
5. rerun the deterministic C football certificate;
6. invoke `xi_portable.py` again with the same user screenshot;
7. only the second, cleared runtime result may produce ACT/BOOK/PASS.
   A bounded G3 BOOK target does not require the recheck to fund G4 because it
   remains below O3.50 and preserves the O2.50 certificate.

When the frozen board says `G4_RESEARCH_INCOMPLETE`, the runtime marks the
material disagreement as a **certificate-completeness recheck**. The market is
still only the trigger. The recheck may incorporate football evidence that
already existed before rank when that evidence was never incorporated into a
completed frozen G4 investigation. Do not call that evidence "new"; record the
repair as `VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH`.

A suppressive same-competition/continental sample takes precedence over generic
domestic scoring. The market never manufactures a certificate.

### Frozen-certificate upgrade guard

For every ranked fixture, `/xi` must carry both the frozen certified burden and
`frozen_board_g4_research_status`.

If the frozen status is `G4_RESEARCH_COMPLETE_REJECTED`, a material market
disagreement still forces one independent **football reclassification recheck**.
The market is only the trigger. It does not overturn the frozen rejection.

After that source-backed recheck, a higher current C certificate is allowed by
either:

- `VERIFIED_NEW_FOOTBALL_EVIDENCE` when genuinely changed XI/incentive/
  mechanism evidence changes certificate-relevant fields; or
- `VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION` when the same prospective
  football evidence available at rank was misclassified or underweighted.

The misclassification route requires a completed disagreement recheck,
non-empty source/evidence references, explicit verification of
`upper_tail_transferability` and
`upper_tail_comparable_context_signal`, and named G4 certificate fields whose
classification changed. The legacy contract field
`certificate_upgrade_new_evidence_fields` carries those named fields even when
the status says they are reclassified rather than genuinely new.

If the frozen status is `G4_RESEARCH_INCOMPLETE`, a higher current C
certificate may use
`VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH`, but only after the previously
unassessed G4 fields are actually researched and named.

A higher market total alone, merely confirming the same XI, or repeating the
old rank conclusion is never enough. The independent football recheck must
either confirm the rejection or produce a deterministic C certificate repair.

## Conditional BOOK targets

Active Football C no longer exposes WAIT as a normal user-facing price action.

When the football thesis is intact but the acceptable visible line/price is
not available, C may return **BOOK** with an exact custom target line and minimum
odds. BOOK means a zero-exposure target instruction only:

- it creates no exposure until independently confirmed filled;
- the target line does not need to appear in the screenshot;
- no unseen current target price may be inferred;
- a **0.50+** market/certificate disagreement still requires the football
  recheck before publishing the lower target;
- FRAGILE certificates cannot create BOOK targets;
- CONDITIONAL or ROBUST football may create a custom BOOK at its deterministic
  direct ACT ceiling; above-certificate G3 extensions still require their
  separate football-strength gate.

The normal minimum remains 1.65, with the existing supported-line 1.60 soft
zone only where deterministic C corroboration allows it. There is **one**
above-certificate G3 extension policy for both visible ACT and custom BOOK:
O2.75 requires non-fragile current football; O3.00 requires either a
CONDITIONAL NEAR_FUNDED tail or the ROBUST independent-tail path; O3.25 requires
the strict ROBUST gate and 2.00+; O3.50 still requires funded G4. No second
BOOK-only robustness policy exists.

If the target is not currently met, report `BOOK — PENDING/UNFILLED`, not ACT
and not exposure.
## Strict executable decision

A strict decision requires a current executable prematch quote plus all current
XI/tournament/evidence requirements. It returns one C decision receipt.

The on-demand GitHub backend additionally emits `xi_assessment_index` with
`request_id`, Match ID, evidence epoch, screenshot reference/time, the entire
visible ladder, selected line/odds, action and custom-line review. The stored
`xi_runtime_results/<request-id>.json` provides an append-only **audit
fallback** for normal-chat and explicit exceptions; it is **not proof** of
Google Sheets persistence or bet execution. A future audit must reconcile
the assessment index against Decision States by Assessment ID, report missing
rows separately, and include all /xi calls rather than using ranked rows as
surrogates. Do not publish an official verdict on the strength of GitHub
storage alone.

Every football-only, screenshot-priced, or strict-decision runtime result emits
`decision_state_persistence` and the backend mirrors it as
`sheets_handoff = XI_SHEETS_HANDOFF_V1`. Treat this as a mandatory **same-turn
orchestration contract**, not an audit suggestion.

Normal chat must use the connected Google Drive/Sheets capability in the same
/xi turn. GitHub runtime-result persistence is never a substitute for the
Google Sheets write/readback.

Treat that object as a mandatory write contract:

1. upsert its exact `row` to the active Google Sheet **Decision States** using
   **Assessment ID** as the immutable key;
2. set `Persisted At UTC` at write time;
3. independently refetch the same Assessment ID;
4. verify the fields named by `readback_assertions`, including the exact
   `Engine C Result`, action, supported/evaluated line, odds and engine source
   revision;
5. only after exact readback may the publication guard create an official
   user-facing ACT/BOOK/PASS or Website Pick.

Before readback, `publication_authorized=false` and
`publication_blocker=DECISION_STATE_PERSISTENCE_READBACK_REQUIRED` are
binding. The user-facing /xi turn is incomplete until the Sheets upsert and
independent refetch finish. If the Google Sheets connector is unavailable, the
write fails, or the readback differs, return `XI_PERSISTENCE_UNAVAILABLE` /
`ENGINE_EVALUATED — NOT PUBLISHED`; do **not** narrate the runtime's candidate
ACT/BOOK/PASS as an official verdict and do not ask the user to run another
command just to persist it.

A screenshot comparison is the user's sole odds authority, but it is still not
a physical bet or persistence receipt. Actual user exposure remains separate
and requires the existing verified-slip accounting path.

## Started fixtures

After kickoff continue Football C assessment with current score/minute/material
events. Never recreate a prematch ACT/BOOK/PASS retrospectively.

## Output

After verified Decision States readback, the first line must be the **execution
verdict**, never the inherited rank classification. Before that readback, the
first line must be `ENGINE_EVALUATED — NOT PUBLISHED`, followed by the
candidate action only as non-official diagnostic output.

After readback:

- `ACT — <line> @ <odds>` when the current quote is accepted;
- `BOOK — <target line> @ <minimum odds>+ — PENDING/UNFILLED` for a conditional
  target;
- `PASS — <reason>` when there is no acceptable current or conditional entry.

Rank classification is metadata underneath the action. Display internal
`C-WATCH` as **REVIEW_ONLY**. Never use WATCH/REVIEW_ONLY as the final /xi
verdict and never confuse it with a price instruction.

Also show a compact authority line for routine ranked fixtures:

`RANK: #<n> FOCUS · cert O<line> · <rank run id>`

For BOOK always print the protected certificate, target line, minimum odds, and
that the order is **not exposure until independently confirmed filled**.

Do not mention retired models unless the user asks for historical audit.


## XI execution repair V1 — 2026-11-08

Separate **line decay** from an **immediately selectable custom total**.

- A WAIT/decay path remains limited to one 0.25-goal step. Never tell the user
  to wait for a distant main total to collapse before the first goal.
- A custom line available from the user's bookmaker is different: the runtime
  may publish `BOOK NOW O<target> @ <minimum>+` without reusing the screenshot
  odds. This means **select/check that custom line immediately**, not wait.
- The immediate custom path is intentionally narrow. ROBUST G4/G5/G6 football
  may use the exact protected certificate line. G3-only football may use a
  distant O2.75 custom target only through the strict carrier rescue: STRONG
  self-funded carrier, STRONG primary route, HIGH burden completion, frozen
  3+ >=75%, trap <=10%, and the canonical O2.75 intermediate profile already
  authorized. It never manufactures G4.
- CONDITIONAL G4+ does not receive a generic lower custom-line rescue. This
  prevents the old Bayern-style O3.25 target from returning merely because a
  custom selector exists.
- Every custom BOOK remains **PENDING/UNFILLED, zero exposure** until the user
  independently confirms the actual custom quote/fill.

### Single-elimination G3 ACT throttle

For regulation totals in `SINGLE_ELIMINATION` or `FINAL`, a two-sided/mixed
G3 may not ACT O2.50 when continuation and failure resistance are only MEDIUM,
unless at least one of these counterweights exists: a self-funded carrier, HIGH
continuation, HIGH failure resistance, or frozen 3+ >=70%. This prevents a
Kansas-style level-tolerant knockout profile from receiving the easiest ACT
merely because the bookmaker line is low.

### Strong-block / G4-rejection conflict gate

When frozen block evidence has **4+ >=55%, trap <=10%, and a STRONG route/carrier**
but deep /xi returns `G4_RESEARCH_COMPLETE_REJECTED` or
`G4_RESEARCH_COMPLETE_MIXED`, do not seal ACT/BOOK/PASS immediately. Complete
one bounded market-independent recheck and freeze:

- `g4_carrier_path`;
- `g4_distributed_path`;
- `g4_reply_path`;
- `g4_continuation_after_g3`;
- `upper_tail_transferability`;
- `upper_tail_comparable_context_signal`;
- `failure_resistance`;
- `continuation_quality`.

Set `block_g4_conflict_recheck_status=COMPLETED` with a substantive basis and
source refs, then rerun the deterministic runtime. The recheck is not an
automatic G4 upgrade; it only prevents generic control/absence caution from
silently erasing a strong frozen upper-tail signal. Until completed, runtime
returns `BLOCK_G4_CONFLICT_RECHECK_REQUIRED`.
