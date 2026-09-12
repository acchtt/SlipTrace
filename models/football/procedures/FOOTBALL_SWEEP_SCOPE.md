# Football Sweep Scope

**Status:** ACTIVE  
**Purpose:** Narrow fixture screening before Work so deep research is spent only on plausible Over environments.  
**Fixture authority:** AiScore only  
**Timezone:** source timezone preserved at Step 0; ICT conversion later for scheduling

This file controls the operational scope of the daily AiScore sweep. It is a screening-scope layer, not a scoring-model patch. `CURRENT_MODEL.md` remains the higher authority if there is ever a direct conflict.

The league-level admission registry is:

`models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`

---

## 1. Core principle

The daily sweep is broad at discovery and narrow before Work.

`RAW AISCORE UNIVERSE -> SOURCE-TIME INTEGRITY -> MODEL QUALITY EXCLUSIONS -> LEAGUE ENVIRONMENT REGISTRY -> WORK HANDOFF`

The objective is to reduce Work usage. Work should not repeatedly deep-research large numbers of marginal domestic-league fixtures whose competition environment is already known to be poor or uncertain for the Over model.

**DISCOVER BROADLY; EXCLUDE WEAK ENVIRONMENTS EARLY; DEEP-RESEARCH NARROWLY.**

Small league size alone is not an exclusion reason. Goal-environment usefulness and data quality are what matter.

---

## 2. Apply the active model-quality exclusions first

Before league-environment admission, continue to exclude fixtures removed by the active senior-quality overlay, including:

- youth/Uxx, academy and junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- domestic lower divisions unless explicitly approved;
- very small/obscure weak-data environments;
- senior leagues whose data quality/coverage is too weak to support reliable cheap admission.

Use:

`SMALL / OBSCURE WEAK-DATA LEAGUE — SCOPE EXCLUSION`

where applicable.

These fixtures are excluded **before** the league registry's CONDITIONAL gate. Do not fetch recent-five statistics or run a cheap Over test merely to rescue an environment that already fails the quality/scope prerequisite.

A league being a national top flight does **not by itself** guarantee CONDITIONAL status.

The separate UEFA Youth League trial remains a manual user override until the repository explicitly promotes it into official scope.

---

## 3. League-environment admission

For senior domestic national leagues that survive the quality/data overlay, apply `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

### PRIORITY

Send to Work automatically.

### NORMAL

Send to Work automatically.

### CONDITIONAL

Only established, sufficiently covered professional senior top flights may reach this class.

Do not send the whole competition to Work.

Run only the cheap Step-0 admission test defined in the registry. If the fixture passes, send it to Work. If it fails or the required cheap evidence is not readily available, exclude it before Work as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

This is a scope decision, not a structural PASS.

Do not reinterpret a genuinely small/obscure weak-data league as CONDITIONAL just because it is not named elsewhere in the registry.

### LOW-GOAL EXCLUDE

Do not send to Work during the normal sweep. Use:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

Current examples include V.League 1, K League 1, and Argentina Liga Profesional / Primera División as defined in the registry.

### HARD EXCLUDE

Do not send to Work.

Current hard exclusions are:

- Finland — all domestic leagues, every tier/category;
- Japan — all domestic league competitions, every tier/category, effective 2026-09-12 ICT onward.

Use the applicable reason:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

or

`JAPANESE DOMESTIC LEAGUE — HARD EXCLUSION`

The Japanese rule is an explicit user scope directive. It excludes league play from the normal sweep; it does not by itself exclude Japanese domestic cups or senior continental fixtures involving Japanese clubs.

---

## 4. Nordic and Scottish survival rule

Do not accidentally remove useful northern-European leagues merely because they are smaller than the major five.

The registry currently keeps these directly actionable when the normal quality overlay is satisfied:

- Norway Eliteserien;
- Sweden Allsvenskan;
- Denmark Superliga;
- Iceland top flight;
- Scotland Premiership.

Finland remains the explicit Nordic exception and is hard-excluded for domestic league play.

---

## 5. Continental competitions and cups

The domestic-league registry does not automatically exclude senior first-team continental competitions or domestic cups.

Senior UCL, UEL and UECL remain actionable when they clear the active model. Other senior continental competitions and cups remain governed by `CURRENT_MODEL.md` and the normal quality overlay.

A club from a low-goal or hard-excluded domestic league is not automatically excluded when playing in an independently eligible cup or continental competition.

Weak/obscure cup or continental environments can still fail the quality/data overlay; senior status alone does not force admission.

---

## 6. Coverage accounting

AiScore discovery does not need exact one-by-one enumeration of every raw excluded fixture before Work readiness.

Every fixture actually discovered and removed before Work should remain auditable with an explicit reason, including where applicable:

- `SMALL / OBSCURE WEAK-DATA LEAGUE — SCOPE EXCLUSION`
- `CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`
- `LOW-GOAL NATIONAL LEAGUE — EXCLUDED`
- `FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`
- `JAPANESE DOMESTIC LEAGUE — HARD EXCLUSION`
- the existing model-quality exclusion reasons.

Unenumerated blocks that are unambiguously youth/reserve/lower/amateur/regional/weak-data/hard-excluded may remain `raw_audit_complete=false` nonblocking gaps.

Only fixtures that survive all scope and quality gates enter the compact Work handoff.

---

## 7. Work-usage target

Do not optimize for sending the largest possible slate to Work.

A healthy run may discover 100+ raw fixtures but send only a fraction of them to deep research.

The intended behavior is:

`RAW AISCORE -> EARLY QUALITY EXCLUSION -> CHEAP CONDITIONAL FILTERING -> SMALL ACTIONABLE HANDOFF -> DEEP WORK SWEEP`

If a conditional fixture needs full match research merely to decide whether it deserves Work research, it has failed the purpose of the cheap gate and should remain excluded for that run.

If a weak/obscure league needs research merely to decide whether it deserves CONDITIONAL status, it is already outside normal Step-0 scope for that run.

---

## 8. Temporary override and registry maintenance

If the user explicitly asks to trial a normally excluded or conditional league, include it only for that requested run unless the repository is deliberately updated.

Do not promote/demote a league from one slate. Use league-level audits and repeated model evidence, then update `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md` once so later sweeps inherit the result cheaply.