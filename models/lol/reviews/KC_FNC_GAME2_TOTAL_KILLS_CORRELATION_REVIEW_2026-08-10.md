# KC vs FNC Game 2 — Total Kills + Same-Map Correlation Review

**Date:** 2026-08-10 UTC+7  
**Model at entry:** LoL v0.3.48  
**Map:** Karmine Corp vs Fnatic, LEC 2026 Summer, Game 2

## Draft

KC blue: Yorick / Vi / Viktor / Kalista / Renata  
FNC red: Jayce / Olaf / Ryze / Ziggs / Shen

## Confirmed shadow positions

1. Under 27.5 total kills @1.955, 0.25u — LOSS (-0.25u)
2. FNC +13.5 kills @2.122, 0.25u — WIN (+0.2805u)

Net same-map P/L: +0.0305u shadow.

## Final

KC won 20-8 at 31:53.  
Total kills: 28.  
Final kill margin: KC +12.

## What was correct

### Handicap engine

The FNC +13.5 entry was structurally sound. At 10:48 KC led 5-1, so KC still needed +10 additional net kills to beat the handicap. KC had strong map-control and pick tools, but the line demanded a large signed-margin expansion. Final margin was +12, so FNC covered by 1.5 kills.

This validates the v0.3.48 distinction between map dominance and kill-margin dominance.

## What failed

### Total Kills engine

The Under 27.5 thesis over-weighted the following:

- low early kill count;
- side-lane / structure conversion routes;
- FNC poke, waveclear and global tools as generic fight suppressors.

It under-weighted:

- KC's reliable hard access through Vi;
- Renata follow-up and fight extension;
- Kalista's ability to convert catches/objective control into additional kills once ahead;
- FNC's weak ability to fully disengage after first contact;
- the number of future compulsory contest windows created by KC objective control;
- the fact that a trailing team can be forced into repeated losing contests even if its own draft is not naturally fight-seeking.

The key error was treating `quiet so far` as too informative about `quiet later`.

## New distinction: Observed Pace vs Forward Contact Inventory

Current kill count is a state variable, not mechanism proof.

For Total Kills, separately estimate:

1. **Observed Kill Pace (OKP):** kills/minute and recent fight outcomes.
2. **Forward Contact Inventory (FCI):** future opportunities where one team can reliably force contact or the trailer is compelled to contest.
3. **Contact Lethality (CL):** expected deaths once contact occurs, based on access, disengage, damage continuation, cleanup and return-kill structure.

A low OKP cannot by itself support or upgrade an Under when FCI and CL remain high.

## Forced-contact sources

Count future contact windows only when they are matchup-functional. Relevant sources include:

- reliable hard engage / point-and-click or near-guaranteed access;
- repeated pick tools plus vision control;
- dragon soul-point / soul / Elder contests;
- Baron setup or Baron defense;
- inhibitor/base-defense sequences;
- side-lane collapses that the defender cannot safely concede;
- objective pressure that forces the losing team to walk into enemy control.

Do not assume waveclear, poke or globals suppress kills if the trailing team cannot actually disengage after contact.

## Contest Compulsion

A trailing team may become more kill-generating as the map worsens because it loses the option to concede objectives indefinitely.

When the leader has strong objective control and reliable access, future contests can become increasingly compulsory. This can raise total-kill expectation even if the leader also has efficient structure conversion.

Therefore Structure Substitution can reduce favorite kill margin while Total Kills still rises through traded or terminal fights.

## Same-map correlation lesson

Under + underdog +kills are not automatically strongly positively correlated.

Let:

- `T = favorite kills + underdog kills`;
- `M = favorite kills - underdog kills`.

A map can have high T but moderate M through return kills/traded fights. KC-FNC G2 was exactly that: T=28 lost Under 27.5, while M=12 won FNC +13.5.

Same-map add-ons must therefore price the joint distribution rather than apply a generic correlation penalty based only on shared narratives.

Minimum joint matrix for two positions A and B:

- P(A win, B win)
- P(A win, B lose)
- P(A lose, B win)
- P(A lose, B lose)

The correlation assessment must identify the concrete branch that creates one-win/one-loss outcomes.

## Calibration decision

Promote model to v0.3.49 with:

- mandatory OKP / FCI / CL decomposition for Total Kills;
- quiet-start non-persistence rule;
- contest-compulsion adjustment;
- access/disengage mismatch check;
- separate T and M projections for same-map Total Kills + Kill Handicap positions;
- joint four-cell add-on correlation pricing.

The existing v0.3.48 handicap conversion framework remains active.
