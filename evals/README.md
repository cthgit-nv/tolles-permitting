# Evals: how we know whether to trust the desk

Two instruments.

1. **Gold questions** (`gold-questions.md`). Questions with a known answer, from counsel
   or from settled law. Rerun them after changing a skill, the model, or a large part of
   the library. Score each answer against the reference: Match, Partial, Miss, and note
   whether the agent cited the right cards and flagged the right uncertainty. A drop in
   score blocks the change.
2. **Calibration log** (`calibration-log.md`). Every substantive piece of advice or
   red-team finding the desk gives, with its confidence label, and later its outcome:
   counsel agreed, counsel corrected, agency accepted, agency rejected. Over months this
   shows, by topic, where the desk is reliable and where it is not.

## How to run the gold set

In a fresh Claude Code session in this repo: "Run the gold questions in
evals/gold-questions.md without reading the Reference answer sections. Answer each using
the desk skills, then score yourself against the references and append a dated row per
question to evals/results.md." Then read the misses yourself; self-scoring is a first
pass, not the verdict.

## Red-team canaries

Seeded defects the red team must find without being told:

| Canary | Document | Expected finding |
|---|---|---|
| Substation of about 60 acres shown on BLM land | Hazen BLM and Reclamation PPOD drafts (Aug 2026) | Blocking: contradicts facts (chip F7, F8) |
| Great Basin pipeline described as existing disturbance | Aug 14 risk memo (Background 5, Q3), any draft copying it | Serious: pipeline is yet to be built (fmdp F2) |
| Reclamation crossings described as part of the transmission project | Any Application 1 or 2 draft | Blocking: segmentation self-harm |
| Friends of the Earth v. Coleman cited as 1995 | H&H memo fn. 3 | Minor: citation year (verify in A-case-foe-coleman) |
| "counsel advises" or a Holland & Hart reference in an outward draft | Synthetic test file | Blocking: privilege leak |
