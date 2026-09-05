# Pediatric ED 72-Hour Revisit Study — PMC Ramallah

Unscheduled 72-hour return visits to the pediatric emergency department of a
Palestinian governmental hospital: rate, reasons, and predictors.

**Site:** Palestine Medical Complex (PMC), Ramallah — Palestinian MoH governmental hospital
**PI:** Dr Lami Qurt
**Design:** retrospective records-only cohort, children under 13, proposed period 1 Jan 2024 – 31 Dec 2025

Private repository. It names the study team and holds an unsubmitted protocol and
ethics proposal — keep it private.

**No patient data is in this repository, and none should ever be committed here.**
Every spreadsheet is generated synthetic data and is labeled FAKE DATA or SYNTHETIC in
its filename. When the real export arrives it goes somewhere access-controlled, not
into git.

## Start here

- **`STATUS.md`** — the authoritative record: stage 3 of 10, what changed on which date,
  team, next actions, open decisions. Read this first.
- **`START HERE.md`** — the orientation document for the team.

## Layout

```
source/                  the sources of truth — edit these, never the .docx
  *.md                   protocol, ethics proposal, coding manual, data dictionary,
                         analysis plan, reviewer workbook, team briefing, access requests
  build_all.py           rebuilds every document into its numbered location
  build_docx.py          markdown -> .docx (one file)
  make_xlsx.py           the two blank reviewer coding sheets
  make_fake_data.py      the pre-filled synthetic practice copies
  make_sample.py         synthetic sample reviewer data
  compare_reviewers.py   agreement statistics between the two coding sheets

STEPS/                   generated — the numbered documents the team actually uses
REFERENCE/               generated — samples and pre-filled practice sheets (FAKE DATA)
```

`STEPS/` and `REFERENCE/` are **build output**. The `.md` files in `source/` are the
originals; a document edited only in Word is lost at the next rebuild.

## Rebuilding

Requires Python 3 with `python-docx` and `openpyxl`.

```bash
cd source
python build_all.py            # everything
python build_all.py 05         # one step
python build_all.py workbook   # or match part of the name
```

Paths resolve from `source/`'s own location, so the repo can be cloned anywhere.
Close Word and Excel first — an open file fails that one build with a clear message
and the rest still finish.

**Before rebuilding, check whether the .docx has been hand-edited.** It has happened
before: `source/Protocol _ Proposal (hand-edited 2026-08-17 backup).docx` is the
surviving copy of one such round. Build to a temporary path and diff first, then fold
the change into the `.md` rather than the `.docx`.

## Critical path

Stage 4 — **team agreement and authorship**. The MoH proposal is complete except for
the co-investigator names; Reviewer 1 and Reviewer 2 are recorded as "Dr Waad" and
"Dr Ainaa" with full names still needed. The multi-week ethics wait cannot start until
those blanks are filled, and stages 6 through 10 are blocked behind ethics approval.

Two questions can be asked of IT now, before approval, because they ask how the system
behaves rather than for any patient data: whether the patient identifier is stable for
the same child across visits — the single assumption the whole design rests on — and
the rough pediatric ED visit count for the study period.

See `STATUS.md` § NEXT ACTIONS for the full list.
