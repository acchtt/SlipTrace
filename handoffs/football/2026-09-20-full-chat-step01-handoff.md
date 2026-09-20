# Football v2.0 — CURRENT CHAT HANDOFF — 2026-09-20 ICT

**Purpose:** preserve the full operational state of the current Football v2.0 chat and make the next chat start from **Step 01 / Work structural ranking** without losing the Step-2/live/audit state accumulated here.

**Repo:** `acchtt/SlipTrace`  
**Branch:** `main`  
**Official track:** Football A  
**Airtable base:** `appWyZJjitSBATXAU`

---

# 0. NEW-CHAT STARTUP DIRECTIVE — LAUNCH STEP 01 FIRST

When this handoff is opened in a new chat:

1. Read this file fully.
2. Read `models/football/CURRENT_MODEL.md`.
3. Load and execute:
   `models/football/prompts/01_WORK_DAILY_SWEEP.md`
4. If the user attached a fresh `AISCORE_FIXTURES_*.zip`, validate/extract it exactly as Step 01 requires and run structural ranking.
5. If no fresh fixture package is attached, **do not invent or rerun Step 0**. Preserve the current frozen board and Airtable state below; tell the user Step 01 is loaded and ready for the next fixture package.
6. Never overwrite prior official picks, WAITs, HOLDs, actual bookmaker execution, or audit rows merely because a new Work run starts.
7. After Step 01, continue normal production:
   `STEP 01 WORK -> STEP 02 XI+ODDS -> STEP 03 LIVE -> STEP 04 AUDIT`.

Portable launcher text is stored in:
`handoffs/football/01_STEP01_RESUME_LAUNCHER.txt`

---

# 1. Canonical model / process state

Always use the current repo as authority, not memory.

Read:
- `models/football/CURRENT_MODEL.md`
- `models/football/prompts/01_WORK_DAILY_SWEEP.md`
- `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`
- `models/football/prompts/03_NORMAL_CHAT_LIVE.md`
- `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- `models/football/rules/MODEL_RULES_FOOTBALL_AB_DECAY_FIRST_EXECUTION.md`
- `models/football/rules/MODEL_RULES_FOOTBALL_A_LIVE_DECAY.md`
- `models/football/rules/MODEL_RULES_FOOTBALL_A_AUTO_PUBLISH_USER_PREMATCH_ODDS.md`
- `models/football/rules/MODEL_RULES_FOOTBALL_A_NO_CROSS_MATCH_EXPOSURE_SUPPRESSION.md`
- active session override:
  `models/football/session_overrides/SESSION_OVERRIDE_2026-09-19_TO_2026-09-20_EARLY_CONVERSION.md`

## Critical execution principles

### Decay-first burden protection
`STRONGER STRUCTURE = MORE CONFIDENCE TO WAIT, NOT AUTOMATIC PERMISSION TO BUY A HIGHER TOTAL.`

Normal direct exposure requires:
- football/XI intact;
- market alignment acceptable;
- selected burden at/below supported burden unless a separately justified execution exception is explicitly documented;
- price >= hard floor;
- suppression/upper-tail/exposure gates clear.

### WAIT vs HOLD completeness
Never use HOLD merely because the current bookmaker total is too high.

- supported line available + price clears -> DIRECT / LOCK path
- supported line available + price below floor -> PRICE WAIT
- current line above supported burden -> LIVE DECAY WAIT
- football/XI/evidence itself fails -> STRUCTURAL HOLD
- genuine frozen PASS -> PASS

All active WAITs remain visible until execution, invalidation, expiry, or match completion.

### Live verdict-first latency control
This was patched after Hong Kong U23–Thailand U23 was missed because the verdict arrived after a goal.

For live/just-started screenshots:
`MINIMAL STATE READ -> ACTIONABLE VERDICT FIRST -> PERSIST / RESEARCH / EXPLAIN SECOND`

Do not delay a clear live action for web research, Airtable writes, or long prose.

Relevant commits from this chat:
- `models/football/prompts/03_NORMAL_CHAT_LIVE.md`: `fa26fa276ce14ac008c9d9ee025754444ca17e90`
- `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`: `04c3475c9517bdfecedc66454fee6cb666f6647c`
- procedure: `efb33b42f64280e5b5e14ebef756e602de6a12a5`
- `CURRENT_MODEL.md`: `3e1519bdf68c82d383180366a6d1da878034b071`

### No cross-match suppression
A valid fixture is not blocked because another higher-ranked fixture is active.

### Auto-publish
User-supplied prematch executable odds that clear all gates -> immediately OFFICIAL LOCK + Website Pick. No second confirmation required.

### One exposure per match
Still mandatory.

### No retroactive backfill
Missed entry is audit-only.

---

# 2. Temporary Sep19/20 rule still active until 2026-09-21 00:00 ICT

For eligible A1/A2 FOCUS and A2 WATCHLIST:

- O2.5: QUALITY-PROVEN 3+ path may clear.
- O2.75: ROBUST 3+ path + non-trivial fourth-goal support.
- O3.0+: permanent strict 4+ / TRUE CC+ / elite two-sided standard.
- B+/B/PASS do not receive the automatic temporary relaxation.

Early-conversion score-epoch logic remains active for eligible A1/A2 FOCUS cases.

Recent H2H suppression must be screened:
`same-venue recent H2H -> all-venue recent H2H -> long-run H2H`.

Do not let long-run averages erase recent same-venue suppression.

---

# 3. New execution lesson from this chat — fast-start miss risk

## Feyenoord–Utrecht
Frozen:
- #9 A2 FOCUS
- TWO-SIDED
- original supported burden around O2.75/O3.0 execution target

The match **never reached the intended decay target before two early goals** and the user later reported it at **5-0**.

Airtable decision:
- `recBNVpk2HhcMgyRE`
- state: `MISSED EXECUTION — DECAY TARGET NEVER REACHED BEFORE EARLY GOALS — NOW 5-0`

Interpretation:
- structural read was right;
- execution path missed;
- do not retroactively book it;
- do not turn this into a blanket “always buy high totals” rule.

## Match-specific follow-on adjustments
These are **match-specific current decisions, not yet a permanent global rule**.

### Twente–PSV
Frozen:
- #1 A1 FOCUS
- TWO-SIDED
- PROVEN+PROVEN
- original supported burden O3.0

After the Feyenoord miss, repeated 4+ H2H/upper-tail evidence plus intact elite routes justified a **match-specific fast-start-adjusted lock**:

- OFFICIAL: **O3.5 @1.68, 1u**
- Decision: `reclye3a5IXv9Waqu`
- Website Pick: `recG4LY8BFA8PFiMH`

Do not stretch above O3.5.

### AZ–Telstar
Frozen:
- #10 A2 FOCUS
- ELITE CARRIER / TRUE CC+
- original supported burden O3.0

Current market was O3.5 @1.78 / O3.75 @1.98 / O4 @2.23.

Revised match-specific execution:
- **SHALLOW LIVE DECAY WAIT**
- target **O3.25 >=1.65**
- Decision: `recf5YMOJaXfA8LrQ`

Reason: reduce fast-start miss risk, but Telstar route remains nominal and AZ recently had 0-0 / 0-1 low-output results; therefore do not jump straight to O3.5.

### Frosinone–Como
Frozen:
- #42 B+ WATCHLIST
- NOMINAL+SUPPORTED
- original burden O2.5

Step-2 form/environment hardener improved the case, but current board was O3.25 @1.73 / O3.5 @1.95 / O3.75 @2.17.

Current decision:
- **QUALIFIED — SHALLOW LIVE DECAY**
- target **O3.0 >=1.65**
- Decision: `rec72m6A5J1KTbKhH`

This is another match-specific shallower wait after the Feyenoord audit; not a global B+ promotion rule.

---

# 4. B+ false-negative vs A2 false-positive audit signal

The user repeatedly observed that protected B+ HOLDs often convert while some official A2 locks fail.

## Paired inversion 1
### Incheon–Daejeon
- Official O2.5 @2.07, 1u
- FT **1-0**
- LOSS -1u
- Website Pick: `recpu0UjUuk4YhThh`
- Decision: `recJzbAfCPA4HGD7c`

### Pohang–FC Seoul
- B+ HOLD O2.5 @1.96
- user reported match reached **3 total goals**
- guaranteed counterfactual WIN at held line
- Decision: `recmul7ClaVQVVJvV`

Audit signal:
- B+ independent-hardener requirement may be too restrictive at protected O2.25/O2.5 when both usable routes are preserved;
- A2 “route preservation” may still overstate actual conversion reliability.

## Paired inversion 2
### Gamba–Vissel Kobe
- Official O2.5 @1.89, 1u
- user later reported it was still 0-0 while Machida had reached 3 goals
- final result was not supplied in this chat at handoff time; revalidate before settlement.
- Website Pick: `recCuiPA4qFwEbeVP`

### Machida–Kashiwa
- B+ HOLD O2.25 @1.82
- user reported match had already produced **3 goals**
- Decision: `recJbyPGrfUv2pm1I`
- provisional false-negative audit warning; do not invent final score unless verified.

Do not automatically promote all B+ cases. Preserve this as an audit question for Step 04.

---

# 5. Current / recent Step-2 states from this chat

## OFFICIAL LOCKS / Website Picks

### Jeonbuk–Gwangju
- O2.5 @1.73, 1u
- Website: `recwXD2MY21S3OFc4`
- result not settled in this handoff; revalidate before updating.

### Gamba Osaka–Vissel Kobe
- O2.5 @1.89, 1u
- Website: `recCuiPA4qFwEbeVP`
- user later reported 0-0 while Machida reached 3; final not supplied here.

### Incheon–Daejeon
- O2.5 @2.07, 1u
- FT 1-0
- LOSS -1u
- Website: `recpu0UjUuk4YhThh`

### Brøndby–Copenhagen
- O2.5 @1.65, 1u
- Decision: `recrzO4oUQo81HPfe`
- Website: `recEWZJ77wnVI0AKc`

### Kalmar–Häcken
- O2.5 @1.69, 1u
- Decision: `rec1WxhczBlccDHiX`
- Website: `rec9jS72gqYLbCPmE`
- IMPORTANT: lineup-page screenshot was once misread as HT 1-0; user corrected it. It was **not a live score**. State was reverted to PRE. Never infer a live score from lineup-page thumbnail overlays.

### Twente–PSV
- O3.5 @1.68, 1u
- match-specific fast-start-adjusted execution
- Decision: `reclye3a5IXv9Waqu`
- Website: `recG4LY8BFA8PFiMH`

### Bournemouth–Liverpool
Frozen:
- #18 A2 WATCHLIST
- TWO-SIDED / PROVEN+SUPPORTED
- supported O2.75

Latest assessment:
- **OFFICIAL LOCK O2.75 @1.74, 1u**
- Decision: `recwv21aPmEszYddZ`
- Website: `recZ008hIuCCgzTu9`

Reason: robust 3+ route plus non-trivial fourth-goal support, XI intact, recent H2H non-suppressive. Do not stretch to O3.

## ACTIVE WAITs

### AZ–Telstar
- shallow target **O3.25 >=1.65**
- current pre board at assessment: O3.5 @1.78 / O3.75 @1.98 / O4 @2.23
- Decision: `recf5YMOJaXfA8LrQ`

### Frosinone–Como
- shallow target **O3.0 >=1.65**
- current board at assessment: O3.25 @1.73 / O3.5 @1.95 / O3.75 @2.17
- Decision: `rec72m6A5J1KTbKhH`

### Vaduz–Thun
- target **O2.5 >=1.65**
- current pre board at assessment: O3.5 @1.75 / O3.75 @1.94 / O4 @2.20
- Decision: `recim9Z5U9lSYKJ9v`

### Feyenoord–Utrecht
No longer active — target missed before early goals; audit-only miss.

## STRUCTURAL HOLDs / PASS

### Sigma Olomouc–Sparta Prague
- Frozen #39 B+ WATCHLIST, NOMINAL+SUPPORTED, supported O2.5
- O2.5 @1.67
- **STRUCTURAL HOLD — B+ positive gate not cleared**
- Decision: `recH3Nf0plXO72stH`

### Manchester City–Sunderland
- Frozen #25 B+ WATCHLIST / CARRIER-LED / PROVEN+NOMINAL
- supported O2.75
- current board: O2.5 @1.61 / O2.75 @1.78 / O3 @2.04
- **STRUCTURAL HOLD — B+ carrier gate not clear enough**
- strong XI with Haaland is preservation; not enough new self-funded 3+ proof to rewrite frozen B+
- Decision: `recCIh4Zxvngj9VkX`

### SV Ried–Wolfsberger
- Frozen #30 B+ WATCHLIST, supported O2.5
- O2.5 @1.68
- STRUCTURAL HOLD
- Decision: `recBpaFg8ufF0FRPt`

### Hartberg–LASK
- Frozen #31 B+ WATCHLIST, supported O2.5
- current market starts O3.0 @1.69
- STRUCTURAL HOLD because B+ gate itself remains uncleared; not a simple line-only WAIT
- Decision: `recyVNkK21IW5rpHD`

### Sønderjyske–Randers
- Frozen #40 B+ WATCHLIST, supported O2.5
- O2.5 @1.65
- STRUCTURAL HOLD
- Decision: `recWxavvjzwTpFUli`

### Halmstads–AIK
- frozen B/PASS, no supported burden
- PASS

### Vålerenga–Fredrikstad
- frozen B/PASS, no supported burden
- current O2.75 @1.64 / O3 @1.82
- PASS
- Decision: `recUyFMmuRLAmxKDy`

---

# 6. Live/U23 exception lane from this chat

## Iran U23–China U23
User granted explicit match-specific live exception.

Official:
- **O2.0 @1.65**
- 1u
- around 5' at 0-0
- Website Pick: `recs4d813ECudzWem`

Revalidate result before settlement.

## Hong Kong U23–Thailand U23
At ~2' 0-0:
- O2.5 @1.72 would have cleared under a match-specific live exception
- verdict arrived too late; goal occurred first
- no retroactive exposure

This event directly caused the live verdict-first latency patch.

Later at 1-0 ~25':
- O2.75 @1.59 below floor
- O3.0 @1.81 higher score-epoch burden
- no chase / HOLD

Airtable:
- `recyRYP8CVT9xvCZ5`

---

# 7. Actual bookmaker execution is model-recommended execution

The user clarified a crucial accounting point:

**The bets visible in bookmaker history are model-recommended lines that the user actually placed, even when they never came back to chat to confirm/persist them.**

Therefore do NOT classify them as independent personal bets.

Maintain three audit categories:

1. **Confirmed/persisted model exposure** — recommendation explicitly confirmed/published in chat.
2. **Unconfirmed model-recommended execution** — user physically placed a model-recommended line but did not return to confirm it, so Website Picks may miss it.
3. **Independent personal bet** — only if user explicitly says it was their own non-model bet.

Airtable reconciliation row:
- `recn0dQtcWeprwcGf`

User bookmaker footer for Sep19–20:
- **28 bets**
- total stake **8,519,552 VND**
- net **+1,113,174.30 VND**
- roughly **+13.07% on turnover**

Visible examples from screenshots:
- Club America–Chivas O2.5 @2.04 300k WIN +312k
- Portland–Atlanta O2.75 @1.90 300k LOSS
- Nashville–Chicago O2.75 @1.97 300k HALF WIN +145.5k
- Monterrey–Cruz Azul O2.5 @1.90 300k LOSS
- St Louis–Toronto O2.75 @1.98 300k WIN +294k
- DC United–Charlotte O2.75 @1.90 300k HALF WIN +135k
- Montreal–Columbus O2.75 @2.25 270k LOSS
- Sevilla–Barcelona O3.5 @1.90 350k WIN +315k
- Anderlecht–Zulte O2.5 @1.99 300k WIN +297k
- Ajax–Excelsior O3.5 @1.90 341,802 WIN +307,621.80
- Stuttgart–Dortmund O3.5 @1.90 300k LOSS
- Sparta–Heerenveen O3.25 @1.90 300k WIN +270k
- Molde–Aalesund O3.75 @1.81 300k LOSS
- ADO–Cambuur O3 @1.90 300k LOSS
- KR–Vikingur O4 @1.90 300k LOSS
- Werder–Augsburg O2.5 @1.90 300k WIN +270k
- Vasteras–Malmo O2.5 @1.90 300k LOSS
- Tottenham–Aston Villa O2.5 @1.90 300k WIN +270k
- La Paz–Correcaminos O3.75 @2.03 300k HALF WIN +154.5k
- Alianza Lima–ADT Tarma O2.5 @1.92 300k LOSS
- Piratas–Venados O2.5 @1.91 300k WIN +273k
- Gent–Standard O2.25 @2.01 300k WIN +303k
- Bayern–Union O4.25 @1.91 357,750 WIN +325,552.50
- Rapid Wien–WSG Tirol O2.5 @1.96 300k WIN +288k
- Greuther Furth–Magdeburg O3.75 @2.14 300k LOSS
- Hoffenheim W–Wolfsburg W O3.25 @1.88 300k HALF LOSS -150k
- Mainz W–Frankfurt W O4 @1.91 300k WIN +273k

One cropped bookmaker row was not fully legible; do not invent its exact line/odds/stake.

Do not overwrite historical model recommendation odds with bookmaker execution odds. Compare them as separate execution evidence.

---

# 8. Current Work board / website schedule

Current Work board:
- **`B-20260920-1401-20260921-0300`**
- window: **20 Sep 14:01 -> 21 Sep 03:00 ICT**
- **42 publishable fixtures**
  - 16 FOCUS
  - 26 WATCHLIST

The website schedule was corrected to publish this Work board, not the manually-created K1/J1 mini-board.

Important correction:
- a temporary manual K1/J1 schedule had been published by mistake;
- its website schedule timestamps were cleared;
- assessments remain in Airtable for audit, but it is not the authoritative Work-board schedule.

Current Work schedule spans approximately:
- first: Feyenoord–Utrecht
- through late slate including Porto–Benfica
- use Airtable `tblcl1UAyMqZT6Ub0` and Board ID `B-20260920-1401-20260921-0300` as authority.

---

# 9. Airtable IDs / persistence

Base:
- `appWyZJjitSBATXAU`

Tables:
- Coverage / Work PRE: `tblcl1UAyMqZT6Ub0`
- Decision States: `tblQmUpd5WjBLQ38X`
- Website Picks: `tblg3J5sbJYbzuTYD`

Important process/audit rows:
- restored WAIT completeness: `rec9vyKWtOrjgoOaY`
- temporary override: `recXwoow0JdvolAbo`
- Nordic audit: `recrAeaEMw5OLClhT`
- actual bookmaker execution reconciliation: `recn0dQtcWeprwcGf`

Always search Airtable before reconstructing an official bet/result from memory.

---

# 10. Recent settled / known results that matter to the model audit

Known from this chat:
- KR–Vikingur O4 -> LOSS
- ADO–Cambuur O3 -> LOSS
- Molde–Aalesund O3.75 -> LOSS
- Stuttgart–Dortmund O3.25 -> LOSS
- Roma–Inter O2.75 -> WIN
- Luzern–Grasshopper O3.5 -> WIN
- Sparta–Heerenveen O3.25 -> WIN
- Ajax–Excelsior O3.5 -> WIN
- Sevilla–Barcelona O3.5 -> WIN
- St Louis–Toronto O2.75 -> WIN
- Monterrey–Cruz Azul O2.5 -> LOSS
- Nashville–Chicago O2.75 -> HALF WIN
- Incheon–Daejeon O2.5 -> LOSS, FT 1-0

Counterfactual/false-negative signals:
- Pohang–Seoul held O2.5 @1.96 -> user reported 3 total goals
- Machida–Kashiwa held O2.25 @1.82 -> user reported 3 total goals
- Feyenoord–Utrecht WAIT target missed -> user reported 5-0 after early goals

Do not settle any match not explicitly completed/verified.

---

# 11. Nordic warning remains audit-only, not blanket rule

Recent official Nordic sample had performed poorly. Same-venue H2H, conversion stability and secondary-route independence should receive explicit attention.

Do **not** create a blanket Nordic PASS unless the user explicitly authorizes a permanent safeguard.

---

# 12. Image interpretation safeguard

A repeated error in this chat:
- lineup pages can contain thumbnail/score-style overlays at the bottom;
- those are **not necessarily live-score evidence**.

Rule:
- treat an AiScore lineup page as XI evidence only;
- infer live score only from a clearly live-score/market screen or explicit user statement;
- if ambiguous, do not change a PRE Website Pick to LIVE.

This specifically corrected Kalmar–Häcken.

---

# 13. What the next chat should do after loading this handoff

## First action
Launch Step 01 using the portable launcher.

## If a new fixture ZIP is attached
Run fresh Work structural ranking, preserving all prior slate/audit state.

## If the user instead immediately sends XI/odds/live screenshots
Do not force them back to Step 01. Continue the existing current slate from Airtable using this handoff and the active canonical model.

## For every Step-2 assessment
Use:
`FROZEN PRE -> XI -> MARKET HISTORY -> H2H/SUPPRESSION -> BURDEN -> CURRENT MARKET -> DECAY/FAST-START EXECUTION -> EXPOSURE`

## For live
Verdict first.

## Key unresolved model question for later Step 04
Audit whether:
- protected B+ O2.25/O2.5 gates are too restrictive after multiple false negatives;
- some A2 locks are over-promoted from route preservation despite weak conversion reliability;
- strongest A1/A2 Dutch matches need a formally-defined shallower-decay / fast-start lane rather than ad hoc match-specific adjustments.

Do not promote that final fast-start rule globally until the user approves it after audit.

---

# 14. New-chat one-line instruction

**Read this handoff + CURRENT_MODEL, launch Step 01, preserve Airtable/Website state exactly, and do not repeat the two key mistakes: silent HOLD instead of WAIT, or waiting so deep on elite fast-start matches that the target becomes unreachable before early goals without an immediate score-epoch reprice.**
