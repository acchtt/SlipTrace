# Football A — Compiled Step-2 Execution Specification (Historical)

**Status:** RETIRED FOR NEW FOOTBALL C PRODUCTION — HISTORICAL FOOTBALL A ONLY
**Current authority:** `models/football/CURRENT_MODEL.md` + `models/football/production/FOOTBALL_C.md` + `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` + `03_NORMAL_CHAT_LIVE.md`

> This file is retained only to reconstruct historical Football A/v0.2.x decisions. It must not be loaded as predictive or execution authority for a new Football C board, XI/odds assessment, live decision, or persistence transaction.


**Historical workflow:** Football A XI + odds / live execution compiler  
**Historical model:** Football A

The rules below describe the Football A execution authority that existed at that historical epoch. They remain valid only for reconstructing decisions actually created under that authority. They do not govern a new Football C XI/odds or live assessment.

---

## 1. Fixed execution order

Every material XI+odds assessment must execute this order:

`FROZEN PRE TRACE -> IDENTITY/STATUS -> EPOCH CLASS -> XI ROLE-MECHANISM MATRIX -> POST-XI FOOTBALL RESEARCH -> H2H/MATCHUP GATE -> CURRENT CQ/FAILURE UPDATE -> MARKET-HISTORY ATTEMPT -> FROZEN_PRE_MARKET_ALIGNMENT -> EGE/CARRIER CURRENT-EPOCH COMPILER -> CURRENT_PRE_EXECUTION_FIT -> BURDEN AUTHORITY -> B+/UPPER-TAIL GATES -> DECAY/REACHABILITY -> PRICE -> LIVE/PREMATCH ELIGIBILITY -> PROVISIONAL/FINAL VERDICT -> PERSISTENCE TRANSACTION`

Do not:
- rebuild frozen PRE from scratch;
- let market price retroactively improve frozen PRE;
- use a later current-PRE state to overwrite frozen Work history;
- treat H2H scorelines as a scoring route;
- treat HMA as permission to buy a worse ordinary burden;
- publish a prematch official lock before the mandatory post-XI football-research attempt is recorded;
- convert an opportunistic post-kick quote into official exposure without a predeclared plan or explicit active exception;
- infer an official state from stale v0.2.54 persistence wording.

---

## 2. Required frozen PRE input

Read the frozen `FOOTBALL_PRE_DECISION_SPEC_V1` trace when present.

Minimum required historical fields:
- AiScore fixture ID;
- kickoff ICT / UTC authority;
- PRE grade;
- board tier;
- Structural Rank;
- HOME/AWAY route states;
- weaker-route independence state;
- HOME/AWAY carrier state;
- dominant failure mode + severity;
- supported burden/range;
- burden basis/confidence;
- upper-tail state if already frozen;
- evidence confidence.

If the coverage row conflicts with the original Work artifact:

`PERSISTENCE SYNC FAULT — FROZEN PRE PRESERVED`

Do not repair the football thesis by conversational memory.

---

## 3. Identity / status gate

Before any material verdict:
1. match AiScore fixture ID;
2. verify home/away orientation;
3. verify kickoff/status;
4. inside 90 minutes of kickoff, recheck current AiScore status/time;
5. inside 30 minutes when official exposure is considered, identity/status recheck is mandatory.

Conflict:

`FIXTURE IDENTITY / HOME-AWAY / STATUS CONFLICT — HOLD`

A side-symmetric Over market does not waive identity because venue assumptions may have affected PRE.

---

## 4. Evidence epoch class

Set exactly one:

- `PREMATCH` — fixture has not kicked off;
- `JUST-STARTED/LIVE — PREDECLARED PLAN EXISTS`;
- `JUST-STARTED/LIVE — ACTIVE MATCH-SPECIFIC EXCEPTION`;
- `JUST-STARTED/LIVE — NO PREDECLARED PLAN`;
- `STALE/FINISHED — AUDIT ONLY`.

This class is decided before any `TAKE NOW` language.

If LIVE and there is no predeclared plan or active match-specific exception:

`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`

Do not issue an official TAKE.

---

## 5. XI role-mechanism matrix

Evaluate XI by mechanism, not by headcount.

For every frozen route/carrier identify the required functional layers:

- **CREATE** — primary chance creators / progression / final-ball source;
- **FINISH** — penalty-box finishers / high-value-shot receivers;
- **SERVICE** — width, central combinations, set-piece delivery, transition outlet, or equivalent mechanism service;
- **SUSTAIN** — midfield/press/territory or bench depth required to maintain pressure;
- **RESIST** — defensive/structural personnel relevant to opponent scoring leakage.

Classify each required layer:

- `PRESERVED` — expected functional quality remains;
- `REPLACED-EQUIVALENT` — named replacement plausibly preserves the same function;
- `DEGRADED` — function remains but at materially lower quality/cohesion;
- `BROKEN` — sole/critical function is absent with no credible equivalent;
- `UNKNOWN`.

Then classify each scoring mechanism:

### XI MECHANISM — PRESERVED
All critical CREATE/FINISH/SERVICE layers are PRESERVED or REPLACED-EQUIVALENT and no known SUSTAIN/RESIST change creates the frozen failure mode.

### XI MECHANISM — DEGRADED
At least one critical layer is DEGRADED or unresolved, but the route still has a credible current path.

### XI MECHANISM — BROKEN
A sole/critical CREATE, FINISH or SERVICE layer is BROKEN and no credible equivalent exists, or current XI directly creates the dominant frozen failure mode.

### XI MECHANISM — UNKNOWN
Material lineup/role identity remains unresolved.

Effects:
- PRESERVED may retain the frozen route/carrier state;
- DEGRADED may lower current burden/tier or block upper-tail;
- BROKEN cannot be rescued by price/market and requires current structural downgrade/HOLD unless an independent surviving carrier route remains;
- UNKNOWN blocks final official exposure if it can change the executable burden.

`ROTATION — ATTACKING DEPTH PRESERVED` corresponds to all critical attacking layers being PRESERVED/REPLACED-EQUIVALENT.  
`ROTATION — COHESION / ROUTE DAMAGE` corresponds to one or more critical layers being DEGRADED/BROKEN.

---

## 6. Mandatory post-XI football research

After first-pass XI interpretation, attempt targeted fixture-specific football research.

Persist exactly one:
- `POST-XI RESEARCH = FOUND`;
- `POST-XI RESEARCH = LIMITED`;
- `POST-XI RESEARCH = UNAVAILABLE — ATTEMPTED`;
- `POST-XI RESEARCH = SKIPPED — EXPLICIT USER WAIVER`.

Market-history lookup does not satisfy this gate.

For PREMATCH:
- final official publication is forbidden until this status is recorded.

For JUST-STARTED/LIVE:
- latency-first verdict may be surfaced first only after live eligibility from Section 4 is known;
- the verdict is `PROVISIONAL FAST VERDICT` until the research attempt is recorded;
- do not write Website Picks as final official exposure before the research attempt completes;
- if research materially contradicts the first verdict while the quote/state remains current, correct immediately;
- if state changes first, old quote is VOID and a new evidence epoch begins.

---

## 7. H2H / matchup-history compiler

H2H is supporting/matchup evidence. It never creates a scoring route by itself.

Use this order:

`CURRENT MECHANISM -> TRANSFERABLE SAME-VENUE H2H -> TRANSFERABLE RECENT ALL-VENUE H2H -> LONG-RUN BACKGROUND`

### 7.1 Transferability

Label:
- `HIGH TRANSFERABILITY` — same competition/class, broadly comparable tactical role and no material manager/core-mechanism change;
- `MEDIUM TRANSFERABILITY` — one relevant context changed but the tested mechanism remains comparable;
- `LOW TRANSFERABILITY` — major manager/system/core-personnel/division/class/competition-role change;
- `UNKNOWN`.

Do not use a fixed old scoreline merely because the teams are the same.

### 7.2 H2H state

Set exactly one:
- `H2H = MECHANISM-CORROBORATING`;
- `H2H = MECHANISM-CONTRADICTING`;
- `H2H = MIXED`;
- `H2H = LOW TRANSFERABILITY`;
- `H2H = INSUFFICIENT / NONE`.

### 7.3 Allowed effect

- H2H alone = context / SOFT PENALTY at most.
- A HARD VETO requires mechanism-compatible H2H suppression **plus an independent current negative channel** such as current CQ suppression, tactical control, route damage, or opponent mechanism resistance.
- Long-run H2H alone never creates a veto, route upgrade, burden upgrade, or direct execution permission.
- Open historical H2H cannot rescue current suppressive football evidence.

### 7.4 O3.0+ gate

Before O3.0+ official execution:
1. run same-venue transferable H2H review;
2. identify the current suppression/openness mechanism;
3. if H2H corroborates suppression and an independent current negative channel agrees, O3.0+ is blocked **unless the current upper-tail proof explicitly defeats that same mechanism**;
4. if H2H is mixed/low-transferability/insufficient, record that and do not auto-lower burden.

### 7.5 B+ exact-burden gate

H2H may block B+ exact-burden exposure only when:
- H2H is HIGH/MEDIUM transferability;
- suppression is mechanism-compatible;
- an independent current negative channel corroborates it.

H2H must not reintroduce an extra positive hardener.

Persist transferability, sample context, H2H state, tested mechanism and independent corroborating channel.

---

## 8. Current chance-quality / failure update

Use the same evidence discipline as frozen PRE, but at the current XI epoch.

Set:
- `CURRENT CQ = STRONG / USABLE / WEAK / UNKNOWN`;
- `CURRENT FAILURE = HARD_VETO / SOFT_PENALTY / NONE / UNRESOLVED`.

### CURRENT CQ — STRONG
Direct current football evidence materially supports high-value chance creation through the relevant route: big chances, xG/xGOT, central/box access, quality SOT, sustained dangerous creation, or a credible data-poor equivalent reinforced by mechanism + repeatability.

### CURRENT CQ — USABLE
The route remains credible but direct current chance evidence is incomplete or moderate.

### CURRENT CQ — WEAK
Current evidence materially undermines high-value chance production.

### CURRENT CQ — UNKNOWN
Required current evidence cannot be established.

A HARD VETO follows the same non-compensatory rule as PRE:
- two independent current negative channels; or
- one decisive current fact that directly removes the required mechanism.

Price/market never upgrades CURRENT CQ.

---

## 9. Market-history attempt

Attempt:

`OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH`

Persist:
- `MARKET HISTORY FOUND`;
- `MARKET HISTORY UNAVAILABLE — ATTEMPTED`;
- `MARKET HISTORY SKIPPED — USER REQUEST`.

Market history:
- may trigger reinspection;
- may corroborate a football explanation;
- may not create a scoring route, carrier, EGE, upper-tail path, or official exposure by itself.

---

## 10. Frozen-PRE market alignment

This is the anti-circularity diagnostic and must remain separate from later current PRE.

Persist:

`FROZEN_PRE_MARKET_ALIGNMENT = CLEAR / UNDERCUT / SEVERE_UNDERCUT / HIGH_MARKET_CONFLICT / UNCLEAR`

Compare current market center against **frozen PRE supported burden/range**.

### Undercut
- 0.25+ below frozen lower edge/single burden -> `UNDERCUT — RE-SCREEN REQUIRED`;
- 0.50+ below -> `SEVERE_UNDERCUT — NO INSTANT LOCK` absent a football-led override.

A football-led override requires:
1. one specific current football explanation for why frozen PRE overestimated burden; and
2. one independent corroborating current channel.

Persist both. Market price itself is not corroboration.

### High-market conflict
A materially weak/PASS/lower frozen state with market center 0.50+ above implied burden triggers mandatory football/carrier re-screen. Market alone never promotes it.

Do not recompute this field after market-calibrated current PRE is created.

---

## 11. EGE current-epoch compiler

v0.2.50 EGE remains a valid **current football-regime diagnostic** after XI.

It may establish:
- `EGE CURRENT REGIME = CLEARED / NOT CLEARED`;
- a football-supported `EGE CURRENT BURDEN` for monitoring, upper-tail assessment and comparison.

However, under later Decay-First authority:

**EGE alone does not authorize direct prematch execution above frozen supported burden.**

Therefore:
- EGE inside/below frozen burden may support ordinary execution;
- EGE above frozen burden does not replace the official ordinary execution anchor;
- direct above-frozen execution requires a later explicit current-PRE authority, namely the ELITE/EXTREME Carrier Market Decomposition lane or another future explicit rule;
- otherwise above-frozen EGE becomes `QUALIFIED — LIVE DECAY PLAN` to the ordinary supported execution burden.

This preserves EGE football information while honoring the later Decay-First execution precedence.

---

## 12. Carrier Market Decomposition — explicit current-PRE exception

After frozen-PRE market alignment is recorded, run the active carrier decomposition.

Inputs:
- current Asian total;
- current Asian handicap;
- current 1X2;
- XI mechanism state;
- current football/carrier evidence.

Use the active heuristics:
- `MCL ≈ (Total + |AH|)/2`;
- `MOS ≈ max(0,(Total-|AH|)/2)`.

Classify:
- `MARKET CARRIER = ELITE`;
- `MARKET CARRIER = EXTREME`;
- `MARKET CARRIER = NOT CLEARED`;
- `MARKET CARRIER = UNRESOLVED`.

Only ELITE/EXTREME may create:

`MARKET-CALIBRATED CURRENT PRE`

above or below frozen PRE under the active carrier-decomposition rule.

This is the **only current generic Step-3 burden-reopen exception** that may bypass raw frozen-burden Decay-First after this compilation.

Do not use HMA, old MCE, EGE alone, or price alone as a substitute for this exception.

---

## 13. Current-PRE execution fit

After current PRE is determined, persist separately:

`CURRENT_PRE_EXECUTION_FIT = CLEAR / ABOVE_CURRENT_PRE / BELOW_CURRENT_PRE_CONFLICT / UNCLEAR / NOT_APPLICABLE`

Rules:
- for ELITE/EXTREME carrier lane, compare selected line to market-calibrated current PRE;
- for all other lanes, current PRE = ordinary supported execution burden and this field is normally CLEAR/ABOVE;
- this field never replaces `FROZEN_PRE_MARKET_ALIGNMENT`.

Thus:
- frozen alignment remains the anti-circularity audit;
- current execution fit determines whether the explicit current-PRE exception is executable.

---

## 14. Burden authority

Use this precedence:

1. **ELITE/EXTREME MARKET-CALIBRATED CURRENT PRE**, if Section 12 clears;
2. otherwise **frozen supported burden/range**, adjusted downward only by current football/XI damage;
3. **EGE CURRENT BURDEN** is diagnostic/monitoring unless it is independently absorbed by #1;
4. generic HMA never raises official ordinary burden;
5. MCE remains shadow/audit unless a later explicit authority says otherwise.

Never raise burden solely because the market is high.

---

## 15. B+ execution compiler

### 15.1 Exact frozen supported burden

For frozen `B+ WATCHLIST`, exact supported-burden direct eligibility clears when:
- XI mechanism is PRESERVED or credibly equivalent;
- selected line = exact frozen supported burden;
- price >= 1.65;
- frozen-PRE market alignment is acceptable/resolved;
- no current HARD VETO;
- post-XI research gate completed.

No extra positive hardener is required.

Use:
`B+ PROTECTED-LINE — DIRECT LOCK ELIGIBLE`

then, if no other blocker:
`B+ PROTECTED-LINE — OFFICIAL LOCK`.

### 15.2 B+ +0.25

The older B+ file contains both a +0.25 direct label and an explicit statement that it does **not** override Decay-First.

Compiled result:

- ordinary B+ +0.25 above frozen burden = `B+ ABOVE BURDEN — WAIT / LIVE DECAY`;
- VERIFIED PRE carrier status alone does not override this;
- a +0.25 line may become direct only if the later ELITE/EXTREME Carrier Market Decomposition independently creates a current PRE that includes that line.

Thus B+ +0.25 has one canonical ordinary answer: WAIT.

### 15.3 +0.50 or more
Never automatic for ordinary B+.

---

## 16. Generic HMA compiler

HMA remains:
- monitoring tolerance;
- audit label;
- context for how far a strong fixture remains structurally interesting.

For new ordinary official decisions:

**HMA does not create direct prematch exposure above frozen supported burden.**

Disable as official ordinary paths:
- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`;
- HMA-boundary direct entry;
- HMA-boundary live-decay target above supported burden.

If market is above ordinary supported burden:
`QUALIFIED — LIVE DECAY PLAN`
to the ordinary supported execution burden.

Only the explicit ELITE/EXTREME current-PRE carrier lane may create a higher official execution burden.

---

## 17. Upper-tail compiler

Required when:
- A2 executes at the top of its supported range;
- O3.0+ official execution is considered;
- a current-PRE carrier line materially requires a 4+ path.

Set one:
- `UPPER TAIL = PROVEN`;
- `UPPER TAIL = NOT PROVEN`;
- `UPPER TAIL = BLOCKED BY SUPPRESSION`;
- `UPPER TAIL = UNRESOLVED`;
- `UPPER TAIL = NOT REQUIRED`.

### PROVEN
At least one of:

**A. Carrier-funded 4+ path**
- current carrier mechanism is VERIFIED/ELITE;
- credible independent 3+ team-goal path remains;
- at least one additional-goal channel is current and route-owned or opponent-failure compatible;
- XI mechanism preserved;
- no current HARD VETO.

**B. Elite two-sided 4+ path**
- both current routes survive XI;
- both have at least USABLE current CQ;
- at least one has STRONG current CQ;
- combined route mechanisms plausibly fund 4+ without a low-probability late rescue;
- no current HARD VETO.

Historical Over/BTTS/H2H scorelines cannot prove this alone.

For O3.0+, Section 7 H2H gate must also clear.

---

## 18. Decay / reachability

For ordinary non-ELITE/non-EXTREME lanes:

If selected/current line > supported execution burden:
`QUALIFIED — LIVE DECAY PLAN`

Target:
- lowest acceptable line inside frozen supported burden/range;
- never a generic HMA boundary.

Persist:
- target;
- minimum price;
- current line/price;
- `Decay Gap`;
- `Reachability = REACHABLE / BORDERLINE / UNREACHABLE`;
- cancellation triggers.

For ELITE/EXTREME carrier:
- evaluate current-PRE direct execution before WAIT;
- Decay Gap >=1.00 requires explicit unreachable-decay review;
- Decay Gap >=1.50 may not remain a raw-frozen-burden WAIT without documented market distortion.

---

## 19. Price

- hard minimum = 1.65;
- preferred = 1.70+;
- burden before price;
- lowest acceptable burden first;
- price is tie-breaker after football/burden validity;
- higher payout never compensates for higher burden.

If supported line is present but price <1.65:
`QUALIFIED — PRICE BELOW FLOOR`.

---

## 20. Prematch / live verdict compiler

### PREMATCH

A final prematch official lock requires:
- identity/status clear;
- XI/current football gates clear;
- post-XI research status recorded;
- market-history attempt recorded;
- H2H gate where required;
- market alignment resolved;
- burden authority resolved;
- upper-tail/B+ gates where required;
- price clears;
- no blocker.

Then:
`OFFICIAL LOCK`
or
`B+ PROTECTED-LINE — OFFICIAL LOCK`
or
`OFFICIAL LOCK — MARKET-CALIBRATED ELITE CARRIER`.

### JUST-STARTED/LIVE with predeclared plan or active exception

Latency-first is allowed.

First-line state may be:
`PROVISIONAL FAST VERDICT — TAKE <line> @ <price> NOW`
only if the predeclared plan/exception and already-known football/price/state gates clear.

This is user-facing latency control, not final persistence authority.

Immediately complete mandatory research attempt. If still clear:
`FINAL LIVE VERDICT — OFFICIAL LOCK`
and persist.

If research contradicts before state changes:
correct immediately.

If score/card/state changes:
old quote = VOID; new epoch required.

### JUST-STARTED/LIVE without predeclared plan/exception

Immediate verdict:
`NO OFFICIAL LIVE ENTRY — NO PREDECLARED PLAN`

Persist as:
`SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

No `TAKE NOW`.

---

## 21. Canonical output-state taxonomy

Final material states for new Step-3 assessments:

### Official
- `OFFICIAL LOCK`
- `B+ PROTECTED-LINE — OFFICIAL LOCK`
- `OFFICIAL LOCK — MARKET-CALIBRATED ELITE CARRIER`
- `OFFICIAL LOCK — LIVE DECAY PLAN` only from predeclared plan/active exception after final same-epoch checks

### Qualified waits
- `QUALIFIED — LIVE DECAY PLAN`
- `QUALIFIED — PRICE BELOW FLOOR`

### Holds
- `STRUCTURAL HOLD`
- `MARKET UNDERCUT — RE-SCREEN REQUIRED`
- `SEVERE MARKET UNDERCUT — NO INSTANT LOCK`
- `NO BET — EXPOSURE HOLD — UPPER-TAIL INSUFFICIENT`
- `B+ PROTECTED-LINE — HOLD — NEGATIVE VETO`
- `FIXTURE IDENTITY / HOME-AWAY / STATUS CONFLICT — HOLD`

### Shadow / non-official
- `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`
- `SHADOW MCE +0.25 — NO OFFICIAL EXPOSURE`
- `HMA MONITORING ONLY`

### Provisional latency state
- `PROVISIONAL FAST VERDICT` — never sufficient by itself for final Website Pick persistence

Superseded ordinary official states:
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`;
- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`;
- `QUALIFIED — EARLY SAME-LINE PRICE PLAN` at an above-burden HMA line.

Historical records retain their original labels.

---

## 22. Persistence contract

For each material assessment preserve:

### Historical/frozen
- frozen PRE compiler trace/reference;
- frozen supported burden;
- frozen Structural Rank;
- frozen failure mode.

### Current football
- assessment epoch;
- XI mechanism state per relevant route/carrier;
- post-XI research status;
- current CQ;
- current failure state;
- H2H transferability/state where material;
- market-history status.

### Market/current PRE
- current market center;
- AH;
- 1X2;
- selected line/price;
- `FROZEN_PRE_MARKET_ALIGNMENT`;
- market carrier state;
- EGE current regime/burden if assessed;
- market-calibrated current PRE if applicable;
- `CURRENT_PRE_EXECUTION_FIT`;
- upper-tail state;
- execution burden authority/source;
- decay target/gap/reachability when waiting.

### Final
- execution class;
- exposure decision;
- exact blocker/reason;
- model = `Football A`;
- Assessment Time.

For official exposure, persistence is a logical transaction:
1. write/upsert Decision State;
2. write/upsert Website Pick;
3. reconcile fixture/model/line/odds/stake/epoch/timestamps;
4. verify no duplicate active official pick.

If reconciliation fails:
`PERSISTENCE SYNC FAULT — EXPOSURE STATE UNCERTAIN`.

Never backfill an official Website Pick after the executable quote/epoch has passed.

---

## 23. Decision-State version authority

For **new** current assessments:
- official model label = `Football A`;
- v0.2.54/v0.2.53 fields/sections are historical compatibility only;
- old ranking/priority/MCE/live quarantine wording may not override this compiled specification.

Frozen historical Decision States keep their original version labels.

---

## 24. Deterministic replay outcomes

The following are canonical:

1. exact supported burden + price >=1.65 + gates clear -> DIRECT -> OFFICIAL LOCK;
2. exact supported burden + price <1.65 -> QUALIFIED — PRICE BELOW FLOOR;
3. ordinary +0.25 above frozen burden -> QUALIFIED — LIVE DECAY PLAN;
4. ordinary +0.50+ above frozen burden -> QUALIFIED — LIVE DECAY PLAN;
5. severe market undercut -> re-screen; no instant lock without defined football override;
6. B+ exact protected burden + gates clear -> B+ OFFICIAL LOCK;
7. B+ +0.25 + VERIFIED PRE carrier only -> WAIT; ELITE/EXTREME current-PRE carrier may independently reopen;
8. ELITE/EXTREME carrier clears -> evaluate market-calibrated current PRE before WAIT;
9. EGE clears above frozen burden without ELITE/EXTREME current-PRE carrier -> WAIT to ordinary supported burden;
10. EGE + ELITE/EXTREME carrier clears -> carrier current-PRE rule controls;
11. suppressive transferable H2H + independent current suppression -> HARD VETO contribution / O3+ blocked unless same mechanism explicitly defeated;
12. suppressive H2H without current corroboration -> SOFT PENALTY at most;
13. open H2H + current football suppression -> current suppression controls;
14. just-started quote + no predeclared plan/exception -> SHADOW / NO OFFICIAL LIVE ENTRY;
15. just-started quote + predeclared plan + known gates clear -> PROVISIONAL FAST VERDICT, then research, then final/persist if still clear;
16. score/card/material state change before finalization -> old quote VOID; new epoch;
17. Decision State succeeds / Website Pick fails -> PERSISTENCE SYNC FAULT;
18. duplicate official pick attempt -> block duplicate, preserve original official exposure.

---

## 25. Authority

This file is the final operational compiler for new XI/odds assessments and resolves overlaps among:

- `MODEL_RULES_FOOTBALL_V0.2.50.md` EGE;
- `MODEL_RULES_FOOTBALL_V0.2.51.md` MCE;
- `MODEL_RULES_FOOTBALL_A.md`;
- `MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`;
- `MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`;
- `MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`;
- `MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md`;
- `MODEL_RULES_FOOTBALL_AB_MARKET_ALIGNMENT.md`;
- `MODEL_RULES_FOOTBALL_A_CARRIER_MARKET_DECOMPOSITION.md`;
- `MODEL_RULES_FOOTBALL_A_POST_XI_WEB_RESEARCH_GATE.md`;
- `FOOTBALL_BETTING_PROCEDURE.md`;
- `02_NORMAL_CHAT_XI_ODDS.md`;
- `FOOTBALL_DECISION_STATE_AIRTABLE.md`.

This compiler does not change frozen Step-1 PRE. It only determines the current Step-2/Step-3 evidence state, executable burden, verdict and persistence behavior.
