# Football League Environment Registry

**Status:** ACTIVE  
**Purpose:** Reduce Work usage by deciding league-level admission before deep structural research.  
**Scope:** Senior domestic national leagues only.  
**Fixture authority:** AiScore only  
**Timezone:** source timezone preserved at Step 0; ICT conversion later for scheduling

This registry is an operational cost-control layer. It does **not** decide bets and does **not** replace match-level structural research for fixtures that reach Work.

The goal is simple:

`AISCORE RAW UNIVERSE -> QUALITY/SCOPE EXCLUSION -> CHEAP LEAGUE ADMISSION -> SMALLER ACTIONABLE HANDOFF -> WORK DEEP RESEARCH`

Work should spend tokens on plausible Over environments, not on repeatedly proving that low-value domestic leagues are PASS.

---

## 1. Admission prerequisite — quality/scope first

A competition must first survive the active senior-quality overlay before this registry can classify it as PRIORITY, NORMAL, or CONDITIONAL.

Exclude **before any conditional cheap gate**:

- youth/Uxx, academy and junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial competitions;
- domestic lower divisions unless explicitly approved;
- very small/obscure weak-data senior leagues or competitions;
- any competition whose data environment is too weak to support reliable cheap-gate evidence.

Use:

`SMALL / OBSCURE WEAK-DATA LEAGUE — SCOPE EXCLUSION`

when that is the operative reason.

**Important:** small league size by itself is not the test. A smaller but established, well-covered professional top flight can remain actionable. The exclusion targets weak/obscure/data-poor environments, not merely countries or leagues with fewer clubs.

A league that fails this prerequisite is **not CONDITIONAL** and must not consume cheap-gate research.

The Netherlands **Eerste Divisie**, Mexico **Liga de Expansión MX / Ascenso MX**, Germany **2. Bundesliga**, and Norway **OBOS-ligaen (1. divisjon)** are explicit approved NORMAL second-division exceptions. England **Championship** is a narrowly approved CONDITIONAL second-division pilot; it is never blanket Work admission.

### Netherlands Eerste Divisie Jong/U21 participant exception — effective 2026-09-19 ICT

Official Netherlands Eerste Divisie league fixtures remain NORMAL/direct-to-Work even when one or both participant teams are Jong/U21/reserve-branded. The generic youth/Uxx/reserve/development exclusion is overridden **only for participant identity inside this approved competition**.

Examples include Jong Ajax, Jong PSV, Jong AZ, Jong FC Utrecht, and equivalent U21-labelled participants when they are playing an official Eerste Divisie fixture.

Do not extend this exception to separate youth/U21 leagues, reserve/development competitions, friendlies, cups, or other competitions involving those clubs. No structural or ranking bonus is implied.

---

## 2. Admission classes

### PRIORITY

Automatically eligible to enter the Work handoff when the fixture also clears the normal senior-quality rules.

These are leagues where the goal environment and/or recurring model usefulness justify regular deep screening.

### NORMAL

Automatically eligible to enter the Work handoff when the fixture clears the normal senior-quality rules.

These leagues are worth screening, but are not given any structural advantage merely because of league status.

### CONDITIONAL

CONDITIONAL covers **credible senior professional national top flights** and explicitly approved professional second-division pilots (currently **England Championship**) that survive Section 1, without blanket Work admission.

Do **not** send the entire league to Work by default.

A fixture from a CONDITIONAL league may enter Work only when Step 0 can establish a cheap, current Over signal without deep research. Use AiScore-level fixture/team information already present in the date/fixture batch, one directly related AiScore team/fixture surface, or another already-cached registry note only; do not perform the full structural research here.

**Operation bound:** do not run broad web search for a conditional gate. Batch fixtures from the same competition/team surface where possible. If the required recent-form evidence is not immediately available from the batch/cached evidence or one direct AiScore surface, exclude the fixture for that run rather than expanding research.

Cheap conditional admission requires at least one of the following, with no obvious contradictory low-goal signal:

- both teams' recent five-match average total goals are at least 2.8; or
- one team is at least 3.2 recent average total goals and the opponent is at least 2.6; or
- both teams show at least 3 of their last 5 matches reaching 3+ total goals; or
- a current cached league note in this registry explicitly marks the competition as temporarily `CONDITIONAL-ADMIT` for the active season.

If the required cheap evidence is not readily available, **exclude before Work** rather than spending Work usage to resolve it.

Classify the row as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

This is an operational scope exclusion, not a model PASS and not evidence that the specific match would have gone under.

### LOW-GOAL EXCLUDE

Never send normal domestic-league fixtures from these competitions to Work unless the user explicitly requests a temporary trial.

Classify as:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

### HARD EXCLUDE

Absolute operational exclusion under the active user rule. No automatic override.

---

## 3. Current direct-to-Work registry

### PRIORITY

- Netherlands — Eredivisie
- Germany — Bundesliga
- Belgium — Belgian Pro League / First Division A
- Norway — Eliteserien
- Norway — OBOS-ligaen / 1. divisjon **(approved professional second-tier NORMAL intake; PROVEN_LEAGUE mandatory, not Tier 1)**
- Sweden — Allsvenskan
- Denmark — Superliga
- Iceland — Besta deild karla / top flight
- Austria — Bundesliga
- United States/Canada — Major League Soccer
- Australia — A-League Men

### NORMAL

- Netherlands — Eerste Divisie **(explicit approved lower division)**
- England — Premier League
- Germany — 2. Bundesliga **(approved professional lower-division NORMAL intake; PROVEN_LEAGUE required, not Tier 1)**
- Spain — LaLiga
- Italy — Serie A
- France — Ligue 1
- Portugal — Primeira Liga
- Scotland — Premiership
- Switzerland — Super League
- Brazil — Serie A
- Mexico — Liga MX
- Mexico — Liga de Expansión MX / Ascenso MX **(explicit approved lower division)**
- Saudi Arabia — Saudi Pro League

These classes control **admission to Work only**. They do not award a PRE grade, archetype, burden, or betting preference.

---

## 4. Current CONDITIONAL pool

A league is **not automatically CONDITIONAL merely because it is a senior top flight**.

To enter the CONDITIONAL pool it must first be an established senior professional national top flight with sufficient current data quality for the cheap gate. Unknown, obscure, weak-data, semi-pro-like, or otherwise marginal environments stay scope-excluded without a cheap-gate attempt.

The following competitions are the **complete normal-sweep CONDITIONAL whitelist**. Only these may receive the cheap conditional gate unless this registry is deliberately updated or the user grants a one-run override:

- England — EFL Championship / Championship **(targeted 2026-10-11 pilot only; fresh source-backed fixture goal gate)**
- Czech Republic — First League
- Poland — Ekstraklasa **(2026-10-11 bounded FAST_PRODUCTION source-local conditional pilot; both-side scored/conceded proof, draw-trap guard)**
- Greece — Super League
- Romania — Liga I
- Croatia — HNL
- Serbia — SuperLiga
- Slovenia — PrvaLiga
- Slovakia — Niké Liga
- Hungary — NB I
- Bulgaria — First League
- Republic of Ireland — Premier Division
- China — Super League
- India — Indian Super League
- UAE — Pro League
- Qatar — Stars League
- Peru — Liga 1
- Bolivia — Primera División / División Profesional
- Chile — Primera División
- Colombia — Primera A
- Ecuador — LigaPro Serie A
- Uruguay — Primera División
- Russia — Premier League

This list **is a whitelist** for normal Step-0 execution.

Any unlisted domestic league is outside the normal sweep, even if it is a senior top flight, until it is deliberately promoted into PRIORITY, NORMAL, or CONDITIONAL through a registry update or explicit one-run user override.

Do not research an unlisted league merely to determine whether it might deserve CONDITIONAL status.

---

## 5. Current LOW-GOAL EXCLUDE registry

- Vietnam — V.League 1
- South Korea — K League 1
- Argentina — Liga Profesional / Primera División

These remain excluded from the normal daily Over sweep until a later league-level audit explicitly restores them.

Club nationality does not transfer the exclusion to continental or cup competition.

---

## 6. Current HARD EXCLUDE registry

### Finland — all domestic leagues, every tier/category

Includes men's and women's domestic league competitions.

Use:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

Finnish Cup and senior continental fixtures involving Finnish clubs are not excluded solely by this rule.

### Japan — all domestic league competitions, every tier/category

**Effective:** 2026-09-12 ICT onward, by explicit user directive.

Includes J1 League and any other Japanese men's or women's domestic league competition that would otherwise survive the quality overlay.

Use:

`JAPANESE DOMESTIC LEAGUE — HARD EXCLUSION`

Japanese domestic cups and senior continental fixtures involving Japanese clubs are **not** excluded solely by this rule.

---

## 7. Existing quality exclusions still apply first

The registry does not generally revive fixtures excluded by the active model quality overlay. Continue to remove youth/Uxx, reserve/development, amateur/semi-pro, regional/state/provincial, domestic lower divisions unless explicitly approved, and very weak/obscure data environments.

**Explicit lower-division approvals:** Netherlands Eerste Divisie, Mexico Liga de Expansión MX / Ascenso MX, Germany 2. Bundesliga (NORMAL), Norway OBOS-ligaen / 1. divisjon (NORMAL) and England Championship (CONDITIONAL cheap gate, not wholesale). They enter through the NORMAL lane in Section 3 and are not filtered out merely for being second divisions.

**Scoped participant override:** official Netherlands Eerste Divisie league fixtures involving Jong/U21/reserve-branded teams are included under the 2026-09-19 exception. Do not classify those official league fixtures as youth/reserve exclusions solely from the participant name.

The UEFA Youth League remains a separate manual trial and is not made official by this registry.

---

## 7A. Explicit 2026-10-11 Big Five second-division intake overlay

For *new* sweeps only, Germany **2. Bundesliga** enters the NORMAL league-profile verification footprint; it is not Tier 1 and must furnish PROVEN_LEAGUE source evidence (>=2 genuinely observed previous confirmed XI fixtures and >=2 observed Asian-total market fixtures), actual canonical fixture/time, A/B operational status, current news/market channel evidence and near-KO recheck. No generic fixture automatically becomes C FOLLOW/RESERVE/BET.

England **Championship** is the *only* second-tier exception to the usual FAST_PRODUCTION skip of CONDITIONAL leagues. Review its in-window block cheaply, without a league-wide XI or bookmaker crawl. For each Championship fixture that could be forwarded to Work, the new league-channel intake validator requires `championship_recent_goal_evidence`: **five actual competitive pre-kickoff results for each team** with match IDs, UTC timestamps, scored/conceded goals, independently checked source URLs and observation timestamp <=7 days before KO. Admission requires both five-match mean total goals >=2.8; OR a >=3.2 carrier with opponent >=2.6; OR both sides >=3/5 Over 2.5. Reject either side with >=3/5 0-0/1-1 results or >=4/5 <=2-goal results. Missing/stale/unverifiable data => no Work. It also requires PROVEN_LEAGUE evidence independently of the goal signal. This is a limited *research-admission gate*, never a goal forecast.

Spain Segunda, Italy Serie B, France Ligue 2, England League One/Two, Spain Primera Federación, Italy Serie C, France National remain outside routine proactive discovery. One-run explicitly named exceptions may be assessed outside the routine scope but do not rewrite the permanent registry; France Ligue 2's prior run-specific skip must not be silently reversed. Germany 3. Liga remains explicitly excluded. Explicit country/friendly exclusions and protected women's/continental coverage unchanged.

The active `CURRENT_MODEL.md` and Step0 launcher outrank stale historical sections elsewhere in the registry. This overlay is a prospective **competition research filter**, not a retroactive Step0 mutation. See `research/LOWER_DIVISION_PROOF_MANIFEST_2026-10-11.md`.

## 7B. Norway OBOS-ligaen source-gated lower-division intake — 2026-10-11

For only NEW prospective Step0 sweeps, Norway **OBOS-ligaen / 1. divisjon / Norway First Division** is approved NORMAL for **routine competition-block discovery and operational research screening**, not automatic inclusion in an A/B Work queue. Its country+league name must match the exact code registry; `Norway 2. divisjon` and `Norway 3. divisjon` are not approved. Excluded domestic countries, all friendlies, reserve/youth-only leagues and protected women's/cup/continental coverage are unchanged.

OBOS **must** carry a real verified `PROVEN_LEAGUE` publication profile, **never** `TIER1_STANDARD`: at least two distinct completed 2026 league fixtures with actual published lineup sources (both teams), and two real league fixtures with observed Asian goal-total ladder publication, verified by the sweep operator from retrievable source URLs. Preserve season, source URLs, evidence checked timestamp, team-news channels and fixture identity/kickoff. The historical evidence manifest at `models/football/research/OBOS_LEAGUE_CHANNEL_PROOF_2026-10-11.md` documents inspectable examples but is **not** a persisted live-season `VERIFIED_CHANNELS` attestation. If fresh providers are unavailable, this league's individual fixtures do not pass the A/B intake gate; do not fabricate odds or verified XI.

A routine league profile is **not** an Over goals forecast; do not promote Ranheim/Moss/Kongsvinger via hardcoded team names or assumed >2.5 price. The prospective Step1 whole-queue goal-route screen still uses actual 4–10 previous competitive results. Step1 requires fixture-specific actual Asian totals, news and XI sources; Step2 requires the genuinely current offered line, reachable WAIT and independent C/C2 decision. Never reopen or relabel completed sweeps, original source hashes, historical boards or Actual Bets.

## 7C. Poland Ekstraklasa conditional coverage pilot — 2026-10-11

Poland Ekstraklasa remains **CONDITIONAL**, not a NORMAL or Tier1 automatic intake league. For NEW prospective /sweep only, it receives a single source-local block look-up when its in-window competition block is directly available or a current cached league locator exists. Do **not** launch global discovery or per-fixture deep XI/market crawls because a season-wide Over 2.5 percent looks favorable. This is not an expansion to Poland I Liga or youth/reserve-only competitions.

To route an individual Ekstraklasa fixture to the A/B Work queue, the `LEAGUE_CHANNEL_FIRST_V1` validator requires:
- Country `Poland`, exact competition label `Ekstraklasa`, canonical real fixture ID and kickoff UTC; no other country receives this pilot.
- Fresh `poland_ekstraklasa_recent_goal_evidence` with one `captured_at_utc` at most seven days before actual kickoff and independently source-backed `home` and `away` collections, each exactly five genuine completed competitive match records with unique `match_id`, `kickoff_utc`, `goals_for`, `goals_against`, `competitive=true`. Each result must be demonstrably finished at capture and no more than 120 days old. No hypothetical match odds or user bets in this evidence.
- Admission signal: both last-five total-goal means >=2.8, OR a >=3.2 carrier and opponent >=2.6, OR each side >=3 of five Over 2.5. Block if either team has >=3/5 0–0/1–1 draws or >=4/5 matches ending <=2 total goals. Incomplete/stale evidence means **not ready for Work**, not an Under or C PASS.
- All independent normal professional A/B viability, source-checked season `PROVEN_LEAGUE` (minimum two real lineup and two Asian-goal-total fixture publication examples) because it is **not** in TIER1_STANDARD, legitimate league market/news channels, observed verified fixture/time, and near-kickoff recheck. /rank separately verifies actual match bookmaker totals, line, quote timestamp, XI and news; /xi handles genuinely executable odds.

No hardcoded GKS/Raków/Lech boosts. A past high Over frequency can arise from conceding, and a 1–1 can be a dead end. Step1's whole-queue goal-first scoring remains decisive **only for research order** across already eligible A/B fixtures. No frozen sweep, Step0 source hash, operational rank, C official/C2 shadow decisions, or Actual Bets are modified. See `research/POLAND_EKSTRAKLASA_CONDITIONAL_PILOT_2026-10-11.md`.

## 8. Promotion / demotion policy

Do not move a league between classes because of one slate.

Use post-slate and league-level audits to update the registry when there is meaningful evidence. Useful signals include average goals, Over 2.5 frequency, scoreline distribution, bookmaker total baselines, and repeated model outcomes.

Changes should be written here once, so future daily sweeps benefit without repeating the same research.

---

## 9. Work-usage invariant

The raw AiScore universe may be large. That is acceptable.

The Work handoff should contain only:

`PRIORITY + NORMAL + QUALIFIED CONDITIONAL fixtures that passed the cheap gate + separately eligible cups/continental fixtures`

It must not contain:

- youth/reserve/lower/amateur/regional fixtures, except the explicitly approved lower divisions Netherlands Eerste Divisie, Mexico Liga de Expansión MX / Ascenso MX, Germany 2. Bundesliga (NORMAL), Norway OBOS-ligaen / 1. divisjon (NORMAL) and England Championship fixtures with a verified conditional cheap goal signal; official Eerste Divisie fixtures involving Jong/U21/reserve-branded participant teams are specifically allowed;
- small/obscure weak-data leagues;
- LOW-GOAL EXCLUDE;
- HARD EXCLUDE;
- conditional fixtures that failed/no-data'd the cheap gate.

**DISCOVER ONLY THE ACTIVE NARROW-CORE REGISTRY FOOTPRINT; DO NOT CRAWL UNLISTED LEAGUES.**

---

## 10. v0.2.53 ranking and burden modifiers

These modifiers are prospective from 2026-09-12 ICT and operate after the admission class is known.

### Japan domestic leagues

The HARD EXCLUDE in Section 6 remains absolute for the normal daily board, including J1 League. Do not reopen the pool from an isolated winner or high-scoring exception. Only a later explicit user directive and registry update may change this class.

### China Super League

China Super League remains CONDITIONAL at the admission stage.

A CSL fixture that clears the cheap admission gate is not automatically eligible for an O3.0+ burden or MCE. For either state require:

- both teams' relevant current home/away evidence independently supports a credible 3+ match environment; or
- one team qualifies as true `CC+ — CARRIER CEILING` and the proposed burden survives weak opponent contribution.

Otherwise record:

`CSL HIGH-BURDEN GATE FAILED — HOLD/PASS`

All-venue recent averages alone do not clear this final burden gate.
