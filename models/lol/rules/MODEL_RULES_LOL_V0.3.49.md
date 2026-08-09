# MODEL RULES — LEAGUE OF LEGENDS v0.3.49

**Status:** Active delta  
**Effective date:** 2026-08-10 01:27 UTC+7  
**Supersedes:** v0.3.48 only where stated

## Purpose

Correct the Total Kills and same-map correlation errors exposed by KC vs FNC Game 2.

Confirmed positions under v0.3.48:

- Under 27.5 total kills @1.955 — LOSS (-0.25u)
- FNC +13.5 kills @2.122 — WIN (+0.2805u)

Final: KC 20-8 FNC at 31:53, 28 total kills, KC +12 kill margin.

Review: `models/lol/reviews/KC_FNC_GAME2_TOTAL_KILLS_CORRELATION_REVIEW_2026-08-10.md`.

The central correction is:

> **For Total Kills, observed pace is not future pace. Project future forced contact and lethality explicitly. For same-map add-ons, total-kill volume and signed kill margin are separate random variables and must be priced jointly rather than treated as generically correlated.**

v0.3.48 Draft-to-Conversion / KCV / Structure Substitution / NKB / RFI controls remain active. v0.3.47 Draft Primacy, v0.3.44 symmetric handicap pricing, v0.3.45 Duration, v0.3.42 lineup/team-strength controls and all retained execution rules remain active unless superseded below.

---

## 1. Total Kills Must Separate State From Mechanism

Current kill count and recent kills/minute are **state variables**. They are not sufficient evidence that the remaining map will be low- or high-kill.

Every Total Kills evaluation must separately model:

1. **Observed Kill Pace (OKP)** — what has happened so far;
2. **Forward Contact Inventory (FCI)** — how many future matchup-functional contact windows remain;
3. **Contact Lethality (CL)** — how many deaths are likely when those contacts occur.

A low OKP cannot positively support or upgrade an Under unless FCI and CL are also low enough.

A high OKP cannot positively support or upgrade an Over if the map is moving toward a clean terminal close with little FCI remaining.

---

## 2. Observed Kill Pace (OKP)

Record:

- current total kills;
- kills/minute from game start;
- kills added since prior synchronized snapshot;
- whether recent fights were 1-for-0, 2-for-0, 2-for-1, 3+ kills, or traded;
- whether kills were repeatable mechanisms or isolated anomalies.

Classify OKP:

- `LOW`;
- `MEDIUM`;
- `HIGH`.

### Quiet-start non-persistence rule

Before 15:00, a low current kill count or low kills/minute **cannot by itself** increase Under probability.

An Under upgrade before 15:00 requires at least one of:

- >=2 synchronized snapshots showing both low OKP and declining/limited FCI;
- repeated contact resolving with low CL because disengage/peel is demonstrably functioning;
- a clear structure-only/clean-close branch that removes future contact windows faster than it creates them.

`Quiet so far` is never equivalent to `quiet later`.

---

## 3. Forward Contact Inventory (FCI)

FCI replaces generic counting of objectives as fights.

For each remaining window, estimate whether **actual contact is likely** and whether either team can reliably force it.

Relevant windows include:

- dragon / soul-point / soul;
- Baron / Elder;
- inhibitor/base defense;
- side-lane collapse;
- repeat-pick cycles;
- forced face-check / vision denial;
- terminal chase after a won fight;
- cross-map response where the defender cannot safely concede.

Classify every meaningful window:

- `FORCED / HIGH-CONTACT`;
- `LIKELY CONTACT`;
- `AVOIDABLE / TRADEABLE`;
- `STRUCTURE-ONLY PLAUSIBLE`;
- `UNLIKELY BEFORE END`.

Do not count an objective as a fight merely because it exists on the map.

---

## 4. Contest Compulsion

A trailing team can become **more** kill-generating as the map worsens because it loses the option to concede indefinitely.

Flag **Contest Compulsion (CC)** when:

- leader controls vision/chokes/objectives;
- trailer is approaching soul, Baron, inhibitor or terminal-map pressure where conceding materially worsens win probability;
- trailer must walk into enemy control or defend fixed terrain;
- leader has reliable access once the trailer enters contest range.

When CC is active:

- increase FCI;
- increase Over branches if CL is medium/high;
- do not assume poke/waveclear/global tools suppress kills unless they actually allow the trailer to avoid or safely exit contact.

Structure pressure can therefore **increase Total Kills** through compulsory contests even while it **reduces favorite kill-handicap margin** through return kills and faster map compression.

---

## 5. Contact Lethality (CL)

For each high-contact window, estimate expected death production using the Draft Function Matrix.

Relevant CL inputs:

- reliable first contact;
- point-and-click / near-guaranteed target access;
- hard-CC chain length;
- damage continuation after first contact;
- chase / cleanup;
- re-engage;
- disengage / peel;
- mobility / escape;
- return-kill capability;
- terrain/choke amplification;
- current role-level gold concentration.

Classify CL:

- `LOW` — contact often disengages or resolves 0-1 deaths;
- `MEDIUM` — normal 1-3 kill fights/trades;
- `HIGH` — first contact frequently creates multi-kill continuation or unavoidable return-kill sequences.

### Access / disengage mismatch

If the leader has reliable hard access and the trailer lacks functional disengage after first contact, increase CL even when the trailer draft is nominally poke, waveclear or side-lane oriented.

Do not credit generic range as kill suppression if the ranged team cannot escape once engaged.

---

## 6. Total Kills Projection Formula Discipline

For every Total Kills market, explicitly project:

`Final Total Kills = Current Kills + kills from remaining FCI windows + low-contact residual kills`.

Internally produce at minimum:

- low final-kill branch;
- central final-kill branch;
- high final-kill branch;
- probability of line crossing;
- uncertainty width.

The projection must answer:

1. How many meaningful contact windows remain?
2. Which are forced versus avoidable?
3. What is CL in those windows?
4. Does map acceleration remove windows, or create compulsory defense windows first?
5. Are return kills likely even if the leader wins cleanly?

---

## 7. Under-Specific Vetoes

An Under cannot be TAKEN or positively upgraded merely because:

- current kills are low;
- towers are low;
- the leader has Grubs/Herald;
- one or both drafts have side-lane, poke or waveclear tools;
- the leader can theoretically win through structures.

### Hard-access Under surcharge

For a pregame or early-live Under, if all are true:

- one side has >=1 highly reliable hard-access tool plus follow-up;
- the opposing side has weak functional disengage after first contact;
- >=3 meaningful future objective/base-defense windows are likely;

then add **+2pp** to the normal Total Kills lower-bound requirement.

This surcharge stacks with the existing v0.3.46 gates but does not exceed a total required cushion of +9pp over break-even.

### Forced-contact veto

If FCI contains >=3 `FORCED / HIGH-CONTACT` windows and CL is `HIGH`, Under defaults to PASS unless the line is sufficiently high that the lower-bound probability still clears the applicable gate after explicit kill-window arithmetic.

---

## 8. Over-Specific Discipline

Do not overcorrect toward Overs.

An Over still requires enough remaining time/contact inventory and must account for:

- one-sided clean close;
- structure cannibalization;
- Baron ending the map without another full fight;
- objective trades;
- low CL despite frequent contact.

High FCI with LOW CL is not an automatic Over.

---

## 9. Total Kills and Kill Handicap Are Separate Axes

Define:

- `T = favorite kills + underdog kills`;
- `M = favorite kills - underdog kills`.

Project T and M separately.

Examples:

- high T, low/moderate M: traded fights / return kills;
- low T, high M: clean one-sided kill conversion;
- low T, low M: structure-heavy controlled map;
- high T, high M: true kill cascade.

A Total Kills position cannot be used as direct evidence for a Kill Handicap position without mapping the relevant T/M branch.

Likewise, a +kills handicap can remain strong in a map where the Under is weak because traded fights raise T while keeping M inside the cushion.

---

## 10. Same-Map Add-On Joint Distribution

When two same-map positions are considered, do not apply a generic correlation label such as `high positive` based only on narrative similarity.

For positions A and B, estimate the four-cell joint outcome matrix:

- `P(A win, B win)`;
- `P(A win, B lose)`;
- `P(A lose, B win)`;
- `P(A lose, B lose)`.

Before approving an add-on, identify at least one concrete scenario for each materially non-zero one-win/one-loss branch.

### Total Kills + underdog +kills example

Potential branches:

- both win: low total + moderate favorite margin;
- Under wins / +kills loses: low total but nearly all kills belong to favorite;
- Under loses / +kills wins: traded/high-contact game with return kills;
- both lose: high total + favorite kill cascade.

The KC-FNC G2 result was `Under loses / +kills wins`.

### Correlation pricing rule

Each add-on must independently clear its market gate **and** remain +EV after joint-distribution adjustment.

Do not double-count the same mechanism as two independent edges.

No stake escalation is permitted because two correlated positions qualify.

---

## 11. KC vs FNC Game 2 Calibration

### Pregame Under 27.5 @1.955

The model classified KC as Pick-and-Reset + Side-Lane/Structure and FNC as poke/waveclear/global. That correctly described map-conversion possibilities but incorrectly inferred low Total Kills too strongly.

Missing factors:

- Vi supplied reliable hard access;
- Renata extended contact;
- Kalista converted lead into cleanup/objective pressure;
- FNC lacked strong full disengage after engagement;
- future objective/base-defense windows were numerous;
- trailing FNC eventually had to contest rather than concede indefinitely.

Correct v0.3.49 interpretation: **PASS pregame Under 27.5 @1.955 unless the explicit OKP/FCI/CL projection still clears the higher hard-access Under gate.**

### 10:48 state

KC 5-1 FNC, +1.9k, towers 0-0, dragon 1-0, KC 3 Grubs.

The old process said the Under thesis strengthened because only six kills existed near 11 minutes.

Correct v0.3.49 interpretation: **do not upgrade Under from kill count alone.** FCI remained substantial and CL was at least medium because KC had reliable access and FNC weak disengage.

### FNC +13.5 @2.122

This remains a correct TAKE under v0.3.48/v0.3.49. KC still needed +10 additional net kills to beat the line. Final margin +12 validated handicap survival despite the Total Kills Over branch materializing.

---

## 12. Mandatory Total Kills Internals

Before every Total Kills TAKE, internally lock:

1. current kills and line-cross arithmetic;
2. OKP state;
3. FCI list and classification;
4. Contest Compulsion status;
5. CL state;
6. access/disengage mismatch;
7. clean-close vs compulsory-contest branches;
8. low/central/high final-kill distribution;
9. exact break-even;
10. lower-bound probability after uncertainty and all surcharges.

If OKP is the primary reason for an Under but FCI/CL are not established, PASS/HOLD.

---

## 13. Mandatory Same-Map Add-On Internals

For every add-on, internally lock:

1. standalone edge for the new market;
2. existing open position thesis;
3. shared mechanisms;
4. independent mechanisms;
5. T/M relationship if Total Kills and Kill Handicap are involved;
6. four-cell joint outcome matrix;
7. correlation-adjusted lower-bound edge;
8. unchanged stake size.

If the add-on qualifies only because the existing position narrative is reused, PASS.

---

## 14. Review Window

For the next **10 settled v0.3.49+ Total Kills positions**, record:

- entry clock;
- current kills;
- OKP;
- FCI count by class;
- Contest Compulsion;
- CL;
- access/disengage mismatch;
- low/central/high final-kill range;
- entry probability range/lower bound;
- final total kills;
- whether late contact exceeded early pace expectation;
- result and ROI.

For the next **10 same-map add-ons involving Total Kills + Kill Handicap**, also record the predicted and realized T/M quadrant and which joint-outcome cell occurred.

Audit for:

- excessive Under bias from quiet starts;
- undercounted forced-contact inventory;
- over-crediting poke/waveclear as kill suppression;
- generic correlation penalties that miss one-win/one-loss branches.

---

## 15. Retained Controls

- Draft remains the most important post-lock conditional mechanism layer.
- v0.3.48 Kill Handicap conversion framework remains active.
- v0.3.44 signed-margin symmetry and handicap surcharges remain active.
- Existing Total Kills lower-bound gates remain active: +5pp pregame, +4pp early live, +3pp mid/late, with v0.3.49 surcharges where applicable.
- Duration remains live-only under v0.3.45.
- Minimum odds remain 1.60.
- Default shadow stake remains 0.25u; actual exposure remains 0u while official betting is paused.
- Same-map add-ons remain enabled only when each independently qualifies and joint correlation is explicitly priced.
- No martingale, rescue, loss chasing or stake escalation.
- Missing decision-critical state => PASS/HOLD.

Where this delta conflicts with v0.3.48 Total Kills or same-map correlation interpretation, **v0.3.49 controls**.
