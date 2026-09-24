# D-20260924-privileged-sensitivity-tier: Add PRIVILEGED above INTERNAL

- **Project:** all
- **Status:** Active
- **Made by / on:** Cory Hunt, 2026-09-24
- **Sensitivity:** INTERNAL
- **Source:** Cory, setup session 2026-09-24

## Decision

Add a fourth sensitivity tier, PRIVILEGED, above INTERNAL, in this repo and in the
project brains. Counsel memos, meeting notes and transcriptions, and emails are tagged
PRIVILEGED at intake; anything derived from them inherits the tag and points to its
source. PRIVILEGED content may be stored in this private repo and in the brains (Cory:
"it will evolve and we need their input"). It informs analysis and drafting. It never
appears in OUTWARD text, and outward points are supported by public authority instead.

## Why

Counsel's input has to shape the work, so it must live where the agent can read it.
The risk is leakage into agency submissions (FOIA, waiver), not storage in a private
store.

## Rejected

Keeping privileged material out of git entirely (proposed 2026-09-24). Rejected by Cory:
it would cut the agent off from counsel's analysis.

## Reverse this if

- The repo becomes non-private or gains collaborators outside Tolles and counsel.
- Counsel advises a different storage practice for privileged material.

## Conditions

- The CHIP Brain in Dropbox takes INTERNAL or PRIVILEGED writes only after its public
  edit links are fixed (`projects/chip/questions/open/Q-20260924-dropbox-public-edit-links.md`).
- `tools/check_outward.py` and the red-team agent enforce rule 3 on every outward document.
