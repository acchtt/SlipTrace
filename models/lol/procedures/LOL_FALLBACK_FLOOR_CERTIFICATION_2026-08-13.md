# LoL Fallback Floor Certification — 2026-08-13

**Status:** Mandatory under LoL v0.3.57
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

## C. False-Stable Guard

Set `ACTIVE` if any material condition remains:

- fallback is described mainly as another engage/re-engage/pick;
- peel resources are also primary initiation resources;
- several members must commit forward together;
- carry protection disappears when initiation starts;
- behind-state objective entry repeats the same all-in dependency;
- opponent has repeatable range/pick/disengage/re-engage and the underdog lacks a demonstrated reset route;
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
- False-Stable Guard ACTIVE/INACTIVE;
- DCR;
- FF;
- v0.3.56 HARD Draft-Collapse Veto ACTIVE/INACTIVE.

If any certification field is missing or unresolved: `PASS/HOLD`.

If hard veto is ACTIVE: stop. Do not run RIT or handicap pricing looking for an exception.

## F. Lock rule

Ordinary live evidence cannot upgrade `FRAGILE`, `ABSENT`, or `UNCERTIFIED` to `STABLE` for underdog +kills. Only a genuine draft-input correction may reopen the certification.
