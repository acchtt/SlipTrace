# MODEL RULES — LEAGUE OF LEGENDS v0.3.43

**Status:** Active delta  
**Effective date:** 2026-08-09 15:38 UTC+7  
**Supersedes:** v0.3.42 only where stated

## Purpose

Correct the live-duration calibration failure exposed by DK vs KT Game 1, where **Over 33 minutes @2.020** was recommended at 16:00 with KT leading 5-3 kills and +2.1k gold, despite a composition and game state capable of rapid post-14-minute structural conversion.

The error was not simply that the game ended under the line. The process over-weighted 0-0 towers, split dragons and theoretical defensive waveclear, while under-weighting:

1. the **remaining survival horizon** required for the Over to cash;
2. KT's **latent conversion architecture** before the first tower fell;
3. the fact that **absence of structures taken is not equivalent to observed stall**;
4. the high elasticity of post-plate tower cascades;
5. the large disagreement between the model's 59-66% Over estimate and the market's ~49.5% break-even without enough observed evidence.

All v0.3.42 team-strength, draft-function and handicap controls remain active.

---

## 1. Duration Is a Survival Event

For a duration Over at line `L` and current game clock `t`, define:

`remaining survival horizon R = L - t`

The modeled event is **the game surviving at least R more minutes**, not whether the current map merely "looks slow".

Before any duration TAKE, explicitly estimate:

- `P(finish before L)`;
- `P(finish shortly after L)`;
- `P(material extension beyond L)`;
- the central expected closing window.

The probability assigned to the Over must come from these survival branches.

A large `R` is high friction. If the game must survive **15+ additional minutes** from a midgame snapshot, theoretical scaling or current towerlessness is insufficient by itself.

---

## 2. Structural Absence Is Neutral, Not Stall

A 0-0 or low-tower state is **not affirmative Over evidence** unless there is observed evidence that structural conversion is being denied.

From 14:00 onward, especially after turret plates expire:

- towerlessness may simply mean the first structural break has not happened yet;
- the first tower can rapidly unlock side-lane access, deeper vision, objective setup and follow-up towers;
- multiple towers may fall in one conversion cycle.

Therefore:

**0-0 towers after 14:00 is neutral evidence by default.**

It becomes positive stall evidence only when supported by at least two independent observed stall signals from Section 4.

---

## 3. Latent Conversion Potential (LCP)

Before a live duration Over, score the currently advantaged team for the following six accelerants:

1. **reliable first contact** — point-and-click or otherwise high-reliability engage/pick;
2. **numbers creation** — globals, semi-globals, fast collapse, teleport/map mobility or cross-map reinforcement;
3. **safe follow-up damage** — ranged DPS, poke, chase or cleanup that can convert first contact into kills;
4. **wave/structure access** — side-lane pressure, strong wave push, siege, dive or fast turret damage;
5. **objective leverage** — ability to force dragon/Herald/Baron and turn the objective into structure access;
6. **opponent suppression** — the trailing side's waveclear, disengage or peel is functionally weakened by the leader's draft/state.

Set `LCP = number of credible accelerants`, after matchup-adjusted interaction testing.

Interpretation:

- **0-1:** low latent conversion;
- **2:** moderate;
- **3-4:** high;
- **5-6:** very high.

When `LCP >= 3`, do not infer a long game from missing towers alone.

When `LCP >= 3` **and** the leader has >=+1.5k gold between 14:00 and 18:00, an Over requiring >=15 additional minutes is `PASS/HOLD` unless at least two observed stall signals are already demonstrated.

When `LCP >= 4` and the leader has >=+2.0k gold in that window, assign a meaningful fast-close branch even with 0-0 towers.

---

## 4. Observed Stall Evidence

Theoretical defensive tools are not stall evidence until they work on the live map.

Qualifying observed stall signals include:

- two or more meaningful leader pushes neutralized without a tower loss;
- repeated waveclear visibly preventing structure access after the leader wins tempo;
- at least two failed engage/pick sequences by the leader that do not create objective or structural conversion;
- the leader's gold lead is stable or shrinking across synchronized snapshots despite having initiative;
- the trailing side repeatedly cross-maps objectives/structures after losing local priority;
- side lanes remain genuinely stable rather than merely untaken;
- the trailing team demonstrates repeatable disengage/reset that prevents second-wave chase;
- a Baron/Herald/major objective buff is acquired but produces little or no structural gain.

Purely theoretical statements such as "they have Taliyah waveclear," "they have Milio peel," or "dragons are split" do not qualify unless the mechanism has been observed functioning.

---

## 5. First-Break Elasticity Rule

Before taking an Over while few structures are down, model the **first structural break** as a regime-change event.

Required question:

> If the leading team gets the next pick, dragon fight, Herald/Baron access or first tower, how many additional structures can realistically fall before the defender fully resets?

If the answer is **two or more**, increase the fast-close branch.

If the leader has reliable pick -> numbers advantage -> objective -> structure routing, treat those events as serially dependent. Do not price each tower or fight as an independent low-probability event.

A map can move from 0-0 towers to decisive base access very quickly after the first break.

---

## 6. Duration Market-Divergence Sanity Gate

For any live duration market with visible odds, calculate the market break-even probability.

Compare the model's central probability to break-even:

- **0-5pp difference:** normal;
- **>5 to 9pp:** require at least two independent current-map reasons;
- **>9pp:** require at least three independent current-map reasons, including at least one **observed stall/acceleration** reason rather than draft theory.

If the evidence is absent, shrink toward the market and widen uncertainty.

A single descriptive feature such as 0-0 towers, split dragons, or waveclear cannot justify a >9pp disagreement.

---

## 7. Duration Probability Buffers

A live duration TAKE now requires an explicit probability range and the lower bound must clear break-even by:

- **+5pp** when current clock is before 18:00;
- **+4pp** from 18:00 through 24:59;
- **+3pp** from 25:00 onward.

These are minimum evidence buffers, not target edges.

If the range is wide enough that the lower bound fails the buffer, output `PASS` or `HOLD`.

---

## 8. Leader-State High-Friction Over Veto

For a live Over, apply a veto when all are true:

1. one team leads by >=+1.5k gold after 14:00;
2. the Over requires >=15 more minutes of survival;
3. the leader has `LCP >= 3`;
4. fewer than two observed stall signals exist.

The veto can be overridden only by exceptional synchronized evidence such as repeated failed conversions, severe composition-specific siege failure already observed, or a verified game-state mechanic materially delaying access.

This veto is independent of current tower count.

---

## 9. DK vs KT Game 1 Calibration

At the recorded 16:00 snapshot:

- KT led 5-3 kills;
- KT led by +2.1k gold;
- towers were 0-0;
- dragons were 1-1;
- no Baron/inhibitors;
- Over 33 minutes was 2.020, break-even ~49.5%;
- model estimated ~59-66% and recommended TAKE.

Draft:

- KT: Olaf / Pantheon / Ryze / Ezreal / Nautilus
- DK: Ambessa / Vi / Taliyah / Lucian / Milio

Under v0.3.43, KT had high latent conversion potential:

- Pantheon/Nautilus supplied reliable first contact;
- Pantheon/Ryze supplied numbers creation and fast collapse;
- Ezreal/Ryze supplied safe follow-up and chase pressure;
- Olaf reduced the reliability of conventional control as a stop mechanism;
- the +2.1k lead gave KT enough state advantage for one successful fight to unlock multiple structures.

DK's Taliyah/Milio defensive tools were theoretical at the entry snapshot; repeated stall had not been demonstrated.

The Over required roughly **17 more minutes** of survival. With `LCP >=3`, +2.1k gold, no observed stall sample and a model estimate >9pp above break-even, the correct v0.3.43 verdict is **PASS/HOLD**, not TAKE.

By 28:29, KT had converted to approximately +11k gold, 8-3 towers, 3-1 dragons, Baron, an inhibitor and a 14-4 kill lead, validating the missing cascade branch.

---

## 10. Mandatory Duration Output Discipline

Before any duration recommendation, internally lock:

1. current clock `t`;
2. duration line `L`;
3. remaining survival horizon `R`;
4. leader/defender state and gold trajectory;
5. latent conversion potential score;
6. observed stall signal count;
7. first-break elasticity / next conversion route;
8. fast / central / extension finish branches;
9. break-even probability;
10. model probability range and applicable buffer;
11. market-divergence sanity check.

Missing any decision-critical item => `PASS` or `HOLD`.

---

## 11. Retained Controls

All v0.3.42 controls remain active unless explicitly superseded.

Where this delta conflicts with earlier duration heuristics, **v0.3.43 controls**.
