---
name: nepa-analyze
description: Apply the library to a project's facts to answer structuring questions: CX vs EA vs EIS, segmentation and phasing between Hazen Application 1 and Application 2, connected actions and Seven County scoping of private-land generation, lead and cooperating agencies, applicant-prepared EAs, the Section 112 opt-in fee, ESA and Section 106 scope, FONSI protection, and litigation exposure. Use when the user asks what pathway to take, whether a structure is defensible, or how a change in facts affects the NEPA position.
---

# NEPA analysis

## Method

1. **Facts.** State the facts relied on, each with its `facts.md` row or CHIP Brain
   citation. Missing facts become open questions, not assumptions.
2. **Issues.** Break the question into propositions. For each, pull the card (run
   `nepa-research` for gaps).
3. **Apply.** For each proposition: rule (card id, status, weight), application to these
   facts, the strongest counterargument, and the answer to it.
4. **Conclude** with a confidence label per conclusion:
   - *Strong*: settled or majority law, facts clearly within it.
   - *Defensible*: majority or contested law, facts support it, a real counterargument exists.
   - *Advocacy*: our argument; plausible, not established.
   - *Weak*: we would likely lose if challenged.
5. **Actions.** What to do to strengthen the position: design commitments, record
   choices, sequencing, questions for counsel or the agency.
6. **Record.** Propose any decision to Cory. Write open questions directly.

## Standing checks for Hazen

- **Segmentation (Application 1 vs 2).** Test independent utility, whether Application 1
  forecloses alternatives for Application 2, whether it commits resources to it, timing,
  and financial interdependence. Use pre- and post-Seven County authority and say which
  controls.
- **Phasing discipline.** Application 1 has its own purpose (CHIP parcel access and
  utilities). No FMDP document calls it a phase.
- **Private generation.** Seven County scoping for NEPA; separately test ESA Section 7
  (but-for plus reasonably certain) and Section 106 APE (indirect and visual effects).
- **Existing vs future disturbance.** Only the NV Energy road and line are existing. The
  GBGT pipeline is a future action for cumulative effects.
- **EIS avoidance.** Name what could push BLM to an EIS: controversy, precedent-setting,
  cumulative effects, military conflict, tribal concerns, species.

## Standing checks for Denim

- Substation footprint on BLM land; land use plan conformance; corridor designation.
- Desert tortoise consultation pathway.
- Holder and future utility ownership.

## Output

A short memo: Question, Short answer (with confidence labels), Facts relied on, Analysis
by proposition, Risks, Actions, Questions for counsel. Sensitivity: PRIVILEGED if it
relies on counsel material, otherwise INTERNAL. Save to `projects/<p>/privileged/` or
`projects/<p>/drafts/` accordingly.
