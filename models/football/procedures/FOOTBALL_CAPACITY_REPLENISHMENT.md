# Football Capacity Replenishment

**Status:** ACTIVE OPERATIONAL CAPACITY CONTROL  
**Applies to:** Step 0 -> Step 1 `/rank`  
**Predictive authority:** none

## Purpose

Prevent the 15-fixture Step-0 workload cap from becoming a permanent slate cutoff when the first research wave produces many C-PASS/STOP/invalid fixtures.

The 15 limit controls **concurrent deep-research workload**, not how many A/B candidates may ever reach Step 1.

## 1. Freeze the full A/B queue first

Before selecting the first Work batch:

1. enumerate every fixture that plausibly clears Step-0 operational grade A/B;
2. freeze operational grade, XI expectation, market observability, team-news observability, researchability and competition class;
3. assign a unique positive `Step0 Capacity Queue Rank` over the full A/B pool.

Queue order is operational only:
1. A before B;
2. XI YES before UNCERTAIN;
3. market HIGH before MEDIUM;
4. team-news HIGH before MEDIUM;
5. protected/required/major senior competition class as an otherwise-equal tie-break;
6. canonical match identity.

Source order, kickoff discovery order and model attractiveness are forbidden queue inputs.

## 2. Initial wave

- ranks 1–15: initial Work wave;
- ranks 16+: `OPERATIONAL_CAPACITY_DEFERRED`.

Deferred means **queued**, not rejected.

## 3. Replenishment trigger

After each completed Step-1 wave, calculate:

`active_lane_count = FOLLOW + RESERVE`

Lane caps remain:
- FOLLOW <= 6;
- RESERVE <= 4;
- combined active lanes <= 10.

If active lanes are below 10 and deferred prematch A/B candidates remain, replenishment is mandatory.

Prospective quarantine/HOLD rows such as `INCENTIVE-INCOMPLETE` have no lane and therefore consume zero active-lane capacity. They do not suppress replenishment.

## 4. Next wave

Read deferred rows in ascending immutable queue rank.

Skip rows only when:
- fixture has already started;
- fixture was postponed/cancelled/finished;
- identity/time became invalid;
- a genuine Step-0 operational fact changed so it no longer qualifies A/B.

Serialize the current state and run:

`python models/football/engine/capacity_replenishment_cli.py --input <capacity_replenishment.json>`

The selector validates unique queue ranks and returns the next wave strictly in ascending queue order.

Pull at most:

`10 - active_lane_count`

into the next wave.

Persist:
- `Step1 Replenished = true`;
- `Replenishment Wave = N`;
- `Replenishment Reason = ACTIVE LANE CAPACITY UNDERFILLED`.

Run the complete Step-1 process for those fixtures, including the C official + C2 shadow board pair and deterministic validation.

Then recompute official C rank/lane allocation across all assessed fixtures still in the prematch window.

Repeat if active lanes are still under 10.

## 5. Stop conditions

Stop replenishing only when:
- FOLLOW + RESERVE = 10; or
- no deferred prematch A/B candidate remains.

A board is allowed to finish below 10 active lanes when the queue is exhausted or every remaining fixture left prematch.

If the ranked eligible universe is empty because all admitted candidates were legitimately quarantined/closed and the deferred queue is exhausted, this is a valid completed empty board, not a blocked board.

This does not require the model to manufacture selections.

## 6. No cherry-picking

Never choose a replenishment candidate because:
- it looks more likely to go Over;
- C/C2 would probably like it;
- odds look attractive;
- another result was good/bad;
- it is in a preferred league.

The next candidate is always the lowest remaining Step0 queue rank.

## 7. Historical board rule

Do not retroactively rewrite a frozen historical board merely because this rule was added later.

A still-open current sweep may be replenished prospectively only when a complete Step-0 queue already exists in the attached/persisted handoff. /rank must never reconstruct or repair the Step-0 queue itself. If the queue is incomplete, return to `/sweep repair`.
