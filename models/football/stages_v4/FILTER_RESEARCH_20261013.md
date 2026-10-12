# Sweep cheap-filter research snapshot — 2026-10-13

**Purpose:** workload triage only. These observations do not create C/C2
predictions, do not authorize bets, and must not hard-exclude a valid fixture.

**Refresh boundary:** team-event priors in `cheap_sweep_filters.py` expire on
2026-11-13 UTC and fall back to `NEUTRAL_RESEARCH` until refreshed.

## Netherlands — Eerste Divisie 2026/27

Current sampled league environment (100/380 matches):
- 3.52 total goals per match;
- 67% Over 2.5;
- 67% BTTS;
- 46% Over 3.5.

Current high-event examples used only to prioritize missing-form research:
Heracles, VVV, FC Emmen, NAC Breda, Dordrecht and several Jong/vulnerable
defensive teams. The whole league is not auto-qualified: ordinary fixtures are
SECONDARY, while current high-event-team fixtures are PRIMARY.

Statistical source:
https://footystats.org/netherlands/eerste-divisie

Cross-check:
https://www.soccerway.com/netherlands/eerste-divisie/

## Japan — WE League 2026/27

Current early-season sample (19/132):
- 3.00 goals per match;
- 63% Over 2.5;
- 68% BTTS.

Because only 14% of the league season was complete at research time, the
competition receives a SECONDARY base priority rather than blanket PRIMARY.
NTV Beleza, INAC Kobe, Urawa and Nojima Stella currently receive a temporary
high-event research boost.

Official format/source:
https://weleague.jp/overview/league/

Statistical source:
https://footystats.org/japan/we-league

Official results cross-check:
https://data.weleague.jp/

## Japan — WE League Cup 2026/27

Current sample (35/48):
- 2.94 goals per match;
- 56% Over 2.5;
- 66% BTTS;
- 1-1 is the most frequent scoreline at 17.1%.

Therefore the cup is not blanket-promoted. Current attack/leak teams are
SECONDARY; otherwise the competition is DEFERRED with draw-trap caution.

Official format: 12 teams, eight league-stage matches per club, top six advance.
https://weleague.jp/kraciecup/2026-27/outline/

Statistical source:
https://footystats.org/japan/we-league-cup

Official results:
https://data.weleague.jp/

## Japan — Nadeshiko League 1 2026

Official format: 12 teams, double round robin, 22 rounds / 132 matches.

Current sample near season end:
- 56% Over 2.5 overall;
- Nittaidai current match environment about 3.80 goals/match;
- Shizuoka SSU Bonita about 3.35 goals/match.

The league is selective, not blanket Over-friendly. Those two currently known
event teams receive SECONDARY research priority; other fixtures default to
DEFERRED until match-specific goal evidence is obtained.

Official format:
https://www.nadeshikoleague.jp/2026/info_nadeshiko1.html

Statistical sources:
https://footystats.org/japan/nadeshiko-league-1
https://footystats.org/japan/nadeshiko-league-1/average-total-goals-table

## Japan — Nadeshiko League 2 2026

Official format: 12 teams, double round robin, 22 rounds / 132 matches.

Current sample (120/132):
- 2.27 goals per match;
- 41% Over 2.5;
- 40% BTTS;
- 0-0: 12.5%;
- 1-1: 8.3%;
- at least one clean sheet in 73% of sampled matches.

This is a strong workload-demotion prior. Fixtures remain in the ledger and may
still become goal-qualified with fresh source-backed match evidence, but missing
form is DEFERRED rather than consuming primary research capacity.

Official format:
https://www.nadeshikoleague.jp/2026/info_nadeshiko2.html

Statistical source:
https://footystats.org/japan/nadeshiko-league-2

## Japan — Empress's Cup

The 2026 competition runs 14 November 2026 to 1 January 2027 and mixes teams
from different levels in knockout football. Recent editions show both low-score
late-round ties and high-scoring mismatches/semifinals, so competition identity
alone is not a reliable Over prior.

All Empress's Cup fixtures use `SPECIAL_RESEARCH`: obtain round, team-tier and
current form context before deciding research priority. No blanket promotion.

Official competition:
https://www.jfa.jp/match/empressscup_2026/

2025/26 result cross-check:
https://www.flashscore.com/football/japan/empress-s-cup-women-2025-2026/
