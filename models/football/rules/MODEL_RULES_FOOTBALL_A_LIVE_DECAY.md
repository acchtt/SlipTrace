# Football A — Predeclared Live-Decay Execution Patch

**Status:** ACTIVE OFFICIAL PATCH  
**Model:** Football A  
**Effective:** immediately from this commit  
**Purpose:** replace unrealistic planned prematch line-decay waiting with a controlled, predeclared live-decay execution path.

This patch is prospective. It does not create retroactive Website Picks, stakes, settlements, or P/L for earlier fixtures.

---

## 1. Core correction

Football A must no longer plan around the assumption that an Asian total will conveniently fall by 0.25 before kickoff.

When the football/XI thesis qualifies at a supported burden but the current prematch market is above that burden, the normal planned path is **not**:

`WAIT FOR PREMATCH LINE DECAY`

Instead use:

`QUALIFIED — LIVE DECAY PLAN`

The supported burden remains fixed before price. The market is allowed to reach that burden naturally after kickoff through clock decay.

Prematch movement may still be accepted if the user supplies it, but Football A must never require or expect a prematch quarter-line drop as the normal route to execution.

---

## 2. Prematch execution-feasibility classification

At final XI + odds review, classify the execution path separately from structural quality.

### 2.1 DIRECT PREMATCH

Use when the actual prematch line is no higher than supported burden, price clears the floor, and the Football A exposure gate passes.

### 2.2 QUALIFIED — LIVE DECAY PLAN

Use when:

- the structural thesis remains qualified after XI;
- the supported burden is lower than the actual prematch line, or the supported target price is not currently available;
- no structural hold applies;
- the match remains suitable for later execution if the live market reaches the protected burden under a clean state.

Persist before kickoff:

- supported target line;
- minimum target price;
- prematch offered line/price;
- expected live-decay route;
- maximum acceptable state window where relevant;
- dominant failure mode that would cancel the plan.

Do **not** label this as a realistic prematch wait.

### 2.3 STRUCTURAL HOLD / SHADOW

Existing structural hold and quarantined shadow rules remain unchanged unless this patch explicitly overrides live-decay treatment below.

---

## 3. Predeclared live-decay may become official exposure

A live Over reached through a **predeclared `QUALIFIED — LIVE DECAY PLAN`** is no longer automatically quarantined.

It may become an official lock only when all of the following are true:

1. the live-decay plan was frozen before kickoff;
2. the live line is at or below the predeclared supported burden;
3. the live price clears the active floor;
4. the score/time state has not materially invalidated the original scoring thesis;
5. no red card, major injury, tactical collapse, or other new negative information has damaged the routes;
6. the target is reached by ordinary clock decay rather than by a materially different match state that creates a new thesis;
7. the Football A upper-tail and priority-inversion exposure gates are re-run at the actual live burden;
8. the user supplies the current executable live line/price.

If all clear:

`DIRECT LOCK ELIGIBLE — PREDECLARED LIVE DECAY`

and, after the Football A exposure gate:

`OFFICIAL LOCK — LIVE DECAY PLAN`

Website Picks may be created only at the moment this live execution is actually approved. Never backfill a live lock after the market has moved or after a goal.

---

## 4. State integrity rule

The target line being numerically identical is not enough. A live O2.5 is not automatically equivalent to a prematch O2.5.

The model must distinguish:

- **clean clock decay:** target reached while the original thesis remains substantially intact;
- **state-changed decay:** target reached only after goals/cards/injuries/tactical events materially alter what is required from the remainder of the match.

A first goal does **not automatically cancel** a predeclared live-decay plan. It triggers a state recheck.

For example, a 1-0 state can still be eligible when the original two-sided/carrier thesis remains intact and the target burden now requires a plausible number of additional goals. However, the model must reassess route survival, remaining-goal requirement, and dominant failure mode before exposure.

No mechanical minute-only rule overrides football context. The model should be stricter as elapsed time increases or as the remaining-goal requirement becomes more demanding.

---

## 5. Opportunistic live bets remain quarantined

This patch does **not** open ordinary ad-hoc live betting.

If there was no predeclared live-decay plan before kickoff, an attractive live Over remains:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

unless the user explicitly grants a separate match-specific exception.

Thus:

`PREDECLARED LIVE DECAY != OPPORTUNISTIC LIVE BET`

---

## 6. Prematch price-only waits

A same-line price improvement can still occur before kickoff, but Football A must not build its normal execution plan around it.

If the line is already at supported burden but the price is below the hard floor, use:

`QUALIFIED — PRICE BELOW FLOOR`

The candidate may become directly executable if the same supported line later clears the floor before kickoff.

If the line itself is above burden, the normal label is now:

`QUALIFIED — LIVE DECAY PLAN`

not `WAIT FOR PREMATCH DECAY`.

---

## 7. Required persistence

For every predeclared live-decay candidate, persist:

- `Model Version = Football A`;
- Structural Rank;
- supported burden;
- prematch offered line/price;
- `Execution Plan = LIVE DECAY`;
- target line and minimum price;
- route/failure-mode cancellation triggers;
- first observed target-line timestamp/state;
- score and match minute when target first becomes available;
- actual target price;
- state-integrity result: `CLEAR / DAMAGED / NEW THESIS`;
- upper-tail state;
- priority-inversion state;
- final Exposure Decision.

Audit separately:

- predeclared live-decay official locks;
- predeclared plans that never reached target;
- target reached but state damaged;
- target reached and exposure suppressed by Model A;
- opportunistic live shadows.

---

## 8. Authority

This patch overrides earlier Football A / v0.2.55 wording only where those rules treated line-above-burden candidates as if the normal expectation were a prematch quarter-line decay or automatically quarantined every later live target.

All structural grading, A2 FOCUS guard, burden construction, price floor, upper-tail gate, priority-inversion guard, +0.25 acceptance quarantine, MCE quarantine, and settlement rules remain in force.
