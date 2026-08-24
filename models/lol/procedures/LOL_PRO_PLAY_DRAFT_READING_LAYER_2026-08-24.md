# LoL Pro-Play Draft Reading Layer — 2026-08-24

**Status:** PENDING_NEXT_SLATE under any currently active Session Authority Lock  
**Analytical model:** LoL v0.3.58 in-place amendment; no new model version  
**Scope:** professional and officially sanctioned semi-professional League of Legends matches only  
**Excludes:** solo queue, amateur/open-ladder play, generic champion tier-list inference, and non-competitive win-rate shortcuts

## Purpose

The existing Draft Interaction Matrix (DIM) is strong at composition-vs-composition combat geometry, but a professional draft is not five champions appearing simultaneously on a neutral board.

In pro play, draft value also depends on:

- exact series format and champion-availability rules;
- blue/red side and first-pick / selection rights;
- player-specific champion proficiency and role flexibility;
- lane priority and matchup volatility;
- jungle/support access created by those lanes;
- first-move and reset timing before compulsory objectives;
- the composition's tempo curve and item/level transitions;
- whether the team can execute the composition at coordinated pro tempo;
- previous games in the same series and the remaining champion pool under Fearless or other restrictive formats.

This procedure adds a **Pro Draft Reading Layer (PDRL)** on top of DIM. It does not replace DIM, UDKC, KMS, TAM, CAS, or any live-state gate.

---

# 1. Activation rule

Run PDRL whenever all are true:

1. the match is professional or officially sanctioned semi-professional competition;
2. the exact ten champions and roles are known or can be resolved;
3. a model-certified draft edge is being issued or the draft is being used as a prior for a live market.

If the competition format materially changes champion availability across a series, the current series draft state is mandatory input.

For a one-game draft read with no reliable series context, unresolved format-dependent fields remain `UNRESOLVED`; do not invent champion availability or prior-game constraints.

---

# 2. Evidence hierarchy — pro data only

Use evidence in this order:

### Tier A — match/series-specific competitive facts

- exact starting five and roles;
- current competitive patch;
- tournament draft format;
- current series score;
- side / first-pick / Right of First Selection state where applicable;
- champions already used or otherwise unavailable in the current series;
- exact previous-game drafts in the same series.

### Tier B — current-patch / current-split pro evidence

- player champion usage and role history;
- team pick/ban tendencies;
- lane-pair and jungle/support tendencies;
- recent pro execution of similar composition identities;
- opponent-specific bans or adaptations.

### Tier C — older professional evidence

Older champion comfort, historical team style, and prior-season tendencies may be used only as weak modifiers when current evidence is sparse.

### Pro-only prohibition

Do **not** use solo-queue win rate, solo-queue pick rate, generic public tier lists, or low-level amateur results to upgrade a professional draft edge.

They may be used only for champion-mechanics orientation when absolutely necessary, never as draft-edge evidence.

---

# 3. Mandatory series-format state — `FDS`

Resolve **FDS — Format & Draft State** before the pro layer.

Record:

`PATCH | FORMAT | GAME_NUMBER | SERIES_SCORE | SIDE | FIRST_PICK/SELECTION_RIGHT | USED/LOCKED_CHAMPIONS | MATERIAL_REMAINING_POOL_CONSTRAINTS`

Classify:

- `FDS = PASS` — decision-relevant format/availability state known;
- `FDS = PARTIAL` — format known but some noncritical pool information missing;
- `FDS = UNRESOLVED` — material series restrictions or selection rights unknown.

### Fearless / restricted-pool hard rule

When the event uses Fearless Draft or another series-wide champion restriction, Game 2+ must never be evaluated as an isolated full-pool draft.

Ask:

1. Which high-priority champions have already been removed by prior games?
2. Which team's remaining player pools are being compressed more severely?
3. Which roles still retain credible blind picks?
4. Did one team spend a premium comfort/meta champion earlier in the series to create a later pool disadvantage?
5. Is a current pick strong in absolute terms but weak relative to what remains available?

Champion-pool depletion is part of draft value, not post-hoc context.

---

# 4. Lane Priority Matrix — `LPM`

Resolve all three lanes using realistic pro lane states rather than isolated 1v1 labels.

For TOP / MID / BOT classify:

- early push / first three waves;
- level-2/3 threat and all-in volatility;
- crash/reset control;
- susceptibility to jungle intervention;
- ability to move first without losing unacceptable lane resources;
- post-6 matchup change;
- side-lane assignment after first rotations.

Output each lane:

`PRIO+ / EVEN / PRIO-` plus `VOLATILITY=LOW/MED/HIGH`.

Then answer:

**Which team is more likely to own two-lane priority at the first meaningful jungle/objective decision?**

Hard rules:

- three individually playable lanes do not automatically produce a playable map;
- one losing lane may be acceptable if the composition is designed to concede it safely;
- a nominal counterpick that cannot convert push, reset, roam or side pressure receives limited draft credit.

---

# 5. Jungle–Support Coupling — `JSC`

Professional map control is often produced by lane priority feeding jungle/support movement.

Evaluate:

- which jungler can enter river/second quadrant first;
- which support can leave lane first and on what wave;
- invade and warding safety;
- early objective access;
- countergank / cover requirements;
- whether one jungler must spend time stabilizing a losing lane;
- whether the support roam creates unacceptable ADC exposure;
- whether mid priority enables or blocks jungle/support pairing.

Classify:

- `JSC = ADV [TEAM]`
- `JSC = EVEN`
- `JSC = CONDITIONAL`

Do not grade jungle matchups independently of lane access unless the composition genuinely permits it.

---

# 6. Tempo Transition Map — `TTM`

Map when each composition changes state.

At minimum evaluate:

- levels 3 / 6;
- first recall / first major component;
- first completed item;
- two-item core;
- major ultimate unlocks;
- objective-specific spikes;
- side-lane transition;
- late-game damage/access scaling.

For each team identify:

`EARLY WINDOW | MID WINDOW | LATE WINDOW | DEAD ZONE`

A generic label such as `better scaling` is insufficient.

Mandatory questions:

1. Who is favored before first dragon/grubs/Herald-type compulsory map decisions?
2. Who is favored at the first major completed-item fight?
3. Is there a period where one team must avoid 5v5 but can still trade cross-map?
4. Does the supposed scaling team have a credible route to reach its scaling state without surrendering decisive map control?

---

# 7. Objective Sequence Projection — `OSP`

Extend DIM's Objective-Setup Geometry into a pro-tempo projection.

Project the first three meaningful compulsory map cycles using LPM + JSC + TTM:

`CYCLE 1 -> CYCLE 2 -> CYCLE 3`

For each cycle ask:

- who should arrive first from ordinary lane states?
- who can establish vision without face-checking the opponent's strongest threat?
- who has the better objective turn?
- who can safely concede and gain an equivalent cross-map return?
- does one lost cycle make the next setup materially easier for the same team?

Classify:

- `OSP = ADV [TEAM]`
- `OSP = BALANCED`
- `OSP = HIGHLY STATE-DEPENDENT`

This is a draft projection only. Do not import live objectives or live gold when reconstructing after game start.

---

# 8. Player Fit & Proficiency — `PFP`

DIM's ETS team-strength modifier is too coarse for professional draft execution by itself.

Evaluate each decision-critical champion assignment against current professional evidence:

- recent competitive champion usage;
- role authenticity / flex history;
- mechanical burden;
- lane-specific proficiency;
- whether the player has previously executed the same strategic responsibility;
- whether the pick forces an unusual resource share or role swap.

Classify each material assignment:

- `COMFORT`
- `PROVEN`
- `PLAUSIBLE`
- `UNPROVEN`
- `ROLE-RISK`

Then classify team-level `PFP`.

Hard rules:

- champion reputation is not player proficiency;
- a statistically common pro champion is not automatically comfortable for the current player;
- old signature picks cannot override current-patch evidence without support;
- no solo-queue evidence may upgrade PFP.

---

# 9. Execution Burden Differential — `EBD`

Compare how precisely each team must play to realize its win condition.

Evaluate:

- number of sequential actions required before damage becomes reliable;
- flank/vision dependency;
- skillshot or narrow initiation dependency;
- requirement for synchronized multi-angle entry;
- protection demands on one carry;
- reset/re-engage sequencing;
- side-lane timing precision;
- tolerance for one missed engage or one lost setup cycle.

Classify:

- `EBD = EASIER [TEAM]`
- `EBD = SIMILAR`
- `EBD = NARROW [TEAM]`

A stronger team may receive more credit for a coordination-heavy composition, but PFP/ETS cannot erase a mechanically losing interaction.

---

# 10. Win-Condition State Robustness — `WCSR`

Grade both drafts from three starting regimes:

### EVEN

What is the normal repeatable win condition from roughly even resources?

### AHEAD

Does the composition become easier to execute, or does it still require narrow mechanics?

### BEHIND

Can it still:

- clear waves safely;
- create picks without face-checking;
- trade cross-map;
- threaten side lanes;
- contest through range/terrain;
- disengage and reset;
- protect a meaningful damage source?

Classify:

- `ROBUST` — multiple viable states;
- `NORMAL` — coherent near even/ahead, limited from behind;
- `FRAGILE` — requires narrow state or first move;
- `BINARY` — one primary condition with weak fallback.

This is distinct from UDKC. WCSR describes overall pro-game draft resilience; UDKC/KMS still separately govern underdog +kills.

---

# 11. Series Pool Pressure — `SPP`

For multi-game professional series, especially Fearless formats, evaluate **remaining-pool leverage**.

Ask:

- which role is being pinched by prior picks/bans?
- which team has deeper current-patch professional champion coverage?
- which flex picks preserve future options?
- did a previous game expose a champion-pool dependency the opponent can now target?
- are later-game drafts likely to force unproven assignments?

Classify:

- `SPP = ADV [TEAM]`
- `SPP = EVEN`
- `SPP = UNRESOLVED`

SPP may affect the current Game 2+ draft because the remaining pool determines the opportunity cost and replacement quality of each selection.

Do not use SPP to predict a future game from nothing; it must be grounded in known current-series availability and current professional pools.

---

# 12. Series Adaptation Pass — `SAP`

For Game 2+ run a pro-only adaptation pass:

1. What did the previous draft attempt to accomplish?
2. Which part was actually denied by draft interaction, independent of game result?
3. What changed in bans/picks now?
4. Did the team repair the failed mechanism or merely change champion names?
5. Did the opponent preserve the same structural answer through different champions?
6. Has Fearless depletion removed the previous answer or the previous threat?

Outcome-blind rule:

A previous win does not prove the previous draft was superior; a previous loss does not prove it was inferior. Separate draft mechanism from in-game execution and state.

---

# 13. Mandatory Pro Adversarial Pass — `PAP`

After DIM + PDRL, attack the favored draft from the other side.

State:

1. the easiest lane/map route for the nominally weaker draft;
2. the first timing at which it can flip priority or objective setup;
3. the best professional adaptation available through lane assignment, jungle path, support roam or side-lane trade;
4. what happens if the favored team loses the first compulsory cycle;
5. whether the favored draft still has a repeatable second route.

If the edge disappears after one ordinary professional adaptation, downgrade the draft edge.

---

# 14. Output separation

Never compress all pro information into one opaque draft grade.

Produce:

### `DIM_EDGE`

Pure composition interaction from existing DIM.

### `PRO_MAP_EDGE`

Lane + jungle/support + tempo + objective projection.

### `PRO_EXEC_EDGE`

Player fit + execution burden + team-strength modifier.

### `SERIES_DRAFT_EDGE`

Format/Fearless/remaining-pool/adaptation effect.

### `FINAL_PRO_DRAFT_EDGE`

One of:

- `STRONG [TEAM]`
- `CLEAR [TEAM]`
- `SLIGHT [TEAM]`
- `EVEN / STYLE-DEPENDENT`
- `UNRESOLVED`

The final edge must explain **why the advantage should materialize in professional play**, not simply list champion strengths.

---

# 15. Hard downgrade / unresolved rules

A `STRONG` or `CLEAR` professional draft label is forbidden when any decision-critical item below is unresolved:

- exact roles;
- material format/Fearless state for Game 2+;
- a decisive lane/flex assignment;
- the primary lane-priority chain that supports the claimed map edge;
- the main damage-access interaction from DIM;
- a decision-critical player assignment classified `ROLE-RISK` with no professional evidence;
- contradictory PDRL outputs with no adjudicated reason for weighting one above the other.

Do not force certainty merely because a visible draft must be discussed.

---

# 16. Anti-simplification rules for professional drafts

Forbidden shortcuts:

- `more scaling = better draft`;
- `more engage = better draft`;
- `more tanks = easier draft`;
- `three winning lanes = automatically better draft`;
- `counterpick = lane win`;
- `comfort champion = good pick` without current player evidence;
- `meta champion = good pick` independent of remaining series pool and composition fit;
- grading Game 2+ Fearless drafts as full-pool isolated drafts;
- using solo-queue stats to break a pro draft tie;
- treating a previous game's result as proof of draft quality.

---

# 17. Compact internal certificate

Persist when practical as:

`PDRL[FDS=P/Pa/U; LPM=...; JSC=...; TTM=...; OSP=...; PFP=...; EBD=...; WCSR=...; SPP=...; SAP=P/F/U; PAP=P/F/U; PRO_MAP=...; PRO_EXEC=...; SERIES=...; FINAL=...]`

For a professional draft verdict, DIM remains mandatory and PDRL becomes the pro-only extension.

For live Moneyline, `FINAL_PRO_DRAFT_EDGE` supplies the original draft prior before normal DPS/LRO degradation rules.

For underdog +kills, PDRL may downgrade draft confidence but may **not** bypass DIM, TAM, CAS, UDKC, KPA/KMS, RLD, LAC or UCS.

---

# 18. Governance

This procedure is an in-place v0.3.58 analytical amendment requested on 2026-08-24 to improve professional-play draft reading.

It does not alter the current frozen Session Authority Lock unless the user explicitly authorizes an immediate relock/new authority epoch.

Default activation is the next valid slate lock after this procedure and the corresponding `CURRENT_MODEL.md` amendment are committed.
