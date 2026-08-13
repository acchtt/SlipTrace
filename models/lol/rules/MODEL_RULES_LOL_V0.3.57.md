# MODEL RULES — LEAGUE OF LEGENDS v0.3.57

**Status:** Active delta
**Effective date:** 2026-08-13 UTC+7
**Supersedes:** v0.3.56 only where stated

## Purpose

Prevent false `STABLE` fallback classifications. The triggering error was WBG Gnar/Lee Sin/Annie/Mel/Rell being treated as resilient merely because it had several engage/peel tools. Forcing redundancy is not survival redundancy.

## 1. STABLE is a positive certification

For any underdog +kills evaluation, `FF = STABLE` may be assigned only after all four critical tests pass matchup-relative opponent-counter testing:

1. **Failed-Engage Reset Test (FER):** after the primary engage/access sequence fails or trades poorly, the team can disengage and reform without sacrificing the protected damage source or multiple members.
2. **Protected-DPS Continuation Test (PDC):** at least one reliable damage source can continue dealing damage through/after enemy first contact with credible protection that does not depend on the same all-in resources used to initiate.
3. **Pressured Space Test (PST):** at least one of objective entry or wave/base defense remains functional while behind without requiring a face-check, perfect flank, or immediate all-in.
4. **Alternative Route Independence (ARI):** at least one lower-variance fallback route remains that does not share the same champions, timing window, terrain requirement, or primary failure cluster as the preferred engage/access plan.

If any critical test is unresolved or fails, `STABLE` is forbidden for underdog +kills.

## 2. Forcing redundancy != fallback redundancy

Score separately:

- `FRI` — Forcing Route Independence;
- `SRI` — Survival Route Independence.

Multiple engage, pick, CC, flank or re-engage tools can raise FRI while SRI remains LOW.

Never use the following as proof of STABLE by themselves:

- multiple engage buttons;
- multiple CC champions;
- generic peel labels;
- generic waveclear;
- range;
- scaling;
- one champion that can either engage or peel but cannot reliably do both in the same failed-contact branch.

## 3. False-Stable Guard

`FF = STABLE` is automatically blocked when any of these apply and are not independently disproven:

- the fallback description is mainly another engage/re-engage/pick sequence;
- primary peel resources are also required for initiation;
- multiple members must step forward into the opponent's control envelope to execute the main plan;
- the damage source loses protection when the engage line commits;
- objective entry while behind requires the same all-in route as the primary plan;
- the opponent has repeatable range/pick/disengage/re-engage that punishes failed contact and no clean reset route is demonstrated;
- champion-role/function uncertainty prevents a confident matchup-relative certification.

When the False-Stable Guard is active, classify FF as `FRAGILE` or `ABSENT`.

## 4. Conservative DCR tie-break

For underdog +kills only, when DCR is materially ambiguous between MEDIUM and HIGH, use `HIGH` if the opponent has at least two repeatable punish/continuation routes and the underdog's failed-contact branch can expose multiple members.

This is an eligibility tie-break, not a general map-win probability rule.

## 5. Fail-closed underdog +kills gate

Order is mandatory:

1. MKT + TEAM underdog identity;
2. DER;
3. FRI;
4. SRI;
5. FER;
6. PDC;
7. PST;
8. ARI;
9. False-Stable Guard;
10. DCR;
11. FF certification;
12. v0.3.56 HARD Draft-Collapse Veto;
13. RIT only if veto inactive;
14. signed-margin / NKB / RFI / KCV / Structure Substitution pricing.

If the certification is incomplete, ambiguous, or unavailable: **PASS/HOLD. Never TAKE underdog +kills.**

## 6. No live upgrade

Ordinary live events cannot upgrade `FRAGILE/ABSENT/UNCERTIFIED` to `STABLE` for underdog +kills. Kill parity, return kills, temporary role-gold gains, objective parity, larger cushions, or two-snapshot eligibility do not change the certification.

Only a draft-input correction may reopen certification.

## 7. WBG vs NIP Game 3 reference correction

WBG: Gnar / Lee Sin / Annie / Mel / Rell
NIP: Tristana / Xin Zhao / Twisted Fate / Ashe / Seraphine

Correct underdog +kills classification:

- WBG FRI: meaningful;
- WBG SRI: insufficient;
- WBG FER/PDC/PST/ARI: not all certified;
- False-Stable Guard: ACTIVE;
- WBG DCR: HIGH for handicap eligibility;
- WBG FF: FRAGILE;
- v0.3.56 hard veto: ACTIVE.

Therefore WBG +8.5 kills @1.951 at 20:12 was **TAKE-ineligible**. Correct verdict: `PASS — WBG +8.5 kills @1.951 — 0u.`

## 8. Retained controls

All non-conflicting v0.3.56 and earlier controls remain active. Favorite -kills remains independent; a blocked underdog +kills position never implies a favorite -kills TAKE. ML, TK and Duration retain their separate gates.

Where earlier language allows engage redundancy, live success, or generic peel to certify resilience, **v0.3.57 controls**.
