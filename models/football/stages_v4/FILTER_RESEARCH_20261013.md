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


## Netherlands — Eredivisie 2026/27

Current sample through 11 October: 72 matches, 3.74 goals per match, 72% Over
2.5, 61% Over 3.5 and 69% BTTS. That is strong enough for a SECONDARY league
base despite the season still being relatively young. Current extreme/event
teams such as PSV, Feyenoord, Ajax, Groningen, Excelsior, Go Ahead Eagles,
Utrecht and Sparta receive PRIMARY research priority; actual source-backed
fixture evidence remains required before GOAL_PRIORITY.

Current season source:
https://compactstats.com/league/ned-eredivisie/

Cross-check:
https://footystats.org/netherlands/eredivisie

Eerste Divisie remains stronger than the top division as a workload environment:
3.52 goals/match with 67% Over 2.5 and 67% BTTS after 100 matches.
https://www.statometrics.com/stats/netherlands/eerste-divisie?view=this

## Iceland — Besta deild karla 2026

The official KSÍ competition is Besta deild karla. Official standings after the
22-match regular phase show 74-49 for KR and 56-42 for Fram, confirming the
very open current environment seen in statistical aggregators.

League-wide current sample: about 3.87 goals per match, 71% Over 2.5 and 71%
BTTS. That merits SECONDARY by default; KR and Fram receive PRIMARY current
high-event priority.

Official competition / standings:
https://www.ksi.is/oll-mot/mot?banner-tab=overview&id=7025510

Statistical cross-check:
https://probettinghub.com/en-US/betting-stats/over-under/leagues/iceland/urvalsdeild
https://footystats.org/iceland/urvalsdeild/average-total-goals-table

## Iceland — Lengjudeild karla 2026

Official regular-season totals are strongly goal-positive: Afturelding 65-33,
Fylkir 49-36, HK 52-40 and Ægir 25-69 over 22 matches. Independent aggregate
tracking gives about 3.58 goals/match, 64% Over 2.5 and 61% BTTS.

Base priority is SECONDARY. Afturelding, Fylkir, HK and Ægir currently receive
PRIMARY. Because promotion play-offs are separately scheduled under the same
competition family, match-specific phase context remains mandatory.

Official table:
https://www.ksi.is/oll-mot/mot?id=7025540

Official promotion play-off:
https://www.ksi.is/oll-mot/mot?id=7025545

Aggregate cross-check:
https://matchpulsestats.com/en/league/165

Iceland 2. deild has a very high 2026 Over 2.5 rate (about 73%), but remains a
PILOT/DEFERRED workload lane because of lower-tier identity/data depth rather
than being promoted automatically.
https://footystats.org/iceland/2-deild/over-25-goals-table

## Faroe Islands — Meistaradeildin menn 2026

The Faroese federation renamed the former Betrideildin to Meistaradeildin for
2026. Current league aggregate is roughly 2.91 goals/match, 57% Over 2.5 and
58% BTTS: useful but not strong enough for blanket promotion.

Therefore the top flight is DEFERRED by default; HB Tórshavn, NSÍ Runavík and
EB/Streymur receive SECONDARY current event priority.

Official naming:
https://www.fsf.fo/fremstu-deildirnar-nytt-navn/

Current statistical cross-check:
https://compactstats.com/league/fro-meistaradeildin/
https://www.soccerstats.com/trends.asp?league=faroeislands

## Faroe Islands — 1. deild 2026

The second division is materially different: about 4.15 goals/match, 79% Over
2.5, 59% Over 3.5 and 66% BTTS. B36 Tórshavn II has been around 4.71 total
goals/match and FC Suðuroy around 4.42.

Base priority is SECONDARY, with B36 II / FC Suðuroy fixtures PRIMARY.
Because reserve sides are common, exact team identity remains mandatory.

Sources:
https://footystats.org/faroe-islands/1-deild
https://footystats.org/faroe-islands/1-deild/average-total-goals-table

## Norway — Eliteserien 2026

Current league environment: roughly 3.18 goals/match, 62% Over 2.5 and 59%
BTTS. This is positive but not strong enough for every Eliteserien match to
consume active research.

Base priority is DEFERRED. Viking, Bodø/Glimt, Molde, Brann and Aalesund are
current event-team overrides to SECONDARY. Examples: Viking has roughly 73%
Over 2.5, Bodø/Glimt 77%, Molde 68% and Brann 77%.

Sources:
https://compactstats.com/league/nor-eliteserien/
https://www.statometrics.com/stats/norway/eliteserien
https://footystats.org/norway/eliteserien/average-total-goals-table

## Norway — First Division / OBOS-ligaen 2026

This is one of the strongest researched workload environments: around 3.83
goals/match, 72% Over 2.5, 50% Over 3.5 and 65% BTTS.

The whole league receives SECONDARY. Ranheim, Haugesund, Kongsvinger and
Strømsgodset receive PRIMARY current event priority. Ranheim has been around
4.95 total goals/match and Haugesund around 4.77.

Sources:
https://footystats.org/norway/first-division
https://footystats.org/norway/first-division/average-total-goals-table
https://footystats.org/norway/first-division/over-25-goals-table

## Denmark — Superliga 2026/27

Current aggregate: about 3.0 goals/match, 53-54% Over 2.5 and 58-59% BTTS.
This is not a blanket research-positive league. FC Copenhagen and AC Horsens
are the clearest current event overrides; other fixtures stay DEFERRED unless
match-specific goal evidence is already present.

FC Copenhagen has been around 67% Over 2.5 / 67% Over 3.5, while AC Horsens
has been around 67% Over 2.5 and 78% BTTS.

Sources:
https://compactstats.com/league/den-superliga/
https://probettinghub.com/en-US/betting-stats/over-under/leagues/denmark/superliga

## Denmark — 1. Division 2026/27

Current league aggregate is only about 2.77-2.78 goals/match and 53-55% Over
2.5, while BTTS is around 62-63%. One source also reports a very high draw rate
around 38%. This is exactly the profile that can become a 1-1 trap if BTTS is
mistaken for strong total-goal continuation.

Base priority is DEFERRED with draw-trap caution. Hvidovre, Vejle, Hobro and
Esbjerg currently receive SECONDARY due materially stronger O2.5 environments.

Sources:
https://compactstats.com/league/den-1-division/
https://rachasports.com/en/liga/120
https://footystats.org/denmark/1st-division

## Sweden — Allsvenskan 2026

Current aggregate: 2.93 goals/match, 54% Over 2.5 and 53% BTTS. This is too
mixed for blanket promotion. Sirius (73% O2.5), Malmö (64%), AIK (64%) and
Brommapojkarna (73%) are the current event-team overrides to SECONDARY;
ordinary fixtures stay DEFERRED.

The league also contains strongly under-friendly profiles such as GAIS and
Halmstad at roughly 36% Over 2.5, reinforcing the selective treatment.

Sources:
https://www.statometrics.com/stats/sweden/allsvenskan
https://compactstats.com/league/swe-allsvenskan/

## Sweden — Superettan 2026

Current aggregate is roughly 2.89-2.90 goals/match, 56% Over 2.5 and 61% BTTS.
The division is selective rather than blanket goal-positive. Falkenberg,
Varberg, Östers, Brage and Helsingborg are current event-team overrides to
SECONDARY; ordinary fixtures stay DEFERRED.

Examples: Falkenberg and Varberg are around 68-69% Over 2.5; Brage has been
around 3.42 total goals/match and Helsingborg around 3.19.

Sources:
https://compactstats.com/league/swe-superettan/
https://footystats.org/sweden/superettan
https://footystats.org/sweden/superettan/average-total-goals-table
