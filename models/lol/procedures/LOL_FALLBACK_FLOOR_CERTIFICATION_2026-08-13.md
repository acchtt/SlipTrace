# LoL Fallback Floor Certification — 2026-08-13

**Status:** Mandatory under LoL v0.3.57; retained and amended in canonical LoL v0.3.58
**Purpose:** mechanically prevent false `STABLE` fallback labels before any underdog +kills decision.

Complete internally before pricing the handicap. Do not use the displayed +kills line as evidence.

## A. Separate forcing from survival

Score:

- `FRI` — Forcing Route Independence: LOW / MEDIUM / HIGH
- `SRI` — Survival Route Independence: LOW / MEDIUM / HIGH

Engage redundancy does not imply survival redundancy.

## B. Four critical certification tests

For the underdog, mark each `PASS / FAIL / UNRESOLVED`:

1. `FER` — Failed-Engage Reset: can the team disengage and reform after primary contact fails without losing the carry or several members?
2. `PDC` — Protected-DPS Continuation: can at least one damage source continue through/after first contact with protection that does not consume the same resources required to engage?
3. `PST` — Pressured Space: can the team either enter an objective or defend waves/base while behind without face-checking, perfect flank, or immediate all-in?
4. `ARI` — Alternative Route Independence: is there a lower-variance route that does not share the same champions, timing, terrain, and failure cluster as the primary plan?

`FF = STABLE` requires all four PASS.

Any FAIL or UNRESOLVED => STABLE is forbidden.

## B2. Kill Production vs Kill-Margin Suppression — mandatory v0.3.58 amendment

Before `STABLE`, separately certify both of these questions:

- `KPA` — Kill Production Ability: can the underdog still generate kills while behind?
- `KMS` — Kill-Margin Suppression: can the underdog plausibly prevent the favorite from repeatedly converting advantages into **net kill-margin expansion**?

Classify each `PASS / FAIL / UNRESOLVED`.

`STABLE` requires **KPA = PASS and KMS = PASS** in addition to FER/PDC/PST/ARI.

Do not infer KMS merely because the underdog has:

- engage or counter-engage;
- scaling frontline;
- safe waveclear;
- one pick champion;
- a safe marksman;
- utility/disengage;
- theoretical return-kill tools.

Those can support kill production without suppressing the favorite's final margin.

For KMS, explicitly test the opponent's repeatable routes:

1. range/zone control;
2. first-contact reliability;
3. re-engage and continuation after first contact;
4. siege/structure conversion that forces later defensive entries;
5. objective-entry control;
6. ability to punish the same underdog failure cluster repeatedly;
7. whether underdog damage access remains conditional on entering controlled space.

If the favorite has multiple independent repeatable routes and the underdog's kill plan shares one fragile entry/reset dependency, KMS is FAIL/UNRESOLVED and `STABLE` is forbidden.

### Team-strength prior modifier

Team strength is a modifier, never a standalone veto.

When the favorite has a materially stronger execution prior **and** also owns superior repeatable control/zone/siege/continuation routes, the burden of proof for KMS increases. Do not neutralize that interaction merely because the underdog draft contains theoretically functional fallback tools.

This does not authorize favorite -kills by itself; favorite -kills still requires its separate FFD/RNE live gates.

Reference:
`models/lol/reviews/KC_GX_G1_UNDERDOG_KILLS_FALSE_STABLE_REVIEW_2026-08-18.md`

## B3. Role-Leverage Decomposition — mandatory v0.3.58 clarification

Before `KMS = PASS`, classify **RLD — Role-Leverage Decomposition** as `PASS / FAIL / UNRESOLVED`.

RLD must answer:

1. Where is each side's meaningful gold/level advantage concentrated: top, jungle, mid, ADC, support?
2. Which pockets convert directly into the next compulsory grouped fights, protected DPS, objective turn, siege or re-engage?
3. Does an underdog top-side lead create an **independent kill-margin-suppression route**, or is it only isolated lane value?
4. Are grubs/towers/objective assets creating real kill-margin suppression, or only structure/tempo leverage?
5. Does the favorite hold carry-centered economy plus cleaner grouped access/control while the underdog's resistance is localized elsewhere?

Hard interpretation:

- if favorite carry leverage + grouped control is materially stronger and the underdog's resistance is mainly isolated top/grubs without an independent suppressive route, `KMS = PASS` is forbidden;
- `RLD = UNRESOLVED` forbids `FF = STABLE`;
- grubs are never automatic KMS evidence;
- no fixed lane-value multiplier is introduced — top gold may be highly valuable when it creates side-lane inevitability, reliable flank/access, durable frontline control or another independent suppressive mechanism.

Reference:
`models/lol/reviews/DNS_BRO_G1_UNDERDOG_KILLS_ROLE_LEVERAGE_AND_DURATION_EXECUTION_REVIEW_2026-08-19.md`

## B4. Pre-live UDKC hard lock — mandatory v0.3.58 enforcement

Before the first live state is used to evaluate an underdog +kills market, create a complete **UDKC — Underdog +Kills Draft Certificate** from draft/team inputs only.

The UDKC consists of the full Eligibility Output in section E and must be completed after draft lock but before live-state reasoning for this market.

Hard rules:

- every field must be explicitly resolved; omitted, implied, narrative-only, or `UNRESOLVED` fields mean `UNCERTIFIED`;
- the UDKC must be persisted in the map's post-draft audit trail or latest live handoff so a new chat can verify it;
- if a new chat begins mid-map and cannot locate a complete persisted pre-live UDKC, underdog +kills is `UNCERTIFIED — HOLD/PASS FOR THIS MAP`;
- do not reconstruct a missing certificate from a live scoreboard after the fact;
- live evidence may preserve or downgrade a pre-live STABLE classification but may never create, fill, or upgrade one;
- exact current kill margin, NKB, a large displayed +kills cushion, low current gold separation, 0-0 towers, grubs, safe ADC play, peel, waveclear, scaling, or theoretical return kills cannot create KMS or FF=STABLE.

Mandatory guard:
`models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

Reference incident:
`models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`

## C. False-Stable Guard

Set `ACTIVE` if any material condition remains:

- fallback is described mainly as another engage/re-engage/pick;
- peel resources are also primary initiation resources;
- several members must commit forward together;
- carry protection disappears when initiation starts;
- behind-state objective entry repeats the same all-in dependency;
- opponent has repeatable range/pick/disengage/re-engage and the underdog lacks a demonstrated reset route;
- opponent has repeatable range/zone/siege/continuation while the underdog's kill routes require entering the same controlled space;
- the analysis shows kill-production tools but cannot independently explain how the underdog suppresses favorite net kill-margin expansion;
- a materially stronger favorite execution prior combines with superior repeatable control routes and KMS remains unresolved;
- favorite carry-centered leverage plus cleaner grouped control is being offset mainly by isolated underdog top/grub resistance without an independent suppressive route;
- role/champion-function uncertainty prevents confident certification.

If ACTIVE: classify FF as `FRAGILE` or `ABSENT`.

## D. DCR conservative tie-break

For underdog +kills, if DCR is between MEDIUM and HIGH, use HIGH when:

- failed contact can expose multiple members; and
- opponent has at least two repeatable punish/continuation routes.

## E. Eligibility output

Record internally before any underdog +kills verdict:

- MKT/TEAM underdog;
- DER;
- FRI;
- SRI;
- FER;
- PDC;
- PST;
- ARI;
- KPA;
- KMS;
- RLD;
- False-Stable Guard ACTIVE/INACTIVE;
- DCR;
- FF;
- v0.3.56 HARD Draft-Collapse Veto ACTIVE/INACTIVE.

For a valid pre-live UDKC:

- FER/PDC/PST/ARI/KPA/KMS/RLD must all be PASS;
- False-Stable Guard must be INACTIVE;
- FF must be STABLE;
- hard Draft-Collapse Veto must be INACTIVE.

If any certification field is missing or unresolved: `PASS/HOLD`.

If hard veto is ACTIVE: stop. Do not run RIT or handicap pricing looking for an exception.

## F. Lock rule

Ordinary live evidence cannot upgrade `FRAGILE`, `ABSENT`, or `UNCERTIFIED` to `STABLE` for underdog +kills. Only a genuine draft-input correction may reopen the certification.

A missing persisted pre-live UDKC is `UNCERTIFIED`, not an invitation to certify from live evidence.

Live evidence may only preserve or downgrade an already-complete pre-live STABLE UDKC.

## G. Pre-structure control note

`0-0 towers` is neutral. It must not be used as an implicit anti-control signal in underdog +kills reassessment.

A favorite may already have a strong control state before the first structure falls. When evaluating whether a previously certified underdog fallback is still behaving as expected, distinguish:

- **no structural conversion yet**, from
- **absence of favorite control**.

A material economy lead, clean fight/kill lead, role-distributed pressure, superior range/zone/access and favorable compulsory-objective schedule can jointly indicate pre-structure control even at 0-0 towers.

No single signal — including gold lead, kill lead, team strength or 0-0 towers — is decisive by itself.
