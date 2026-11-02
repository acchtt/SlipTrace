# 2026-11-02 Completed Current-Repair Replay — Recent 44

## Scope

Completed same-information replay of the exact frozen 44-match Decision States cohort.

- Production base: `cd2d51bcf2fa426d6af8eb9797f40502e2cd02dc`
- Audit branch: `audit/replay-44-current-repair-20261102`
- Complete replay commit: `cebb9de1538da0047ecd04142df27c94ee439670`
- GitHub Actions run: `41408622965` — SUCCESS
- Fixtures: **44**
- Outcomes excluded until after final board compilation.

## Research completion

- G3 borderline second passes completed: **6**
- Block comparisons completed: **10**
- Block-comparison candidates: **42**
- Remaining selection checkpoints: **0**
- Remaining block checkpoints: **0**

The six borderline WATCH rows remained REVIEW_ONLY after the bounded second pass.
Their frozen evidence did not justify a result-blind upgrade to HIGH
completion/continuation/leakage or self-funded carrier strength.

## Final board

- FOCUS: **29**
- WATCH: **15**
- FOLLOW: **8**
- RESERVE: **4**
- FOCUS_UNFOLLOWED: **17**
- STOP: **15**

### FOLLOW 8

| Rank | Fixture | FT | 3+ | 4+ |
|---:|---|---:|:---:|:---:|
| 1 | Bayern Munich–Borussia Dortmund | 2–2 | YES | YES |
| 2 | SC Heerenveen–NEC Nijmegen | 1–0 | NO | NO |
| 3 | Selangor–Star City | 1–0 | NO | NO |
| 4 | Young Boys–FC Zürich | 3–5 | YES | YES |
| 5 | Piratas–Tapatío | 1–1 | NO | NO |
| 6 | Kashima Antlers–Cerezo Osaka | 4–1 | YES | YES |
| 7 | CF América–Toluca | 2–2 | YES | YES |
| 8 | Mito Hollyhock–Sanfrecce Hiroshima | 0–3 | YES | NO |

FOLLOW:
- 3+ = **5/8 (62.5%)**
- 4+ = **4/8 (50.0%)**
- Mean goals = **3.50**

## Lane performance

| Lane | Count | 3+ | 4+ | Mean goals |
|---|---:|---:|---:|---:|
| FOLLOW | 8 | 5/8 = 62.5% | 4/8 = 50.0% | 3.50 |
| RESERVE | 4 | 3/4 = 75.0% | 1/4 = 25.0% | 2.75 |
| FOCUS_UNFOLLOWED | 17 | 9/17 = 52.9% | 7/17 = 41.2% | 3.06 |
| STOP | 15 | **13/15 = 86.7%** | **8/15 = 53.3%** | **4.00** |

## State performance

| State | Count | 3+ | 4+ | Mean goals |
|---|---:|---:|---:|---:|
| FOCUS | 29 | **17/29 = 58.6%** | 12/29 = 41.4% | 3.14 |
| WATCH | 15 | **13/15 = 86.7%** | 8/15 = 53.3% | **4.00** |

The selection boundary is inverted on this cohort. WATCH beats FOCUS by
**28.1 percentage points at 3+** and also beats it at 4+ and mean goals.

## Borderline second-pass result

All six rows intercepted by `G3_BORDERLINE_DISCRIMINATION_V2` remained WATCH:

- Alacranes de Durango–Atlético Morelia — 3–1
- Monterrey–Tijuana — 3–3
- Colorado Rapids–Chicago Fire — 2–4
- Cheongju FC–Paju Citizens — 1–2
- Persib Bandung–Isenmulang Kalteng — 4–0
- Portland Timbers–Houston Dynamo — 2–1

Outcome overlay:
- 3+ = **6/6**
- 4+ = **4/6**

This demonstrates that the new checkpoint detects the false-negative class but
does not repair the qualification rule that keeps those rows outside FOCUS.

## Other major false negatives

WATCH/STOP 3+ hits also include:

- Sanfrecce Hiroshima Regina W–Vegalta Sendai W — 1–2
- PSIM Yogyakarta–Borneo — 2–1
- Chungnam Asan–Gimpo — 5–1
- FC Anyang–Bucheon — 2–1
- Guadalajara–Atlante — 4–2
- Arema–Bali United — 1–3
- Persik Kediri–Persita — 1–5

Therefore the false-negative problem is broader than the six borderline rows.

## Conclusion

The research-completeness repair is operationally successful but predictively
insufficient.

It successfully prevents generic MEDIUM cards from passing without a second
look and forces equal-depth block comparison, but after those contracts are
actually completed the unchanged G3 qualification compiler recreates essentially
the same bad selection boundary.

This cohort shows:

- WATCH 3+: **86.7%**
- FOCUS 3+: **58.6%**
- FOLLOW 3+: **62.5%**
- STOP 3+: **86.7%**

The next repair must therefore target the **G3 qualification boundary / evidence
to certificate mapping**, not add more checkpointing, ranking keys or block
comparison prose. The strongest candidate for investigation is the rule that
requires either HIGH completion+continuation or the frozen distributed Step-0
threshold even when current source-backed strong-primary + usable-reply
mechanisms are independently present.
