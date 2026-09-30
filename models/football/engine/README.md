# Football C Deterministic Engine — Phase 1

This directory begins the migration from a prose-only football model toward a hybrid coded model.

## Why this exists

Football C still needs an LLM/research layer for tasks that are genuinely semantic:

- interpreting current team news;
- assigning route strength from current football evidence;
- deciding whether H2H is transferable;
- mapping XI changes to mechanisms;
- judging whether live attacking quality is still healthy.

But once those judgments are expressed as structured fields, deterministic rules should not be reinterpreted differently from run to run.

Phase 1 therefore codes:

- the Football C/C2 qualitative data contract;
- deterministic lexicographic ranking;
- C2 selection-quality floor;
- Football C price/burden execution;
- C2 Focus Market-Gap Bridge eligibility;
- WAIT reachability vs negative-information check;
- Asian-total settlement.

## What this does NOT do

It does not:

- manufacture probabilities;
- invent xG from text;
- replace research with arbitrary weights;
- train an ML model;
- automatically become production authority.

The current text model remains authoritative until the coded engine is validated.

## Architecture

```text
web / XI / H2H research
        ↓
LLM produces structured MatchAssessment
        ↓
engine/core.py
        ↓
deterministic rank / floor / execution / settlement
        ↓
audit comparison against text decision
```

## Ranking

The first coded ranking intentionally uses a lexicographic tuple matching the declared Football C/C2 priority rather than a weighted score:

1. route reliability
2. independent route quality
3. carrier strength
4. chance quality
5. failure resistance
6. XI robustness
7. evidence confidence
8. burden protection

This avoids pretending that an unvalidated coefficient such as "route = 35%" is meaningful.

## Next milestones

1. Feed real frozen board assessments into this schema.
2. Compare coded output with the text-model decision on several boards.
3. Measure disagreement causes.
4. Only then decide whether to add numerical football features (xG, big chances, box entries, SOT quality, opponent xGA, etc.).
5. Train statistical probability models only after we have enough clean historical feature rows.
