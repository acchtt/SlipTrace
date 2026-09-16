# Football A/B Shared Market-Alignment + Protected-Line Integrity Patch

**Scope:** Football A and Model B execution only.  
**Activation:** prospective from this commit.  
**Structural effect:** none. Frozen PRE rank, route states, supported burden and ceiling remain unchanged.

---

## 1. Purpose

This patch fixes a recurring execution error: treating a bookmaker total that is **lower than the model's frozen supported burden** as automatically safer/value and therefore as an instant-lock upgrade.

A lower Over line is mechanically more protected, but a materially lower **market center** can also be evidence that the model is overestimating the goal environment.

Therefore:

`LOWER LINE != AUTOMATIC VALUE`

and:

`PROTECTION != MARKET AGREEMENT`

This rule applies to both Football A and Model B before either model's model-specific execution overlay is considered.

---

## 2. Separate three concepts

For every current Asian-total board, distinguish:

1. **Best protected line** — the lowest acceptable Over burden.
2. **Best price** — the highest decimal return.
3. **Best execution** — the line/price combination that clears structural, market-alignment and model-specific gates.

Never call a higher total a "better line" merely because its price is higher.

Example:

- `O2.0 @1.69` is **more protected** than `O2.25 @2.01`;
- `O2.25 @2.01` has the **better price**, but also the higher burden;
- choosing O2.25 is a conscious burden concession, not an upgrade in line protection.

Price remains subordinate to burden protection after the football and market-alignment gates clear.

---

## 3. Determine the current market center

Do not compare frozen PRE against a cherry-picked alternate total.

Use the current **market center**: the primary Asian-total line around which Over/Under prices are most balanced, normally the displayed main total or the line nearest even pricing. Use adjacent alternate totals only to confirm the distribution.

Persist:

- current market center;
- Over/Under prices at that center when supplied;
- frozen supported range / ceiling;
- delta between market center and the relevant frozen structural reference.

If the board is ambiguous, mark `MARKET CENTER = UNCLEAR` and do not use a low alternate line to create an instant lock.

---

## 4. Market-alignment states

### 4.1 ALIGNED / NON-CONFLICT

Use when the current market center is broadly consistent with the frozen supported burden/range.

A protected alternate below the center may then be treated as genuine burden protection, subject to the model's normal exposure rules.

### 4.2 MARKET UNDERCUT — RE-SCREEN REQUIRED

Trigger when the market center is **0.25 goal or more below the lower edge of the frozen supported range** or, for a single-point burden, 0.25 or more below that frozen burden.

This is a bearish market disagreement, not an automatic bargain.

Before any instant/direct lock, re-screen for:

- hidden or newly confirmed attacking absences;
- tactical/formation suppression;
- competition incentive/state differences;
- opponent resistance or low-tempo matchup factors missed in PRE;
- stale/misleading recent-goal or leakage evidence;
- source/time mismatch;
- lineup quality or rotation not captured in the frozen structural read;
- other credible football-led reasons the market may be lower.

Until resolved:

`MARKET UNDERCUT — RE-SCREEN REQUIRED — NO INSTANT LOCK`

### 4.3 SEVERE MARKET UNDERCUT

If the market center is **0.50 goal or more below** the lower edge / single-point frozen burden:

- instant/direct lock is prohibited for both models;
- a specific football-led explanation plus independent corroboration is required even to restore direct eligibility;
- otherwise use HOLD / no exposure.

A low alternate total cannot override this state.

---

## 5. Direct-lock integrity gate

For both Football A and Model B, the old technical shortcut:

`CURRENT LINE <= SUPPORTED BURDEN + PRICE FLOOR CLEARS -> DIRECT`

is no longer sufficient by itself.

The new shared gate is:

`FROZEN STRUCTURE -> CONFIRMED XI -> CURRENT MARKET CENTER -> MARKET ALIGNMENT -> MODEL-SPECIFIC EXECUTION RULE -> EXPOSURE DECISION`

A direct/instant lock requires:

- frozen football structure still valid;
- XI integrity acceptable;
- market alignment `CLEAR`, **or** an explicit `MARKET UNDERCUT OVERRIDE — FOOTBALL EXPLAINED`;
- selected line clears the model's burden and price rules;
- all model-specific exposure gates clear.

If the market is materially below the model and the disagreement cannot be explained, the lower line is **not** promoted simply because it is easier to clear.

---

## 6. Watchlist / lower-rank protection

A market undercut may never upgrade structural quality.

In particular:

- B+ WATCHLIST cannot become an instant lock merely because the book offers O2.0/O2.25 below a frozen O2.5 burden;
- A2 WATCHLIST cannot become an instant lock merely because the offered total sits below its ceiling;
- a lower total removes burden but does not prove the match belongs among the best Over environments.

Model A's upper-tail and priority-inversion rules remain active.

Model B's participation lane remains active, but it also must pass this shared market-alignment gate before direct participation.

---

## 7. Upward market disagreement / rescue re-screen

The inverse disagreement also matters.

If a fixture is B/PASS, unsupported, or materially lower-ranked structurally but the current market center is **0.50+ above the model's implied burden** or is among the slate's clearly highest goal totals, do not automatically promote it. Instead trigger:

`HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN`

Recheck whether PRE missed:

- carrier depth;
- cross-league / class-gap scoring environment;
- competition-specific volatility;
- lineup quality;
- misleading suppression from a small recent-score sample;
- stronger two-sided chance quality than the initial route labels captured.

The market may force reinspection but cannot create structure by itself.

This rule exists to prevent a strong market disagreement from being silently discarded as an ordinary PASS.

---

## 8. Relationship to Football A HMA

Football A HMA remains unchanged in burden allowance.

Order becomes:

1. frozen structure;
2. XI;
3. market center / alignment;
4. if market is below structure, resolve undercut first;
5. if market is above structure, test HMA;
6. then upper-tail / priority-inversion / exposure gates.

HMA handles **high** market burdens. This patch handles both low-market undercut and high-market conflict/reinspection.

A lower market center cannot be interpreted as HMA protection or as an automatic official-value signal.

---

## 9. Relationship to Model B

Model B keeps its existing participation behavior, including its +0.25 participation allowance where otherwise valid.

This patch does **not** remove that lane.

It adds a shared precondition:

`MARKET ALIGNMENT = CLEAR / FOOTBALL-EXPLAINED OVERRIDE`

before a Model B instant/direct participation decision.

Thus Model B may remain more permissive than Model A on upward burden, but it may not treat a bearish market undercut as free value.

---

## 10. Line selection after alignment clears

Once a fixture clears structure, XI and market alignment:

`LOWEST ACCEPTABLE BURDEN -> PRICE FLOOR -> PRICE AS TIE-BREAKER`

Do not voluntarily add 0.25 goal burden merely to obtain a higher payout unless the model explicitly authorizes that burden and the user is told it is a **higher-risk price alternative**.

Preferred wording:

- `PROTECTED LINE: O2.0 @1.69`
- `HIGHER-PRICE / HIGHER-BURDEN ALTERNATIVE: O2.25 @2.01`

Never label the second line "better" without specifying that only its price is better.

---

## 11. Persistence

For every material A/B XI + odds review, persist when observable:

- frozen supported range / ceiling;
- current market center;
- market-center delta vs frozen lower edge / burden;
- `MARKET ALIGNMENT = CLEAR / UNDERCUT / SEVERE UNDERCUT / HIGH-MARKET CONFLICT / UNCLEAR`;
- re-screen reason/result;
- `MARKET UNDERCUT OVERRIDE = NONE / FOOTBALL EXPLAINED`;
- selected protected line;
- higher-price alternatives if relevant;
- final Model A decision;
- final Model B decision.

New exact labels:

- `MARKET UNDERCUT — RE-SCREEN REQUIRED`
- `SEVERE MARKET UNDERCUT — NO INSTANT LOCK`
- `MARKET UNDERCUT OVERRIDE — FOOTBALL EXPLAINED`
- `HIGH-MARKET CONFLICT — MANDATORY RE-SCREEN`

---

## 12. Audit

Track separately:

- undercut fixtures that were correctly rejected;
- undercut fixtures later overridden with football evidence;
- low-line instant-lock candidates prevented by this patch;
- high-market PASS/WATCHLIST fixtures reopened by mandatory re-screen;
- selected protected lines vs higher-price/higher-burden alternatives;
- Model A and Model B outcomes separately.

Historical decisions remain historical. Do not retroactively convert prior bets or P/L.
