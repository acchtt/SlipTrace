# /xi — Football C assessment

Apply `../procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md`. Use native result
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
analysis.

Optional:

- --screenshot-quote screenshot.json for exact user-supplied observed quote;
- --price-c c_decision.json only when a genuinely executable current prematch
  quote and all strict evidence already exist.

## Routine authority

For every normal /xi, rank authority is the **first mandatory operation**.

### Mandatory rank-discovery preflight

Before choosing `authority.mode`, resolve whether the fixture is already ranked.
This lookup is part of /xi; it is not optional conversational context.

1. Resolve the exact fixture identity / match ID from the user's evidence.
2. Read the active store route in
   `../google_sheets/ACTIVE_STORE_ROUTING.json`, then query the exact fixture in
   **Daily Coverage Ledger**. This ledger lookup is discovery/readback only; it
   does not replace the sealed V4 rank package as execution authority.
3. If the ledger has a current ranked FOCUS row, capture its Run ID, Match ID,
   rank, supported line and rank-integrity hash, then locate the matching
   portable verified rank artifact in the current conversation, Project files,
   or Library. Do not stop at the GitHub checkout: a newest verified rank
   artifact may be persisted outside `main`.
4. Load the exact package and require
   `V4_RANK_PERSISTENCE_VERIFIED` or
   `V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`, the exact FOCUS board row, and the
   matching frozen model-input row.
5. If the active ledger proves the fixture is ranked but the sealed package
   cannot be loaded, return `RANK_RECEIPT_REQUIRED`. **Never convert that
   fixture to EXCEPTION.**
6. `authority.mode = EXCEPTION` is permitted only when the user's command
   explicitly requests `/xi exception`; the runtime authority must carry
   `user_requested_exception = true`. Normal `/xi` must never infer or
   manufacture exception authority.

After that preflight:

1. resolve the newest verified V4 rank package that contains the requested
   fixture;
2. require `V4_RANK_PERSISTENCE_VERIFIED` or
   `V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`;
3. require the exact **FOCUS** board row and matching frozen model input;
4. pass that package through the shared `engine/xi_authority.py` contract;
5. inherit the frozen board state/certificate/evidence before current XI or
   material football updates are applied.

Do not ask the user to resubmit a rank receipt that is already available to the
conversation/runtime. Do not silently build a new Football C assessment when the
rank package cannot be resolved. Fail closed with `RANK_RECEIPT_REQUIRED`.

The direct `xi_portable.py` path and the GitHub backend use the same authority
contract. A free-standing `c_football.json` is not a valid normal /xi input.

Only an explicitly requested `/xi exception` may use
`authority.mode = EXCEPTION` without a ranked FOCUS row. The exception reference
must be non-empty, `user_requested_exception` must be `true`, and the result
remains visibly tagged `EXCEPTION`. A normal /xi ranked-ledger hit can never be
downgraded or rerouted to EXCEPTION because a package lookup was skipped or failed.

Do not replay Step-1 source/status in Step 2.

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
- frozen V4 goal signal;
- whether availability actually attacks an identified scoring route.

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

## Screenshot quote

A user screenshot is `USER_SCREENSHOT_ONLY` observed evidence. Use the exact
screenshot only and persist its normal evaluated line/odds fields when readback
is required.

- no replacement odds search;
- no inferred missing price;
- no re-timing;
- no new screenshot request merely because processing took time.

The runtime calls adapter.evaluate_observed_quote(), the same Football C quote
policy used by strict execution.

If the screenshot burden materially exceeds C's certificate, the runtime
normally hard-gates the observed burden before ACT/BOOK/PASS at that burden.

A bounded **BOOK** is different because it does not accept the observed burden
or upgrade the certificate. The normal 0.50+ material-disagreement football
recheck still runs first. After it completes, a G3-only C-FOCUS row may publish
a lower settlement-aware target under the core extension policy even if G4
remains unfunded/rejected:

- BOOK O2.75 @1.85+ when the base G3 extension clears;
- BOOK O3.00 @1.90+ when the stronger route extension clears;
- BOOK O3.25 @2.00+ only when the strongest G3 extension gate clears;
- never BOOK O3.50 from G3 alone; O3.50 requires funded G4.

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

When the football thesis is intact but the acceptable line/price is not
currently available, C may return **BOOK** with an exact target line and minimum
odds. BOOK means a conditional target order only:

- it creates no exposure until independently confirmed filled;
- it must be reachable pre-goal without requiring negative football news;
- one-step unsupported burden may target the certified burden only across
  **0.25 goals**;
- a gap of **0.50+** cannot manufacture a lower target;
- a FRAGILE internal `C-WATCH`/`REVIEW_ONLY` exception cannot create a BOOK
  target until the current football recheck validates the certificate to at
  least CONDITIONAL.

The normal minimum remains 1.65, with the existing supported-line 1.60 soft
zone only where the deterministic C corroboration allows it. The settlement-
aware G3 extension remains O2.75 @1.85+, O3.00 @1.90+, and O3.25 @2.00+ when
its existing shape requirements clear. O3.50 still requires funded G4.

If the target is not currently met, report `BOOK — PENDING/UNFILLED`, not ACT
and not exposure.
## Strict executable decision

A strict decision requires a current executable prematch quote plus all current
XI/tournament/evidence requirements. It returns one C decision receipt.

Persist once, independently read back once, then run the publication guard.
A screenshot comparison alone never authorizes execution/publication.

## Started fixtures

After kickoff continue Football C assessment with current score/minute/material
events. Never recreate a prematch ACT/BOOK/PASS retrospectively.

## Output

The first line must be the **execution verdict**, never the inherited rank
classification:

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
