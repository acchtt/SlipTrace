# MODEL RULES — LEAGUE OF LEGENDS v0.3.52

**Status:** Active delta  
**Effective date:** 2026-08-10 22:47 UTC+7  
**Supersedes:** v0.3.51 only where stated

## Purpose

Correct the SK Gaming vs Team Vitality Game 1 live-moneyline error under v0.3.51.

Confirmed position:

- SK ML @1.752 — LOSS (-0.25u)

Entry at 12:50: SK 5-2 VIT, SK +1.6k gold, towers 0-0, VIT 1-0 dragons, Grubs SK 2-1.  
Final user-authoritative result: VIT won; latest synchronized grading frame VIT 23-14 SK at 32:50.

Review: `models/lol/reviews/SK_VIT_G1_TERMINAL_THREAT_ANSWERABILITY_REVIEW_2026-08-10.md`.

The central correction is:

> **A real early lead is not automatically a high-quality closing lead. Before upgrading live ML, the model must prove that the leader can answer the opponent's strongest terminal 20-25+ minute threat or close the map before that threat becomes decisive.**

v0.3.51 Total Kills recurrence logic, v0.3.50 contact-realization logic, v0.3.48 Kill Handicap conversion controls, v0.3.47 Draft Primacy, v0.3.45 Duration, v0.3.44 signed-margin symmetry and all execution controls remain active unless superseded below.

---

## 1. Terminal Threat Answerability (TTA) Is Mandatory for ML

After draft lock and before every post-draft/live Moneyline TAKE, identify each team's strongest **terminal threat**: the matchup mechanism that becomes disproportionately difficult to answer if the game reaches a stable 20-25+ minute state.

Terminal threats may include:

- scaling control mage / zone-control carry;
- protected sustained-damage carry;
- long-range siege shell;
- split-push side-lane win condition;
- front-to-back hypercarry;
- repeatable pick engine with superior vision control;
- objective setup that becomes progressively harder to enter.

Do not credit a terminal threat merely from champion identity. It must be matchup-functional against the opponent's actual draft.

For the current leader, classify answerability:

- `ROBUST` — leader has multiple repeatable, opponent-tested ways to neutralize, bypass, outrange, isolate or close before the threat dominates;
- `CONDITIONAL` — answer exists but depends on flank, narrow engage angle, first-spell success, specific side-map setup, or significant execution burden;
- `UNANSWERED` — no reliable repeatable solution is visible if the game reaches the threat's preferred state.

TTA must be recorded internally before a live ML TAKE.

---

## 2. TTA Answerability Test

For each terminal threat ask:

1. **Access:** Can the leader reliably reach the threat through the opponent's peel/zone/frontline?
2. **Lockdown:** Once reached, can the leader keep the threat controlled long enough to kill or force it out?
3. **Range / zone parity:** Can the leader contest prepared objective terrain without walking through losing space?
4. **Side-map bypass:** Can the leader win through split pressure, globals or map dislocation so the terminal threat cannot simply set standard 5v5s?
5. **Threat suppression:** Is the terminal threat materially behind in role gold / farm / map access and staying suppressed?
6. **Close-before-maturity:** Is there demonstrated structural acceleration likely to end or break the map before the terminal threat reaches its preferred state?
7. **Fallback after first engage:** If the leader's first initiation fails, can it disengage, reset or re-engage without immediately losing the fight?

Champion-counting is prohibited. Every credited answer must survive opponent-counter testing.

---

## 3. Execution Burden Gradient (EBG)

Execution simplicity is no longer treated as static.

Classify how relative execution burden changes with time:

- `FAVORABLE` — leader's win condition becomes easier or remains simpler as the game progresses;
- `NEUTRAL` — no meaningful time-driven shift;
- `ADVERSE` — leader's initiation/positioning becomes increasingly difficult while the trailer's standard fight or objective setup becomes easier.

Examples of ADVERSE EBG:

- leader requires flank/angle-based engage into growing zone control;
- trailer's scaling control carry can front-to-back from protected terrain;
- leader has one-shot initiation but weak fallback if the first engage fails;
- trailer gains superior range/peel/choke control over time.

For live ML, an `UNANSWERED` or weakly `CONDITIONAL` TTA plus `ADVERSE` EBG materially increases comeback probability even when the early leader is ahead in kills and gold.

---

## 4. Lead Quality: Terminal vs Non-Terminal

Every material live lead must be classified as either:

### `TERMINAL / CLOSING LEAD`
The lead is already translating into a credible close path through several of:

- meaningful tower advantage / base access;
- dragon/soul-point leverage;
- Herald-to-tower or other structural acceleration;
- Baron control / inhibitor pressure;
- repeated successful access onto the opponent's terminal threat;
- role-level suppression of the terminal threat that is persistent rather than cosmetic;
- map state that removes the trailer's ability to set its preferred fights.

### `NON-TERMINAL LEAD`
The leader is ahead in kills/gold but the map remains structurally reversible.

Reference early-live warning pattern before 15:00:

- lead below roughly +2.5k;
- no tower advantage;
- no major objective acceleration toward a close;
- opponent terminal threat remains economically functional;
- standard 5v5 setup is becoming easier for the trailer.

The reference numbers are not standalone rules; the mechanism classification controls.

**Kills + distributed gold alone do not make a lead terminal.**

---

## 5. Hard Early-Live ML Veto — Unanswered Terminal Threat

Before 15:00, do **not** TAKE the current leader's ML when all are true:

1. leader's TTA is `UNANSWERED` or strongly `CONDITIONAL`;
2. EBG is `ADVERSE`;
3. current lead is `NON-TERMINAL`;
4. no repeated live evidence shows reliable access onto or suppression of the terminal threat.

Verdict defaults **HOLD/PASS** until at least one condition materially changes.

This veto applies even if:

- current kills favor the leader;
- gold lead is distributed across several roles;
- the leader's early draft functions are visibly working;
- market odds appear attractive relative to a scoreboard-only reprice.

This rule directly blocks the SK ML @1.752 error at 12:50.

---

## 6. Live ML Probability Buffer

Live Moneyline now has explicit lower-bound edge requirements over break-even:

- **early live (<15:00): +5pp**;
- **mid live (15:00-24:59): +4pp**;
- **late live (25:00+): +3pp**.

If TTA is `CONDITIONAL` with ADVERSE EBG, add **+2pp** to the relevant live ML requirement.

If TTA is `UNANSWERED` with ADVERSE EBG, add **+4pp**.

Total live-ML surcharge is capped at **+9pp over break-even**.

The hard veto in Section 5 controls when applicable; probability surcharge cannot rescue a vetoed early leader ML.

---

## 7. Comeback Conversion Reserve (CCR)

For every live ML decision where the trailer retains a meaningful terminal threat, explicitly inventory a **Comeback Conversion Reserve** branch.

The branch must answer:

- What happens if the leader fails to convert the next 1-2 objective/structure windows?
- Can the trailer reach a standard 5v5 or side-map state that is easier for its composition?
- Can one failed leader engage flip dragon/Baron and immediately create structural control?
- Does the trailer's terminal threat improve the lethality or reliability of that first comeback fight?
- Does the leader have a safe reset/fallback if the first engage fails?

Do not use one deterministic central line. Maintain at least:

- clean-close branch;
- stalled-but-ahead branch;
- terminal-threat stabilization branch;
- one-fight reversal branch.

If the last two branches are materially live, widen ML uncertainty and lower the leader's probability range.

---

## 8. Reassessment Triggers for TTA / EBG

Re-run TTA and EBG after:

- first tower or material tower swing;
- dragon/soul-point alignment change;
- Herald-to-tower acceleration;
- first Baron;
- >=2k meaningful gold swing;
- >=2 net-kill swing;
- material role-level suppression or recovery of the terminal threat;
- repeated successful access onto the terminal threat;
- repeated failed attempts to reach the terminal threat;
- clock entering ~20:00 and ~25:00 even without a large scoreboard swing;
- transition from skirmish-heavy play to organized objective setups.

TTA may improve or deteriorate independent of raw gold.

---

## 9. Draft Primacy Addendum

The existing 14-part Draft Function Matrix remains unchanged.

After the matrix, add a mandatory **Terminal Threat Overlay**:

1. strongest 20-25+ minute threat for each side;
2. opponent answerability class ROBUST / CONDITIONAL / UNANSWERED;
3. EBG FAVORABLE / NEUTRAL / ADVERSE;
4. which team benefits if the map slows into standard objective setups;
5. whether the current leader must close early or can safely scale alongside.

Draft Primacy therefore evaluates both **current-state conversion** and **future-state answerability**.

---

## 10. Kill Handicap Interaction

An unanswered terminal threat is both a map-saving and margin-saving mechanism until disproven.

For favorite negative kill handicaps:

- compress wide favorite-win margin tails when the underdog's terminal threat remains functional;
- raise Structure Substitution / stalled-close branches;
- require stronger KCV evidence before -kills expansion if the favorite's access worsens with time.

For underdog +kills:

- terminal-threat survival can increase P(cover | map loss) and P(outright comeback);
- do not confuse this with guaranteed low Total Kills.

Kill Handicap still uses signed-margin distribution, NKB, RFI, KCV and Structure Substitution from v0.3.48.

---

## 11. Total Kills Interaction

TTA does not directly imply Over or Under.

- An unanswered control threat can lower CRR by forcing concessions;
- it can also raise CL and SRR once the opponent is forced to engage through controlled terrain;
- if both sides retain independent forcing, v0.3.51 BF/SRR rules still control.

Do not reuse an ML terminal-threat thesis as a Total Kills edge without separate OKP / FCI / CRR / SRR / CL analysis.

---

## 12. SK vs VIT G1 Calibration

Draft:

SK: Gnar / Jarvan IV / Ryze / Varus / Shen  
VIT: Rumble / Pantheon / Viktor / Corki / Bard

At 12:50:

- SK 5-2;
- SK +1.6k;
- towers 0-0;
- VIT 1-0 dragons;
- Grubs SK 2-1.

Old v0.3.51 read:

- SK early forcing functioning;
- distributed economic lead;
- map win ~67-72%;
- SK ML @1.752 TAKE.

Correct v0.3.52 read:

- early forcing: functioning;
- lead quality: **NON-TERMINAL**;
- VIT terminal threat: Viktor-centered scaling/control shell;
- SK TTA: **UNANSWERED / highly CONDITIONAL**;
- EBG: **ADVERSE** for SK;
- no tower lead / no demonstrated close path;
- hard early-live ML veto: **ACTIVE**;
- verdict: **HOLD/PASS**.

---

## 13. Mandatory ML Internals — v0.3.52

Before every post-draft/live ML TAKE lock:

1. exact clock / odds / break-even;
2. current kills / gold / towers / dragons / Grubs-Herald / Baron / inhibitors;
3. verified draft-conditioned map prior;
4. Draft Function Matrix;
5. current conversion mode for each team;
6. leader's lead quality TERMINAL/CLOSING or NON-TERMINAL;
7. opponent terminal threat(s);
8. TTA ROBUST / CONDITIONAL / UNANSWERED;
9. EBG FAVORABLE / NEUTRAL / ADVERSE;
10. comeback conversion reserve branches;
11. structural close path or lack thereof;
12. live ML phase buffer and any TTA surcharge;
13. lower-bound P(win) after all uncertainty adjustments;
14. Section 5 hard-veto status.

Missing TTA/EBG/lead-quality on a material live ML decision => widen uncertainty and PASS/HOLD.

---

## 14. Review Window

For the next **10 settled v0.3.52+ live ML positions**, record:

- entry clock;
- odds / break-even;
- kills / gold / structures / objectives;
- lead quality;
- terminal threat;
- TTA class;
- EBG class;
- comeback conversion reserve branches;
- final winner;
- whether the terminal threat became decisive;
- whether the leader demonstrated a real close path before entry;
- result / ROI.

Audit specifically for:

- scoreboard anchoring;
- overrating distributed gold without structural conversion;
- underpricing control-scaling threats;
- ignoring time-varying execution burden;
- treating functioning early engage as proof of late answerability;
- failing to reserve one-fight reversal probability.

---

## 15. Retained Controls

- v0.3.51 Total Kills uses OKP + FCI + CRR + SRR + CL.
- v0.3.51 pre-12:00 Under hard gate remains active.
- v0.3.50 Threat Deterrence / contest-concede-trade-delay remains active.
- v0.3.48 signed Kill Handicap conversion controls remain active.
- v0.3.47 Draft Primacy remains active with the v0.3.52 Terminal Threat Overlay.
- v0.3.45 Duration restrictions remain active.
- Minimum odds remain 1.60.
- Default shadow stake remains 0.25u; actual exposure remains 0u while official betting is paused.
- A recommendation is recorded only after explicit confirmation of the same executable line/price.
- No martingale, rescue, loss chasing or stake escalation.
- Missing decision-critical state => PASS/HOLD.

Where this delta conflicts with earlier live-ML interpretation, **v0.3.52 controls**.