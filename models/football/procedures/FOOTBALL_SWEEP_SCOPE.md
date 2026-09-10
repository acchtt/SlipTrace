# Football Sweep Scope

**Status:** ACTIVE  
**Purpose:** Narrow fixture screening before Work so deep research is spent only on plausible Over environments.  
**Fixture authority:** AiScore only  
**Timezone:** Asia/Ho_Chi_Minh (ICT)

This file controls the operational scope of the daily AiScore sweep. It is a screening-scope layer, not a scoring-model patch. `CURRENT_MODEL.md` remains the higher authority if there is ever a direct conflict.

The league-level admission registry is:

`models/football/procedures/FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`

---

## 1. Core principle

The daily sweep is broad at discovery and narrow before Work.

`RAW AISCORE UNIVERSE -> TIME INTEGRITY -> MODEL QUALITY EXCLUSIONS -> LEAGUE ENVIRONMENT REGISTRY -> WORK HANDOFF`

The objective is to reduce Work usage. Work should not repeatedly deep-research large numbers of marginal domestic-league fixtures whose competition environment is already known to be poor or uncertain for the Over model.

**DISCOVER BROADLY; DEEP-RESEARCH NARROWLY.**

Small league size alone is not an exclusion reason. Goal-environment usefulness and data quality are what matter.

---

## 2. Apply the active model-quality exclusions first

Before league-environment admission, continue to exclude fixtures removed by the active senior-quality overlay, including:

- youth/Uxx, academy and junior competitions;
- reserve/B-team/development competitions;
- amateur/semi-professional competitions;
- regional/state/provincial leagues;
- domestic lower divisions unless explicitly approved;
- very small/obscure weak-data environments.

The separate UEFA Youth League trial remains a manual user override until the repository explicitly promotes it into official scope.

---

## 3. League-environment admission

For senior domestic national leagues that survive the quality overlay, apply `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md`.

### PRIORITY

Send to Work automatically.

### NORMAL

Send to Work automatically.

### CONDITIONAL

Do not send the whole competition to Work.

Run only the cheap Step-0 admission test defined in the registry. If the fixture passes, send it to Work. If it fails or the required cheap evidence is not readily available, exclude it before Work as:

`CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`

This is a scope decision, not a structural PASS.

### LOW-GOAL EXCLUDE

Do not send to Work during the normal sweep. Use:

`LOW-GOAL NATIONAL LEAGUE — EXCLUDED`

Current examples include V.League 1, K League 1, and Argentina Liga Profesional / Primera División as defined in the registry.

### HARD EXCLUDE

Do not send to Work. Current Finnish domestic-league rule remains absolute and uses:

`FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`

---

## 4. Nordic and Scottish survival rule

Do not accidentally remove useful northern-European leagues merely because they are smaller than the major five.

The registry currently keeps these directly actionable when the normal quality overlay is satisfied:

- Norway Eliteserien;
- Sweden Allsvenskan;
- Denmark Superliga;
- Iceland top flight;
- Scotland Premiership.

Finland remains the explicit exception and is hard-excluded for domestic league play.

---

## 5. Continental competitions and cups

The domestic-league registry does not automatically exclude senior first-team continental competitions or domestic cups.

Senior UCL, UEL and UECL remain actionable when they clear the active model. Other senior continental competitions and cups remain governed by `CURRENT_MODEL.md` and the normal quality overlay.

A club from a low-goal or hard-excluded domestic league is not automatically excluded when playing in an independently eligible cup or continental competition.

---

## 6. Coverage accounting

AiScore discovery still records the complete raw fixture universe for the requested window.

Every fixture removed before Work must remain auditable in the coverage ledger with an explicit reason, including where applicable:

- `CONDITIONAL LEAGUE — NO CHEAP OVER SIGNAL`
- `LOW-GOAL NATIONAL LEAGUE — EXCLUDED`
- `FINNISH DOMESTIC LEAGUE — HARD EXCLUSION`
- the existing model-quality exclusion reasons.

Only fixtures that survive all scope and quality gates enter the compact Work handoff.

---

## 7. Work-usage target

Do not optimize for sending the largest possible slate to Work.

A healthy run may discover 100+ raw fixtures but send only a fraction of them to deep research.

The intended behavior is:

`RAW AISCORE -> CHEAP FILTERING -> SMALL ACTIONABLE HANDOFF -> DEEP WORK SWEEP`

If a conditional fixture needs full match research merely to decide whether it deserves Work research, it has failed the purpose of the cheap gate and should remain excluded for that run.

---

## 8. Temporary override and registry maintenance

If the user explicitly asks to trial a normally excluded or conditional league, include it only for that requested run unless the repository is deliberately updated.

Do not promote/demote a league from one slate. Use league-level audits and repeated model evidence, then update `FOOTBALL_LEAGUE_ENVIRONMENT_REGISTRY.md` once so later sweeps inherit the result cheaply.