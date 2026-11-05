# Football C — Downward Market Disagreement Blind Spot

Date: 2026-11-05 ICT
Status: CONFIRMED CODE DEFECT
Scope: /xi observed screenshot market-disagreement gate

## Trigger case

Sao Paulo–Corinthians, frozen prematch /xi:
- Football C certified burden after confirmed XI: O2.50.
- User screenshot line evaluated as prematch: O1.75 @ 1.80.
- Gap = -0.75 goals versus Football C.
- Current model action: ACT, because the visible line was below the direct ceiling and price exceeded the normal floor.

At halftime the match remained 0-0. The halftime state is post-decision evidence and is not used to retroactively alter the prematch verdict, but it makes the prospective pre-match market disagreement worth auditing.

## Code defect

adapter._market_disagreement_recheck_gate currently defines material disagreement only when:

observed_line >= compiled_burden + MATERIAL_MARKET_DISAGREEMENT_GOALS

Therefore:
- Market 0.50+ ABOVE Football C -> mandatory football recheck.
- Market 0.50+ BELOW Football C -> no mandatory recheck.

This asymmetry means a materially lower market line is treated only as a safer burden, even when the lower line may indicate that Football C is overestimating the goal environment.

For Sao Paulo–Corinthians:
- compiled_burden = 2.50
- observed_line = 1.75
- observed_line - compiled_burden = -0.75
- material_gap = false under the current implementation

The price policy then sees O1.75 as below the supported burden and can return ACT without a dedicated downward-disagreement football review.

## Why this matters

This is consistent with repeated user-flagged cases where the market burden was materially below Football C's supported burden before a low-total or control-heavy outcome.

A lower bookmaker burden must not automatically veto Football C, and market information must never create or erase a football certificate by itself. However, a large negative gap should trigger a football-only recheck for:
- route overstatement,
- lineup/role downgrades,
- first-leg/draw utility,
- control/stall risk,
- missing/suppressive H2H or current-context evidence,
- carrier transferability,
- burden-completion and continuation grades.

## Required repair direction

Make material market disagreement symmetric for RECHECK TRIGGERING ONLY:

abs(observed_line - compiled_burden) >= MATERIAL_MARKET_DISAGREEMENT_GOALS

Then preserve direction:
- UPWARD_GAP: market burden materially above Football C.
- DOWNWARD_GAP: market burden materially below Football C.

The market remains diagnostic only:
- no automatic downgrade,
- no automatic certificate promotion,
- no price-derived football grade,
- no retrospective outcome use.

For DOWNWARD_GAP, require a completed football recheck before ACT/BOOK/PASS, with emphasis on:
- route reliability,
- chance quality,
- burden completion,
- continuation,
- stall risk,
- failure resistance,
- lineup quality,
- tournament/aggregate incentive,
- upper-tail transferability when relevant.

## Positive control

Botafogo–Atletico-MG remained no-G3 / PASS after confirmed rotations. At 1-0 HT, the low-endpoint path remained consistent with the prematch suppression read. This is not proof of final correctness, but it shows the issue is not simply "market lower = always right."

## Audit classification

defect_class:
- MARKET_DISAGREEMENT_ASYMMETRY
- FALSE_POSITIVE_RISK

severity: HIGH

implementation_requested: false
