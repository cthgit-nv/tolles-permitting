# Research: Seed library with NEPA project-definition, segmentation, and connected-action cases

- **Date:** 2026-09-24
- **Project:** library seed (shared; relevant to chip, fmdp)
- **Asked by:** orchestrating agent for Cory
- **Sensitivity:** PUBLIC

## Question

What do the listed NEPA cases actually hold on project definition, federalization, segmentation, and connected actions, with verified quotes and pin cites? Are counsel's citations correct (Friends of the Earth v. Coleman year; Save the Sound LEXIS cite)? Which Ninth Circuit and D.C. Circuit decisions from June 2025 to September 2026 apply Seven County to segmentation or connected-action claims, and does Seven County undercut the pre-2025 Ninth Circuit cases?

## Sources searched

| Source | Query or path | Result |
|---|---|---|
| CourtListener REST API v4 | /api/rest/v4/search/?q="Seven County Infrastructure Coalition"&type=o | Refused: "Request was throttled. Rate limit exceeded: 125/day." Not used further. |
| CourtListener REST API v4 | /api/rest/v4/opinions/10933370/, /clusters/10933370/ | 401, authentication required. |
| CourtListener opinion pages | /opinion/10933370/save-the-sound-inc-v-faa/ | 202 with AWS WAF challenge (empty body). Opinion pages not readable. |
| CourtListener HTML search (www.courtlistener.com/?q=...&type=o) | citation:("605 U.S. 168"), ("541 U.S. 752"), ("882 F.2d 407"), ("295 F.3d 955"), ("408 F.3d 1113"), ("753 F.2d 754"), ("222 F.3d 1105"), ("518 F.2d 323"), ("753 F.3d 1304"), ("260 F. Supp. 2d 997"), ("598 U.S. 651"), ("153 F.4th 1295") | Worked with a browser user agent. Cited-by counts recorded on each card. 260 F. Supp. 2d 997 and 153 F.4th 1295 returned no citation match. |
| CourtListener HTML search | "Border Power Plant Working Group" (sorted by date) | Found 260 F. Supp. 2d 997 (May 2, 2003) and later 467 F. Supp. 2d 1040 (Nov. 30, 2006); cited-by count not displayed. |
| CourtListener HTML search | "Save the Sound" FAA | Found Save the Sound (D.C. Cir. July 21, 2026); For a Better Bayou (citing it as 2026 WL 2093931); Cow Creek Band (D.D.C. Sept. 4, 2026) and Safe Skies Clean Water Wisconsin (D.D.C. Sept. 11, 2026) in results, not opened. |
| CourtListener HTML search, courts ca9 + cadc, filed after 06/01/2025 | "Seven County" segmentation; "Seven County" segment*; "Seven County" "connected actions"; "Seven County" "connected action"; "Seven County" "independent utility"; "Seven County" "single project"; "Seven County" "separate project"; "Seven County" "40 C.F.R. § 1501.9(e)"; "Seven County" "project at hand"; "Seven County" piecemeal*; "Seven County" "Thomas v. Peterson"; "Seven County" "Delaware Riverkeeper" | Candidates: Save the Sound v. FAA (24-1028); Sierra Club v. FERC (24-1099, Sept. 30, 2025, two entries); Sierra Club v. FERC (24-1199, Aug. 1, 2025); Sovereign Inupiat v. BLM (23-3627, June 13, 2025); San Carlos Apache Tribe / Arizona Mining Reform Coalition v. USFS (25-5189, Mar. 13 and Apr. 8, 2026); For a Better Bayou v. FERC (24-1291, Aug. 25, 2026). The piecemeal, Thomas, and Delaware Riverkeeper queries returned nothing in these courts. |
| CourtListener HTML search, court ca9, filed after 06/01/2025 | "Seven County" NEPA | Also listed Cascadia Wildlands v. BLM (Aug. 27, 2025), Friends of Animals v. Burgum (Jan. 14, 2026), Alliance for the Wild Rockies v. Higgins (July 16, 2026). Not opened. |
| CourtListener HTML search, court cadc, filed after 06/01/2025 | "Seven County" NEPA | Same five D.C. Circuit entries as above. |
| CourtListener HTML search, all courts, filed after 06/01/2025 | "Save Our Sonoran" "Seven County"; "Thomas v. Peterson" "Seven County"; "Wetlands Action Network" "Seven County"; "Border Power Plant" "Seven County"; "Sylvester" "Army Corps" "Seven County"; "Ka Makani" "Seven County"; "Friends of the Earth, Inc. v. Coleman" "Seven County"; "Delaware Riverkeeper" "Seven County" | No results for all but the last, which found one state case (Twp. of Marple v. Pa. PUC, Pa. Commw. Ct. Feb. 2, 2026), not reviewed. "No results" was confirmed on the page itself. |
| CourtListener HTML search, ca9 + cadc, filed after 06/01/2025 | "Sovereign Inupiat" segmentation | Only the June 13, 2025 opinion. |
| Caselaw Access Project static export (static.case.law) | /{reporter}/{vol}/CasesMetadata.json and /html/{file}.html for us/541/752, f2d/882/407, f2d/871/817, f2d/884/394, f3d/295/955, f3d/408/1113, f2d/753/754, f3d/222/1105, f2d/518/323, f3d/753/1304, f-supp-2d/260/997, f3d/789/1075 | All retrieved, with reporter page markers. Used for every pre-2019 case. |
| supremecourt.gov | /opinions/slipopinion/24 and /22 (link lists) | Found slip PDFs 23-975_m648.pdf and 21-454_4g15.pdf and reporter-paginated preliminary prints 605us1r34_h3ci.pdf and 598us2r28_hgcj.pdf. |
| supremecourt.gov | 23-975_1a72.pdf (guessed filename) | 404. |
| D.C. Circuit opinions archive (media.cadc.uscourts.gov/opinions) | /bydate/2026/7; /bydate/2025/8; /bydate/2025/9; /bydate/2026/8 | Found 24-1028-2184183.pdf (Save the Sound), 24-1099.pdf, 24-1199-2128320.pdf, 24-1291-2189732.pdf. Note /bydate/2026/07 (leading zero) returns the current month instead. cadc.uscourts.gov/internet/opinions.nsf returned 404. |
| Ninth Circuit (cdn.ca9.uscourts.gov/datastore/opinions) | 2025/06/13/23-3627.pdf; 2026/03/13/25-5189.pdf; 2026/04/08/25-5189.pdf | Retrieved. |
| Justia (law.justia.com, supreme.justia.com), openjurist.org, Google Scholar | case pages | 403 (site blocks). |
| casetext.com | case page | 410 (gone). |
| law.resource.org | F2/882/ | Index reachable; not needed after CAP. |
| loc.gov | usrep605168 | 403 / 404. |

## Found

Cards created (all `verified_by: agent-free-sources`, `keycite: pending`):

- A-case-seven-county (good-law)
- A-case-public-citizen (good-law)
- A-case-sylvester (good-law; 882 F.2d 407 is Sylvester II, see Notes)
- A-case-ka-makani (good-law)
- A-case-save-our-sonoran (questioned, on our reading of Seven County and Sackett)
- A-case-thomas-v-peterson (questioned, remedy holding abrogated by Cottonwood, 789 F.3d at 1092)
- A-case-wetlands-action (good-law)
- A-case-foe-coleman (good-law; decided 1975, not 1995)
- A-case-del-riverkeeper (good-law)
- A-case-border-power (questioned, but-for reasoning undercut by Public Citizen and Seven County)
- A-case-save-the-sound (good-law; retrieved from the D.C. Circuit site)
- A-case-sackett (good-law)
- A-case-sierra-club-ferc-cumberland (good-law; post-Seven County connected actions)
- A-case-sovereign-inupiat (good-law; post-Seven County segmentation, Ninth Circuit)
- A-case-az-mining-reform (good-law; post-Seven County separate project, Ninth Circuit)

Post-Seven County decisions found but not carded:

- Sierra Club v. FERC, No. 24-1199 (D.C. Cir. Aug. 1, 2025) (Saguaro Connector pipeline; alternatives and upstream effects; cites Seven County at 145 S. Ct. 1512 to 13). Downloaded and skimmed only.
- For a Better Bayou v. FERC, No. 24-1291 (D.C. Cir. Aug. 25, 2026) (CP2 LNG and pipeline; cumulative effects; cites Cumberland and Save the Sound). Downloaded and skimmed only.
- Cascadia Wildlands v. BLM (9th Cir. Aug. 27, 2025); Friends of Animals v. Burgum (9th Cir. Jan. 14, 2026); Alliance for the Wild Rockies v. Higgins (9th Cir. July 16, 2026). Listed by CourtListener as citing Seven County in NEPA cases; not opened.
- Beyond Nuclear, Inc. v. NRC, No. 24-1318 and American Whitewater v. FERC, No. 25-1092 (D.C. Cir. July 2026) appear in the D.C. Circuit archive; not checked for NEPA content.

## Not found

- **Save the Sound LEXIS cite.** Counsel's "2026 U.S. App. LEXIS 21635" could not be verified from any free source. The only parallel cite seen is 2026 WL 2093931 (in For a Better Bayou). No F.4th cite yet on CourtListener.
- **Cumberland reporter pages.** 153 F.4th 1295 is confirmed only by citations in two later D.C. Circuit opinions; the reporter text and its internal pages were not seen.
- **Seven County bound-volume pages.** Pins were verified against the preliminary print, which is subject to revision. S. Ct. pages (used by Cumberland) were not mapped.
- **CourtListener cited-by lists and negative treatment.** The API was rate-limited and opinion pages were behind a WAF challenge, so only the counts shown in search snippets were recorded. No citator was run; free sources cannot reliably show negative treatment.
- **Any post-Seven County court decision expressly questioning Save Our Sonoran, Thomas v. Peterson, Wetlands Action Network, Sylvester, Ka Makani, FOE v. Coleman, or Border Power.** Searched CourtListener full text (all courts, after June 1, 2025); none found. The "questioned" statuses on Save Our Sonoran and Border Power are our own reading.
- **Relationship between Sylvester I at 871 F.2d 817 and 884 F.2d 394.** Both carry the same decision date in CAP metadata; whether 884 F.2d 394 is an amended opinion was not determined.
- **Later history** for Sovereign Inupiat, Arizona Mining Reform Coalition, Save the Sound, and Cumberland (rehearing, certiorari, mandate) was not checked.
- **Why CourtListener shows two entries for Cumberland (24-1099)** was not determined.

## Open threads

- Counsel to confirm which Sylvester opinion their memo means; the "federalization" and "links in a chain" rule is in Sylvester I (871 F.2d 817 / 884 F.2d 394), not 882 F.2d 407. Consider a separate card for Sylvester I.
- Correct the FOE v. Coleman year to 1975 in the counsel memo.
- Send the KeyCite batch (`tools/verify_library.py --keycite-list`) to Holland & Hart, with priority on Save Our Sonoran, Thomas v. Peterson, Border Power, and Cumberland.
- Status of 33 C.F.R. pt. 325, app. B (Corps NEPA scope rule relied on in Wetlands Action and Save Our Sonoran) after the CEQ rescission was not checked.
- Card For a Better Bayou and Sierra Club v. FERC (24-1199) if cumulative effects or upstream effects become live issues.
- Source files are verbatim court text and contain em-dashes from the originals; the cards and this log do not.
