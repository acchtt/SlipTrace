# MODEL RULES — LEAGUE OF LEGENDS v1.3 — MONEYLINE HIERARCHY CORE

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Origin:** user-authorized v1.2 weighting repair after Game 3  
**Market scope:** LIVE MONEYLINE

## 1. Objective

Estimate live map-win probability with the causal hierarchy:

`TEAM STRENGTH = LIGHT STARTING PRIOR`
`DRAFT = MEANINGFUL MAP-SPECIFIC CORRECTION`
`LIVE STATE = DOMINANT ONCE REAL EVIDENCE EXISTS`

This patch keeps the v1.2 team-strength tier but reduces its probability weight and increases the draft contribution. Duration is unchanged.

---

# 2. Team-strength prior `K`

From Team A perspective:

- `K=+2` clear major persistent team-strength edge;
- `K=+1` meaningful persistent team-strength edge;
- `K=0` no robust persistent edge;
- `K=-1` meaningful persistent disadvantage;
- `K=-2` clear major persistent disadvantage.

Allowed evidence is pre-series and price-independent only: recent official same-league performance, opponent quality/competition path, roster continuity/substitutions and established current form.

Forbidden: sportsbook odds, current-map state, same-series map results, hindsight.

Freeze `K` for a series unless a genuine roster/availability change occurs.

### Light strength baseline

`P0(A)=50%+5*K percentage points`

Discrete baselines are therefore `40/45/50/55/60%` for `K=-2/-1/0/+1/+2`.

Team strength is intentionally informative but not dominant.

---

# 3. Draft prior

Output:

`DRAFT PRIOR = SIDE A / EVEN / SIDE B`

From Team A perspective:

- Team A draft edge -> `D=+1`
- EVEN -> `D=0`
- Team B draft edge -> `D=-1`

State concrete professional win mechanisms using exact roles, patch/context, player fit and Fearless/restricted-pool constraints.

Draft is map-specific and must not absorb team reputation.

---

# 4. Live state

Score Team A perspective on `-2,-1,0,+1,+2`:

- `R` — role-weighted useful resources;
- `X` — realized meaningful fight/contact execution;
- `O` — objective access/control and next compulsory cycle;
- `T` — reachable composition trajectory from current state.

Raw aggregate kills/gold/towers/objectives are not standalone conclusions.

For ML, structures matter only through actual forward-control consequences.

---

# 5. Draft-mechanism contradiction

Classify:

- `INTACT`
- `WEAKENING`
- `BROKEN`
- `REPLACED`

Draft contribution:

- INTACT -> `D_eff=D`
- WEAKENING -> `D_eff=0.5D`
- BROKEN or REPLACED -> `D_eff=0`

`K` remains a distinct persistent layer and is not erased by draft-mechanism contradiction.

---

# 6. Probability engine

State score:

`S = 1.5*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

Final probability:

`P(A)=clamp(P0(A)+3*S percentage points,15%,85%)`

`P(B)=100%-P(A)`

Lock `K/P0`, draft/live state and both probabilities before using offered ML price as analytical evidence.

### Weight interpretation

- one `K` tier = 5pp baseline movement;
- one intact draft step = 4.5pp;
- one `R` or `X` step = 4.5pp;
- one `O` step = 3.75pp;
- one `T` step = 3pp.

Because live variables can each reach ±2 and combine, synchronized in-game evidence dominates the light pre-series prior once the map meaningfully develops.

---

# 7. Causal thesis gate — price cannot create the bet

Effective prospectively from the user instruction on 2026-08-30:

**A favorable price is necessary for value but can never create the directional betting thesis.**

Before using odds as analytical evidence, compute the selected side's non-price causal score:

`C = 1.5*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

This deliberately excludes `K/P0` and excludes price.

For a selected side to be TAKE-eligible:

- `C > 0` is required;
- there must be a coherent, currently reachable draft/live win mechanism supporting that side;
- team-strength prior alone does not satisfy the gate;
- a long underdog price cannot rescue a side whose draft/live causal state is neutral or negative;
- if `C <= 0`, verdict is `PASS` even when model-vs-book edge exceeds the numerical threshold.

This gate does not change the probability formula. It is an execution-quality interlock preventing price-only contrarian entries.

---

# 8. Price decision

For decimal odds `O`:

`BOOK IMPLIED q=1/O`

`EDGE=MODEL PROBABILITY-q`

TAKE CANDIDATE requires:

- causal thesis gate `C>0` for the selected side;
- synchronized executable live Moneyline;
- odds `>=1.60`;
- edge `>=+5.0pp`;
- price-independent `K/P0`;
- probability locked before price use;
- position-blind reassessment;
- fresh internally consistent evidence;
- actual exposure `0u`;
- no chasing/rescue/martingale/stake escalation.

Use raw implied probability during the initial v1.3 validation epoch.

---

# 9. Verdicts / live-only scope

`HOLD` — state/market/prior cannot be scored responsibly.

`PASS` — usable state but no executable side clears requirements, including the causal thesis gate.

`TAKE CANDIDATE` — requirements pass; set `USER_LINE_CONFIRMATION=PENDING`.

No pregame or immediate-postdraft betting TAKE.

No Position exists until exact quoted ML is confirmed before material state change.

---

# 10. Compact record

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;C=...;S=...;P=...;BOOK=...;EDGE=...;THESIS=P;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`
