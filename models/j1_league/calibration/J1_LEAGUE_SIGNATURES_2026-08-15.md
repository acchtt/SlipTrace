# J1 League Calibration Signatures — 2026-08-15

## Status

Calibration metadata for **J1 League v0.1**. This file does **not** change the active model version, create a predictive rule, or enable real-money betting.

The purpose is to record an auditable starting league signature before the independent J1 50-match calibration sample develops. These values are priors/context only and must yield to verified current J1 evidence as the child sample grows.

## Dataset boundary

- Primary reference population: completed **2025 J1 League** season.
- 2026/27 J1 observations are tracked separately because the new season has only just started.
- The 2026 J1 100 Year Vision League is a separate competition and must not silently enter this J1 calibration population.
- J2/J3, Emperor's Cup, J.League Cup, AFC, friendlies, reserve/youth and national-team matches remain contextual only under the existing child rules.

## Completed-2025 league baseline

Source: Opta data presented by BetExplorer, cross-checked against other season-stat aggregations.

| Signature | 2025 value |
|---|---:|
| Matches | 380 |
| Total goals | 911 |
| Goals per match | 2.40 |
| Home goals per match | 1.32 |
| Away goals per match | 1.08 |
| Home wins | 44% |
| Draws | 26% |
| Away wins | 30% |
| Over 2.5 | 45% |
| Under 2.5 | 55% |
| BTTS | ~47% |
| First-half goals per match | ~1.01 |
| Second-half goals per match | ~1.39 |
| Goals after 80' | ~21.8% |

## Provisional signature interpretation

These are descriptive starting signatures, not betting triggers:

1. **Home-field signature:** 2025 showed a meaningful home result/scoring edge: 44% home wins versus 30% away wins and 1.32 home goals versus 1.08 away goals per match.
2. **Totals signature:** the completed season was more Under-2.5 than Over-2.5 (55% vs 45%) at an overall 2.40 goals per match. This does not justify an automatic Under bias; closing total and team/match state must be priced independently.
3. **Draw signature:** draws represented about 26% of matches, material enough that DNB/+0.25 protection and one-goal-margin distributions must remain explicit rather than collapsing team strength into win probability.
4. **Second-half / late-goal signature:** available season summaries show more goals in the second half than the first and roughly one-fifth of goals after 80'. Late-game event budgets and stoppage-time risk should therefore remain explicit, but this is not yet a child-model calibrated hazard curve.
5. **Margin signature:** no league-wide deep-favorite or protected-underdog conclusion is recorded yet. Favorite one-goal versus 2+ margin behavior must be learned in the child dataset by handicap band.
6. **Context signature:** travel, summer heat/humidity, congestion and promoted-team effects remain hypotheses/modifiers requiring verified asymmetric context and child-sample evidence.

## 2026/27 structural regime note

The J.League moved to an August-to-May calendar from the 2026/27 season. The league officially scheduled the season to begin in early August 2026, pause in winter, and conclude in late May 2027.

The opening J1 round included unusually high-scoring headline matches, including Yokohama F. Marinos 3-4 Kashima Antlers and Gamba Osaka 4-3 Urawa Reds. These are **early observations only**. They do not overwrite the completed-2025 baseline and do not establish a new high-scoring league signature.

## Promoted-team context for 2026/27

Mito Hollyhock, V-Varen Nagasaki and JEF United Chiba entered the new J1 season from the 2025 J2 promotion cohort. Their J2 performance may inform personnel/team-strength context, but those matches are not part of the J1 calibration population.

## Model-use rules

- Never use one signature above as a standalone reason for a positive shadow verdict.
- Apply current team, lineup, venue, opponent-adjusted strength, tactical and market evidence first.
- Separate win probability from draw and margin probability.
- Treat xG/xGOT as secondary diagnostics.
- Record contradictory 2026/27 evidence rather than forcing it to fit the 2025 baseline.
- Update or supersede this signature record only through documented calibration review; do not rewrite the historical snapshot after seeing later outcomes.

## Review path

Use the existing `J1_50_MATCH_PROTOCOL.md` review points (approximately 10, 25 and 50 completed assessed J1 matches) to compare these starting signatures with the child-model sample. Early differences are diagnostic and do not by themselves justify a league-wide rule.

## Sources captured 2026-08-15

- J.League season timing transition: https://www.jleague.co/en/news/jleague-season-timing-to-transition-from-202627-season/
- J.League 2026/27 opening announcement: https://www.jleague.co/news/announcement-of-home-opening-fixtures-for-the-202627-meiji-yasuda-jleague/
- 2025 J1 statistics (Opta via BetExplorer): https://www.betexplorer.com/football/japan/j1-league-2025/stats/
- 2025 supplementary season statistics: https://www.bettingacademy.co.uk/stats/competition/japan/109
- 2025 supplementary period split: https://nofluffpicks.com/japan/j1-league/season/2025
- Reuters opening-week context: https://www.reuters.com/sports/soccer/week-asian-football-2026-08-10/
