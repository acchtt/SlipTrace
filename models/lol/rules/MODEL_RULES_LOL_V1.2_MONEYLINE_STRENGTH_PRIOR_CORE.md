# MODEL RULES — LEAGUE OF LEGENDS v1.2 — MONEYLINE STRENGTH-PRIOR CORE

**Status:** CANDIDATE UNTIL `CURRENT_MODEL.md` ACTIVATION  
**Origin:** v1.1 Moneyline Core plus explicit repair for missing team-strength prior  
**Market scope:** LIVE MONEYLINE

## 1. Objective

Estimate current map-win probability from an independent pre-series team-strength prior, draft mechanism and synchronized professional live state. Lock probability before offered Moneyline price is used as analytical evidence.

This patch fixes a mechanical omission in v1.1: materially different teams were forced to begin from a neutral 50% baseline before draft/live evidence.

---

# 2. Team-strength prior `K`

From Team A perspective score exactly one of:

- `K=+2` — clear major persistent team-strength edge;
- `K=+1` — meaningful persistent team-strength edge;
- `K=0` — no robust persistent edge;
- `K=-1` — meaningful persistent disadvantage;
- `K=-2` — clear major persistent disadvantage.

Allowed evidence must be available before the series begins and independent of sportsbook price:

- recent official same-league series/map results;
- opponent quality and competition path/seed context;
- roster continuity, substitutions and role stability;
- sufficiently established current-form evidence.

Forbidden inputs:

- sportsbook odds or implied probability;
- current-map price movement;
- current-map live state;
- earlier map results from the same series when assigning the series prior;
- hindsight from the eventual result.

For a series, `K` is locked before the first draft and remains fixed for every map unless a genuine roster/availability change occurs. If v1.2 activates mid-series, reconstruct `K` only from evidence that existed before Game 1 and freeze it prospectively.

Team-strength baseline:

`P0(A) = 50% + 10*K percentage points`

Thus the discrete baseline is `30/40/50/60/70%` for `K=-2/-1/0/+1/+2`.

This baseline is intentionally larger than one draft step: persistent team quality should matter more than a slight composition edge, while live state can still overcome it.

---

# 3. Draft prior

Output:

`DRAFT PRIOR = SIDE A / EVEN / SIDE B`

State concrete professional win mechanisms using exact roles, current patch/context, player fit and Fearless/restricted-pool constraints.

For Team A perspective:

- Team A draft edge -> `D=+1`
- EVEN -> `D=0`
- Team B draft edge -> `D=-1`

Draft remains a small map-specific prior and does not replace `K`.

---

# 4. Live state

Score Team A perspective on `-2,-1,0,+1,+2`:

- `R` — role-weighted useful resources;
- `X` — realized meaningful fight/contact execution;
- `O` — objective access/control and next compulsory cycle;
- `T` — composition trajectory from the current reachable state.

Raw aggregate gold, kills, towers or objective count are not standalone conclusions.

For ML, structures remain contextual unless they create real forward-control consequences.

---

# 5. Mechanism contradiction

Classify the original draft thesis:

- `INTACT`
- `WEAKENING`
- `BROKEN`
- `REPLACED`

Draft contribution:

- INTACT -> `D_eff=D`
- WEAKENING -> `D_eff=0.5D`
- BROKEN or REPLACED -> `D_eff=0`

`K` is not erased by draft-mechanism contradiction. Team strength and the current draft mechanism are different causal layers.

---

# 6. Probability engine

Live/draft state score:

`S = 1.0*D_eff + 1.5*R + 1.5*X + 1.25*O + 1.0*T`

Final map-win probability:

`P(A) = clamp(P0(A) + 3*S percentage points, 15%, 85%)`

`P(B) = 100% - P(A)`

Lock `K`, `P0`, state variables and both probabilities before offered Moneyline price is used as analytical evidence.

Price is never allowed to choose or adjust `K`.

---

# 7. Price decision

For decimal odds `O`:

`BOOK IMPLIED q = 1/O`

`EDGE = MODEL PROBABILITY - q`

TAKE CANDIDATE requires:

- synchronized executable live Moneyline;
- odds `>=1.60`;
- edge `>=+5.0pp`;
- `K/P0` locked independently of price;
- current probability locked before price use;
- position-blind reassessment;
- fresh internally consistent evidence;
- actual exposure `0u`;
- no chasing, rescue, martingale or stake escalation.

Use raw implied probability during the initial v1.2 ML validation epoch.

---

# 8. Verdicts and live-only scope

`HOLD` — evidence/market/strength prior cannot be scored responsibly.

`PASS` — usable state but no executable side clears requirements.

`TAKE CANDIDATE` — analytical/execution requirements pass and exact user line confirmation becomes pending.

No pregame or immediate-postdraft betting TAKE.

---

# 9. Compact record

`ML_CORE[K=...;P0=...;D=...;MC=...;R=...;X=...;O=...;T=...;S=...;P=...;BOOK=...;EDGE=...;SYNC=P;EXEC=P;ODDS=P;POSBLIND=P;EXPOSURE=0u]`
