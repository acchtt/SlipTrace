# 00 — Normal Chat: AiScore Researchable Senior Intake

**Use in:** Normal Chat, high reasoning.

Read upstream `models/football/CURRENT_MODEL.md` first.

Football C is the active official model.

## Purpose

Build a trustworthy **OPERATIONALLY VIABLE, RESEARCHABLE SENIOR** AiScore universe for the requested window.

The objective is the middle ground between the old narrow allowlist and the later over-broad senior sweep:

- do not miss meaningful senior blocks such as international qualifiers;
- do not send obscure, weak-data competitions to Work when there is not enough current evidence to assess them responsibly.

Operational principle:

`AISCORE SENIOR DISCOVERY -> HARD SCOPE FILTER -> OPERATIONAL VIABILITY GATE -> RESEARCHABILITY GATE -> CAPACITY GATE -> VERIFIED TIME/IDENTITY -> PACKAGE -> FOOTBALL C`

This intake is about **information quality and later executability**, not whether a competition is historically high-scoring.

Read and apply:
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`
- `models/football/airtable/FOOTBALL_COMPETITION_RELIABILITY_AIRTABLE.md`

The operational gate is mandatory for every surviving senior fixture before deep Work research.

## Default mode

`sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`

Do not use:
- legacy `NARROW_CORE` / PRIORITY-NORMAL-CONDITIONAL as the primary admission rule;
- unrestricted `BROAD_SENIOR_PRODUCTION`.

A prior sweep may be reused only if it was completed under RESEARCHABLE_SENIOR_PRODUCTION for a covering window.

## Source authority

AiScore remains the fixture-discovery authority.

Other public sources may be used only to determine whether a discovered AiScore fixture is sufficiently researchable. They may not create new fixtures.

## Time / identity integrity

Resolve the requested ICT/UTC window once and follow:

`models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`

Every admitted fixture must have:
- resolved AiScore identity;
- authoritative zoned kickoff;
- verified UTC;
- verified ICT;
- in-window proof.

Do not guess timezone from geography or treat a bare display clock as UTC.

## 1. Hard scope exclusions

Exclude before the researchability gate:

- youth/Uxx-only competitions;
- academy/junior competitions;
- reserve/B/development-only competitions, except reserve-branded teams participating in a normal professional senior league;
- amateur or clearly semi-professional micro competitions with unreliable identity/data;
- regional/state/provincial competitions outside the intended senior professional universe;
- school/university/military/company competitions;
- friendlies/exhibitions unless explicitly requested;
- cancelled/postponed/abandoned/already-finished fixtures for an upcoming sweep;
- unresolved fixture identity/home-away;
- unresolved authoritative kickoff;
- duplicates.

## 2. Competition reliability memory — mandatory

After senior discovery/hard scope filtering and before final operational grading:

1. normalize a stable competition key;
2. read the matching row from Airtable `Competition Reliability` (`tbl1KShXxXErUdVKW`);
3. if no row exists, use `UNPROVEN`;
4. preserve any explicit Manual Override without inventing one;
5. calculate the raw current A/B/C/D grade from current evidence;
6. apply the deterministic historical cap from `FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`.

Historical state behavior:
- TRUSTED / NEUTRAL / UNPROVEN: no promotion and no cap;
- CAUTION: max B;
- DEMOTED: default C; allow at most one B-grade probation fixture from that competition in the sweep only when the raw current grade independently clears full A requirements.

Persist:
- `raw_operational_viability_grade`;
- `competition_reliability_state`;
- `competition_reliability_reason`;
- `competition_reliability_sample` when available;
- `operational_viability_grade` after the history cap.

Do not use FT score, goals, C/C2 result, betting result or P/L to set this state.

## 3. Operational viability gate — mandatory

For every fixture surviving hard scope/identity/time checks, persist:

- `operational_viability_grade = A / B / C / D`;
- `xi_expected = YES / UNCERTAIN / NO`;
- `market_observability = HIGH / MEDIUM / LOW / NONE`;
- `team_news_observability = HIGH / MEDIUM / LOW / NONE`;
- `operational_viability_reason`.

Apply the procedure exactly:

- A = normal executable candidate.
- B = conditional candidate; may be admitted after A but cannot be routine FOLLOW at board time.
- C = `LOW OPERATIONAL OBSERVABILITY — STEP0 EXCLUDED`.
- D = `NON-OPERATIONAL FIXTURE — STEP0 EXCLUDED`.

Do not upgrade a fixture because its score history looks attractive. Small-league status alone is not a rejection; missing XI/market/team-news observability is.

## 4. Protected senior competition classes

The following classes bypass the ordinary domestic researchability exclusion when identity/time are valid, but they still require an explicit operational viability grade:

- FIFA senior World Cup qualifiers/finals;
- senior continental national-team qualifiers/finals (AFCON, EURO, Asian Cup, Copa America/CONMEBOL, Gold Cup/CONCACAF, OFC equivalents);
- senior Nations League-style official national-team competitions;
- major senior continental club competitions administered by UEFA/AFC/CAF/CONMEBOL/CONCACAF/OFC;
- other clearly major senior international tournament blocks explicitly requested by the user.

These are protected because the previous narrow sweep missed meaningful national-team blocks.

They still receive normal Football C PASS/WATCH/FOCUS screening later.

## 5. Researchability gate — ordinary domestic / small competition blocks

For all other senior domestic league/cup fixtures, run a **cheap researchability check** before admitting them to Work.

A fixture is `RESEARCHABLE` only when a quick preflight can establish enough current evidence for both teams to support the Football C evidence schema.

Minimum required evidence:

### Required A — recent team evidence
For **both teams**, at least one reliable source exposes a usable recent-match sequence/current form with opponents and scores.

### Required B — competition/context evidence
At least one reliable source exposes meaningful current competition context such as standings, phase/table, recent competition results, or equivalent tournament state.

### Required C — mechanism evidence
At least one of the following must be available without deep/manual hunting:

- team-level goal/chance profile;
- shots/SOT/box/chance-quality/xG-type statistics;
- reliable match/team statistical profiles;
- credible current team news/lineup/absence information that can materially inform routes;
- another repeatable quantitative or qualitative source sufficient to assess scoring mechanisms rather than only final scores.

### Required D — matchup/H2H availability
H2H is preferred when usable, but absence of H2H alone does **not** exclude a fixture.

However, if H2H is absent **and** mechanism evidence is weak, exclude.

### Admission rule

Admit when:
- Required A = PASS;
- Required B = PASS;
- Required C = PASS;
- fixture identity/time = PASS.

Otherwise exclude as:

`INSUFFICIENT RESEARCHABILITY — STEP0 EXCLUDED`

Do not spend deep Work research trying to rescue a competition that fails this cheap preflight.

## 6. What researchability is NOT

Do not exclude a fixture merely because:

- it is expected to be low scoring;
- its league was historically LOW-GOAL;
- it is from Japan or Finland;
- it is a professional lower division;
- it is a women's senior competition;
- it is unfamiliar;
- it is a cup.

If adequate current evidence exists, admit it and let Football C decide football quality.

Likewise, do not admit an obscure league merely because it is senior/professional if usable evidence is absent.

## 7. Efficiency rule

The researchability check must stay cheap.

Normal limit per unfamiliar competition block:
- one AiScore competition/fixture surface;
- up to two quick public-web searches for current team/competition evidence.

If those checks cannot establish A+B+C, exclude.

Do not turn Step 0 into the full Step-1 research process.


### Block timestamp collision sentinel — mandatory

Before `work_ready=true`, inspect admitted fixtures within each competition/date block for suspicious timestamp reuse.

Trigger a hard revalidation when either condition holds:
- 3 or more distinct fixtures in the same competition/date have the exact same verified UTC kickoff; or
- a two-legged/repeat pairing within 14 days receives the same UTC kickoff as the previous leg without a current canonical match-page proof.

When triggered:
1. do not trust the batch timestamp;
2. reopen the current AiScore canonical match page for every affected admitted fixture;
3. verify current match ID, date, home/away and Match Info UTC/API epoch individually;
4. rebuild the affected kickoff fields before packaging;
5. label any mismatch `SOURCE TIME / BLOCK PARSER FAULT`.

A uniform competition-block timestamp is never sufficient proof by itself.

## 8. Operational capacity gate

After A/B viability and researchability are known, cap the normal Work handoff at **15 fixtures**.

Order by operational quality only:
1. A before B;
2. stronger XI/market/team-news observability first;
3. protected major competition class only as an otherwise-equal tie-break.

Never use Over profile, expected goals, C/C2 state, or attractive odds to choose the 15.

Overflow remains recorded as:

`OPERATIONAL CAPACITY DEFERRED — STEP0`

It may be reopened only by explicit user exception.

## 9. Completeness

Production completeness means:

> every potentially relevant senior block in the requested window was discovered, then hard-excluded, operationally excluded, researchability-excluded, capacity-deferred, or admitted.

A skipped visible senior block with no recorded disposition makes the handoff incomplete.

For cross-midnight/early-morning windows, perform the normal terminal-interval recheck.

## 10. Persistence / counts

For every discovered in-window senior fixture preserve one disposition:

- `ADMITTED_TO_C`
- `HARD_EXCLUDED`
- `OPERATIONAL_EXCLUDED`
- `RESEARCHABILITY_EXCLUDED`
- `OPERATIONAL_CAPACITY_DEFERRED`
- `UNRESOLVED`

Record researchability reason compactly.

Required funnel counts:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C`

## 11. Work-readiness gate

Package only when:

- `complete=true`
- `actionable_complete=true`
- `work_ready=true`
- every visible senior block has a disposition;
- every admitted fixture is operational grade A or B;
- every admitted fixture has a competition reliability snapshot;
- no CAUTION fixture is admitted above B;
- no DEMOTED fixture is admitted except the allowed B-grade probation rule;
- admitted fixture count is <= 15;
- protected senior blocks were not removed by the researchability gate without an explicit operational disposition;
- every admitted fixture has resolved identity/time;
- terminal scan is complete where required;
- admitted count equals handoff array count.

If not:

`HANDOFF INCOMPLETE — RESEARCHABLE SENIOR COVERAGE GAP`

## 12. Canonical ZIP handoff

Create one root-level canonical `AISCORE_FIXTURES_*.txt` inside the ZIP.

Required metadata:

- `model=Football C`
- `sweep_scope_mode=RESEARCHABLE_SENIOR_PRODUCTION`
- requested ICT/UTC window;
- listing dates checked;
- terminal scan state;
- `complete=true`;
- `actionable_complete=true`;
- `work_ready=true`;
- `raw_senior_count`;
- `hard_excluded_count`;
- `operational_excluded_count`;
- `researchability_excluded_count`;
- `capacity_deferred_count`;
- `admitted_to_c_count`;
- protected-block audit result;
- admitted fixtures with identity/time provenance;
- per admitted fixture: raw operational grade, final operational grade, XI expectation, market observability, team-news observability, competition reliability state/sample/reason and operational reason.

Do not include hard-excluded, operationally excluded, researchability-excluded, or capacity-deferred fixtures in the Work array.

## 13. Step-0 boundary

Step 0 may determine whether enough evidence exists.

It must **not** decide:

- route strength;
- carrier strength;
- chance quality;
- supported burden;
- C-PASS/WATCH/FOCUS;
- rank;
- BET/WAIT/PASS.

Those remain Football C/C2 Step-1/Step-2 decisions.

## Output

Return:

`RESEARCHABLE SENIOR HANDOFF COMPLETE`

with:

- requested window;
- raw senior count;
- hard excluded;
- operationally excluded;
- researchability excluded;
- capacity deferred;
- admitted to Football C;
- unresolved = 0;
- ZIP filename.
