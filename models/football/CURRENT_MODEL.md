# Football v2 — Current Model Authority

## ACTIVE STACK

This file describes only the current production path.

- **Official model:** Football C.
- **Shadow model:** Football C2.
- **Retired models:** C3/C4. Historical records remain immutable; they never participate in new /rank, /xi, /live, accounting or publication.
- **Active source/rank stages:** Football V4 only.
- **Active Airtable model base:** appbzxqXYf0lKfD4P (Football v2 — Active Operations 2026-10-11).
- **User P/L authority:** Actual Bets — Current only.

The active command surface is:

- /sweep -> models/football/stages_v4/SWEEP.md
- /rank -> models/football/stages_v4/RANK.md
- /xi and /xi exception -> models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md
- /live -> the same C/C2 football-assessment path with current live state
- /audit -> models/football/prompts/04_WORK_POST_SLATE_AUDIT.md
- /report -> models/football/prompts/06_NORMAL_CHAT_REPORT.md

Retired V1-V3 source, checkpoint, repaired-handoff, compact-capacity, terminal-rank and ZIP workflows are not production dependencies. They may remain in Git history or explicitly historical documents for audit only.

## Production sequence

SOURCE DATE SURFACES -> V4 GOALS-FIRST INTAKE -> V4_SWEEP_READY -> ORIGINAL-SOURCE REPLAY + FRESH FULL-COHORT STATUS -> C BOARD + C2 BOARD -> ONE AIRTABLE READBACK -> /xi FOOTBALL -> OPTIONAL OBSERVED-QUOTE MODEL EVALUATION OR STRICT EXECUTABLE PRICE DECISION -> ONE DECISION READBACK/PUBLICATION GATE -> LIVE/AUDIT

C and C2 share factual evidence but never model-owned policy fields.

## /sweep — V4 source-backed intake

Authority: models/football/stages_v4/SWEEP.md, source_completeness.py, league_registry.py, goals_first_intake.py, discovery_goal_gate.py and cheap_sweep_filters.py.

The sweep must:

1. acquire the complete provider date/listing surfaces for all ICT and UTC dates touched by the requested window;
2. exhaust pagination and reconcile provider page/block/fixture counts;
3. perform the terminal-sentinel refresh;
4. freeze the full source-visible fixture union before registry/filter logic;
5. apply explicit exclusions and research-priority filters;
6. apply the same source-backed goals-first screen to registered and discovery competitions;
7. place only verified GOAL_PRIORITY fixtures in the rank-eligible queue;
8. retain pending/low-signal/excluded rows in the audit ledger rather than inventing model PASS;
9. emit one native V4_SWEEP_READY receipt and preserve the unchanged source.json.

There is no arbitrary 8/12/15/20-match cap and no lineup/odds-history blocker at intake.

### Standing scope rules

- Noncompetitive friendlies remain excluded.
- **All African domestic football** (men's domestic leagues, women's domestic top flights and domestic cups) is excluded after complete source acquisition with reason USER_AFRICA_DOMESTIC_EXCLUSION. CAF/other continental club competitions and protected official internationals are not excluded solely because an African club/nation participates.
- Israel, Iraq, Wales and Kuwait domestic football remain excluded; Germany 3. Liga remains excluded.
- **UEFA Youth League** is the specifically approved youth exception. It is conditional and requires fixture-specific goal evidence plus current competition-path/format/incentive research. Generic youth competitions are not automatically included.
- Big Five status is not a goal signal. No league is admitted to the shortlist solely by reputation.
- Researched league/team priors in cheap_sweep_filters.py are workload priorities only and cannot override fresh source-backed match evidence.

## /rank — one verified Step-1 chain

Authority: models/football/stages_v4/RANK.md and models/football/stages_v4/stage.py.

Before C/C2 board execution, /rank must:

1. load the frozen V4 receipt and unchanged original source;
2. perform **original-source replay**;
3. refresh kickoff/status for the entire eligible cohort within the V4 freshness bound;
4. remove already-started or source-changed fixtures from prematch ranking with explicit unranked reasons;
5. research the complete eligible cohort in goal-first order;
6. freeze one common factual epoch plus independent C and C2 model-owned fields;
7. execute C official and C2 shadow board engines;
8. persist exact per-match engine JSON and board/lane fields to the active Daily Coverage Ledger;
9. independently refetch once with stage.py verify.

The verified persistence receipt must preserve:

- rank receipt hash;
- source_replayed=true;
- current_fixture_status_checked=true;
- original-source and status-refresh hashes;
- model_evidence_readback_verified=true;
- exact model_evidence_sha256.

That verified Step-1 receipt is the Step-2 provenance authority. Routine /xi does **not** replay the original source/status payloads again.

### Cross-chat handoff

A sweep handoff should keep the matching source and native receipt together. The current replay artifact may include <run>-source.json, <run>-v4_sweep_ready.json and <run>-rank-handoff.json. /rank newest receipt resolves that handoff without asking the user to upload a source already present in repository or workflow provenance.

This transport exists to preserve the original sweep evidence; it is not a second football policy layer.

## C/C2 Step-1 model ownership

Shared evidence includes fixture identity, routes, carrier/chance/failure evidence, H2H materiality, tournament state, current news/XI evidence and other factual observations.

Football C independently owns its completion/continuation/stall/leakage diagnostics, supported line, board state/rank and FOLLOW/RESERVE/STOP lane.

Football C2 independently owns its supported line, route-quality selection state, C2 board state/rank and optional C2-specific opponent-leakage grade + basis. Never infer C2 leakage from C's completion/stall/leakage labels.

### Active O2.25 calibrations

The narrow prospective calibrations remain active:

- C: models/football/procedures/FOOTBALL_C_O225_LEAKAGE_CALIBRATION_20261013.md
- C2 shadow: models/football/challengers/football-c2/FOOTBALL_C2_O225_LEAKAGE_CALIBRATION_20261013.md

They are O2.25-specific counterweights, not general O2.5/O2.75 relaxation and not fourth-goal proof. Historical boards are never rewritten.

## /xi — one football assessment, one quote policy

Authority: models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md, models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md, engine/core.py, engine/adapter.py, and the thin engine/xi_portable.py runner.

Every /xi:

1. assesses Football C and Football C2 independently from current football evidence **without requiring odds**;
2. reports the football result even when a price is unavailable or a price gate fails;
3. if an observed quote already exists, evaluates that quote through the same pure C/C2 quote-policy functions used by strict execution;
4. keeps execution/publication authorization separate.

### Routine vs exception

Routine V4 /xi verifies only the sealed V4 rank receipt + its verified persistence receipt and the exact board row. The queue guard must not re-run Step-1 source replay.

/xi exception may assess an explicitly requested fixture without board authority. It still requires independent C/C2 football evidence. An exception never creates a retroactive prematch decision after kickoff.

## Observed quotes and user screenshots

A user screenshot is exact observed market evidence:

- use the displayed line and odds exactly;
- do not search for replacement bookmaker odds;
- do not change the screenshot timestamp;
- do not ask for a new quote merely because processing took time;
- store ordinary evaluated line/odds fields rather than a screenshot-specific serialized persistence protocol.

adapter.evaluate_observed_quote() is the single non-executable price comparison path. It calls the same pure model policy used by run_decision().

An observed quote may therefore produce model **ACT / WAIT / PASS**, but:

- execution_authorized=false;
- it creates no Website Pick;
- it creates no model exposure;
- it creates no Actual Bet.

A screenshot can never by itself prove that the offer remains executable.

## WAIT policy

There is no wrapper-specific decay-gap rule.

WAIT is produced only by the C/C2 core policy when the model's current research explicitly establishes:

- wait_reachable=true;
- a non-empty reachability basis;
- wait_requires_negative_info=false;
- current football thesis/mechanism remains intact;
- no material veto.

If reachability is not established, the wrapper must not invent WAIT.

The target/minimum price comes from the core model policy:

- target = the applicable protected/model supported burden;
- normal minimum price = 1.65;
- top-ranked FOCUS soft-zone minimum = 1.60 where the core policy permits it.

A WAIT is a **plan**, not exposure. It does not become an assumed bet merely because the target is declared.

Any goal, red card, major injury or other material football change requires a new current football state before acting.

## Strict executable price decision

A currently executable prematch quote may enter the strict run_decision() path only when its execution evidence and required current football/XI/tournament checks are real.

The strict decision reuses exactly the same C/C2 quote policy as observed quote comparison, then applies execution authorization.

After a strict C+C2 pair executes:

1. persist the exact Decision State once;
2. independently refetch once;
3. immediately before publication verify that the quote/fixture/evidence epoch is still valid using step2_publication_guard.py.

The publication guard verifies the existing pair receipt and readback; it does not execute the models a second time and does not run a second session reconciliation layer.

C is the only model that may authorize an official Website Pick. C2 remains shadow-only.

## /live

Started fixtures use the same C/C2 football assessment with the actual current score/minute/events. There is no separate fixture-transition state machine.

After kickoff:

- continue football assessment;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/WAIT/PASS retrospectively;
- an observed live quote may be shown as a current burden comparison, but a separate live execution policy is required before any live bet could be authorized.

## Persistence

Use models/football/airtable/ACTIVE_MODEL_ROUTING.json as the one machine-readable routing authority. The Markdown routing document explains the schema but must not override the JSON mapping.

For new model operations:

- /rank, /xi, /live, /audit, /report, model QA/accounting and website publication use active base appbzxqXYf0lKfD4P;
- old base appWyZJjitSBATXAU is historical read-only;
- C2 cannot create Website Picks;
- exact C/C2 engine results are independently read back;
- one failed optional price check does not convert a successful football assessment into engine failure.

## Accounting and P/L

Do not create synthetic active exposure from classifications or plans.

- WATCH creates no model bet.
- Unresolved WAIT creates no model bet.
- A direct strict BET may create model accounting from its actual observed line/odds.
- A WAIT may enter model accounting only when its reached terms are actually confirmed under the accounting contract.
- C2 accounting remains shadow-only.
- **User profit/loss is calculated only from user-confirmed rows in Actual Bets — Current.** Website Picks, WATCH, WAIT and shadow decisions never become user P/L automatically.

## Deterministic runtime

The active /xi runner is a **thin shared runtime**. It imports the real core.py, adapter.py and decision_pair_cli.py; it does not embed or repin copies of those source files.

No transport bootstrap, source-byte staging helper or runtime-probe ceremony is part of normal /xi execution. If a real deterministic call fails, report the actual failure; do not invent a model output.

## Audit and report

/audit reads frozen prospective evidence/results and actual outcomes without rewriting the past. Experimental probability/shadow tools may be used only as explicit QA/trials and cannot become current C/C2 actions.

/report is read-only. Physical P/L comes from Actual Bets — Current.

## Retired/dormant mechanisms

The following concepts are non-authoritative for current work:

- V1/V2/V3 Step0 portable bundles and ZIP packaging;
- sweep checkpoint/FAST_FINISH/repair mechanics;
- compact capacity/replenishment and old rank-terminal state machines;
- repaired-handoff normalization;
- old rank-persistence reconciler superseded by V4 stage.py verify;
- duplicate V4 /xi source replay validator;
- Step-2 session reconciliation/audit wrappers;
- standalone kickoff-transition router;
- embedded-source XI handoff/repinning;
- synthetic WATCH/WAIT assumed-exposure accounting;
- shadow price/probability experiments as production policy.

Git history remains the audit source for retired implementations. Active launchers and production CI must not depend on them.
