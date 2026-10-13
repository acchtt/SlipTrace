# Historical source-acquisition procedure — retired

## Status

This document previously described the V1–V3 AiScore/Step0 acquisition,
checkpoint and work-ready handoff system.

It is **not current production authority**.

Current source acquisition is governed only by:

- models/football/CURRENT_MODEL.md
- models/football/stages_v4/SWEEP.md
- models/football/stages_v4/source_completeness.py
- models/football/stages_v4/stage.py

## Current rule

V4 acquires complete provider date/listing surfaces for the requested window,
reconciles pagination/block/fixture counts, performs the independent terminal
sentinel check, freezes the source-visible union, and only then applies
registry/filter/goal-history logic.

There is no active work_ready flag, Step0 ZIP, checkpoint resume contract,
capacity queue or Work-admission artifact.

If a historical V1–V3 record must be audited, use the historical Git revision
that actually produced that record. Do not load this retired procedure into a
new /sweep.
