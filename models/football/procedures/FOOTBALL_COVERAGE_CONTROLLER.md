# Football Coverage Controller

**Status:** Active mandatory pre-ranking controller  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Applies to:** Football v0.2.47 CLEAN official track and Football v0.2.48-SHADOW  
**Purpose:** Prevent silent omission of worthwhile fixtures before structural ranking.

This controller sits **above** both football models. It is not a betting rule and does not change how either model grades a match. Its job is to guarantee that both models receive the same reconciled fixture universe.

Core sequence:

`FIXTURE UNIVERSE → ELIGIBILITY → SCREEN EVERY ELIGIBLE FIXTURE → PRE DISPOSITION → FOCUS/WATCHLIST/PASS → XI WINDOW RERANK → MARKET → MODEL VERDICT`

The visible shortlist is allowed to be small. The internal screened universe is not.

---

## 1. Coverage invariant

Before publishing a daily/upcoming board, every fixture in the requested time window must be accounted for as one of:

- `SCREENED`
- `LATE-DISCOVERED BUT SCREENED`
- `EXCLUDED`
- `PENDING SCREEN / DATA INCOMPLETE`

A board is **coverage-complete** only when:

`eligible fixtures = screened eligible fixtures + pending/data-incomplete eligible fixtures`

with no unexplained fixture gaps.

If this equality cannot be established, label the slate:

`COVERAGE INCOMPLETE`

and do not imply the visible board is exhaustive.

---

## 2. Fixture-universe reconciliation

For every daily or user-requested fixture window:

1. Build Source 1 fixture list from the canonical football fixture feed/API available to the workflow.
2. Build Source 2 fixture list from an independent schedule source whenever possible.
3. Normalize team names, competition names, dates, and kickoff times to ICT.
4. Take the union of both lists before exclusions.
5. Reconcile duplicate fixtures and obvious naming aliases.
6. Record source disagreement rather than silently choosing one source.
7. Only after the union is stable, apply competition eligibility.

A single-source fetch is permitted only when no independent source is available. In that case mark `Reconciled = false` and report the coverage limitation.

Do not use model attractiveness, odds, team reputation, or kickoff convenience to decide whether a fixture enters the universe.

---

## 3. Eligibility gate

Apply exclusions before structural ranking.

Eligible normal competition universe:

- league fixtures except hard-excluded leagues;
- English domestic cups: FA Cup and EFL/Carabao Cup;
- DFB-Pokal;
- North American Leagues Cup (MLS/Liga MX).

Hard exclusions currently include:

- K League;
- Belgian Pro League / Jupiler Pro League;
- all other domestic/continental/League Cup competitions unless explicitly added later.

Every excluded fixture still receives a ledger row with `Eligibility = EXCLUDED` and an explicit exclusion reason. Exclusion is not omission.

---

## 4. Mandatory screen-every-fixture rule

There is no undefined `credible candidate` prefilter before PRE screening.

Every **eligible** fixture must receive at least a lightweight structural disposition using the current operating layer:

- team GF/GA profile;
- 2+/3+ scoring and conceding frequency where relevant;
- home/away context when useful;
- carrier ceiling;
- secondary route;
- suppression/resistance;
- recent-total/leakage flag;
- chance-quality support when required/available;
- obvious competition/incentive drag;
- primary failure mode.

Assign one PRE band:

- `A1`
- `A2`
- `B+`
- `B / PASS`
- `DATA INCOMPLETE`

No eligible fixture may disappear before receiving one of those dispositions.

---

## 5. Board tiers

After all eligible fixtures are screened, assign a board tier.

### FOCUS
Use for the strongest A1/A2 candidates and any B+ candidate that is genuinely close enough to become a lock after XI/market.

### WATCHLIST
Use for other A2/B+ fixtures whose routes are real but currently carry a material uncertainty, weaker priority, uncertain XI, or market dependency.

### PASS
Use for B/PASS fixtures whose route is too fragile for normal XI follow-up absent genuinely new prematch information.

### UNRESOLVED
Use when data is materially incomplete.

**Important:** shortening applies only to the user-facing display. FOCUS and WATCHLIST rows remain alive internally until kickoff, explicit downgrade, or exclusion.

---

## 6. Display-compression rule

The instruction to “aggressively shorten the board” means:

- show the best few FOCUS fixtures prominently;
- optionally summarize WATCHLIST compactly;
- do not dump every PASS fixture into the normal user-facing board.

It does **not** mean:

- stop screening after finding a few good matches;
- discard A2/B+ fixtures because another match looks better;
- forget an overlapping match once a primary focus match is selected.

Display compression must never become screening compression.

---

## 7. Coverage-count reconciliation

For every completed daily screen, maintain this count block:

`Universe | Eligible | Excluded | Screened | Focus | Watchlist | Pass | Unresolved`

Required invariant:

`Eligible = Focus + Watchlist + Pass + Unresolved`

and

`Universe = Eligible + Excluded`

If the numbers do not reconcile, the workflow must search for the missing row before publishing the board as complete.

---

## 8. Persistence and Airtable

Persist the daily universe to Airtable table:

- Base: `SlipTrace Football Decision Control`
- Base ID: `appWyZJjitSBATXAU`
- Table: `Daily Coverage Ledger`
- Table ID: `tblcl1UAyMqZT6Ub0`

Use one row per fixture per slate date.

Recommended stable `Coverage ID`:

`YYYYMMDD-COMPETITION-HOME-AWAY`

Upsert rather than duplicate when the same fixture is seen again.

The coverage ledger is the authoritative source for “what's next?” within an already-screened slate. Do not rebuild a fresh partial board from memory when a reconciled ledger exists.

If the requested window has changed materially or the ledger is stale/incomplete, reconcile again and update it.

---

## 9. Same-window monitoring / anti-sunk-cost rule

Matches starting in the same practical monitoring block must remain comparable.

Before kickoff and again at confirmed XI:

1. collect all FOCUS + WATCHLIST fixtures in the relevant kickoff window;
2. rerank them head-to-head;
3. if the top match is downgraded by XI/market, immediately promote the next strongest surviving match;
4. do not keep monitoring a weakened first-choice match simply because it was selected earlier.

This rule is designed to prevent errors such as prioritizing one match while another same-window A2/A1 candidate silently disappears.

Suggested comparison window: roughly 90 minutes either side of the current next kickoff, adjusted when the slate is sparse.

---

## 10. XI-stage survival rule

Every FOCUS match and every WATCHLIST match that can still plausibly reach LOCK must receive XI attention when reliable confirmed lineups become available.

A WATCHLIST match is not dead merely because it was not in the top three visible board.

At XI:

- preserve frozen PRE;
- rerank rather than rebuild;
- update `XI Status` in the coverage ledger;
- compare surviving candidates in the same kickoff block;
- only then move to Asian-total market expression.

---

## 11. Dual-model routing

The coverage controller is shared.

Both tracks must receive:

- the same reconciled fixture universe;
- the same competition eligibility;
- the same PRE evidence timestamp;
- the same confirmed XI snapshot;
- the same Asian-total market snapshot.

Then the tracks diverge only in model logic:

- **Official:** Football v0.2.47 CLEAN
- **Shadow:** Football v0.2.48-SHADOW

Store both PRE dispositions in the Daily Coverage Ledger.

Do not let a v0.2.48 shadow HOLD remove a match from the v0.2.47 official workflow, and do not let a v0.2.47 PASS prevent the shadow track from recording its own disposition when the match was eligible and screened.

---

## 12. Late discovery

If an eligible fixture is discovered after the first board was published:

### Before kickoff
Label:

`LATE-DISCOVERED BUT SCREENED`

Screen it immediately and insert it into FOCUS/WATCHLIST/PASS normally.

### After kickoff
Label:

`TRUE MISSED SCREEN` if it was never properly assessed before kickoff.

Do not retroactively pretend it was part of the original screen and do not automatically convert it into a live bet.

A just-kicked grace or explicit manual-live override remains governed by the betting procedure.

---

## 13. Audit taxonomy

Use these coverage labels consistently:

- `SCREENED` — assessed before/around kickoff, even if not shown on the first visible board;
- `LATE-DISCOVERED BUT SCREENED` — initially omitted but found and assessed in time;
- `TRUE MISSED SCREEN` — never properly assessed before kickoff;
- `RANKING MISS` — screened but another match was incorrectly prioritized over it;
- `HOLD/PASS` — screened and deliberately rejected;
- `FALSE-NEGATIVE HOLD` — screened but available prematch evidence likely justified a lock;
- `BAD LOCK` — locked despite structure/XI/line probably not clearing;
- `CORRECT HOLD, OVER LANDED` — result went Over but prematch evidence did not justify the bet.

Do not classify a match as a missed lock from final score alone.

---

## 14. User-facing board contract

For normal `list upcoming matches`, `what's next?`, or daily-board requests, output:

1. coverage status/count line;
2. FOCUS board;
3. WATCHLIST only when useful or when the user asks for full coverage;
4. next-match designation based on the persisted coverage ledger.

Example coverage line:

`Coverage: 42 universe | 27 eligible | 27 screened | 5 focus | 8 watch | 14 pass | 0 unresolved`

If any eligible row remains unresolved, say so explicitly.

---

## 15. Fail-closed rules

Do not claim `full slate screened` when:

- only one partial fixture source was checked and reconciliation was not possible;
- eligible fixture counts do not reconcile;
- a league block is known to be missing;
- timezone conversion is unresolved;
- newly discovered eligible fixtures have not yet been screened.

In those cases, use:

`COVERAGE INCOMPLETE — board provisional`

A provisional board may still contain useful candidates, but it must not be presented as exhaustive.

---

## Operating principle

**Prove coverage before optimizing selection. Every eligible fixture gets a disposition. Shorten the display, not the screened universe. Persist FOCUS and WATCHLIST. Rerank same-window survivors at XI. Route the same complete evidence set to v0.2.47 CLEAN and v0.2.48-SHADOW.**