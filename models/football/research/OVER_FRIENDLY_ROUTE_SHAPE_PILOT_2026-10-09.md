# Over-Friendly League Goal-Route Pilot — FT scoreline audit v0.1

**Research freeze:** 2026-10-09 ICT.  
**Authority:** RESEARCH ONLY. No change to production /sweep, Football C / C2, operational A/B/C/D, mandatory protected and women's coverage, 15-slot operational capacity, model predictions or odds.  
**Prior research:** [Over-Friendly League Watchlist](./OVER_FRIENDLY_LEAGUE_WATCHLIST_2026-10-09.md).  
**Data source:** [OpenFootball](https://github.com/openfootball), public-domain historical league match records. All figures below were computed from *per-match full-time scorelines*, not scraped league percentage summaries, and use denominator `FT matches actually present`.

## 1. Core results — latest verified complete source seasons

| League | Season | Confirmed FT / expected | O2.5 | BTTS | BTTS & O2.5 | Two-sided share **of Overs** | Over with clean sheet | 5+ goals (all FT) | 0-0 or 1-1 (all FT) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Germany Bundesliga | 2025/26 | **306 / 306** | 195 / 306 **63.7%** | 189 / 306 **61.8%** | 155 / 306 **50.7%** | **79.5%** (155 / 195) | **20.5%** (40 / 195) | **20.6%** (63 / 306) | **15.0%** (46 / 306) |
| Netherlands Eredivisie | 2024/25 | **306 / 306** | 169 / 306 **55.2%** | 170 / 306 **55.6%** | 130 / 306 **42.5%** | **76.9%** (130 / 169) | **23.1%** (39 / 169) | **19.3%** (59 / 306) | **17.0%** (52 / 306) |
| Switzerland Super League | 2024/25 | **228 / 228** | 126 / 228 **55.3%** | 139 / 228 **61.0%** | 105 / 228 **46.1%** | **83.3%** (105 / 126) | **16.7%** (21 / 126) | **20.2%** (46 / 228) | **19.3%** (44 / 228) |
| Iceland Úrvalsdeild | 2024 | **162 / 162** | 108 / 162 **66.7%** | 106 / 162 **65.4%** | 90 / 162 **55.6%** | **83.3%** (90 / 108) | **16.7%** (18 / 108) | **30.9%** (50 / 162) | **12.3%** (20 / 162) |
| Netherlands Eerste Divisie | 2023/24 | **380 / 380** | 229 / 380 **60.3%** | 229 / 380 **60.3%** | 186 / 380 **48.9%** | **81.2%** (186 / 229) | **18.8%** (43 / 229) | **21.3%** (81 / 380) | **17.1%** (65 / 380) |

**Terminology and denominator discipline:**
- `O2.5` = `home_goals + away_goals >= 3` (denominator all confirmed FT matches).
- `BTTS` = both teams scored ≥1 (all FT).
- `BTTS & O2.5` = match cleared both criteria (all FT); **this excludes 1–1**.
- `Two-sided share of Overs` = `(BTTS & O2.5) / O2.5`, not the probability that the teams will score in a future fixture.
- `Over with clean sheet` = `(O2.5 with one side scoring zero) / O2.5`. Thus `two-sided Over count + clean-sheet Over count = O2.5 count` for each season.
- `5+ goals` = total ≥5, **not the same as Over 3.5**.
- `0–0 or 1–1` = specific draw-trap scorelines, all FT; other low-total scorelines are not included.

### Raw goal-count bins (0 / 1 / 2 / 3 / 4 / 5+)

| League / season | 0 | 1 | 2 | 3 | 4 | 5+ | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bundesliga 2025/26 | 12 | 38 | 61 | 64 | 68 | 63 | **306** |
| Eredivisie 2024/25 | 12 | 46 | 79 | 67 | 43 | 59 | **306** |
| Swiss Super League 2024/25 | 10 | 31 | 61 | 46 | 34 | 46 | **228** |
| Iceland Úrvalsdeild 2024 | 4 | 18 | 32 | 28 | 30 | 50 | **162** |
| Eerste Divisie 2023/24 | 22 | 45 | 84 | 94 | 54 | 81 | **380** |

**Validation checks passed:** source FT count equals source fixture count and expected season count for each complete row; every goal-bin sum equals FT count; every O2.5 count equals `BTTS & O2.5 + clean-sheet Over`. Mixed JSON score shapes (`score: [h,a]` versus `score: {ft:[h,a]}`) were handled; Football.TXT FT `0-0` without a separate HT parenthesis was explicitly counted as a played 0–0, not discarded. Source fixture rows without an FT score were excluded from numerical analysis.

## 2. Sixth pilot league — **not representative enough to classify**

| League | File | Scored match records | Scheduled | Data coverage | Outcome |
|---|---|---:|---:|---:|---|
| Norway First Division / OBOS-ligaen | OpenFootball 2025 | **40** | **240** | **16.7%** | **FAIL-CLOSED — no season-wide route classification** |

The 2025 OpenFootball file contains 200 fixture listings without a final score. The 40 scored rows span an incomplete early-season subset. Their observed O2.5 (23/40) must **not** be used as a full-season estimate, as a stable over-friendly verdict, or to update Football C. The [Norwegian Football Federation official 2024 OBOS results](https://www.fotball.no/fotballdata/turnering/hjem/?fiksId=193220) and [RSSSF 2024 first division results](https://www.rsssf.no/2024/First.html) are potential complete independent alternatives, **not yet parsed into this report**. Source gap remains open.

## 3. Cross-season stability check

| Competition | Prior complete sample | Main sample | Later available sample | Lesson |
|---|---|---|---|---|
| Bundesliga | 2024/25 **183/306 = 59.8% O2.5** | 2025/26 **195/306 = 63.7%** | Not used | Both seasons above half, but the absolute rate changes ~4 percentage points |
| Eredivisie | 2023/24 **195/306 = 63.7% O2.5** | 2024/25 **169/306 = 55.2%** | 2025/26 **189/305 = 62.0%**; one match FT missing in chosen source | Material season-to-season drift: **do not assign permanent 76%+ over probabilities from a short 2026/27 sample** |

The 2025/26 Eredivisie file contains **305 scored FT for 306 listed fixtures**. Its 62.0% is a descriptive *305-match observed rate only*, not a claim the full season is verified at 100%. The original watchlist's early-2026/27 76% Eredivisie or 78% Swiss current-season snapshot cannot substitute for these verified historical match data.

## 4. Interpretation and limits

- **Iceland 2024:** Highest match-average goals in the full scored set (3.556), O2.5 66.7% and 5+ tail 30.9%. A higher 5+ fraction **may reflect heavy tails or frequent sustained goal production**; aggregate totals alone do not distinguish these mechanisms. Need team/opponent splits before using an `OUTLIER_TAIL` tag for a specific fixture.
- **Swiss 2024/25:** Just 55.3% O2.5, but 83.3% of Overs involved both teams scoring. **Joint BTTS+Over is evidence about historical scoreline shape only**, not a match's current XI or current Asian-total line.
- **Eredivisie 2024/25:** Among Overs, 23.1% had a clean sheet — highest share of these five main samples. This indicates a meaningful **one-sided-scoreline component**, not proof the next Eredivisie game will be a one-sided carrier.
- **Bundesliga 2025/26:** 20.5% of all results had 5+ goals? **No.** The correct fraction is 63/306 = 20.6%; the two-sided share **among O2.5** is 155/195 = 79.5%. Different denominators answer different questions.
- **Eerste 2023/24:** 60.3% O2.5 with 81.2% two-sided share of Overs, but 65/380 = 17.1% ended 0–0 or 1–1, so draw/low-total stall risk cannot be dismissed by the league label.

The interpretation `Over with a clean sheet` is only a scoreline-shape classifier. It **does not prove** a genuine xG chance creation mechanism, lineup strength, mismatch or market mispricing. O2.5 counts alone do not justify changing Step 0 selection or Football C/C2 burdens.

## 5. Frozen source manifest

Match scores originate from [OpenFootball JSON](https://github.com/openfootball/football.json) and [OpenFootball Europe TXT](https://github.com/openfootball/europe), both public-domain repos. The Git blob SHA locks the exact input bytes. Retrieval 2026-10-09 ICT.

| Source dataset | GitHub file | Blob SHA | FT / expected |
|---|---|---|---|
| Bundesliga 2025/26 | [`2025-26/de.1.json`](https://github.com/openfootball/football.json/blob/master/2025-26/de.1.json) | `320994ff4b376c0aa7abe7929f9b9740cfc0eff5` | 306/306 |
| Eredivisie 2024/25 | [`2024-25/nl.1.json`](https://github.com/openfootball/football.json/blob/master/2024-25/nl.1.json) | `668124659dac4fe9ab3a956a7b72b8b91b7c7bbb` | 306/306 |
| Swiss Super League 2024/25 | [`switzerland/2024-25_ch1.txt`](https://github.com/openfootball/europe/blob/master/switzerland/2024-25_ch1.txt) | `91b5af25584f3458420f5e57878415501c16409f` | 228/228 |
| OBOS-ligaen 2025 **partial** | [`norway/2025_no2.txt`](https://github.com/openfootball/europe/blob/master/norway/2025_no2.txt) | `fed0a0a9eddc79b7859c27203f7f039da6112518` | 40/240 |
| Iceland Úrvalsdeild 2024 | [`iceland/2024_is1.txt`](https://github.com/openfootball/europe/blob/master/iceland/2024_is1.txt) | `33b7e1e3645d9879be7528d1547300f9c848c738` | 162/162 |
| Eerste Divisie 2023/24 | [`netherlands/2023-24_nl2.txt`](https://github.com/openfootball/europe/blob/master/netherlands/2023-24_nl2.txt) | `627d40bb24c8b6df1df765436f3508386c3806e2` | 380/380 |

**Parsing contract:** For JSON take full-time `score.ft` or two-integer `score`; for TXT read fixture lines containing ` v ` with terminal `\d+-\d+` and optional half-time `(h-a)`. Restrict scores to non-negative integers; reject lines without FT. The team names and timestamps are retained only for data-context validation, never to make future FT forecasts. Require 100% fixture-score coverage before designating a league/season "complete"; a nominal header match count is not enough.

## 6. Follow-up research milestones — still **not production**

1. Obtain a **complete** OBOS 2024/2025 season from the Norwegian FA/RSSSF or independent licensed match-level provider; recompute all scoreline shape metrics; until then `INSUFFICIENT_SCORELINE_COVERAGE`.
2. Obtain more **comparable completed seasons** for Swiss, Iceland and Eerste from the same/independent data pipelines; explicitly distinguish regular vs playoff/championship splits where relevant.
3. For each league split home/away and *individual teams*, calculate pre-match rolling six/eight-match `BTTS & O2.5`, clean-sheet Over fraction and 0–0/1–1 trap share **using only previous matches**. Include source coverage and fixtures lacking current XI/news/market.
4. Compare **prospectively frozen** Football C and C2 Step-1 assessments on overlapping historical boards, using competition environment only as a **zero-weight diagnostic feature**; report whether it identifies false positives / 1–1–trap routes without selecting winners after the event.
5. Before **any** proposed production use, run explicit leakage QA, scoreline-formation evidence review, effective samples/uncertainty, model C/C2 divergence and operational market availability. No automatic changes.

### Runtime isolation / pause

`SWEEP-20261009-1300-20261010-0300` remains **user-paused, saved at Chunk 12 (Airtable status RUNNING), 3 pending**. Do not advance or edit it for these historical calculations. The current exclusion rule (Israel/Kenya/Iraq/Wales/Kuwait domestic competitions and **Germany 3. Liga only**) stays authoritative regardless of goal distributions.
