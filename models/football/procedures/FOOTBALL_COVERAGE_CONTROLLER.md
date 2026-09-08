# Football Coverage Controller

**Status:** Active mandatory pre-ranking controller  
**Timezone:** Asia/Ho_Chi_Minh / ICT (UTC+7)  
**Applies to:** Football v0.2.49 official, v0.2.47 CLEAN shadow, and v0.2.48-SHADOW  
**Purpose:** Prevent silent omission of worthwhile fixtures before structural ranking.

This controller sits above the model tracks. It is not a betting rule. Its job is to ensure the models receive the same screened fixture universe and evidence state.

**Fixture-source authority is defined by `FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`: sweep AiScore only; research sources remain flexible.**

Core sequence:

`AISCORE FIXTURE UNIVERSE → ELIGIBILITY → SCREEN EVERY ELIGIBLE FIXTURE → PRE DISPOSITION → FOCUS/WATCHLIST/PASS → XI WINDOW RERANK → MARKET → MODEL VERDICTS`

The visible shortlist is allowed to be small. The internal screened universe is not.

---

## 1. Coverage invariant

Before publishing a daily/upcoming board, every AiScore fixture in the requested time window must be accounted for as one of:

- `SCREENED`
- `LATE-DISCOVERED BUT SCREENED`
- `EXCLUDED`
- `PENDING SCREEN / DATA INCOMPLETE`

A board is coverage-complete only when the relevant AiScore window was traversed and:

`eligible fixtures = screened eligible fixtures + pending/data-incomplete eligible fixtures`

with no unexplained AiScore fixture gaps.

If this cannot be established, label the slate:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

---

## 2. Fixture-universe sweep — AiScore only

For every daily or user-requested fixture window:

1. Build the fixture list only from AiScore daily/live listings and AiScore match pages.
2. Normalize team names, competition names, dates, and kickoff times to ICT.
3. Traverse the full relevant AiScore window before exclusions.
4. Reconcile duplicate representations of the same AiScore fixture.
5. Only after the AiScore list is stable, apply competition eligibility.

Do **not** build a union with an independent schedule source.

Do **not** allow Soccerway, FotMob, Google/web search, Bzzoiro/BSD, league sites, bookmaker pages, or any other provider to add fixtures to the universe.

If another source reveals a possible fixture, verify it on AiScore before adding it. If it cannot be verified on AiScore, it is not part of the active sweep universe.

Under this policy, `Reconciled = true` means the requested AiScore listing/window was fully traversed, normalized, and accounted for. It does not require cross-provider agreement.

Do not use model attractiveness, odds, team reputation, or kickoff convenience to decide whether an AiScore fixture enters the universe.

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

Every excluded AiScore fixture still receives a ledger row with `Eligibility = EXCLUDED` and an explicit exclusion reason. Exclusion is not omission.

---

## 4. Mandatory screen-every-fixture rule

There is no undefined `credible candidate` prefilter before PRE screening.

Every eligible fixture must receive at least a lightweight structural disposition using the current operating layer:

- team GF/GA profile;
- 2+/3+ scoring and conceding frequency where relevant;
- home/away context when useful;
- structural archetype;
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

No eligible fixture may disappear before receiving a disposition.

---

## 5. Board tiers

After all eligible fixtures are screened, assign a board tier.

### FOCUS
Use for the strongest A1/A2 candidates and any B+ candidate genuinely close enough to become a lock after XI/market.

### WATCHLIST
Use for other A2/B+ fixtures whose routes are real but currently carry material uncertainty, weaker priority, uncertain XI, or market dependency.

### PASS
Use for B/PASS fixtures whose route is too fragile for normal XI follow-up absent genuinely new prematch information.

### UNRESOLVED
Use when data is materially incomplete.

Shortening applies only to the user-facing display. FOCUS and WATCHLIST rows remain alive internally until kickoff, explicit downgrade, or exclusion.

---

## 6. Display-compression rule

The instruction to aggressively shorten the board means:

- show the best few FOCUS fixtures prominently;
- optionally summarize WATCHLIST compactly;
- do not dump every PASS fixture into the normal user-facing board.

It does not mean:

- stop screening after finding a few good matches;
- discard A2/B+ fixtures because another match looks better;
- forget an overlapping match once a primary focus match is selected.

**SHORTEN THE DISPLAY, NEVER THE SCREENED UNIVERSE.**

---

## 7. Coverage-count reconciliation

For every completed daily screen, maintain:

`Universe | Eligible | Excluded | Screened | Focus | Watchlist | Pass | Unresolved`

Required invariants:

`Eligible = Focus + Watchlist + Pass + Unresolved`

`Universe = Eligible + Excluded`

If the numbers do not reconcile, search the AiScore sweep for the missing row before publishing the board as complete.

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

Upsert rather than duplicate when the same AiScore fixture is seen again.

Recommended source fields:

- `Source 1 = AiScore`
- `Source 2 = blank` unless used only as a research/reference note

The coverage ledger is the authoritative source for `what's next?` within an already-screened slate. Do not rebuild a fresh partial board from memory when the ledger exists.

If the requested window changes materially or the ledger is stale/incomplete, rerun the affected AiScore sweep and update it.

---

## 9. Same-window monitoring / anti-sunk-cost rule

Matches starting in the same practical monitoring block must remain comparable.

Before kickoff and again at confirmed XI:

1. collect all FOCUS + WATCHLIST fixtures in the relevant kickoff window;
2. rerank them head-to-head;
3. on the official v0.2.49 track, apply its current structural ordering, including two-sided priority for comparable grades;
4. if the top match is downgraded by XI/market, immediately promote the next strongest surviving match;
5. do not keep monitoring a weakened first-choice match simply because it was selected earlier.

Suggested comparison window: roughly 90 minutes either side of the current next kickoff, adjusted when the slate is sparse.

---

## 10. XI-stage survival rule

Every FOCUS match and every WATCHLIST match that can still plausibly reach LOCK must receive XI attention when reliable confirmed lineups become available.

At XI:

- preserve frozen PRE;
- rerank rather than rebuild;
- update `XI Status` in the coverage ledger;
- compare surviving candidates in the same kickoff block;
- only then move to Asian-total market expression.

---

## 11. Research after sweep

Once AiScore establishes the fixture, match research runs normally using the best available sources.

Research may use official team/league sources, Soccerway, FotMob, FBref, BSD/Bzzoiro where supported, reputable statistical/news sources, and user-supplied screenshots.

These sources may improve lineup, profile, chance-quality, tactical, injury, incentive, and market evidence. They may not add a non-AiScore fixture to the sweep universe.

---

## 12. Three-track routing

The coverage controller is shared. All three model tracks receive:

- the same AiScore fixture universe;
- the same competition eligibility;
- the same PRE evidence timestamp;
- the same confirmed XI snapshot;
- the same Asian-total market snapshot.

Then the tracks diverge by model logic:

- **Official:** Football v0.2.49
- **Shadow 1:** Football v0.2.47 CLEAN, run without the v0.2.49 patch
- **Shadow 2:** Football v0.2.48-SHADOW, run with its own documented shadow deltas and without silently importing the v0.2.49 patch

Only v0.2.49 enters official P/L.

Store v0.2.47 and v0.2.48 comparison dispositions in their existing coverage fields where applicable. Do not overwrite those fields with the v0.2.49 official state.

A shadow HOLD/PASS must not remove a match from the official v0.2.49 workflow.

---

## 13. Late discovery

If an eligible fixture that was present on AiScore is found after the first board was published:

### Before kickoff
Label:

`LATE-DISCOVERED BUT SCREENED`

Screen it immediately and insert it into FOCUS/WATCHLIST/PASS normally.

### After kickoff
Label:

`TRUE MISSED SCREEN` if it was on AiScore but was never properly assessed before kickoff.

A fixture found only through a non-AiScore research source is not added until verified on AiScore.

A just-kicked grace or explicit manual-live override remains governed by the betting procedure.

---

## 14. Audit taxonomy

Use these coverage labels consistently:

- `SCREENED`
- `LATE-DISCOVERED BUT SCREENED`
- `TRUE MISSED SCREEN`
- `RANKING MISS`
- `HOLD/PASS`
- `FALSE-NEGATIVE HOLD`
- `BAD LOCK`
- `CORRECT HOLD, OVER LANDED`

Do not classify a match as a missed lock from final score alone.

---

## 15. User-facing board contract

For normal `list upcoming matches`, `what's next?`, or daily-board requests, output:

1. coverage status/count line;
2. FOCUS board;
3. WATCHLIST only when useful or requested;
4. next-match designation based on the persisted coverage ledger.

Example:

`Coverage: 42 universe | 27 eligible | 27 screened | 5 focus | 8 watch | 14 pass | 0 unresolved`

If any eligible row remains unresolved, say so explicitly.

---

## 16. Fail-closed rules

Do not claim `full slate screened` when:

- the relevant AiScore listing/window was not fully traversed;
- eligible fixture counts do not reconcile;
- a known AiScore league block is missing;
- timezone conversion is unresolved;
- newly discovered eligible AiScore fixtures have not yet been screened.

Use:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

or, when the sweep is complete but screening/counts are not:

`COVERAGE INCOMPLETE — board provisional`

---

## Operating principle

**Sweep AiScore only. Screen every eligible AiScore fixture. Research each match normally. Shorten the display, not the screened universe. Route the same evidence state through v0.2.49 official, v0.2.47 shadow, and v0.2.48 shadow.**
