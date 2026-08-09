# MODEL RULES — LEAGUE OF LEGENDS v0.3.42

**Status:** Active delta  
**Effective date:** 2026-08-09 14:55 UTC+7  
**Supersedes:** v0.3.41 only where stated

## Purpose

Correct two linked calibration failures exposed by LNG vs IG Game 1 and the preceding NAVI vs SK sequence:

1. **unstable team-strength priors** caused by stale/incorrect roster assumptions, excessive reaction to isolated sources, and unbounded movement between independent model estimates and the market prior;
2. **draft-tool counting** that credited generic range, waveclear, engage, scaling, or return-kill tools without first testing whether those tools were functional into the opponent's actual composition and player-strength context.

v0.3.41 position-blind reassessment, mechanistic handicap resilience, Draft Cascade-Structure Veto, v0.3.40 ML/total calibration, v0.3.39 handicap probability gates, v0.3.38 favorite structural ladder, Objective-Control Handicap Veto, executable-price discipline, settlement rules, and all retained controls remain active.

---

## 1. Verified Team-Strength Prior Gate

No numerical team-strength or map-win prior may be issued until the **current expected/confirmed five-player lineup** is verified or explicitly supplied by the user.

If the roster is uncertain:

- do not substitute season-long team strength from a materially different roster;
- do not use departed/inactive players in lane or role comparisons;
- state the prior as unverified and fail closed on numeric betting edges that depend on it.

A user-supplied current lineup overrides stale public roster pages unless contradicted by stronger synchronized evidence.

### Roster-discontinuity rule

When a team has changed one or more starting roles materially within the current split/stage:

- downweight results from prior lineups;
- sharply downweight full-year aggregate statistics when they are not representative of the current five;
- prioritize results, role performance and execution tendencies from the current lineup;
- widen uncertainty when the current lineup sample is small.

Old team identity is not current team strength.

---

## 2. Team-Strength Construction Order

Build the pre-draft map/series prior in this order:

1. verified current lineup;
2. current-stage results with that lineup;
3. opponent-adjusted quality of those results;
4. role-by-role player strength and current role fit;
5. macro/early-game/objective/lead-conversion tendencies from representative samples;
6. side/format context when map-specific and verified;
7. de-vigged market prior as an external calibration anchor;
8. explicit uncertainty band.

Do not begin with historical reputation and then search for confirming statistics.

### Role-strength matrix

For each matchup, score all five roles as one of:

- material edge;
- slight edge;
- approximately even;
- slight disadvantage;
- material disadvantage.

Then separately score:

- shot-calling / macro coordination;
- early-game creation;
- objective setup;
- teamfight execution;
- lead conversion;
- comeback resistance;
- volatility / throw risk.

A famous player name is not itself a material edge. Current role fit, form and team integration matter.

---

## 3. Market-Divergence Sanity Gate

The de-vigged market prior is **not** automatically correct, but a large disagreement requires evidence.

Before draft, if the model's central map/series win probability differs from the de-vigged market by:

- **0–6pp:** normal disagreement;
- **>6 to 10pp:** require at least two independent verified reasons;
- **>10pp:** require at least three independent verified reasons, including at least one current-lineup performance reason and one matchup/role reason.

If those reasons are absent, shrink the model estimate toward the market until the disagreement is <=6pp and widen the uncertainty band.

**Uncertainty is not edge.** A wide model band must never be converted into automatic underdog value.

Sportsbook movement may be evidence of information but may not be used circularly as proof that the bet is good.

---

## 4. Map Prior Must Be Distinct from Series Prior

Do not transfer a Bo3 series probability directly to a single-map moneyline or kill handicap.

For each map:

- start from a map-level team-strength prior;
- account for verified side;
- account for series-state adaptation only as a soft factor;
- then apply the draft adjustment.

A heavy series favorite can still have a substantially lower single-map probability, but the map underdog is not automatically valuable because the series price looks extreme.

---

## 5. Matchup-Adjusted Draft Function Rule

Draft evaluation is **relative**, not additive.

A composition receives credit for a tool only if the tool can function against the opponent's actual answers.

For every claimed advantage, test the opposing interaction:

- **safe range** vs opponent engage radius, flank access, globals and dive;
- **waveclear** vs siege range, side-lane pressure and dive threat;
- **disengage** vs point-and-click, multi-axis or unstoppable/repeat engage;
- **peel** vs number of simultaneous dive threats and target-access routes;
- **engage** vs anti-engage, terrain denial and mobility denial;
- **objective contest** vs choke control, poke, zone denial and face-check burden;
- **return-kill reliability** vs enemy cleanup mobility, reset/chase, invulnerability or ranged follow-up;
- **scaling** vs whether the scaling carries can actually deliver damage safely.

A nominal tool that is directly suppressed by the opponent counts as **weakened or nonfunctional**, not as a full resilience category.

---

## 6. Functional Counter Tax

Apply an explicit draft penalty when one opponent champion or interaction suppresses multiple core functions of the other draft.

Examples of functional suppression include:

- anti-dash / displacement denial into multiple dash-reliant engage or carry champions;
- point-and-click lockdown into a composition dependent on one mobile carry;
- long-range zone control into a short-range contest composition;
- unstoppable/multi-axis engage into nominal single-layer disengage;
- side-lane pressure that forces a teamfight composition into losing map assignments.

If one opponent tool materially degrades **two or more** of the six handicap-resilience categories, the affected composition cannot be credited with those categories at full strength.

Do not hard-code champion names; score the functional interaction.

---

## 7. Execution-Burden and Stronger-Team Simplicity Adjustment

After the draft scorecard, identify:

- which team has the simpler first successful sequence;
- which team needs more precise spacing, flank timing, target selection or multi-step setup;
- which team has more independent ways to start a favorable fight;
- which composition becomes nonfunctional first when one role falls behind.

When the **stronger team also has the simpler and more reliable execution path**, increase its clean-win and high-margin branches.

When the underdog requires high mechanical or sequencing precision merely to access its theoretical tools, reduce the value of those tools in moneyline and positive-handicap pricing.

Draft quality is not symmetric with execution burden.

---

## 8. Damage-Access Map

Before any post-draft TAKE, explicitly identify the expected primary damage route for both teams:

1. who hits frontline safely;
2. who can access backline;
3. who must cross enemy control to deal meaningful damage;
4. which carry is easiest to isolate;
5. whether the main DPS can continue dealing damage after first contact;
6. whether the losing team can produce return kills while retreating.

If the underdog's damage carriers must repeatedly enter the opponent's control zone to function, do not classify the draft as high handicap resilience merely because it has multiple damage champions.

---

## 9. Conditional Kill-Margin Decomposition

For positive kill handicaps, estimate cover probability through explicit winner/margin branches:

`P(dog +H covers) = P(dog wins) + P(favorite wins AND favorite margin <= H)`

The second term must be evaluated **conditional on a favorite win**, not from an unconditional generic margin distribution.

Required branches:

- underdog wins;
- favorite wins close;
- favorite wins moderate;
- favorite wins high-margin.

Use team-strength gap, draft execution asymmetry, cascade architecture and expected total kills to allocate these branches.

A high underdog cover estimate is invalid if it implicitly assumes both a large favorite win probability and an unrealistically high close-loss rate without evidence.

For pregame positive handicaps, state or internally calculate the conditional probability that the favorite wins by more than the line.

---

## 10. Draft Adjustment Cap — Refined

Retain the v0.3.40 normal draft move of **0–4pp** from the verified pre-draft map prior.

A >4pp move requires at least three independent **functional** advantages after opponent-counter testing, not merely three listed tools.

A draft should rarely overcome a large verified team-strength gap by itself.

If the weaker team is receiving a large positive handicap, the handicap may still qualify, but only through the Section 9 conditional-margin decomposition and applicable probability gate.

---

## 11. LNG vs IG Game 1 Calibration

Verified lineups supplied before Game 1:

- LNG: sheer / Weiwei / Nia / 1xn / Missing
- IG: TheShy / Wei / Rookie / Assum / Meiko

Draft:

- LNG: K'Sante / Naafiri / Akali / Corki / Nautilus
- IG: Olaf / Jarvan IV / Ryze / Kai'Sa / Poppy

Market at 0:00 approximately:

- IG ML 1.231;
- LNG ML 4.032;
- IG -9.5 kills 1.793;
- LNG +9.5 kills 1.970.

LNG +9.5 @1.970 was recommended and confirmed for 0.25u shadow.

Final: **IG 26-13 LNG**, IG +13 kill margin; LNG +9.5 lost -0.25u shadow.

### Team-strength error

The pre-series strength estimate moved excessively across assessments because stale roster assumptions and incomplete current-lineup verification were allowed to dominate. Once the user supplied the actual current lineups, the model still moved too far away from a heavily IG-favored market without enough current-lineup evidence.

Under v0.3.42, the pre-draft team-strength prior must remain market-calibrated unless a >6pp disagreement is supported by the required verified reasons.

### Draft error

The LNG +9.5 case over-credited nominal resilience:

- Corki range/waveclear;
- K'Sante frontline/peel;
- Nautilus pick/return-kill potential;
- Akali/Naafiri counter-access.

It underweighted the **relative matchup**:

- IG's Poppy functionally interfered with multiple dash/engage/access patterns;
- Jarvan + Ryze + Kai'Sa created reliable multi-axis follow-up and target access;
- Olaf increased front-line run-through pressure and reduced the reliability of conventional control as a stop mechanism;
- LNG's Akali/Naafiri damage had meaningful access burden into IG's control structure;
- IG's stronger team prior plus simpler engage-to-follow-up sequence increased the conditional high-margin branch when IG won.

The correct question was not whether LNG possessed four theoretical tools. It was whether those tools remained functional enough **against IG's exact composition** to keep an IG win within nine kills.

Under v0.3.42, LNG +9.5 would require a substantially lower conditional probability of IG winning by 10+ than the matchup justified; absent that evidence it is a `PASS`.

---

## 12. Mandatory Pregame Output Discipline

Before a pregame/0:00 recommendation, internally lock these four objects separately:

1. **verified team-strength prior** with uncertainty;
2. **market de-vig prior** and model-vs-market divergence;
3. **matchup-adjusted draft score** with execution burden and damage access;
4. **market-specific distribution** for ML / handicap / total / duration.

Do not let the draft narrative rewrite team strength after seeing the price.

Do not let a positive-handicap cushion substitute for conditional margin analysis.

---

## 13. Retained Controls

All prior controls remain active unless explicitly superseded:

- verdict first;
- official wagering remains paused until explicit restoration;
- default shadow stake 0.25u;
- minimum odds 1.60;
- executable-price confirmation before recording;
- position-blind reassessment;
- no correlated same-map add-ons unless the user explicitly designates a separate independent bet and it separately qualifies;
- no rescue/chasing logic;
- moneyline, kill handicap, total kills and duration are separate markets;
- current-map hard evidence resets every map;
- item verification remains suspended;
- settlement rules unchanged.

Where this delta conflicts with earlier rules, **v0.3.42 controls**.
