# Football Step 1 — goal-first full-queue research screen

**Production research scheduler for new prospective /rank executions, 2026-10-10 onward.**
`GOAL_FIRST_STEP1_RESEARCH_V1` changes **which matches receive deep research**, not which fixtures exist, their frozen Step0 admission, the C/C2 model decisions or official betting rules.

## Reason

An 8-fixture initial Step0 **operational** handoff is not an 8-fixture **football-scoring** search. On 2026-10-10, Go Ahead Eagles–Sparta was frozen as credible operational A at queue #13 but received no Step1 C/C2 scoring model execution, later ending 3–3. Inter–Parma was queue #15 in an earlier sweep; a later board did rank Inter and reject a high bookmaker line, which is **a separate** Step2 calibration question.

A high-scoring final result is **audit evidence**, never input to a historical prematch screen. Do not retrofit these results to claim the new scheduler would certainly have picked them.

## Strict stage separation

1. Validate the original complete Step0 source, source hash, A/B identity, UTC KO, league profiles, competition coverage and **immutable queue ranks 1..N**. Preserve the Step0 **ADMITTED first eight** and **CAPACITY_DEFERRED remainder** exactly, including in Airtable and the original ZIP.
2. Before **any new deep Step1 research**, run a **single bounded lightweight football-history pass for *every* A/B fixture**. Use only results demonstrably completed before the screen epoch (4–10 latest competitive games per team if available); capture separate home and away published historical goal scores, verified public HTTPS source and observation timestamp. No XI research, market shopping or full model execution at this stage. Limit source attempts per candidate so the screen does not turn into a second multihour sweep.
3. Record `QUANTIFIED` (team-history heuristic, not calibrated goal probability), `EVIDENCE_LIMITED` (no fabricated goal rate, neutral scheduling baseline), or `CLOSED` (fixture started/KO elapsed). A blank form sample is not evidence of low scoring. The score combines each team's scoring, the other's concession, recent >=3-total frequency and natural <=2-total stall profile. **No results from the fixture being scheduled** and no post-screen observations, odds, bookmaker market total, user bet, FT settlement or C/C2 outputs.
4. Freeze a separate `research_priority_manifest` against the existing **source_payload_hash**, with **all original ranks unchanged**, all fixture IDs counted and independent `initial_research_match_ids` (maximum eight). Source-backed route score and verified urgency influence research order; C and C2 still independently predict **after** this selection. Neither an operational A/B grade nor a research priority guarantees FOLLOW or BET.
5. For deep Step1 initial wave, research the manifest's **eight current prematch** candidates, which may legitimately include a **Step0-capacity-deferred** fixture such as original #13. Tag each promotion `STEP1_GOAL_SCREEN_PRIORITY`; preserve the original `Step0 Capacity Queue Rank`, original disposition and original source proof. Originally admitted fixtures not selected for deep research remain eligible in the rest of the **same full A/B research queue**. Do not claim an original Step0 re-admission or alter its package.
6. Before *each* deterministic replenishment call, use `research_schedule_policy=GOAL_FIRST_STEP1_RESEARCH_V1`, the full same-source `research_priority_manifest`, the original complete A/B candidate list, unique researched IDs and a **current attested UTC time**. This can select unresearched original Step0-admitted or deferred rows, skipping genuinely started fixtures. Re-screen after **three hours**, never reuse a future/stale epoch. Keep the 8 initial, 12 standard and **20 adaptive maximum**, with time/next KO verification after twelve and the new zero-FOLLOW refill behavior.
7. The existing **match-specific Step1 intake gate** still requires real current fixture bookmaker line/source/time and verifiable team-news/XI channels. Execute the independent C+C2 board. Actual Step2 still requires genuine fresh executable odds and its current hard integrity checks.
8. Persist screen coverage, initial/promotion order, source digest, reason for EVIDENCE_LIMITED, original operational rank, time attestations, and any research exhaustion reason. The full original ledger must remain immutable.

## CLI usage

Create `goal_route_prescreen.json` with:

```json
{
  "schema_version": "football-goal-route-prescreen-v1",
  "run_id": "SWEEP-... (original Step0 run ID)",
  "source_payload_hash": "exact original frozen hash",
  "screen_at_utc": "2026-10-10T10:00:00Z",
  "candidates": [
    {
      "match_id": "original source match ID",
      "queue_rank": 1,
      "operational_grade": "A",
      "fixture_status": "PREMATCH_CONFIRMED",
      "kickoff_utc": "2026-10-10T16:00:00Z",
      "football_evidence": {
        "home": {
          "source_url": "https://scores.example.org/club-home",
          "observed_at_utc": "2026-10-10T09:59:00Z",
          "recent": [
            {"kickoff_utc": "2026-10-09T15:00:00Z", "goals_for": 2, "goals_against": 1}
          ]
        },
        "away": null
      }
    }
  ]
}
```

**Example only**; incomplete `recent` correctly produces `EVIDENCE_LIMITED`. In actual runs supply the entire preserved A/B queue, not one selected fixture.

`python models/football/engine/goal_route_prescreen_cli.py --input goal_route_prescreen.json --output goal_route_screen.json`

From the output, use `initial_research_match_ids` for the new Step1 deep wave. Supply `manifest` in subsequent `capacity_replenishment_cli.py` calls, for example:

```json
{
  "budget_policy": "COMPACT_GOAL_ROUTE_V1",
  "research_schedule_policy": "GOAL_FIRST_STEP1_RESEARCH_V1",
  "source_payload_hash": "same exact Step0 source hash",
  "research_priority_manifest": {"schema_version": "football-goal-first-research-manifest-v1"},
  "research_at_utc": "current VERIFIED UTC timestamp",
  "follow_count": 0,
  "reserve_count": 0,
  "researched_match_ids": ["all unique actually researched match IDs"],
  "candidates": ["entire original A/B queue in capacity_replenishment schema"]
}
```

The manifest and candidate-list placeholders must be replaced by **actual complete validated data**. Omitting the schedule-policy field retains **unchanged historic Step0 rank order**, for old frozen boards and legacy workflows.

## Reporting

Always report: discovered vs A/B, quantified/limited/closed counts, original Step0 admissions and queue ranks, actual goal-first deep research IDs and priorities, overflow, actual researched count, C FOLLOW/RESERVE/STOP, and research-budget/fixture time disposition. No speculative losses or hypothetical bets in C official accounting. C2 remains shadow-only.

**Outcome QA:** count genuinely prospectively screened missed 3+/4+ fixtures and false positives after FT over a meaningful sample. Don't loosen C/C2 betting gates because a deferred match retrospectively finished high.
