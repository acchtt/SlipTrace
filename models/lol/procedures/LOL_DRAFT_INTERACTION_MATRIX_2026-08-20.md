# LoL Draft Interaction Matrix — 2026-08-20

**Status:** CANONICAL v0.3.58 IN-PLACE AMENDMENT ON DEFAULT BRANCH  
**Activation:** subject to the active Session Authority Lock; changes after the current lock are `PENDING_NEXT_SLATE` unless the user explicitly authorizes an immediate relock  
**Analytical model:** LoL v0.3.58 unchanged  
**Purpose:** improve draft reading by forcing mechanism-to-mechanism interaction analysis before a draft edge, UDKC stability label, or other draft-derived certification.

This procedure is not an outcome patch and does not create a new model version. It corrects a demonstrated classification failure: treating generic defensive utility as if it answered the opponent's actual kill mechanism.

## 1. Mandatory scope

Before issuing any model-certified **draft verdict** such as `strong/clear/slight edge`, `even`, or a draft-derived fallback classification, complete the Draft Interaction Matrix (`DIM`).

For underdog +kills, DIM is a hard prerequisite to UDKC certification. A UDKC may not be `STABLE` when DIM is incomplete, when the underdog's claimed defensive answers do not directly match the favorite's primary kill routes, or when collapse-suppression remains unresolved.

DIM is draft-only. When reconstructed after live play begins, use champion roles, team/lineup inputs and known team-strength priors only. Exclude current kills, gold, objectives, structures, live odds, handicap size and current kill margin.

## 2. Exact roles first

Before DIM, resolve the five champion-role assignments for both teams.

- Do not infer matchup geometry from an incorrect flex assignment.
- A genuine role correction reopens DIM and any draft-derived certificate.
- If a decision-critical flex remains ambiguous, the affected DIM row is `UNRESOLVED`; do not issue a strong draft label or UDKC `STABLE` from that ambiguity.

## 3. Mechanism map — both teams

For each team explicitly identify:

- `PKM` — Primary Kill Mechanism;
- `SKM` — Secondary Kill Mechanism;
- `SETUP` — how the team creates the board state needed for those mechanisms;
- `FAILURE` — what happens when first contact or setup fails;
- `RESET` — whether the team can disengage/reform or must continue forward;
- `CLOSE` — how the composition converts control into objectives/structures/game end.

Examples of kill mechanisms include, but are not limited to:

- front-to-back protected DPS;
- hard dive/backline access;
- poke -> zone -> pick -> follow-up;
- catch/pick from fog or globals;
- flank/collapse;
- side-lane pressure -> numbers advantage;
- wombo/terrain choke;
- reset/chase continuation.

Do not reduce a composition to labels such as `engage`, `scaling`, `frontline`, or `poke` without explaining the actual sequence that produces kills and margin expansion.

## 4. Required interaction rows

Resolve every row below before a draft verdict.

### A. TAM — Threat-Answer Matching

For every claimed defensive/reset mechanism, name the opponent threat it actually answers.

Hard rule: **generic utility is not generic suppression.**

- anti-dive may count against committed dive;
- peel may count against reachable melee access;
- disengage may count against continuation when it can actually be cast before the fight is already lost;
- waveclear may count against siege only when the defending composition can safely access the wave;
- anti-engage does not automatically suppress poke/pick;
- revival/renata-style reset does not automatically suppress pre-contact chunking, ranged zoning or isolated pick chains.

If the favorite's primary kill route is not directly answered, `TAM = FAIL/UNRESOLVED` for underdog KMS purposes.

### B. OSG — Objective-Setup Geometry

Evaluate who controls the space **before** the compulsory fight begins:

- range and poke;
- choke/terrain control;
- vision-entry safety;
- first move and wave priority;
- globals/semi-globals;
- flank denial/access;
- objective turn safety;
- ability to force the opponent through controlled space.

A composition can dominate objective geometry without owning a traditional tank.

### C. DAU — Damage Access & Uptime

For each meaningful damage source ask:

- can it reach priority targets from realistic neutral setup?
- can it continue dealing damage after first contact?
- what protection/resources are consumed to preserve uptime?
- does it have to cross the opponent's strongest zone to function?
- can the opponent's damage operate before committing bodies?

Do not credit theoretical DPS that cannot safely access the fight.

### D. SLI — Side-Lane Independence

A side-lane/split-push route counts as an **independent** mechanism only if it remains credible against the opponent's actual answers.

Test:

- lane matchup and waveclear;
- global/semi-global response;
- catch/pick threat on rotation;
- objective timing cost;
- whether the four-man unit can survive while the side-laner pressures;
- whether the side route creates forced resources rather than merely farming safely.

If globals, catch or matchup control can cheaply neutralize the split, do not count it as independent KMS/ARI evidence.

### E. FNF — Frontline Necessity Fit

Do not penalize `no tank` or limited frontline by default.

Ask whether the composition actually requires sustained front-to-back occupancy.

A poke/pick composition that wins space before contact may function with little traditional frontline. Conversely, a composition whose carries need long uninterrupted DPS windows may have a real frontline requirement.

Frontline quantity is therefore conditional on composition identity, not a standalone draft-quality score.

### F. CAS — Collapse Asymmetry

Stress the state **after the favorite gains the first ordinary advantage**.

Ask:

- after a 2-3 kill fight or one pick plus objective, does the underdog still have a distinct way to prevent repeated net kill-margin expansion?
- does the favorite's setup become easier after first control is gained?
- can the underdog safely contest the next compulsory cycle, or must it re-enter the same losing geometry?
- can structures/objectives force repeated exposed entries?
- does the underdog have a real reset/concession/cross-map route that breaks the chain?

For underdog +kills, `CAS = FAIL/UNRESOLVED` forbids `KMS = PASS` and therefore forbids UDKC `STABLE`.

### G. ETS — Execution & Team-Strength Modifier

Apply team/player strength only after the interaction map is built.

- stronger teams receive more confidence when executing a mechanically coherent but coordination-sensitive composition;
- weaker teams receive less benefit of the doubt for narrow execution windows;
- team strength never turns an interaction-losing draft into a mechanically winning one by fiat;
- team strength is a modifier, not a standalone veto or TAKE signal.

## 5. Mandatory adversarial second pass

Before finalizing the draft edge, perform an **Adversarial Favorite Pass (`AFP`)**:

1. state the strongest repeatable kill/control route for the favored/stronger side;
2. state what the opponent must do to stop it;
3. identify whether that answer directly matches the mechanism or is merely generic utility;
4. identify how the favorite adapts if the first route is denied;
5. stress one ordinary won fight/objective and the next compulsory cycle.

If this pass reveals a clean repeatable route that the underdog cannot directly answer, downgrade the underdog's draft/fallback classification before any live evidence is considered.

## 6. Separate outputs — never conflate them

DIM must produce two separate conclusions when relevant:

### Draft Edge

One of:

- `STRONG [TEAM]`
- `CLEAR [TEAM]`
- `SLIGHT [TEAM]`
- `EVEN / STYLE-DEPENDENT`
- `UNRESOLVED`

This is the overall composition interaction judgment.

### Underdog +Kills Stability

Separately determine whether UDKC can be `STABLE / FRAGILE / ABSENT / UNCERTIFIED`.

A playable draft is not automatically a good +kills draft. A team may have realistic win conditions while still lacking kill-margin suppression after falling behind.

## 7. UDKC integration hard rules

Before `UDKC_STABLE = PASS`, all of the following are mandatory:

- exact roles resolved;
- DIM complete;
- favorite `PKM/SKM` explicitly identified;
- `TAM = PASS` for the underdog's suppression tools against the favorite's primary repeatable mechanism;
- `OSG`, `DAU`, `SLI`, and `FNF` explicitly adjudicated where material;
- `CAS = PASS` for underdog kill-margin suppression;
- `AFP` completed with no unresolved clean favorite route;
- existing FER/PDC/PST/ARI/KPA/KMS/RLD/False-Stable/DCR/FF/Draft-Collapse rules still pass.

DIM does not replace KMS/RLD/UDKC. It is a prerequisite interaction layer that makes those certifications harder to satisfy incorrectly.

## 8. False-credit prohibitions

The following are specifically forbidden:

- counting anti-dive tools as generic anti-stomp protection against a poke/pick favorite without a direct mechanism explanation;
- counting a side-lane champion as an independent route without testing globals/catch/waveclear/four-man survival;
- treating lack of traditional frontline as a generic weakness for a composition designed to win pre-contact space;
- treating engage buttons as equivalent to reliable target access;
- treating theoretical scaling as current kill-margin suppression;
- using champion-name reputation rather than interaction geometry;
- allowing one attractive underdog tool to offset multiple favorite repeatable routes without mechanism matching.

## 9. Compact internal record

A completed matrix may be persisted compactly as:

`DIM[ROLES=P; PKM=...; SKM=...; TAM=P/F/U; OSG=...; DAU=...; SLI=...; FNF=...; CAS=P/F/U; ETS=...; AFP=P/F/U; EDGE=...]`

For any underdog +kills TAKE under an authority lock that includes this procedure, the position gate evidence must include `DIM=PASS` and `TAM=PASS`/`CAS=PASS` directly or through an exact persisted UDKC reference.

## 10. Reference incident — BLG vs LGD Game 3, 2026-08-20

Draft:

- BLG: Jayce / Pantheon / Syndra / Corki / Nami
- LGD: Yorick / Maokai / LeBlanc / Kalista / Renata

The original read called only a slight BLG edge and credited Maokai + Renata as broad anti-cascade protection plus Yorick as an independent side route.

Correct interaction read:

- BLG's primary route was **poke -> zone -> pick -> Pantheon follow-up**, not sustained front-to-back;
- limited BLG frontline was therefore not a major weakness;
- Maokai/Renata answered committed engage better than they answered pre-contact poke/zone/pick;
- Yorick's side route was not automatically independent against Jayce pressure plus Pantheon global response and the vulnerability of LGD's four-man unit to ranged setup;
- BLG's stronger team execution prior amplified a mechanically easier repeatable setup;
- LGD's KMS should have been `FAIL/UNRESOLVED`, making UDKC `FRAGILE`, not `STABLE`.

The correct draft conclusion is **CLEAR/STRONG BLG**, and LGD +kills should have remained draft-locked out.

Reference review:
`models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`
