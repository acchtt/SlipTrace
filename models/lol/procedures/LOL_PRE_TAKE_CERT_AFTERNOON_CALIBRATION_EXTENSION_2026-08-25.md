# PRE_TAKE_CERT Afternoon Calibration Extension — 2026-08-25

**Status:** ACTIVE only when incorporated by `models/lol/CURRENT_MODEL.md` and the slate's frozen authority commit.

This extension is mandatory in addition to the retained PRE_TAKE mechanical validator and, for Kill Handicap, the KH margin extension.

## A. Professional / officially sanctioned semi-professional draft dependency

If a TAKE thesis materially depends on draft analysis and the match is professional or officially sanctioned semi-professional, PRE_TAKE_CERT must resolve:

`PML_RUN | META_SOURCE_CLASS | ARCHETYPE_INVENTORY_UPDATED | PLAYER_STAGE_FIT | POCKET_TAX | DRAFT_CAUSAL_ORDER | PRO_ADVERSARIAL_PASS`

Hard rules:

- `PML_RUN = PASS` is required whenever PDRL is required.
- `META_SOURCE_CLASS` must be `PRO_ONLY`, `PRO_RELEVANT`, or `N/A` when no current meta assertion is used. Solo-queue-only evidence cannot upgrade a pro draft edge.
- For Fearless/restricted-pool Game 2+, `ARCHETYPE_INVENTORY_UPDATED = PASS` is mandatory.
- If player stage fit cannot be established, record `UNKNOWN` and apply uncertainty/pocket tax; never assume proficiency from champion reputation.
- Pocket/low-priority pro picks must either have player/team stage evidence or carry an explicit execution uncertainty tax.
- Draft reasoning must follow causal mechanisms rather than standalone labels such as more scaling, more engage, more tanks, three winning lanes, counterpick, or more meta champions.

Any omitted mandatory field is mechanical FAIL.

## B. Underdog +kills cushion asymmetry

After the side-neutral KH margin distribution is locked and the preliminary sign is selected as underdog `+H`, PRE_TAKE_CERT must record:

`DOG_CUSHION_CLASS | ONE_FIGHT_SWING_TEST | ML_LIKENESS_TEST | UCS | LAC | WMS`

Allowed `DOG_CUSHION_CLASS` values:

- `INSUFFICIENT`
- `THIN`
- `MATERIAL`
- `LARGE`

Hard rules:

- `INSUFFICIENT` => TAKE forbidden.
- `THIN` => presumptive HOLD/SKIP. It may pass only if UCS + LAC + WMS contain explicit exceptional proof that the normal one-fight/cleanup expansion tail is suppressed. Attractive price alone cannot override this.
- `MATERIAL` or `LARGE` does not itself authorize TAKE; all retained UDKC/UCS/LAC/KHMC gates still apply.
- The line number alone never defines the class. Classification is state- and distribution-dependent.

This calibration is intentionally asymmetric: a small positive handicap often fails to buy meaningful underdog protection.

## C. Favorite -kills small-line treatment

If the preliminary KH sign is favorite `-H`, PRE_TAKE_CERT must not reject solely because `ABS(H)` is small.

Require the retained side-neutral distribution, favorite mechanism validator, exact cover threshold arithmetic, WMS, lower-bound cover probability, break-even and phase/uncertainty buffer. If these pass, a small negative favorite handicap can be TAKE-eligible.

`DOG_CUSHION_CLASS` is N/A for favorite -kills.

## D. Synchronization provenance

For live ML/KH/TK snapshot eligibility, record one of:

- `SYNC_PROVENANCE = INTERNAL_MATCH`
- `SYNC_PROVENANCE = USER_CONFIRMED_SAME_STATE`

Phone/device status-bar timestamps or capture-order differences alone cannot fail synchronization when the user explicitly confirms the screenshots represent the same state. Internal contradictions still fail closed.

This does not waive the two-snapshot requirement.

## E. Workload context

If recent-series workload/fatigue is used to move a probability or draft/execution grade, PRE_TAKE_CERT must record:

`WORKLOAD_MECHANISM = <observable mechanism>`

Generic previous-day play, turnaround, travel, or long-series narrative without a concrete mechanism is `CONTEXT_ONLY` and cannot upgrade a TAKE.

## Compact extension signature

For applicable TAKES persist:

`AFT25[PML=<P/N-A>;META=<...>;ARCH=<P/N-A>;FIT=<...>;POCKET=<...>;DOGC=<.../N-A>;1F=<P/N-A>;SYNC=<...>;WORK=<.../N-A>]`

Missing required values => mechanical FAIL.
