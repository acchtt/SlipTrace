# MODEL RULES — LEAGUE OF LEGENDS v1.1 — MONEYLINE CORE

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Origin:** analytical core carried forward unchanged from LoL v1.0 Moneyline Core  
**Market scope:** LIVE MONEYLINE

## 1. Objective

Estimate each team's current map-win probability from synchronized professional live state, lock that probability before using offered price as analytical evidence, then compare it with executable Moneyline odds.

The v1.1 scope extension does **not** change the Moneyline weights, probability mapping, odds floor or edge requirement from v1.0.

---

# 2. Draft prior

Output:

`DRAFT PRIOR = SIDE A / EVEN / SIDE B`

State one concrete professional win mechanism for each side using decision-relevant role, patch, player-fit, lane/map access, composition timing and Fearless/restricted-pool context.

For Team A perspective:

- Team A draft edge -> `D = +1`
- EVEN -> `D = 0`
- Team B draft edge -> `D = -1`

Draft is a small prior, not a permanent veto.

---

# 3. Live state

Score Team A perspective on `-2,-1,0,+1,+2`:

- `R` — role-weighted resources: where useful gold/levels/items sit;
- `X` — realized fight/contact execution: what meaningful contact has actually demonstrated;
- `O` — objective access/control and next compulsory cycle;
- `T` — composition trajectory: whether current timing/scaling/assignments make the demonstrated mechanism easier or harder.

Raw kills, aggregate gold, towers or objective counts are not standalone conclusions.

For ML, towers/structures are context by default and enter only through real forward-control consequences such as first move, vision depth, side pressure, cross-map terminal threat or base access.

---

# 4. Mechanism contradiction

Classify the original draft thesis:

- `INTACT`
- `WEAKENING`
- `BROKEN`
- `REPLACED`

Numeric draft contribution:

- INTACT -> `D_eff = D`
- WEAKENING -> `D_eff = 0.5D`
- BROKEN or REPLACED -> `D_eff = 0`

REPLACED never automatically inverts the old prior; the replacement mechanism earns probability through live `R/X/O/T`.

A directional/verdict reversal requires genuine causal change in live state or mechanism status, not price movement or descriptive-stat movement alone.

---

# 5. Probability engine — unchanged from v1.0

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

`P(A) = clamp(50% + 3*S percentage points, 15%, 85%)`

`P(B) = 100% - P(A)`

Lock both probabilities before using offered Moneyline price as evidence.

---

# 6. Price decision — unchanged from v1.0

For decimal odds `O`:

`BOOK IMPLIED q = 1/O`

`EDGE = MODEL PROBABILITY - q`

TAKE CANDIDATE requires:

- executable synchronized live Moneyline;
- odds `>=1.60`;
- edge `>=+5.0pp`;
- probability locked before price use;
- position-blind reassessment;
- fresh internally consistent evidence;
- actual exposure `0u`;
- no chasing/martingale/rescue/stake escalation.

Use raw implied probability in the initial validation epoch.

---

# 7. Verdicts

`HOLD` — state/market insufficient, stale, contradictory or unsynchronized.

`PASS` — usable state but no executable ML side clears the fixed price/edge and execution requirements.

`TAKE CANDIDATE` — a side qualifies analytically, then set:

`USER_LINE_CONFIRMATION=PENDING`

No Position exists until the exact quoted ML/odds are explicitly confirmed.

---

# 8. Live-only scope

No pregame or immediate-postdraft betting TAKE.

There is no universal fixed snapshot-count gate. One state may be enough if it supports responsible `R/X/O/T` scoring; many screenshots may still be insufficient if they add no causal information.

---

# 9. Active market relationship

Under v1.1, Duration is independently active through its own rules and procedure.

Do not use Duration state/price as automatic ML evidence, and do not import historical KH/TK/Duration gate trees into ML.

Kill Handicap and Total Kills remain retired from betting.

---

# 10. Compact internal record

`ML_CORE[D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`
