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

Use the competition's current accessible information plus recent operational history when known. Do not claim that XI is expected merely because the fixture is senior.

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

## 4. Step-0 capacity cap

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

## 5. Protected competition classes

Protected international/continental classes may bypass the ordinary domestic **researchability exclusion**, but they do **not** bypass this operational viability declaration.

If a protected fixture is temporarily B, it may be retained subject to the 15-match cap. If it is C/D because XI/market/team-news observability is materially inadequate, keep the explicit operational disposition rather than pretending it is executable.

## 6. Handoff contract

The normal Step-0 funnel is:

`RAW SENIOR -> HARD EXCLUDED -> OPERATIONAL EXCLUDED -> RESEARCHABILITY EXCLUDED -> CAPACITY DEFERRED -> ADMITTED TO C`

Every admitted Work fixture must be A or B and carry all five operational fields.

Work must fail closed if a C/D fixture leaks into the board payload.

## 7. Follow-through boundary

Operational viability does not change Football C's predictive state.

- A-grade C-FOCUS: normal FOLLOW/RESERVE rules may apply.
- B-grade C-FOCUS: maximum routine lane is RESERVE at board time.
- C/D: must not enter the normal board.
- User exception: may reopen research/Step 2, but does not waive tournament-incentive, XI, market, or evidence-integrity rules.

## 8. Audit

Audit these separately:

- predictive false negatives/positives among admitted A/B fixtures;
- operational exclusions;
- capacity deferrals;
- cases where `xi_expected` proved wrong;
- competitions repeatedly producing B/C because XI, team news or executable totals are unavailable.

Repeated operational failures should lower future competition preflight confidence. Do not retroactively alter historical board states.
