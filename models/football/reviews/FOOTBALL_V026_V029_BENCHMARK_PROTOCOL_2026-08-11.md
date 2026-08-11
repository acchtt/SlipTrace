# Football v0.2.6-v0.2.9 Benchmark Protocol — 2026-08-11

## Purpose

Test the hypothesis that SlipTrace's earlier football edge, if any, was concentrated in live goal totals with settlement protection rather than broad directional side selection.

This is a benchmark arm inside Football v0.2.42 AUDIT MODE. It is not a rollback and cannot produce official bets.

## Historical signal

The strongest explicitly version-tagged positive ledger results currently identified are:

- v0.2.6: Alajuelense vs Xelaju Under 1.75 @1.87 — full win, +0.2175u.
- v0.2.9: O'Higgins vs Boca Juniors Under 1.25 @1.85 — half win, +0.10625u.

The v0.2.7 sample itself was negative, so the benchmark must reconstruct the decision philosophy rather than assume every rule from v0.2.6-v0.2.9 was profitable.

## Historical philosophy to test

The benchmark retains only the generic concepts that characterized the early live-total workflow:

1. Start from the exact current score, minute and settlement line.
2. Treat remaining-goal count as a distribution, not a narrative about which team is better.
3. Explicitly price 0, 1, 2 and 3+ additional-goal branches when relevant.
4. Prefer quarter/whole-goal protection when it materially improves the most likely boundary settlement.
5. Reprice from zero after goals, red cards, penalty/VAR events, attacking substitution clusters or tactical regime changes.
6. Discount overlapping evidence channels; possession, raw shots and related chance metrics cannot be counted as independent proof.
7. In knockout matches, separate single-goal-to-level from true multi-goal chase states and price aggregate-reset risk.
8. Use adjacent total lines as a market-coherence check.
9. Deliver the decision before extended analysis and invalidate it on material state change.
10. NO BET is a valid benchmark output and must not be converted into a side merely because the total fails.

## What is deliberately excluded

The benchmark does not inherit the later model's tendency to solve every match through a directional handicap. It also does not recreate early overreliance on xG/xGOT. Under current audit rules, xG/xGOT remain secondary and may be discarded when unreliable.

No historical outcome may be used to tune a decision after the fact.

## Parallel shadow test

For every new live football decision point with a synchronized totals board, record two independent outputs:

### Arm A — Current audit model

Apply Football v0.2.42 plus all active validator and audit controls. Scan all market families. Directional markets remain quarantined.

### Arm B — Early totals benchmark

Evaluate only:

- full-match total goals;
- remaining-match total goals when settlement is explicit;
- team totals only when the data clearly supports a team-specific event rate.

Arm B may output one of:

- `BENCHMARK SHADOW — OVER [line] @ [odds]`;
- `BENCHMARK SHADOW — UNDER [line] @ [odds]`;
- `BENCHMARK NO BET`.

No Arm B output is executable.

## Mandatory fields for Arm B

Capture at decision time:

- match, competition and format;
- score and minute;
- exact settlement scope;
- available adjacent totals and odds;
- reliable shots/SOT/box access/set-piece/transition evidence;
- cards and substitutions;
- regulation-win/draw/qualification utility where relevant;
- remaining-goal branch assessment;
- boundary settlement table for the chosen line;
- primary invalidation event;
- final result and simulated P/L after settlement.

## Selection gate

A benchmark total can be shadow-selected only when all are true:

1. The exact line and odds are visible and at least 1.70.
2. Settlement scope is verified.
3. At least two reliable forward-looking evidence channels support the same goal-environment direction.
4. No unresolved state-change reset is active.
5. The chosen line is preferable to its adjacent alternatives after settlement protection is considered.
6. The thesis survives an explicit adverse branch: early goal for an Under, or a 10-15 minute scoreless interval for an Over.
7. The candidate remains preferable to NO BET after clock decay and uncertainty.

## Anti-under-bias control

The early positive examples were Unders, but this protocol must not become an Under-only system.

At every checkpoint, evaluate both Over and Under. If neither side of the totals market has a demonstrable edge, output `BENCHMARK NO BET`.

A quiet historical interval is not sufficient evidence for an Under. A high shot count is not sufficient evidence for an Over.

## Comparison metrics

Track separately for Arm A and Arm B:

- number of assessed checkpoints;
- number of shadow selections;
- full win / half win / push / half loss / full loss;
- net units;
- ROI on simulated stake;
- average odds;
- Over versus Under split;
- prematch versus live split;
- league/competition type;
- line family: whole, quarter, half;
- process-valid versus process-invalid result;
- closing-line movement when available.

Also track `NO BET` frequency. A higher pass rate is not inherently better.

## Minimum evaluation sample

Do not declare this benchmark superior from a handful of outcomes.

First review at:

- 20 synchronized live decision points;
- at least 10 Arm B shadow selections if the gate naturally produces that many;
- at least 5 Over-eligible and 5 Under-eligible states, whether selected or passed.

Promotion consideration requires at least 30 settled Arm B shadows or a later explicitly approved threshold. Until then this is exploratory calibration only.

## Decision rule after review

Possible conclusions are:

- early totals philosophy shows no edge -> retire the benchmark;
- totals outperform sides but remain negative -> keep official betting paused and simplify further;
- a specific totals subfamily is positive with process validity -> continue targeted shadow validation;
- robust positive results across a sufficient sample -> propose a simplified next model version for user approval.

Historical v0.2.6 or v0.2.9 will not be restored wholesale. Any future model must retain modern synchronization, provider-quality, settlement and audit controls.