# Football Sweep Repair Mode

**Status:** ACTIVE BOUNDED REPAIR CONTROL  
**Applies to:** `/sweep repair ...`  
**Purpose:** repair an existing sweep/window without repeating full open-ended discovery

## 1. Trigger

When the user's command begins with:

`/sweep repair ...`

enter `repair_mode=true`.

Repair mode is not a fresh sweep.

It reuses:
- the existing persisted Sweep Run/window;
- the existing Daily Coverage fixture rows;
- already-verified fixture identities/times;
- already-resolved competition blocks;
- already-persisted source-acquisition state when still valid.

Do not restart full discovery unless a specific missing block cannot be reconstructed from the persisted run.

## 2. Repair target

Resolve exactly one target run:
- the explicitly named Run ID; or
- otherwise the latest sweep covering the requested repair window.

Persist:
- `Repair Mode = true`;
- `Repair Target Run ID`;
- `Repair Notes`.

If no matching prior run exists:

`SWEEP REPAIR BLOCKED — NO MATCHING PRIOR RUN`

Do not silently convert repair into a fresh full sweep.

## 3. Repair scope

Build a repair set from only:

1. block-level deferred rows that must now be expanded fixture-by-fixture because the current capacity policy requires a complete A/B queue;
2. fixtures with unresolved/conflicting identity;
3. fixtures with unresolved/conflicting kickoff;
4. required/protected/women's top-flight blocks whose fixture-level disposition is incomplete;
5. rows missing current mandatory queue/persistence fields, including any of the six Step-0 operational/reliability contract fields: `xi_expected`, `market_observability`, `team_news_observability`, `operational_viability_reason`, `competition_reliability_state`, `competition_reliability_reason`;
6. fixtures whose previously stored kickoff is contradicted by a current authoritative source.

Everything else is reused unchanged.

Do not re-research already-complete competitions just because repair mode is active.

## 4. Started-match rule

At the beginning of repair, establish current ICT once.

For every repair candidate:
- if authoritative kickoff < repair start time and fixture has started/finished, exclude from prematch modelling;
- preserve it in coverage accounting;
- set disposition/reason to the existing prematch-closed equivalent;
- do not spend additional time researching model viability.

This check happens **before** deep verification.

## 5. Bounded verification budget

Per unresolved competition block:

- use the existing persisted carrier/source first;
- then make at most **2 independent authoritative verification attempts** total;
- preferred order:
  1. official competition/club/provider fixture page when available;
  2. Flashscore or Soccerway corroboration;
- search-engine result pages are navigation aids only, not a reason to continue searching indefinitely.

Per known fixture:
- once identity + authoritative zoned kickoff are confirmed by one primary/current source with no material contradiction, stop;
- if a second source contradicts materially, use the second attempt to resolve;
- after two unresolved attempts, mark the row/block `REPAIR_UNRESOLVED` and move on.

Do not open third/fourth/fifth websites for the same competition in the same repair pass.

## 6. No web-search wandering

Repair mode must not:
- search broad phrases such as "October 2026 football fixtures" after the target competition/fixture is already known;
- enumerate unrelated competition pages;
- reopen complete blocks;
- search team-by-team when a competition-level fixture page is sufficient;
- keep searching after the verification budget is exhausted.

If a broad web result reveals a timing error for one known fixture, repair that fixture/block only and continue through the remaining repair set.

## 7. Time correction

When a stored kickoff is wrong:

1. preserve the old value in the repair note/audit text;
2. write the corrected authoritative UTC/ICT kickoff;
3. recalculate whether the fixture is still inside the requested sweep window;
4. recalculate whether it has already started;
5. update disposition accordingly;
6. do not restart the whole competition discovery unless the correction indicates a block-level parser/timestamp fault.

A single wrong fixture time does not automatically invalidate sibling fixtures.

## 8. Block timestamp fault

Reopen an entire competition block only when:
- multiple fixtures share a suspicious timestamp and at least one is proven wrong; or
- provider/source parsing clearly applied one incorrect kickoff to multiple fixtures.

Otherwise keep sibling fixture times intact.

## 9. Capacity-queue repair

For repair caused by the new global capacity queue:

1. expand only previously block-deferred plausible A/B blocks that lack fixture rows;
2. reuse all already fixture-level A/B rows;
3. remove already-started fixtures from prematch eligibility;
4. freeze the complete remaining A/B pool;
5. assign deterministic `Step0 Capacity Queue Rank`;
6. write queue ranks to Daily Coverage;
7. preserve existing operational grades/evidence unless a current hard fact invalidates them;
8. for every remaining A/B queue fixture, require all six Step-0 operational/reliability contract fields. Reuse persisted evidence first. If a field is genuinely absent, use the bounded repair budget to establish it; never infer XI/market/team-news observability or reliability reason from league reputation, grade, or fixture name;
9. if any required semantic field is still missing after the bounded attempts, mark that fixture `REPAIR_UNRESOLVED` rather than emitting a supposedly complete package;
10. output a repaired handoff for `/rank`.

Do not perform Step-1 football modelling inside repair mode.

## 10. Repair completion

Repair ends when every repair-set item is exactly one of:
- `REPAIRED`;
- `PREMATCH_WINDOW_CLOSED`;
- `REPAIR_UNRESOLVED`.

Persist:
- `Repair Unresolved Count`;
- `Repair Verification Attempts`;
- compact `Repair Notes`.

If unresolved count = 0 and required coverage/queue fields are complete, write these handoff markers into the repaired package:
- `repair_mode = true`;
- `repair_status = COMPLETE`;
- `repair_unresolved_count = 0`;
- `step0_fixture_universe_frozen = true`;
- `capacity_queue_complete = true`;
- `repair_target_run_id`;
- `repair_completed_at`.

Before packaging the repaired handoff, run the same deterministic normalizer/contract validator used by /rank:

`python models/football/engine/repaired_handoff_normalize.py --input <repair.json> --output <repair.normalized.json>`

Required success means both deterministic metadata normalization **and** validation of the complete A/B Step-0 operational contract. The validator must not synthesize semantic evidence. In particular, every admitted or capacity-deferred A/B fixture must carry:
- `xi_expected`;
- `market_observability`;
- `team_news_observability`;
- `operational_viability_reason`;
- `competition_reliability_state`;
- `competition_reliability_reason`.

If any are missing, the repair is not complete. Use:
`HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING`

Package the normalized structured payload only after that validator passes, then re-run the women counter/disposition equality and queue-rank reconciliation. Do not emit a repaired ZIP with missing semantic Step-0 evidence, contradictory duplicate dispositions, stale women counters, or non-boolean `women_top_flight`.

Then emit:

`SWEEP REPAIR COMPLETE — READY FOR /RANK`

If unresolved items remain:

`SWEEP REPAIR COMPLETE WITH UNRESOLVED ITEMS — /RANK BLOCKED`

Return the unresolved rows compactly. Do not keep searching in the same turn.

## 11. Runtime target

Normal expectation for repair mode is a **short bounded pass**, because it reuses the persisted sweep.

The workflow should prefer finishing with a small explicit unresolved list over spending a long period chasing perfect corroboration.

## 12. Airtable fields

Sweep Runs:
- `Repair Mode` — `fldjFlyBEoQ2N92t9`
- `Repair Target Run ID` — `fld1EptBTr3b4AfIK`
- `Repair Unresolved Count` — `fldgTZ1NpMOk4yilt`
- `Repair Verification Attempts` — `fld1PLeqyX9fdWSDi`
- `Repair Notes` — `fldSk62aouNLMZTNi`
