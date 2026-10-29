# Football C — Full sweep/rank pipeline regression audit

**Date:** 2026-10-29 ICT  
**Repository:** acchtt/SlipTrace  
**Audited HEAD before this report:** `a4790c69e1947329c3da75bd22b352e8deb64466`  
**Authority:** Football C only  
**Scope:** `/sweep -> sweep handoff -> /rank -> FOLLOW allocation -> Google Sheets persistence`  
**Predictive production changes in this audit:** **NONE**

## Executive decision

**CURRENT SWEEP/RANK SELECTION PIPELINE FAILS AUDIT.**

The present failure is not a CI or syntax failure. Current deterministic workflows pass. The failure is a selection-universe and priority-semantics regression created by several coordinated repairs that became production behavior at the same time.

Two defects are critical and directly explain the user's recent observations:

1. **Sweep still treats a fully quantified negative goal screen as a terminal production exclusion, while only four negative-screen controls per sweep receive zero-authority review.** At the same time a large source-visible discovery backlog can remain deferred while the handoff reports the requested surface complete.
2. **FOLLOW allocation intentionally consumes capacity by chronological kickoff blocks before global merit.** A regression test explicitly locks the behavior where seven earlier weak candidates receive FOLLOW while a later stronger candidate is RESERVE.

The latest persisted 28-Oct -> 29-Oct board demonstrates the second defect in production: global ranks 11 and 12 are FOLLOW while global rank 4 is RESERVE.

This is a pipeline-selection inversion. It is upstream of `/xi`.

## 1. Audit boundary and change volume

The 24-Oct whole-model audit at `cbbe24908bbcb1950017f9ebdbf6893ddb4d9bd0` correctly diagnosed several architecture risks and explicitly made no predictive production changes.

The following repair window then accumulated a large number of simultaneous changes. From the pre-audit parent `f7b4dc6bdc45c55171374c80b61b74a179d515c4` to the audited HEAD, GitHub reports 437 commits. Among the production files:

- `models/football/engine/core.py`: about 840 changed lines;
- `models/football/engine/adapter.py`: about 586 changed lines;
- `models/football/CURRENT_MODEL.md`: about 170 changed lines;
- `models/football/engine/schema.json`: about 117 changed lines;
- V4 sweep intake, discovery, rank-session and registry logic also changed repeatedly.

Not every commit is predictive; many are runtime persistence or QA. The governance problem is that multiple material selection behaviors changed in the same repair period, so outcome attribution is no longer clean.

The football-model QA contract requires one material challenger change at a time. This window does not provide that isolation.

## 2. CRITICAL — sweep completion semantics hide a truncated research universe

### Current code

`goals_first_intake.py` still states and implements:

> a fully quantified negative goal screen is terminal WATCH, not incomplete research.

Only `DISCOVERY_GOAL_QUALIFIED` and `DISCOVERY_GOAL_REVIEW` rows are appended to the production `eligible_queue`.

A negative `WATCH_GOAL_SIGNAL` can enter `CONTROL_REVIEW`, but:

- `CONTROL_REVIEW_MAX_PER_SWEEP = 4`;
- it remains in the research backlog;
- it is explicitly never appended to the production eligible queue;
- it has zero production rank authority.

Therefore the critical architecture issue identified on 24 Oct was not actually removed. The negative screen is still a hard production gate. The repair added a calibration/control lane, not a non-terminal route into full Football C selection.

### Latest 28-Oct source/handoff evidence

For `V4-20261028-1610-20261029-0300-LEAGUEPROOF`:

- source fixtures: **553**;
- active research targets: **92**;
- sweep eligible targets: **34**;
- WATCH targets: **34**;
- evidence-limited targets: **24**;
- deferred source backlog: **131**;
- deferred discovery backlog: **131**;
- `research_exhaustive = false`;
- `unresolved_or_deferred_candidates_remain = true`;
- yet `whole_requested_surface_complete = true`.

This is a semantic contradiction for an operator reading “complete” as “the requested match universe was fully considered for selection.”

Source acquisition may be complete, but **selection research is not exhaustive**. These must be separate statuses.

### Impact

This explains why many plausible fixtures visible in the source surface never reach ranking. They are not losing inside Football C. They are losing before Football C receives them.

### Required repair

Split completion into at least:

- `source_surface_complete`;
- `selection_research_complete`;
- `deferred_candidate_count`;
- `rank_universe_complete`.

A handoff may only call the rank universe complete when every in-scope source-visible prematch fixture has one of:

1. completed Football C research;
2. an explicit deterministic exclusion that is itself part of the audited selection policy;
3. an explicit `DEFERRED_NOT_RANKED` state that prevents the board from being presented as exhaustive.

The goal-history screen should order research, not silently stand in for Football C. Negative-screen rows can be deprioritized, but the current fixed four-row zero-authority control is insufficient as the only recovery path.

## 3. CRITICAL — FOLLOW allocation is chronological, not global selection

### Current code

`_allocate_c_follow_lanes()` creates one primary CLEARABILITY nominee per exact kickoff block.

The current champion then sorts those primary nominations by:

1. kickoff time;
2. clearability within that kickoff;
3. rank;
4. match id.

It fills `MAX_FOLLOW = 7` from that chronological list before considering secondary nominations.

This means a weak candidate at an early kickoff can consume a scarce FOLLOW slot before a materially stronger candidate at a later kickoff is considered.

### This behavior was intentionally reintroduced

On 26 Oct, commit `708165ce8564c5806d3ac016b007deaae8f04762` changed the allocator to compare primary nominations globally by quality and use kickoff only as a tie-breaker.

Later the same day, commit `c3b68608b7afb12168114ff31b2ea75b55043f02` rolled that back after a frozen replay found the then-global clearability scheme could promote over-certified O4.5 rows.

The rollback conflated two independent issues:

- **global vs chronological allocation**, and
- **bad scoring of over-certified high burdens**.

The correct response to the O4.5 problem was to repair the global merit score / burden normalization. Restoring chronological capacity consumption introduced a different deterministic selection inversion.

Commit `ff05f443ae6bcdc2a6fc20c394729bf27e1d4d42` then locked this behavior in a regression test. The test explicitly expects:

- seven `early-weak` rows to be FOLLOW;
- a `later-strong` row to be RESERVE.

That test proves the present behavior is intentional, not incidental.

### Production proof on the latest persisted board

For `V4-20261028-1610-20261029-0300-LEAGUEPROOF`, the Google Sheets Daily Coverage Ledger contains 16 C-assessed rows, all persisted as C-FOCUS.

FOLLOW rows include:

- rank 5 — ND Beltinci vs NK Triglav, 20:00 ICT;
- rank 12 — Nasaf Qarshi vs Kuwait SC, 20:45 ICT;
- rank 11 — FC Goa vs Hyderabad FC, 21:00 ICT;
- rank 2 — FC Kosice vs DAC, 00:00 ICT;
- rank 1 — Venezia vs Inter, 00:30 ICT;
- rank 3 — Chelsea W vs Roma W, 00:45 ICT;
- rank 6 — Brommapojkarna vs Haecken, 01:00 ICT.

After those seven chronological primary slots are consumed:

- **rank 4** Spelle-Venhaus vs TuS Bersenbrueck at 01:30 is RESERVE;
- rank 7 Celtic vs Dundee United is RESERVE;
- ranks 8, 9, 14, 15 and 16 are FOCUS_UNFOLLOWED.

So the production board itself exhibits the inversion: **rank 11 and rank 12 are FOLLOW while rank 4 is not.**

### Required repair

FOLLOW must again be a **global merit allocation**.

Do not restore the old over-certified O4.5 scoring. Build a safe global selector whose first comparison is lower-burden/G3 clearability and execution-floor quality, with G4+ depth only as later evidence.

Kickoff may be:

- a tie-breaker;
- a display sort;
- or a small explicit coverage constraint.

It must not be allowed to consume all scarce FOLLOW capacity before later candidates enter the comparison.

## 4. HIGH — every funded G3 is compiled as FOCUS, causing board inflation

`compile_c_board_state()` currently returns FOCUS for every funded G3 unless the row has a direct route-destroying suppression state.

That makes FOCUS primarily a qualification label, not a priority label.

The latest persisted board has **16 C-assessed rows and all 16 are C-FOCUS**. FOLLOW then attempts to express actual priority inside an already inflated FOCUS set.

This is the source of the “massive focus board” behavior.

The engine already has newer semantic axes such as qualification and priority, but the persisted/public legacy `board_state` still carries FOCUS and therefore continues to communicate the wrong meaning.

### Required repair

Separate the concepts:

- **QUALIFIED**: funded G3 / eligible football structure;
- **FOCUS**: top globally selected priority set;
- **RESERVE / REVIEW_ONLY**: qualified but not currently selected;
- **STOP/PASS**: actual football rejection or operational exclusion.

A funded G3 should not automatically become public FOCUS.

The final admitted board must use the configured board cap rather than exposing an unbounded number of FOCUS rows and then hiding priority in FOLLOW metadata.

## 5. HIGH — ranking and allocation are two competing orderings

The current official rank key is global and execution-structure first:

1. G3 execution-floor authorization;
2. G3 mechanism strength;
3. burden-normalized clearability;
4. certificate robustness;
5. certificate depth;
6. endpoint/control risk;
7. goal-signal evidence;
8. remaining mechanism quality.

But the FOLLOW allocator then applies a separate chronological portfolio selection.

As a result, the row called “rank 4” is not necessarily the fourth operational priority, and a row called “rank 12” can be in the primary FOLLOW lane.

That makes `rank`, `FOCUS` and `FOLLOW` disagree about what “best” means.

### Required repair

One ordering must own selection.

Recommended contract:

- global rank = merit order;
- admitted top-N = selection;
- FOLLOW = operational follow state for those admitted rows, not a second predictive selector;
- kickoff sorting happens only in the presentation layer.

If a portfolio-diversity constraint is desired, apply it explicitly after a global merit shortlist and report every displacement.

## 6. HIGH — audit repairs became a moving champion instead of isolated challengers

The 24-Oct audit explicitly called for a clearability **challenger** and stated that architecture should be repaired before result-driven threshold changes.

The following days introduced or changed:

- compiled board state;
- G3 execution-floor behavior;
- endpoint split;
- ranking-key ordering;
- G4/G5 proof requirements;
- FOLLOW allocation;
- discovery/review routes;
- recent-four research review;
- cup research identities;
- rank/deadline diagnostics;
- multiple replay-based rollbacks.

Several of these are good individual ideas. The problem is simultaneous production movement.

This makes “did the audit help?” impossible to answer cleanly because the champion was not held stable long enough for prospective separation.

### Required repair

Freeze the current champion while repairs are built as isolated challengers.

No more outcome-triggered production edits until the pipeline regression challenger is replayed on frozen same-information slates and then tested prospectively.

## 7. MEDIUM-HIGH — active Google Sheets persistence has referential inconsistency

The active Google spreadsheet is still receiving current Daily Coverage rows.

However, a live audit of the `Sweep Runs` tab found no V4 run IDs for 26, 27, 28 or 29 Oct, while `Daily Coverage Ledger` contains the current 28-Oct `LEAGUEPROOF` rank rows.

Therefore the child coverage rows exist without the expected current parent run entries in `Sweep Runs`.

This does not create the selection inversion by itself, but it harms:

- `newest receipt` discovery;
- operational auditability;
- run/row referential integrity;
- deterministic resume logic;
- comparison of eligible count vs ranked count.

### Required repair

Every persisted Daily Coverage run must have a matching verified `Sweep Runs` parent row, written/read back atomically with run ID, window, eligible count, ranked count and receipt integrity hash.

Publication should fail closed if the parent run record is absent.

## 8. What is NOT the root cause

### Current HEAD CI

At audited HEAD `a4790c69...`, the following workflows passed:

- Football V4 sweep rank stages;
- XI Football C deterministic runtime;
- Football C production invariants;
- Football V4 normal-chat sweep backend;
- Football V4 original-source replay attestation.

Therefore this is not a failing-test or broken-runtime incident.

The tests validate current contracts, including the bad kickoff-protected behavior.

### Latest official-cup alias repair

The latest cup repair is prospective, fixture-bound, requires format/incentive proof, and its G3/FOLLOW probes are shadow-only. It should not be wholesale-reverted.

The regression predates that patch.

### /xi

The present audit does not assign the main failure to `/xi`. The most damaging errors occur before execution:

- candidate never reaches rank;
- too many rows become FOCUS;
- FOLLOW capacity is allocated chronologically rather than by global merit.

## 9. Repair program

### P0 — freeze

Freeze predictive production logic at the audited HEAD until the following challengers are evaluated. Do not add another result-driven threshold patch.

### Challenger A — global safe FOLLOW selection

Change only FOLLOW allocation:

- remove chronological primary consumption;
- compare all eligible FOCUS/QUALIFIED candidates globally;
- prioritize G3 execution floor + burden-normalized clearability;
- do not reward unsupported G4/G5 burden;
- kickoff only tie-breaks or supplies at most one explicitly reported late-window coverage slot.

Replay against frozen 23-29 Oct inputs.

### Challenger B — non-terminal sweep research

Starting from A, change only sweep admission:

- terminal negative goal screen becomes `DEPRIORITIZED_RESEARCH`, not model-equivalent exclusion;
- replace fixed four-row zero-authority control with a broader, deterministic secondary research lane;
- report exact source-visible -> researched -> rankable funnel;
- preserve friendlies/country/league exclusions and tournament-proof requirements.

Do not infer that all negative screens are good matches. The purpose is recall and full Football C comparison, not automatic promotion.

### Challenger C — qualification vs priority semantics

Starting from the better of champion/A/B:

- G3-funded becomes QUALIFIED;
- FOCUS is assigned only after global rank selection;
- final admitted board is capped;
- RESERVE/REVIEW_ONLY remains visible;
- presentation is sorted by kickoff only after selection freezes.

This can initially be a display/semantic challenger if the underlying selection is unchanged.

### Operational repair — Sheets parent run persistence

Repair `Sweep Runs` parent-row persistence independently of predictive logic.

This is an operational integrity fix and should not be bundled with model tuning.

## 10. Replay metrics

For each frozen slate from 24-29 Oct, compare champion vs A vs B without using outcomes to build the challenger.

Report:

1. source-visible prematch fixture count;
2. in-scope count;
3. researched-before-kickoff count;
4. terminal/deferred count;
5. eligible/rankable count;
6. G3-funded count;
7. globally admitted top-N count;
8. late-window candidate recall;
9. exact G3/O2.50 certificate clear rate;
10. exact funded burden clear rate;
11. 3+ and 4+ reach;
12. PASS/STOP false-negative controls;
13. first-assessment deadline losses;
14. selection displacement manifest: champion vs challenger.

The key acceptance test is not ROI and not one night of final scores. The challenger must improve selection separation and later-window recall without destroying the lower-burden G3 signal.

## Governance decision

**KEEP CURRENT CHAMPION FROZEN ONLY AS A REFERENCE; DO NOT TREAT IT AS VALIDATED.**

**Status: DEEP PIPELINE REPAIR REQUIRED.**

Priority order:

1. repair FOLLOW global-selection semantics;
2. repair sweep rank-universe completeness/terminal-screen semantics;
3. separate qualification from FOCUS priority and restore the admitted-board cap;
4. repair Google Sheets parent-run persistence;
5. replay each challenger separately;
6. only then promote one coherent champion.

The central lesson from the last few days is that the audit process itself became a source of model drift. Further fixes must be isolated, same-information and attributable.
