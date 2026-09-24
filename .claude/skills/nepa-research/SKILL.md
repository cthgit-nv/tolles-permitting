---
name: nepa-research
description: Library-first legal research for NEPA and permitting questions (NEPA statute and Interior procedures, CEQ history, FLPMA Title V and 43 CFR 2800, Reclamation Part 429, categorical exclusions, segmentation and connected actions, cumulative effects, ESA Section 7, NHPA Section 106, CWA 404, Nevada UEPA, IBLA and case law). Use when a question needs legal authority, when a proposition card is missing or stale, when checking whether a case or rule is still good law, or when the watchlist flags a change. Adds everything it finds to the library so it is not researched twice.
---

# NEPA research

The goal is an answer backed by verified cards, and a library that is richer afterward.

## 1. Library first

1. Search `library/propositions/` for the proposition. Search `library/authorities/` by
   citation and topic. `grep -ril "<term>" library/`.
2. Search `library/research-log/` for the question, including **Not found** sections.
   If a prior session searched and found nothing, do not repeat that search unless the
   law has changed since (check `library/watchlist.md`).
3. If a fresh card answers it (see freshness in `library/README.md`), answer from the card
   with its id. Stop.

## 2. Outside research (only for gaps)

Free sources, in order of authority:
- Statutes: uscode.house.gov, govinfo.gov. Regulations: eCFR API
  (`https://www.ecfr.gov/api/versioner/v1/full/<date>/title-<n>.xml?part=<p>&section=<s>`).
- Federal Register: `https://www.federalregister.gov/api/v1/documents/<doc>.json`.
- Cases: CourtListener (`/api/rest/v4/search/`, citation lookup), supremecourt.gov,
  cdn.ca9.uscourts.gov, cadc.uscourts.gov.
- IBLA: DOI OHA, `https://www.doi.gov/oha/organization/ibla/Finding-IBLA-Decisions`
  (1970 to present; chronological index). Persuasive only.
- Agency practice: BLM National NEPA Register (eplanning.blm.gov), usbr.gov, doi.gov.
- Nevada: leg.state.nv.us (NRS, NAC), puc.nv.gov.

For each new authority:
1. Save the operative text to `library/sources/<id>.txt`, first line
   `SOURCE: <url> RETRIEVED: <date>`.
2. Write the card from `library/_templates/authority.md`. Quotes copied verbatim from the
   source file, with the pin cite actually verified.
3. Record treatment you can see. Leave `keycite: pending`.
4. Link it to propositions. Create the proposition card if none exists.
5. Run `python3 tools/verify_library.py` until clean.

If the question sits on a moving target (pending litigation, new rule, recent circuit
split), add it to `library/watchlist.md`.

## 3. Answer

- Every legal statement carries a card id, or is marked UNVERIFIED.
- Give the proposition status (settled, majority, contested, open, advocacy) and the
  binding weight in the Ninth Circuit.
- Separate what the law says from what we would argue.
- Name the best adverse authority and the answer to it. An answer with no adverse
  authority considered is incomplete.
- Say when the question needs counsel, and draft the question for Holland & Hart.

## 4. Log

Write `library/research-log/YYYY-MM-DD-<slug>.md` for every outside research session,
with the Not found section filled in.
