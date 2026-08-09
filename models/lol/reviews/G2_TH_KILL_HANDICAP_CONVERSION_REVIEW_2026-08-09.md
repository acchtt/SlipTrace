# G2 vs Team Heretics — Kill Handicap Conversion Review

**Date:** 2026-08-09  
**Series:** LEC 2026 Summer, G2 Esports vs Team Heretics  
**Model under review:** LoL v0.3.47  
**Purpose:** separate draft quality from kill-margin conversion speed and improve both favorite -kills and underdog +kills pricing.

---

## Executive conclusion

The series produced two complementary lessons.

1. **Game 1:** the draft read correctly favored G2, but the model over-translated draft superiority and map control into kill-margin velocity. G2 won 16-5 with +12k gold, 8-2 towers and two Barons, yet G2 -11.5 @2.254 lost by 0.5 kills. The map was dominant but relatively structure/objective-centric.
2. **Game 2:** the model correctly recognized that TH +13.5 @2.336 could survive a G2 map win because TH's draft retained real anti-cascade/return-kill tools and G2's early conversion was not fully distributed. The position won as G2 finished 17-7, margin +10. However, the 17:06 live reassessment incorrectly moved the position to INVALIDATED simply because G2 had +7k, 2-0 towers and an 11-3 kill score. That conflated map dominance with handicap failure probability.

The correction is not to reduce draft importance. **Draft remains the primary post-lock mechanism layer.** The correction is to add a second layer after draft: **how this draft converts superiority — kills, structures, objectives, side lanes, or a mixture.**

---

## Game 1 review

### Draft

G2: Vayne / Jarvan IV / Cassiopeia / Corki / Alistar  
TH: Ambessa / Skarner / Syndra / Viktor / Shen

### Entry state

At 17:21:

- G2 5-2 TH;
- G2 +3.3k gold;
- towers 1-0 G2;
- dragons 3-0 TH;
- G2 had broad role-level economic control;
- Vayne was heavily accelerated;
- G2 -11.5 kills @2.254;
- current margin +3, so G2 still needed +9 additional net kills to cover.

### What the model got right

- G2's draft had excellent punish into TH's commitment-heavy engage.
- Vayne/Cassiopeia/Alistar made failed Ambessa/Skarner/Shen entry highly dangerous.
- G2 were clearly more likely to win the map from the synchronized state.
- TH's three-dragon state created mandatory future contest pressure.

### What the model got wrong

The model treated those facts as sufficient evidence for a wide kill-margin tail.

But the previous synchronized snapshot at 15:50 was already G2 5-2, +2.8k, towers 1-0. By 17:21:

- gold lead expanded;
- kill margin did **not** expand;
- structure count did not materially expand;
- TH acquired another dragon;
- there was not yet demonstrated repeated 2-0 / 3-0 fight conversion.

The correct interpretation was: **G2 control was real, but kill-conversion velocity was not yet proven.**

Final:

- G2 16-5 TH;
- final margin +11;
- +12k gold;
- towers 8-2;
- Barons 2-0;
- G2 -11.5 lost by 0.5 kills.

The final is consistent with the pre-existing warning signal: G2 converted much of their superiority through structures, Barons and controlled closure rather than enough additional net kills.

### Correct process verdict

At 17:21, under the revised framework, **G2 -11.5 @2.254 should be PASS**, despite the attractive price, because the line was wide, the remaining net-kill burden was +9, and observed kill-conversion velocity had not validated the cascade assumption.

---

## Game 2 review

### Draft

G2: Twisted Fate / Xin Zhao / Akali / Lucian / Milio  
TH: K'Sante / Naafiri / Orianna / Yunara / Lulu

### Entry state at 12:16

- G2 8-3 TH;
- G2 +3.5k;
- towers 0-0;
- TH 1-0 dragons;
- G2 3 Grubs;
- strongest G2 role leads were TF and Lucian;
- TH +13.5 kills @2.336;
- current margin +5, so G2 still needed +9 additional net kills to beat the handicap.

### Why the entry was good

TH had matchup-functional anti-cascade tools:

- K'Sante front-line disruption;
- Orianna zone/counter-engage;
- Lulu peel and carry protection;
- Yunara protected scaling damage;
- Naafiri return access onto G2's carries.

G2's Grubs and TF side-lane pressure increased **structure conversion**, but did not automatically imply kill-margin acceleration. G2 were ahead, but the lead was not yet a clean 4-5-role DED state.

The positive handicap therefore had two independent supports:

1. large remaining net-kill burden for G2 (+9 additional net kills needed);
2. draft architecture capable of producing return kills or surviving enough fights to keep the final margin below +14.

### 17:06 reassessment error

At 17:06:

- G2 11-3 TH;
- +7k;
- towers 2-0;
- dragons 1-1;
- role-level economy favored G2 in all five roles.

The model changed TH +13.5 to INVALIDATED.

That was too aggressive. The current margin was +8, so G2 still needed +6 additional net kills. DED/DDC substantially increased danger, but it did **not** by itself prove that TH's cover probability had fallen below the original 42.81% break-even.

The position should have been **DEGRADED**, not INVALIDATED, unless a fresh signed-margin distribution actually priced TH cover at or below break-even.

### Final

- G2 17-7 TH at 26:19;
- final margin +10;
- +14k;
- towers 11-0;
- Baron 1-0;
- inhibitors 3-0;
- TH +13.5 covered by 3.5 kills.

This is the strongest evidence from the series that **structure dominance and kill-margin dominance are not interchangeable**. G2 destroyed the map structurally while failing to reach +14 kills.

---

## Combined lessons

### 1. Draft remains primary — but it must project a conversion mode

After the Draft Function Matrix, identify the likely favorite-win mode:

- fight-cascade / repeated multi-kill;
- pick-and-reset;
- side-lane/global overload;
- objective/structure snowball;
- siege/choke;
- scaling front-to-back;
- mixed.

A strong draft advantage does not automatically mean a large kill margin.

### 2. Separate map control from kill conversion

Gold, towers, Baron and win probability describe **map control**. Kill handicap requires a second variable: **net-kill conversion velocity**.

If gold/structures expand while kill margin stays flat, compress the favorite wide-margin tail unless there are clear upcoming forced-fight windows.

### 3. Structure conversion can cannibalize future kills

A leader that converts efficiently through towers, Baron and inhibitors may shorten the game and reduce the number of future fights required to end. This can help a positive handicap even while the underdog has almost no chance to win the map.

### 4. Wide favorite lines need conversion evidence

For favorite lines of -10.5 or wider, draft dominance + DED/DDC is insufficient by itself when the favorite still needs many additional net kills.

Require either:

- demonstrated margin expansion across synchronized snapshots; or
- a small remaining net-kill burden; or
- multiple near-mandatory 5v5/base-defense windows with strong favorite multi-kill mechanics.

### 5. Positive-handicap survival is different from map survival

The underdog can be strategically dead but still have a strong +kills position. Counter-engage, peel, return damage and terminal base-defense kills can preserve the handicap while the nexus is doomed.

### 6. Thesis states must be probability-based

DED/DDC is evidence, not an automatic INVALIDATED flag for an underdog +kills position.

- ACTIVE: lower bound still clears current buffer;
- DEGRADED: cover probability remains above break-even but no longer clears buffer;
- INVALIDATED: current reprice is at/below break-even or a hard veto applies.

Do not downgrade directly from ACTIVE to INVALIDATED merely because the favorite becomes overwhelmingly likely to win the map.

---

## Model action

Promote these lessons into LoL v0.3.48:

- mandatory Draft-to-Conversion classification;
- Kill Conversion Velocity tracking;
- Structure Substitution / Kill Cannibalization adjustment;
- Net-Kill Burden vs Remaining Fight Inventory gate;
- wide-favorite handicap conversion veto;
- explicit handicap-survival vs map-survival separation;
- stricter probability-based thesis-state transitions.
