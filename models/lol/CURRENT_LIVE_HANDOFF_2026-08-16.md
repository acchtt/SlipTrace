# CURRENT LIVE HANDOFF — 2026-08-16 UTC+7

**Purpose:** Preserve the complete operating state from the long 2026-08-16 live-betting chat so a new chat can continue immediately without rebuilding the model or becoming more conservative merely because context changed.

---

## 1. Authority and active model

- Repository: `acchtt/SlipTrace`
- **GitHub = model/rules authority.**
- **Airtable = canonical maps/snapshots/positions/rosters ledger.**
- Active analytical model: **LoL v0.3.58 canonical**.
- `v0.3.59` and `v0.3.60` are retired/discarded from the active analytical hierarchy. They may remain only as historical/audit artifacts and must not be loaded, blended, or auto-restored.
- User instruction that established this state: **“Discard newer versions, update this version accordingly.”**
- New positions must be recorded as **LoL v0.3.58**.
- Do not create/promote a newer model from an individual outcome unless the user explicitly asks for a model change.

Primary authorities:
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
3. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
4. retained v0.3.57 through v0.3.26 deltas/procedures according to CURRENT_MODEL
5. this handoff **last**

The active v0.3.58 now directly contains the narrow corrections that were missing after the reset. Do not load v0.3.59/v0.3.60 to obtain them.

---

## 2. Shadow governance

- Official betting remains paused.
- Shadow TAKE stake: **0.25u simulated**.
- Actual exposure: **0u**.
- Minimum odds: **1.60**.
- Maximum one TAKE per market family per map:
  - Moneyline
  - Kill Handicap
  - Total Kills
  - Duration / TT
- Multiple distinct TAKEs on one map are allowed across different families.
- Once a family has a TAKE, that family is closed for the map regardless of later side/line/price.
- No rescue, martingale, chasing, averaging, or stake escalation.
- Correlated same-map positions must each independently qualify and are treated as one evidence cluster.

---

## 3. Mandatory live execution behavior

### Verdict first

On an active map, **no GitHub/Airtable/connector call before the visible verdict**.

Use exact compact first-line style:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Compact output must never mean skipped analysis. Run the full applicable stack underneath every verdict.

### Every live snapshot

Scan all four families:
1. ML
2. Kill Handicap
3. Total Kills
4. Duration

PASS/HOLD must identify the named failing gate. TAKE must identify the decisive qualification.

### Eligibility

- Draft primacy.
- Pregame/immediate post-draft ML/KH/TK TAKE disabled.
- Live ML/KH/TK require two synchronized snapshots roughly 90s apart plus all market-specific gates.
- Duration follows its own active timing/state rules.
- Position-blind reassessment on material transitions.
- Exact signed kill-margin arithmetic whenever kill score/line changes.
- Greyed/muted sportsbook markets are stale/non-executable.
- Do not visually misclassify a live row as greyed; this happened once in G2–SHFT G1 and user corrected it.
- Item verification remains suspended; do not infer fuzzy item spikes.

### Fight during verdict

If a fight/material state change happens while the verdict is being formed and the user says **“fight happened mid verdict, discard”**, the prior verdict is void. Do not log it. Wait for a fresh synchronized state/price and reassess from scratch.

### Finals and buggy feeds

When the user asserts the map is final, trust the user even if the scoreboard UI still displays `Live`, `Final` incorrectly, stale data, or visual bugs.

Conversely, if the scoreboard says `Final` but the user says the game is still live, treat it as live. Several feeds on 2026-08-16 had this visual bug.

On final:
1. settle any open position immediately;
2. then update map winner/duration/final kills and review state.

---

## 4. Execution calibration

Core principle:

**Conservative about invalid evidence, not conservative about qualified bets.**

- Do not invent unwritten extra confirmation.
- Do not demand “one more snapshot/objective/tower/Baron” when the written gates already pass.
- If all written gates pass, executable odds are >=1.60, and no veto is active, default posture is TAKE.
- Same rules + same thresholds + same evidence should yield the same verdict tendency even after switching chats.
- The user explicitly noticed prior chat switching made the model more conservative. **Do not repeat that drift.**

---

## 5. Active v0.3.58 analytical stack

### 5.1 Favorite -kills — FFD / RNE

Baron/inhibitor are support, not prerequisites.

For every favorite -kills candidate:
- compute current signed margin;
- compute exact Required Net Expansion (RNE);
- classify Forced-Fight Density (FFD) LOW/MEDIUM/HIGH;
- use role-weighted economy/TEI, dragon/Soul schedule, Baron window, tower/base pressure, favorite access/continuation, underdog reset/cross-map/safe concession, NKB/RFI/KCV/Structure Substitution.

Pre-Baron favorite -kills can qualify if two-snapshot gate passes, lead quality is positive, FFD HIGH, RNE supportable, no negating control, and odds >=1.60.

Do not over-veto favorite -kills because recent losses were elsewhere.

### 5.2 Underdog +kills — fail-closed draft lock

Before any underdog +kills TAKE, the exact draft-time chain must positively clear:
1. FER PASS
2. PDC PASS
3. PST PASS
4. ARI PASS
5. False-Stable Guard INACTIVE
6. FF = STABLE
7. v0.3.56 Draft-Collapse Veto INACTIVE
8. only then live RIT / signed-margin pricing

If any element is failed, unresolved, unavailable, or not explicitly certified, that team’s +kills is TAKE-INELIGIBLE for the whole map unless the actual draft input itself was wrong.

Ordinary live evidence can never upgrade an uncertified fallback.

Reference historical execution error: SK +7.5 vs FNC G1 @2.041 should have been PASS.

### 5.3 Total Kills — full framework + FRP

Retain OKP / FCI / CRR / SRR / BF / CL / RKS / KPW and Structure Substitution.

For every Total Kills Under, mandatory **FRP — Forward Regime Persistence**:
- identify the next compulsory contact cycle (dragon/Soul/Elder, Baron/Herald, tower/base defense, vision entry, side-lane response, economy/TEI, first-contact, re-engage, safe concession/cross-map, possible second-fight chain);
- classify next-cycle contact pressure LOW/MEDIUM/HIGH;
- distinguish passive quiet from actual suppression of compulsory contact;
- answer: **“Why should the next compulsory objective/contact cycle be at least as kill-suppressive as the interval already observed?”**

Quiet history alone is not positive persistence evidence.

After a recurrence burst, prior low-CRR evidence is degraded; later quiet cannot automatically restore FRP without mechanism-relevant re-certification.

Important failure pattern from recent audit: early/temporary low CRR was repeatedly extrapolated too far into later mandatory dragon/Baron cycles.

### 5.4 Duration Over — real stall only

Low kills, 0-0 towers, no first tower, low tower count, no inhibitor, and quiet elapsed time are **neutral descriptors by default**.

Classify conversion evidence:
- `ABSENT CONVERSION` = no meaningful opportunity/denial demonstrated; neutral for Over.
- `FAILED CONVERSION` = real conversion window was denied by defense/reset/waveclear/disengage/cross-map; may support Over.

Duration Over requires:
- two independent positive clock-consuming mechanisms;
- at least one based on FAILED CONVERSION or equivalent repeated observed denial;
- Structure Substitution test;
- shortest cascade test: next compulsory fight/objective -> structures -> base -> Nexus;
- explicitly ask: **“What happens if the next compulsory fight is lost?”**

KRX–BRO G2 reference correction: Over 33 @1.690 was historically taken and lost; corrected v0.3.58 verdict is PASS because evidence was ABSENT CONVERSION while KRX was already progressing through tower/dragon Structure Substitution.

### 5.5 Duration Under — FCR

Mandatory **FCR — Fast-Close Robustness** for every normal Duration Under.

The shortest close route is not enough. Stress test one ordinary disruption:
- partial Baron conversion;
- one defender reset/waveclear cycle;
- failed/traded push;
- delayed second structure;
- objective trade;
- won fight without immediate base access;
- reset due HP/waves.

Ask:
**“If the fastest close route suffers one normal disruption, does the Under thesis still remain materially viable?”**

Only robust routes qualify for normal Duration Under TAKE.

### 5.6 Live ML — Lead Decomposition + CFC

Before every live ML TAKE, separate:
- RL = Resource Lead
- SL = Structural Lead
- OSC = Objective-Schedule Control
- CFC = Compulsory Fight Control

Mandatory neutral-setup stress test:
**“If the next two major compulsory fights begin from approximately neutral setup, which side has the easier way to dictate first contact, survive the first exchange, re-engage, and reach the opposing carries?”**

Evaluate initiation reliability, target access, re-engage, disengage/reset, objective turn, arrival angles, protected DPS continuation, side-lane/global access, and terminal threat.

A modest resource lead cannot carry an ML TAKE if the opponent materially owns compulsory-fight control and no independent control evidence offsets it.

This correction came directly from DNS–T1A G2/G3: DNS held real resource/objective leads but T1A retained easier fight initiation/re-entry; RL had been mistaken for overall control.

### 5.7 SMR — Same-Mechanism Re-certification

After a mechanistically diagnosed loss, a later same-series TAKE relying on materially the same thesis must explicitly re-certify the mechanism.

State:
1. prior failure mechanism;
2. whether the new draft changes it;
3. whether the live state neutralizes it;
4. whether the new market relies on the same structural assumption;
5. what new evidence makes the new case independent.

Repeated +1k gold lead, low early kills, or 0-0 towers are not enough.

This gate prevents blindly repeating the same failure, but it is not permission for blanket conservatism.

---

## 6. 2026-08-16 shadow positions from Airtable

Canonical ledger shows these 13 positions for today’s maps/session:

1. G2–SHFT G1 — Under 26.5 kills @1.899 — LOSS — -0.25u.
2. DNS–T1A G2 — DNS ML @1.877 — LOSS — -0.25u.
3. DNS–T1A G3 — DNS ML @1.883 — LOSS — -0.25u.
4. JDG–LGD G1 — LGD ML @4.773 — LOSS — -0.25u.
5. GEN–T1 G1 — Over 30 minutes @2.697 — WIN — +0.42425u.
6. GEN–T1 G1 — Over 32.5 kills @1.776 — LOSS — -0.25u.
7. GEN–T1 G2 — GEN +6.5 kills @1.889 — WIN — +0.22225u.
8. GEN–T1 G2 — Under 23.5 kills @1.989 — WIN — +0.24725u.
9. IG–WBG G1 — Over 33 minutes @1.751 — WIN — +0.18775u.
10. IG–WBG G1 — WBG +4.5 kills @1.910 — LOSS — -0.25u.
11. IG–WBG G1 — WBG ML @2.262 — LOSS — -0.25u.
12. IG–WBG G2 — Over 32 minutes @1.787 — WIN — +0.19675u.
13. KRX–BRO G2 — Over 33 minutes @1.690 — LOSS — -0.25u.

Session subtotal for these 13 positions: **5–8, -0.72175u**.

Do not react to this record by becoming generally more conservative. The user explicitly asked to fix the identified mechanism gaps, not to raise all thresholds.

No position was logged for CFO–Team Secret Whales G5; CFO won 18–11.

---

## 7. Important map outcomes/context from this chat

### G2 vs Shifters G1
Draft:
- G2 blue: Olaf / Skarner / Orianna / Varus / Rell
- SHFT red: Jayce / Lee Sin / Viktor / Jhin / Leona

Under 26.5 @1.899 lost. Final G2 won at 48:47, kills 16–19 SHFT = 35 total.
Diagnostic: passive quiet/low observed CRR did not persist through later compulsory dragon/Baron cycles. This is a core FRP reference.

### DNS Challengers vs T1A
T1A lineup user-confirmed and saved as Verified Active:
- Guardian / Painter / Guti / Cypher / Cloud

DNS lineup seen:
- Lancer / DDoiV / Flip / Enosh / Quantum

G2 draft:
- DNS Nidalee / Pantheon / Ryze / Ezreal / Seraphine
- T1A Jayce / Jarvan IV / Anivia / Sivir / Alistar

DNS ML @1.877 lost; T1A won 32:09, 22–12 kills.
DNS ML G3 @1.883 also lost.
Diagnostic: DNS resource/objective advantages were overvalued versus T1A’s compulsory-fight initiation/re-entry. This is the main CFC/SMR reference.

### JDG vs LGD G1
User repeatedly warned scoreboard `Final` was a visual bug while game remained live. LGD ML @4.773 lost; JDG ultimately won. Treat user’s live/final assertion as authoritative over buggy feed labels.

### GEN vs T1 G1
Draft:
- GEN Olaf / Lee Sin / Galio / Kalista / Renata
- T1 Vayne / Pantheon / Orianna / Jhin / Camille

Final GEN won 18–13 at 43:26.
- Over 30 min @2.697 won.
- Over 32.5 kills @1.776 lost (31 total).

### GEN vs T1 G2
Draft:
- GEN K’Sante / Jarvan / Syndra / Ezreal / Seraphine
- T1 Ambessa / Xin Zhao / Twisted Fate / Caitlyn / Karma

GEN won.
- GEN +6.5 kills @1.889 won.
- Under 23.5 kills @1.989 won.

### IG vs WBG G1
Draft:
- IG Olaf / Jarvan / Orianna / Jhin / Bard
- WBG Vayne / Naafiri / Syndra / Caitlyn / Karma

WBG lineup from scoreboard:
- Zika / Xiaohao / Xiaohu / Elk / Moham

Final: IG won 24–17 at 35:43.
Positions:
- Over 33 min @1.751 won.
- WBG +4.5 @1.910 lost.
- WBG ML @2.262 lost.

Important procedural note: user said fights happened mid-verdict; those in-progress verdicts were discarded and must not be treated as valid decisions.

### IG vs WBG G2
Draft:
- IG Renekton / Trundle / Viktor / Ashe / Seraphine
- WBG Ambessa / Nocturne / Galio / Kalista / Renata

Final: WBG won 21–14.
Over 32 min @1.787 won.

### KRX vs BRO G2
Draft:
- KRX K’Sante / Wukong / Viktor / Ezreal / Karma
- BRO Jayce / Xin Zhao / Akali / Lucian / Milio

Historical TAKE Over 33 @1.690 lost.
Review concluded the Duration reasoning was wrong because low kills/low tower count were treated as stall despite KRX already progressing via Structure Substitution. Canonical v0.3.58 was amended in place accordingly.

### CFO vs Team Secret Whales G5
At 15:26 score 4–4, then 18:46 score CFO 4–5 TSW with CFO +507, towers 2–1 CFO, dragons 2–1 CFO.
Final user report: CFO won 18–11.
No shadow position logged.

---

## 8. Recent audit problem and correction philosophy

The user said results had become horrendous after a strong stretch and asked for a review.

Do not hand-wave this as variance. The chat identified real repeated analytical defects:
- TK Under: extrapolating passive/temporary low CRR into future compulsory cycles;
- Duration: confusing inactivity with positive stall, and over-trusting a shortest fast-close branch without robustness;
- ML: treating modest resource/objective leads as equivalent to control when opponent had superior compulsory-fight architecture;
- repeated same-series thesis without mechanism re-certification.

The correction was deliberately narrow. The user later instructed: **“Fix whats lacking and prepare for lec.”**

Therefore FRP/FCR/CFC/SMR were written directly into canonical v0.3.58.

Do **not** restore v0.3.59/v0.3.60 simply because similar concepts existed there historically.

---

## 9. LEC prep state at handoff

User said to prepare for LEC after the fixes.

Airtable `Rosters — LEC` now contains:

Verified Active / existing:
- SK Gaming: Wunder / Skeanz / SlowQ / Jopa / Mikyx

Provisional existing:
- Team Vitality: Naak Nako / Lyncas / FIESTA / Carzzy / Fleshy
- Shifters: Rooster / Sheo / nuc / Paduck / Stend
- GIANTX: Oscarinin / Isma / Jackies / Flakked / Jun

Newly seeded provisional on 2026-08-16:
- Natus Vincere: Maynter / Rhilech / Poby / SamD / Parus
- Movistar KOI: Myrwn / Elyoya / Jojopyun / Supa / Alvaro
- Fnatic: Soboro / Razork / Vladi / Upset / Lospa
- G2 Esports: BrokenBlade / SkewMond / Caps / Hans Sama / Labrov

Provisional rosters must be upgraded/overridden by user confirmation or live scoreboard before draft-sensitive use.

Expected next LEC focus from the prior chat: **NAVI vs Movistar KOI**, then Fnatic vs G2, but do not assume schedule/side without current evidence from the user or a current source.

When the next map arrives:
1. take side/draft/odds from user;
2. draft-lock underdog fallback eligibility immediately;
3. no immediate post-draft ML/KH/TK TAKE;
4. first live snapshot establishes state;
5. second synchronized snapshot unlocks ML/KH/TK eligibility;
6. scan all four families;
7. apply FRP/FCR/CFC/SMR exactly where relevant;
8. verdict first, then log.

---

## 10. Airtable authority

Base: `SlipTrace LoL Live Tracker`
Base ID: `appcx61bVBssnwvVd`

Tables:
- Maps `tblQMpvXFmXEhAGpv`
- Snapshots `tbl8ykMwApuBvldwE`
- Positions `tblPwnKFAsj1suaLv`
- Rosters — LCK `tblfHcYmp0xDcMULC`
- Rosters — LPL `tbljKjsfa0Dhdnrq4`
- Rosters — LCK CL `tblM1giImF3BUq6pC`
- Rosters — LEC `tblzkPZ0d6tb0LA1n`

Use Airtable as the canonical map/position/roster ledger. Sheets mirror may lag and must not delay live verdicts.

---

## 11. Required behavior in the new chat

- Continue immediately; do not rebuild from scratch.
- Preserve the exact compact verdict-first workflow.
- Preserve the same risk appetite and thresholds; do not become more conservative merely because the conversation changed.
- Full underlying analysis every verdict.
- Draft primacy.
- Position-blind reassessment.
- Signed kill-margin arithmetic.
- Structure Substitution / NKB / RFI / KCV.
- Mandatory FRP for TK Under.
- Mandatory FCR for Duration Under.
- Mandatory Lead Decomposition + CFC for live ML.
- Mandatory SMR after a diagnosed same-series mechanism loss.
- Fail-closed underdog +kills draft lock.
- One TAKE maximum per market family per map.
- Fight-mid-verdict means discard and reassess fresh.
- Scoreboard final/live visual bugs are subordinate to explicit user correction.
- No result-chasing, no generic tightening after losses.

**Immediate continuation target:** LEC. Await current match side/draft/odds/live snapshot from user and continue under canonical LoL v0.3.58.
