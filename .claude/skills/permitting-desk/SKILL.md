---
name: permitting-desk
description: Front door for all NEPA and permitting work on CHIP (Hazen Application 1, Reclamation crossings and Hart Lane road), FMDP (Hazen Application 2, BLM transmission and roads) and Project Denim (Jean BLM substation, lines, road, fiber). Use at the start of any session in this repo, whenever the user uploads or names a permitting document, asks where an authorization stands, asks a NEPA, ESA, NHPA, FLPMA, Reclamation, case law or procedure question, or asks to research, analyze, edit, red-team or track anything permitting-related.
---

# Permitting desk

You route the request, load the right context, and make sure the other skills' rules are
followed. Read `CLAUDE.md` if you have not this session.

## 1. Orient (every session)

1. `python3 tools/verify_library.py`. Report errors before relying on the library.
2. Identify the project: `chip`, `fmdp`, `denim`, or several. If ambiguous, ask. The
   referent matters: Application 1 and Application 2 must never blur (segmentation).
3. Read `projects/<p>/index.md`, `facts.md`, `tracker.md`, `questions/open/`, and the
   decisions in `decisions/` and `projects/<p>/decisions/`.
4. Skim the latest two files in `projects/<p>/log/`.
5. For Hazen program facts (acreage, parcels, GID), use the `chip-brain` skill rather than
   memory. Its Step 1b shared-link check governs writes to the CHIP Brain.

## 2. Route

| Request | Skill |
|---|---|
| "What does the law say about X", "find cases on", "is X still good law" | `nepa-research` |
| "What pathway", "can we use a CX", "segmentation risk", "how should we structure" | `nepa-analyze` (calls research as needed) |
| Uploaded document to update, conform, or redline | intake (below), then `nepa-edit` |
| "Red-team", "what's wrong with", "is this ready to send", before anything outward | `nepa-redteam` |
| "Where does X stand", deadlines, commitments, agency asks | `permit-track` |
| "Lint the library", stale cards, citator batch | `library-lint` |

Several skills can run in one request. Typical document flow: intake, edit, red-team.

## 3. Intake of an uploaded document

1. Identify it: type, author, date, version, project, and whether it is the current
   version of something already listed in `projects/<p>/facts.md` Documents.
2. **Tag sensitivity.** Counsel memos, meeting notes or transcriptions, and emails:
   PRIVILEGED. Documents with a privilege header: PRIVILEGED. Agency submissions and
   drafts of them: OUTWARD. Everything else: INTERNAL unless public.
3. Record it in the project's Documents table (path, sensitivity, status).
4. Extract every factual assertion that bears on permitting and compare each to
   `facts.md` and the CHIP Brain. List agreements, contradictions, and new facts.
5. Propose new facts and corrections to Cory (facts need approval). Write any new open
   questions directly and show them.
6. If PRIVILEGED and substantive, write or update a distillation in
   `projects/<p>/privileged/`.

## 4. Close the session

1. Update `index.md` and `tracker.md` in present tense.
2. Confirm new decisions and questions reached their folders.
3. Write `projects/<p>/log/YYYY-MM-DD-topic.md`: what happened, what changed, what is
   open, which cards were used or added.
4. If anything changed the Hazen program, write the matching CHIP Brain entry via
   `chip-brain` (only once its shared-link check passes), then `brain-wrap`.
5. Commit with a message naming the project and the change. Push if a remote exists.
