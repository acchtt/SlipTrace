# Poland Ekstraklasa selective conditional intake — evidence baseline
**Created:** 2026-10-11 ICT
**Status:** source-linked RESEARCH SUPPORT for prospective new /sweep scope. Not preverified run evidence, executable odds, C/C2 predictions, or official bets.

## Why a targeted scan?
The Oct 10 completed-match CompactStats 2026/27 Ekstraklasa snapshot reports 83 finished games, 3.01 total goals/game, 63% Over 2.5, 33% Over 3.5 and 66% BTTS.
- https://compactstats.com/league/pol-ekstraklasa/
- https://footystats.org/poland/ekstraklasa/over-25-goals-table
- https://ekstraklasa.org/en/ (official fixture/identity source)
Other same-season provider samples contain 80 vs 83 FT, so avoid mixing denominators. Sample O2.5 rate is *not* an actionable Over 2.5 probability or an Asian handicap-burden proof. It can disguise 1–1/0–0 fixtures, 3–0 single-side goals and defensive leakage.

High-O2.5 candidate teams for source-driven later review: Raków 9/10 (historically large concessions), GKS Katowice 8/9, Lech Poznań 7/9. Negative controls Korona Kielce 3/9 and Pogoń Szczecin 3/8. Do NOT use fixed team names to pass or exclude a fixture; always validate both teams' last five completed competitive scorelines on the actual observation date.

## Source publication channels — feasibility, not certification
- **Official competition fixture identity and kickoff:** https://ekstraklasa.org/en/ . Verify provider time zone independently and preserve the exact immutable AiScore match ID when present.
- **Named starting lineup publication:** https://www.gkskatowice.eu/game/3196-gks-katowice-rakow-czestochowa_2026-10-09 ; the Oct 9 Raków 1–4 GKS Katowice club match-center identifies named starters for *both* sides. Another lineup-provider discovery surface: https://www.sportsgambler.com/lineups/football/poland-ekstraklasa/ , separating predicted from confirmed lineup lists.
- **League fixtures/lineup source surface:** https://www.soccerway.com/poland/ekstraklasa/fixtures/ ; this index is not itself proof that XI was actually published for two different games.
- **Bookmaker over/under / Asian menu possibilities:** https://www.soccerpunter.com/football/Poland-Ekstraklasa/453/ and https://www.infobetting.com/calcio/quote/polonia/ekstraklasa/rakow-czestochowa_katowice/dett-t-40-1-q-20-341-1404594.htm . These show market-menu/publisher availability but the research snapshot has **NOT independently confirmed two separate senior fixture Asian goal-total quote records with bookmaker ID and observation UTC**. Do not mark 2026/27 `PROVEN_LEAGUE` already passed merely by reading these generic links. Fresh /sweep must prove two real lineup publishing fixtures and two real Asian-total publishing fixtures; otherwise keep operational A/B excluded.

## Implemented future-sweep scope
Ekstraklasa remains source-local CONDITIONAL (Poland only). One pass over the directly available in-window listing/cached competition locator, no broad country recrawl. The per-fixture `poland_ekstraklasa_recent_goal_evidence` object needs `captured_at_utc`, and each `home`/ `away` needs `source_url`, `recent_competitive_matches` of exactly five entries. Each entry has `match_id`, `kickoff_utc`, `goals_for`, `goals_against`, `competitive: true`. All must be finished by capture, within 120d before the upcoming KO; capture is within 7d prior KO. Missing/fabricated data fails closed (not an Under prediction).

Admission requires both sides recent average total goals >=2.8 OR one side >=3.2 and other >=2.6 OR both >=3 of five >2.5 total goals. If either team has >=3 last-five 0–0/1–1 draws OR >=4 <=2-total-goal matches, reject its conditional intake regardless of the opponent's large total-goal streak. The same current fixture must additionally pass A/B operational viability, PROVEN_LEAGUE proof, news and market channels, fixture ID/UTC/KO integrity and near-KO XI recheck. No old/missing team source or unknown country can be filled with the snapshot's 63% average.

At Step1/Step2, actual match-specific bookmaker Asian goal totals, quote timestamps, XI/news and C official/C2 shadow assessments remain independent. Never alter prior frozen source hashes, ranks, boards, excluded domestic regions, friendlies, women's top-flight or protected continental fixtures. No admission based on retrospectively known Over or FT scorelines.
