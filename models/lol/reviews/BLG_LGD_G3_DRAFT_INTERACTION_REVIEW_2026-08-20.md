# BLG vs LGD Game 3 — Draft Interaction Review — 2026-08-20

**Series:** LPL 2026-08-20 LGD vs BLG, Game 3  
**Historical shadow position:** LGD +12.5 kills @2.060, 0.25u shadow, 0u actual  
**Final kills:** BLG 18-2 LGD  
**Model namespace:** LoL v0.3.58

## Review question

Was the loss merely ordinary variance under a sound draft certification, or did the draft read materially misclassify the interaction and therefore create a false `UDKC = STABLE`?

## Draft

BLG:
- Jayce
- Pantheon
- Syndra
- Corki
- Nami

LGD:
- Yorick
- Maokai
- LeBlanc
- Kalista
- Renata

## Original classification

The original live process treated:

- BLG as only a slight draft favorite;
- Maokai + Renata as meaningful generic anti-cascade tools;
- Yorick as an independent side-lane suppression route;
- BLG's lack of traditional frontline as a meaningful draft weakness;
- LGD UDKC as `STABLE`, which later allowed LGD +12.5 kills to reach UCS and qualify.

## Mechanism-level diagnosis

### 1. BLG did not need sustained front-to-back

BLG's primary interaction was not tank-frontline into protected DPS.

The repeatable sequence was:

`Jayce/Corki/Syndra ranged pressure -> Nami setup/zone support -> target chunk or isolation -> Pantheon follow-up -> objective/space control -> repeat`

This composition can win the fight before a conventional frontline engagement begins. Treating limited frontline as a large weakness overstated LGD's ability to stabilize.

### 2. LGD's defensive tools did not directly match the primary threat

Maokai and Renata are meaningful against committed access, dive and cleanup. They are not automatically strong answers to pre-contact poke, ranged zone control and isolated pick pressure.

The original read committed a **threat-answer mismatch**: useful defensive champions were counted as generic kill-margin suppression without proving that they actually interrupted BLG's main kill-production sequence.

### 3. Yorick was not automatically an independent suppression route

A side-lane champion only supplies independent fallback if the split cannot be cheaply neutralized and if the remaining four-man unit can survive the opponent's control geometry.

Against Jayce pressure, Pantheon global response, BLG ranged setup and pick threat, LGD's Yorick route was conditional rather than reliably independent. It should not have been credited as sufficient ARI/KMS evidence by itself.

### 4. Objective setup geometry favored BLG more than the original read acknowledged

Jayce, Corki, Syndra and Nami create strong pre-contact control. Pantheon adds global/semi-global collapse pressure. LGD's four-man group had to navigate range and pick threat to contest space, which increased repeated-margin expansion risk after BLG gained control.

### 5. Team-strength prior amplified a mechanically coherent draft

BLG's materially stronger team execution prior did not create the draft edge by itself, but it increased confidence in a composition whose repeatable setup was already mechanically favorable.

## Correct classification

A clean draft-only interaction pass should have produced:

- **Draft Edge: CLEAR/STRONG BLG**
- LGD `TAM`: FAIL/UNRESOLVED against BLG primary kill route
- LGD side-lane independence: conditional, not sufficient proof
- LGD collapse suppression: FAIL/UNRESOLVED
- LGD KMS: FAIL/UNRESOLVED
- LGD UDKC: **FRAGILE**, not STABLE
- LGD +kills: **draft-locked out for the map**

Therefore the historical LGD +12.5 TAKE should be treated in audit as a **draft-certification error candidate**, not simply used as evidence that large cushions are unsafe. The arithmetic/UCS layer was downstream of an incorrectly generous UDKC classification.

Historical result and P/L must remain unchanged.

## Corrective action

Create and require:

`models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`

The procedure adds mandatory:

- exact role resolution;
- primary/secondary kill-mechanism mapping;
- Threat-Answer Matching;
- objective-setup geometry;
- damage access/uptime;
- side-lane independence testing;
- conditional frontline-necessity analysis;
- collapse-asymmetry stress;
- team-strength execution modifier;
- adversarial favorite second pass;
- separate Draft Edge and UDKC Stability outputs.

This is an in-place v0.3.58 correction. It does not create v0.3.59/v0.3.60.

## Activation governance

The active 2026-08-20 slate is frozen by Session Authority Lock. This review/procedure is committed after that lock and is therefore `PENDING_NEXT_SLATE` unless the user explicitly authorizes an immediate relock. A historical outcome alone does not silently mutate the active lock.
