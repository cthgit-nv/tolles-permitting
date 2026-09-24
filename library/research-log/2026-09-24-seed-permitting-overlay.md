# Research: Seed library with the non-NEPA permitting overlay for the Hazen and Jean projects

- **Date:** 2026-09-24
- **Project:** library seed (shared; relevant to chip, fmdp, Jean ROW for Jean Data Partners LLC)
- **Asked by:** orchestrating agent for Cory
- **Sensitivity:** PUBLIC

## Question

Which non-NEPA permitting authorities apply to (1) Hazen, Churchill County: Reclamation Part 429 crossings and road, and the BLM Title V ROW for FMDP transmission and access roads next to NAS Fallon and the FRTC; and (2) Jean, Clark County: a BLM ROW for a substation, lines, road and fiber serving facilities on a Nevada Division of State Lands leasehold in desert tortoise habitat? What does the primary text say?

The authorities in scope are:

- Nevada UEPA
- NRS 533 (State Engineer)
- ESA section 7 and the tortoise programmatic BO
- the Clark County MSHCP
- 36 CFR 800.2(c)(2)
- Section 368 corridors and the governing RMPs
- 32 CFR 211 and the FRTC withdrawal
- 14 CFR 77
- FAST-41 and 28 U.S.C. 2401(a)
- MBTA and the Eagle Act

## Sources searched

| Source | Query or path | Result |
|---|---|---|
| leg.state.nv.us | /NRS/NRS-704.html | Retrieved (windows-1252; Rev. 4/15/2026, 2025 session). NRS 704.820 to 704.900 extracted. |
| leg.state.nv.us | /NRS/NRS-533.html | Retrieved (Rev. 4/15/2026). 533.025, .030, .035, .325, .370 extracted. |
| uscode.house.gov | view.xhtml granuleid USC-prelim-title16-section1536, -section703, -section668, -section668a; title42-section4370m, -4370m-2, -4370m-6; title28-section2401 | All retrieved; pages state "laws in effect on September 23, 2026". 4370m-2 was fetched but not used. |
| eCFR API | titles.json | Titles 14, 32, 36, 50 up to date as of 2026-09-22. |
| eCFR API | full/2026-09-22/title-36.xml?part=800&section=800.2; title-32.xml?part=211; title-14.xml?part=77&subpart=B; title-50.xml?part=22; title-50.xml?part=21&subpart=A; title-50.xml?part=17&section=17.11 | Retrieved. The first attempt returned 406 until an Accept-Encoding compression header was sent. Part 21 subpart A was fetched but not used. |
| Federal Register API | documents.json, term "migratory bird" incidental take, agency FWS | Found 2025-06782 (90 FR 16664), withdrawal of the 2021 MBTA incidental take ANPRM. |
| Federal Register API | term "eagle permits", agency FWS | Only information collection notices since 2024 (e.g. 2026-06274). No rule revising 50 CFR 22 subpart E. Also surfaced 2026-14195 (91 FR 43300, rescinding ESA "harm" definition, effective 2026-09-14). |
| Federal Register API | term "Interagency Cooperation Regulations" since 2025-06 | Only the 2025-20551 proposed rule (90 FR 52600). No final rule. |
| Federal Register API | documents/{2025-06782, 2025-20551, 2026-14195}.json | Metadata and abstracts saved to the ESA and MBTA source files. |
| Federal Register API | term "Protection of Historic Properties", agency ACHP, since 2024-06 | No results. |
| Federal Register API | term "part 77" obstruction notice rule, type RULE, since 2024-06 | No relevant result. |
| Federal Register API | term "Mission Compatibility Evaluation Process" since 2024-06 | No relevant result. |
| Federal Register API | term "covered project" Permitting Council, type RULE, since 2024-06 | No relevant result. |
| Federal Register API | term "Section 368" corridor, agency BLM; term "Section 368 Energy Corridor" (any agency) | Found 2023-26493 (88 FR 83959 NOI), 2024-26598 (Purple Sage), 2024-20864 (Greenlink West ROD), 2026-15270 (Mosey NOI), and others. No Draft or Final EIS or ROD for the 2023 Section 368 revision effort. |
| Federal Register API | term "Carson City District" resource management plan; "Carson City resource management plan revision"; "Greenlink North" | Found 2012-4198 (revision NOI), 2024-00942 (Dodge Flat II), 2023-11070 (Greenlink North NOI), 2024-19544 (Greenlink North DEIS NOA, not fetched), 2025-09497 (Greenlink North FEIS NOA), 04-7001 and 03-18560 (not fetched). No revision termination, draft or ROD; no Greenlink North ROD. |
| federalregister.gov | documents/full_text/text/2023/12/01/2023-26493.txt | Returned "Request Access" bot page; used govinfo instead. |
| govinfo | content/pkg/FR-{date}/html/{doc}.htm for 2023-26493, 2024-26598, 2024-20864, 2024-12960, 2026-15270, 2019-09696, 2012-4198, 2025-09497, 2024-00942, 2023-11070 | Retrieved. |
| govinfo | content/pkg/PLAW-117publ263/html/PLAW-117publ263.htm | Retrieved (6.5 MB). Title XXIX subtitle A (FRTC) extracted. |
| WebSearch | Interior Solicitor opinion 2025 MBTA incidental take; "M-37086" OR "M-37085" | Identified M-37085 (Apr. 11, 2025). |
| doi.gov | sites/default/files/documents/2026-05/m-opinions-index-1993-may-2026.pdf | Retrieved. M-37085 is the latest MBTA opinion listed (index through M-37089, May 22, 2026). |
| doi.gov | sites/default/files/documents/2025-04/m-37085.pdf | Retrieved (1 page scanned; OCR text saved as extracted). |
| WebSearch | programmatic biological opinion BLM Southern Nevada District desert tortoise rights-of-way; "84320-2010-F-0365"; "2019-F-0153" SNDO | Identified the ePlanning URL for the 08ENVS00-2019-F-0153 PBO. Earlier file 84320-2010-F-0365.R003 appeared only in search snippets. |
| ecos.fws.gov | tails/pub/document/7879863 | Retrieved. It is the 2017 California Desert Conservation Area BO (Carlsbad FWO), not Nevada. Not used. |
| ecos.fws.gov | ecp/pullreports/catalog/species/report/bo/export?format=html | Retrieved 2,999 rows (latest 01/21/2022). SNDO PBO reinitiation and appended ROW rows found. |
| eplanning.blm.gov | 7MM Decision Record PDF; SNDO PBO PDF (nepa/1504053/...); Greenlink West BO PDF; eplanning-ws and eplanning-ui project 1504053 | All returned the NEPA Register HTML shell or "This document is not currently available". Not read (curl and WebFetch). |
| fws.gov | 2024-07 April 2024 MOG meeting summary PDF; 20220426 MOG notes PDF | Retrieved. No SNDO PBO details. Not used. |
| deserttortoise.org | Nevada Multi-District OHV SRP EA comments PDF | Retrieved (secondary). Not used. |
| usbr.gov | lc/region/g2000/envdocs/LaughlinRacesYearRoundRacingAreaEA.pdf | Empty reply from server. |
| blm.gov | press-release/blm-seeks-input-northern-ivanpah-valley-desert-tortoise-habitat-plan-nevada | Retrieved (July 10, 2024). |
| WebSearch | Clark County MSHCP section 10 permit covered activities non-federal land amendment | Identified County pages. |
| clarkcountynv.gov | MSHCP/EIS ch. 2 PDF (chap2.pdf); mshcp-permit-amendment-faq page; dcp-andmshcp-101.pdf | Retrieved. |
| WebSearch | Section 368 energy corridor Nevada Ivanpah Jean corridor abstracts | Identified corridoreis.anl.gov abstracts for 27-41, 27-225, 224-225, 37-223. |
| corridoreis.anl.gov | documents/docs/corridor-abstracts/corridor-27-225.pdf, -224-225.pdf, -225-231.pdf | HTTP 403 (curl and WebFetch). Not read. |
| WebSearch | BLM Las Vegas Pahrump RMP revision status | Identified 84 FR 20657 termination notice. |
| WebSearch | Public Law 117-263 Fallon Range Training Complex withdrawal text | Identified govinfo and congress.gov. Used the govinfo PLAW text. |

Retrieved text was normalized to ASCII quotes and dashes in the saved source files. Word-processor artifacts ("Ê" hanging-indent characters) were stripped from the NRS extracts.

## Found

Cards created: A-nrs-704-uepa, A-nrs-533-state-engineer, A-usc-16-1536, A-guid-tortoise-programmatic-bo, A-guid-clark-msch, A-cfr-36-800-2, A-guid-section-368-corridors, A-guid-rmp-southern-nv, A-guid-rmp-carson-city, A-cfr-32-211, A-usc-frtc-withdrawal, A-cfr-14-77, A-usc-42-4370m, A-usc-28-2401, A-usc-16-703-mbta, A-usc-16-668-eagle.

Key findings:

- UEPA (NRS 704.860, .865, .870):
  - A PUCN permit is required for transmission lines and substations of 200 kV or more outside incorporated cities, with no length threshold.
  - It is also required for every non-renewable generating plant of any size, and for renewable plants over 70 MW.
  - When a federal agency does NEPA, the applicant must file a notice with the PUCN on or before the day it files the federal application. It then files the UEPA application within 30 days after the final EA or EIS.
  - The PUCN must accept the federal environmental findings and may not duplicate the review.
- NRS 704.848(2) excludes the State Engineer from the UEPA coordination scheme.
- Desert tortoise (Mojave DPS) is listed as threatened. FWS ECOS lists an SNDO programmatic BO reinitiation, 08ENVS00-2019-F-0153 (01/14/2020), with ROW and transmission projects appended to it. The PBO text itself could not be retrieved.
- The Clark County MSHCP covers take only on non-Federal land. It excludes take "resulting from Federal actions on non-Federal lands". The permit expires at 145,000 acres or January 2031, and an amendment is planned.
- The FY2023 NDAA (sec. 2991(j) of the FRTC subtitle) confirms a designated West-Wide Energy Corridor next to the B-16 Range, with an existing transmission line along B-16's western boundary. The Navy must allow one more line inside B-16. The withdrawal ends Nov. 6, 2047.
- Section 368 corridor 224-225 ("North Pahrump/U.S. 95 to Las Vegas/Ivanpah Valley") is designated. The 2023 BLM revision NOI covers seven other corridors, and no later EIS or ROD was found.
- The Las Vegas RMP (1998, as amended) governs; its revision was terminated in 2019. The Carson City CRMP (2001, as amended) governs; the 2012 revision NOI has no visible outcome. The Greenlink North FEIS notice says lines over 100 kV did not conform to the CRMP objectives, which triggered an RMP amendment.
- MBTA: under M-37085 (Apr. 11, 2025), Interior treats M-37050 as binding, meaning no incidental take liability, except within the S.D.N.Y. FWS withdrew its incidental take ANPRM (90 FR 16664).
- Eagle Act: 50 CFR 22.260 (2024) offers a general permit for power lines with a maximum tenure of 5 years.
- FAST-41: the covered project sectors now include data storage, high-performance computing and energy storage. The limitations period is 2 years from the Federal Register notice. The Mosey Solar Project in the SNDO was made a covered project on Jan. 17, 2025.
- 32 CFR 211 still cites NDAA FY2011 sec. 358 and uses 30-day steps. 10 U.S.C. 183a (see A-usc-10-183a) now provides 75 days, so the part is marked questioned.

## Not found

- The text of the FWS SNDO programmatic BO (08ENVS00-2019-F-0153), including covered activities, acreage caps, remuneration fee and appending procedure. The ePlanning PDF returns "not currently available". It was not found on fws.gov or ecos.fws.gov (the ECOS catalog shows metadata only, and its export appears capped at 2,999 rows ending January 2022). Any SNDO PBO reinitiation or appends after January 2022 were not seen.
- Whether the Jean site lies within or near the Large-Scale Translocation Site, the Northern Ivanpah Valley connectivity project area, or desert tortoise critical habitat. No mapping was done.
- The Clark County section 10 permit itself (permit number, issuance date, terms), the current per-acre mitigation fee, and whether the amendment application has been filed or approved. Also not found: whether Nevada Division of State Lands leaseholds at Jean are treated as within the permit area for fee purposes.
- Argonne corridor abstracts (corridoreis.anl.gov, HTTP 403). Therefore not verified: corridor 27-225's endpoint "south of Jean, NV" (search snippet only), and the number and location of the West-wide corridor next to B-16.
- The 2009 WWEC ROD and its interagency operating procedures (not searched).
- Any Draft EIS, Final EIS or ROD for the 2023 Section 368 revision effort (FR API search, no hits after the NOI).
- The status of the 2012 Carson City District RMP revision (no FR notice after the NOI found). Also not found: a Greenlink North ROD (FR API search, latest hit is the May 28, 2025 FEIS NOA).
- The FRTC map "Churchill County Proposed Fallon Range Training Complex Modernization and Lands Bill" (Nov. 30, 2022). The location of B-16 relative to Hazen. The full text of FY2023 NDAA secs. 2907 (Churchill County conveyances) and 2989 (Fallon Paiute-Shoshone trust land). Amendments to the FRTC subtitle after enactment (not checked).
- Whether the Great Basin Gas Transmission pipeline is FERC-certificated, which bears on the NRS 704.865(3)(c) exclusion (not searched).
- Whether a behind-the-meter gas plant serving only the data center is a UEPA "utility facility" (no PUCN order or NAC 703 text read).
- NAC 703 UEPA implementing regulations (not searched).
- NRS Chapter 534 groundwater provisions and the Churchill County basin status (not searched).
- The Jean Sport Aviation Center airport data (public-use status, runway length) and the NAS Fallon runway distance from the Hazen site (not searched).
- Corner Post (2024) opinion text (not retrieved; noted without a card).
- Case law on MBTA incidental take in the Ninth Circuit (not searched).
- Whether FAST-41 still carries a sunset provision (42 U.S.C. 4370m-12 not read).

## Open threads

- Get the SNDO PBO from BLM Las Vegas FO or the FWS Southern Nevada FWO. Confirm the Jean ROW can be appended to it, and the fee.
- Ask Clark County DCP whether the State Lands leasehold facilities at Jean pay into the MSHCP. Ask how the "Federal actions on non-Federal lands" carve-out is applied where a BLM ROW serves the leasehold.
- Map the FMDP route against the Carson City CRMP corridors, the B-16 West-wide corridor and the Greenlink North corridor. Decide early whether an RMP amendment is needed.
- File the UEPA 704.870(2) notice with the PUCN no later than the federal application filing for any FMDP line of 200 kV or more and for the gas plant. Confirm with counsel whether a UEPA permit is needed for a behind-the-meter gas plant.
- Request an informal DoD Clearinghouse review (32 CFR 211.7) for the Hazen site before any FAA 7460-1 filing. Run the FAA Notice Criteria Tool for both sites.
- Decide whether to seek FAST-41 covered status for either project, to get the 2-year limitations period.
- Watch for: a final 50 CFR 402 rule (90 FR 52600 proposal); a Section 368 revision Draft EIS; the Clark County MSHCP amendment; any new MBTA M-Opinion.
