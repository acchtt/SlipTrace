# SK vs VIT Series — Draft Calibration / Market-Anchor Failure Review

**Date:** 2026-08-10  
**Model at series start:** v0.3.51  
**Model after Game 1 patch:** v0.3.52  
**Status:** Review only; no automatic version promotion from this document

## Executive finding

The SK vs VIT series exposed a deeper issue than the Game 1 Viktor-specific terminal-threat error.

The model is systematically capable of identifying plausible draft mechanisms, but it is assigning too much probability mass to those mechanisms without sufficiently pricing:

1. team-strength / player-execution priors;
2. market information;
3. role/economy dependency of draft tools;
4. synchronization burden and failure cost;
5. underdog collapse / wide-margin tails;
6. within-series evidence about execution quality.

The result is **qualitative mechanism overconfidence**: the model can tell a coherent story for an underdog draft and then convert that story into an unjustifiably large numerical edge.

---

## Game 1

Confirmed position:

- SK ML @1.752, 0.25u shadow — LOSS (-0.25u)

Entry at 12:50:

- SK 5-2 VIT;
- SK +1.6k gold;
- towers 0-0;
- VIT 1-0 dragons;
- SK 2-1 Grubs.

Final user-authoritative result: VIT won. Latest grading frame: VIT 23-14 SK at 32:50.

User correction: SK threw the game and had no reliable answer to Viktor.

v0.3.52 correctly identified the missing Terminal Threat Answerability / adverse Execution Burden Gradient concept, but this was only part of the series-level failure.

---

## Game 2

Draft:

VIT blue — Aatrox / Lee Sin / Akali / Jhin / Alistar  
SK red — Twisted Fate / Nocturne / Orianna / Kai'Sa / Skarner

Confirmed position:

- SK +6.5 kills @1.814, 0.25u shadow — LOSS (-0.25u)

Pregame/post-draft market:

- VIT ML 1.609;
- SK ML 2.279;
- VIT -6.5 kills 1.964;
- SK +6.5 kills 1.814.

Final user-authoritative result: VIT won; user described SK as stomped. Latest synchronized grading frame at 24:04:

- VIT 24-7 SK;
- VIT +13k gold;
- towers 9-1;
- dragons 3-0;
- Baron 1-0;
- inhibitors 1-0.

The +6.5 handicap lost by a wide margin.

---

## What the Game 2 analysis got wrong

### 1. Nominal tools were mistaken for reliable tools

The model credited SK with multiple margin-saving / threat-answering layers:

- Twisted Fate point-and-click control;
- Nocturne darkness / engage;
- Orianna control;
- Skarner suppression;
- Kai'Sa follow-up.

That inventory was mechanically true but probabilistically misleading.

The functions were highly **conditional and synchronized**. SK needed multiple pieces to be in range, on timing, and sufficiently funded. Once top/jungle/mid fell behind, the entire chain degraded together.

The model needs to distinguish:

- nominal function availability;
- matchup reliability;
- economy dependence;
- synchronization dependence;
- redundancy if the first sequence fails.

### 2. Role/economy assignment was underweighted

Skarner support was treated too much like generic Skarner utility/frontline rather than a low-economy support implementation.

Twisted Fate top was credited for global/point-click utility without enough penalty for lane durability, frontline loss and vulnerability into Aatrox.

Champion function cannot be separated from role assignment and expected economy.

### 3. SK's execution burden was much higher than stated

SK's best fights required coordinated sequencing and target access. VIT had more independent ways to create and continue fights through Lee Sin / Alistar / Akali / Aatrox.

The model overvalued synchronized upside and underpriced the **failure cost of the first engage**.

### 4. Jhin was incorrectly used as a wide-margin dampener

The analysis argued that Jhin's lower sustained-DPS profile should compress VIT's 7+ kill-margin tail.

That was too archetype-driven. In a composition where other roles supply damage/access and Jhin supplies long-range follow-up, root, slow and execute pressure, Jhin does not prevent a kill cascade.

Wide-margin projection must evaluate total team damage-source redundancy and cleanup reliability, not ADC archetype in isolation.

### 5. Team strength and market information were overridden too aggressively

The market priced VIT around 62% raw implied ML pregame/post-draft (1.609), while the model moved the matchup toward roughly coin-flip based mostly on draft-function interpretation.

That is too large a divergence for an unvalidated qualitative draft overlay.

Draft Primacy should modify the team-strength prior, not erase it.

### 6. Game 1 execution evidence did not carry strongly enough into Game 2

Fearless Draft requires draft mechanisms to be rebuilt each game, but **team execution quality should not reset to zero**.

Game 1 supplied fresh evidence that VIT could stabilize, set objective fights, punish failed engages and execute later states better than SK.

That information should have strengthened VIT's Game 2 team-level execution prior.

### 7. v0.3.52 was promoted too quickly from one loss

The Game 1 terminal-threat patch was conceptually useful, but it was activated immediately and then used as positive evidence for SK's Game 2 +kills survival.

This is change-control overfitting.

A new concept derived from one map should enter an experimental/probationary layer until multiple out-of-sample observations support it.

---

## Ledger evidence — post-circuit-breaker shadow positions

At the time of this review, the Airtable shadow ledger contains 23 settled post-CB positions:

- record: 10-13;
- net P/L: -0.7755u;
- stake: 5.75u;
- ROI: approximately -13.5%.

By market family:

- Kill Handicap: 13 positions, 7-6, +0.311u (~+9.6% ROI);
- Total Kills: 5 positions, 1-4, -0.8095u (~-64.8% ROI);
- Moneyline: 3 positions, 1-2, -0.25525u (~-34.0% ROI);
- Duration: 1 position, 0-1, -0.25u;
- Series Handicap: 1 position, 1-0, +0.22825u.

The Kill Handicap aggregate hides a critical phase split:

### Pregame / post-draft Kill Handicap

- 5 positions;
- 1-4;
- -0.7295u.

### Live Kill Handicap

- 8 positions;
- 6-2;
- +1.0405u.

Therefore the data does **not** support the claim that all handicap logic is inverted. It strongly suggests that the model's profitable information is coming from synchronized live state, while **draft-only/pregame handicap repricing is currently harmful**.

Total Kills is separately and clearly underperforming.

---

## Contrarian/fade interpretation

A pure opposite-side strategy cannot be assigned an exact historical ROI without the executable opposite-side odds for every logged position.

However, directionally, the post-CB model is 10-13, so the opposite selection would have been correct on 13 of 23 binary decisions before accounting for price.

For the two SK-VIT positions specifically, the opposite sides were visible at entry:

- fade SK ML @1.752 -> VIT ML @2.042: 0.25u stake would profit +0.2605u;
- fade SK +6.5 @1.814 -> VIT -6.5 @1.964: 0.25u stake would profit +0.2410u.

Combined two-position fade: +0.5015u versus model -0.5000u.

So the user's criticism is exactly correct for this series, while a blanket fade-all conclusion still requires full opposite-price reconstruction.

---

## Required model-design corrections before further promotion

### A. Market-anchor shrinkage

Qualitative draft analysis may adjust but not freely replace the de-vigged market/team-strength prior.

Until calibrated, large model-market divergence should trigger shrinkage or PASS rather than confidence escalation.

### B. Functional Reliability / Economy Dependency overlay

For every credited draft function, grade:

- reliability under opponent counterplay;
- economy dependency;
- role-assignment dependency;
- synchronization dependency;
- redundancy / fallback after first failure.

Nominal champion access is not sufficient.

### C. Underdog Collapse Tail

Before every +kills TAKE, explicitly price the branch where the underdog's coordinated mechanism fails early and several roles become simultaneously nonfunctional.

This tail must be wider when:

- the underdog has fragile lanes;
- engage is synchronization-heavy;
- frontline is low-economy or role-swapped;
- opponent has multiple independent engage/damage sources;
- team-strength prior favors the opponent materially.

### D. Within-series execution Bayesian update

Carry forward observed teamfight execution, objective setup, lead conversion, comeback resistance and adaptation between games.

Fearless resets champion availability/mechanisms, not team skill evidence.

### E. Change-control discipline

Do not promote a new active rule from one anecdotal loss unless it is a hard safety constraint.

New explanatory features should be tracked experimentally over multiple maps before they are allowed to create additional positive edge.

### F. Probability-calibration restraint

Do not output 65-75% subjective probabilities from qualitative mechanism analysis unless empirical calibration supports those ranges.

Probability ranges should remain market-anchored and uncertainty should expand when the model disagrees materially with the market.

---

## Recommended temporary operating policy

Pending recalibration:

1. pregame/post-draft Kill Handicap should be analysis-only;
2. Total Kills should be analysis-only;
3. live Kill Handicap remains the only market family with positive post-CB evidence, but must still clear all existing signed-margin / KCV / Structure Substitution gates;
4. Moneyline should require synchronized live evidence and explicit market-anchor shrinkage; no large draft-only probability departures;
5. new model concepts should be tagged experimental until validated out of sample.

This is a proposed review outcome, not yet an active version delta.
