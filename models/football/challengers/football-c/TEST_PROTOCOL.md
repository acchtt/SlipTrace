# Football C — Prospective A/B Test Protocol

**Champion:** Football A  
**Challenger:** Football C — SHADOW  
**Status:** frozen prospectively before first eligible Football C board result.

## 1. Initial run

Run Football C for the next **5 complete boards** created after the experiment-freeze commit.

This 5-board block is an **initial feasibility checkpoint**, not enough by itself for permanent promotion.

Do not edit C during the five boards.

After Board 5:
- report results;
- report operational workload;
- report paired A-vs-C decision differences;
- issue only `CONTINUE SHADOW`, `STOP/REJECT`, or `RESTART AS NEW CHALLENGER`.

Normal QA promotion thresholds remain authoritative.

## 2. Shared universe

A and C must start from the same AiScore fixture handoff/window.

C must independently screen and rank the common eligible universe. Do not feed A's ranks/grades into C.

If one model excludes a fixture for a football reason and the other keeps it, that difference is part of the experiment.

Shared hard scope/identity exclusions are not counted as model-selection differences.

## 3. Information clock

At each epoch both models may use only evidence available at that time.

For XI/odds comparisons:
- same confirmed-XI snapshot;
- same user-supplied current odds;
- same public information availability window.

C should be frozen before reading A's final action whenever practical.

If that cannot be guaranteed, mark:
`C CONTAMINATION RISK — EXCLUDE FROM CONFIRMATORY PAIRED DECISION METRIC`

The fixture may remain in operational notes but not in confirmatory action-delta results.

## 4. Exposure

Football A remains the only official production model.

Football C creates:
- `C-BET — SHADOW`;
- `C-WAIT — SHADOW`;
- `C-PASS`.

No C decision may create user exposure or a Website Pick during this test.

Actual user bets remain a separate execution-truth track.

## 5. Primary metric

Primary metric:

`FLAT-STAKE UNIT RETURN DELTA ON SETTLED A-vs-C EXPOSURE DIFFERENCES`

Use the exact contemporaneous line/odds each model selected.

A decision difference means:
- A BET / C no-bet;
- C BET / A no-bet;
- both bet but materially different line/burden or execution epoch.

Do not award value to a held match simply because FT would have cleared some unquoted hypothetical line.

## 6. Secondary metrics

Track:
- total common eligible fixtures;
- researched fixtures;
- A exposures;
- C shadow exposures;
- W/HW/P/HL/L;
- yield;
- max drawdown;
- average line/odds;
- direct vs WAIT;
- WAIT target reached;
- WAIT cancelled for thesis decay;
- false-positive/false-negative paired outcomes;
- rank monotonicity;
- time from raw handoff to board;
- time from XI/odds receipt to final action;
- number of separate model stages/tools needed;
- number of resumptions/retries;
- number of persistence corrections;
- number of verdict reversals before kickoff.

## 7. Operational guardrail

C is intended to be materially simpler.

For a complete board, its normal reasoning architecture is limited to:
1. one integrated screen/research/rank pass;
2. one XI/odds confirmation per serious candidate;
3. optional WAIT resolution only for a predeclared plan.

If C starts requiring separate internal sub-model stages comparable to Football A, record:
`FOOTBALL C SIMPLICITY GUARDRAIL FAIL`

## 8. Predeclared subgroup cuts

Report, without changing rules:
- C-FOCUS vs C-WATCH;
- two credible routes vs carrier-led;
- line <=2.5, 2.75–3.0, >=3.25;
- odds <1.65, 1.65–1.79, >=1.80;
- direct C-BET vs C-WAIT execution;
- market below C supported burden vs aligned vs above;
- H2H suppressive-corroborated vs non-suppressive;
- senior club vs senior international.

These are diagnostic cuts unless the frozen QA procedure says otherwise.

## 9. Discovery set — zero validation weight

The following motivated Football C and must not count as prospective proof:
- Belgium vs France;
- Central African Republic vs Burkina Faso;
- Armenia vs Montenegro;
- Sweden vs Poland;
- Zimbabwe vs DR Congo;
- Northern Ireland vs Hungary;
- historical v0.2.47-vs-Football-A direct/decay performance comparisons;
- prior workflow failures involving sweep latency, resumptions, H2H omission, post-XI research regression, or persistence mismatch.

## 10. Stop / invalidation conditions

Stop confirmatory counting if:
- C rules are edited after results begin;
- C reads FT/future evidence before freezing a decision;
- C directly copies A's rank/verdict;
- quote epoch cannot be reconstructed;
- fixture identity is unresolved;
- C creates official exposure;
- same-board selection is retrospectively changed after seeing results.

A changed C rule requires a new challenger ID and a new prospective window.

## 11. Evidence target

Initial checkpoint:
- 5 complete boards.

Existing governance target for meaningful shadow evidence:
- prefer >=40 eligible decisions;
- prefer >=20 settled exposure differences.

Five boards may reach that target, but if they do not, report the checkpoint without a promotion claim.

## 12. End-of-five-board report

Report:
- board-by-board A vs C summary;
- paired decision matrix;
- C shadow P/L and A official/model P/L on comparable epochs;
- direct vs WAIT results;
- missed-winner and avoided-loser counts using exact quoted lines only;
- processing/runtime burden;
- strongest failure case for C;
- strongest failure case for A;
- whether C should continue unchanged.

Do not promote Football C from the five-board checkpoint alone unless the standing QA governance requirements are independently satisfied.
