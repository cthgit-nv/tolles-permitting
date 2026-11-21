"""Desk redline of the Oct 29, 2026 SF-299 narrative (EPS), Nov 21, 2026.

Run from projects/chip/drafts with the narrative unpacked in ./work_sf299.
Comments are written for EPS and BRK (no internal repo ids, no counsel content).
Internal sources for each change: redteam/2026-11-21-sf299-102926.md.
"""
import sys
sys.path.insert(0, '.')
import redline_lib
redline_lib.DATE = '2026-11-21T09:00:00Z'
from redline_lib import Redliner

R = Redliner('work_sf299/word/document.xml')
T = R.text
PENDING = {}


def rep(i, old, new, comment=None):
    """Queue a replacement; all replacements in one paragraph become one tracked edit."""
    cur = PENDING.setdefault(i, [T(i), []])
    assert old in cur[0], (i, old, cur[0][:160])
    cur[0] = cur[0].replace(old, new)
    if comment and comment not in cur[1]:
        cur[1].append(comment)


GEOM = ('GEOMETRY (blocking). Width and acreage do not match. A wing whose long side spans a corridor W feet wide has area W x W / 4. '
        'At a 500-ft corridor that is 62,500 sq ft = ~1.43 ac per wing, ~10.0 ac for seven wings. '
        '2.87 ac per wing is a triangle with 500-ft legs on the section lines, which is a corridor ~707 ft wide. '
        'Please confirm which one Bald Eagle engineering means, remap, and make 7(c), 13(b), 17(f), the map and the shapefiles agree. '
        'Report permanent and temporary acreage separately.')

R.edit(2, 'Desk redline of the Oct 29, 2026 EPS draft, Nov 21, 2026. Working copy for EPS; not part of the filing. Text matches the PDF form; checkbox items are listed in the transmittal email.')

# ---- Item 1 ----
R.edit(4, 'CHIP LLC, a Nevada limited liability company',
       'Applicant is CHIP LLC only (agreed Nov 6). Two names leave the applicant of record unclear for the authorization, bond and cost recovery. '
       'Item 3: use a CHIP LLC phone and a general mailbox rather than a personal email.')
R.delete_para(7, 'Moved to the first line of item 1.')

# ---- Item 2 ----
rep(12, "Appointed as the Applicant's agent under the Master Services Agreement dated July 20, 2026.",
    "Appointed as the Applicant's agent by letter of authorization (attached).",
    'Attach a short letter of authorization signed by CHIP LLC rather than citing the MSA (avoids disclosing the contract and any question whether CHIP LLC is a party to it).')

# ---- Item 7 ----
rep(14, 'medium-voltage collector lines,', '34.5 kV medium-voltage distribution lines,',
    '"Collector" is a generation-side term; state the voltage.')
rep(14, 'A use authorization is requested under 43 CFR Part 429; this application is filed on SF-299 in accordance with 43 CFR 429.10.',
    'A use authorization (easement) is requested under 43 CFR Part 429; this application is filed on SF-299 in accordance with 43 CFR 429.10. The crossings serve the CHIP industrial park\'s internal roads and utilities and do not depend on any off-site transmission facility.',
    'Names the instrument sought (confirm easement vs. license) and states the crossings\' own purpose.')
rep(15, 'medium-voltage collector lines (overhead or underground; both configurations are under evaluation);',
    '34.5 kV medium-voltage distribution lines (overhead or underground; the requested areas accommodate either);',
    'Reviewer will want one defined action. If overhead vs. underground stays open, the acreage and disturbance should reflect the larger case.')

rep(16, 'each designed as a road and utility corridor approximately 500 feet in total width.',
    'each designed as a road and utility corridor approximately [500] feet in total width.', GEOM)
rep(16, 'the fourth crossing (Corner Crossing 2 located in the northeast crossing), is limited to a single wing.',
    'the fourth crossing (Corner Crossing 2, [section corner]) is limited to a single wing.',
    'Identify Crossing 2 by section corner. Expect Reclamation to ask why the other three need two wings if one works at Crossing 2; a sentence on why would help.')
rep(16, 'The existing road will be graded, widened, and paved as necessary to provide safe and reliable access. Improvements may include vegetation clearing, earthwork, drainage improvements, placement of aggregate base material, and asphalt paving within the authorized footprint.',
    'Roads within each crossing would be constructed, or where a road already exists, improved, to provide safe and reliable access. Work may include vegetation clearing, earthwork, drainage improvements, placement of aggregate base material, and paving within the authorized footprint.',
    '"The existing road" has no antecedent now that Hart Lane is out of this application. If an existing road or two-track runs through a crossing, name it: prior disturbance helps the "minor and localized" test (Reclamation looks at ground disturbance on previously undisturbed land, 90 FR 2735).')
rep(16, 'approximately 2.87 acre each as mapped in the project GIS, approximately 20.1 acres in total;',
    'approximately [__] acres each, approximately [__] acres in total;', GEOM)
rep(16, 'Crossings of Reclamation facilities would be approximately perpendicular, with required vertical clearance; no lateral encroachment is proposed. The 500-foot configuration remains subject to confirmation against the engineering test fit.',
    'No Reclamation canal, lateral, or drain has been identified within a crossing; if one is encountered, it would be crossed approximately perpendicular, with required vertical clearance, and no lateral encroachment is proposed.',
    'Draft said both that facilities would be crossed and (17(c)) that none lie in a crossing. Please confirm against TCID/Newlands facility data at the final footprint, including the "excavated" NWI feature at Crossing 2. '
    'Test-fit caveat deleted: the filed application should state the request.')

rep(17, 'a term of a minimum of 25 years is requested. A term exceeding 25 years requires Truckee-Carson Irrigation District approval under 43 CFR 429.6(a); the District will be notified in any event.',
    'a term of 25 years, renewable, is requested.',
    '"Minimum of 25 years" is open-ended. Terms over 25 years need approval from a repayment-obligated water user organization (43 CFR 429.6(a)); at 25 years renewable that step does not arise. Notice to TCID is Reclamation\'s step and need not be volunteered.')

rep(20, 'not yet established; the construction start date, duration, and in-service date will be provided in future iterations of the Plan of Development.',
    'construction is anticipated to begin in [month, year] and to take approximately [__] months, subject to authorization.',
    'Give a target even if approximate. Earlier planning used February 2027; Cory to confirm.')
rep(20, 'A temporary permit or consent is requested', 'A temporary permit is requested',
    'Under Part 429 a "consent document" is for a Reclamation easement over non-Reclamation land; on Reclamation fee land the instrument is a permit.')
rep(20, 'In addition, a cultural survey would be required prior to construction, requiring a field work authorization.',
    'Cultural resources inventory would be completed before construction under a field work authorization obtained by the Applicant\'s qualified consultant.', None)

rep(21, 'work, staging, and access areas outside the requested boundary, principally on adjacent private land, requested as temporary short-term right-of-way area.',
    'construction staging and laydown would be on adjacent private land. [Temporary use of Reclamation land during construction, if any: __ acres, shown on the map.] Construction access would be [route and land status].',
    'Draft both put work areas on private land and requested an undefined temporary federal ROW. Size the permanent grant for the permanent road and utility template only; show any construction-only area on Reclamation land as temporary, with acres. '
    'Laydown and "planning allowance" inside a permanent grant make the footprint harder to defend as minimal. '
    'Also state how construction traffic reaches the crossings: if it uses the gravel road on Reclamation land (no recorded ROW), that use needs authorization (43 CFR 429.33), so request it here.')
rep(21, 'The $100 fee (43 CFR 429.16) will accompany the filed application. See attached Plan of Development and map.',
    'The $100 nonrefundable application fee accompanies this application. See attached map and project description.',
    'Item 10 should be checked "Attached", not "To be determined by agency". Recommend filing without the PPOD (map, shapefiles, short project description); see email.')

# ---- Item 12 ----
rep(23, 'Following formation of a Churchill County general improvement district for CHIP, the Applicant anticipates assigning the authorization to that district, subject to Reclamation approval.',
    'The Applicant may later request Reclamation approval to assign the authorization to a Churchill County general improvement district serving CHIP.',
    'Wording under review; hold for final.')
rep(23, 'to prepare and process this application and the accompanying Plan of Development,',
    'to prepare and process this application,', 'Conforms to filing without the PPOD.')
R.edit(26, '[CHIP LLC financial capability statement, or reference to attached documentation.]',
       'Cory to provide. Supplemental page also needs CHIP LLC formation documents, good standing certificate, authorizing resolution, and the 3% holder/affiliate disclosure; see email on item 4.')

# ---- Item 13 ----
rep(28, 'included the selected alternative consisting of corner crossings.',
    'included the proposed corner crossings (Alternative 1).',
    '"Selected" reads as a decision already made; "proposed".')
rep(30, 'Alternative 2 was not selected as creating a corridor across BOR land from east to west or north to south, may adversely affect the ability of BOR to use the remaining areas of the parcel. Acquisition or exchange would not meet the development schedule.',
    'Alternative 2 was not selected because a corridor across Reclamation land parallel to a section line would disturb more federal land and divide the remainder of each parcel, limiting Reclamation\'s use of it. Alternative 3 was not selected because acquisition or exchange of the intervening sections would require a separate land transaction with its own approvals and is not necessary to connect the parcels.',
    'Reasons tied to federal land and resources, not the developer\'s schedule. If you have Alternative 2 acreage, add it.')
rep(30, 'The selected configuration, a road and utility corridor approximately 500 feet wide crossing directly over each section corner, confines the permanent federal use for the crossings to approximately 20.1 acres; The configuration remains subject to confirmation against the engineering test fit; if additional width or a different configuration is required, the requested crossing areas will be revised before filing.',
    'The proposed configuration, a road and utility corridor approximately [500] feet wide crossing directly over each section corner, confines the permanent federal use to approximately [__] acres at the section corners. The width accommodates [__] travel lanes, shoulders and drainage, and separated utility alignments [basis from engineering cross-section].',
    'The "revised before filing" sentence cannot be in the filed text. Physical size is the first thing Reclamation weighs for this CX; the record shows the width going 200, 400, then 500 ft. Please add a one-line engineering basis (lanes, utility separations, clearances). ' + GEOM)

# ---- Item 14 ----
rep(34, 'No prior or pending authorization has been issued or applied for from the Bureau of Reclamation for this Project.',
    'None for this Project. [Existing authorized rights-of-way within or adjacent to the crossings: __.]',
    'Re-run the encumbrance check on the final geometry (earlier mapping showed existing authorized ROWs near Crossing 2). Optional: cite LBAO categorical exclusions for similar road and utility licenses near Fallon, verified against LBAO CEC lists.')

# ---- Item 15 ----
rep(36, 'Without an authorized crossing at each corner the parcels cannot be connected by road or utility line, and any future development cannot be built or operated.',
    'Without an authorized crossing at each corner the parcels cannot be connected by road or utility line.',
    'Deleted the clause on future development. It states that private development depends on the federal action, which works against the categorical exclusion and invites a connected-action argument.')
rep(36, '(a) Cost of proposal: to be provided when engineering is complete. (b) Cost of next best alternative: to be provided.',
    '(a) Cost of proposal: approximately $[__] for construction within the crossings. (b) Cost of next best alternative: approximately $[__], higher because of greater federal land area and road and utility length.',
    'A planning-level estimate is enough; "to be provided" twice reads as an incomplete application.')
rep(36, 'The road improvements will provide connectivity between project parcels and facilitate the installation, operation, and maintenance of project utilities, including electrical, communications, and related infrastructure.',
    'The crossings will provide connectivity between project parcels and facilitate the installation, operation, and maintenance of project utilities, including electrical, communications, and related infrastructure, while keeping Reclamation and TCID access unrestricted.',
    'Adds a benefit to the public land manager.')

# ---- Item 16 ----
rep(38, 'Future NEPA compliance, may evaluate impacts near the project area beyond the direct effects of the proposed action, including related infrastructure and facilities such as CHIP facilities, where appropriate. ', '',
    'Deleted. It invites review of the private CHIP facilities and signals the applicant expects more than a categorical exclusion. Scope is Reclamation\'s call.')

# ---- Item 17 ----
rep(42, 'National Hydrography Dataset and National Wetlands Inventory data show two unnamed ephemeral streams and three riverine features in Crossings 2 and 3;',
    'National Hydrography Dataset and National Wetlands Inventory data show [__] features in Crossings [__];',
    'Counts were taken at the smaller footprint. Re-run NHD/NWI on the final geometry and report by crossing; wetlands are an extraordinary-circumstances screen.')
rep(45, 'approximately 20.1 acres in the four crossings;', 'approximately [__] acres in the four crossings;', GEOM)
R.edit(46, '(g) Historic and archaeological resources: a Class I records search and a Class III cultural resources inventory of the crossing areas will be completed to support Reclamation\'s Section 106 review, including tribal consultation, and Indian Trust Assets will be reviewed, before construction.',
       'Section 106 applies to Reclamation\'s authorization regardless of NEPA level; "if required" made it sound optional and conflicted with 7(g).')

# ---- Item 18 ----
rep(48, 'and consultation under Section 7 of the Endangered Species Act may not be required based on findings.',
    'and the [date] species list identifies [__]; no effect on listed species or critical habitat is expected [attach IPaC list]. Ground and aerial raptor and eagle surveys of the project area have been completed [report, date]; pre-construction nest surveys would be conducted during the nesting season.',
    '"May not be required based on findings" is unsupported without the IPaC result. Cory confirmed raptor and eagle surveys are complete; please cite the report. Migratory birds and eagles are on the extraordinary-circumstances screen.')

# ---- Item 19 ----
rep(50, ' See Plan of Development, Sections 7 and 10.', '', 'Conforms to filing without the PPOD.')

# ---- Item 20 ----
R.edit(52, 'U.S. Department of the Interior, Bureau of Reclamation, Interior Region 10 (California-Great Basin), Lahontan Basin Area Office, Carson City, Nevada.',
       'Item 20 asks only where this application is filed. Removed the TCID "concurrent crossing application" (not needed at a 25-year term), the description of a separate transmission application, and the "stand-alone action" sentence, which draws attention to the question it answers. Any disclosure of other projects is under review; hold for final.')

for i, (txt, cms) in sorted(PENDING.items()):
    R.edit(i, txt, '\n\n'.join('(%d) %s' % (n + 1, c) for n, c in enumerate(cms)) if len(cms) > 1 else (cms[0] if cms else None))

R.save('work_sf299')
print(len(R.log), 'changes')
