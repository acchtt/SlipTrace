# MODEL RULES — LEAGUE OF LEGENDS v0.3.48

**Status:** Active delta  
**Effective date:** 2026-08-09 23:48 UTC+7  
**Supersedes:** v0.3.47 only where stated

## Purpose

Correct two linked kill-handicap errors from G2 Esports vs Team Heretics:

- Game 1: G2 -11.5 @2.254 was taken from a strong draft/control state but lost by 0.5 kills because the model over-translated map dominance into kill-margin velocity.
- Game 2: TH +13.5 @2.336 correctly won, but the live thesis was incorrectly moved to INVALIDATED when G2 became overwhelmingly dominant on the map. The model conflated map-win probability with handicap-cover probability.

Review: `models/lol/reviews/G2_TH_KILL_HANDICAP_CONVERSION_REVIEW_2026-08-09.md`.

The central correction is:

> **Draft remains the primary post-lock mechanism layer, but kill-handicap pricing must separately model how the draft converts advantage: kills, structures, objectives, side lanes, or a mixture.**

v0.3.47 Draft Primacy, v0.3.46 Total Kills, v0.3.45 Duration, v0.3.44 symmetric handicap pricing, v0.3.42 lineup/team-strength controls and all retained execution rules remain active unless superseded below.

---

## 1. Draft Primacy Retained — Add Draft-to-Conversion Classification

After completing the v0.3.47 Draft Function Matrix, classify each team's most likely **conversion mode**.

Minimum categories:

1. **Fight Cascade** — repeated forced 5v5 or multi-kill sequences.
2. **Pick-and-Reset** — single pick -> objective/vision reset, not necessarily multi-kill.
3. **Side-Lane / Global Overload** — numbers creation, split pressure, cross-map structures.
4. **Objective / Structure Snowball** — towers, Herald/Grubs, Baron, inhibitors and map compression.
5. **Siege / Choke** — controlled space denial, structures before kills.
6. **Scaling Front-to-Back** — stronger later teamfights but not necessarily early margin acceleration.
7. **Mixed** — no single dominant conversion mode.

For Kill Handicap, every TAKE must answer:

`If the favored team wins from this state, what fraction of that winning branch is kill-centric versus structure/objective-centric?`

A strong draft edge may increase map-win probability while only modestly increasing final kill margin.

---

## 2. Kill Conversion Velocity (KCV)

Kill handicap requires an explicit live **Kill Conversion Velocity** assessment.

When at least two synchronized snapshots are available, preferably >=90 seconds apart, record:

- change in signed kill margin;
- change in team gold lead;
- change in towers/inhibitors;
- objective gains;
- whether fights ended 1-for-0, 2-for-0, 3-for-0+, or traded;
- whether the leader's first contact repeatedly created additional kills after the first target.

### KCV states

**HIGH**
- kill margin is expanding with the lead;
- leader repeatedly converts first contact into 2+ net kills;
- cleanup/chase is functioning;
- structures/objectives are following kills, not replacing them.

**MEDIUM**
- kill margin expands intermittently;
- fights produce mixed 1-for-0 / 2-for-1 outcomes;
- leader converts through both kills and structures.

**LOW / STRUCTURE-SUBSTITUTED**
- gold/structure control expands while kill margin is flat or slow;
- leader wins objectives without many kills;
- split/global pressure creates towers rather than repeated fights;
- Baron/inhibitor pressure is ending the map faster than it creates new net kills.

A single snapshot can establish a KCV prior from draft, but **wide favorite handicaps require stronger confidence than a draft-only KCV assumption**.

---

## 3. Structure Substitution / Kill Cannibalization

Map dominance is not equivalent to kill-margin dominance.

Flag **Structure Substitution (SS)** when any of the following are observed:

- team gold lead expands materially while signed kill margin is unchanged or only slightly larger;
- multiple towers/objectives are secured without corresponding net kills;
- side-lane/global pressure repeatedly converts into structures rather than fights;
- Baron/inhibitor control creates a plausible fast end with limited additional combat.

When SS is active:

- shift probability mass from extreme favorite-margin bins into medium favorite-win bins;
- reduce the assumption that every remaining objective creates a full fight;
- reduce favorite -10.5/-12.5/-13.5+ cover probability unless remaining forced-fight inventory is large;
- increase underdog +kills survival probability even when underdog map-win probability is near zero.

**Baron, inhibitors and towers can cannibalize future kills by shortening the game.** They are not automatically positive for a favorite kill handicap.

---

## 4. Net-Kill Burden vs Remaining Fight Inventory

For every kill-handicap evaluation, calculate the **Net-Kill Burden (NKB)**.

If favorite current margin is `m` and displayed favorite line is `-H`:

`NKB_favorite = minimum additional net kills required to finish above H`.

For an underdog `+H`, the same number measures how many additional net kills the favorite can gain before the dog stops covering.

Then compare NKB against **Remaining Fight Inventory (RFI)**:

- next dragon / soul-point / soul fight;
- Herald where relevant;
- Baron setup/fight;
- Elder setup/fight;
- inhibitor siege;
- terminal base defense;
- unavoidable side-lane collapse;
- any demonstrated repeat-pick cycle.

Do not count each objective as an automatic fight. Mark each window as:

- **forced/high-contact**;
- **likely but avoidable**;
- **structure-only plausible**;
- **unlikely to occur before end**.

### Core rule

A large NKB is not a veto by itself, but a favorite wide handicap requires a credible path from RFI to that many **net** kills.

If NKB is large and RFI is mostly structure-only or avoidable, compress the favorite wide-margin tail.

---

## 5. Wide Favorite Conversion Gate

For favorite handicap lines **-10.5 or wider**, DED/DDC alone is no longer sufficient.

A TAKE requires at least one of the following:

1. **Observed HIGH KCV** across synchronized snapshots; or
2. current NKB is **<=5** and at least one high-contact fight/base-defense sequence remains; or
3. at least **two high-contact forced windows** remain and the draft has demonstrated multi-kill cleanup/return-denial; or
4. an early-live v0.3.47 fast-path case where the line is still relatively cheap, DED + DDC are strong, and the favorite has not yet shifted into structure-substituted conversion.

### Slow-conversion veto

For -10.5 or wider, if across two synchronized snapshots:

- gold lead expands materially; and
- kill margin is flat or expands by <=1; and
- no repeated 2+ net-kill conversion is observed;

then favorite -H is **PASS/HOLD** unless NKB <=5 or two clear high-contact windows remain.

This rule is designed to preserve early JDG -9.5-type opportunities while preventing late overextension into G2 -11.5-type lines without demonstrated kill velocity.

---

## 6. Early Favorite Fast Path Refined

v0.3.47's Early Favorite Handicap Fast Path remains active, especially for lines around -5.5 to -9.5.

The fast path is strongest when:

- favorite has DED or equivalent broad control;
- favorite has DDC or near-DDC draft interaction;
- trailer has CC Scarcity / weak proactive forcing;
- favorite's lead sits on engage/control plus damage roles;
- current line is still inside the likely cascade tail;
- enough map remains for serial pick -> objective -> vision -> pick sequences.

For **-10.5 or wider**, additionally apply the Wide Favorite Conversion Gate above.

Do not respond to the G2 Game 1 miss by restoring generic underdog-cover bias. The goal is to distinguish **cheap early favorite lines with real cascade architecture** from **wide later lines requiring proven kill velocity**.

---

## 7. Handicap Survival vs Map Survival

For underdog +kills, explicitly separate:

- `P(underdog wins map)`;
- `P(underdog survives handicap | loses map)`.

A team can be strategically dead and still be a strong +kills position.

Positive-handicap survival can be supported by:

- return kills during lost fights;
- counter-engage after the leader dives;
- peel that saves one carry long enough to trade back;
- terminal base-defense kills;
- structure-substituted leader conversion;
- a large NKB relative to remaining fight inventory;
- leader composition that wins through side lanes/picks rather than repeated wipeouts.

Do not downgrade a +kills position merely because live Moneyline moves to 95-99% for the favorite.

---

## 8. Anti-Cascade Survival Is Graded, Not Binary

v0.3.47 correctly requires matchup-functional resilience, but v0.3.48 adds a graded interpretation.

A defensive mechanism may fail to stop the leader from winning while still reducing final kill margin.

Examples:

- Lulu/Orianna/K'Sante may fail to prevent tower loss but still produce return kills;
- waveclear may fail to stop Baron siege but delay long enough to avoid another full fight;
- frontline may die while buying time for carries to trade one kill back.

Therefore classify anti-cascade mechanisms as:

- **MAP-SAVING** — can plausibly reverse/stop the leader's map conversion;
- **MARGIN-SAVING** — unlikely to save the map but can reduce net kills;
- **NONFUNCTIONAL** — does neither in the actual matchup.

For Kill Handicap, MARGIN-SAVING tools matter even when Moneyline is effectively decided.

---

## 9. Thesis-State Discipline for Open Kill Handicaps

Existing position-blind definitions remain mandatory:

- ACTIVE: lower cover bound clears current buffer;
- DEGRADED: cover probability remains above break-even but below required buffer;
- INVALIDATED: current cover probability is at/below break-even or hard veto applies;
- CONFIRMED: materially stronger under current framework.

### New explicit prohibition

Do **not** move an underdog +kills position directly to INVALIDATED solely because:

- favorite reaches DED;
- favorite becomes 95%+ to win the map;
- favorite gains Baron/inhibitors;
- favorite has a large gold lead.

Those are inputs to a fresh signed-margin distribution. INVALIDATED requires the reprice itself to cross below break-even or a hard market-specific veto.

Likewise, do not mark a favorite -kills position CONFIRMED solely from map-control evidence if KCV is LOW/SS.

---

## 10. G2 vs TH Calibration

### Game 1

At 17:21:

- G2 5-2;
- +3.3k;
- towers 1-0;
- TH 3-0 dragons;
- G2 -11.5 @2.254;
- NKB = +9 additional net kills.

From 15:50 to 17:21 the kill margin remained +3 while the gold lead expanded. KCV was not HIGH.

**Correct v0.3.48 verdict: PASS — G2 -11.5 @2.254.**

Final 16-5, margin +11, confirms that the map could be dominant without producing enough kill margin.

### Game 2

At 12:16:

- G2 8-3;
- +3.5k;
- towers 0-0;
- TH +13.5 @2.336;
- NKB for G2 to beat the dog = +9 additional net kills;
- TH had K'Sante/Orianna/Lulu/Yunara margin-saving architecture;
- G2's lead was concentrated primarily on TF and Lucian.

**Correct v0.3.48 entry verdict remains TAKE — TH +13.5 @2.336.**

At 17:06:

- G2 11-3;
- +7k;
- towers 2-0;
- NKB remaining = +6 additional net kills.

DED/DDC made the position dangerous, but did not prove TH cover probability <=42.81% break-even.

**Correct thesis state: DEGRADED, not INVALIDATED, absent a fresh reprice below break-even.**

Final G2 17-7, margin +10; TH +13.5 won.

---

## 11. Mandatory Kill-Handicap Output Internals

Before any Kill Handicap TAKE, internally lock:

1. signed current margin;
2. displayed line and exact break-even;
3. NKB;
4. Draft Function Matrix;
5. conversion-mode classification;
6. DED / DDC / CC-scarcity status;
7. KCV state;
8. Structure Substitution status;
9. RFI by forced/avoidable/structure-only categories;
10. MAP-SAVING vs MARGIN-SAVING anti-cascade tools;
11. signed final-margin distribution;
12. lower-bound cover probability after uncertainty.

If any of 3, 5, 7, 8 or 9 is decision-critical and cannot be established, widen uncertainty and PASS/HOLD.

---

## 12. Review Window

For the next **10 settled v0.3.48+ kill-handicap positions**, record:

- side and line;
- current signed margin;
- NKB at entry;
- draft conversion mode;
- DED/DDC;
- KCV state;
- Structure Substitution status;
- number of high-contact RFI windows;
- MAP-SAVING and MARGIN-SAVING mechanisms;
- projected signed margin distribution;
- entry cover range / lower bound;
- final margin;
- whether the favorite won via kill cascade or structure/objective conversion;
- result and ROI.

Audit after 10 settled positions for:

- favorite vs underdog directional skew;
- overestimation of wide favorite tails;
- overreaction when dog positions are strategically dead but handicap-alive;
- missed early favorite lines before the market widens.

---

## 13. Retained Controls

- Draft remains the most important post-lock conditional mechanism layer.
- Team strength remains the verified pre-draft baseline.
- v0.3.44 signed-margin symmetry and surcharges remain active: +7pp pregame, +6pp early live, +5pp mid/late.
- v0.3.46 Total Kills controls remain active.
- v0.3.45 Duration controls remain active.
- Minimum odds remain 1.60.
- Default shadow stake remains 0.25u; actual exposure remains 0u while official wagering is paused.
- Same-map add-ons remain enabled only when each independently qualifies and correlation is priced.
- No rescue, martingale or loss-chasing logic.
- Missing decision-critical state => PASS/HOLD.

Where this delta conflicts with v0.3.47 Kill Handicap interpretation, **v0.3.48 controls**.
