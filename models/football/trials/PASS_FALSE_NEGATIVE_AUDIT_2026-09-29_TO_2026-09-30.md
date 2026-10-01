# PASS False-Negative Audit — 2026-09-29 to 2026-09-30

**Status:** HISTORICAL AUDIT — NO PRODUCTION RULE CHANGE  
**Audit opened:** 2026-10-01 ICT

## Scope

Two completed evening slates are reviewed version-faithfully:

1. 2026-09-29 evening board — Football A was the official model.
2. 2026-09-30 evening board — Football C was the official model, with Football C2 shadow.

The 2026-09-30 morning corrected C/C2 board contained no official C-PASS among its four prospective fixtures and is not a PASS false-negative source.

No post-result state is retroactively rewritten.

---

## 1. 2026-09-29 Football A PASS audit

Frozen board:
- 14 PASS
- 7 Watchlist
- 0 Focus
- 2 unresolved

PASS FT results:

| Match | Frozen PASS reason | FT | Total goals | Diagnostic |
|---|---|---:|---:|---|
| South Sudan vs Egypt | Egypt suppression; Salah unavailable | 0-5 | 5 | CLEAR FALSE NEGATIVE |
| Mozambique vs Sudan | two low-volume routes | 4-1 | 5 | CLEAR FALSE NEGATIVE |
| Ethiopia vs Senegal | Ethiopia suppression | 0-1 | 1 | PASS HELD |
| Madagascar vs Tanzania | Tanzania suppression | 1-1 | 2 | PASS HELD |
| Ghana vs Gambia | Ghana suppression; no verified rescue | 2-4 | 6 | CLEAR FALSE NEGATIVE |
| Guinea-Bissau vs Nigeria | low-event home route; no verified 3+ ceiling | 3-0 | 3 | FALSE-NEGATIVE CANDIDATE |
| Uganda vs Libya | both routes rest on one qualifier | 1-0 | 1 | PASS HELD |
| Zambia vs Togo | no repeatability | 2-0 | 2 | PASS HELD |
| Oman vs Kuwait | game-state-dependent routes | 3-1 | 4 | CLEAR FALSE NEGATIVE |
| Finland vs Belarus | Belarus suppression | 0-0 | 0 | PASS HELD |
| Moldova vs Faroe Islands | Moldova suppression | 1-1 | 2 | PASS HELD |
| Gabon vs Niger | no verified rescue | 2-0 | 2 | PASS HELD |
| Somalia vs Cote d'Ivoire | Somalia suppression | 0-2 | 2 | PASS HELD |
| Congo vs Cameroon | Congo suppression | 1-1 | 2 | PASS HELD |

Summary:
- 14 PASS
- 4 produced 4+ goals
- 1 additional match produced exactly 3
- 9 stayed at 0-2 goals
- average FT total: 2.64

Interpretation:
Football A's old PASS logic was materially vulnerable to one-sided/self-funded carrier outcomes. This is historical context only; do not re-tune Football C from Football A's frozen board.

---

## 2. 2026-09-30 Football C Step-1 C-PASS audit

Frozen board:
- 14 C-FOCUS
- 19 C-WATCH
- 8 C-PASS

All eight C-PASS rows also failed the C2 selection floor at board epoch.

| Match | Frozen support | FT | Frozen reason | Audit classification |
|---|---:|---:|---|---|
| Fortuna Hjorring W vs PSV W | O2.25 | 0-0 | first-leg 1-0; no strong carrier | PASS HELD |
| Sporting Lagos vs Ikorodu City | O2.00 | 0-0 | neither owns strong repeatable route | PASS HELD |
| Real Sociedad W vs Hearts W | O2.25 | 4-0 | low Sociedad scoring + first-leg 0-0 suppression | DETECTABLE FALSE NEGATIVE — RESEARCH INTERPRETATION |
| Crystal Palace W vs Charlton W | O2.25 | 3-0 | Charlton scoring route too weak | DETECTABLE FALSE NEGATIVE — OPPONENT LEAKAGE / RECENCY |
| Independiente FBC vs Nacional | O2.25 | 2-2 | five straight low home totals / suppression | FALSE NEGATIVE, LIKELY VARIANCE / CUP STATE |
| Enyimba vs Shooting Stars | O2.00 | 4-2 | both routes compressed; low H2H over rate | DETECTABLE FALSE NEGATIVE — RECENCY / MECHANISM |
| Warri Wolves vs Enugu Rangers | O2.00 | 0-1 | low creation and mutual compression | PASS HELD |
| Katsina United vs Rivers United | O2.00 | 1-1 | home compression + away caution | PASS HELD / SUPPORT PUSH |

Diagnostic settlement at the frozen supported burden only:
- 4 would have cleared the frozen line
- 1 would have pushed
- 3 would have lost
- no hypothetical P/L is valid because Step 1 had no executable price

Average frozen supported line: 2.125  
Average FT goals: 2.50

### Why the four misses are not equivalent

#### Real Sociedad W vs Hearts W — research interpretation error

Frozen state:
- home route WEAK
- chance quality LOW
- failure_attacks_route = true
- material_suppression = true
- reason: recent Sociedad scoring around 0.6 and first leg 0-0

But available pre-match information stated:
- Real Sociedad had been the clearly superior side in the first leg;
- they had created numerous good chances;
- the 0-0 was attributed to poor finishing rather than absent creation;
- the return leg was 0-0 on aggregate at home and required a win to advance.

The model treated the **scoreline** as suppression while failing to preserve the underlying chance-creation mechanism.

Primary audit tag:
`C-PASS FALSE NEGATIVE — CHANCE CREATION LOST BEHIND SCORELINE`

#### Crystal Palace W vs Charlton W — opponent leakage / evidence recency error

Frozen state:
- Palace USABLE
- Charlton WEAK
- no carrier
- Charlton route weakness used as a hard suppression argument

Available recent results before kickoff included Charlton defeats:
- 0-4 vs Liverpool
- 1-4 vs London City
- 0-4 vs Brighton
- 0-1 vs Manchester City

Palace also entered after a 3-3 league match with Birmingham.

The board's evidence note summarized Charlton at roughly 0.6 scored / 1.0 conceded, which did not reflect the current defensive leakage shown by the most recent matches.

Primary audit tag:
`C-PASS FALSE NEGATIVE — WEAK SCORING ROUTE CONFUSED WITH STRONG SUPPRESSION`

A weak team scoring route does not automatically imply a low total if the same team materially leaks goals and the opponent can self-fund.

#### Enyimba vs Shooting Stars — recency / mechanism update error

Frozen state:
- WEAK / WEAK
- chance quality LOW
- material suppression
- recent H2H low-output background

But the pre-match current context included Enyimba's immediately preceding 3-2 home loss to Sporting Lagos, in which Enyimba scored twice and led twice.

The FT 4-2 itself must not be used to backfill the mechanism. However, the latest 3-2 before kickoff was available and should have prevented the home attack from being treated as fully WEAK without a stronger explanation.

Primary audit tag:
`C-PASS FALSE NEGATIVE — LATEST ROUTE EVIDENCE UNDERWEIGHTED`

#### Independiente FBC vs Nacional — likely outcome variance / knockout volatility

Frozen evidence strongly supported suppression:
- five straight Independiente home matches under 2.5;
- low current home creation;
- no verified carrier;
- independent pre-match models also leaned low total.

FT was 2-2.

There is not enough pre-match evidence to call this a model error confidently.

Primary audit tag:
`C-PASS FALSE NEGATIVE — NOT YET ACTIONABLE`

---

## 3. 2026-09-30 Football C Step-2 PASS audit

Exclude Farul-Sparta from normal PASS evaluation because its Step 2 was missed by a kickoff/schedule fault.

Valid official Step-2 PASS decisions:

| Match | Decision quote | FT | Audit |
|---|---:|---:|---|
| Brunei vs Hong Kong | PASS O4.5 @1.87 vs support O3.25 | 0-2 | PASS HELD |
| Follo vs Sarpsborg | PASS O3.5 @1.68 vs support O2.75 | 0-2 | PASS HELD |
| Roma W vs Barcelona W | PASS O4.25 @1.67 vs support O3.0 | 0-6 | MISSED OPPORTUNITY — UPPER-TAIL CEILING |
| Benfica W vs Bayern W | PASS O3.5 @1.92 vs support O2.75 | 0-3 | PASS HELD |

Summary:
- 4 genuine Step-2 C-PASS
- 3 correctly avoided losing above-support purchases
- 1 missed winner (Roma-Barcelona)

This supports retaining Football C's protected-burden discipline while investigating only the narrow elite upper-tail class.

---

## 4. Main finding

The larger current-model issue is **not Step-2 price conservatism**.

The stronger signal is at **Step 1 evidence interpretation**:

1. low scoreline can be mistaken for low chance creation;
2. a weak scoring route can be incorrectly treated as total suppression even when that team has severe defensive leakage;
3. latest route-changing evidence can be underweighted relative to older H2H / aggregate low-output summaries;
4. boolean `failure_attacks_route=true` + `material_suppression=true` is currently too capable of turning an uncertain case directly into C-PASS.

The 30 Sep sample is still only eight C-PASS fixtures. Do not change production thresholds from this sample alone.

---

## 5. Prospective recommendation

Before any production change, add a non-predictive PASS observer for C-PASS rows with one of these contradictions:

- scoreline suppression but documented high chance creation;
- WEAK scoring route + material defensive leakage;
- latest match materially stronger/open than the older sample used for the route grade;
- unresolved knockout tie where one side must win and prior low score came from finishing rather than creation.

Observer output:
- original C-PASS state;
- contradiction type;
- whether a fresh review would have promoted PASS -> WATCH without seeing market/result;
- FT only after freeze;
- no exposure and no state rewrite.

Require a prospective sample before changing C-PASS gates.
