import sys
sys.path.insert(0, '.')
from redline_lib import Redliner

R = Redliner('work/word/document.xml')
T = R.text

SCOPE = 'Tolles decision 9/25: Application 1 covers the four corner crossings and the Hart Lane access road segment only. Switching-station / transmission corridor removed from this application.'
ACRES = 'Tolles decision 9/25: 400-ft ROW straight over each corner (four-lane road plus the 34.5 kV lines and utilities). Each wing: legs ~283 ft on the section lines, outer face ~400 ft, ~0.92 ac; 7 wings = ~6.43 ac. Computed from BLM CadNSDI section corners (desk KMZ 2026-09-25); each wing stays within the aliquot listed in Table 1. EPS/civil: confirm and remap.'
ROAD = 'Tolles 9/25: the Hart Lane road is a three-lane road following the existing gravel road on Reclamation land, ending at the CHIP property line, then running around the site perimeter on private land. Desk KMZ candidate alignment: straight southward continuation of the mapped county centerline of Hart Lane to the north line of Sec. 3, T.19N., ~2,650 ft (~2,620 ft on Reclamation land in Sec. 34, T.20N.). The gravel road is shown as a historical county road; no recorded county right-of-way. Confirm alignment and ROW width (80 ft assumed = ~4.8 ac).'
EO = 'Tolles decision 9/25: remove the EO 14318 Qualifying Project request. It presents the data center as the reason for the crossings, which cuts against the categorical exclusion (prong (b)) and the independent-purpose framing. May be raised orally at pre-application.'
FMDP = ('Tolles decision 9/25: remove description of the separate transmission application. Application 1 stands on its own purpose. '
        'Option for Tolles/counsel: if a disclosure line is wanted, suggested neutral text: "A separately proposed transmission and access project in the region will be the subject of its own applications and environmental review; it is not required for, and does not require, the facilities described in this PPOD."')

APP = 'Tolles decision 9/25: applicant of record is CHIP LLC, a Nevada limited liability company, the landowner and developer of the CHIP parcels connected by the crossings. A landowner connecting its own parcels also reinforces the independent purpose of the crossings.'

def rep(i, old, new, comment=None):
    t = T(i)
    assert old in t, (i, old, t[:120])
    R.edit(i, t.replace(old, new), comment)

# ---- Section 1 Introduction ----
rep(205, 'filed with the Reclamation', 'being submitted to the Reclamation', 'Neither application has been filed yet.')
R.edit(206, 'This PPOD and the accompanying SF-299 address four corner crossings and an access road segment on Reclamation-administered land, described in Section 1.1. A separately proposed transmission and access project in the region will be the subject of its own applications and environmental review; it is not required for, and does not require, the facilities described in this PPOD.', 'Tolles 9/25: include the neutral disclosure sentence for now. FLAG FOR COUNSEL: confirm whether to keep this sentence or omit any reference to the separate project. Prior text describing the transmission application as connected-action context was deleted per the Stantec NEPA planner and Tolles decision.')

# ---- 1.1 Project Description ----
rep(219, 'The four crossings comprise seven wings and occupy approximately 3.57 acres in total, on land administered by Reclamation as part of the Newlands Project.',
    'The four crossings comprise seven wings and occupy approximately 6.4 acres in total at the 400-foot design standard (Section 3), on land administered by Reclamation as part of the Newlands Project. The Project also includes an access road segment of approximately 2,650 feet on Reclamation-administered land that improves an existing gravel road on the Hart Lane alignment, described below.', ACRES)
t = T(220)
eo_sent = t[t.index(' The CHIP development served by these facilities'):]
R.edit(220, t.replace(eo_sent, '').replace('medium-voltage collector lines, water', 'medium-voltage collector lines (anticipated to operate at 34.5 kV), water'), EO)
rep(222, 'A permanent use authorization is requested for the corner crossings.', 'A permanent use authorization is requested for the corner crossings and the access road segment.', ROAD)
R.edit(223, 'Hart Lane access road segment. The Project includes an access road segment of approximately 2,650 feet on Reclamation-administered land in Sec. 34, T.20N., R.26E., continuing Hart Lane south from its current mapped end to the north line of Sec. 3, T.19N., R.26E., at the CHIP property line. The segment follows an existing gravel road that has been in use for many years and is shown as a historical county road; no recorded county right-of-way has been identified. The proposed improvement would pave and improve the existing alignment as a three-lane road within a road corridor of [INSERT: road right-of-way width] feet, so that most of the associated ground disturbance would occur on previously disturbed land. At the CHIP property line the road would continue on private land around the perimeter of the development and would not occupy additional Reclamation-administered land. Construction use of the existing gravel road prior to its improvement is also requested under this authorization, to the extent it is not already covered by an existing public right-of-way. [INSERT: confirmed alignment, legal description, and acreage on Reclamation-administered land].', SCOPE + '\n' + ROAD)
rep(224, 'The industrial, data center, generation, and storage facilities located on private land are not proposed as components of this PPOD and are not the subject of the requested federal authorization.',
    'The crossings and the access road segment serve the CHIP industrial park as a whole, including its internal roads, water, wastewater, communications, and on-site power distribution from generation and storage facilities within the park, and do not depend on any off-site transmission facility. The industrial, commercial, generation, and storage facilities located on private land are separately proposed, are outside Reclamation\'s authority to approve, and are not the subject of the requested federal authorization; any federal permits those facilities require would be subject to their own review.',
    'States the independent purpose of the crossings and road (park-wide access and utilities; power from on-site generation and storage). Replaces the prior statement that private facilities "require no federal construction approval," which is not certain (e.g., CWA, FAA) and invited contradiction.')
R.delete_para(225, FMDP)
t = T(227)
a1 = 'Tolles Development is anticipated to construct, own, operate, and maintain the Project.'
b1 = 'CHIP LLC, the landowner and developer of the CHIP parcels, is anticipated to construct, own, operate, and maintain the Project.'
a2 = t[t.index('[INSERT: confirm the applicant of record'):]
b2 = ''
assert a1 in t
R.edit(227, t.replace(a1, b1).replace(a2, b2), APP)
rep(124, 'Tolles Development', 'CHIP LLC', APP)
R.insert_after(15, 'CHIP LLC', APP, like=17)
rep(204, 'Tolles Development (Applicant)', 'CHIP LLC, a Nevada limited liability company (Applicant),', APP)
rep(574, ', and whether the authorization should be applied for by the Applicant or by Churchill County]', ']', APP)

# ---- Section 2 Purpose and Need ----
R.edit(233, 'The proposed butterfly configuration was selected because it confines the federal land use at each section corner to a small, discrete area and produces a crossing of Reclamation land rather than a longitudinal use of it. The access road segment improves an existing road alignment rather than creating a new corridor on Reclamation land. Consistent with Reclamation policy that lateral encroachments along Reclamation facility rights-of-way are not authorized, the Project crosses Reclamation-administered land at defined points and does not parallel or occupy any Newlands Project facility right-of-way. No Newlands Project canal, lateral, or drain has been identified within or adjacent to the proposed crossings or the access road segment in the screening performed to date [INSERT: confirm TCID facility locations from the land-status review and TCID records, including whether the excavated riverine feature mapped in Corner Crossing 2 (Section 8.2.6) is a Newlands Project facility].',
       'Transmission-corridor and railroad-corridor references removed with the corridor. Adds the road segment, which is on an existing alignment. Flags the NWI "excavated" feature in Crossing 2, which could be a drain and would contradict the "no facility" statements.')
t = T(234)
R.edit(234, t.replace('acquiring or exchanging federal land, which would not meet the development schedule;', 'acquiring or exchanging federal land, which would require a separate land-tenure action for a use that a use authorization can accommodate; constructing a new road alignment rather than improving the existing gravel road, which would create new disturbance on undisturbed land;').replace('The selected 200-foot corridor configuration', 'The selected 400-foot corridor configuration'), 'Replaces a schedule-based reason (ties the purpose to the private development timeline) with a land-use reason, adds the road alternative, and updates the corridor width to 400 ft.')
R.delete_para(236, EO)

# ---- Section 3 ROW Location ----
R.insert_after(244, 'Access road segment, on Reclamation-administered land in Sec. 34, T.20N., R.26E., from the current mapped end of Hart Lane (approximately 39.55520 N, 119.05261 W) south to the north line of Sec. 3, T.19N., R.26E. (approximately 39.54793 N, 119.05280 W) [INSERT: confirm endpoints].', ROAD, like=244)
t = T(245)
a1='with a wing on each side of the corner. As mapped in the project GIS, each wing is approximately 0.51 acre, and the four crossings total approximately 3.57 acres.'
b1='with a wing on each side of the corner (a single wing at Corner Crossing 2). At that standard each wing has legs of approximately 283 feet along the section lines and an outer face of approximately 400 feet, for approximately 0.92 acre per wing and approximately 6.4 acres for the seven wings [INSERT: confirm against the remapped project GIS]. Roads within the crossings are anticipated to be four-lane roads.'
a2='improved roadway.single wing of approximately 0.51 acre located entirely'
b2='improved roadway. Corner Crossing 2 is a single wing of approximately 0.92 acre located entirely'
assert a1 in t and a2 in t
R.edit(245, t.replace(a1,b1).replace(a2,b2).replace('approximately 200 feet in total width','approximately 400 feet in total width'), ACRES)
rep(246, 'the surface area of the seven wings together with the roads, collector lines, and other utility lines installed within them.', 'the surface area of the seven wings together with the roads, collector lines, and other utility lines installed within them, and the access road segment described in Section 1.1.')

# ---- Table 1 ----
rep(309, 'Transmission Easement', 'Hart Lane Access Road Segment', SCOPE)
rep(310, 'T.19N., R.26E.', 'T.20N., R.26E.')
rep(311, '2', '34')
rep(312, 'Lot 4', 'NE¼SW¼, SE¼SW¼, NW¼SE¼, SW¼SE¼ [INSERT: confirm against final alignment]')
R.delete_row(R.row_of(316))
R.delete_row(R.row_of(320))

# ---- Section 4 Facility Design ----
rep(330, 'narrow surface corridors across Reclamation-administered land at four section corners.', 'narrow surface corridors across Reclamation-administered land at four section corners and an improved access road segment on an existing road alignment.')
R.insert_after(331, 'Hart Lane access road segment. Three-lane paved road [INSERT: typical section, travel-way width, shoulders, right-of-way width, and drainage]. The segment would be built on the existing gravel road alignment and would be designed to Churchill County road standards for its connection to Hart Lane.', ROAD, like=331)
rep(332, 'Collector lines. If installed overhead,', 'Collector lines. Medium-voltage collector lines are anticipated to operate at 34.5 kV [INSERT: confirm]. If installed overhead,')
rep(336, 'No Newlands Project canal, lateral drain, or operating road lies within or adjacent to a corner crossing.', 'No Newlands Project canal, lateral, drain, or operating road has been identified within or adjacent to a corner crossing [INSERT: confirm with TCID records and field check; see Section 8.2.6].')

# ---- Table 2 ----
for i in (348, 356, 360):
    rep(i, 'Approximately 1.02 acres', 'Approximately 1.84 acres', ACRES if i == 348 else None)
rep(352, 'Approximately 0.51 acre', 'Approximately 0.92 acre')
rep(382, 'Transmission Corridor', 'Access Road Segment', SCOPE)
rep(383, 'Transmission corridor', 'Hart Lane access road segment')
R.edit(384, 'Sec. 34, T.20N., R.26E., MDM; Reclamation-administered land between the current end of Hart Lane and the north line of Sec. 3, T.19N., R.26E.')
R.edit(385, 'Paving and improvement of approximately 2,650 feet of an existing gravel road as a three-lane road; no new alignment on Reclamation land [INSERT: right-of-way width and typical section]')
R.edit(386, '[INSERT: acreage on Reclamation-administered land]')

# ---- Tables 3 and 4 ----
rep(406, 'Temporary', 'Permanent', 'Header typo: this is the permanent disturbance table.')
rep(415, 'Approximately 3.57 acres', 'Approximately 6.4 acres [INSERT: confirm against remapped KMZ]', ACRES)
rep(431, 'Transmission corridor', 'Hart Lane access road segment', SCOPE)
R.edit(432, 'Approximately 2,650 feet on the existing gravel road alignment [INSERT: width]')
R.edit(453, 'Within the crossing authorization boundaries (approximately 0.92 acre per wing); not additive to Table 3', 'Avoids double counting the wings as both permanent and temporary disturbance.')
R.edit(459, 'Anticipated on private land outside the authorization boundary')
rep(464, 'Transmission corridor construction areas', 'Hart Lane access road construction work area', SCOPE)
R.edit(465, '[INSERT: width and length of temporary work area along the existing road]')

# ---- Section 5 ----
rep(490, 'are Churchill County roads, not Reclamation or TCID operating roads [INSERT: confirm county road status and any required Churchill County actions]',
    'are shown on the Churchill County road inventory and are not Reclamation or TCID operating roads [INSERT: confirm whether a county right-of-way exists across Reclamation-administered land and any required Churchill County actions]',
    'An inventory listing does not by itself create a right-of-way across Reclamation land. Construction use without authorization risks unauthorized-use charges under 43 C.F.R. 429.33.')
rep(496, 'Existing unpaved roads that may be used or improved for construction and maintenance access;', 'Existing unpaved roads that may be used or improved for construction and maintenance access, including the existing gravel road on the Hart Lane alignment, shown as a historical county road with no recorded county right-of-way, that is proposed for improvement under this authorization (Section 1.1);', ROAD)
rep(507, 'Reclamation has advised that precise, minimized footprints materially improve the case for a categorical exclusion, and the Applicant does not propose', 'The Applicant does not propose',
    'No pre-application meeting has occurred, so there is no record of Reclamation advising this. Removed.')

# ---- Section 6 ----
rep(510, 'The Regional Director, acting through LBAO Land Resources and Realty staff, issues the authorization.', 'The authorization would be issued by Reclamation through LBAO.', 'No source for the delegation statement; softened.')
rep(518, ' — ', ', ')
rep(520, '(43 C.F.R. 429.17; 43 U.S.C. 397a)', '(43 C.F.R. 429.17 to 429.19)', '43 U.S.C. 397a covers advances for operation and maintenance of projects, not applicant cost recovery. Part 429 is the authority.')
R.delete_para(529, FMDP)
rep(536, '(the corner crossings and, when added, the transmission corridor)', '(the corner crossings and the access road segment)')
rep(564, 'Reclamtion', 'Reclamation')
t = T(566)
s961 = t[t.index(' Facility-specific right-of-way statutes also apply'):]
R.edit(566, t.replace(s961, ''), '43 U.S.C. 961 is not in Part 429\'s authority line, carries a 50-year cap, and frames the Project as a transmission right-of-way. Part 429 is sufficient.')
rep(567, 'under 43 C.F.R. 429.17 and 43 U.S.C. 397a and,', 'under 43 C.F.R. 429.17 to 429.19 and,')
R.edit(576, 'Reclamation selects the level of NEPA review. The Applicant requests that Reclamation consider a categorical exclusion. Reclamation maintains a categorical exclusion for the issuance or renewal of use authorizations (as defined in 43 C.F.R. 429.2, including crossing agreements which provide rights-of-way) that authorize use of Reclamation land, facilities, or waterbodies where one or more enumerated conditions apply, including where impacts of the action are expected to be minor and localized (DOI NEPA Handbook, Appendix 2, 14.5(D)(8); formerly 516 DM 14, revised effective January 13, 2025). In revising that exclusion, Reclamation identified physical size, surrounding land use, and the extent of potential ground disturbance on previously undisturbed land as the considerations for a minor-and-localized determination (90 Fed. Reg. 2735). The corner crossings total approximately 6.4 acres of discrete areas at section corners, and the access road segment improves approximately 2,650 feet of an existing gravel road, so that new disturbance on previously undisturbed land is limited [INSERT: permanent disturbance acreage, and the previously disturbed and undisturbed split, from Tables 3 and 4].',
       'Aligns the CX argument with the actual scope (crossings plus road) and with the three factors Reclamation named in its 2025 revision. Citation format follows the Handbook.')
R.edit(577, 'Even where a categorical exclusion applies, it is not used where an extraordinary circumstance listed at 43 C.F.R. 46.215 is present. The Applicant proposes to complete the resource clearances described in Section 8 in advance so that Reclamation can document its review of each circumstance at 46.215(a) through (i) on a complete record. In the Newlands setting, cultural resources, wetlands and floodplains, and migratory birds are the principal resource considerations; Reclamation\'s Indian Trust Assets assessment is addressed in Section 6.6. The crossings and the access road segment provide access and utility connectivity within the CHIP industrial park, and their approval would not commit Reclamation to any other action.',
       'Indian Trust Assets are a Reclamation policy requirement, not a listed 46.215 circumstance. Adds the facts Reclamation needs for 46.215(d) and (e) without referring to other projects.')
R.delete_para(578, EO)
rep(579, 'one-year statutory target', 'one-year statutory deadline')
rep(582, 'An Indian Trust Assets assessment is a mandatory, Reclamation-specific element of the environmental review and a potential extraordinary circumstance.', 'An Indian Trust Assets assessment is a mandatory, Reclamation-specific element of the environmental review.')

# ---- Section 7 ----
rep(584, 'Construction within the corner crossings would include', 'Construction within the corner crossings and along the access road segment would include')
rep(587, 'would be limited to the four corner crossings,', 'would be limited to the four corner crossings, the access road segment,')
t = T(589)
R.edit(589, t.replace('four butterfly corner crossings totaling approximately 3.57 acres,', 'four corner crossings (seven wings) totaling approximately 6.4 acres and an access road segment of approximately 2,650 feet on an existing gravel road alignment,').replace(' The transmission corridor described in Section 1.1 comprises approximately 90.07 acres of Reclamation-administered land, as shown in Table 1.', ''), SCOPE)
rep(613, 'Anticipated working hours and days] are 8-10 hours per week, Monday-Friday.', 'Anticipated working hours are 8 to 10 hours per day, Monday through Friday [INSERT: confirm].')
rep(660, 'collector-line and pipeline alignments', 'collector-line and utility-line alignments', 'Gas pipeline is excluded; conforming leftover references.')
rep(666, 'collector-line and pipeline installation', 'collector-line and utility-line installation')
rep(686, ' — ', ', ')

# ---- Section 8 ----
rep(729, 'The evaluation covers the four corner crossings, the facilities carried within them, and the associated temporary work areas.', 'The evaluation covers the four corner crossings, the facilities carried within them, the access road segment, and the associated temporary work areas.')
rep(732, 'consistent with Reclamation policy that lateral encroachments on Reclamation land are not authorized.', 'consistent with Reclamation policy that lateral encroachments along Reclamation facility rights-of-way are not authorized. The access road segment improves an existing gravel road alignment.')
rep(733, 'Three existing authorized rights of way have been identified within the Project.', 'Four existing authorized rights-of-way have been identified within the Project [INSERT: re-verify locations against the remapped Corner Crossing 2 geometry].', 'The paragraph lists four serial numbers; three were located in Crossing 2 before it was moved into Lot 1.')
rep(750, 'No Newlands Project conveyances lie within a proposed corner crossing.', 'No Newlands Project conveyances have been identified within a proposed corner crossing [INSERT: confirm whether the excavated feature (R4SBCx) in Corner Crossing 2 is a Newlands Project facility].')
rep(756, 'limited to the corner crossings, the facilities within them,', 'limited to the corner crossings, the facilities within them, the access road segment,')
rep(760, 'and are not anticipated to delay the start of construction [INSERT: confirm the anticipated construction start date and survey schedule].', 'and survey timing would be coordinated with the construction schedule.',
    'Removes an assurance on schedule. Raptor nesting begins in late winter; outward documents should not commit to no delay.')
rep(768, 'is a mandatory element of Reclamation\'s environmental review and a potential extraordinary circumstance under 43 C.F.R. 46.215.', 'is a mandatory element of Reclamation\'s environmental review.', 'Indian Trust Assets are not a listed 46.215 circumstance.')

# ---- Section 10 ----
rep(778, ' and applicable pipeline design code, if a pipeline is included,', '')
rep(785, 'collector-line and pipeline condition', 'collector-line and utility-line condition')
rep(793, 'use the authorized roads within the corner crossings', 'use the authorized roads within the corner crossings and the access road segment')

# ---- References ----
rep(812, '(effective April 11, 2025).', '(effective April 11, 2025); adopted as final, 91 Fed. Reg. 618 (Jan. 8, 2026).')
R.delete_para(813, EO)
rep(815, '145 S. Ct. 1497 (2025)', '605 U.S. 168 (2025)')
R.delete_para(823, 'Internal strategy memorandum; should not be cited in the application record.')

TERM = 'Tolles 9/25: request a 25-year term, renewable, so that the TCID approval required by 43 C.F.R. 429.6(a) for terms over 25 years is not triggered. TCID is still notified (429.6(b)), and Reclamation may request TCID concurrence (429.6(c)). Trade-off: renewal is at Reclamation discretion.'

rep(568, 'The Applicant requests a term of a minimum of 25 years. The Applicant acknowledges that an easement or right-of-way granted for a term exceeding 25 years requires the approval of TCID under 43 C.F.R. 429.6(a), and that TCID will be notified of the authorization in any event.', 'The Applicant requests a term of 25 years, with the right to apply for renewal. TCID will be notified of the proposed use authorization under 43 C.F.R. 429.6(b).', TERM)
t = T(571)
R.edit(571, t.replace(', and TCID approval would be required for an easement or right-of-way granted for a term exceeding 25 years', ''), TERM)
t = T(563)
R.edit(563, 'Notice of the proposed Reclamation use authorization (43 C.F.R. 429.6(b)); district approval under 43 C.F.R. 429.6(a) applies only to terms exceeding 25 years and is not required for the requested 25-year term', TERM)
rep(586, 'This will include anticipated construction start date, construction duration, and in-service date.', 'Construction is anticipated to begin in February 2027, subject to issuance of the authorization and completion of pre-construction surveys and clearances [INSERT: construction duration and in-service date].', 'Tolles 9/25: February 2027 target. Note: a February start requires the CX, Section 106 consultation and surveys to be complete within about four months of filing, and falls at the start of raptor nesting season.')

R.save('work')
print(len(R.log), 'operations;', len(R.comments), 'comments')
