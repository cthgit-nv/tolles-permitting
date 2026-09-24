---
name: nepa-edit
description: Edit an uploaded permitting document (Plan of Development, SF-299 narrative, EA section, application letter, response to agency comments, memo) so it matches the current project brain and library, as tracked changes in a copy with a sourced comment on every change. Use when the user uploads or names a document and asks to update, conform, fix, redline, or draft from it.
---

# Document editing

## Rules

- **Never edit the original.** Write `<original name> - Desk Redline YYYY-MM-DD.docx`
  beside it (local Dropbox folder when running on Cory's Mac; otherwise
  `projects/<p>/drafts/`).
- **Tracked changes, not silent edits.** Use the `docx` skill's tracked-change support.
  Every insertion or deletion gets a Word comment: `Source: facts F3; A-cfr-43-429` or
  `Conform to D-20260924-hazen-two-application-structure`.
- **Brain first.** The document conforms to the brain, not the other way around. If the
  document holds a fact the brain lacks, stop and propose the fact before editing.
- **Sensitivity.** An OUTWARD document never receives PRIVILEGED or INTERNAL content.
  If a change needs a point counsel made, support it with a public authority card.
  Hazen OUTWARD text uses role names only.
- **Scope.** Change only what the request and the brain require. List anything else you
  noticed as a comment or in the summary.

## Steps

1. Intake via `permitting-desk` (sensitivity, version, fact comparison).
2. Build a change list before touching the file: each change, reason, source. Show it to
   Cory if it runs past a dozen items or changes positions.
3. Apply as tracked changes with comments.
4. Run `python3 tools/check_outward.py <copy> --project <p>` for OUTWARD documents.
5. Hand to `nepa-redteam` for anything going outside Tolles.
6. Record the new version in `projects/<p>/facts.md` Documents and log the session.
