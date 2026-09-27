# Football v0.2.50 — Extreme Goal Environment / Persistent High-Line Patch

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-10 ICT  
**Base:** Football v0.2.47 CLEAN + active v0.2.49 Two-Sided Priority patch  
**Shadow comparisons:** Football v0.2.47 CLEAN and Football v0.2.48-SHADOW remain unchanged

This patch fixes a specific execution failure discovered in the Sep 9–10 audit: some genuinely extreme goal environments never decayed into the model's preferred absolute total, so the model waited correctly under the old burden rule but missed matches whose true supported burden was higher than the frozen PRE estimate.

It does **not** make price a structural input, does **not** authorize chasing high totals, and does **not** weaken the protected-line principle for normal matches.

---

## 1. Core principle

The official order remains:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → CONFIRMED XI RERANK → GOAL BURDEN / REGIME → PRICE → LOCK / HOLD`

v0.2.50 adds a post-XI burden regime:

- `STANDARD` — normal protected-line logic;
- `EGE` — **EXTREME GOAL ENVIRONMENT**, where structure + team profile + confirmed XI independently support a materially higher goal burden.

`EGE` is **not** a PRE grade and **not** a new structural archetype. Frozen PRE remains frozen.

---

## 2. Why EGE exists

Do not assume that every strong Over should eventually decay to O2.75/O3.0/O3.25.

In a truly extreme environment, a stubbornly high market total can coexist with a valid Over thesis because:

- both teams can independently create multiple goals;
- an elite carrier has realistic self-funded 4+ capacity;
- the opponent still has a credible contribution route;
- suppression resistance is unusually weak;
- the confirmed XI preserves the high-end attacking structure.

The old failure was waiting indefinitely for an absolute line that the match's actual goal environment never justified offering.

---

## 3. EGE eligibility gate

A fixture may enter EGE only after confirmed XI.

### Normal eligibility

The fixture should normally be:

- **A1 FOCUS**; and
- `TWO-SIDED` or `ELITE CARRIER`.

### A2 exception

An **A2 FOCUS** may enter EGE only when all of the following are true:

1. the frozen structure is genuinely TWO-SIDED or an unusually strong ELITE CARRIER;
2. confirmed XI does **not** materially reduce attacking route quality;
3. any rotation still preserves credible senior creators/finishers and the intended attacking shape;
4. the main failure mode is not strengthened enough to make a 0-0 / 1-0 / 2-0 / 2-1 type result dominant.

A B+ WATCHLIST does not enter EGE merely because the market total is high.

---

## 4. Structural requirements for EGE

### TWO-SIDED EGE

Require all of:

- both independent scoring routes survive XI;
- at least one side has credible multi-goal / 3+ contribution capacity;
- the other side has a real scoring route, not merely theoretical leakage;
- team GF/GA, scoring-2+, conceding-2+, home/away or competition evidence supports a 4+ ceiling;
- suppression / sterile-possession risk is not the dominant failure mode.

### ELITE CARRIER EGE

Require all of:

- the carrier has repeatable self-funded 3+ capacity and a credible 4+ ceiling in this matchup;
- confirmed XI preserves the carrier's primary creators and finishers or equivalent attacking depth;
- either the opponent has a credible scoring route **or** the opponent's resistance is weak enough that 3-0/4-0/5-0 remains structurally realistic;
- the classic carrier slowdown branch after 1-0/2-0 is specifically evaluated and is not dominant.

Recognizable attackers or a famous favorite are never sufficient by themselves.

---

## 5. EGE burden re-open

Frozen PRE burden remains historical truth, but v0.2.50 allows a **new post-XI burden assessment epoch**.

When EGE clears, explicitly record:

- frozen PRE burden;
- EGE supported burden;
- why the higher burden is independently supported;
- whether the main failure mode has changed;
- whether the current market sits inside, above, or below the EGE burden.

The EGE burden may be materially above the frozen PRE band. This is allowed because it is a documented post-XI rerank, not a retroactive rewrite of PRE.

The bookmaker line may be used as a **calibration/consistency cue**, but never as the sole reason to raise the burden.

---

## 6. Persistent High-Line Acceptance

For a confirmed EGE match, the model no longer requires an arbitrary absolute target such as O3.0 or O4.0 if the independently supported EGE burden is higher.

### Direct EGE execution

If:

- the current Asian total is inside the EGE supported burden;
- price is at least 1.65;
- XI is confirmed;
- no material failure-mode veto is active;

then the match may be an **OFFICIAL LOCK before kickoff**. Do not wait for live decay merely because the headline total looks visually high.

### Relative-decay execution

If the current line is only **0.25 above** the EGE supported ceiling, HOLD for a relative quarter-line improvement rather than demanding a return to the old frozen PRE band.

If a 0-0 opening reaches roughly 8–15 minutes with no structural veto and the line remains unusually elevated, that persistence may corroborate the EGE calibration. It may not create EGE on its own.

---

## 7. No-chase rule remains absolute

An early goal that expands the total is **not** Persistent High-Line Acceptance.

After a goal:

- do not immediately raise the supported burden because the bookmaker did;
- wait for post-goal normalization;
- compare the normalized line against the already documented EGE burden;
- never chase a goal-driven expansion merely because the match looks open.

EGE fixes non-decay misses; it does not authorize score-driven chasing.

---

## 8. Standard matches remain unchanged

If EGE does not clear, use the normal v0.2.49/v0.2.47 protected-line policy:

- choose burden after structure + XI and before price;
- prefer the lowest protected line expressing the thesis;
- never stretch O2.5 → O2.75 → O3.0 merely to improve price;
- hard minimum odds remain 1.65, preferred 1.70+;
- a line above supported burden remains HOLD even at an attractive price.

---

## 9. Rotation interpretation

Do not treat all rotation as an automatic downgrade.

At XI, distinguish:

- `ROTATION — ATTACKING DEPTH PRESERVED`: replacement attackers/creators are senior-quality, roles remain coherent, and multi-route creation survives;
- `ROTATION — COHESION / ROUTE DAMAGE`: creators/finishers are removed without equivalent replacements, shape becomes less aggressive, or service quality materially weakens.

Only the second category is an automatic burden downgrade.

This is especially important in deep elite squads and cup/continental rotation contexts.

---

## 10. Audit labels

Use one of these labels for later review:

- `STANDARD DIRECT`
- `STANDARD DECAY`
- `EGE DIRECT`
- `EGE RELATIVE DECAY`
- `NON-DECAY HOLD`
- `GOAL-EXPANSION HOLD`

A final high-scoring result after `NON-DECAY HOLD` is not automatically a model error. Audit whether EGE should have been recognized from structure + XI **before** using the result as evidence.

---

## 11. Version boundary

v0.2.50 is prospective from 2026-09-10 ICT.

Do not rewrite historical v0.2.49 PRE grades, locks, holds or P/L. Historical missed opportunities may be tagged for audit, but official exposure remains exactly what was actually placed under the version active at the time.

Shadow v0.2.47 CLEAN and v0.2.48-SHADOW do not inherit this EGE patch unless explicitly versioned later.
