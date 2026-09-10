# Football Sweep Scope

**Status:** ACTIVE  
**Purpose:** Narrow fixture screening before Work so small national leagues do not consume research time or appear on the actionable board.  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)

This file controls the operational scope of the daily AiScore sweep. It is a screening-scope layer, not a scoring-model patch. `CURRENT_MODEL.md` remains the higher authority if there is ever a direct conflict.

---

## 1. Core principle

The daily sweep should be deliberately selective.

`RAW AISCORE UNIVERSE -> TIME INTEGRITY -> SWEEP SCOPE -> CURRENT MODEL ELIGIBILITY -> WORK`

Do not send every senior top-flight national league to Work merely because it is technically professional or top division.

**SMALL NATIONAL LEAGUES ARE EXCLUDED BY DEFAULT.**

A smaller national league may only enter the actionable sweep when the user explicitly approves it for that run or the repository later adds it to the core set.

---

## 2. Core national-league set

The following senior domestic top flights are in the default national-league sweep scope:

- England — Premier League
- Spain — LaLiga
- Germany — Bundesliga
- Italy — Serie A
- France — Ligue 1
- Netherlands — Eredivisie
- Portugal — Primeira Liga
- Belgium — Belgian Pro League / First Division A
- United States/Canada — Major League Soccer
- Mexico — Liga MX
- Brazil — Serie A
- Argentina — Liga Profesional / Primera Division
- Japan — J1 League
- Saudi Arabia — Saudi Pro League

This is an explicit allowlist for **domestic national leagues**. Top-flight status alone does not make another national league actionable.

Examples normally excluded unless temporarily user-approved include Nordic leagues other than a separately approved competition, Korea K League, Australia A-League, China Super League, India ISL, Scotland Premiership, Austria Bundesliga, Switzerland Super League, Greece Super League, Czech First League, Poland Ekstraklasa, Serbia SuperLiga, Croatia HNL, Romania Liga I, and comparable smaller national leagues.

Do not infer permanent approval from a one-off historical review.

---

## 3. Finnish hard exclusion

All Finnish domestic league competitions are excluded at every tier/category, men's and women's.

This rule is absolute for the normal daily sweep and overrides any generic top-flight or core-league logic.

- Veikkausliiga: excluded
- Ykkosliiga / Ykkonen and lower: excluded
- Finnish women's domestic leagues: excluded
- reserve/development/youth Finnish leagues: excluded

Finnish Cup and senior continental matches involving Finnish clubs are **not** excluded solely because the club is Finnish; they remain subject to the current model's other competition-quality rules.

---

## 4. Existing quality exclusions remain active

The sweep scope does not restore competitions already excluded by the current model. Continue to exclude:

- youth/Uxx, academy and junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- domestic lower divisions unless explicitly approved;
- weak/obscure data environments.

The separate UEFA Youth League trial remains a manual user override until the repository explicitly promotes it into official scope.

---

## 5. Continental competitions

This national-league allowlist does not automatically exclude senior first-team continental competitions.

Senior UCL, UEL and UECL remain actionable when they clear the current model. Other senior continental competitions remain governed by `CURRENT_MODEL.md` and the normal quality overlay.

---

## 6. Coverage accounting

AiScore discovery still records the complete raw fixture universe for the requested window.

Fixtures removed by this scope must remain auditable in the coverage ledger with an explicit exclusion reason, preferably:

- `NON-CORE NATIONAL LEAGUE`
- `FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

They must not be sent to Work, assigned FOCUS/WATCHLIST, or consume deep structural research.

The user-visible board should therefore be smaller by design.

---

## 7. Temporary override

If the user explicitly asks to trial a normally excluded national league, include it only for that requested run and label it as a temporary scope override.

A temporary override does not modify this core set and does not create precedent for later sweeps.
