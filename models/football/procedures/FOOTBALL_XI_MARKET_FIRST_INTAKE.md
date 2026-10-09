# Football XI + Asian Market First Intake Gate (2026-10-09)

**Status: ACTIVE for new compact Step-0 /sweep runs; prospectively applies to their final Work handoff.**
**Runtime:** `models/football/engine/sweep_intake_evidence.py`, enforced by `step0_handoff_cli.py` for `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1`.
**Do not rewrite existing paused, frozen or historical sweeps.** This specifically grandfathered run `SWEEP-20261009-1300-20261010-0300` remains at Chunk 12 unless explicitly resumed by the user.

## What changed, and why

A hard cap of eight Work matches does **not** guarantee quality: the current 119-row source ledger carried eight `ELIGIBLE` fixtures, **five with `xi_expected=UNCERTAIN`**, despite the user's repeated reports about obscurity and no lineups. A raw discovered senior fixture is NOT an A/B Work candidate. We must prevent the `UNCERTAIN` B loophole from manufacturing an expensive candidate.

This is an **information availability gate**, not a betting prediction, league-performance rule or gender/country blacklist.

## 1. Funnel, scope and work budget

`SOURCE DISCOVERY (RETAIN) → USER/HARD SCOPE EXCLUSION → COMPETITION PROVENANCE → BOUNDED XI+MARKET PREFLIGHT → OPERATIONAL GRADE/RESEARCHABILITY → FROZEN A/B QUEUE → 8 INITIAL WORK / <=12 ROUTINE TOTAL`

Maintain raw senior source coverage, protected official internationals/continental competitions, required Netherlands Eerste Divisie and women’s senior top-flight **exact discovery and dispositions**. A source-visible fixture that lacks lineups/market is accounted for as an **explicit operational exclusion**, never silently omitted. User scope exclusions remain Israel, Kenya, Iraq, Wales and Kuwait domestic football and Germany **3. Liga only**. Senior national teams and international/continental teams from these countries are not automatically excluded.

### Unsupported competition block fast-close

If a domestic competition has verifiable source-local evidence that its normal XI, Asian goal-total market and team-news ecosystem cannot satisfy the gate, write a **competition/date block disposition** with source and exact reason (e.g. `XI_CHANNEL_NOT_VERIFIABLE` or `CURRENT_ASIAN_TOTAL_UNAVAILABLE`). Retain individual rows already captured, and retain required/protected/women top-flight fixture-level accounting. **No routine expanded block research** after the bounded cheap preflight. The result is **not** a predictive C-PASS or a finding that Overs are unlikely.

`small/obscure` is not a permissible standalone failure reason: classify competition senior/professional status from an official source, not reputation, team name, league country, or gender. Professional domestic lower divisions with genuinely reliable XI and Asian markets may qualify. Amateur/micro/development competitions are already hard-excluded. If evidence is missing, record `COMPETITION_SUPPORT_UNVERIFIED`, not an invented negative claim.

## 2. Mandatory A/B → Work **proof**, for both admitted and capacity-deferred queue members

All *new compact* A/B Work-queue rows, **including rank 9+ deferred**, must carry:

- `xi_expected=YES`, **not** `UNCERTAIN` or `NO`. Source **recent actual starting lineups** for each team separately, including `xi_home_recent_match_id`, `xi_away_recent_match_id`, `xi_home_recent_match_kickoff_utc`, `xi_away_recent_match_kickoff_utc` and fixture-specific `xi_home_lineup_source_url`, `xi_away_lineup_source_url`. Historical kickoff dates must precede the upcoming fixture and be within 240 days. Historical confirmed XI is proof the provider/competition actually publishes XIs, **not** an assertion that the upcoming lineup is already confirmed.
- `market_observability=HIGH/MEDIUM` **and** a current named **Asian total market**, with `asian_total_market_match_id` (matching the current canonical `match_id`), `asian_total_fixture_source_url`, `asian_total_market_observed_at_utc`, `asian_total_market_line` (e.g. 2.5 or 2.75), and `asian_total_market_bookmaker`. The evidence must concern **this match**, not a general O2.5 leaderboard, vague historic odds or a market implied from league popularity. Store the capture time explicitly and compare to the fixture kickoff; the observed quote must be within the previous 72 hours and never post-kickoff.
- `team_news_observability=HIGH/MEDIUM`, meaningful team-specific `team_news_source_url` (recent relevant news, availability, squad status or comparable).
- `competition_support_tier` from `PROTECTED_OFFICIAL`, `VERIFIED_PROFESSIONAL`, `VERIFIED_WOMEN_TOP_FLIGHT`, `MAJOR_SENIOR_DOMESTIC_CUP` or `USER_EXCEPTION`, plus `competition_official_url` and a compact `competition_support_reason`. Lower status, unsupported amateur/micro or unknown tier **cannot enter Work**. A named official source is evidence of identity/tier, not proof of bookmaker/XI availability.
- `fixture_identity_verified=true` and `fixture_kickoff_utc` with a zoned ISO 8601 timestamp; no stale, already-started or ambiguous kickoff admitted.
- `preflight_complete=true` with evidence metadata and normal researchability A/B/C checks, competition reliability cap, existing source/time validation. Missing one channel is **not** rescued by a high historical Over rate or projected lineup.

A/B grade by itself does **not** admit a fixture. `UNCERTAIN` may remain a *raw preliminary* B observation, but it cannot remain `ELIGIBLE`, `ADMITTED_TO_C` or `OPERATIONAL_CAPACITY_DEFERRED` in a new compact handoff. Final disposition after the bounded preflight:
- `XI_CHANNEL_NOT_VERIFIABLE — STEP0 OPERATIONAL EXCLUDED` when both teams' recent actual starting XIs cannot be demonstrated;
- `CURRENT_ASIAN_TOTAL_UNAVAILABLE — STEP0 OPERATIONAL EXCLUDED` for no current match-specific Asian total;
- `COMPETITION_SUPPORT_UNVERIFIED — STEP0 SCOPE/OPERATIONAL EXCLUDED` for unsupported competition level;
- `TEAM_NEWS_NOT_OBSERVABLE — STEP0 OPERATIONAL EXCLUDED` for no credible current news;
- `STEP0 PREFLIGHT INCOMPLETE — NO WORK ADMISSION` while the bounded check is not yet complete.

An explicitly requested one-fixture exception can reopen research, not waive XI/market/incentive/time evidence necessary for an official C action. For opaque but protected senior fixtures, preserve **exact source/fixture coverage**, then record the actual operational non-admission; don't label an entire women's or international competition nonoperational based on its category.

## 3. Efficient proof check per block

For ordinary domestic fixtures, share one competition/provider lineup surface and one totals/standings surface across the block; at most two quick public-web searches per unfamiliar block; use fixture-specific extra calls only where the shared source misses a plausible A/B fixture. Classify unknown after the bounded attempt instead of looping indefinitely. Proof must be from directly opened or otherwise verifiable original sources. No speculative `xi_expected=YES` because the match is popular.

Capture summary counts separately:
`raw_discovered`, `user_excluded`, `no_lineup_channel`, `no_asian_total`, `news_insufficient`, `unresolved_preflight`, `verified_operational_ab_queue`, `admitted_to_work`, `capacity_deferred`.
Do not equate discovered or preliminary A/B records with verified queue members.

## 4. Model boundaries and migration

- This is a stricter **prospective admission qualification**, not a revision of older C/C2 verdicts. C retains official predictive authority; C2 shadow. No result-based backfills.
- Preserve full A/B operational ordering and the 8 initial / 12 unique research / refill-to-4 compact policy *only after the proof gate*.
- Legacy 15-slot / 10-refill handoffs without compact policy **stay unchanged**. Paused 2026-10-09 Chunk 12 is not resumed, re-ranked, re-graded or rewritten by this change.
- The independent engine validator must reject compact handoffs with missing proof fields, `xi_expected=UNCERTAIN`, unsupported competition support, current-market evidence missing, or unverified identity.
- The user may request revalidation and reopening of any explicitly named fixture later, without adding a blanket league exception.
