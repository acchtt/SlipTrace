# Football Chat Transfer Handoff — 2026-08-21

**Project:** Football v1.0 / SlipTrace  
**Purpose:** Preserve the complete operational state, current model, recent live decisions, user corrections, audit lessons, Airtable control details, and response protocol when moving to a new chat.  
**Status at handoff:** Football betting remains **PAUSED** for official execution. **SHADOW CALIBRATION ONLY.**

---

## 1. Canonical model state

Active model: **Football v0.2.49 — Team Goal/Concede Profile Weighting Gate — AUDIT MODE**.

Canonical source: `models/football/CURRENT_MODEL.md`.

Newest active rules:

- **v0.2.47 — High-Scoring Halftime Compression / Goal-Saturation Gate**
- **v0.2.48 — Dominant Goal-Carrier Slate Priority and Monitoring Allocation**
- **v0.2.49 — Team Goal/Concede Profile Weighting Gate**

All older synchronization, reset, style, provider-quality, settlement, protected-line, market-scan, Airtable, timeliness, validator, circuit-breaker and audit rules remain active unless explicitly superseded.

### Audit operating values

- `1u = 1,000,000 VND`
- Default shadow stake: **0.125u = 125,000 VND**
- Minimum odds reference: **1.70** unless explicitly overridden
- Official football betting: **PAUSED**
- Shadow calibration: **ACTIVE**
- Official ledger writes: **ON HOLD** unless explicitly approved
- `/ledger.json` is the official accounting source only and must not be loaded or written for ordinary shadow decisions
- Directional AH/DNB/ML selections remain quarantined from official promotion
- Totals remain the main audit focus

---

## 2. Mandatory execution-control protocol

Every shadow/executable verdict requires an Airtable Decision State write and **Validator PASS**.

If Airtable decision-state validation is unavailable:

`NO BET — HOLD — decision-state validation unavailable`

Do not issue a shadow/executable PASS without the Airtable validation step.

### Airtable base/table

Base: `SlipTrace Football Decision Control`  
Base ID: `appWyZJjitSBATXAU`

Decision States table ID: `tblQmUpd5WjBLQ38X`  
Circuit Breaker table ID: `tblcJfh8zbNyzjArK`

### Decision State important field IDs

- Assessment ID `fldw5PxzbUDRxPTN6`
- Match `fldOhDnn8HJx4cv5H`
- Competition `fldHMLKkm2qToiZ1O`
- Model Version `fldEozpHKiyLBvou9`
- Assessment Time `fld3FF6oSQjdYFOAy`
- Minute `fldGl8MD1MDJETVyZ`
- Score `fldTN65kHAyUj7TyW`
- Reset Epoch `fldbPsoX2ZxywShf0`
- Assessment Period `fldhnnmkvbUvEFH52`
- Verdict `fldKHk8vNQMYGx0GU`
- Candidate `fld9xNR6kkR8oYISu`
- Line `fldLrWtsOoe503UTv`
- Odds `fldvslKY49svSlXCx`
- Goal Environment `fldDyMTJlF5gPX1RO`
- Synchronized State `fldXbAUPmgQkOZdaX`
- Reset Resolved `fldJR1gsmr6g7zncK`
- Competition Format Verified `fld2sc8z4Fh5gL7Op`
- Utility Verified `fldXAYNAW0LS8sUF1`
- xG Role `fldulLHGJxfWKrJj9`
- Primary Channels `fld6Rcz1ryT2TsfMu`
- Independent Primary Channels `fldGz8gbcyuPUqZWD`
- Favorite Fade Gate `fldZhL6NWpiNCwQCS`
- Directional Persistence `fldz2otbFIu7Dr8OE`
- Major Markets Scanned `fldoWuPOW46IuEhlF`
- Circuit Breaker Mode `fldnMIgdPKLcXc64W`
- Validator Result `fldCuQ8rqNrmhgpld`
- Fail Reasons `fldlkav9gyDQI7jKb`
- Evidence Summary `fldTAwWTDJvfusgj7`
- Margin Incentive Propagated `fldU7zDQfsrNz7ynX`
- HT Goals `fldwssNwjgGXOcmtE`
- HT Saturation Gate `fldcdRGbFGhlRqzlY`
- Conversion Quality Gate `fldv1u9Hd3eMwckYa`
- Second-Half Hazard `fldrRCpTPn0tQjYCy`
- Remaining Goal Budget `fldkiqxcL1YRjJNZ6`

Verdict choices include:

- `NO BET — HOLD`
- `NO BET`
- `SHADOW LEAN — DO NOT PLACE`
- `OFFICIAL BET`

Validator choices: `PASS / HOLD / FAIL`.

Official betting is paused, therefore do not use `OFFICIAL BET` unless a later explicit model/audit change authorizes it.

---

## 3. User interaction / response protocol

The user strongly prioritizes **speed and verdict-first delivery** during live matches.

Operational response sequence:

1. Parse the screenshot/state immediately.
2. Perform the **minimal Airtable validator write first**.
3. If PASS, output immediately:
   - `SHADOW LEAN — DO NOT PLACE: <line> @ <odds>, 0.125u simulated`
4. If not PASS, output immediately:
   - `NO BET — HOLD`
5. Give only 1–3 short sentences of reasoning after the verdict.

Do not let explanation consume the executable window.

### Continuity after delayed delivery

If a prior PASS was reached but delivery was late and the user confirms the same market is still available, perform a **minimal continuity recheck** only:

- current score
- material event/reset state
- line still materially same

If unchanged, re-issue promptly rather than restarting the full analysis.

This lesson came from the Qatar SC missed-win sequence.

---

## 4. Core evidence principles retained

- xG/xGOT are **secondary**, not primary by themselves.
- Raw shots or SOT cannot be relabeled into multiple independent channels.
- One event cluster cannot count twice.
- Persistence requires comparable score-stable snapshots or a clearly repeated timestamped sequence.
- Pressure persistence is not automatically scoring-hazard persistence.
- `PERSISTENT BUT UNPROVEN` cannot promote an Over.
- Under cannot be promoted from vague conservation/saturation narratives alone; actual suppression/deceleration must be observed.
- One team may fund an Over by itself if that team provides sufficient genuinely independent forward evidence.
- Opponent contribution is not universally mandatory.
- After a goal: full tactical/state reset unless an active fallback explicitly applies.
- A material event before delivery invalidates the pending quote as a state-change race.
- When an Over clears, prefer the **lowest eligible protected boundary** with acceptable odds and lower remaining-goal burden.

---

## 5. v0.2.47 halftime compression rules

- 0–2 HT goals: normal halftime reset
- 3 HT goals: `HT COMPRESSION GATE — MODERATE`
- 4+ HT goals: `HT GOAL-SATURATION GATE — STRONG`

After 3+ HT goals:

- first-half activity becomes context only
- fresh second-half conversion-quality evidence is mandatory

After 4+ HT goals, normally require:

- resolved reset
- score-stable second-half sample
- two independent second-half primary channels
- at least one conversion-quality channel
- exact remaining-goal budget
- protected-line comparison
- no-bet comparator

Do not promote an Over from `SECOND-HALF HAZARD: PERSISTENT BUT UNPROVEN`.

---

## 6. v0.2.48 dominant goal-carrier slate priority

### Why it was added

The user correctly pointed out that the model was treating ordinary strong/notable European sides too similarly to elite or near-elite attacking teams such as **Ajax / Benfica / Beşiktaş-type profiles** against clearly weaker opposition.

The slate-selection layer had been spending too much monitoring time on Tier-2/3 matches while stronger one-team blowout routes were available.

### Goal-carrier tiers

**T1 — Dominant Goal Carrier**

A matchup-specific side with a credible **solo 3+ goal route**. Usually requires multiple supporting factors:

- elite/near-elite attacking quality relative to opponent
- squad/talent mismatch
- strong attacking starters available
- opponent defensive weakness / lower competition level
- tactical access for repeated territory / box entries / transition threat
- acceptable format/incentive
- market consistent with mismatch

Ajax-, Benfica-, Beşiktaş-type mismatches are examples of the profile, not permanent membership.

**T2 — Strong Attacking Side / Secondary Carrier**

Good team with meaningful attack but a less reliable solo 3+ route. Salzburg-, Copenhagen-, Midtjylland-, Nordsjælland-type situations may fall here depending on matchup.

**T3 — Shared-Route / Two-Sided Over**

The Over depends materially on both teams contributing or on balanced openness.

### Ranking priority

Normally:

1. T1 dominant-carrier mismatch with strong/acceptable lineup and low format drag
2. T1 with one uncertainty
3. T2 strong favorite with plausible solo route
4. High-quality T3 open match
5. Lower-information/provider-quality matches

Do not keep a weak T2/T3 primary just because time has already been invested if a higher-ranked T1 begins.

### Important limitation

T1 affects **monitoring priority only**. It does not create an automatic Over PASS.

---

## 7. v0.2.49 team goals-for / goals-against profile weighting gate

### Why it was added

Three recent shadow losses — Salzburg, Nordsjælland–St. Gallen and Botafogo — exposed a recurring issue:

`LIVE PRESSURE + MODERATE CHANCE QUALITY -> OVER PROMOTION`

was overpowering a weaker underlying scoring/conceding profile.

The user explicitly instructed that **team goal profile and concession profile must be treated more heavily**.

### Required structural profile

For serious ranked/live Over candidates, evaluate:

**Attack**

- recent goals scored per match
- 2+ scoring frequency
- 3+ scoring frequency
- 0–1 goal frequency
- home/away split
- opponent-strength context
- competition/format context
- attacking lineup quality / missing scorers-creators
- whether multi-goal outputs are repeatable or outlier-driven

**Defense**

- recent goals conceded per match
- 2+ concession frequency
- 3+ concession frequency
- clean-sheet / one-goal concession tendency
- home/away split
- opponent-strength context
- defensive absences / goalkeeper context
- whether heavy concessions are repeatable or outlier-driven

### Goal-route matrix

Compare:

1. stronger team GF profile vs weaker team GA profile
2. weaker team GF profile vs stronger team GA profile
3. stronger team multi-goal frequency vs opponent multi-goal concession frequency
4. two-sided contribution probability vs one-team carrier probability

A one-team route remains valid, but it must have **structural multi-goal support**, not merely badge strength, possession, shots, SOT or forced-chase incentive.

### Revised T1 gate

Strong T1 normally requires:

- high enough multi-goal scoring frequency versus comparable opponents
- opponent repeated 2+/3+ concession vulnerability OR an exceptional talent/competition mismatch
- attacking lineup capable of sustaining output
- no major format drag
- no strong evidence that the favorite commonly settles after taking the lead

If the favorite is commonly held to 0–1 or the opponent commonly limits stronger teams to 0–1, cap the matchup at T2 unless exceptional evidence exists.

### Required profile-support label

Every serious live Over candidate should carry:

- `TEAM PROFILE SUPPORT: STRONG`
- `TEAM PROFILE SUPPORT: ACCEPTABLE`
- `TEAM PROFILE SUPPORT: CONFLICTING`
- `TEAM PROFILE SUPPORT: UNKNOWN`

### Remaining-goal burden interaction

**1 additional goal required**  
A strong live state may pass with ACCEPTABLE profile support.

**2 additional goals required**  
Normally require at least ACCEPTABLE profile support plus repeated live conversion-quality evidence.

**3+ additional goals required**  
Normally require **STRONG profile support + clearly re-accelerating live state**. One upgraded snapshot is insufficient.

Possession dominance, forced chase or raw SOT cannot justify a 3+ remaining-goal burden by themselves.

### Post-lead behavior now matters more

If a team historically protects one-goal leads or reduces attacking output after scoring, this lowers the Over promotion state unless fresh post-goal evidence clearly contradicts it.

### Required compact profile fields

- `Team profile support:` STRONG / ACCEPTABLE / CONFLICTING / UNKNOWN
- `Primary carrier 2+ scoring tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Primary carrier 3+ scoring tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent 2+ concession tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent 3+ concession tendency:` HIGH / MODERATE / LOW / UNKNOWN
- `Opponent contribution route:` STRONG / PLAUSIBLE / WEAK / UNKNOWN
- `Post-lead behavior:` CONTINUES / MIXED / PROTECTS / UNKNOWN

These are structural priors, not independent live evidence channels.

### Validator question added

For an Over PASS, ask:

`Does the team goals-for / goals-against profile support the exact remaining goal burden?`

If materially conflicting and live evidence is not exceptional:

`NO BET — HOLD — team-profile burden not cleared`

No arbitrary numeric 40/60 or similar weighting has been assigned yet. Profile is a **gating prior**, with burden increasing as required remaining goals increase.

---

## 8. Circuit-breaker sample already completed

The four-slot circuit-breaker sample is complete, but official betting remains paused.

1. Austin FC–Dallas O2.25 @1.84 — WIN `+0.105u`
2. Gnistan–Ilves O3.75 @1.83 — WIN `+0.10375u`
3R. Necaxa–León O2.75 @1.91 — FT 1–2 — half-win/half-push `+0.056875u`
4R. Pachuca–Puebla U4.5 @1.70 — FT 2–3 — LOSS `-0.125u`

Nõmme/Kalju O4 was process-invalid/excluded.  
Original Pachuca O4.25 state-change race was void/not counted.

Do not infer official audit exit from completion of this four-slot sample; broader exit criteria remain unmet.

---

## 9. Important recent match history before this transfer

### Barcelona vs Al Ahly — Joan Gamper friendly

- HT 2–0, Al Ahly made it 2–1 around 51'
- Around 67', U4.25 @1.85 became a leading candidate but major substitutions crossed the cooling sample, so HOLD was correct
- Around 73', model incorrectly promoted `SHADOW LEAN O3.75 @1.72`, 0.125u
- FT 2–1
- Result: **LOSS -0.125u**

Lesson: after prior conservation + late substitution reset, first renewed activity should usually cancel an Under into HOLD, not prove Over. Need clear conversion quality or a second stable post-reset snapshot.

### Minnesota United vs Atlanta United

At 27:47, score 0–0:

`SHADOW LEAN O2.0 @1.84`, 0.125u

FT 1–2.  
Result: **WIN +0.105u**

Airtable record: `rec85vMsV5UUJ00N4`.

### Portland Timbers vs San Diego FC

HT 1–1.  
Issued `O3.5 @1.71`, 0.125u.

Match reached 3–1 and line was mathematically secured. User later clarified/closed it as a win.

Result: **WIN +0.08875u**.

Main issue was delivery latency even though validator PASS existed.

### Shanghai Shenhua vs Beijing Guoan

Carried into this chat and settled:

`O2.25 @1.96` — full win `+0.120u`.

### São Paulo vs Bolívar

Carried into this chat and settled:

`O2.25 @1.84` — full win `+0.105u`.

### Qatar SC / Al-Wakrah sequence — critical missed-win lesson

Primary Over-friendly monitor.

At 58:38, 1–1, cumulative approximately:

- xG 0.77–1.04
- shots 13–9
- SOT 3–5
- big chances 0–2
- corners 2–2
- box touches 16–6

Reached:

`SHADOW LEAN — DO NOT PLACE: Over 3.25 @1.84`, 0.125u, Validator PASS.

Delivery was too slow. User said verdict took too long. We treated the original entry as expired. User then confirmed O3.25 was still available, but we overcorrected into a full restart/HOLD, adding more latency. User skipped.

FT **2–2**. O3.25 from the original 58:38 state would have won, but it is **NOT COUNTED** because no fresh executable shadow was re-issued.

Classification: **missed win / execution miss**, not P/L.

Relevant Airtable records:

- `recJOwyup4yRlIwUA`
- `recUiltlg5l5PbQpX`

This directly produced the continuity-recheck rule: after a late-delivered prior PASS, if the user confirms the market remains available, recheck only score/material event/line continuity rather than restarting the whole process.

### RSL vs Dallas

At HT 1–3, four HT goals triggered v0.2.47 STRONG saturation. HOLD after halftime reset was correct. Match later reached 3–3 around 73–74'. No shadow entry was opened in this sequence.

Airtable record: `recPux7H24j19qnEG`.

This remained an example that the **pre-match Over-ranking selection** can be directionally right even if no shadow entry is made.

---

## 10. Current-chat live sequence and outcomes

### A. Mjällby vs RB Salzburg

Competition: UEFA Europa League qualification, first leg.

Pre-match view:

- O2.75 @1.82
- O3.0 @2.06
- O2.5 @1.66 below floor
- HOLD due first-leg structure and no live evidence

Known Airtable records:

- pre-match lock: `rechUBOvyZcQt9Rs5`
- 12' state: `recsmWZDbK8LvCqhF`
- 21' state: `rec2BrrwCzjR1PIH0`

At 30': 0–0. Salzburg had heavy possession/shot/SOT/box-touch dominance but only about 0.21 xG, no big chances, and limited inside-box quality. Correct verdict: HOLD.

At 38': conversion quality upgraded enough to issue:

`SHADOW LEAN — DO NOT PLACE: Over 1.75 @1.85`, 0.125u simulated.

Rationale at entry included roughly:

- 10 shots
- 5 SOT
- 1 big chance
- 6 inside-box shots
- 17 box touches
- meaningful +inside-box and +big-chance improvement from the prior checkpoint

User later stopped monitoring at 77' with score still 0–0.

FT: **Mjällby 1–0 Salzburg**.

Result: **LOSS -0.125u**.

### B. Nordsjælland vs St. Gallen

At 36', Nordsjælland 1–0 St. Gallen:

- xG ~0.26–0.40
- shots 4–6
- SOT 1–1
- big chances 0–0
- inside-box shots 1–4
- box touches 11–7

HOLD.

At 42:30:

- both teams had added shots, SOT and inside-box attempts while score remained 1–0

Issued:

`SHADOW LEAN — DO NOT PLACE: Over 3.0 @1.81`, 0.125u simulated.

FT: **1–0**.

Result: **LOSS -0.125u**.

This became a key example of over-promoting balanced live activity without enough structural scoring/conceding support.

### C. Slate-selection correction after European card

User observed that many genuinely notable/elite teams on the broader card went Over while the model had spent attention on lower-tier European names.

Initial assistant response incorrectly compared clubs such as Salzburg/Copenhagen/Midtjylland/Nordsjælland too closely with true upper-tier attacking brands.

User corrected the distinction explicitly:

- Ajax / Benfica / Beşiktaş-type teams belong in the higher goal-carrier tier
- Salzburg/Copenhagen/Midtjylland/Nordsjælland-type teams are lower for this specific one-team goal-carrying job

This led to **v0.2.48**.

### D. CONMEBOL ranking and Botafogo vs Cienciano

For the CONMEBOL block, primary monitor was **Botafogo vs Cienciano** due the first-leg 1–6 aggregate and forced chase.

Important correction: Botafogo was treated as a **T1 opportunity**, but not an Ajax/Benfica/Beşiktaş-level proven T1 carrier. The value case came mainly from forced chase + transition route.

At 1:34: 0–0, pre-live O3.5 ~1.81. HOLD pending evidence.

Around 9': Botafogo scored, 1–0. Full reset. Pre-goal stats were still light. HOLD.

Around 16': approximately:

- xG 0.47–0.03
- shots 3–1
- SOT 1–0
- big chances 1–0
- inside-box 3–0

HOLD.

Around 26': approximately:

- shots 6–2
- SOT 4–0
- xG 0.69–0.05
- big chances 1–0
- inside-box attempts not materially improving enough

HOLD.

At 33:12, Botafogo 1–0 Cienciano:

- xG ~0.87–0.05
- shots 7–2
- SOT 4–0
- big chances 2–0
- inside-box shots 5–0
- xGOT ~1.07–0.00

Since the prior checkpoint there was fresh conversion-quality improvement: +1 big chance and +2 inside-box attempts.

Issued:

`SHADOW LEAN — DO NOT PLACE: Over 3.0 @1.81`, 0.125u simulated.

Airtable record: `recKgcJje5PRg8Zui`.

FT: **Botafogo 1–0 Cienciano**.

Result: **LOSS -0.125u**.

Airtable settlement note was added to the same record.

Audit lesson: forced-chase incentive plus moderate chance quality can overstate sustained scoring hazard if the team's structural multi-goal profile and post-lead behavior are not strong enough.

This loss directly led to **v0.2.49**.

---

## 11. Recent shadow P/L context

Do not mix ranking success, missed wins or non-entered matches into shadow P/L.

Prospectively issued/settled shadows explicitly tracked in this recent continuity set:

- Barcelona–Al Ahly O3.75 @1.72: `-0.125u`
- Minnesota–Atlanta O2.0 @1.84: `+0.105u`
- Portland–San Diego O3.5 @1.71: `+0.08875u`
- Shanghai Shenhua–Beijing Guoan O2.25 @1.96: `+0.120u`
- São Paulo–Bolívar O2.25 @1.84: `+0.105u`
- Mjällby–Salzburg O1.75 @1.85: `-0.125u`
- Nordsjælland–St. Gallen O3.0 @1.81: `-0.125u`
- Botafogo–Cienciano O3.0 @1.81: `-0.125u`

Net for this listed 8-entry continuity sample: **-0.08125u**.

This is a small audit sample and must not be treated as proof of durable edge or failure by itself.

The last three listed Over shadows all lost 1–0 FT, which is why v0.2.49 now raises the structural profile burden.

---

## 12. Ranking tracker must remain separate from entry P/L

The user specifically wants **Over-friendly ranking performance tracked separately from actual shadow-bet ROI**.

For prospectively ranked matches, track:

- final total goals
- O2.5 hit/miss
- 3+ total hit indicator
- 4+ total hit indicator
- assigned tier and rank
- T1 carrier final goals where relevant

A match that goes Over without a synchronized PASS is a **selection success**, not a betting win.

A live PASS that was reached but not delivered/executed in time is an **execution miss**, not a betting win.

Examples:

- Qatar / Al-Wakrah FT 2–2: ranking right, missed execution, not P/L
- RSL / Dallas reached 3–3: ranking direction right, no shadow P/L

---

## 13. Current major diagnostic conclusion

The current audit no longer treats the main problem as simply 'not selecting enough Over-friendly matches.'

Two distinct layers must be evaluated separately:

### A. Slate selection / ranking

v0.2.48 corrects the prior mistake of ranking merely notable T2/T3 teams too close to genuine elite/near-elite solo goal carriers.

### B. Live entry validation

v0.2.49 corrects the more recent mistake of letting live pressure + moderate conversion quality overpower weak/uncertain team scoring and opponent concession profiles.

The intended operating balance is now:

**Select the right high-ceiling matches aggressively, but require structural goal/concede support and strict live validation before entry. Execute immediately once validated.**

---

## 14. Practical next-chat checklist

At the start of the new chat:

1. Load `models/football/CURRENT_MODEL.md`.
2. Load this handoff: `models/football/handoffs/CHAT_TRANSFER_HANDOFF_2026-08-21.md`.
3. Treat **v0.2.49** as canonical.
4. Keep official betting paused.
5. Do not load/write `/ledger.json` unless official accounting reconciliation is explicitly authorized.
6. Keep Airtable Decision State + Validator PASS mandatory.
7. For slate ranking, distinguish T1/T2/T3 prospectively.
8. Before any serious Over PASS, establish the team GF/GA structural profile and `TEAM PROFILE SUPPORT` state.
9. Apply stronger profile burden as required remaining goals increase.
10. For live screenshots, answer **verdict first and fast**.
11. If PASS, Airtable write first, then immediate shadow line/odds/stake, explanation second.
12. Keep ranking performance separate from entry P/L.
13. Do not use hindsight to re-tier teams after results.

---

## 15. One-line operating principle for continuation

**Rank true goal carriers rather than famous badges; weight demonstrated goals-for/goals-against behavior heavily; let live evidence time the entry rather than erase profile conflict; and deliver validated verdicts immediately.**
