# Football Sweep Scope

**Status:** ACTIVE  
**Purpose:** Narrow fixture screening before Work by removing domestic league environments that are persistently poor fits for the Over model.  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)

This file controls the operational scope of the daily AiScore sweep. It is a screening-scope layer, not a scoring-model patch. `CURRENT_MODEL.md` remains the higher authority if there is ever a direct conflict.

---

## 1. Core principle

The sweep scope is based primarily on **goal-environment suitability**, not league size or prestige.

`RAW AISCORE UNIVERSE -> TIME INTEGRITY -> SWEEP SCOPE -> CURRENT MODEL ELIGIBILITY -> WORK`

Do not exclude a senior top-flight league merely because it is small. If its data quality is acceptable and its goal environment is suitable for the Over model, it may remain actionable under the normal model overlay.

Conversely, a major or recognizable league may be excluded when its league-wide scoring environment is persistently low and repeatedly produces poor Over conditions.

The purpose is to avoid spending deep Work research on competitions whose baseline frequently sits around or below the model's useful Over range.

---

## 2. Persistent low-goal national-league exclusion

The following senior domestic leagues are excluded from the normal daily Over sweep because they are currently treated as persistent low-goal environments:

- Vietnam — V.League 1
- South Korea — K League 1
- Argentina — Liga Profesional / Primera Division

These competitions remain in the raw AiScore universe for reconciliation but are classified before Work as:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

They must not receive FOCUS/WATCHLIST status or consume deep structural Work research during the normal sweep.

This is a **league-environment rule**, not a club-nationality rule. Clubs from these countries may still be assessed in continental competitions, cups, or other competitions that independently clear the active model rules.

---

## 3. How additional leagues enter the low-goal exclusion list

Do not expand the exclusion list casually from one bad slate or a short run of unders.

A league should be added only after a league-level audit shows a persistent low-scoring baseline across a meaningful sample, preferably using both current-season and recent historical evidence where available.

Useful audit signals include:

- average total goals consistently around or below 2.5;
- Over 2.5 hit rate consistently below a neutral 50% baseline;
- a high share of 0-0, 1-0, 1-1, 2-0 and similar low-total scorelines;
- bookmaker Asian-total baselines persistently centered near 2.0-2.25 rather than 2.5+;
- repeated model audits showing that apparent match-level Over candidates are being suppressed by the league environment.

No single signal is sufficient by itself. The decision should be made at league level and then written into this file so daily sweeps remain cheap and deterministic.

If a league later changes materially, it can be re-audited and restored.

---

## 4. Finnish hard exclusion

All Finnish domestic league competitions are excluded at every tier/category, men's and women's.

This remains a separate absolute rule and does not depend on the current scoring environment.

- Veikkausliiga: excluded
- Ykkosliiga / Ykkonen and lower: excluded
- Finnish women's domestic leagues: excluded
- reserve/development/youth Finnish leagues: excluded

Classify these as:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

Finnish Cup and senior continental matches involving Finnish clubs are **not** excluded solely because the club is Finnish; they remain subject to the current model's other competition-quality rules.

---

## 5. Existing model-quality exclusions remain active

The sweep scope does not restore competitions already excluded by the current model. Continue to apply the active senior-quality overlay, including exclusions for:

- youth/Uxx, academy and junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- domestic lower divisions unless explicitly approved;
- very small/obscure weak-data environments.

The separate UEFA Youth League trial remains a manual user override until the repository explicitly promotes it into official scope.

Important distinction: **small league size alone is not an exclusion reason under this scope file.** A small but credible, sufficiently documented and Over-friendly senior top flight may remain in the normal sweep unless another active model-quality rule removes it.

---

## 6. Continental competitions and cups

The low-goal domestic-league exclusion does not automatically transfer to other competitions.

Senior UCL, UEL and UECL remain actionable when they clear the current model. Domestic cups and other senior continental competitions remain governed by `CURRENT_MODEL.md` and the normal quality overlay.

A K League, V.League, Argentine, or Finnish club is not automatically excluded when playing in an independently eligible continental or cup competition.

---

## 7. Coverage accounting

AiScore discovery still records the complete raw fixture universe for the requested window.

Fixtures removed by this scope must remain auditable in the coverage ledger with an explicit exclusion reason:

- `LOW-GOAL NATIONAL LEAGUE — EXCLUDED`
- `FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

They must not be sent to Work, assigned FOCUS/WATCHLIST, or consume deep structural research.

---

## 8. Temporary override

If the user explicitly asks to trial or review a normally excluded low-goal league, include it only for that requested run and label it as a temporary scope override.

A one-off override does not modify the permanent scope and does not create precedent for later sweeps.
