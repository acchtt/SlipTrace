# Football Repaired Handoff Authority

**Status:** ACTIVE STEP-0 INPUT AUTHORITY  
**Applies to:** `/rank` when the user supplies a repaired Step-0 handoff/ZIP  
**Purpose:** prevent Work/ranking from reopening fixture-universe repair

## 1. Repaired handoff marker

A repaired handoff is authoritative for Step 0 through either acceptance path.

### Path A — explicit repair markers

Accept when it contains:
- `repair_mode = true`;
- `repair_status = COMPLETE`;
- `repair_unresolved_count = 0`;
- `step0_fixture_universe_frozen = true`;
- `capacity_queue_complete = true`;
- complete fixture-level A/B queue ranks;
- complete protected/required/women coverage manifests required by the active launcher.

### Path B — structural compatibility for an already-produced repaired file

When the user explicitly supplies/describes the attachment as the repaired sweep, accept even if the older repair package predates the formal marker fields **only when local file validation proves**:
- every plausible A/B fixture in the package is fixture-level, not block-only;
- every A/B fixture has a unique positive `Step0 Capacity Queue Rank`;
- no repair/coverage unresolved row remains;
- protected/required/women manifests are complete under current launcher requirements;
- the initial/deferred dispositions reconcile exactly to the queue.

This structural compatibility check is file-local. Do not use the web to decide whether the repaired package is complete.

When accepted through either path:

`REPAIRED HANDOFF AUTHORITY: ACCEPTED`

## 2. What becomes frozen for /rank

The repaired handoff is authoritative for:

- fixture identity;
- competition identity;
- scheduled kickoff / timezone;
- requested-window inclusion;
- Step-0 disposition;
- operational grade and Step-0 observability fields;
- protected/required/women block reconciliation;
- `Step0 Capacity Queue Rank`;
- initial-admission/deferred state.

Ranking must consume these fields as frozen input.

## 3. Forbidden ranking behavior

After repaired handoff acceptance, /rank must not:

- search the web to re-verify fixture kickoff;
- search the web to rediscover the fixture universe;
- rebuild deferred competition blocks;
- replace a repaired kickoff with a search result;
- restart Step-0 source acquisition;
- call `/sweep repair` logic internally;
- infer a new capacity-queue order from web/source order;
- spend time corroborating already-frozen Step-0 fixture metadata.

Football research remains allowed for Step-1 modelling: team form, mechanisms, personnel context, H2H transferability, tournament incentives, etc. That research must not be used to mutate frozen Step-0 identity/time/queue fields.

## 4. Current-time filtering

/rank may exclude a fixture that has left the prematch window using:

- the **frozen repaired kickoff**; and
- current ICT.

No web kickoff re-verification is required.

Record:

`RANK SKIP — PREMATCH WINDOW CLOSED USING REPAIRED HANDOFF KICKOFF`

## 5. Contradiction discovered incidentally

If Step-1 football research incidentally reveals a material contradiction with a frozen repaired Step-0 field:

1. do not repair it inside /rank;
2. do not search additional fixture sites;
3. stop that fixture/block;
4. report:

`REPAIRED HANDOFF CONFLICT — RETURN TO STEP0 REPAIR`

Include only:
- fixture/block;
- frozen repaired value;
- conflicting observed value/source;
- field in conflict.

Continue other fixtures only when the conflict cannot contaminate their identity/time/queue ordering.

## 6. Failed authority preflight

If neither explicit-marker nor structural-compatibility acceptance passes:

`REPAIRED HANDOFF INCOMPLETE — STEP0 REPAIR REQUIRED`

Report the exact missing/inconsistent file fields. Do not use the web to complete them and do not attempt repair inside /rank.

## 7. Replenishment source

When a complete repaired handoff includes the full deferred A/B queue, /rank uses that attached queue as the primary replenishment source.

Airtable may be used only to:
- reconcile persisted state;
- persist Step-1 replenishment state;
- detect persistence drift.

Do not replace the attached repaired queue with a newly reconstructed Airtable/web queue.

## 8. Completion

Once accepted, Step-0 validation in /rank is contract validation only. It should be short and local.

Expected flow:

`ATTACHED REPAIRED HANDOFF -> CONTRACT VALIDATION -> CURRENT-TIME PREMATCH FILTER -> STEP1 RESEARCH/MODELS -> REPLENISHMENT -> BOARD`

Not:

`ATTACHED REPAIRED HANDOFF -> WEB FIXTURE SEARCH -> STEP0 REPAIR -> RANK`
