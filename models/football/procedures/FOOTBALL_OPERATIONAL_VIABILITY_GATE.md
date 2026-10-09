# Football Operational Viability Gate

**Status:** mandatory Step-0 production gate  
**Purpose:** stop low-observability fixtures from consuming Football C research and Step-2 attention.

This gate is operational, not predictive. It must not prefer a fixture because it looks high-scoring or because its market price is attractive.

## 1. Required preflight fields

Every in-scope senior fixture that survives hard identity/time exclusions must receive:

- `operational_viability_grade = A / B / C / D`;
- `xi_expected = YES / UNCERTAIN / NO`;
- `market_observability = HIGH / MEDIUM / LOW / NONE`;
- `team_news_observability = HIGH / MEDIUM / LOW / NONE`;
- `operational_viability_reason = <compact evidence-based reason>`.

Use the competition's current accessible information to assign the **raw current grade**. Then apply `models/football/procedures/FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md` as a separate historical cap. Do not blend predictive results into either layer, and do not claim that XI is expected merely because the fixture is senior.

## 2. Grades

### A — EXECUTABLE

Use A only when all are true:

- `xi_expected = YES`;
- `market_observability = HIGH`;
- `team_news_observability = HIGH / MEDIUM`;
- fixture identity/time is reliable;
- the normal researchability gate can be completed cheaply.

A fixtures may receive normal Football C board treatment and, if football quality also clears, routine FOLLOW.

### B — CONDITIONAL

Use B when:

- `xi_expected = YES / UNCERTAIN`;
- `market_observability = HIGH / MEDIUM`;
- `team_news_observability = HIGH / MEDIUM`;
- researchability still clears;
- one operational channel is weaker than A.

B fixtures may enter Football C after A-grade candidates but are **not routine FOLLOW candidates at board time**. A B-grade C-FOCUS can be retained at most as RESERVE until confirmed XI/current executable market evidence is actually available or the user explicitly reopens it.

### C — LOW OBSERVABILITY

Use C when any material execution channel is weak, for example:

- no reliable expectation of a confirmed XI;
- lineup/team-news information is consistently absent or arrives too late to be useful;
- only thin or unstable Asian-total market visibility exists;
- research depends mainly on scorelines/H2H because current mechanism/news data are sparse.

Normal disposition:

`LOW OPERATIONAL OBSERVABILITY — STEP0 EXCLUDED`

C fixtures do not enter the normal Work board. A user-declared exception may reopen them, but all other integrity gates still apply.

### D — NON-OPERATIONAL

Use D for amateur/development/micro blocks, unreliable fixture identity, effectively absent market/lineup ecosystem, or other cases where routine execution is not realistic.

Normal disposition:

`NON-OPERATIONAL FIXTURE — STEP0 EXCLUDED`

This complements, and does not weaken, the existing hard-scope exclusions.

## 3. Competition size is not the rule

Do not automatically exclude a league because it is small, unfamiliar, lower division, women's football, or from a particular country.

Do exclude or demote it when the **observable execution ecosystem** is poor.

A small league with dependable XI, team news, market and current data can still be A/B. A famous competition with materially unavailable execution evidence can still be B/C for the affected fixture.

For senior women's domestic top-flight fixtures, grade the actual XI/market/team-news ecosystem. Do not infer LOW/NONE observability from the competition being women's football or from audience size alone.

## 4. Persistent competition reliability cap

Before capacity selection, retrieve the current competition state:

`UNPROVEN / TRUSTED / NEUTRAL / CAUTION / DEMOTED`

Rules:

- UNPROVEN / TRUSTED / NEUTRAL: no historical cap; current raw grade stands.
- CAUTION: raw A is capped to B.
- DEMOTED: raw A/B becomes C by default.
- DEMOTED recovery: at most one fixture from that competition per sweep may enter as B probation when the current fixture independently clears every raw A requirement. A raw B fixture is not sufficient for probation.
- history may never promote B->A or C->B.
- an explicit user exception may reopen a fixture but does not waive any other integrity gate.

Persist the reliability state and reason with the fixture so later audit can reconstruct why the final operational grade differed from the raw current grade.

### Prospective compact Work budget override

For sweeps **created after 2026-10-09** whose authoritative cursor/handoff carries `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1`, apply `FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md`: initial **8** unique fixtures from the **complete** deterministic A/B operational queue; 12 maximum routine unique deep-researched fixtures in the slate; automatic replenishment only while FOLLOW+RESERVE <4. No league-historical O2.5 feature enters operational A/B grading or queue rank. A/B Asian total-market observability must be based on an identifiable current match-specific market surface, not a historical O2.5 leaderboard. Current/frozen legacy sweeps without that policy preserve Section 5's original 15 limit and normal legacy replenishment.

## 4A. XI-verified queue admission proof — new compact sweeps / optional marked unfinished legacy

An operational letter grade is **necessary but not sufficient** for Work eligibility. Apply `FOOTBALL_XI_MARKET_FIRST_INTAKE.md` before constructing the A/B Work queue for all new compact runs and marked unfinished legacy runs with `strict_intake_policy=XI_MARKET_FIRST_V1`. Reject `xi_expected=UNCERTAIN` as a **final Work queue status**, even if its preflight grade is B, until match-specific source proof demonstrates actual recent starting-XI availability for both teams. Require a current, fixture-linked and time-stamped Asian goal-total market, plus adequate team news, official competition tier and identity integrity. A fixture with a raw preliminary B may be closed with `XI_CHANNEL_NOT_VERIFIABLE`, not admitted.

This must never silently remove required/protected or women's top-flight raw coverage. Real observable XI+market ecosystem, **not gender or league popularity**, determines routine researchability. A user one-match exception may reopen screening, not waive proof for an official C market action. For already frozen complete/legacy handoffs without the marker, preserve historic semantics.

## 5. Step-0 capacity cap

The normal production handoff to Work is capped at:

`MAX_WORK_ADMISSIONS = 15`

Selection order is operational, never predictive:

1. A-grade fixtures before B-grade fixtures;
2. stronger XI/market/team-news observability before weaker observability;
3. protected major competition classes may break otherwise-equal ties;
4. never use expected goals, Over profile, model state, or attractive odds to decide Step-0 capacity.

If more than 15 A/B fixtures clear, preserve the overflow as:

`OPERATIONAL CAPACITY DEFERRED — STEP0`

A capacity-deferred fixture is not a Football C PASS and is not a coverage failure. It remains recoverable by explicit user exception.

## 6. Protected competition classes

Protected international/continental classes may bypass the ordinary domestic **researchability exclusion**, but they do **not** bypass this operational viability declaration.

If a protected fixture is temporarily B, it may be retained subject to the 15-match cap. If it is C/D because XI/market/team-news observability is materially inadequate, keep the explicit operational disposition rather than pretending it is executable.

## 7. Handoff contract

The normal Step-0 funnel is:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C`

Every admitted Work fixture must be A or B and carry all five current operational fields plus `competition_reliability_state` and `competition_reliability_reason`.

Work must fail closed if a C/D fixture leaks into the board payload.

## 8. Follow-through boundary

Operational viability does not change Football C's predictive state.

- A-grade C-FOCUS: normal FOLLOW/RESERVE rules may apply.
- B-grade C-FOCUS: maximum routine lane is RESERVE at board time.
- C/D: must not enter the normal board.
- User exception: may reopen research/Step 2, but does not waive tournament-incentive, XI, market, or evidence-integrity rules.

## 9. Audit

Audit these separately:

- predictive false negatives/positives among admitted A/B fixtures;
- operational exclusions;
- capacity deferrals;
- cases where `xi_expected` proved wrong;
- competitions repeatedly producing B/C because XI, team news or executable totals are unavailable.

Repeated operational failures update the persistent competition reliability memory through the post-slate audit. The memory may cap future fixtures, but it must not retroactively alter historical board states.
