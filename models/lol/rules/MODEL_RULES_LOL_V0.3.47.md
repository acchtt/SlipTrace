# MODEL RULES — LEAGUE OF LEGENDS v0.3.47

**Status:** Active delta  
**Effective date:** 2026-08-09 20:05 UTC+7  
**Supersedes:** v0.3.46 only where stated

## Purpose

Correct a live kill-handicap miss exposed by JDG vs WE Game 2. At 11:46, JDG led 6-4 with +2.9k gold, no tower advantage yet, and an economic lead across four of five roles. The live market offered JDG -9.5 kills @1.844. The model passed, over-crediting WE's nominal defensive resilience and underweighting the draft interaction that made JDG's lead highly convertible into a wide kill margin. Final: JDG 19-5 WE at 25:18.

Review: `models/lol/reviews/JDG_WE_GAME2_DRAFT_PRIMACY_REVIEW_2026-08-09.md`.

The correction is structural: **draft interaction is the primary conditional engine for how a live state converts into kills, margin, objectives and terminal pressure.** Team strength remains the pre-draft baseline prior; current synchronized state remains the live state variable. But once draft is locked, the model must not treat composition as a small cosmetic adjustment to a generic margin distribution.

v0.3.46 Total Kills controls, v0.3.45 Duration controls, v0.3.44 symmetric handicap controls, v0.3.42 lineup/team-strength controls and all retained execution rules remain active unless superseded below.

---

## 1. Draft Primacy Principle

### Pre-draft

Team strength, verified lineup, current-stage evidence and de-vigged market form the baseline map prior.

### Post-draft / live

Draft becomes the **primary mechanism layer** for projecting how a given gold/kill/objective state evolves.

For each market, ask:

`Given the current state, which composition can force, survive, convert and repeat the next sequence?`

Do not reduce draft to a flat `+/- X pp` adjustment once live state exists.

The same gold lead has different kill-margin implications depending on:

- reliable first contact;
- hard-CC density and reliability;
- anti-engage/disengage;
- target access;
- damage delivery after first contact;
- frontline stability;
- chase/cleanup;
- reset/re-engage;
- objective/choke control;
- waveclear/base defense;
- side-lane/global pressure;
- execution simplicity.

Current-map evidence can prove or disprove a draft mechanism, but it must be interpreted **through the matchup**, not separately from it.

---

## 2. Mandatory Draft Function Matrix

Before any post-draft TAKE in Moneyline, Kill Handicap or Total Kills, score both teams relative to each other on the following functions:

1. **Reliable first contact** — point-and-click or high-reliability engage, range, terrain dependence, flank dependence.
2. **Hard-CC density** — number of independent reliable hard-control layers, not raw champion count.
3. **CC reliability** — immediate vs conditional/delayed; single-target vs area; short-range vs long-range; easy vs high-burden execution.
4. **Anti-engage / disengage** — whether it actually stops the opponent's exact engage routes.
5. **Frontline access** — ability to damage or bypass tanks/bruisers.
6. **Backline access** — ability to reach primary carries without crossing prohibitive control.
7. **Carry protection** — peel, spacing, invulnerability/denial, reset routes.
8. **Damage continuation** — whether DPS can keep dealing damage after first contact.
9. **Chase / cleanup** — ability to turn one kill into multiple kills.
10. **Re-engage / repeat forcing** — ability to restart after initial disengage.
11. **Objective/choke control** — ability to force face-checks, hold entrances and secure follow-up.
12. **Waveclear/base defense** — whether it functions under dive, Baron, side-lane and engage pressure.
13. **Side-lane / global numbers** — ability to create unequal fights or overload assignments.
14. **Execution burden** — number of precise steps required for the composition's preferred fight.

Score each function as `material edge / slight edge / even / slight disadvantage / material disadvantage`.

A post-draft market recommendation is invalid if the model cannot explain the decisive functions behind the projected branch distribution.

---

## 3. CC Scarcity and Proactivity Tax

A trailing composition must not be called "resilient" merely because it has durability, waveclear or peel.

Apply a **CC Scarcity / Proactivity Tax** when the trailing team has:

- zero or one reliable hard first-contact source; or
- most control is conditional, delayed, short-range or defensive-only; and
- the leader has two or more reliable independent initiation layers plus follow-up damage.

Effects:

- reduce trailing-team comeback forcing;
- reduce its ability to choose favorable objective fights;
- reduce its positive-handicap resilience;
- increase leader's repeat-pick and chase branches;
- increase leader's `+10/+15` kill-margin tail when already ahead.

### Durability is not control

A durable frontline champion does not by itself provide:

- reliable initiation;
- backline protection;
- disengage;
- target denial;
- comeback forcing.

Do not convert "hard to kill" into generic handicap resilience.

---

## 4. Lead x Draft Interaction

Live handicap pricing must explicitly combine **where the economic lead sits** with **what the draft can do with it**.

### Distributed Economic Dominance

When role-level gold information is available, count how many roles the current favorite leads.

Flag **Distributed Economic Dominance (DED)** when:

- favorite leads economically in at least **4 of 5 roles**; and
- the total gold lead is material for the clock; and
- at least one engage/control role and one primary damage role are ahead or functionally online.

Suggested material-gold reference points, not hard standalone gates:

- around `>=2.5k` by 15:00;
- around `>=3.5k` by 18:00;
- around `>=5k` by 22:00.

If role-level gold is unavailable, do not invent DED from team gold alone.

### DED interaction rule

DED expands the favorite wide-margin tail **only when the draft has a credible conversion mechanism**: reliable engage, target access, objective control, chase/cleanup, or repeated forced contact.

If the trailing draft instead has demonstrated disengage, superior waveclear under pressure, anti-dive or reliable counter-initiation, DED expansion must be reduced.

---

## 5. Draft-Dominance Cascade State

Flag **Draft-Dominance Cascade (DDC)** when all are true:

1. current favorite has a material live lead or DED;
2. favorite has a material edge in reliable first contact / hard-CC layering;
3. favorite has a material or slight edge in target access plus damage continuation;
4. trailing team has weak proactive forcing or a CC Scarcity Tax;
5. at least three meaningful future fight/pressure windows remain: dragons, Herald, Baron, soul, inhibitor/base defense or equivalent;
6. no demonstrated hard anti-cascade mechanism is functioning.

When DDC is active:

- move meaningful probability mass from close-favorite-win bins into `+10..14` and `15+` bins;
- do not let generic waveclear/frontline language cap the wide-win tail;
- price future objective fights as **leader-selected or leader-favored contact**, not neutral coin flips;
- explicitly price serial dependency: first pick -> objective -> deeper vision -> second pick -> structure/base access.

### Conditional wide-margin sanity check

If DDC is active and the model assigns

`P(favorite wins by 10+ | favorite wins) < 60%`,

it must identify at least **two independent, matchup-functional anti-cascade mechanisms** supporting that low estimate. Otherwise the distribution is presumed too compressed and must be recalculated upward.

This is a calibration guardrail, not an automatic 60% floor.

---

## 6. Early Favorite Handicap Fast Path

For an early-live favorite negative handicap, the model must perform an explicit fast-path check before defaulting to the underdog cushion.

Fast-path conditions:

- favorite already controls the map economically;
- DED or equivalent broad control is present;
- DDC is active or nearly active;
- current handicap still sits **inside** the projected cascade tail rather than beyond it;
- enough fight/objective inventory remains for margin expansion;
- exact price clears the existing v0.3.44 lower-bound surcharge.

If these conditions are met, a favorite -H can qualify even when the raw additional net kills required initially look large.

**Arithmetic is not a veto.** "They still need +8/+9 more net kills" is not a reason to PASS when the distribution says the branch is common.

The v0.3.44 surcharge remains active; v0.3.47 changes how the probability distribution is built, not the threshold itself.

---

## 7. Underdog Resilience Must Be Mechanistic

For a positive handicap, credit resilience only if the trailing composition can plausibly reduce the leader's high-margin tail through the exact matchup.

Require concrete mechanisms such as:

- reliable disengage that stops the leader's primary engage;
- waveclear that remains functional under dive/Baron/side-lane pressure;
- anti-dive or peel that protects the actual damage carriers;
- counter-initiation that punishes repeated first contact;
- long-range damage that can be delivered safely while retreating;
- objective contest that does not require losing face-checks;
- credible return-kill mechanics during chase/base defense.

Do not count:

- durability alone;
- theoretical waveclear that cannot be safely cast;
- peel that only protects one target against multi-axis engage;
- conditional CC that the trailing team cannot reliably start with;
- scaling if the carries cannot access fights safely.

---

## 8. Draft Asymmetry Is Market-Specific

Draft primacy does not mean the same draft edge is copied into every market.

- **Moneyline:** ask whether the composition increases the probability of winning the map.
- **Kill Handicap:** ask whether it changes the conditional final-margin distribution, especially wide-win/close-loss tails.
- **Total Kills:** ask whether it increases forced contact, multi-kill amplification, cleanup and return-kill inventory.
- **Duration:** continue to require observed live conversion/stall evidence under v0.3.45; draft remains a mechanism prior, not sufficient duration evidence.

A draft can support favorite -kills while simultaneously making a Total Kills Under worse.

---

## 9. JDG vs WE Game 2 Calibration

### Draft

JDG: Olaf / Jarvan IV / Syndra / Ezreal / Nautilus  
WE: Dr. Mundo / Xin Zhao / Viktor / Lucian / Milio

### 11:46 synchronized state

- JDG 6-4 WE;
- JDG +2.9k gold;
- towers 0-0;
- WE 1-0 dragons;
- role-level economy favored JDG in top, jungle, mid and ADC;
- largest role leads were jungle and mid;
- JDG -9.5 kills @1.844;
- WE +9.5 kills @1.912.

### Draft interaction

JDG had:

- Nautilus reliable first contact;
- Jarvan independent initiation/displacement;
- Syndra immediate burst/control follow-up;
- Olaf run-through pressure into limited stop tools;
- Ezreal safe follow-up and cleanup;
- simpler sequence from first contact to multi-kill/objective control.

WE had:

- Mundo durability but little proactive hard control;
- Xin conditional close-range knock-up rather than reliable long-range first contact;
- Viktor zoning/delayed control;
- Milio primarily defensive peel;
- Lucian no hard control;
- limited ability to force JDG off preferred objective/engage states once behind.

The previous model over-credited Mundo/Viktor/Milio as generic resilience and underweighted WE's lack of reliable proactive CC.

### Corrected 11:46 margin read

A defensible reconstructed range is approximately:

- `P(JDG final margin >=10)` ~60-67%;
- break-even for JDG -9.5 @1.844 = 54.23%;
- early-live v0.3.44 surcharge requires lower bound ~60.23%.

With DED + DDC evidence, JDG -9.5 is at or just through the qualifying gate.

**Correct process verdict under v0.3.47: TAKE — JDG -9.5 kills @1.844.**

Final was JDG 19-5, margin +14. The final confirms the mechanism but is not used as the reason for the corrected live verdict.

---

## 10. Mandatory Live Draft Reassessment

Re-run the Draft Function Matrix when any of the following occurs:

- >=2k meaningful gold swing;
- role-level lead becomes broadly distributed or concentrated;
- first tower / material Herald opening;
- dragon/soul alignment changes contest incentives;
- first Baron;
- >=2 net-kill swing;
- a supposed disengage/waveclear/anti-dive mechanism repeatedly fails;
- the leader demonstrates repeated first-contact-to-objective conversion.

Do not keep the same draft-resilience label after the map proves it false.

---

## 11. Review Window

For the next **10 settled v0.3.47+ kill-handicap positions**, record:

- draft first-contact edge;
- reliable hard-CC layer count;
- CC Scarcity Tax status;
- target-access edge;
- execution-burden edge;
- DED status and role count;
- DDC status;
- conditional `P(10+ | favorite wins)`;
- projected signed margin distribution;
- chosen side and line;
- final margin;
- result and ROI.

Also record **untaken calibration misses** when a line passed under the old framework would qualify under v0.3.47. These do not enter P/L.

Audit after 10 settled handicap entries for favorite/underdog directional skew. The goal is not a favorite quota; the goal is accurate draft-conditioned margin tails.

---

## 12. Retained Controls

- Team strength remains the pre-draft baseline prior; verified lineup gate remains mandatory.
- Post-draft draft analysis is matchup-relative, not additive champion counting.
- v0.3.44 side-neutral signed margin distribution and probability surcharges remain active.
- v0.3.46 Total Kills forced-fight calibration remains active.
- v0.3.45 Duration live-only rebuild remains active.
- Position-blind reassessment remains mandatory.
- Minimum odds remain 1.60.
- Official wagering remains paused until explicit restoration.
- Default shadow stake remains 0.25u; actual exposure remains 0u.
- Same-map add-ons remain enabled only when each independently qualifies and correlation is priced.
- No martingale, rescue or loss-chasing logic.
- Missing decision-critical evidence => `PASS/HOLD`.

Where this delta conflicts with earlier draft/handicap interpretation, **v0.3.47 controls**.
