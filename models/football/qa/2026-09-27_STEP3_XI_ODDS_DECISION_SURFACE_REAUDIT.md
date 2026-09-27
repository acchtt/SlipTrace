# Football Model QA — Step 3 XI/Odds Decision-Surface Re-Audit

**Date:** 2026-09-27 ICT  
**User workflow ordinal:** Step 3 = XI + odds assessment  
**Repo prompt:** `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`  
**QA framework:** `models/football/procedures/FOOTBALL_DECISION_SURFACE_QA.md`  
**Overall result:** `QA FAIL — CONTRADICTORY AUTHORITY + UNDER-SPECIFIED DECISION SURFACES`

This re-audit replaces the earlier contradiction-only Step-3 audit. It starts from a complete decision-input inventory and traces every material surface through collection, semantics, verdict effect, precedence and persistence.

## 1. Coverage result

- material Step-3 decision surfaces inventoried: **46**
- material surfaces traced: **46**
- explicitly non-material surfaces: **0**
- untraced material surfaces: **0**
- deterministic replay branches required by QA: **18**
- replay branches with one canonical outcome: **10**
- replay branches with contradictory or under-specified outcomes: **8**
- stale production authorities found: **5**
- critical contradictions: **6**
- high under-specification findings: **7**
- medium/stale findings: **5**

The re-audit is therefore complete in coverage, but Step 3 itself is not deterministic enough to pass.

---

## 2. Decision-surface matrix

| # | Decision surface | Current authority/effect | QA status |
|---:|---|---|---|
| 1 | AiScore fixture ID | canonical identity; mismatch blocks publication | PASS |
| 2 | competition + home/away | must match frozen board/user surface | PASS |
| 3 | kickoff + current status | near-kickoff revalidation; conflict = HOLD | PASS |
| 4 | frozen PRE grade/tier/rank | historical structural state; must not be rewritten | PASS |
| 5 | frozen route pair / second-route state | input to XI survival and current rerank | PASS |
| 6 | frozen practical-carrier state | input only; post-XI carrier may create new current state | PASS |
| 7 | frozen failure mode/severity | current XI/research may strengthen/weaken it without rewriting history | PASS |
| 8 | frozen supported burden / upper-tail state | core execution anchor, except disputed later lanes | **CONTRADICTORY** |
| 9 | confirmed XI starters/formations | user-supplied current football epoch | PASS |
| 10 | attacking mechanism survival | may preserve/damage current thesis and carrier lane | **UNDER-SPECIFIED** |
| 11 | defensive absences | may harden leakage/current burden | **UNDER-SPECIFIED** |
| 12 | rotation/bench/cohesion | PRESERVED vs COHESION/ROUTE DAMAGE changes burden | **UNDER-SPECIFIED** |
| 13 | current chance quality | can harden route/upper tail/current burden | **UNDER-SPECIFIED** |
| 14 | recent GF/GA / scoring-conceding form | supporting evidence; cannot create structure alone | PASS |
| 15 | home/away splits | route/context support | PASS |
| 16 | tactical matchup | may create suppression/override explanation | **UNDER-SPECIFIED** |
| 17 | competition incentive / leg state | context, not automatic veto | **UNDER-SPECIFIED** |
| 18 | fatigue/schedule | may reduce supported burden | **UNDER-SPECIFIED** |
| 19 | weather/pitch/data fault | prompt permits it as market-conflict explanation but no canonical acquisition/effect protocol | **UNDER-SPECIFIED** |
| 20 | H2H / matchup history | can affect O3.0+, B+ veto, compression | **UNDER-SPECIFIED — MATERIAL** |
| 21 | post-XI football-research status | mandatory separate process gate | PASS |
| 22 | market-history status | mandatory attempt; context only | PASS |
| 23 | current Asian-total market center | core market-alignment input | PASS |
| 24 | adjacent total board | protected-line / distribution context | PASS |
| 25 | user-supplied current Over price | executable-price authority for epoch | PASS |
| 26 | current Asian handicap | mandatory carrier decomposition input | PASS |
| 27 | current 1X2 favorite price | mandatory carrier decomposition input | PASS |
| 28 | market alignment vs frozen PRE | undercut/high-market re-screen | **SEMANTIC GAP** |
| 29 | EGE regime / post-XI EGE burden | can reopen burden under v0.2.50 | **CRITICAL CONTRADICTION** |
| 30 | MCE | current official use is shadow/quarantined | **STALE ACTIVE-LOOKING PATHS** |
| 31 | MCL/MOS carrier tier | explicit numeric decomposition plus football/XI gate | PASS with qualitative tail |
| 32 | market-calibrated current PRE | later carrier exception may raise/lower actionable burden | PASS as exception, but interaction gap remains |
| 33 | A2 upper-tail / 4+ gate | can block official exposure at high burden | **UNDER-SPECIFIED** |
| 34 | B+ exact protected burden | direct eligible with XI/alignment/floor/no veto | PASS |
| 35 | B+ +0.25 VERIFIED-carrier extension | one rule says direct; same file says it does not override Decay-First | **CRITICAL CONTRADICTION** |
| 36 | generic HMA above frozen burden | Decay-First disables direct HMA; prompt/procedure still re-enable it | **CRITICAL CONTRADICTION** |
| 37 | decay target / reachability | raw supported burden for ordinary lane; carrier exception later | PASS outside disputed lanes |
| 38 | just-started/live predeclared-plan eligibility | official live requires prior plan/exception, but fast path can say TAKE NOW without checking | **CRITICAL CONTRADICTION** |
| 39 | score/minute/state integrity | new state epoch; old quote void; plan separately survives/modifies/closes | PASS |
| 40 | 1.65 price floor | hard floor | PASS |
| 41 | one-exposure-per-match + auto-publish | affirmative final prematch lock publishes without second confirmation | PASS prematch |
| 42 | Decision State persistence | material current epoch | **STALE MODEL CONTRACT** |
| 43 | Website Pick transaction | required for official exposure with timestamp + reconciliation | PASS |
| 44 | model version / historical fidelity | current = Football A, but persistence contracts still declare v0.2.54 | **CRITICAL STALE AUTHORITY** |
| 45 | cross-match suppression | removed; each fixture independent | PASS, but stale HMA/old files still mention prior guard |
| 46 | active session/match overrides | only exact current, unexpired override may alter normal lane | PASS; production prompts contain expired examples that add noise |

---

## 3. Critical findings

### CRITICAL 1 — EGE vs Decay-First has no canonical current meaning

`MODEL_RULES_FOOTBALL_V0.2.50.md` explicitly creates a **post-XI EGE supported burden** that may be materially above frozen PRE and permits direct prematch `EGE DIRECT` when the market is inside that EGE burden.

Later `MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md` says:

- "The frozen supported burden is the execution anchor";
- ordinary direct exposure above frozen supported burden is disabled;
- above-burden market = WAIT to frozen supported burden.

Current production prompt still executes:

`... FINAL XI -> CHANCE QUALITY -> STANDARD/EGE BURDEN -> MARKET ... -> DECAY-FIRST ...`

There is no explicit rule saying whether:

A. EGE is still a legitimate **chosen supported execution burden** that Decay-First respects; or  
B. Decay-First killed EGE's ability to raise official burden, leaving only Carrier Market Decomposition as the later burden-reopen exception.

Same inputs can therefore yield `EGE DIRECT` or `WAIT — LIVE DECAY`.

**Required repair type:** PROCESS COMPLIANCE COMPILER, unless user intends to change EGE predictive eligibility itself.

### CRITICAL 2 — Generic HMA is disabled and re-enabled simultaneously

Final Decay-First authority disables automatic prematch official exposure above frozen burden.

But `02_NORMAL_CHAT_XI_ODDS.md` still contains executable sections for:

- `DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`;
- `QUALIFIED — EARLY SAME-LINE PRICE PLAN` at an HMA line;
- live-decay toward an HMA boundary.

`FOOTBALL_BETTING_PROCEDURE.md` also says Decay-First overrides HMA, then later verdict wording reintroduces supported/HMA direct execution and HMA-boundary targets.

The HMA rule file itself has a supersession notice, but production prompt/procedure still contain contradictory executable instructions.

### CRITICAL 3 — B+ +0.25 VERIFIED-carrier branch contradicts Decay-First inside the B+ patch itself

`MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md` says:

- +0.25 above burden is allowed for `CARRIER-LED / PROVEN+NOMINAL` with `PRACTICAL CARRIER CEILING — VERIFIED`;
- `B+ +0.25 CARRIER EXTENSION — DIRECT LOCK ELIGIBLE`.

The same file then says:

- it **does not override decay-first burden protection**.

Decay-First says any current prematch line above supported burden is WAIT, not direct exposure.

This branch has no unique correct action.

### CRITICAL 4 — just-started TAKE NOW conflicts with opportunistic-live quarantine

The Step-3 fast path says that after kickoff / just-started:

- if exact supported burden is available and known gates clear, say `TAKE ... NOW` immediately.

Later in the same prompt:

- official post-kick execution requires a **predeclared live-decay/HMA plan**;
- without a predeclared plan, attractive live Over is `SHADOW LIVE/DECAY — NO OFFICIAL EXPOSURE`.

The fast path does not first assert that a predeclared plan or match-specific exception exists.

A just-started screenshot can therefore produce either an official-looking TAKE or a quarantined shadow state.

### CRITICAL 5 — provisional fast verdict vs mandatory research vs auto-publish race

The post-XI research gate says an ordinary final prematch publication cannot occur until the targeted football-research attempt is recorded.

The just-started fast path intentionally emits the first verdict before that research.

Auto-publish says an affirmative final user-odds decision publishes immediately.

There is no canonical state distinction between:

- `PROVISIONAL FAST VERDICT — NOT PUBLISHABLE YET`; and
- `FINAL OFFICIAL VERDICT — PUBLISH NOW`.

The system can therefore publish too early or delay a supposedly immediate TAKE, depending on interpretation.

### CRITICAL 6 — active persistence contracts still declare Football v0.2.54

`FOOTBALL_DECISION_STATE_AIRTABLE.md` declares:

- official model = Football v0.2.54;
- older ranking/B+/MCE/live semantics.

`FOOTBALL_COVERAGE_AIRTABLE.md` also still declares Football v0.2.54 in active-looking header/workflow text.

But current authority and Step-3 prompt require `Model Version = Football A`.

Because these files are in the canonical load order, this is not harmless archival text. It can create version/persistence drift and revive superseded semantics.

---

## 4. High under-specification findings

### HIGH 1 — H2H has verdict power without a deterministic protocol

Current active stack requires recent same-venue H2H before O3.0+ and permits mechanism-compatible H2H suppression to contribute to B+ vetoes.

Still undefined:

- recency window;
- minimum/maximum sample;
- same-manager/personnel era;
- promotion/relegation/class-transferability;
- same-venue vs all-venue weighting;
- scoreline vs mechanism evidence;
- missing-H2H behavior;
- exact burden reduction;
- exact soft-penalty vs hard-veto threshold.

H2H must become a dedicated Step-3 compiler gate.

### HIGH 2 — XI integrity has no deterministic pass threshold

The stack uses:

- `ATTACKING DEPTH PRESERVED`;
- `COHESION / ROUTE DAMAGE`;
- "confirmed XI remains clean enough";
- "materially preserves the route/mechanism";
- "equivalent senior attacking quality".

Those labels can change EGE, carrier, B+, upper-tail and final exposure, but there is no fixed role/mechanism checklist with required pass count or hard role-loss rule.

### HIGH 3 — post-XI chance-quality hardening is not compiled

Step 1 now has a deterministic CQ/REP/MECH/CTX compiler.

Step 3 can still newly classify:

- strong chance quality;
- 4+ total path;
- elite two-sided path;
- current suppression;
- conversion stability;

using older qualitative rules.

This reintroduces subjectivity after PRE even though PRE itself is now deterministic.

### HIGH 4 — upper-tail gate remains qualitative

A2 exposure may depend on:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH`;
- `ELITE TWO-SIDED PATH`.

But the Step-3 stack has no single deterministic compiler for those three states.

### HIGH 5 — market-undercut override evidence is under-defined

A severe undercut can be restored only with:

- a "specific football-led explanation";
- "independent corroboration".

Those are sensible requirements, but neither `specific` nor `independent corroboration` is operationally defined.

Because the result can change HOLD to direct eligibility, this needs exact semantics.

### HIGH 6 — frozen-PRE alignment and current-PRE execution fit are conflated

The current prompt compares market center to frozen PRE for anti-circularity, then Carrier Market Decomposition may create a separate market-calibrated current PRE.

There should be two immutable fields:

- `FROZEN_PRE_MARKET_ALIGNMENT`;
- `CURRENT_PRE_EXECUTION_FIT`.

Without this split, a run may re-evaluate alignment against the newly market-informed burden while another keeps the frozen comparison only.

### HIGH 7 — ordinary B+ carrier caution can silently re-add the hardener removed by B+ Protected-Line

The B+ exact-burden patch says no extra positive hardener is required when the six core gates clear.

Later Carrier Market Decomposition says ordinary B+ carrier-led direct exposure at the protected line requires "stronger carrier failure-resistance."

That phrase is not defined as merely a negative-veto check vs a new positive hardener.

The exact-burden B+ lane therefore remains vulnerable to inconsistent HOLD/LOCK decisions.

---

## 5. Medium / stale-authority findings

1. `CURRENT_MODEL.md` decision-order/output sections still list generic HMA official paths despite Decay-First supersession.
2. `FOOTBALL_BETTING_PROCEDURE.md` still contains MCE/EGE/v0.2.54-era decision-order language as active-looking current procedure.
3. Expired Sep-19/20 temporary execution text remains in `02_NORMAL_CHAT_XI_ODDS.md`.
4. HMA file body still contains removed priority-inversion/direct-execution concepts below its supersession notice.
5. `weather/data faults` is allowed as a market-conflict explanation without a canonical source/freshness/effect rule.

---

## 6. Deterministic replay suite

| Branch | Expected unique result under a coherent current model | Current replay |
|---|---|---|
| exact supported burden, price >=1.65, all football gates clear | DIRECT -> OFFICIAL LOCK | PASS |
| exact supported burden, price <1.65 | WAIT — PRICE BELOW FLOOR | PASS |
| ordinary A1/A2 market +0.25 above frozen burden | Decay-First should define one result | **FAIL: WAIT vs HMA direct** |
| ordinary A1/A2 market +0.50 above frozen burden | Decay-First should define one result | **FAIL: WAIT vs HMA direct/plan** |
| severe market undercut | re-screen, no instant lock absent explicit override | PASS to re-screen; override threshold under-specified |
| B+ exact protected burden, six gates clear | B+ DIRECT -> OFFICIAL | PASS |
| B+ +0.25, VERIFIED carrier | one canonical action required | **FAIL: DIRECT extension vs Decay-First WAIT** |
| ELITE/EXTREME carrier decomposition clears | Carrier current-PRE exception before WAIT | PASS |
| EGE clears with post-XI burden above frozen PRE | one canonical action required | **FAIL: EGE DIRECT vs Decay-First WAIT** |
| high market + weak/pass frozen PRE | mandatory football/carrier re-screen; market alone cannot promote | PASS |
| intact XI vs mechanism-damaged XI | deterministic current state required | **FAIL: XI integrity threshold under-specified** |
| post-XI research unavailable after attempted search | process may continue with explicit limitation | PASS |
| suppressive recent same-venue H2H + current suppression | stronger negative effect expected | **FAIL: exact veto/burden rule missing** |
| suppressive H2H without current corroboration | no H2H-only hard veto | PASS directionally, but O3+ burden effect still under-specified |
| open H2H + current football suppression | current mechanism should dominate | PASS directionally |
| just-started quote, no predeclared plan | SHADOW/opportunistic live unless exception | **FAIL: fast path can TAKE NOW** |
| score changes before finalization | old quote VOID; new epoch/reprice | PASS |
| Decision State succeeds, Website Pick fails | PERSISTENCE SYNC FAULT | PASS |

Replay failures: **8 / 18**.

---

## 7. Correct Step-3 repair architecture

The prior recommendation is confirmed, but the full-surface audit makes the required compiler broader.

Create:

`models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`

as the sole compiled Step-3 operational authority.

Required fixed order:

`FROZEN PRE TRACE -> IDENTITY/STATUS -> XI ROLE-MECHANISM MATRIX -> POST-XI FOOTBALL RESEARCH -> H2H/MATCHUP GATE -> CURRENT CQ/FAILURE UPDATE -> MARKET HISTORY -> FROZEN_PRE_MARKET_ALIGNMENT -> EGE/CARRIER CURRENT-EPOCH COMPILER -> CURRENT_PRE_EXECUTION_FIT -> BURDEN AUTHORITY -> B+/UPPER-TAIL GATES -> DECAY/REACHABILITY -> PRICE -> PROVISIONAL/FINAL VERDICT -> PERSISTENCE TRANSACTION`

It must explicitly resolve:

1. whether EGE can still raise current supported burden after Decay-First;
2. generic HMA = audit/monitoring only vs any surviving official lane;
3. B+ +0.25 vs Decay-First;
4. exact B+ protected-line precedence;
5. H2H recency/transferability/effect;
6. XI mechanism-preservation thresholds;
7. post-XI chance-quality/upper-tail compiler;
8. frozen-PRE market alignment vs current-PRE execution fit;
9. carrier-decomposition exception boundaries;
10. just-started predeclared-plan check before any TAKE;
11. provisional fast verdict vs publishable final verdict;
12. current Football A Decision-State schema/version;
13. one canonical Step-3 state taxonomy.

This is primarily a **PROCESS COMPLIANCE COMPILATION**. Any choice that changes the substantive eligibility of EGE, B+ +0.25, HMA, H2H veto threshold, or another predictive/exposure boundary must be isolated and classified under the model-QA procedure as PROCESS FIX vs MODEL CHALLENGER.

---

## 8. QA conclusion

The repaired QA framework successfully found material Step-3 gaps that the earlier contradiction-only audit missed.

The correct overall state is:

`QA FAIL — CONTRADICTORY AUTHORITY + UNDER-SPECIFIED DECISION SURFACES`

not:

`QA INCOMPLETE`

because this re-audit achieved complete input coverage: all 46 material surfaces were inventoried and traced.

Do not trust Step 3 to be fully repeatable across chats until the compiled execution spec resolves the failed replay branches above.
