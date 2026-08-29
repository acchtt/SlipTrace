# LoL v1.1 Moneyline Live Procedure — 2026-08-29

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Model:** LoL v1.1 — Moneyline + Duration Core  
**Family:** Moneyline

## 1. Scope

This procedure carries the v1.0 Moneyline workflow forward **without analytical change** while removing the obsolete v1.0 statement that Duration is retired.

Use:
`models/lol/rules/MODEL_RULES_LOL_V1.1_MONEYLINE_CORE.md`.

Duration is evaluated separately under the v1.1 Duration procedure.

---

# 2. Draft preparation

Once exact professional draft/roles and material competition context are known:

1. classify `DRAFT PRIOR = SIDE A / EVEN / SIDE B`;
2. state concrete win mechanisms for both teams;
3. include Fearless/restricted-pool context when material;
4. do not issue a pregame/immediate-postdraft betting TAKE.

---

# 3. Evidence intake

A betting assessment requires a usable synchronized game state and executable live Moneyline from the same decision window.

If stale, contradictory, greyed/non-executable, or decision-critical state is missing:

`HOLD`

No fixed screenshot-count gate applies.

---

# 4. Price-blind probability pass

From Team A perspective resolve:

`D | R | X | O | T | MECHANISM CONTRADICTION`

Then:

`D_eff = D / 0.5D / 0` for `INTACT / WEAKENING / BROKEN-or-REPLACED`

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A) = clamp(50% + 3*S pp, 15%, 85%)`

`P(B) = 100% - P(A)`

Lock probabilities before offered price is used as analytical evidence.

---

# 5. Causal interpretation

- `R`: useful role-weighted resources, not raw aggregate alone.
- `X`: realized meaningful fight/pick/turn execution, not duplicated cleanup.
- `O`: next compulsory objective/map-control cycle, not objective count alone.
- `T`: reachable composition trajectory from current state.
- structures: ML context only unless they alter forward control.

A later side/verdict reversal requires a genuine causal change in `R/X/O/T` or mechanism state.

---

# 6. Price pass

For decimal odds `O`:

`BOOK IMPLIED = 1/O`

`EDGE = MODEL WIN PROBABILITY - BOOK IMPLIED`

Frozen ML requirements:

- odds `>=1.60`;
- edge `>=+5.0pp`.

Use raw implied probability.

---

# 7. Verdict format

`ML — [TEAM A vs TEAM B]`

`Draft: [A / EVEN / B] — [one-sentence mechanism]`

`Live: R [x] | X [x] | O [x] | T [x] | Mechanism [state]`

`Model: A [xx]% / B [yy]%`

`Price: [selection] @[odds] -> book [q]% | edge [e]pp`

`Verdict: HOLD / PASS / TAKE CANDIDATE — [short causal reason]`

For TAKE CANDIDATE:

`USER_LINE_CONFIRMATION=PENDING — confirm exact TEAM ML @ODDS still exists.`

---

# 8. Confirmation / moved price

No Position while confirmation is pending.

If exact line/odds are confirmed before material state change, accepted shadow Position may be logged under current governance.

If only price changes with unchanged state, retain locked ML probability and reprice.

If game state changes materially, rebuild the probability estimate first.

---

# 9. Family independence

Moneyline and Duration may both qualify on the same map, but each must clear its own model independently.

Duration Over/Under price or central duration estimate does not change ML probability by itself.

Kill Handicap and Total Kills remain retired.

---

# 10. Position/stake controls

- position-blind reassessment;
- default shadow stake per current lock;
- actual exposure 0u;
- no rescue, martingale, chasing, averaging down or stake escalation;
- no retroactive Position creation.

---

# 11. Airtable

A pending candidate is not a Position.

Accepted ML Position preserves exact odds, entry clock/state, current model generation, shadow stake, 0u actual exposure and:

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`
