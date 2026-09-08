# Football Match Sweep & Research Procedure

**Status:** ACTIVE / mandatory fixture-source and model-routing procedure  
**Effective:** 2026-09-08 ICT  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Official model:** Football v0.2.49  
**Shadow comparison models:** Football v0.2.47 CLEAN and Football v0.2.48-SHADOW

This procedure defines two things that must stay separate:

1. how the fixture universe is built; and
2. how an already-discovered match is researched and routed through the models.

The separation is deliberate: **AiScore controls fixture discovery; research remains source-flexible.**

---

## 1. Fixture sweep authority — AiScore only

For any daily slate, upcoming-match request, or requested time window, the fixture universe must be swept from **AiScore only**.

Allowed fixture-discovery source family:

- `aiscore.com`
- `m.aiscore.com`
- AiScore daily/live fixture listings and AiScore match pages

No other source may add a fixture to the slate.

Do **not** build a union from Soccerway, FotMob, Google/web search, Bzzoiro/BSD, Flashscore, league sites, bookmaker pages, or any other schedule source.

If another source reveals a match that is not present in the AiScore sweep, do not silently add it. Verify whether it exists on AiScore first. If it cannot be verified on AiScore, it is outside the active fixture universe for that sweep.

If AiScore is unavailable or cannot be traversed sufficiently for the requested window, state:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

Do not backfill the missing universe with another schedule provider.

---

## 2. Sweep window and traversal

1. Resolve the requested window in ICT.
2. Traverse the relevant AiScore daily/live listing completely for that window.
3. Include the established overnight continuation when the requested slate spans past midnight.
4. Record every discovered fixture before attractiveness filtering.
5. Normalize team names, competition names, and kickoff times to ICT.
6. Deduplicate only obvious duplicate representations of the same AiScore fixture.
7. Apply competition eligibility only after the AiScore universe is captured.

The visible board may be compact. The AiScore universe must still be screened completely.

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

---

## 3. Coverage meaning under a single-source sweep

The previous multi-source-union concept is no longer the active fixture-source policy.

For this workflow, coverage completeness means:

- the relevant AiScore listing/window was traversed completely;
- every AiScore fixture in the requested window was accounted for;
- eligibility/exclusion was applied explicitly;
- every eligible fixture received a PRE disposition;
- coverage counts reconcile.

`Reconciled = true` may be used when the AiScore sweep itself was fully traversed and normalized for the requested window. It does **not** require agreement from an independent schedule source.

Recommended coverage-source fields:

- `Source 1 = AiScore`
- `Source 2 = blank` unless used only as a research/reference note

A non-AiScore research source must never become a second fixture-universe authority.

---

## 4. Eligibility and screening

After the AiScore universe is frozen for the window:

1. apply the active competition eligibility rules;
2. mark excluded fixtures explicitly rather than omitting them;
3. screen every eligible fixture structurally;
4. assign PRE grade and structural type;
5. assign FOCUS / WATCHLIST / PASS / UNRESOLVED;
6. preserve all FOCUS and relevant WATCHLIST fixtures through the XI stage.

The active official ranking priority is defined by Football v0.2.49 and its current operating documents.

---

## 5. Match research runs normally

Once AiScore has established that a fixture belongs to the universe, research may proceed normally using the best available sources.

Research sources may include, where useful:

- official club, league, and competition sources;
- Soccerway for confirmed lineups or match information;
- FotMob;
- FBref;
- Bzzoiro/BSD where supported;
- reputable statistical databases;
- reliable news/team sources;
- user-supplied lineup, market, and match screenshots;
- general web research when needed.

Use normal source-quality judgment for the research task.

Research may establish or refine:

- GF/GA profile;
- scoring/conceding frequencies;
- home/away splits;
- chance quality;
- xG/xGA/xGOT where available;
- big chances / box access / SOT quality;
- injuries, suspensions, rotation, and incentives;
- confirmed XI and bench depth;
- tactical shape;
- failure modes;
- Asian-total market expression.

**Research source flexibility does not change fixture-universe authority.**

---

## 6. Metadata corrections

A research source may flag that an AiScore kickoff, team alias, or competition label appears wrong.

When this happens:

1. verify the fixture identity against AiScore;
2. correct the working metadata only when the same AiScore fixture is clearly identified;
3. record the correction in coverage notes when material;
4. do not use the correction as a reason to add a non-AiScore fixture.

AiScore remains the discovery authority even when another source provides better match-level detail.

---

## 7. Model routing — one official + two shadows

Every eligible match that reaches a material model verdict should be evaluated from the **same frozen evidence snapshot** through three tracks:

### Official

**Football v0.2.49**

- active official selection model;
- includes the v0.2.49 two-sided-priority patch;
- only this track may create official P/L.

### Shadow 1

**Football v0.2.47 CLEAN**

- run as a legacy clean-model comparison;
- evaluate the same evidence state without the v0.2.49 two-sided-priority patch;
- never enters official P/L.

### Shadow 2

**Football v0.2.48-SHADOW**

- run as its own shadow-model comparison on the same evidence state;
- apply its documented v0.2.48 shadow deltas;
- do not silently import the v0.2.49 priority patch unless a future rule explicitly says so;
- never enters official P/L.

The shadows are comparison tracks, not vetoes. A shadow HOLD/PASS does not suppress an official v0.2.49 decision.

---

## 8. User-facing pick output

For a material final evaluation, show all three tracks when useful:

### Official v0.2.49

- `OFFICIAL LOCK — O<line> @ <odds>`
- `NO BET — HOLD`
- `PASS`

### Shadow v0.2.47

- `SHADOW v0.2.47 LOCK — O<line> @ <odds> — DO NOT PLACE`
- `SHADOW v0.2.47 HOLD`
- `SHADOW v0.2.47 PASS`

### Shadow v0.2.48

- `SHADOW v0.2.48 LOCK — O<line> @ <odds> — DO NOT PLACE`
- `SHADOW v0.2.48 HOLD`
- `SHADOW v0.2.48 PASS`

Only the official v0.2.49 affirmative selection is an actual bet.

---

## 9. Airtable / decision logging

- Official v0.2.49 LOCKs go to the official Website Picks/P&L workflow.
- Official v0.2.49 material states must be logged with model version `v0.2.49`.
- v0.2.47 shadow material states must be logged with model version `v0.2.47` and treated as shadow/comparison only.
- v0.2.48 shadow material states must be logged with model version `v0.2.48-SHADOW` and treated as shadow/comparison only.
- Shadow states never enter official P/L.
- Existing Daily Coverage Ledger fields named for v0.2.47 and v0.2.48 remain shadow-comparison fields; do not overwrite their meaning with the v0.2.49 official verdict.

If a dedicated v0.2.49 PRE field does not yet exist, preserve the official v0.2.49 state in the material Decision State / notes workflow rather than relabeling a v0.2.47 field.

---

## 10. Late discovery under AiScore-only policy

If an eligible fixture was present on AiScore for the requested window but was omitted by the sweep process and is found before kickoff:

`LATE-DISCOVERED BUT SCREENED`

If it was on AiScore but was never properly assessed before kickoff:

`TRUE MISSED SCREEN`

A fixture discovered only through a non-AiScore research source is not added until its presence on AiScore is verified.

---

## 11. Conflict precedence

This procedure is the active authority for fixture-source policy and three-track routing.

Where an older file instructs the workflow to:

- build a multi-source fixture union;
- require an independent schedule source for reconciliation;
- allow another provider to add fixtures; or
- output only v0.2.49 official + one v0.2.48 shadow track,

this procedure supersedes those instructions.

The betting/model rules themselves remain governed by their respective canonical model files.

---

## Operating principle

**Sweep with AiScore only. Research the match normally. Route the same evidence through v0.2.49 official, v0.2.47 shadow, and v0.2.48 shadow. Only v0.2.49 enters official P/L.**
