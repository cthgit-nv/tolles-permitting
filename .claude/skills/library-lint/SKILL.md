---
name: library-lint
description: Keep the research library trustworthy. Runs the verifier, finds stale and unverified cards, re-checks watchlist items against their sources, flags propositions and project documents that rely on authority that changed, and prepares the KeyCite batch for counsel. Use when the user says lint the library, before any filing, monthly, or when a watchlist item may have moved.
---

# Library lint

1. `python3 tools/verify_library.py`. Fix errors (bad fields, failed quotes, missing
   cards). A failed quote means the card is wrong or the source file changed: re-fetch the
   source and correct the card; never edit the source file to match a quote.
2. `python3 tools/verify_library.py --stale`. Re-verify each stale card against its source
   URL. Update `verified_on` and add a Treatment line.
3. **Watchlist.** For each item in `library/watchlist.md`, check the source (docket,
   Federal Register, agency page) for movement. If something changed: update the card
   status, then find every proposition that cites it and every project document or
   decision whose "Depends on" names those propositions. List them for Cory as "rests on
   authority that moved."
4. **Unverified cards.** Try once more to verify. Anything still unverified that is cited
   in an OUTWARD draft is a Blocking red-team finding.
5. **Citator batch.** `python3 tools/verify_library.py --keycite-list`. Draft a short
   email to Holland & Hart asking for KeyCite on the list. When results come back, set
   `keycite: clean` or `flagged` with a Treatment line naming the date and source.
6. Log the lint in `library/research-log/YYYY-MM-DD-lint.md`.
