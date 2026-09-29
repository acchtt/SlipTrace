# Football A — Remove Cross-Match / Same-Window Exposure Suppression

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-19 ICT  
**Scope:** Football A exposure selection only  
**Prospective:** Yes. Do not rewrite historical decisions or P/L.

---

## 1. Purpose

Football A no longer suppresses an otherwise valid official exposure merely because a higher-ranked candidate exists in the same practical kickoff/exposure window.

The former `PRIORITY-INVERSION GUARD` is removed as an exposure blocker.

Structural ranking remains useful for board ordering and audit, but it does **not** impose a one-bet-at-a-time, same-window, or cross-match exposure restriction.

---

## 2. Independent match execution

Each fixture is now decided on its own football and market evidence.

An official exposure may be approved whenever that fixture independently clears all applicable gates:

- actionable scope / league regime;
- frozen structural validity;
- XI integrity;
- market-history / market-alignment review;
- chance-quality / CC+ / failure-mode requirements;
- burden fit;
- HMA rules where applicable;
- Model A upper-tail requirement where applicable;
- price floor;
- any match-specific or session override rules.

A lower-ranked fixture is **not** blocked solely because a higher-ranked fixture is:

- still active;
- waiting for line decay;
- waiting for price;
- already executable;
- already exposed;
- in the same kickoff window.

---

## 3. What remains unchanged

This patch does **not**:

- promote B+ to A2;
- relax B+ positive-gate requirements;
- remove the A2 upper-tail gate;
- change HMA limits;
- change market-alignment rules;
- change one-exposure-per-match discipline;
- permit stacking multiple bets on the same fixture;
- make price a structural signal;
- alter frozen PRE ranks.

Cross-match comparison may still be shown for context, but it is advisory only and cannot block exposure.

---

## 4. Decision order

For Football A, exposure order becomes:

`STRUCTURAL VALIDITY → MARKET ALIGNMENT → UPPER-TAIL / ROUTE PROOF → BURDEN PROTECTION → PRICE FLOOR → EXPOSURE DECISION`

Do not use `PRIORITY INVERSION = BLOCKED` after this patch.

If a fixture is held, persist the fixture-specific blocker instead.

---

## 5. Persistence

For new decisions after activation:

- set `PRIORITY INVERSION = NOT APPLICABLE — PATCH REMOVED` when that field is retained for compatibility;
- do not use `NO BET — EXPOSURE HOLD — PRIORITY INVERSION GUARD`;
- do not suppress Website Picks because another match is ranked higher;
- keep Structural Rank unchanged for board ordering and audit.

Historical records that were previously blocked by priority inversion remain historical unless the user explicitly asks for a fresh reassessment at a current evidence epoch.

---

## 6. Authority

This patch overrides any conflicting same-window / cross-match exposure-suppression language in:

- `MODEL_RULES_FOOTBALL_A.md`;
- `MODEL_RULES_FOOTBALL_A_HIGH_MARKET_ACCEPTANCE.md`;
- `MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`;
- `02_NORMAL_CHAT_XI_ODDS.md`;
- `CURRENT_MODEL.md`.

All non-conflicting rules remain active.
