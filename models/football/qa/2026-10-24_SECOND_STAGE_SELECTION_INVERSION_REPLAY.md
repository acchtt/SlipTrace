# Football C — Second-stage selection-inversion replay

**Date:** 2026-10-24 ICT  
**Current production HEAD under test:** `1ed0a5354bf677b94f1144fa44b75c85781f5052`  
**Replay type:** frozen same-information rank/execution-capability replay + separate settled-outcome audit  
**Outcome authority:** audit only; no outcome field entered the replay ranking calculation.

## Cohort

Ten retained sealed rank packages were replayed:

- 2026-10-19 daytime
- 2026-10-19 night
- 2026-10-20 morning
- 2026-10-20 night
- 2026-10-21 night
- 2026-10-22 daytime
- 2026-10-23 daytime
- 2026-10-23 night
- 2026-10-24 07:26–12:00
- 2026-10-24 10:46–12:00

Total: **10 boards / 89 fixture-epochs / 50 compiled FOCUS fixture-epochs**.

Baseline is the immediately previous first-repair policy: evidence confidence could
supply the HIGH dimension in robustness, distributed-only G3 retained the funded
O2.50 execution floor when ordinary floor checks cleared, and rank was
robustness/certificate-first.

Challenger is current second-stage policy at the HEAD above: evidence confidence
removed as predictive HIGH, broad-MEDIUM distributed-only G3 denied the execution
floor, and champion rank changed to execution-floor -> mechanism strength ->
clearability -> robustness -> depth.

## Aggregate replay

| Metric | First-repair baseline | Second-stage repair |
|---|---:|---:|
| Boards | 10 | 10 |
| Fixture-epochs | 89 | 89 |
| Compiled FOCUS | 50 | 50 |
| ACT-capable FOCUS | 46 | 28 |
| ACT-capable share of FOCUS | 92.0% | 56.0% |
| ACT-capable rows removed | — | 18 |
| ACT-capable rows added | — | 0 |

Ranking movement:

- 39 / 89 total rows moved;
- 37 / 50 FOCUS rows moved;
- mean absolute FOCUS movement: 1.68 places;
- maximum FOCUS movement: 7 places.

## 10:46–12:00 control board

The ranking component behaves as intended on the latest false-positive control:

| New rank | Old rank | Match | Mechanism | Old direct ceiling | New direct ceiling |
|---:|---:|---|---|---:|---:|
| 1 | 3 | Sanfrecce Hiroshima–Shimizu S-Pulse | CARRIER | O2.50 | O2.50 |
| 2 | 4 | Jeonnam Dragons–Daegu FC | CARRIER | O2.50 | O2.50 |
| 3 | 1 | Mynavi Sendai–Nojima Stella | DISTRIBUTED | O2.50 | none |
| 4 | 2 | Urawa–INAC Kobe | DISTRIBUTED | O2.50 | none |

Settled outcomes:
- Sanfrecce–Shimizu: 4–0;
- Jeonnam–Daegu: 2–4;
- Mynavi–Nojima: 0–0;
- Urawa–INAC: 2–0.

Therefore the **ranking mechanism/clearability change passes this local control**:
the two carrier rows rise to #1/#2 and both clear O2.50, while the two old #1/#2
distributed rows fail O2.50.

## Critical failure — distributed execution veto collapses useful coverage

All 18 rows that lose ACT capability are distributed-only G3 rows.

Settled O2.50 outcome audit:

| Match | FT | O2.50 |
|---|---:|---|
| Tai Po–Southern District | 4–2 | WIN |
| Talinna Kalev–FCI Levadia U21 | 1–2 | WIN |
| Fram Reykjavik–IA Akranes | 2–4 | WIN |
| Jong Ajax–De Graafschap | 2–1 | WIN |
| Antigua Guatemala–Xelaju | 3–0 | WIN |
| Sogndal–Raufoss | 2–1 | WIN |
| HAGL–Song Lam Nghe An | 0–2 | LOSS |
| Sokol Kleczew–Slask Wroclaw II | 4–2 | WIN |
| Adelaide City–APIA Leichhardt | 1–3 | WIN |
| Jong AZ–Helmond Sport | 5–4 | WIN |
| Stuttgart–M'gladbach | 2–3 | WIN |
| Go Ahead Eagles–Telstar | 3–2 | WIN |
| FC Volendam–Jong Utrecht | 6–2 | WIN |
| Vitesse–FC Emmen | 0–2 | LOSS |
| TOP Oss–Jong Ajax | 3–3 | WIN |
| Bolton–Middlesbrough | 1–5 | WIN |
| Urawa–INAC Kobe | 2–0 | LOSS |
| Mynavi Sendai–Nojima Stella | 0–0 | LOSS |

**Removed cohort: 14 / 18 O2.50 wins = 77.8%; 4 / 18 losses = 22.2%.**

This fails the repair acceptance criterion. The execution veto fixes the latest
two false positives only by suppressing a much larger set of historically useful
distributed-G3 opportunities.

The frozen feature table also shows no clean prospective discriminator among
this broad-MEDIUM distributed cohort: all share MEDIUM reliability/chance/
completion/failure/protection shapes, while the losing Urawa row had one of the
strongest historical goal-rate signals. A new score threshold would therefore
be hindsight fitting rather than a demonstrated discriminator.

## Decision

**SECOND-STAGE REPAIR: PARTIAL / FAILED PROMOTION GATE**

Keep under consideration:
- evidence confidence must remain sourcing quality rather than predictive HIGH;
- mechanism/clearability-first ranking materially improves the latest 10:46
  control;
- entry-feasibility and PHANTOM_FLOOR diagnostics are useful;
- unreachable manufactured BOOK targets should remain blocked.

Do **not** treat as validated:
- blanket rule that a distributed-only G3 requires a genuinely HIGH predictive
  dimension to retain the O2.50 execution floor.

The blanket distributed execution veto should be revised or rolled back before
the current HEAD is considered a validated selection-inversion repair.

No threshold should be tuned from the settled scores above. The correct next
step is to preserve ranking demotion while finding a prospective discriminator
that does not erase the 14/18 winning distributed controls.
