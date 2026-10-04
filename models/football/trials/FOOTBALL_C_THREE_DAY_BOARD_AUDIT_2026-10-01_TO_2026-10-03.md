# Football C three-day whole-board audit — 1–3 October 2026

**Audit date:** 4 October 2026  
**Board-date scope:** 1 Oct, 2 Oct, 3 Oct ICT  
**Included:** the 3 Oct overnight board extending into early 4 Oct  
**Official authority:** Football C  
**Shadow:** Football C2 version-faithful; Football C3 only from its later activation boundary  
**Audit mode:** whole-board, hindsight-safe, process + selection + execution separated

## 1. Audit rules

This audit does not rewrite historical states from FT.

For each historical board:
- preserve frozen C/C2 state, rank, lane and supported burden;
- settle only the exact frozen supported burden when a result is known;
- treat frozen supported-line settlement as a diagnostic, not betting P/L;
- keep official model exposure separate from user execution;
- distinguish model false positives/negatives from process, coverage and execution faults;
- do not score C3 retrospectively on boards frozen before C3 activation.

Support diagnostic scale:
- full win = +1
- half win = +0.5
- push = 0
- half loss = -0.5
- full loss = -1

This support-value is not profit because it ignores price and exposure.

## 2. Boards audited

Seven board freezes are in scope:

1. 1 Oct 07:37–13:00
2. 1 Oct 13:00–2 Oct 03:00
3. 2 Oct 07:25–13:00
4. 2 Oct 16:27–3 Oct 03:00
5. 3 Oct 07:44–12:00
6. 3 Oct 14:11–21:00 reassessment
7. 3 Oct 20:02–4 Oct 06:00 overnight reassessment

The 1 Oct boards already had a version-faithful post-slate audit. This report carries that audit forward rather than reconstructing 1 Oct with later model rules.

## 3. Executive verdict

The evidence does not support a simple claim such as “all two-route matches are bad.”

The stronger diagnosis is:

1. Football C still over-credits route availability as burden-completion evidence in some promoted matches.
2. Continuation/control-endpoint calibration remains a real problem.
3. C-PASS has been too aggressive as a screening state.
4. Operational FOLLOW itself was not the main Oct 2–3 problem.
5. Workflow integrity still materially affects the board universe.

No Football C predictive threshold is changed by this audit.

## 4. 1 October — existing audit carried forward

### Board A — 07:37–13:00

Funnel:
- 5 raw
- 1 hard excluded
- 4 admitted
- C: 2 FOCUS / 1 WATCH / 1 PASS
- operational: 0 FOLLOW / 1 RESERVE / 3 STOP

Verified outcomes:
- Khovd Western–Deren: FOCUS/RESERVE O3.0 -> 1-5 -> clear
- Atlético Nacional–Junior: FOCUS/STOP O2.5 -> 3-1 -> clear
- CD FAS–Isidro Metapán: WATCH/STOP -> postponed
- Sacramento–Las Vegas: PASS/STOP O2.0 -> 3-2 -> clear false negative

### Board B — 13:00–03:00

Funnel:
- 55 admitted
- C: 20 FOCUS / 19 WATCH / 16 PASS
- operational: 5 FOLLOW / 4 RESERVE / 46 STOP
- C2: 22 FOCUS / 16 WATCH / 17 PASS

Key FOLLOW outcomes:
- Man City W–Real Madrid W O3.0 -> 1-1 -> official entry LOSS
- Ireland–Austria frozen O2.75 -> 2-2; protected official execution O2.0 -> WIN
- Germany–Serbia O2.75 -> 2-0; WAIT/no entry protected from loss
- HB Køge W–Servette W O2.75 -> 5-1; PRE quote stale/unavailable, no entry
- Madla–Viking O3.0 -> 0-3; FOLLOW process omission, no Step-2 state

Key RESERVE:
- Al Shamal–Muaither O2.75 -> 2-1 -> half-win diagnostically
- Austria Wien W–Inter W O2.75 -> 1-1; activated O2.5 -> LOSS
- Dubai United–Hatta O2.75 -> 3-2 -> reserve opportunity cost
- Sha Tin–Hong Kong FC O2.75 -> 2-2 after 90 -> WAIT target not executable

Persisted routine C exposure:
- 1W–2L
- **-1.25u**

### Oct 1 PASS diagnosis

Among 11 clean played football-quality C-PASS rows:
- 8 cleared frozen support
- 2 pushed
- 1 finished below support

This was the largest Oct 1 screening concern.

## 5. 2 October — morning board

| Rank | Match | C | Lane | Line | C2 |
|---:|---|---|---|---:|---|
| 1 | Seattle Sounders–Sporting KC | FOCUS | FOLLOW | O3.0 | FOCUS |
| 2 | Blooming–Independiente Petrolero | FOCUS | STOP / audit only | O3.0 | FOCUS |
| 3 | Nicaragua–Costa Rica | WATCH | STOP | O2.5 | FOCUS |

Results:
- Seattle–Sporting KC 2-1 -> O3.0 PUSH
- Blooming–Independiente 0-1 -> O3.0 LOSS
- Nicaragua–Costa Rica 0-3 -> O2.5 WIN

Board support result:
- 1 WIN
- 1 PUSH
- 1 LOSS
- support value 0

Process:
- Seattle remained WAIT; no official exposure was persisted.
- Blooming prior live handling incorrectly treated the fixture as an exception before user declaration; that exposure was correctly VOIDed.
- Blooming also exposed the tournament-incentive resolution loophole later closed by the fail-closed gate.
- Nicaragua was a useful C2-positive disagreement sample, but one fixture is not confirmatory evidence.

## 6. 2 October — evening board

Funnel:
- 57 known senior
- 15 operational admissions
- 12 ranked
- 3 incentive-incomplete quarantines

The quarantines received no predictive state/line; this was correct fail-closed behavior.

| Match | C / lane | Line | FT | Support result |
|---|---|---:|---:|---|
| Belgium–Türkiye | FOCUS / FOLLOW | O2.75 | 3-0 | HALF_WIN |
| Bosnia–Sweden | FOCUS / RESERVE | O2.75 | 1-1 | LOSS |
| Cyprus–Armenia | WATCH / STOP | O2.5 | 2-0 | LOSS |
| Helmond–Heracles | FOCUS / RESERVE | O2.75 | 2-2 | WIN |
| Poland–Romania | WATCH / STOP | O2.5 | 6-0 | WIN |
| Faroe Islands–Slovakia | FOCUS / RESERVE | O2.25 | 1-1 | HALF_LOSS |
| Dukla Praha–Jablonec | WATCH / STOP | O2.5 | 0-1 | LOSS |
| Latvia–Montenegro | WATCH / STOP | O2.25 | 1-2 | WIN |
| France–Italy | WATCH / STOP | O2.25 | 1-1 | HALF_LOSS |
| Hungary–Georgia | PASS / STOP | O2.0 | 1-0 | LOSS |
| Kazakhstan–Moldova | PASS / STOP | O2.0 | 1-2 | WIN |
| Ukraine–Northern Ireland | PASS / STOP | O2.0 | 0-3 | WIN |

Board diagnostic:
- 5 WIN
- 1 HALF_WIN
- 2 HALF_LOSS
- 4 LOSS
- support value +0.5

Selection diagnosis:
- Belgium FOLLOW survived but reached exactly three; O2.75 only half-won.
- Bosnia was promoted partly on “two viable routes” and finished 1-1.
- Faroe was carrier-led with known stall risk and also finished 1-1.
- Kazakhstan and Ukraine were C-PASS false-negative clears; Hungary held below.

## 7. 3 October — morning board

Funnel:
- 29 known senior
- 13 operational admissions
- 13 ranked

Timing defect:
- five 08:00–08:06 fixtures were ranked from a valid 07:44 snapshot, but the board freeze was around 08:10;
- their ordinary prematch windows had already closed.

| Match | C / lane | Line | FT/status | Support result |
|---|---|---:|---|---|
| Monterrey W–Club América W | FOCUS / FOLLOW | O3.0 | 4-3 | WIN |
| Wellington Olympic–Ferrymead | FOCUS / RESERVE | O3.0 | 1-2 | PUSH |
| Pumas W–Tigres W | FOCUS / RESERVE | O2.75 | 1-3 | WIN |
| Seattle Reign–NC Courage | FOCUS / RESERVE | O2.5 | 0-1 | LOSS |
| El Salvador–Jamaica | WATCH / STOP | O2.25 | 0-2 | HALF_LOSS |
| Matsumoto–Tottori | WATCH / STOP | O2.5 | 0-1 | LOSS |
| Atlas W–León W | WATCH / STOP | O2.75 | postponed | NO SETTLEMENT |
| Gifu–Renofa | WATCH / STOP | O2.25 | 0-2 | HALF_LOSS |
| La Paz–Venados | WATCH / STOP | O2.25 | 1-2 | WIN |
| San Francisco–UMECIT | PASS / STOP | O2.0 | 0-1 | LOSS |
| Correcaminos–Cruz Azul Hidalgo | PASS / STOP | O2.0 | 0-0 | LOSS |
| Nagano–Nara | PASS / STOP | O2.0 | 0-1 | LOSS |
| Tepatitlán–Jaiba Brava | PASS / STOP | O2.0 | 3-1 | WIN |

Board diagnostic:
- 4 WIN
- 1 PUSH
- 2 HALF_LOSS
- 5 LOSS
- 1 postponed
- support value -2.0

Audit:
- Monterrey FOLLOW was a clean winner.
- Seattle Reign FOCUS/RESERVE O2.5 -> 0-1 is a strong completion/route-realisation false positive.
- C2 promoted El Salvador, Matsumoto, Gifu and La Paz from C WATCH to C2 FOCUS; only La Paz cleared, while two half-lost and one lost.
- Atlas–León was later confirmed postponed to 22 Oct: PROCESS MISS — FIXTURE STATUS.
- Tepatitlán was another C-PASS false-negative clear.

## 8. 3 October — afternoon reassessment

Final corrected board:
- 7 active fixtures
- 0 FOLLOW
- 2 RESERVE
- 5 STOP

The reassessment corrected postponements, Burton carrier direction, stale Reading team news, overstatement of Grimsby carrier strength, and misuse of engine “ok: true” as proof of research quality.

| Match | C / lane | Line | FT | Support result |
|---|---|---:|---:|---|
| Leyton Orient–Plymouth | FOCUS / RESERVE | O2.5 | 0-2 | LOSS |
| Accrington–Cheltenham | WATCH / STOP | O2.5 | 2-0 | LOSS |
| Burton–Huddersfield | FOCUS / RESERVE | O2.5 | 1-3 | WIN |
| Reading–Bradford | WATCH / STOP | O2.25 | 1-1 | HALF_LOSS |
| Grimsby–Shrewsbury | WATCH / STOP | O2.25 | 1-2 | WIN |
| Crewe–Bristol Rovers | PASS / STOP | O2.0 | 3-1 | WIN |
| Exeter–Rotherham | PASS / STOP | O2.0 | 1-0 | LOSS |

Board diagnostic:
- 3 WIN
- 1 HALF_LOSS
- 3 LOSS
- support value -0.5

Audit:
- Leyton was MIXED / completion HIGH / continuation HIGH / stall MEDIUM and finished 0-2: MODEL FALSE POSITIVE.
- Burton RESERVE cleared 1-3; the correction improved process quality and shows not every conservative reassessment should be loosened.
- Reading 1-1 supports stall concerns but was already WATCH/STOP, so it is not a selection over-promotion.
- Crewe PASS/STOP O2.0 -> 3-1 is another screening false negative.

## 9. 3 October overnight board

For unique-outcome statistics, Leyton and Burton are not counted a second time because they were carryovers from the afternoon slate.

| Match | C / lane | Line | FT | Support result |
|---|---|---:|---:|---|
| Kansas City Current W–Bay FC W | FOCUS / FOLLOW | O2.5 | 3-1 | WIN |
| Spain–Czechia | FOCUS / RESERVE | O2.75 | 3-1 | WIN |
| Frankfurt W–Bayern W | FOCUS / RESERVE | O2.75 | 1-0 | LOSS |
| Croatia–England | FOCUS / RESERVE | O2.5 | 0-7 | WIN |
| Racing Louisville W–Utah Royals W | WATCH / STOP | O2.5 | 1-1 | LOSS |
| Köln W–Freiburg W | WATCH / STOP | O2.25 | 0-1 | LOSS |
| Switzerland–Slovenia | WATCH / STOP | O2.25 | 2-1 | WIN |
| Iceland–Bulgaria | WATCH / STOP | O2.25 | 3-0 | WIN |
| North Macedonia–Scotland | PASS / STOP | O2.0 | 0-2 | PUSH |

Unique board diagnostic:
- 5 WIN
- 1 PUSH
- 3 LOSS
- support value +2.0

### Frankfurt W–Bayern W

Frozen:
- C-FOCUS #4
- TWO_SIDED
- completion HIGH
- continuation HIGH
- stall MEDIUM
- O2.75
- C2-FOCUS #4 / O2.75

FT 1-0.

This is more severe than a normal “third goal did not arrive” miss. Only one goal materialised.

Audit tags:
- MODEL FALSE POSITIVE
- RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE

## 10. Oct 2–3 aggregate diagnostic

Unique ranked fixtures:
- 44 rows
- 43 settled
- 1 postponed

Settlement:
- 18 WIN
- 1 HALF_WIN
- 3 PUSH
- 5 HALF_LOSS
- 16 LOSS

Simple support-value sum:
- **0.0**

The raw support universe was not globally collapsing. The problem is discrimination and prioritisation.

### By C state

FOCUS — 16 settled:
- 7 WIN
- 1 HALF_WIN
- 2 PUSH
- 1 HALF_LOSS
- 5 LOSS
- support value +2.0

WATCH — 17 settled + 1 postponed:
- 7 WIN
- 4 HALF_LOSS
- 6 LOSS
- support value -1.0

PASS — 10 settled:
- 4 WIN
- 1 PUSH
- 5 LOSS
- support value -1.0

### By lane

FOLLOW — 4 settled:
- 2 WIN
- 1 HALF_WIN
- 1 PUSH
- 0 full losses
- support value +2.5

RESERVE — 11 settled:
- 5 WIN
- 1 PUSH
- 1 HALF_LOSS
- 4 LOSS
- support value +0.5

STOP — 28 settled + 1 postponed:
- 11 WIN
- 1 PUSH
- 4 HALF_LOSS
- 12 LOSS
- support value -3.0

Interpretation:
- FOLLOW was stronger than the recent highlighted-loss cluster suggests;
- RESERVE/FOCUS grading still contains important false positives;
- STOP/PASS still leaves substantial support-clearing matches behind.

## 11. Three-day C-PASS audit

Oct 1 clean PASS:
- 8 clears
- 2 pushes
- 1 below
- N=11

Oct 2–3 PASS:
- 4 clears
- 1 push
- 5 below
- N=10

Combined:
- **12 clear**
- **3 push**
- **6 below**
- **N=21**

Rates:
- clear 57.1%
- push 14.3%
- below support 28.6%

This is not P/L and many PASS lines are only O2.0/O2.25.

Diagnosis:
- MODEL FALSE NEGATIVE — SCREENING
- likely historical over-penalisation of weak second routes in some carrier/leakage profiles.

The model is showing both errors at once:
- overpromotion of some apparent two-route matches;
- underpromotion of some carrier-led / one-weak-route matches.

## 12. Two-route / continuation audit

Recent failures include:
- Man City W–Real Madrid W 1-1
- Austria Wien W–Inter W 1-1
- Bosnia–Sweden 1-1
- Leyton–Plymouth 0-2
- Frankfurt W–Bayern W 1-0
- Seattle Reign–NC Courage 0-1

These do not prove that two-sided profiles should be removed.

Counterexamples that cleared include:
- Monterrey W–Club América W 4-3
- Pumas W–Tigres W 1-3
- Burton–Huddersfield 1-3
- Croatia–England 0-7
- Kansas City Current W–Bay FC W 3-1

Correct diagnosis:

Route count is not useful by itself. The unresolved variable is whether the route prospectively contributes to the clearing goal and survives common control states.

This is exactly the question assigned to C3:
- BURDEN_CONTRIBUTING
- EXCHANGE_ONLY
- STATE_DEPENDENT
- NONE

Historical matches have zero C3 confirmatory weight.

## 13. C2 audit

C2 did not show a clean solution.

Positive disagreement:
- Nicaragua–Costa Rica: C WATCH / C2 FOCUS -> O2.5 cleared.

But C2 also promoted official WATCH rows that did not clear:
- Cyprus–Armenia
- Dukla–Jablonec
- El Salvador–Jamaica
- Matsumoto–Tottori
- Gifu–Renofa

Other C2 promotions such as Poland–Romania and La Paz–Venados cleared.

Conclusion:
- C2 broader route-quality admission is mixed;
- no evidence from these boards justifies promoting C2 over C;
- the restarted C2 confirmation counter remains **0/5**, because the Step-2 fail-closed repair activated after these board freezes.

## 14. C3 boundary

C3 activated after the historical overnight board had frozen.

Therefore:
- none of the 1–3 Oct boards is a clean C3 Board 1/5;
- historical failures are design motivation only;
- later match-level comparison does not convert the old board into a clean C3 board.

C3 counter:
- **0/5**

## 15. Workflow / integrity findings

A. Oct 1 Madla–Viking FOLLOW had no Step-2 Decision State.  
Diagnosis: PROCESS MISS — FOLLOW-THROUGH OMISSION.

B. Oct 1 HB Køge–Servette PRE signal arrived after the price disappeared.  
Diagnosis: EXECUTION MISS — QUOTE EPOCH LATENCY; no official exposure.

C. Blooming live assessment was handled before a valid declared exception and later VOIDed.  
Diagnosis: PROCESS MISS — INVALID EXCEPTION SCOPE.

D. Blooming exposed the tournament-incentive design gap later fixed by the fail-closed gate.

E. Oct 3 morning board was frozen after five early fixtures had kicked.  
Diagnosis: PROCESS MISS — BOARD LATENCY.

F. Atlas–León was ranked despite being postponed.  
Diagnosis: PROCESS MISS — FIXTURE STATUS.

G. The Oct 3 afternoon first pass had status/research errors, but the final reassessment corrected them before the surviving kickoffs.

H. The Oct 3 overnight Step-0 handoff omitted the Netherlands Eerste Divisie block entirely.

Omitted in-window examples:
- Vitesse–NAC Breda
- TOP Oss–MVV
- RKC Waalwijk–Emmen
- Almere City–Volendam
- Den Bosch–Dordrecht
- FC Eindhoven–De Graafschap

Classification:

HANDOFF INCOMPLETE — ACTIONABLE COVERAGE GAP — NETHERLANDS EERSTE DIVISIE OMITTED

This is a Step-0 coverage failure, not a Work ranking failure. Later user-declared exceptions do not retroactively repair the board universe.

The overnight board is coverage-contaminated for clean confirmatory-model counting.

## 16. Exposure / P&L status

Oct 1 persisted routine C:
- 1W–2L
- -1.25u

Oct 2–3:
- no persisted official Website Pick exposure was found for the routine evening / 3 Oct boards;
- Seattle was WAIT / no entry;
- Blooming was VOID / 0u;
- later frozen-support settlements remain diagnostic only.

Do not infer user P/L from board support. User bet-slip truth remains separate.

## 17. Final diagnosis

### Confirmed

**PASS false-negative screening — HIGH confidence**
- repeated across all three days;
- combined clean sample 12 clears / 3 pushes / 6 below.

**Route-to-burden semantics — MEDIUM-HIGH concern**
- repeated cases where “two viable routes” or HIGH continuation failed to fund the clearing goal;
- Frankfurt–Bayern 1-0 shows some failures occur before the two-goal endpoint.

**Control-endpoint handling — MEDIUM-HIGH concern**
- repeated 1-1 / 2-0 / 0-2 endpoints among promoted/recently discussed matches.

**Step-0 / status / timing reliability — HIGH confidence process issue**
- Atlas postponement;
- early fixtures already live at freeze;
- Eerste Divisie block omitted overnight.

### Not supported

- every two-route match is bad;
- carrier-led is always superior;
- C2 fixes C;
- recent highlighted losses mean FOLLOW itself is failing.

The Oct 2–3 FOLLOW support sample was strong.

## 18. Action after audit

Do not change Football C or C2 from this audit alone.

Current experiment structure remains:
- C official control;
- C2 frozen route-quality challenger;
- C3 prospective clearing-goal / second-route-role challenger;
- factor-calibration observer prospectively only.

Separate next QA item:
- repair Step-0 required-competition coverage so Netherlands Eerste Divisie cannot disappear from a handoff again.

Do not mix the model-selection issue and the sweep-coverage issue into one predictive patch.
