# LoL v1.2 Moneyline Live Procedure — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.2 — Strength-Prior Moneyline + Duration Core  
**Family:** Moneyline

## 1. Scope

Use:
`models/lol/rules/MODEL_RULES_LOL_V1.2_MONEYLINE_STRENGTH_PRIOR_CORE.md`.

Duration remains independently governed by the unchanged v1.1 Duration Core and live procedure.

---

# 2. Strength-prior preparation

Before the first draft of a series, from Team A perspective:

1. assign `K=-2..+2` using only pre-series non-price evidence allowed by the rules;
2. state one sentence explaining the strength gap;
3. compute `P0(A)=50%+10*K pp`;
4. freeze `K/P0` for the whole series unless a genuine roster/availability change occurs.

If v1.2 is activated mid-series, reconstruct `K` solely from evidence that existed before Game 1. Do not use earlier maps in the same series to choose `K`.

If a defensible `K` cannot be established:

`ML — HOLD — TEAM-STRENGTH PRIOR UNRESOLVED`

Do not use sportsbook price to resolve the uncertainty.

---

# 3. Draft preparation

Once exact draft/roles and competition context are known:

1. classify `DRAFT PRIOR = SIDE A / EVEN / SIDE B`;
2. state concrete win mechanisms for both teams;
3. include player fit and Fearless/restricted-pool context where material;
4. do not issue a pregame/immediate-postdraft betting TAKE.

---

# 4. Evidence intake

A betting assessment requires usable synchronized game state and executable live Moneyline from the same decision window.

If stale, contradictory, greyed/non-executable, or decision-critical evidence is missing:

`HOLD`

No universal fixed screenshot-count gate applies.

---

# 5. Price-blind probability pass

From Team A perspective resolve:

`K | P0 | D | R | X | O | T | MECHANISM CONTRADICTION`

Then:

`D_eff = D / 0.5D / 0` for `INTACT / WEAKENING / BROKEN-or-REPLACED`

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A)=clamp(P0(A)+3*S pp,15%,85%)`

`P(B)=100%-P(A)`

Lock both probabilities before offered price is used as analytical evidence.

---

# 6. Causal interpretation

- `K`: persistent pre-series team quality only; never sportsbook price or same-series map result.
- `D`: map-specific composition/draft edge only.
- `R`: useful role-weighted resources, not aggregate gold alone.
- `X`: realized meaningful contact execution, not duplicated cleanup.
- `O`: next compulsory objective/map-control cycle, not count alone.
- `T`: reachable composition trajectory from current state.
- structures: ML context only unless forward control changes.

Do not force team reputation into `D`. Do not erase `K` merely because the draft mechanism weakens.

---

# 7. Price pass

For decimal odds `O`:

`BOOK IMPLIED = 1/O`

`EDGE = MODEL WIN PROBABILITY - BOOK IMPLIED`

Frozen v1.2 ML requirements:

- odds `>=1.60`;
- edge `>=+5.0pp`.

Use raw implied probability.

---

# 8. Verdict format

`ML — [TEAM A vs TEAM B]`

`Strength: K [x] | P0 [xx]% — [one-sentence non-price basis]`

`Draft: [A / EVEN / B] — [one-sentence mechanism]`

`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [selection] @[odds] -> book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [short causal reason]`

For TAKE CANDIDATE:

`USER_LINE_CONFIRMATION=PENDING — confirm exact TEAM ML @ODDS still exists.`

---

# 9. Confirmation / state change

No Position while confirmation is pending.

If exact quote is confirmed before material state change, accepted shadow Position may be logged.

Price-only movement with unchanged state -> retain locked probability and reprice.

Material state change -> rebuild `R/X/O/T` and mechanism first; `K/P0` remain frozen.

---

# 10. Position / family controls

- position-blind reassessment;
- default shadow stake from current lock;
- actual exposure `0u`;
- no rescue, martingale, chasing, averaging down or stake escalation;
- no retroactive Position creation;
- Moneyline and Duration qualify independently;
- Kill Handicap and Total Kills remain retired.

Accepted ML Position preserves:

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`
