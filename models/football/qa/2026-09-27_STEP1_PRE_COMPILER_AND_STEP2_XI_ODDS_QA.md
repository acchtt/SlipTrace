# Football Model QA — Step 1 PRE Consistency + Step 2 XI/Odds Audit

**Date:** 2026-09-27 ICT  
**User workflow ordinal:** Step 1 = sweep, Step 2 = Work/PRE assessment, Step 3 = XI+odds assessment  
**Repo internal naming:** `01_WORK_DAILY_SWEEP.md` = Work/PRE; `02_NORMAL_CHAT_XI_ODDS.md` = XI+odds.

## A. Step-1 / Work PRE consistency fix — IMPLEMENTED

A compiled operational PRE authority was added:

`models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`

Purpose: preserve the active Football A model while removing ambiguity caused by overlapping historical patches.

The compiled sequence is:

`SCOPE/HANDOFF -> FIXED EVIDENCE PACKET -> HOME ROUTE -> AWAY ROUTE -> SECOND-ROUTE INDEPENDENCE -> PRACTICAL CARRIER -> FAILURE/VETO -> GRADE -> BOARD TIER -> PASS RESCUE -> SUPPORTED BURDEN -> RANK FACTORS -> CROSS-MATCH RANK -> FREEZE`

Key consistency rules now enforced:

- fixed CQ / REP / MECH / CTX evidence channels;
- supporting-only proxies cannot independently create SUPPORTED/PROVEN;
- deterministic PROVEN / SUPPORTED / NOMINAL / FAILED compiler;
- deterministic INDEPENDENT / CONDITIONAL second-route state;
- deterministic VERIFIED / CANDIDATE / UNVERIFIED practical-carrier state;
- HARD VETO separated from SOFT PENALTY;
- SUPPORTED+SUPPORTED = A2 WATCHLIST maximum at Step 1;
- PASS Rescue Screen runs exactly once when required;
- PRE rank follows the active Practical Ceiling hierarchy lexicographically;
- price and confirmed XI cannot enter Step-1 PRE;
- missing evidence stays UNKNOWN / lowers cap / creates UNRESOLVED instead of being filled by intuition;
- full `FOOTBALL_PRE_DECISION_SPEC_V1` trace is persisted into frozen PRE summary/notes.

Step-1 launcher/handoff was also hardened so a stale Sep-20 board or expired override cannot become current authority.

## B. Step-2 / XI+odds (user's third step) QA — FINDINGS ONLY

No behavior changes were applied to Step 2 in this audit.

### CRITICAL 1 — Decay-First vs HMA direct-execution contradiction

Current load order makes:

`MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`

final authority over ordinary above-frozen-burden HMA execution.

It explicitly disables automatic prematch direct exposure above frozen supported burden and says ordinary above-burden cases must WAIT for supported burden.

However `02_NORMAL_CHAT_XI_ODDS.md` still actively contains:

- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`;
- `QUALIFIED — EARLY SAME-LINE PRICE PLAN` above frozen burden;
- live-decay targets at an HMA boundary rather than the frozen supported burden.

This can produce opposite actions from the same XI/market depending on which file dominates.

The later `MODEL_RULES_FOOTBALL_A_CARRIER_MARKET_DECOMPOSITION.md` is a separate explicit exception for cleared ELITE/EXTREME carriers and must not be confused with generic HMA.

### CRITICAL 2 — Betting procedure contradicts itself

`FOOTBALL_BETTING_PROCEDURE.md` Section 10A says:

- HMA may not create above-burden prematch official exposure;
- above burden = live-decay plan to supported burden.

But the later verdict section still says:

- line inside valid HMA band may use early same-line price plan;
- direct supported/HMA execution may be DIRECT;
- live-decay may target supported / valid HMA boundary.

This is an internal same-file contradiction.

### CRITICAL 3 — Decision States Airtable contract is stale model authority

`FOOTBALL_DECISION_STATE_AIRTABLE.md` still declares:

- official model = Football v0.2.54;
- old two-sided-first ranking language;
- old B+ preservation-only hardener semantics;
- old v0.2.54 MCE/live quarantine wording.

But Step 2 explicitly loads this contract while the current model is Football A with later patches.

This can contaminate:
- model-version persistence;
- B+ execution;
- ranking/rerank interpretation;
- live/decay state classification;
- audit labels.

### CRITICAL 4 — Just-started TAKE NOW vs mandatory research/auto-publish race

The post-XI research gate says the fast-path first verdict is provisional and mandatory football research must still occur in the same assessment before ordinary final publication.

But `02_NORMAL_CHAT_XI_ODDS.md` tells the assistant to say:

`TAKE ... NOW`

before that research when known gates appear clear.

The auto-publish rule says an affirmative final exposure should be persisted immediately.

Without an explicit state distinction such as:

`PROVISIONAL FAST VERDICT — NOT YET PUBLISHABLE`

one run may publish before research while another waits for the research gate.

### HIGH 5 — Decay-First authority is not explicitly listed in the XI/odds prompt authority list

The prompt says to load stage-relevant files and gives an explicit "including" list, but the crucial `MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md` is absent from that list.

Because it overrides HMA/live-decay wording, omission materially increases interpretation drift.

### HIGH 6 — B+ protected-line rule conflicts with later carrier-decomposition caution

`MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md` says an exact frozen supported B+ line needs **no additional positive hardener** when XI, alignment, floor and veto gates clear.

The later carrier-decomposition file says ordinary B+ carrier-led direct protected-line exposure "requires stronger carrier failure-resistance."

The latter can be read as reintroducing the positive hardener that the B+ patch deliberately removed.

Required future precedence clarification:

- exact frozen B+ supported burden: B+ Protected-Line core rule controls; carrier decomposition may identify a **negative veto**, but must not invent a new positive hardener;
- +0.25 / above-burden / ELITE-EXTREME current-PRE cases: carrier-specific rules may apply.

### HIGH 7 — Frozen market alignment vs market-calibrated current PRE is not explicitly dual-tracked

Current prompt order:

`... MARKET ALIGNMENT -> CARRIER DECOMPOSITION -> MARKET-CALIBRATED CURRENT PRE ...`

is sensible for avoiding pure market circularity, but once carrier decomposition changes the current actionable burden there is no explicit two-field distinction between:

1. market disagreement vs **frozen PRE**; and
2. execution fit vs **market-calibrated current PRE**.

Without this distinction, one run may re-run alignment against the new burden while another may keep only the frozen comparison.

Recommended future state:
- `FROZEN_PRE_MARKET_ALIGNMENT` remains the anti-circularity diagnostic;
- `CURRENT_PRE_EXECUTION_FIT` separately tests the allowed post-XI carrier burden.

### HIGH 8 — Active HMA file still carries superseded priority-inversion/direct-execution language

The no-cross-match patch removes priority-inversion exposure suppression.
Decay-First removes generic HMA above-burden prematch direct execution.

The HMA file still contains both older ideas.

Load-order precedence technically resolves them, but the stale text is a recurring interpretation hazard.

### MEDIUM 9 — Expired Sep-19/20 temporary execution text remains in the live XI/odds prompt

The prompt conditionally describes a temporary Sep-19/20 relaxation that is now expired.

It is date-qualified, so it is not automatically wrong, but it adds unnecessary decision noise to a production prompt.

### MEDIUM 10 — Step-2 output/persistence schema still treats HMA official states as normal active outputs

The XI/odds prompt still asks to persist/output HMA eligibility, HMA boundaries and `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE` as ordinary states.

Under current Decay-First precedence those are not generic ordinary official paths. They should be audit/monitoring fields except where a later explicit carrier/current-PRE authority genuinely permits the burden.

## C. Recommended Step-2 repair architecture

Do not add another isolated patch.

Create one compiled:

`FOOTBALL_STEP2_EXECUTION_SPEC.md`

with one fixed order:

`FROZEN PRE TRACE -> IDENTITY -> XI -> POST-XI RESEARCH -> MARKET HISTORY -> FINAL FOOTBALL STATE -> FROZEN-PRE MARKET ALIGNMENT -> CARRIER DECOMPOSITION -> CURRENT PRE (IF ELITE/EXTREME) -> EXECUTION BURDEN AUTHORITY -> PRICE FLOOR -> EXPOSURE/PERSISTENCE`

It should explicitly compile:

- Decay-First vs HMA precedence;
- carrier-market exception;
- B+ exact-burden precedence;
- market-alignment dual-state semantics;
- just-started provisional-vs-final verdict semantics;
- one canonical execution-state taxonomy;
- one current Decision States persistence contract;
- transactional Decision State + Website Pick publication.

This should be operational compilation, not a predictive-model change.
