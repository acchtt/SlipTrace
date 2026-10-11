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

## 2026-10-11 Big Five top-flight dynamic research-priority overlay

**Active for new Step1 goal-first screens, not for historical frozen prescreens.** The engine applies `BIG_FIVE_DYNAMIC_GOAL_ROUTES_V1` only when the candidate explicitly carries an exact **country + competition name** for England Premier League, Germany Bundesliga, Spain La Liga, Italy Serie A or France Ligue 1. An arbitrary league named Premier League elsewhere and an unknown-country fixture cannot get this adjustment. All other leagues retain the original goal-first score; missing league metadata is neutral.

From each team's 4–10 **verified completed pre-screen competitive scorelines**, calculate the fraction of 4+ total goals and 0–0/1–1 draws, plus the existing 3+ frequency, goals scored/conceded and <=2-goal stalls. Use those verified samples to assign diagnostic route descriptions `BIDIRECTIONAL_CONTRIBUTION`, `ONE_SIDED_CARRIER`, `LOW_GOAL_DRAW_TRAP` or `MIXED_OR_UNVERIFIED`. The score adjustment is bounded to [-25,+8] and specifically penalizes repeated 0–0/1–1 draws, so repeated BTTS 1–1 does NOT become a third-goal signal. The output retains `big_five_route_screen` per original row and totals `big_five_route_screened_count`, `big_five_draw_trap_alert_count`. The manifest fingerprint covers these outputs.

The Oct 11 watchlist of clubs (Chelsea, Barcelona, Bayern, etc.) is a **research seed only**. Do not hardcode named-club bonuses or ever presume any future fixture will score because it was a historical 4+ environment. Score all quantified Big Five *teams*, including newly promoted or unfamiliar clubs, on the same available pre-screen evidence. The overlay cannot admit a source-excluded fixture, downgrade an operational A/B class, erase a deferred queue member, predict C/C2 supported line, price an odd, or create a bet. Missing or too-short evidence stays `EVIDENCE_LIMITED` with no bonus or forced low-goal flag. Use the same full original A/B queue.

The Big Five are already routine competition profiles under Step0; **this is a Step1 research scheduler improvement, not a Step0 broadening**. The 8/12/20 workload and C official / C2 shadow remain unchanged. Apply the normal current match Asian-total source, XI/team-news, tournament incentive and late-price checks at Step1/Step2. Do not change existing frozen manifests or source-hash values. Post-FT, audit **prospective** top-eight capture, 3+/4+ missed opportunity, 0–0/1–1 false-positive exposure and whether the book's live line was realistically reachable.

## 2026-10-11 Netherlands Eredivisie + Eerste Divisie goal-route research overlay

For NEW full A/B `GOAL_FIRST_STEP1_RESEARCH_V1` screens only, the Dutch **Eredivisie** and **Eerste Divisie** use `NETHERLANDS_DYNAMIC_GOAL_ROUTES_V1`, the same source-backed carrier-versus-two-sided and low-goal trap research-order diagnostic as the Big Five. The same required 4–10 completed historical competitive scorelines per club yield offense/concession route strength, share of **4+ total goals**, and 0–0/1–1 and <=2 goal stalls. The adjustment is bounded [-25, +8], not a calibrated total-goal probability or match-specific entry line. Big Five's independent policy remains unchanged; neither overlay is applied twice to one fixture.

Strict **country + registered league identity**, with no free-text Dutch/foreign competition bonuses. Accepted pairs are country `Netherlands` with `Eredivisie` / `Netherlands Eredivisie` / `Eerste Divisie` / `Eerstedivisie` / `Netherlands Eerste Divisie` (case-insensitive, trim spaces). Short league names belonging to Belgium, junior-only leagues or missing country DO NOT qualify. Official senior Eerste Divisie fixtures that include allowed **Jong/U21** participants remain eligible, exactly as currently registered; this changes research ordering, **not** Step0 league scope or the existing competition-scoped Jong exception.

Report `dutch_route_screened_count` and `dutch_draw_trap_alert_count`, with per-match `dutch_route_screen` diagnostics inside the fingerprinted immutable-source-bound manifest. Absent/stale/unverifiable past scores remain `EVIDENCE_LIMITED` (no bonus, no fabricated under/low-goal forecast). Real results must predate screen and KO; prospective research order does not access current-match goals, market odds or future XI. The policy does **not** automatically push PSV, Feyenoord, Go Ahead Eagles, Jong Utrecht, NAC, Emmen or any fixed shortlist to the board. A promoted research-priority item retains immutable Step0 A/B disposition, original match ID, source hash and queue rank.

Retain initial 8, standard 12, adaptive max 20 deep-research budgets; use the exact same Stage-1 approved lineup/news/bookmaker Asian-total evidence and Stage-2 executable price/time checks. C remains official, C2 shadow. New screens only: do not regenerate existing frozen manifests, rescore old boards, insert Airtable decisions or claim an improvement in Over returns without a prospective post-FT audit. Track Dutch baseline-to-overlay selected-wave shifts, high-total captures, 1–1/0–0 stall exposures and infeasible WAIT lines.

## Source-backed kickoff correction without changing Step0

A provider KO revision is a research routing discrepancy, **not** an
automatic match exclusion. Preserve the original Step0 kickoff_utc,
match ID, queue rank, grade and source_payload_hash exactly.

Optionally supply a researched_kickoff_evidence object for the same
fixture, with match_id, fixture_status=PREMATCH_CONFIRMED, kickoff_utc,
observed_at_utc and an independently captured public HTTPS source_url.
The provider observation must be within the past 30 minutes.
Never invent this proof, and never override an actually STARTED,
FINISHED, POSTPONED or CANCELLED match.

The prescreen includes both original kickoff_utc and
research_kickoff_utc, signed kickoff_drift_minutes,
KICKOFF_RECHECK_REQUIRED and source URL in the fingerprinted
manifest. Replenishment uses the observed kickoff to decide only
whether the fixture can still receive **football research**.
The original Step0 source and clock remain immutable.

The current /xi assessment must independently verify actual KO,
score/status, XI and newly priced market. If already started, route
to /live and use actual live odds. A stale old source time cannot
produce a retrospective premarket action.

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
