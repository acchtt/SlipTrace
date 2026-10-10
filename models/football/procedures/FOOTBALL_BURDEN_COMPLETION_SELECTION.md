# Football Burden-Completion Selection

**Status:** mandatory Football C Step-1 selection layer  
**Activation:** prospective only from the merge that activates this procedure  
**Purpose:** select matches by credible path to clearing the protected Asian total, not by cosmetic two-sidedness.

## 1. Core question

For every admitted fixture, after routes/carrier/incentive/H2H are researched and before C rank/lane assignment, answer:

> Where does the goal that clears the supported burden come from?

A match is not strong merely because both teams can score once.

Examples of weak completion logic:
- "both teams are capable of scoring";
- "BTTS is plausible";
- "both attacks are usable";
- "the favorite should dominate".

Those statements do not by themselves explain goal #3 for O2.5/O2.75 or goal #4 for O3.0.

## 2. Frozen completion fields

Persist before outcome and before market-price selection:

- `completion_mode = NONE / TWO_SIDED / CARRIER_LED / FORCED_CHAOS / MIXED`;
- `burden_completion_quality = LOW / MEDIUM / HIGH`;
- `continuation_quality = LOW / MEDIUM / HIGH`;
- `opponent_leakage = LOW / MEDIUM / HIGH`;
- `burden_stall_risk = LOW / MEDIUM / HIGH`.

These are football-evidence judgments. Market price may trigger reinspection but may not create HIGH completion/continuation.

### TWO_SIDED

Both teams have credible scoring routes and the combined mechanisms provide a realistic path beyond a single exchange of goals.

A plausible 1-1 is not enough for HIGH completion.

### CARRIER_LED

One side can plausibly self-fund most or all of the protected burden.

A weak opponent scoring route does not invalidate this lane when:
- carrier is STRONG;
- carrier_self_fund = true;
- independent_upper_tail = true;
- the opponent has material defensive leakage;
- current suppression does not attack the carrier.

This lane explicitly protects 3-0 / 4-0 / 4-1 type paths from being discarded merely because the weaker side is unlikely to score.

### FORCED_CHAOS

Verified match-state/tournament incentives create persistence beyond an initial scoreline: must-win, margin need, aggregate chase, simultaneous-result pressure or another football-grounded continuation mechanism.

Tournament cases remain subject to the full VERIFIED tournament-incentive gate. This mode never bypasses it.

### MIXED

More than one independent completion mechanism is genuinely active.

### NONE

No credible burden-completion mechanism survives.

## 3. Continuation quality

Continuation asks whether scoring is likely to persist after:
- 1-0;
- 0-1;
- 1-1;
- 2-0.

HIGH requires a football reason for further production, such as:
- repeatable carrier chance creation;
- structural defensive leakage;
- transition exposure after conceding;
- a forced chase;
- margin/tiebreak incentive;
- multiple independent high-value chance mechanisms.

Do not infer HIGH continuation from historical goal totals alone.

## 4. Burden stall risk

This is the explicit 0-0 / 1-1 / 2-0 trap assessment.

HIGH when the likely scoring story can plausibly stop below the protected burden despite attractive route labels, for example:
- two balanced sides each plausibly score once but neither has a multi-goal ceiling;
- carrier control produces 1-0/2-0 without enough continuation;
- draw utility or tactical parity compresses the second half;
- finishing/creation evidence supports one exchange but not another;
- transferable matchup evidence plus current football evidence supports compression.

HIGH stall risk blocks routine FOLLOW.

MEDIUM can be RESERVE if the rest of the completion structure is strong.

LOW means the frozen evidence contains a credible continuation path beyond the common stall scorelines.

## 5. Ranking order

Football C deterministic ranking is now burden-completion first:

1. burden-completion quality;
2. continuation quality;
3. lower stall risk;
4. self-funded independent upper-tail path;
5. carrier strength;
6. opponent leakage;
7. burden protection;
8. lower supported burden **only after completion quality is comparable**;
9. route reliability;
10. chance quality;
11. failure resistance;
12. evidence confidence;
13. XI robustness;
14. independent-route quality.

This intentionally removes independent-route quality from the top of the ranking stack.

Two-sidedness is one completion mode, not the preferred mode.

## 6. C-PASS carrier contradiction

A fixture may not remain normal C-PASS solely because one scoring route is WEAK when all of the following are frozen:

- completion mode CARRIER_LED / FORCED_CHAOS / MIXED;
- burden completion HIGH;
- continuation HIGH;
- STRONG carrier;
- at least one STRONG scoring route;
- carrier_self_fund = true;
- independent_upper_tail = true;
- opponent leakage MEDIUM/HIGH;
- stall risk is not HIGH;
- no route-attacking failure;
- no material suppression.

Such a row must be re-reviewed for at least WATCH/FOCUS. The deterministic adapter fails closed on this contradiction.

This is not automatic promotion to FOCUS or BET. It prevents weak-second-route logic from ending the assessment prematurely.

## 7. FOLLOW / RESERVE

Lane is a workload queue, not a second football-selection test.
All C-FOCUS fixtures qualify for operational allocation, including
supported totals above O3.0 and high stall-risk candidates.
A-grade FOCUS can FOLLOW within capacity; B-grade FOCUS can RESERVE.
Capacity overflow can become RESERVE or STOP. WATCH/PASS remain
outside routine Step 2. The original C grades and supported lines
remain frozen; Step 2 still applies all football, XI and quote gates.

## 8. Same-kickoff comparative selection

When multiple candidates share the exact scheduled kickoff minute, compare them against each other before consuming routine FOLLOW capacity.

The deterministic engine:
- calculates `same_kickoff_rank` from the burden-completion ranking key;
- allows at most **2 routine FOLLOW fixtures per exact kickoff minute**;
- demotes otherwise-qualified overflow to RESERVE when reserve capacity exists.

The comparison must prefer the cleaner burden-completion path. A higher supported line must not outrank a lower line merely because it has prettier two-sided route labels.

Global capacities remain:
- FOLLOW <= 6;
- RESERVE <= 4.

## 9. Step-2 recheck

Confirmed XI and fresh fixture-specific research must recheck:
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- stall risk.

A route-preserved XI does not automatically preserve continuation.

If completion/continuation degrades or stall risk becomes HIGH, the Step-1 FOLLOW state does not force a bet.

### Step-2 executable burden (prospective 2026-10-09)

After the current XI/research recheck, C-BET and countable C-WAIT
must pass `clearing_goal_funded` at the actual quote or supported WAIT
target. The rule also applies to user-authorized live exceptions.
O2.25 needs goal three for a full win (two goals means half-loss);
O2.0 instead pushes at two. O3.0+ requires fourth-goal proof.
Do not retroactively upgrade frozen completion grades from FT.

## 10. Audit

Post-slate audit must separate:

- C-PASS contradiction misses;
- FOCUS/STOP opportunity cost;
- same-kickoff priority inversion;
- two-sided stall failures (0-0 / 1-1 / 2-0 type);
- carrier-led clears;
- carrier-led failures where self-fund/upper-tail did not materialize.

Never assign or change the new fields retrospectively after seeing HT/FT.

Audit wording must preserve the exact frozen enum. For example:
- valid: `frozen continuation=HIGH; observed continuation did not materialize`;
- invalid: `continuation should have been MEDIUM`;
- invalid: `continuation was MEDIUM-HIGH`.

If only the result reveals the possible failure mechanism, label it `RETROSPECTIVE HYPOTHESIS ONLY` and test it prospectively on future boards.

Historical boards motivate this procedure but are not confirmatory samples.
