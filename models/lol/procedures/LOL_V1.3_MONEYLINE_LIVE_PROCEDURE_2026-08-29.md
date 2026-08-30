# LoL v1.3 Moneyline Live Procedure — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.3 — Hierarchy Moneyline + Duration Core  
**Family:** Moneyline

## 1. Scope

Use `models/lol/rules/MODEL_RULES_LOL_V1.3_MONEYLINE_HIERARCHY_CORE.md`.

Duration remains independently governed by the unchanged v1.1 Duration Core and procedure.

---

## 2. Strength prior

Before live pricing, assign/freeze `K=-2..+2` from pre-series non-price evidence only.

`P0=50%+5*K pp`

For a mid-series activation, reconstruct/freeze the same `K` tier from evidence that existed before Game 1. Same-series results and sportsbook prices cannot choose `K`.

---

## 3. Draft

Resolve exact roles and mechanisms, then classify `D=+1/0/-1` from Team A perspective.

Draft is a meaningful map-specific correction. Do not mix team reputation into `D`.

No immediate-postdraft betting TAKE.

---

## 4. Evidence intake

A betting assessment requires synchronized live state and executable live ML from the same decision window.

If stale, contradictory, greyed/non-executable, or decision-critical state is missing: `HOLD`.

---

## 5. Price-blind probability and thesis pass

Resolve:

`K | P0 | D | R | X | O | T | MECHANISM`

`D_eff=D / 0.5D / 0` for `INTACT / WEAKENING / BROKEN-or-REPLACED`.

`C=1.5*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

`S=C`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

`P(B)=100%-P(A)`

Lock probability before reading offered price as analytical evidence.

For each potential selection, evaluate its own perspective. A selected side is not TAKE-eligible unless:

- its non-price causal score `C>0`;
- its draft/live win mechanism is coherent and currently reachable.

Team strength alone cannot satisfy this thesis gate. If `C<=0`, the side is `PASS` regardless of how attractive its odds later appear.

---

## 6. Interpretation hierarchy

- `K`: light persistent starting prior only.
- `D`: map-specific composition/mechanism correction.
- `R/X/O/T`: dominant as synchronized live evidence accumulates.
- structures: contextual for ML unless forward control changes.

Do not protect a favorite merely because `K` favors it. Do not erase persistent team quality from one isolated early event either; score the actual live variables.

Most importantly: **price cannot create the thesis**. Never take a side merely because the bookmaker number is long relative to a model probability when the draft/live causal state does not positively support that side.

---

## 7. Price pass

Only after probability and thesis are locked:

`BOOK=1/odds`

`EDGE=P_model-BOOK`

Requirements:

- selected-side causal thesis `C>0`;
- odds >=1.60;
- edge >=+5.0pp;
- synchronized executable ML;
- position-blind;
- actual exposure 0u.

If edge passes but thesis fails: `PASS — PRICE ONLY / NO POSITIVE CAUSAL THESIS`.

---

## 8. Verdict format

`ML — [A vs B]`

`Strength: K [x] | P0 [xx]%`

`Draft: [A / EVEN / B] — [mechanism]`

`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`

`Thesis: C [x] | PASS/FAIL`

`Model: A [xx]% / B [yy]%`

`Price: [selection] @[odds] -> book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [cause]`

For candidate:

`USER_LINE_CONFIRMATION=PENDING — confirm exact TEAM ML @ODDS still exists.`

---

## 9. State change / confirmation

Material state change expires a pending candidate and requires a fresh live pass while retaining frozen `K/P0`.

Price-only movement with unchanged state may reuse locked probability and thesis state for that decision window, then reprice.

No accepted Position without timely exact user confirmation.

No retroactive accepted Position creation.

---

## 10. Controls

- shadow stake from current lock;
- actual exposure 0u;
- no martingale/rescue/chasing/averaging down/stake escalation;
- Moneyline and Duration independent;
- KH/TK remain retired.
