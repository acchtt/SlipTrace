# Football Day-Ahead XI + Asian-Market Intake Gate — revision 2026-10-09

**Status:** ACTIVE prospective Step-0 operational admission evidence, with a **day-ahead expectation** rather than matchday confirmed-XI requirement.
**Policy marker:** `XI_MARKET_FIRST_V1` (compatible marker; October 9 revision fixes over-strict early confirmation).
**Engine:** `models/football/engine/sweep_intake_evidence.py` + `sweep_intake_evidence_cli.py`; `step0_handoff_cli.py` enforces it for new compact runs and explicitly marked unfinished legacy runs.
**Work-budget independence:** New `COMPACT_GOAL_ROUTE_V1` runs still use initial 8 / total 12 / refill-to-4. An unfinished legacy run opting into XI screening **retains** initial 15 / refill-to-10. C official, C2 shadow unchanged.

## 1. What Step 0 CAN and CANNOT know

A 24-hour `/sweep` happens long before most teams publish starting XIs. **Never require confirmed starters for the upcoming fixture at Step 0.** Asking for actual upcoming XI or a confirmed XI one day early incorrectly filters out good professional and protected matches. A known official lineup release window, provider lineup coverage, recent confirmed lineups, and/or credible federation/club squad news provide evidence that starting XI **will be obtainable** near kickoff.

Step 0 must decide **expected XI availability**, not the final starting eleven:
- `xi_expected=YES`: strong evidence of a starting-XI publication channel covering **both teams** (previously published actual XIs or reliable matchday lineup provider); **not** a statement that today's XI is already confirmed.
- `xi_expected=UNCERTAIN`: source-backed but weaker XI expectation; remains **conditional B** only. At least one side has a proven recent-XI/provider publication channel, while the other has credible current official squad coverage or an equivalent provider channel. An entire competition whose XI ecosystem is unavailable cannot use this B exception.
- `xi_expected=NO`: credible evidence shows lineup publication unavailable/nonoperational; exclude from normal Work as C/D after bounded preflight.

**Historical XIs** may be used as supporting evidence, but individual prior-match IDs and kickoff clocks are **not hard required** when a genuine provider lineup page covers the teams, or a B candidate's official squad/news channel is available. A historical lineup must not be misrepresented as the upcoming lineup.

A raw B with no source-backed publishing path is **not** routine Work-eligible. A raw B with `UNCERTAIN` and credible channels **may** enter the **conditional** Work queue; it cannot become routine FOLLOW until Step 2 resolves current XI and executable market.

## 2. Discovery versus actionable Work

`RAW SENIOR DISCOVERY → USER/HARD SCOPE FILTER → CHEAP COMPETITION SUPPORT CHECK → EXPECTED XI PUBLISHING CHANNEL + CURRENT ASIAN TOTAL + NEWS PREFLIGHT → FINAL A/B QUEUE → WORK → PRE-KICKOFF /xi RECHECK`

Retain all previously captured fixture identities and raw coverage for audit, including protected international/continental blocks, Netherlands Eerste Divisie and every visible women's domestic top flight. "Small", "obscure", "women's", "lower division" or low historical Over-rate alone do not reject a fixture. Only demonstrably absent execution channels or other hard scopes justify excluding it from routine Work.

Existing user country exclusions are unchanged: Israel, Kenya, Iraq, Wales and Kuwait **domestic** competitions, and **Germany 3. Liga only**. Their national-team and cross-border continental fixtures are not blanket-excluded.

## 3. Source-backed candidate fields — A and B

Every *new compact* A/B queue fixture, including capacity-deferred rows, must provide:
- `match_id`; `fixture_identity_verified=true`; zoned `fixture_kickoff_utc`; `preflight_complete=true`.
- `competition_support_tier`: one of `PROTECTED_OFFICIAL`, `VERIFIED_PROFESSIONAL`, `VERIFIED_WOMEN_TOP_FLIGHT`, `MAJOR_SENIOR_DOMESTIC_CUP`, `USER_EXCEPTION`. Also `competition_official_url` and specific `competition_support_reason`.
- `xi_expected`: `YES` or `UNCERTAIN`. For **each** side, `xi_home_channel_type` / `xi_away_channel_type` and `xi_home_channel_source_url` / `xi_away_channel_source_url`. Valid types: `RECENT_CONFIRMED_XI`, `PROVIDER_MATCHDAY_COVERAGE`, `OFFICIAL_SQUAD_NEWS`. The latter qualifies only for a **B/UNCERTAIN** expectation and **not both sides alone**; at least one side must be `RECENT_CONFIRMED_XI` or `PROVIDER_MATCHDAY_COVERAGE`. Include `xi_channel_basis`.
- `xi_recheck_due_utc`: zoned recheck time **30–180 minutes before kickoff**; typical recommendation **75 minutes before kickoff**. Step 1/2 subsequently replaces expectation with an actual current-XI state.
- Optional but encouraged `xi_home_recent_match_id`, `xi_away_recent_match_id`, `xi_home_recent_match_kickoff_utc`, `xi_away_recent_match_kickoff_utc` when authentic historical confirmed XIs are seen. Historical proof must predate kickoff if supplied.
- A current **fixture-specific Asian goal-total** with `market_observability=HIGH/MEDIUM`, `asian_total_market_match_id` matching canonical `match_id`, `asian_total_fixture_source_url`, timestamp `asian_total_market_observed_at_utc`, Asian quarter/half line `asian_total_market_line`, `asian_total_market_bookmaker`. The intake validator requires a non-stale quote up to 72 hours before KO, not a generic O2.5 leaderboard.
- `team_news_observability=HIGH/MEDIUM`, `team_news_source_url`, and full existing operational grade A/B, competition reliability, and cheap researchability evidence.

**Do not fabricate** XI source URLs, past XI matches, or market quotes to fill the schema. An official competition fixture page is not automatically proof that both teams have actual usable XI publication paths. One provider lineup page covering both sides may be used for both, with a reason.

## 4. Actions and states

| Step-0 evidence state | Routine disposition |
|---|---|
| Both XI channels credible and expected, current Asian total/news verified | A; eligible |
| One proven XI/provider channel, second has official squad/news, current market/news verified | Conditional B; eligible for Work but **RESERVE maximum until /xi** |
| Only squad lists, no proof any lineup channel publishes | C or `XI_CHANNEL_NO_PUBLISHING_PATH`; excluded after bounded check |
| No usable lineup ecosystem, XI explicitly NO | C/D; exclude |
| No current match-specific Asian-total bookmaker screen | Exclude or hold as `CURRENT_ASIAN_TOTAL_UNAVAILABLE`; no fabricated B |
| Data missing and cheap bounded preflight unfinished | `STEP0 PREFLIGHT INCOMPLETE — NO WORK`; do not claim a verdict |
| Unknown/unsupported competition, amateur/micro/unreliable fixture ID | Scope/operational exclude with actual reason |
| Explicit user exception | May reopen, **not** waive current executable-market /xi requirements for official action |

For domestic blocks with convincingly absent XI/market ecosystem, record a **source-grounded block-level closure** without repeatedly browsing; retain required protected and women top-flight fixture-level disposition/counts. Source-local hard exclusions and user-directed skips consume no external verification budget. At most two quick additional web queries per unfamiliar domestic competition/date block before declaring the channel unverified, unless a plausible A/B candidate warrants the usual bounded specific follow-up.

## 5. Mandatory day-of XI refresh

**Step 0 /sweep:** `XI_EXPECTED`, `XI_CONDITIONAL`, `XI_CHANNEL_UNAVAILABLE`; do not claim upcoming XI confirmed.

**Step 1 /rank:** common match evidence and independent C/C2, B cannot be routine FOLLOW at board time, schedule a /xi recheck. Do not skip tournament incentives or actual goal-route integrity.

**Step 2 /xi near KO:** check genuine confirmed starters and late absences against the expected XI channel, verify live executable Asian-total price, re-assess burden/route and C official + C2 shadow independently. If XI unavailable at check, follow existing XI integrity handling (wait/hold/exception), **not** invented starters or automatic confidence promotion.

## 6. Compatibility and tests

- New compact runs enforce this proof via their `COMPACT_GOAL_ROUTE_V1` budget ID; `strict_intake_policy=XI_MARKET_FIRST_V1` is also accepted as an explicit marker for legacy handoff currently **unfinished**.
- User-paused `SWEEP-20261009-1300-20261010-0300` at Chunk 12 stays **untouched**, including source hash, completed blocks, raw coverage/grades, current legacy budget. On an explicit resume, screen its still-unfrozen Work queue by this **expectation** gate; do not restart raw discovery and do not require upcoming confirmed lineups.
- Previously frozen/complete handoffs without the policy marker preserve historical behavior.
- `step0_handoff_cli.py` checks every A/B queue row, not only first-eight admitted fixtures. `sweep_intake_evidence_cli.py` separates ready/hold/excluded without deleting discovered records.
- Operational results alone never predict Overs: no league goals threshold, future results, or survivor-only evaluation enters Step-0 A/B ranks.

This revision corrects the over-strict confirmed-XI and both-teams-prior-XI requirements introduced earlier on 2026-10-09, without reopening the weak-data league intake problem.
