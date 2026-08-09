# MODEL RULES — LEAGUE OF LEGENDS v0.3.46

**Status:** Active delta  
**Effective date:** 2026-08-09 19:37 UTC+7  
**Supersedes:** v0.3.45 only where stated

## Purpose

Correct the Total Kills process failure exposed by BFX vs KRX Game 2, where **Under 31.5 kills @2.070** was recommended and confirmed pregame, then lost.

Review: `models/lol/reviews/BFX_KRX_GAME2_TOTAL_KILLS_REVIEW_2026-08-09.md`.

The main errors were:

1. treating organized objective fights as if they implied low kill generation;
2. under-applying the existing global/engage/cascade volatility reserve;
3. failing to inventory enough future forced-fight windows;
4. upgrading an Under while KRX held soul point despite BFX controlling the map;
5. treating Baron as automatically favorable to a Total Kills Under because it could shorten duration;
6. positively reassessing the position from a stale kill count after an objective-only update.

v0.3.45 duration rules, v0.3.44 symmetric kill-handicap rules, v0.3.42 team-strength/draft rules and all retained controls remain active unless superseded below.

---

## 1. Pregame / 0:00 Total Kills Probability Gate

Before any pregame / 0:00 Total Kills TAKE, lock:

1. projected final-kill low / central / high range;
2. probability mass of each branch;
3. functional fight-creation channel inventory;
4. unresolved forced-fight window inventory;
5. objective-forcing and base-defense kill reserve;
6. break-even probability;
7. reasonable selection probability range.

The **lower end** of the selection probability range must clear break-even by at least **+5 percentage points**.

If the lower bound does not clear +5pp => `PASS/HOLD`.

For live Total Kills, retain v0.3.40 thresholds unless superseded below:

- early live: lower bound > break-even by +4pp;
- mid/late live: lower bound > break-even by +3pp.

---

## 2. Functional Fight-Creation Channel Inventory

For every Total Kills market, count **functional and distinct** fight-creation/continuation channels across both drafts.

Examples include:

- point-and-click or highly reliable first contact;
- global / semi-global numbers creation;
- multi-axis engage or flank access;
- repeat/re-engage after initial disengage;
- displacement that creates a target-access window;
- safe ranged follow-up / cleanup;
- reset/chase mechanics;
- objective forcing that makes contact difficult to avoid;
- dive/base-entry tools;
- credible return-kill mechanisms during retreat/base defense.

Do not count champion names. Do not count multiple descriptions of the same functional sequence as separate channels.

### Channel interpretation

- 0-2 functional channels: low forced-contact inventory;
- 3: moderate;
- 4-5: high;
- 6+: very high.

For a Total Kills **Under**, 4+ collective functional channels create a mandatory volatility penalty. Six or more create a very-high-tail condition and require especially strong suppression evidence.

---

## 3. Forced-Fight Window Inventory

Before an Under TAKE, explicitly inventory future windows in which one or both teams are likely to be forced to contest rather than simply trade map state.

At minimum consider:

- remaining dragons;
- soul-point and soul fights;
- Elder;
- Herald when still relevant;
- first Baron and subsequent Baron cycles;
- inhibitor/base defense;
- exposed Nexus structures;
- cross-map states where one team cannot afford to concede the objective;
- series/map state only when it directly changes current-map contest incentives.

A high line is not sufficient evidence for an Under when many forced-fight windows remain.

### Objective-conflict accelerator

If **Team A leads materially in gold/map control while Team B owns soul point**, increase the high-kill branch. The next dragon is often structurally difficult for the leader to concede and difficult for the trailing soul-point team to ignore.

This state is an explicit anti-Under signal unless strong observed suppression evidence exists.

---

## 4. Pregame Under Surcharge in High Fight-Inventory Drafts

If both conditions hold at 0:00:

1. the drafts contain **>=4 functional fight-creation channels**; and
2. at least **three major forced-fight windows** are reasonably expected to remain,

then a pregame Total Kills **Under** must satisfy an additional **+2pp lower-bound surcharge**.

Therefore the lower probability bound must clear break-even by **+7pp** in this state.

This is not a permanent anti-Under bias. It is a high-tail reserve for drafts whose kill production can accelerate around inevitable objective contact.

If >=6 functional channels are present, widen the high-kill branch further and require explicit suppression evidence before using a narrow Under probability range.

---

## 5. Suppression Evidence for Unders

Theoretical control, waveclear, scaling or 'organized fights' is not enough to suppress the high-kill branch.

Credible suppression evidence includes:

- repeated objective contests ending with 0-1 deaths;
- repeated successful disengage/reset after first contact;
- demonstrated inability of either side to reach backline targets;
- clean cross-map objective trades that avoid combat;
- leader repeatedly converting structures without base-defense deaths;
- stable low kill generation across multiple meaningful contest windows;
- long-range zoning repeatedly preventing engage rather than merely delaying it.

Pregame Under estimates must remain wider when suppression is theoretical rather than observed.

---

## 6. Remaining-Kill Cushion Is Arithmetic, Not Evidence

For a half-kill Under line `H` and current total kills `K`, define:

`C = floor(H) - K`

where `C` is the maximum number of additional kills that can occur while the Under still wins.

Also calculate:

- number of unresolved forced-fight windows `W`;
- qualitative expected kill severity of each window;
- base-defense kill reserve;
- whether the current leader can end without another full contest cycle.

A large-looking cushion does not itself make an Under good. A small cushion late in a map is especially fragile when soul/Baron/base-defense fights remain.

If the Under has **<=4 kills of cushion** and at least one major forced contest or base-defense sequence remains, default to `INVALIDATED` for an existing position unless there is strong synchronized evidence of a near-terminal clean close with minimal defender contact.

---

## 7. Major Objectives Are Ambiguous for Total Kills

For Total Kills, first Baron, soul, Elder and inhibitor access must be repriced through two separate branches:

1. **clean-close branch:** objective compresses the game and reduces the number of future fights;
2. **kill-inflation branch:** objective creates forced base defense, chase, dive, staggered deaths or repeated re-entry kills.

Do **not** transfer Duration logic into Total Kills.

`Shorter expected duration != fewer expected kills`.

A major objective may improve a Duration Under while worsening a Total Kills Under.

---

## 8. Synchronized-Kill-State Veto for Total Kills Reassessment

For any live Total Kills position, the current total kill count is **decision-critical**.

If a user supplies an objective-only update, timer-only update, Baron/soul update or other state change without a synchronized current kill count:

- do not assume the previous kill count is unchanged;
- do not positively upgrade the Total Kills thesis;
- do not move `INVALIDATED -> DEGRADED/ACTIVE` or `DEGRADED/ACTIVE -> CONFIRMED`;
- fail closed and preserve or worsen the current thesis state until kills are synchronized.

A positive thesis upgrade requires a current kill count from the same or newer synchronized state.

This rule specifically prevents the BFX-KRX Baron reassessment error.

---

## 9. Total Kills CONFIRMED Upgrade Gate

For an existing Total Kills **Under**, `CONFIRMED` requires more than a large numeric cushion.

At least one of the following must be true:

- two independent observed kill-suppression mechanisms have persisted across meaningful fight windows;
- the live line has expanded enough that the lower probability bound materially exceeds the original entry threshold after full forced-fight repricing;
- the map is structurally near-terminal and the clean-close branch clearly dominates the base-defense kill-inflation branch.

Soul-point conflict, first Baron, or a gold lead alone cannot authorize `CONFIRMED`.

---

## 10. BFX vs KRX Game 2 Calibration

Draft:

- BFX: Renekton / Pantheon / Viktor / Jhin / Shen
- KRX: Gnar / Lee Sin / Annie / Miss Fortune / Nautilus

Entry:

- Under 31.5 kills @2.070;
- break-even 48.31%;
- stated model range 57-63%;
- confirmed 0.25u shadow;
- final result: LOSS.

### Corrected interpretation

The draft contained high/very-high collective fight inventory: Pantheon/Shen global numbers creation, Renekton access, Nautilus/Annie reliable first contact, Lee/Gnar secondary disruption and MF/Jhin follow-up.

The existing v0.3.40 volatility reserve should have been strongly active. A more defensible pregame Under range was roughly **49-55%**.

Because the high-fight-inventory Under surcharge would require the lower bound to exceed break-even by +7pp, the required lower bound was approximately **55.31%**.

The corrected lower bound did not reach that threshold.

**Under v0.3.46: PASS.**

At 20:50, BFX led the map while KRX held soul point. This should have widened the high-kill branch, not produced a CONFIRMED upgrade.

After the later Baron-only update, the current kill count was not synchronized. Under v0.3.46, a positive thesis upgrade was prohibited until a fresh kill total arrived.

---

## 11. Same-Map Add-Ons Enabled with Correlation Gate

Same-map add-ons are permitted in shadow mode without requiring a blanket no-add-on veto.

Every add-on must still:

- qualify independently under its own market-family gate;
- use the newest synchronized state;
- be logged as a distinct position;
- explicitly account for correlation with existing same-map positions;
- avoid rescue/chasing logic and automatic stake escalation.

Default individual shadow size remains 0.25u unless a later stake-policy revision changes it. Actual exposure remains 0u while official wagering is paused.

Correlation can reduce confidence or force a PASS, but correlation alone is no longer an automatic prohibition.

---

## 12. Review Window

Review after the next **10 settled Total Kills positions** entered under v0.3.46.

Track:

- Over/Under direction;
- pregame/early/mid-late entry phase;
- functional fight-creation channel count;
- unresolved forced-fight window count;
- soul-point conflict state;
- Baron/Elder/base-defense state;
- current kills and remaining Under cushion at entry/reassessment;
- low/central/high final-kill projection;
- probability range vs break-even;
- synchronized-state compliance;
- final total kills;
- result and ROI.

Do not relax the gate merely because fewer pregame Unders qualify.

---

## 13. Retained Controls

- v0.3.45 Duration remains live-only and independently modeled.
- v0.3.44 symmetric kill-handicap calibration remains active.
- v0.3.42 verified team-strength and matchup-adjusted draft controls remain active.
- v0.3.41 position-blind reassessment remains active.
- Minimum odds remain 1.60.
- Official wagering remains paused until explicit restoration.
- Default shadow stake remains 0.25u.
- No martingale, rescue or loss-chasing logic.
- Total Kills and Duration remain orthogonal.
- Current-map synchronized evidence overrides pregame narratives.
- Missing decision-critical information => `PASS/HOLD`.

Where this delta conflicts with v0.3.45 or earlier Total Kills controls, **v0.3.46 controls**.
