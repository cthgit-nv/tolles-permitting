# Research: Seed library with current text of NEPA-related statutes, regulations, and Federal Register notices

- **Date:** 2026-09-24
- **Project:** library seed (shared; relevant to chip, fmdp)
- **Asked by:** orchestrating agent for Cory
- **Sensitivity:** PUBLIC

## Question

What is the current primary text and status of the listed NEPA procedure statutes, FLPMA right-of-way provisions, 10 U.S.C. 183a, the BLM and Reclamation use regulations, 43 CFR Part 46, 50 CFR 402.02 and 402.17, 36 CFR 800.16(d), 33 CFR 328.3, and the CEQ and Interior NEPA rulemakings (90 FR 10610, 90 FR 29498, 91 FR 8738)? Are the risk memo's statements about 46.225 and an N.D. Cal. challenge correct?

## Sources searched

| Source | Query or path | Result |
|---|---|---|
| uscode.house.gov | view.xhtml?req=granuleid:USC-prelim-title42-section4336a (also 4336e, 4336f) | Retrieved. Title 42 release current through Pub. L. 119-103 (2026-09-02). NEPA sec. 112 is codified at 42 U.S.C. 4336f. |
| uscode.house.gov | title43-section1761, title43-section1764, title10-section183a | Retrieved. Titles 10 and 43 release current through Pub. L. 119-83 (2026-04-13). |
| eCFR API | /api/versioner/v1/titles.json | Titles 10, 33, 36, 43, 50 up to date as of 2026-09-22. |
| eCFR API | /api/versioner/v1/full/2026-09-22/title-43.xml?part=2800&section=2804.14 (also 2806.14, 2807.21, subpart 2804) | Retrieved (requires Accept-Encoding compression). |
| eCFR API | full/2026-09-22/title-43.xml?part=429 | Retrieved full part. |
| eCFR API | full/2026-09-22/title-43.xml?part=46; versions/title-43.json?part=46 | Retrieved. Part 46 has 8 sections; 46.220 and 46.225 removed 2025-07-03 and reinstated 2026-02-24. |
| eCFR API | full/2026-09-22/title-50.xml?part=402&section=402.02; section=402.17; versions/title-50.json?part=402 | 402.02 retrieved. 402.17: "No matching content found"; removed 2024-05-06. |
| eCFR API | full/2026-09-22/title-36.xml?part=800&section=800.16 | Retrieved. |
| eCFR API | full/2026-09-22/title-33.xml?part=328&section=328.3; versions/title-33.json?part=328 | Retrieved. Last change 2023-09-08. |
| Federal Register API | documents.json, term "90 FR 10610", "90 FR 29498", "91 FR 8738" | Full-text term search did not resolve citations. |
| Federal Register API | agencies=interior-department, term "National Environmental Policy Act", type RULE, since 2025-01-01 | Found 2025-12433 (90 FR 29498) and 2026-03708 (91 FR 8738). |
| Federal Register API | term "Removal of National Environmental Policy Act Implementing Regulations" | Found 2025-03014 (90 FR 10610), C1-2025-03014 (90 FR 11221), 2025-04640 (90 FR 12690), 2026-00178 (91 FR 618, CEQ final rule). |
| Federal Register API | documents/{2025-03014, 2025-12433, 2026-03708, 2026-00178}.json | Metadata retrieved. raw_text_url redirects to a "Request Access" bot page; not usable. |
| govinfo | content/pkg/FR-{date}/html/{doc}.htm for 2025-03014, 2025-12433, 2026-03708, 2026-00178, 2024-06902, 2025-20551, 2023-18929, 2025-20402, 2026-18317 | Retrieved full text with page markers. |
| Federal Register API | cfr title 50 part 402 since 2024; title 33 part 328 since 2023; title 40 part 120 since 2023-06; title 36 part 800 since 2020; title 43 part 429 (all); title 43 part 2800 since 2024 | Found ESA proposed rule 90 FR 52600 (Nov. 21, 2025); WOTUS proposed rule 90 FR 52498 (Nov. 20, 2025) and supplemental NPRM 91 FR 57284 (Sept. 9, 2026); no final rules for 402 or 328 after 2024 and 2023; nothing for 36 CFR 800 since 2020; Part 429 last rule 73 FR 74326 (2008); 43 CFR 2800 rules incl. 90 FR 36111 (Aug. 1, 2025). |
| CourtListener API | v4 search type=r, "National Environmental Policy Act Implementing Regulations" AND Interior | Rate limited (125/day); no result. |
| WebSearch | Interior NEPA rule 2026 N.D. Cal. challenge; "25-cv-10793" | Identified Center for Biological Diversity v. DOI, No. 3:25-cv-10793 (N.D. Cal.). |
| Web (secondary) | paulhastings.com client alert (Jan. 14, 2026); eelp.law.harvard.edu/tracker/nepa-department-of-the-interior; clearinghouse.net/case/47836 | Case facts and docket chronology through Aug. 21, 2026. |
| Web | courtlistener.com/docket/72054719 (WebFetch); cand.uscourts.gov case page (curl) | 403 and 404 respectively; docket not viewed. |
| WebSearch | lawsuit challenging CEQ removal of NEPA regulations final rule January 2026 | No challenge identified (web search only). |

## Found

Cards created: A-usc-42-4336a, A-usc-42-4336e, A-usc-42-nepa-112, A-usc-43-1761, A-usc-43-1764, A-usc-10-183a, A-cfr-43-2804-14, A-cfr-43-2806-14, A-cfr-43-2807-21, A-cfr-43-429, A-cfr-43-46, A-cfr-50-402, A-cfr-36-800-16, A-cfr-33-328-3, A-fr-90-10610, A-fr-90-29498, A-fr-91-8738.

Key findings:

- 43 CFR 46.225 exists. It was removed effective July 3, 2025 (90 FR 29498) and reinstated in modified form by 91 FR 8738 effective Feb. 24, 2026. 46.220 followed the same path. The risk memo's statement is out of date.
- NEPA section 112 is 42 U.S.C. 4336f, added by Pub. L. 119-21, sec. 60026. Fee 125 percent confirmed; EA 180 days from fee payment; EIS 1 year from notice of intent publication.
- 50 CFR 402.17 was removed effective May 6, 2024; a November 2025 proposal would reinstate it; not final.
- CEQ's 90 FR 10610 IFR was adopted without change and superseded by 91 FR 618 (Jan. 8, 2026).
- The N.D. Cal. challenge is Center for Biological Diversity v. DOI, No. 3:25-cv-10793, pending, partial summary judgment briefed in mid-2026 (secondary sources).
- 33 CFR 328.3 is the Amended 2023 Rule, enjoined in 26 States; revision proposed Nov. 2025 with a supplemental proposal Sept. 2026.
- 43 CFR Part 429 does not use the term "crossing agreement".
- 10 U.S.C. 183a is now titled the Military Aviation and Installation Assurance Clearinghouse.

## Not found

- The docket of No. 3:25-cv-10793 itself (CourtListener API rate-limited, docket page 403, N.D. Cal. page 404). Chronology rests on Clearinghouse and Harvard EELP. Content of the Aug. 20 to 21, 2026 stipulation and order unknown. No ruling on the partial summary judgment motion found.
- Which 26 States are under the WOTUS injunctions, and whether Nevada is one of them (not in the saved primary text; EPA status page not fetched).
- Any court challenge to CEQ's removal rule (only a web search, no docket search).
- The enrolled text of Pub. L. 119-21 sec. 60026 (only the U.S. Code codification was read).
- The Pub. L. 119-21 provision behind BLM's 90 FR 36111 solar and wind rent changes, and what the 90 FR 36114 amendment changed in 43 CFR 2807.21.
- What Pub. L. 119-60 sec. 1701(a)(5) changed in 10 U.S.C. 183a.
- The effective date of the 2004 amendment to 36 CFR 800.16 (69 FR 40555).
- "Crossing agreement" as a term in any Reclamation regulation (not in Part 429); Reclamation Manual not searched.
- The DOI NEPA Handbook text (not retrieved).
- CEQ correction 90 FR 11221 and related document 90 FR 12690 (listed by the API, not read).
- The Federal Register API raw_text_url returned a bot-block page; govinfo was used instead.

## Open threads

- Confirm the 3:25-cv-10793 docket on PACER; watch for a ruling on partial summary judgment.
- Watch for a final ESA section 7 rule (would reinstate 402.17) and a final WOTUS rule (supplemental comments due Oct. 9, 2026).
- Confirm which WOTUS regime applies in Nevada.
- Run KeyCite on all cards (all pending).
