# Football v2.0 — Friend / Secondary Operator Handoff

**Snapshot:** 2026-09-20 ~02:40 ICT (UTC+7)  
**Repo:** `acchtt/SlipTrace`  
**Branch:** `main`

This file is written so a second operator can continue the same Football v2.0 workflow from the same repository **without relying on the original chat's memory**.

No credentials, tokens, or secrets are stored here. The operator still needs their own authorized access to GitHub/Airtable if they are expected to persist state.

---

## 1. Source of truth

Always read the upstream repo first. Do not work from old downloaded launchers, old handoffs, or remembered rules.

Start with:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/prompts/README.md`
3. the stage prompt being executed
4. all active rules declared by `CURRENT_MODEL.md`

The most important current execution patch is:

`models/football/rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`

The rule to remember is:

> **STRONGER STRUCTURE = MORE CONFIDENCE TO WAIT, NOT PERMISSION TO BUY A HIGHER TOTAL.**

If any older file appears to conflict with that principle on above-burden execution, the decay-first rule wins.

---

## 2. Active official track

Main official model: **Football A**  
Base: **v0.2.47 CLEAN**  
Immediate parent: **v0.2.55**

Model B may be run side-by-side, but it now also inherits the decay-first execution rule.

Important active patches include:

- shared A/B market alignment;
- Football A execution/exposure gate;
- predeclared live-decay execution;
- HMA, now subordinated to decay-first burden protection;
- no cross-match/same-window suppression;
- auto-publish user prematch odds;
- decay-first burden protection.

Read the exact active list from `CURRENT_MODEL.md` at runtime.

---

## 3. Critical execution correction — do not repeat the old mistake

The system recently drifted into this bad pattern:

`HIGH STRUCTURAL CONFIDENCE -> ACCEPT HIGHER TOTAL -> LOCK`

That caused high-ranked matches to absorb O3.25-O4.0 burdens while many lower-ranked protected O2.5/O2.75 candidates were held.

The corrected pattern is:

`STRUCTURAL QUALITY -> SUPPORTED BURDEN -> MARKET EXECUTION`

### Direct prematch exposure

A prematch lock is allowed only when:

- football/XI thesis remains valid;
- market alignment is clear or specifically explained;
- the selected line is **at or below the frozen supported burden**;
- price clears the active minimum;
- suppression/compression checks clear;
- the model-specific exposure gate clears.

### If current market is above supported burden

Use:

`WAIT — LIVE DECAY`

Freeze:

- target line = lowest acceptable supported burden;
- minimum acceptable price;
- current line/price;
- cancellation/state-integrity condition.

Examples:

- supported O2.75, current O3.25 -> **WAIT O2.75**
- supported O3.0, current O3.5 -> **WAIT O3.0**
- supported O3.0-3.25, current O3.75 -> normally wait for the lower independently supported burden, not the HMA boundary.

### HMA

HMA no longer grants automatic official prematch exposure above supported burden.

It may keep a strong A1/A2/CC+ fixture worth monitoring, but it may not raise the official entry target.

### Model B

Model B's +0.25/+0.50/+0.75 participation allowances also cannot create direct prematch exposure above the frozen supported burden.

Above-burden Model B cases become:

`MODEL B — QUALIFIED LIVE DECAY`

Model B exposure slots are counted only when a fixture is actually executable. Do **not** pre-reserve all slots for high-ranked fixtures still waiting for a better line.

---

## 4. WAIT versus HOLD

This distinction is mandatory.

- supported line available + price clears -> **LOCK / direct eligible**
- supported line available + price below floor -> **WAIT — PRICE BELOW FLOOR**
- current line above supported burden -> **WAIT — LIVE DECAY**
- football/XI/evidence itself remains materially insufficient -> **STRUCTURAL HOLD**
- frozen genuine PASS with no valid reopen -> **PASS**

Every WAIT shown to the user/operator must include:

- target line;
- minimum price;
- current line/price;
- cancellation condition.

A WAIT must not silently disappear.

---

## 5. O3.0+ burden check

Before any O3.0+ execution, explicitly re-screen:

1. recent same-opponent H2H;
2. recent **same-venue** H2H;
3. whether any low-total matchup pattern matches the current failure mechanism;
4. recent conversion stability;
5. independence of the second scoring route.

Do not let broad league reputation, long-run H2H, or a very high bookmaker total wash out a recent same-venue suppression pattern.

This correction was learned from:
- KR Reykjavik–Vikingur;
- Stuttgart–Dortmund.

---

## 6. Temporary Sep19-20 rule

Until **2026-09-21 00:00 ICT**, the temporary burden-specific upper-tail relaxation remains active:

- protected O2.5: a quality-proven **3+ total path** may be sufficient;
- protected O2.75: require a robust **3+ path + non-trivial fourth-goal support**;
- O3.0+: retain the strict 4+ / TRUE CC+ / elite two-sided standard;
- B+/B/PASS remain outside the automatic temporary relaxation.

Interaction with decay-first:

`QUALIFY THE LOWER PROTECTED BURDEN -> WAIT IF MARKET IS HIGHER -> EXECUTE ONLY WHEN THE PROTECTED BURDEN APPEARS`

The temporary early-conversion score-epoch logic is still active for eligible A1/A2 FOCUS cases. If a goal arrives before the 0-0 decay target, the old target expires and the new score epoch must be re-priced. Never chase the expanded goal line mechanically.

---

## 7. Other permanent workflow rules

### No cross-match suppression

A valid fixture is not blocked because another higher-ranked match is active, waiting, or already exposed.

Structural Rank orders review only.

### Auto-publish user prematch odds

User-supplied prematch Asian-total odds are treated as current/executable for that evidence epoch.

When all gates clear:

- finalize **OFFICIAL LOCK** immediately;
- create the Website Pick immediately;
- default 1u unless otherwise specified;
- do not ask a second “take it?” or “still available?” question.

### One exposure per match

Still mandatory.

### No retroactive backfill

Never turn a missed prematch/live opportunity into official P/L after the fact.

### AiScore fixture authority

AiScore remains the normal fixture-discovery authority. Other sources may research established fixtures but should not silently add new actionable fixtures.

---

## 8. Canonical workflow

The normal production flow is:

`NORMAL CHAT STEP 0 -> ZIP HANDOFF -> WORK STEP 1 -> NORMAL CHAT STEP 2 -> NORMAL CHAT STEP 3 -> WORK STEP 4 AUDIT`

### Step 0 — fixture discovery

Prompt:

`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

Permanent launcher:

`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first and follow the current active model. Execute now for the ICT window I request. Prove actionable_complete/work_ready; exact enumeration of already-excluded raw micro/youth blocks is best-effort. Return the Work handoff as AISCORE_FIXTURES_*.zip.`

Expected output is an `AISCORE_FIXTURES_*.zip` containing exactly one canonical root-level `AISCORE_FIXTURES_*.txt`.

### Step 1 — Work structural ranking

Prompt:

`models/football/prompts/01_WORK_DAILY_SWEEP.md`

Launcher:

`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first, then validate and extract the attached AISCORE_FIXTURES_*.zip before any deep research. Stop for an invalid package or actionable coverage/scope fault; do not rerun the fixture sweep or repair non-blocking raw-audit gaps.`

Step 1 is price/XI/market-history blind. It freezes structural PRE and ranking.

### Step 2 — confirmed XI + odds

Prompt:

`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

Launcher:

`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first, use my supplied XI/current odds as executable evidence, run the opening-to-prematch market-history watch, then execute immediately.`

Mandatory decision sequence:

`FROZEN PRE -> XI -> MARKET HISTORY -> CONFLICT CHECK -> FINAL XI -> BURDEN -> CURRENT MARKET -> MARKET ALIGNMENT -> DECAY-FIRST EXECUTION -> EXPOSURE DECISION`

### Step 3 — live review

Prompt:

`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Launcher:

`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and use my supplied live state/market. Execute immediately.`

A predeclared live-decay plan may become official when its target is reached under a clean state. Opportunistic unfrozen live bets remain non-official unless a separate exception is explicitly granted.

### Step 4 — post-slate audit

Prompt:

`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

Launcher:

`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the slate/date I specify from Airtable. Execute immediately.`

---

## 9. Airtable persistence

Base ID:

`appWyZJjitSBATXAU`

Tables:

- Coverage / Daily Sweep: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`

Important current model-control records:

- restored explicit WAIT process: `rec9vyKWtOrjgoOaY`
- decay-first patch: `recsrEGPeDCoEEEYH`
- Model B shadow audit: `recrDwaHCXLE9Izkx`
- Nordic false-positive audit: `recrAeaEMw5OLClhT`

These IDs do not grant access. The second operator needs their own authorized Airtable connection.

Search Airtable before reconstructing official history or current P/L.

---

## 10. Why the decay-first correction exists

At the time of the correction, settled Sep19 official locks included:

- KR–Vikingur O4.0 @1.71 -> LOSS
- ADO–Cambuur O3.0 @1.73 -> LOSS
- Molde–Aalesund O3.75 @1.67 -> LOSS
- Roma–Inter O2.75 @1.71 -> WIN
- Luzern–Grasshopper O3.5 @1.78 -> WIN
- Stuttgart–Dortmund O3.25 @1.66 -> LOSS
- Sparta–Heerenveen O3.25 @1.84 -> WIN

Settled subset: **3W–4L, -1.67u**.

A set of completed HOLDs at the same audit point had converted materially better at their protected burdens.

The takeaway is **not** “bet every HOLD.”

The takeaway is:

- stop letting higher structural confidence justify inflated goal burdens;
- keep qualified matches alive through explicit decay WAITs;
- preserve O2.5/O2.75 protection when the football supports it;
- treat O3.0+ as a materially more demanding burden.

---

## 11. Session state at this handoff

These states may have changed by the time the second operator reads this. **Revalidate match status before acting.**

### Existing official Website Picks created before decay-first patch

- Ajax–Excelsior — O3.5 @1.74, 1u
- Sevilla–Barcelona — O3.5 @1.76, 1u

Do not retroactively cancel or rewrite them because the execution rule changed afterward. Settle them normally from actual results.

### Last known active WAIT

Anderlecht–Zulte:
- frozen #13 B+ WATCHLIST / carrier-led;
- same-source bullish price hardener cleared the B+ positive gate;
- last known board: O2.5 @1.63 / O2.75 @1.79 / O3.0 @2.06;
- **WAIT target O2.5 >=1.65**.

Revalidate score/time/market before any execution.

### Last known structural HOLD/PASS examples

- Motor Lublin–Gornik: HOLD — same-venue suppression + weak secondary-route proof.
- KA Akureyri–Thor: HOLD — strong same-venue suppression + Nordic risk.
- Willem II–Fortuna: PASS — high-market conflict re-screen completed, but no valid carrier reopen.

### Potentially incomplete Step-2 item

- Sion–Zurich #10 A2 FOCUS appeared on the structural board, but no persisted XI/odds assessment had been found in the originating chat. Revalidate whether the match is still actionable before doing anything.

---

## 12. Nordic audit warning

Recent Nordic official sample logged at the time of audit:

- Fredrikstad–Sarpsborg O2.5 LOSS
- Djurgardens–GAIS O2.75 LOSS
- Vejle–Brondby O2.5 WIN
- KR–Vikingur O4.0 LOSS
- Molde–Aalesund O3.75 LOSS

Audit result: **1W–4L, -3.15u**.

This is an audit warning, not a blanket Nordic exclusion.

For Nordic candidates, explicitly verify:

- same-venue H2H;
- route independence;
- recent conversion stability;
- whether league-level scoring reputation is masking matchup-specific suppression.

---

## 13. Operating style

Use compact, operational outputs.

For each Step-2 match, show:

- frozen rank/tier;
- supported burden;
- XI state;
- market alignment;
- same-venue/H2H suppression result;
- current user board;
- final state: **LOCK / WAIT / HOLD / PASS**;
- if WAIT: exact target line + minimum price + cancellation condition.

Never hide a WAIT inside a generic HOLD.

Never treat a higher payout as compensation for a worse burden.

Never rewrite history because a result later looks obvious.

---

## 14. Fast bootstrap prompt for the second operator

Use this in a fresh chat:

> Continue the Football v2.0 workflow from repo `acchtt/SlipTrace`, branch `main`. Read `models/football/CURRENT_MODEL.md`, `models/football/prompts/README.md`, and `handoffs/football/2026-09-20-friend-operator-handoff.md` first. The decay-first rule is mandatory: structural strength does not justify a higher total; if the market is above the frozen supported burden, issue a LIVE DECAY WAIT at the protected burden. Revalidate all match statuses and Airtable states before acting. Do not retroactively rewrite earlier official bets.

---

## 15. Final warning

The specific mistake this handoff is designed to prevent is:

> **DO NOT TURN “BEST MATCH” INTO “HIGHEST TOTAL WE ARE WILLING TO BUY.”**

Use Structural Rank to decide what deserves attention.

Use supported burden to decide what is actually acceptable to bet.
