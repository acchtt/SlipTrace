# /block — Primary Football C kickoff-block assessment

Effective 2026-11-04 ICT.

This is the primary production assessment route. Football C certificate,
supported-burden and price-execution rules remain unchanged. Match selection is
now separated from price execution by the deterministic BLOCK_PRIORITY_V1
runtime.

Load:
- `../CURRENT_MODEL.md`
- `COMMAND_ALIASES.md`
- `../procedures/FOOTBALL_ASSESSMENT_DEPTH_AND_BLOCK_COMPARISON.md`
- `../engine/block_runtime.py`
- `02_NORMAL_CHAT_XI_ODDS.md` for runtime/price contracts

## 1. Resolve the complete block before assessing

Resolve all in-scope unstarted fixtures in the requested kickoff block before
judging any candidate. Reuse a current source snapshot when available, but do
not require /rank before assessment.

Do not pre-filter by Current Rank, Slate Rank, FOLLOW capacity, league prestige,
popularity, route count or an existing certificate.

## 2. Equal-depth Football C research

Every new candidate from the 2026-11-05 calibration boundary must reach
`ASSESSMENT_DEPTH_V3`. Historical V1/V2 epochs remain immutable/readable.

V3 retains V2 and additionally freezes structured ignition:

- `activation_quality = LOW | MEDIUM | HIGH`;
- `activation_basis` and at least two activation references;
- `activation_ignition.current_attack_structure`;
- `activation_ignition.early_chance_creation`;
- `activation_ignition.early_concession_opening`;
- `activation_ignition.game_state_force`;
- `activation_ignition.weaker_side_state_change`;
- a substantive ignition basis and at least two ignition references.

A declared HIGH activation requires at least two HIGH ignition signals, including
HIGH early chance creation or HIGH early-concession/opening evidence, with at
least MEDIUM current attack structure. Recent 3+/4+ scorelines or tournament
urgency alone cannot create HIGH activation.

Every fixture with mandatory tournament incentive must also freeze:

- `competition_structure_kind`;
- `competition_structure_basis`;
- `competition_structure_source_tier = OFFICIAL_COMPETITION | PRIMARY_ORGANIZER`;
- `competition_structure_evidence_refs`.

Knockout legs, aggregate state, draw utility and stage must be internally
consistent. Missing official/primary format proof is a research blocker, not a
normal football verdict.

Activation remains selection-only evidence and cannot create a certificate,
supported burden or priced action.

Research incompleteness is not a football PASS.

## 3. Deterministic block comparison

After equal-depth research, compile every candidate through Football C, then run
`engine/block_runtime.py` / `BLOCK_PRIORITY_V1`.

The block selector orders:

1. hard football viability / G3 accessibility;
2. activation;
3. opponent leakage / game opening;
4. continuation;
5. credible G4 / upper tail;
6. endpoint resistance;
7. chance quality;
8. burden completion;
9. frozen goal signal;
10. protected-burden clearability;
11. certificate robustness/depth;
12. G3 mechanism class as a late tiebreaker.

Global /rank and FOLLOW lanes are secondary audit metadata only. They must not
override BLOCK_PRIORITY_V1.

Execute `engine/block_runtime.py` directly when possible. If local execution is
unavailable, write exactly one `football-block-runtime-v1` request to
`engine/block_runtime_requests/<request-id>.json`, wait for the
`Football C deterministic block runtime` workflow, read the persisted
`engine/block_runtime_results/<request-id>.json`, and continue in the same
turn. The request must include an `evidence_epochs` object mapping
every candidate match ID to its frozen ASSESSMENT_DEPTH_V2 evidence epoch. The
result binds each candidate to that epoch and frozen match SHA-256 so a later
/xi can use `authority.mode=BLOCK` without /rank. Do not use conversational judgment as a fallback block order. If both
paths fail, report `BLOCK_RUNTIME_UNAVAILABLE`.

Return the complete block in deterministic block order, not just the top pick.

## 4. Runtime authority

The user's block request authorizes the existing full EXCEPTION research path
candidate-by-candidate. This is not a bypass. Each candidate still needs fresh
source-backed research, H2H/incentive/context checks, certificate funding and
its own evidence epoch.

For new assessment epochs, the exception payload must satisfy
`ASSESSMENT_DEPTH_V2`. Existing frozen V1 epochs remain historical-compatible.

## 5. Odds and actions

The block runtime is **football-only**. It must not consume bookmaker odds or
publish ACT/BOOK/PASS.

No odds are required for block selection. Expose the certified supported burden
and preferred football burden separately from selection order.

If the user supplies a screenshot, use only that exact visible ladder through
the existing deterministic Football C XI runtime. Never search replacement
odds.

No official priced verdict may be published unless all of these exist:

`XI runtime result -> Decision States write -> independent readback -> Step2 publication guard`

Until then, display exactly:

`FOOTBALL ASSESSMENT ONLY — PRICED DECISION NOT PERSISTED`

## 6. Persistence

Persist every assessment independently. Never use a ranked row as a surrogate
for a block assessment that was actually researched independently.

A block-order receipt has no exposure authority. ACT/BOOK/PASS remains a
separate persisted price-execution event.

## 7. Role of /rank

/rank remains a secondary whole-slate comparison, website and audit surface.
Its core ranking key and G3/G4 thresholds are unchanged by this repair.

Use /rank later to measure selection inversion or compare global ordering, but
it cannot decide the primary block order.
