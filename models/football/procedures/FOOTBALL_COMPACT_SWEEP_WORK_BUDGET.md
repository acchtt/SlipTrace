# Football Compact Sweep / Work Budget — v1

**Status:** ACTIVE FOR NEW STEP-0 RUNS from 2026-10-09 ICT forward. **Do not retrofit an existing frozen or RUNNING sweep.**  
**Activation:** User request to reduce over-broad sweeps after reviewing the 2026-10-09 historical goal-route pilot.  
**Authoritative pair:** Football C official / C2 shadow; both still require the existing common evidence/engine reconciliation.  
**Policy ID:** `COMPACT_GOAL_ROUTE_V1`

## 1. What the historical result actually supports

The five-complete-league match-level scoreline pilot found that Over 2.5 was often bidirectional, but league-average O2.5 and 5+/BTTS distributions changed between seasons. A naive chronological six-match veto `both teams <= 2 of their last six O2.5` was independently tested on 1,140 evaluable historical fixture examples: it held only 42 fixtures (3.7%) and **25 of the 42 (59.5%) still finished O2.5**. That filter is **not** a proven negative predictor and is **NOT ACTIVATED** as a hard rejection rule.

The operational pain point is the breadth of **deep Work research**, not a justification to delete the raw source ledger or overfit a goals-only league allowlist. This update is a reversible **workload budget**, not a predictive C/C2 model feature.

## 2. Compact admission scope

- Source acquisition, senior fixture discovery, source/time identity, raw coverage and deduplication remain unchanged. Every sourced protected/required senior block and visible senior women's top-flight block must still receive a valid disposition.
- Hard scope restrictions remain in force: Israel, Kenya, Iraq, Wales and Kuwait **domestic** leagues/cups, and Germany **3. Liga only**; major official national-team/continental competitions are not excluded by nationality.
- Operational A/B/C/D remains strictly XI / Asian-total market / team news / identity / mechanism evidence; competition reliability is operational only.
- **Do not spend targeted external verification budget on an obviously C/D or user-excluded block.** Source-local evidence must justify the C/D classification; otherwise a plausible A/B block stays in the bounded verification queue. Never invent a grade to save time.
- For A/B status, require a **current match-specific obtainable Asian goal-total market**, not just general O2.5 statistics from a comparison website; for B a verified executable **market family / bookmaker screen** with current fixture identity is adequate even if final exact executable entry quote must wait for Step 2. No verified market: `MARKET OBSERVABILITY UNRESOLVED` / nonactionable until recovered, not an invented B.
- A higher or lower historical league over-rate **cannot** upgrade/downgrade current operational grade; it cannot decide the Step-0 operational queue order, override market integrity or exclude an unfamiliar/women's/protected block.
- Persist all A/B fixture candidates and their operational queue rank; **do not silently discard queue overflow**. This is still the complete A/B queue; it is not a goal-scored shortlist.

## 3. Smaller active Work research footprint

For new sweeps carrying `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1`:

| Parameter | Value | Contract |
|---|---:|---|
| Initial deep Work wave | **8** | ranks 1–8 of frozen **operational** A/B queue; ranks 9+ remain explicitly `OPERATIONAL_CAPACITY_DEFERRED` |
| Routine unique-fixture research ceiling / slate | **12** | includes initial 8 + at most 4 replenished fixtures; excludes explicit user-directed exception work which must be separately tagged |
| Automatic replenishment target | **4 active lanes** | replenish only when current `FOLLOW+RESERVE < 4`, rather than trying to fill 10 every time |
| FOLLOW capacity | **6** | existing ceiling preserved |
| RESERVE capacity | **4** | existing ceiling preserved |
| Queue ranking | Operational A/B, XI, market, news, protected/major tie-break, canonical identity | **Never sort by O2.5%, goals, attractiveness, model state, odds, or projected winner** |

If routine research ceiling is exhausted, persist `COMPACT_RESEARCH_BUDGET_EXHAUSTED`; do not fabricate more picks. The frozen overflow pool stays auditable and can be reopened by a user exception or a separately authorized trial. If 4 active lanes exist, do **not** automatically research extra matches merely because more slots remain under the legacy maximum 10.

This policy shrinks the **initial Work wave** 15→8 and prevents unbounded automatic replenishment; it does **not** promise eight good bets. Zero FOLLOW is a valid final slate outcome.

## 4. Step 1 bounded goal-route check (context only, never hard veto)

For each admitted fixture's existing Step-1 common factual evidence epoch (before C/C2 apply their independent policies):
1. Check current competition format, draw/margin/qualification incentive, fixture status and expected lineup availability.
2. Summarize BOTH teams' latest verified competitive fixtures (prefer at least six each), with separate home/away if sample permits. Calculate joint `BTTS & O2.5`, `O2.5 with a clean sheet`, `0–0/1–1`, third-goal funding and tail 5+ share from **pre-kickoff-only** scores. If history incomplete, record `GOAL_ROUTE_UNVERIFIED`; do not infer the missing part.
3. Explicitly identify whether a supported Over can be cleared by: `TWO_SIDED_SCORING`, `ONE_SIDED_CARRIER_WITH_CONTINUATION`, `MIXED`, or `NO_CREDIBLE_CLEARING_GOAL`. A 3–0 outlier does not independently fund O2.75 in a subsequent match.
4. If `NO_CREDIBLE_CLEARING_GOAL`, the **existing** C completion/burden/route rules may yield PASS/STOP. C2 still performs its own shadow evaluation on exactly the same evidence; route diagnostic is not a new policy verdict.
5. Leave the current Asian-total price/available burden and opponent suppression authoritative. An Over-heavy league is not a betting signal.

The historical league table is optional reference context only, with **zero weight** in both model policies and all Step-0 ranks.

## 5. Compatibility, tests and rollout

- New sweeps must persist the policy ID in the Resume Cursor/hand-off metadata and obey its 8/12/4 budget. Use `models/football/engine/capacity_initial_wave_cli.py --input <capacity_queue_input.json>` for deterministic initial selection, and validate the serialized final handoff via `step0_handoff_cli.py`. /rank passes `budget_policy=COMPACT_GOAL_ROUTE_V1` and a deduplicated `researched_match_ids` list to `capacity_replenishment_cli.py` on every replenishment.
- For a legacy handoff with missing policy ID, use the original 15 initial Work slots and legacy refill-to-10 semantics; do not reinterpret it retrospectively.
- The user's still RUNNING `SWEEP-20261009-1300-20261010-0300` at **Chunk 12**, 3 pending, is explicitly **grandfathered/paused**. Do not alter its cursor, queue, ledger, reports, source hash or eligibility solely because of the compact policy.
- Every rank and replenishment replay should check `researched_match_ids` are **unique, actually present in the frozen A/B queue and no more than 12**. Reject missing evidence rather than implicitly granting another wave.
- Report raw discovered / user scope excluded / operationally screened / A/B full queue / admitted 8 / deferred remainder / actually researched / replenished separately. Raw coverage counts must never be described as the number of model selections.

## 6. Trial measurement and rollback

For the first three new boards, compare with the original 15/unbounded-work counterfactual **without predicting winners from future FT**: unique matches deep-researched, high-evidence matched pairs, C FOLLOW+RESERVE yield, exceptional opportunities missed among deferred, time/source faults, and user exception reopenings. **Rollback** `COMPACT_GOAL_ROUTE_V1` for new boards if the smaller wave repeatedly misses high-quality or actionable matches without a meaningful reduction in research workload. Never backfill frozen model verdicts from FT results.

Historical pilot: `models/football/research/OVER_FRIENDLY_ROUTE_SHAPE_PILOT_2026-10-09.md`.
