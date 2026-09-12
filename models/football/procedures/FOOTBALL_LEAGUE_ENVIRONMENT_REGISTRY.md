# Football League Environment Registry

**Status:** ACTIVE  
**Purpose:** Reduce Work usage by deciding league-level admission before deep structural research.  
**Scope:** Senior domestic national leagues only.  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)

This registry is an operational cost-control layer. It does **not** decide bets and does **not** replace match-level structural research for fixtures that reach Work.

The goal is simple:

`AISCORE RAW UNIVERSE -> CHEAP LEAGUE ADMISSION -> SMALLER ACTIONABLE HANDOFF -> WORK DEEP RESEARCH`

Work should spend tokens on plausible Over environments, not on repeatedly proving that low-value domestic leagues are PASS.

---

## 1. Admission classes

### PRIORITY

Automatically eligible to enter the Work handoff when the fixture also clears the normal senior-quality rules.

These are leagues where the goal environment and/or recurring model usefulness justify regular deep screening.

### NORMAL

Automatically eligible to enter the Work handoff when the fixture clears the normal senior-quality rules.

These leagues are worth screening, but are not given any structural advantage merely because of league status.

### CONDITIONAL

Do **not** send the entire league to Work by default.

A fixture from a CONDITIONAL league may enter Work only when Step 0 can establish a cheap, current Over signal without deep research. Use AiScore-level fixture/team information or another already-cached registry note only; do not perform the full structural research here.

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

## 2. Current direct-to-Work registry

### PRIORITY

- Netherlands — Eredivisie
- Germany — Bundesliga
- Belgium — Belgian Pro League / First Division A
- Norway — Eliteserien
- Sweden — Allsvenskan
- Denmark — Superliga
- Iceland — Besta deild karla / top flight
- Austria — Bundesliga
- United States/Canada — Major League Soccer
- Australia — A-League Men

### NORMAL

- England — Premier League
- Spain — LaLiga
- Italy — Serie A
- France — Ligue 1
- Portugal — Primeira Liga
- Scotland — Premiership
- Switzerland — Super League
- Brazil — Serie A
- Mexico — Liga MX
- Saudi Arabia — Saudi Pro League

These classes control **admission to Work only**. They do not award a PRE grade, archetype, burden, or betting preference.

---

## 3. Current CONDITIONAL registry

Any senior domestic national league not listed as PRIORITY, NORMAL, LOW-GOAL EXCLUDE, or HARD EXCLUDE is **CONDITIONAL by default**.

Common examples include:

- Czech Republic — First League
- Poland — Ekstraklasa
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
- comparable smaller senior top flights not otherwise classified

Do not turn these examples into a hidden hard blacklist. A specific fixture may still reach Work if it clears the cheap conditional gate.

---

## 4. Current LOW-GOAL EXCLUDE registry

- Vietnam — V.League 1
- South Korea — K League 1
- Argentina — Liga Profesional / Primera División

These remain excluded from the normal daily Over sweep until a later league-level audit explicitly restores them.

Club nationality does not transfer the exclusion to continental or cup competition.

---

## 5. Current HARD EXCLUDE registry

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

## 6. Existing quality exclusions still apply first

The registry does not revive fixtures excluded by the active model quality overlay. Continue to remove youth/Uxx, reserve/development, amateur/semi-pro, regional/state/provincial, domestic lower divisions unless explicitly approved, and very weak/obscure data environments.

The UEFA Youth League remains a separate manual trial and is not made official by this registry.

---

## 7. Promotion / demotion policy

Do not move a league between classes because of one slate.

Use post-slate and league-level audits to update the registry when there is meaningful evidence. Useful signals include average goals, Over 2.5 frequency, scoreline distribution, bookmaker total baselines, and repeated model outcomes.

Changes should be written here once, so future daily sweeps benefit without repeating the same research.

---

## 8. Work-usage invariant

The raw AiScore universe may be large. That is acceptable.

The Work handoff should contain only:

`PRIORITY + NORMAL + CONDITIONAL fixtures that passed the cheap gate + separately eligible cups/continental fixtures`

It must not contain LOW-GOAL EXCLUDE, HARD EXCLUDE, or conditional fixtures that failed/no-data'd the cheap gate.

**DISCOVER BROADLY; DEEP-RESEARCH NARROWLY.**