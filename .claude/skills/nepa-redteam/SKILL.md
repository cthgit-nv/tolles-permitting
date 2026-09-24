---
name: nepa-redteam
description: Adversarial review of a permitting document or position, run as a separate agent that did not draft it. Checks facts against the project brain, cross-document consistency, citation accuracy, legal vulnerabilities (segmentation, purpose and need, alternatives, cumulative effects, predetermination, EIS triggers), statements that undercut our own positions, and privilege or sensitivity leaks. Use before anything goes to an agency, the county, counsel, or the public, and whenever the user asks what is wrong with a document or how it could be attacked.
---

# Red team

## Always a fresh context

Launch the `red-team` subagent (`.claude/agents/red-team.md`) with only: the document
path, the project, and the purpose of the document. Do not pass the drafter's reasoning.
Then launch the `verifier` subagent on the findings. Report only findings that survive
verification, and say how many were dropped.

## What the red team checks, in order

1. **Mechanical pre-flight.** `python3 tools/check_outward.py <file> --project <p>`.
2. **Facts vs brain.** Every number, acreage, length, agency, office, facility, and date
   against `projects/<p>/facts.md` and the CHIP Brain. Known canaries: substation shown
   on BLM land in the Hazen PPODs; the GBGT pipeline described as existing.
3. **Cross-document consistency.** PPOD vs SF-299 vs memos vs maps: same facilities, same
   footprints, same purpose statements.
4. **Citations.** Each citation has a library card; quotes match; status is not vacated,
   removed, superseded or questioned; year and reporter are right.
5. **Legal attack surface**, argued as an NGO litigant, a skeptical agency reviewer, and
   an IBLA panel:
   - segmentation and phasing (Application 1 vs 2)
   - purpose and need drawn so narrowly it predetermines the outcome
   - alternatives (too few, or rejected without reasons)
   - cumulative effects (GBGT pipeline, private generation, other ROWs)
   - connected actions and scope (Seven County limits and its critics)
   - Section 7 and Section 106 scope diverging from NEPA scope
   - controversy, precedent, or military conflict pushing toward an EIS
   - administrative record gaps (claims with no support in the record)
6. **Self-harm.** Statements that undercut positions we hold elsewhere: minimizing solar,
   calling Application 1 a phase, conceding interdependence, admitting a decision is
   already made.
7. **Sensitivity.** Privileged or internal content, counsel references, Tolles or
   counterparty names in Hazen OUTWARD text, financial model figures.

## Output

`projects/<p>/redteam/YYYY-MM-DD-<doc-slug>.md`: a table of findings ranked by severity
(Blocking, Serious, Minor), each with location, what is wrong, why it matters, the fix,
and the evidence (fact row, card id, or quote). Then a one-paragraph verdict: ready,
ready after fixes, or not ready.

Log each finding's outcome later in `evals/calibration-log.md` (accepted, rejected,
counsel disagreed).
