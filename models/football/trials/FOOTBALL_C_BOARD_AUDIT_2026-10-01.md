# Football C Board Audit — 2026-10-01 ICT

**Status:** HISTORICAL / VERSION-FAITHFUL AUDIT  
**Audit date:** 2026-10-02 ICT  
**Official model:** Football C  
**Shadow model:** Football C2  
**Scope:** both frozen boards covering 2026-10-01 ICT and the overnight window ending 2026-10-02 03:00 ICT

## 1. Audit boundaries

Two frozen boards are in scope:

1. **B-20261001-0737-20261001-1300** — 07:37–13:00 ICT
   - 5 raw fixtures
   - 1 hard exclusion
   - 4 admitted
   - C: 2 FOCUS / 1 WATCH / 1 PASS
   - operational: 0 FOLLOW / 1 RESERVE / 3 STOP

2. **2026-10-01 13:00–2026-10-02 03:00 ICT**
   - 55 admitted
   - C: 20 FOCUS / 19 WATCH / 16 PASS
   - operational: 5 FOLLOW / 4 RESERVE / 46 STOP
   - C2: 22 FOCUS / 16 WATCH / 17 PASS
   - board text/code disagreement: none

No historical state is rewritten from FT.

The hardened tournament-incentive resolution gate was introduced **after these board freezes**. Therefore missing/unresolved incentive fields on these frozen boards are not labelled as then-current rule violations. They are audited separately as **retrospective process debt under the current rule**.

## 2. Morning board outcome

| Match | Frozen C state/lane | Support | Result | Diagnostic |
|---|---|---:|---:|---|
| Khovd Western vs Deren FC | C-FOCUS / RESERVE | O3.00 | 1-5 | support clear; reserve opportunity cost |
| Atlético Nacional vs Junior | C-FOCUS / STOP | O2.50 | 3-1 | support clear; STOP opportunity cost |
| CD FAS vs Isidro Metapán | C-WATCH / STOP | O2.25 | postponed | no settlement |
| Sacramento Republic vs Las Vegas Lights | C-PASS / STOP | O2.00 | 3-2 | clear Step-1 false negative |

The morning board produced **no routine FOLLOW fixture** despite three completed matches later clearing their frozen support.

Sacramento remains a frozen C-PASS false negative. A later user-declared live exception is a separate epoch and must not rewrite the board state. That live exception entered O2.75 @1.71 and won; it is excluded from routine-board P/L.

## 3. Evening operational queue

### FOLLOW

| Rank | Match | Frozen support | FT | Process read |
|---:|---|---:|---:|---|
| 1 | Manchester City W vs Real Madrid W | O3.00 | 1-1 | official C/C2 entry lost |
| 2 | Ireland vs Austria | O2.75 | 2-2 | official execution protected down to O2.00 and won |
| 3 | Germany vs Serbia | O2.75 | 2-0 | WAIT/no entry protected from loss |
| 4 | HB Koge W vs Servette W | O2.75 | 5-1 | prematch O3 quote stale/unavailable; later WAIT did not execute |
| 5 | Madla IL vs Viking | O3.00 | 0-3 | **FOLLOW process omission: no Step-2 Decision State found** |

### RESERVE

| Rank | Match | Frozen support | FT | Process read |
|---:|---|---:|---:|---|
| 6 | Al Shamal vs Muaither | O2.75 | 2-1 | C WAIT/no entry; support would half-win diagnostically |
| 7 | Austria Wien W vs Inter W | O2.75 | 1-1 | activated; C/C2 O2.50 entry lost |
| 8 | Dubai United vs Hatta | O2.75 | 3-2 | no activation found; reserve opportunity cost |
| 9 | Sha Tin vs Hong Kong FC | O2.75 | 2-2 (90m) | user activated live; WAIT target never became executable |

## 4. Persisted official C exposure

Routine board-derived official C exposures found in Website Picks / Decision States:

| Match | Entry | FT | Settlement |
|---|---:|---:|---:|
| Manchester City W vs Real Madrid W | O3.00 @1.68, 1u | 1-1 | -1.00u |
| Ireland vs Austria | O2.00 @1.75, 1u | 2-2 | +0.75u |
| Austria Wien W vs Inter W | O2.50 @1.90, 1u | 1-1 | -1.00u |

**Persisted routine C result: 1W–2L, -1.25u.**

The same three common C2 shadow entries produce **1W–2L, -1.25u**. There is no demonstrated C2 execution advantage on this slate.

This is model-accounting P/L from persisted records, not a replacement for physical bet-slip truth.

## 5. PASS false-negative audit

The evening board contained 16 C-PASS rows. Several Moroccan/Egyptian/Oman fixtures have incomplete or conflicting public result coverage at audit time, and the Khaan Khuns–Central Stallions row was an identity/time-integrity PASS rather than a football-quality PASS, so it is not used as a predictive false-negative.

Among the **11 cleanly verified, played, football-quality C-PASS rows** across the two boards that could be settled against their frozen support:

- **8 cleared the frozen supported line**
- **2 pushed**
- **1 finished below support**

Verified clear examples:

- Sacramento Republic–Las Vegas: C-PASS O2.00 -> FT 3-2
- Hapoel Raanana–Kafr Qasim: C-PASS O2.00 -> FT 1-2
- Al-Msnaa–Ibri: C-PASS O2.25 -> FT 2-2
- Hapoel Afula–Hapoel Rishon: C-PASS O2.00 -> FT 2-2
- Ittihad Al-Ramtha–Sama Al Sarhan: C-PASS O2.00 -> FT 2-1
- Al-Nasr (OMA)–Samail: C-PASS O2.00 -> FT 3-3
- Mombasa United–Kariobangi Sharks: C-PASS O2.00 -> FT 2-1
- El Sekka El Hadid–El Entag Al Harby: C-PASS O2.00 -> FT 5-4

Pushes:
- Malta–Gibraltar O2.00 -> 1-1
- El Mansoura–FC Masar O2.00 -> 2-0

Clean hold:
- Pharco–Tersana O2.00 -> 0-1

This is **diagnostic support settlement only**. It is not hypothetical betting P/L because Step 1 did not contain executable prices.

### PASS mechanism finding

The prior PASS-audit pattern is now stronger:

1. **WEAK second route is too often functioning as a proxy for total suppression.**
2. A weak scoring route does not imply the same team can prevent the opponent/carrier from self-funding.
3. Low-data competitions are especially vulnerable to stale H2H / scoreline summaries overwhelming current leakage or carrier evidence.
4. C-PASS currently appears too final when the evidence is thin rather than truly suppressive.

Do not globally promote PASS rows from this result sample. The proper next test remains a prospective PASS-contradiction observer.

## 6. Follow-through guard audit

The guard clearly reduced workload, but yesterday shows material opportunity cost.

Verified C-FOCUS/STOP support clears include:
- Atlético Nacional–Junior O2.50 -> 3-1
- Bærum–Lillestrøm O3.00 -> high-total win
- PSG W–OH Leuven W O2.75 -> 5-0
- Denmark–Portugal O2.50 -> 2-4
- Greece–Netherlands O2.50 -> 2-2
- Baniyas–Al Wahda O2.50 -> 3-1
- US Virgin Islands–Saint Martin O2.50 -> 0-5
- Rana–Bodø/Glimt O3.00 -> 2-6
- North District–Southern District O2.75 -> 2-1

But STOP also avoided clear failures, including:
- Qatar SC–Al Bidda O2.75 -> 1-0
- Kiryat Yam–Hapoel Kfar Saba O2.50 -> 2-0
- Ashdod–Maccabi Herzliya O2.50 -> 1-0

Therefore the correct finding is **not “remove STOP.”** It is:

> the current FOLLOW quality gate is highly selective and may be leaving too many structurally good FOCUS matches without any Step-2 price/XI observation.

A prospective audit should measure executable price availability and Step-2 survival on a sampled subset of STOP-FOCUS rows before changing capacity/quality thresholds.

## 7. Tournament-incentive audit

### Version-faithful conclusion

Both frozen boards predate the hardened tournament-incentive resolution gate. Do not retro-label the boards as rule violations.

### Current-rule replay

Under the current rule, tournament-sensitive rows cannot receive C/C2 state, rank, supported burden, or lane while qualification/tiebreak/margin/simultaneous-result implications remain LIMITED/UNKNOWN.

The strongest historical example is:

**Indonesia vs Bangladesh**
- frozen board: C-WATCH / STOP, STRONG/WEAK, O2.25
- primary board caveat: Bangladesh route weak
- FT: **9-2**
- official post-match competition reporting confirms Indonesia required a large winning margin while Malaysia played Singapore simultaneously; both finished level on points/GD and Indonesia advanced through goals scored.

This means the board's football route assessment omitted a central persistence mechanism: **margin / goals-scored race under simultaneous results**.

Under the current hardened procedure this fixture would have required, before support:
- exact group table;
- qualification condition;
- tiebreak order;
- margin/goals-scored relevance;
- Malaysia–Singapore simultaneous-result effect;
- explicit `MARGIN_NEEDED` / incentive persistence state.

Until those were VERIFIED it would be:
`INCENTIVE-INCOMPLETE`.

**Malaysia vs Singapore** reinforces the same point: Malaysia won 6-0 but still missed the final after Indonesia's 9-2 result. The simultaneous score and goals-scored tiebreak materially altered late incentive.

### Positive example

Sha Tin–Hong Kong FC was later reassessed with the League Cup's direct-penalty / double-elimination context explicitly recognized. C stayed cautious and the protected wait never became executable. This is the direction the current rule is meant to enforce, although today's hardened contract now requires a more explicit VERIFIED resolution block.

## 8. Elite upper-tail observer

Manchester City W–Real Madrid W was the slate's only `ELITE_UPPER_TAIL_OBSERVER` tag.

- frozen support O3.00
- official C/C2 entry O3.00 @1.68
- FT 1-1
- settlement: loss

This is a valuable **prospective negative** for the observer and directly argues against promoting the elite upper-tail hypothesis from the prior Farul/Brann/Barcelona examples.

## 9. C vs C2

On actual common executable entries yesterday:
- C: 1W–2L, -1.25u
- C2: 1W–2L, -1.25u

Board-level differences remain observational:
- Wales–Norway: C-WATCH / C2-FOCUS; FT 2-1, frozen O2.50 cleared
- Amal Tiznit–DHJ: C-WATCH / C2-FOCUS; result not cleanly verified at audit time
- Al-Sharjah–Al Dhafra: C-WATCH / C2-PASS; FT 2-1, C O2.50 cleared diagnostically

No P/L is assigned to these STOP rows because no exact executable Step-2 C2 quote was frozen.

## 10. Process failures / defects

1. **Madla–Viking FOLLOW omission**
   - normal FOLLOW candidate;
   - no Step-2 Decision State found;
   - this is a workflow failure regardless of FT.
   - FT 0-3 would only push O3.00, so the omission did not hide a winning frozen-support Over.

2. **HB Koge–Servette stale quote**
   - C signal was produced at O3.00 @1.70;
   - quote was no longer available by verdict delivery;
   - correctly voided after user correction;
   - later live wait did not execute.
   - classify as execution-latency / quote-epoch failure, not model loss.

3. **Tournament incentive resolution debt**
   - the board generation predates the hard gate;
   - several tournament rows would fail today's resolution contract.
   - Indonesia–Bangladesh is the clearest example.

4. **PASS false negatives**
   - currently the largest model-screen concern from yesterday.
   - treat separately from operational STOP opportunity cost.

## 11. Audit conclusion

The primary issues from yesterday are:

1. **Step-1 PASS remains too aggressive in thin/one-weak-route cases.**
2. **The FOLLOW/STOP operational gate is probably too selective to evaluate good FOCUS rows efficiently**, but evidence does not justify simply loosening it.
3. **Tournament incentive was materially under-specified in the frozen board era**, especially in simultaneous group/tiebreak situations. The new VERIFIED-resolution hard gate directly addresses this.
4. **C2 showed no execution advantage over C yesterday.**
5. **The elite upper-tail observer received an important negative sample.**
6. **Madla exposed a follow-through completeness defect; HB Koge exposed execution-latency risk.**

No production predictive threshold is changed by this audit.
