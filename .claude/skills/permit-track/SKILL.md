---
name: permit-track
description: Track every federal, state and local authorization for CHIP, FMDP and Denim: agency, instrument, pathway, status, next action, statutory clocks, commitments owed to and by agencies, comment periods, and meetings. Use when the user asks where something stands, what is due, what an agency asked for, after any agency contact or filing, or for a status summary.
---

# Permit tracking

- The trackers are `projects/<p>/tracker.md`. They are State files: rewrite rows in place,
  present tense. History goes in the project log.
- On any event (filing, agency letter, meeting, comment period, counsel answer):
  1. Update the tracker row (status, next action, deadline).
  2. Record commitments in both directions with a date: what we owe the agency, what it
     owes us. Undated commitments get a courtesy follow-up date (3 days if on the critical
     path, otherwise 7).
  3. Start statutory clocks when triggered and note the trigger document: EA 1 year from
     the agency's determination, EIS 2 years from the NOI (42 U.S.C. 4336a(g),
     `A-usc-42-4336a`), or the Section 112 deadlines if the fee is paid.
  4. Log the event in `projects/<p>/log/`.
- **Status summary on request:** for each project, what moved, what is blocked and on
  whom, the next three actions, and the nearest deadline. Plain text, one screen.
- Meeting notes, transcripts and emails that feed the tracker are PRIVILEGED; the tracker
  row records the fact, not the privileged content, and points to its source.
