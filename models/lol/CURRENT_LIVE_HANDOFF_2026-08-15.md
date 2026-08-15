# CURRENT LIVE HANDOFF — 2026-08-15

## Active model

**LoL v0.3.59 — FROZEN FOR CONTINUED SHADOW AUDIT**

GitHub is model/rules authority. Airtable is canonical map/position/roster ledger.

Official betting remains **paused**. Shadow TAKEs remain active.

### Active governance

Procedure:
`models/lol/procedures/LOL_SHADOW_AUDIT_CONTINUATION_2026-08-15.md`

- v0.3.59 is the active model under test.
- Qualified executable shadow TAKEs auto-record at 0.25u simulated stake; actual exposure remains 0u.
- Preserve v0.3.57 and v0.3.58 historical selections/P&L under their original versions.
- New selections are recorded under v0.3.59.
- Do **not** create v0.3.60 or patch v0.3.59 from an individual next result without explicit user authorization or a later batch-review decision.
- Do not state aggregate audit P/L casually; recalculate from Airtable when an aggregate is requested.

## CRITICAL live-response behavior

The user has explicitly complained that verdicts took too long. On every active-map screenshot:

**FIRST visible output must immediately be:**

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

For a final result, first visible output must immediately settle any open position, e.g.:

- `WIN — [selection] @[odds] — shadow P/L +Xu.`
- `LOSS — [selection] @[odds] — shadow P/L -Xu.`

**No GitHub/Airtable/connector/tool calls before the visible verdict or settlement.**

Shadow TAKEs auto-record after the visible verdict. No confirmation is required. Keep the initial live response compact and transactional.

## v0.3.59 — Duration 0-0 Tower Neutralization

Rules:
`models/lol/rules/MODEL_RULES_LOL_V0.3.59.md`

Reference review:
`models/lol/reviews/DURATION_0_0_TOWER_RECURRENCE_REVIEW_2026-08-15.md`

### Core correction

For Duration:

**0-0 towers / no first tower is NEUTRAL by default.**

It is a lagging state descriptor, not evidence that future conversion will remain slow.

Mandatory distinction:

- `ABSENT CONVERSION` — no meaningful structural conversion opportunity occurred or no evidence one was denied. Neutral for Over.
- `FAILED CONVERSION` — a real tempo/objective/push/fight opportunity existed and the defender demonstrably denied expected structure/base access. May support Over.

Only FAILED CONVERSION can satisfy the structure-related stall component of a Duration Over.

### Latent Conversion Hazard (LCH)

Before every Duration Over, classify LCH LOW / MEDIUM / HIGH using:

- dragon/Soul/Elder schedule;
- Baron/Herald timing;
- grubs/tower pressure where relevant;
- role-weighted economy / TEI;
- wave/side-lane/siege access;
- first-contact reliability;
- defender fallback, waveclear and reset quality;
- shortest realistic next-fight -> first tower -> serial structures -> base route.

If LCH is HIGH, Over is TAKE-ineligible unless a high-leverage conversion opportunity has already failed after LCH became high and two independent observed stall mechanisms still persist.

Mandatory pre-first-tower question:

**“What happens if the next compulsory fight is lost?”**

Do not infer an Under automatically from HIGH LCH; retained v0.3.45 Under acceleration gates still apply.

### Recurrence evidence

Audit of settled Duration Overs where 0-0 towers was explicitly part of the entry thesis:

- 8 positions
- record 3-5
- net -0.47575u

This confirmed a recurring execution problem rather than a single-map anomaly.

## v0.3.58 retained — Favorite -kills Forced-Fight Density

Baron ownership and inhibitor destruction are **not mandatory prerequisites** for favorite -kills.

Favorite -kills requires explicit:

- current signed kill margin;
- `RNE` — Required Net Expansion to cover;
- `FFD` — remaining Forced-Fight Density;
- role-weighted economy / TEI and lead quality;
- dragon/Soul/Baron/objective schedule;
- favorite access/continuation;
- underdog avoidance/reset/cross-map routes;
- NKB / RFI / KCV / Structure Substitution.

Pre-Baron favorite -kills can qualify when FFD is HIGH and RNE is realistically supportable. Absence of Baron/inhibitor cannot force a PASS by itself.

Do not infer HIGH FFD from a large lead or strong engage alone. Structure Substitution matters: a favorite can close the game while removing the fight windows needed to cover an extreme handicap.

## v0.3.57 / v0.3.56 retained — Underdog +kills

For underdog +kills, `FF = STABLE` requires matchup-relative certification through:

1. FER — Failed-Engage Reset Test
2. PDC — Protected-DPS Continuation Test
3. PST — Pressured Space Test
4. ARI — Alternative Route Independence

Separate:

- FRI — Forcing Route Independence
- SRI — Survival Route Independence

Multiple engage tools do **not** prove stable fallback. Forcing redundancy is not survival redundancy.

Mandatory order:

MKT + TEAM -> DER -> FRI -> SRI -> FER -> PDC -> PST -> ARI -> False-Stable Guard -> DCR -> FF -> hard veto -> RIT only if veto inactive -> signed-margin pricing.

Incomplete/ambiguous fallback certification => PASS/HOLD.

If DCR HIGH + FF FRAGILE/ABSENT + opponent easier repeat forcing + objective/base schedule can matter, underdog +kills remains TAKE-ineligible for the entire map. Ordinary live events cannot upgrade a draft-locked FRAGILE/ABSENT/UNCERTIFIED classification to STABLE; only correction of the original draft inputs can do that.

## Kill-handicap arithmetic discipline

Always use exact signed-margin arithmetic.

For underdog `+H`:

- current dog signed margin = dog kills - favorite kills;
- final cover condition = signed margin + H > 0 for half-lines;
- compute exactly how many **additional net kills** the favorite requires from the current state to beat the line.

Do not use vague “effective cushion” language without verifying the integer margin.

Example retained from NS +7.5 while BRO led 2-0: BRO only needed +6 additional net kills from that state to finish +8 and beat +7.5.

## Other retained live controls

- Pregame and immediate post-draft ML/KH/TK TAKEs are disabled.
- Live ML/KH/TK require two synchronized live snapshots plus all active gates.
- Draft primacy remains mandatory; lock draft classification before market attractiveness/live cushion.
- Position-blind reassessment on material state changes.
- Role-weighted economy / TEI mandatory when visible.
- Total Kills remains de-duplicated OKP / FCI / CRR / SRR / BF / CL / RKS / KPW framework.
- Live ML must account for terminal threat.
- Same-map add-ons require explicit independent qualification and correlation handling.
- Greyed/muted sportsbook rows are stale/non-executable; never TAKE them.
- Visual feeds sometimes incorrectly label live games as FINAL; defer to sportsbook/live context when obvious.
- Scoreboard gold-lead color can indicate the side; identify the team direction carefully.
- No rescue/martingale/loss chasing.

## Roster ledger behavior

The user wants team lineups stored in Airtable, sorted by league, so live analysis does not rely on stale web roster pages.

When a live scoreboard confirms starters, upgrade those players to current/Verified Active. User corrections override stale web data.

### Current important roster corrections

**LCK — DN SOOPers main lineup:**
- DuDu / Sharvel / Clozer / deokdam / Peter
- User explicitly confirmed Sharvel and Peter are now the **main lineup**, not temporary substitutes.
- Pyosik and Life should be retained only as prior/alternate players unless later live evidence changes this.

**LPL — LNG current lineup:**
- Sheer / Weiwei / Nia / 1xn / Missing

**LPL — EDG:**
- Zdz / Jiejie / Sinian / Leave / Parukia

**LPL — BLG top correction:**
- Flandre at top in the stored current context.

**LEC — SK:**
- SlowQ is SK mid.

## Recent reference audits retained from this chat

### T1 vs DK G1 — favorite handicap correction reference

At 20:27 T1 led 16-8, ~+5.4k, towers 3-1, dragons 3-0. Historical v0.3.57 PASSed T1 -15.5 @1.617 because no Baron/inhibitor. Final T1 30-11.

User explicitly authorized removing Baron/inhibitor as mandatory favorite-handicap prerequisites. This became v0.3.58 FFD/RNE. Historical v0.3.57 ledger/P&L was not changed.

### VIT vs GIANTX G3 — Duration recurrence reference

Historical v0.3.58 TAKE: Over 32 @1.675 at 17:53 with VIT 3-5 GX, ~GX +2.2k, 0-0 towers, VIT dragons 3-0.

Final: VIT 14-6 GX at 27:21. The loss helped identify recurring misuse of 0-0 towers as stall evidence and triggered the user-authorized v0.3.59 correction.

### HLE vs KT G3 — extreme favorite margin restraint

At 15:58 HLE led 11-4, ~+5.5k, towers 1-0, dragons 2-0. Model HOLDed HLE -16.5 @1.871 because RNE remained too large.

Final HLE 17-4 KT at 26:08. HLE won by +13, so -16.5 would have lost despite total structural domination. Positive reference for Structure Substitution / extreme-margin restraint.

Under 31.5 @1.607 would have won, but PASS was considered defensible. Under 26 min would have lost by eight seconds, another reminder not to overinfer terminal timing before visible conversion.

## Latest completed map — BNK FEARX vs DN SOOPers G1

Series: LCK 2026 Rounds 3-4 — BNK FEARX vs DN SOOPers.

### Draft

**BFX:**
- Clear — Kled
- Raptor — Pantheon
- VicLa — Syndra
- Taeyoon — Ezreal
- Kellin — Bard

**DNS:**
- DuDu — Olaf
- Sharvel — Lee Sin
- Clozer — Ryze
- deokdam — Sivir
- Peter — Karma

Immediate post-draft: HOLD BFX -5.5 @1.860, 0u. BFX had cleaner forcing, but DNS had credible survival/return damage through Olaf + Ryze + Sivir/Karma, so no draft hard veto against DNS +kills.

### Shadow entry

At **16:03**:

- BFX 4-1 DNS
- BFX ~+3.1k gold
- towers 1-0
- dragons 1-1

**TAKE — DNS +10.5 kills @1.877 — shadow 0.25u; actual 0u.**

Entry arithmetic: BFX led by +3 and therefore needed **+8 additional net kills** from that state to finish +11 and beat DNS +10.5.

Thesis: DNS’s Olaf + Ryze + Sivir/Karma fallback still passed; BFX had not established a forced-fight schedule supporting an 11+ final margin.

### Mid-map reassessment

At **22:23**:

- BFX 8-4 DNS
- BFX ~+4.6k
- towers 3-0 BFX
- dragons 2-1 DNS

Existing DNS +10.5 thesis was marked **Degraded but Active**. No add-on at DNS +10.5 @2.247 because BFX’s tower/gold conversion had improved, even though DNS retained dragon leverage and return-fight architecture.

### Final / settlement

**Final: DNS 20-10 BFX at 29:50.**

Structures/objectives:
- towers BFX 6-10 DNS
- dragons BFX 1-3 DNS
- Baron BFX 0-1 DNS
- inhibitors BFX 0-2 DNS

Open shadow position settled:

**WIN — DNS +10.5 kills @1.877 — +0.21925u.**

Airtable position:
`LCK-2026-08-15-BFX-DNS-G1-P01`

Audit interpretation: strong positive calibration case. BFX’s early tower/gold lead did not guarantee sustained kill-margin expansion; DNS’s certified fallback, dragon leverage and return-fight capacity eventually reversed the map completely. Do not patch the model from this win.

## Current series state / immediate next action

**BNK FEARX vs DN SOOPers: DNS leads series 1-0. Game 2 is next/live.**

Continue immediately from the next user-provided G2 draft/odds/live screenshot under **v0.3.59**.

Required behavior:
1. verdict first;
2. draft primacy;
3. two-snapshot gate for live ML/KH/TK;
4. exact signed-margin arithmetic;
5. v0.3.57 fallback certification for underdog +kills;
6. v0.3.58 FFD/RNE + Structure Substitution for favorite -kills;
7. v0.3.59 Duration 0-0 tower neutralization + LCH;
8. log after visible verdict;
9. continue audit without further patching unless explicitly authorized.

## User operating preferences

- Wants live verdicts immediately; no pre-verdict connector work.
- Sends screenshots without questions and expects immediate analysis.
- Shadow TAKEs auto-record without confirmation.
- Does not want bets forced simply because a team is favored or draft read is strong.
- Is especially sensitive to repeated false underdog-cushion / false-fallback calls.
- Wants exact draft reassessment when requested, not anchoring on earlier read.
- Wants roster corrections stored by league.
- Wants audit evidence preserved honestly, including lucky wins, bad passes and arithmetic corrections.
