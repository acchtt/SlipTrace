# BFX vs KRX Game 2 — Total Kills Review — 2026-08-09

**Position:** Under 31.5 total kills @2.070  
**Position ID:** POSTCB-SHADOW-11-P01  
**Stake:** 0.25u shadow / 0u actual  
**Result:** LOSS (-0.25u shadow)  
**Model at entry:** LoL v0.3.45

## Draft

BFX blue:

- Renekton
- Pantheon
- Viktor
- Jhin
- Shen

KRX red:

- Gnar
- Lee Sin
- Annie
- Miss Fortune
- Nautilus

## Entry thesis

The post-draft Under 31.5 @2.070 was recommended because the line was high and the analysis framed both teams as more likely to produce organized objective fights than continuous skirmishing. Break-even was 48.31%; the stated Under range was 57-63%.

That probability range was materially too high.

## Primary process failures

### 1. Organized fights were incorrectly treated as low-kill fights

The drafts contained numerous reliable fight-creation and continuation mechanisms:

- Pantheon point-and-click/global access;
- Shen global reinforcement;
- Renekton dive/target access;
- Jhin long-range follow-up;
- Nautilus point-and-click/reliable first contact;
- Annie hard engage/burst follow-up;
- Lee Sin displacement and re-engage;
- Gnar secondary engage/terrain pressure;
- Miss Fortune multi-target follow-up.

The correct variable was not whether fights were organized. It was how many future forced-fight windows remained and how reliably both compositions could create kills once those windows occurred.

### 2. Existing global/cascade reserve was under-applied

v0.3.40 already required a volatility penalty when the two drafts collectively contained four or more meaningful fight-creation channels. This map clearly met that condition, yet the entry estimate did not reserve enough probability for the high-kill branch.

### 3. Objective inventory was underpriced

The map still contained multiple unresolved kill-generating windows: dragons, soul-point/soul, Baron, and base defense.

At 20:50, BFX led 8-3 in kills and about +3.6k gold while KRX held three dragons / soul point. The Under was incorrectly upgraded to CONFIRMED. The combination of one team leading the map while the other controlled soul point made the next dragon structurally difficult to avoid and increased forced-fight probability.

### 4. Major-objective acquisition was treated as automatically Under-positive

After BFX secured Baron, the thesis was upgraded from INVALIDATED to DEGRADED because Baron could shorten the game.

That was an incorrect transfer from duration logic to total-kills logic. Baron can shorten clock duration while increasing base-defense kill volume. Major objective acquisition is therefore ambiguous for a Total Kills Under and must be priced through both clean-close and base-defense-kill branches.

### 5. Stale kill state was used during the Baron reassessment

The latest synchronized screenshot before the Baron-only update showed 19 total kills. The subsequent objective update did not include a synchronized current kill total, yet the reassessment continued using 19 as if it were current.

For a total-kills position, current kills are decision-critical. A thesis upgrade must fail closed when the kill count is stale or missing.

## Corrected entry interpretation

A more defensible pregame Under range was approximately 49-55%, not 57-63%.

At 2.070, that range did not justify a TAKE once forced-fight uncertainty and the high-kill tail were properly reserved.

**Correct process verdict: PASS.**

## Required fixes

1. Add a pregame/0:00 Total Kills probability gate.
2. Add a Forced-Fight Inventory Gate for Unders.
3. Count functional fight-creation channels, not champion names or repeated descriptions of the same combo.
4. Explicitly inventory future dragon/soul, Baron/Elder and base-defense fight windows.
5. Treat leader-vs-soul-point conflict as a forced-fight accelerator.
6. Treat Baron/soul as ambiguous for Total Kills Under; shorter duration is not automatically fewer kills.
7. Prohibit positive thesis upgrades when current kill count is not synchronized.
8. Require explicit base-defense kill reserve after major objectives.
9. Track remaining Under kill cushion against unresolved forced-fight inventory.
10. Review the next 10 settled Total Kills positions under the revised framework.
