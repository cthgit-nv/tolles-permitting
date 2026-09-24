# Tolles Permitting Desk

A Claude Code workspace that researches, analyzes, edits, red-teams and tracks NEPA and
related permitting for:

- **CHIP** (Hazen, Churchill County): Application 1, Reclamation corner crossings and the Hart Lane road
- **FMDP** (Hazen): Application 2, BLM transmission lines and access roads
- **Project Denim** (Jean, Clark County): BLM substation, transmission lines, access road, fiber

**Private repository. Contains PRIVILEGED material.** See `CLAUDE.md` for the rules.

## Using it

Open Claude Code in this folder on the Mac (so it can reach the local Dropbox folder)
and talk normally:

- "Here's the new Reclamation PPOD from EPS. Conform it to the brain and red-team it."
- "Is Save Our Sonoran still good law after Seven County?"
- "What would opposing counsel say about splitting Application 1 and 2?"
- "Where does Denim stand?"
- "Lint the library and give me the KeyCite list for Holland & Hart."

The `permitting-desk` skill routes each request to the right sub-skill.

## Layout

```
library/        the law: authorities, propositions, research log, source text, watchlist
projects/       one brain per project: index, facts, decisions, questions, tracker, log,
                redteam, privileged, drafts
decisions/      decisions that apply to every project
evals/          gold questions, calibration log, red-team canaries
tools/          verify_library.py, check_outward.py (standard library only)
.claude/        skills and subagents
```

## Checks

```bash
python3 tools/verify_library.py            # library integrity, quotes vs sources
python3 tools/verify_library.py --keycite-list
python3 tools/check_outward.py <file> --project chip
python3 -m unittest discover -s tools/tests
```
