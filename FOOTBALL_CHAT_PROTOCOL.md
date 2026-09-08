# SlipTrace Football Chat Operating Protocol

**Status:** ACTIVE  
**Authoritative model entry point:** `models/football/CURRENT_MODEL.md`

Purpose: enforce the same current football state across ChatGPT chats without reconstructing rules or boards from memory.

---

## 1. Authority order

For current football work:

1. **GitHub `acchtt/SlipTrace`** — model rules, procedures, and durable operating policy.
2. **Frozen Work PRE artifact persisted to Airtable Daily Coverage Ledger** — current slate/board bridge.
3. **Airtable Decision States** — later material XI/market/live assessments.
4. **User-supplied current screenshots/text** — XI, odds, and live market evidence when supplied.

Always load `models/football/CURRENT_MODEL.md` first. Do not select an old model version from memory or an old chat handoff.

If a current Airtable coverage row demonstrably conflicts with the original frozen Work board, treat it as a persistence synchronization fault and preserve the original frozen Work PRE until corrected.

---

## 2. Current model routing

- **Official:** Football v0.2.49
- **Base:** v0.2.47 CLEAN
- **Shadow:** v0.2.47 CLEAN
- **Shadow:** v0.2.48-SHADOW

For comparable official grades:

`TWO-SIDED > ELITE CARRIER > CARRIER-LED > FRAGILE / OTHER`

Do not apply the v0.2.49 priority patch to the shadow models.

---

## 3. Fixture coverage rule

Fixture discovery is **AiScore only**.

Do not use a multi-source fixture union. Other providers may support match research only after AiScore establishes the fixture.

For any ICT window that crosses midnight, explicitly traverse every AiScore date listing touched by the window and verify the terminal cutoff block before claiming completeness.

If traversal is incomplete:

`COVERAGE INCOMPLETE — AiScore sweep incomplete`

---

## 4. Current actionable competition overlay

Exclude from the normal actionable board:

- youth/Uxx (U17/U18/U19/U20/U21/U23);
- academy/junior;
- reserve/B-team/development;
- amateur/semi-pro;
- regional/state/provincial;
- very small/obscure weak-data leagues;
- domestic lower divisions below top flight unless explicitly approved/whitelisted.

Do not weaken the overlay to fill the slate.

Do not inherit old generic continental/cup exclusions. Senior first-team competitions such as UEFA Champions League, UEFA Europa League and UEFA Conference League are actionable when otherwise eligible.

---

## 5. Current production workflow

`AiScore universe → quality filter → Work price/XI-blind structural screen → frozen FOCUS/WATCHLIST board → Airtable publish → user supplies XI + odds → Normal Chat final rerank → official v0.2.49 LOCK/HOLD/PASS`

Work publication to Airtable is a state copy/upsert, **not a second structural model run**.

---

## 6. User-supplied XI + odds policy

Normal Chat does not automatically fetch confirmed XI or bookmaker odds.

- user supplies XI + odds;
- only search externally when the user explicitly asks for verification;
- no OFFICIAL LOCK without required current XI + executable price;
- if missing, state `WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`.

Current executable price policy:

- hard floor 1.65;
- preferred 1.70+;
- never stretch the total merely to improve price.

---

## 7. Pre-verdict discipline

Before a material verdict:

- resolve the fixture against frozen PRE;
- verify official model version;
- review team GF/GA/profile and chance-quality support as required by the active rules;
- rerank from confirmed XI;
- identify the main failure mode;
- choose goal burden before price;
- apply current price policy;
- log the material assessment under the model version that produced it.

Price cannot rescue weaker structure.

---

## 8. Record separation

- **Daily Coverage Ledger:** complete-slate coverage + frozen PRE bridge.
- **Decision States:** later material XI/market/live assessment epochs and official/shadow evidence.
- **Official picks/ledger path:** actual official LOCK exposure and settlement according to the current repository contract.
- **GitHub:** current model and durable procedures.

Do not rewrite frozen PRE with a later assessment.

---

## 9. Live and settlement boundary

Live evidence validates or invalidates the frozen thesis; it does not rewrite prematch history.

Shadow/counterfactual/HOLD selections never enter official P/L.

Standard full-match Asian totals settle on 90 minutes + stoppage time unless the market explicitly includes extra time.

---

## 10. Cross-chat non-negotiable

When connected sources can be queried, do not reconstruct authoritative football state from conversational memory.

Load the current repo, read the persisted frozen slate, then apply the user’s current evidence.
