# Research Library

Shared across every project. Holds the law, not the facts. Project facts live in
`projects/<name>/` (and, for Hazen, the CHIP Brain in Dropbox).

The library exists so research is done once. Before going to any outside source, check
here. When outside research is needed, the result becomes a card here.

## Three kinds of entry

| Folder | Unit | Changes by |
|---|---|---|
| `authorities/` | One statute section, regulation, Federal Register notice, agency guidance document, case, IBLA decision, state law, or prior agency NEPA document used as precedent (`agency-precedent`) | Edit in place; every edit updates `verified_on` and adds a Treatment line |
| `propositions/` | One legal proposition we rely on or must answer, with supporting and adverse authority | Edit in place; `last_reviewed` updated |
| `research-log/` | One research session: the question, where we looked, what we found, **including what we did not find** | Never edited after the session |

`sources/` holds the primary-source text each authority card quotes from. Quotes are
checked against these files by `tools/verify_library.py`. A quote that is not in the
source file fails the check.

## Authority card

File: `authorities/A-<kind>-<short-slug>.md` (for example `A-case-seven-county`,
`A-cfr-43-429`, `A-usc-42-4336e`, `A-fr-90-10610`).

```yaml
---
id: A-case-seven-county
type: case            # case | statute | regulation | federal-register | agency-guidance | ibla | agency-precedent | state-law
citation: "Seven County Infrastructure Coalition v. Eagle County, 605 U.S. 168 (2025)"
court: SCOTUS         # SCOTUS | CA9 | CADC | other circuit | district | IBLA | n/a
weight: binding       # binding | persuasive | agency-internal
decided: 2025-05-29   # or effective date for rules
status: good-law      # good-law | questioned | pending-challenge | superseded | vacated | removed | unverified
source_url: "https://..."
source_file: library/sources/A-case-seven-county.txt
verified_on: 2026-09-24
verified_by: agent-free-sources   # agent-free-sources | counsel-keycite | cory
keycite: pending      # pending | clean | flagged (with note) ; set only from a citator result
propositions: [P-separate-projects-not-analyzed]
sensitivity: PUBLIC
---
```

Body sections, in order:

1. `## What it is` : one or two sentences.
2. `## Operative text or holding` : in our words, short.
3. `## Quotes` : verbatim quotes, one per line, each a blockquote with a pin cite:
   `> "exact words from the source" (slip op. at 12)`.
   The words between the quotation marks must appear in `source_file`.
4. `## Treatment` : dated lines. `2026-09-24: no negative treatment found on CourtListener; KeyCite pending.`
5. `## Notes` : anything a future session needs, including known citation errors in our
   own or counsel's documents.

### Pin cites

Free sources often carry only the slip opinion for recent cases, not the bound U.S.
Reports pages. Record the pin you actually verified (`slip op. at 12`). If a document
cites a reporter page you could not verify, say so in Notes; do not guess the mapping.

## Proposition card

File: `propositions/P-<slug>.md`.

```yaml
---
id: P-separate-projects-not-analyzed
statement: "An agency need not analyze the effects of a separate project that it has no authority to regulate, even if that project is but-for dependent on the action under review."
status: settled       # settled | majority | contested | open | advocacy
projects: [chip, fmdp, denim]
supporting: [A-case-seven-county, A-case-public-citizen]
adverse: [A-case-save-our-sonoran]
last_reviewed: 2026-09-24
sensitivity: PUBLIC
---
```

Body: `## Why it matters to us`, `## Best supporting authority`, `## Best adverse authority
and the answer to it`, `## Limits`, `## Relied on by` (documents, decisions, drafts).

Status meanings:

- **settled**: binding authority squarely holds it; no live contrary authority.
- **majority**: most courts agree; some contrary or unsettled authority exists.
- **contested**: live split or pending challenge that could change the answer.
- **open**: no controlling authority.
- **advocacy**: our argument. Defensible, not established. Never present it as settled.

## Research log entry

File: `research-log/YYYY-MM-DD-<slug>.md`. Fields: Question, Project, Sources searched
(with queries), Found (card ids created or updated), **Not found** (what we looked for and
did not find, and where), Open threads.

## Freshness

| Type | Re-verify after |
|---|---|
| Statute, bound case with clean KeyCite | 12 months |
| Regulation, agency guidance | 6 months |
| Anything on `watchlist.md` | 30 days |
| `status: pending-challenge` or `unverified` | Before any use in an OUTWARD document |

## Citator

Free sources cannot reliably report negative treatment. `keycite: pending` stays pending
until counsel (Holland & Hart) runs KeyCite or someone runs a citator. `tools/verify_library.py
--keycite-list` prints the batch to send.
