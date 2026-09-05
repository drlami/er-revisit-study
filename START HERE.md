# START HERE

**Study:** Unscheduled 72-hour return visits to the pediatric emergency department, Palestine Medical Complex, Ramallah
**Principal investigator:** Dr Lami Qurt
**This file last updated:** 2026-08-19 (evening)

This is the map of the folder. It tells you which document to use, and when. For the full history of decisions and the open questions, read `STATUS.md` next to this file.

---

## Where the study is right now

**Stage 4 of 10.** The protocol and all the tools are written. Nothing has been submitted and no data has been requested.

**The team is now named and the two big technical risks are closed.** The patient identifier is present and stable in the Hospital Information System, and the treating doctor's name can be hidden from the reviewers. The study is feasible as designed.

**What is left before the proposal can go in:** the **full names of Dr Waad and Dr Ainaa**, everyone's agreement on author order, and signatures. That is now the whole critical path.

| Person | Role |
|---|---|
| Dr Lami Qurt | Principal investigator, first author. Makes no judgements on any pair |
| Dr Samer Dahdoul | Senior author, and re-reads a random 80 pairs as a check |
| Dr Amani Salman | Reviewer 3 — decides the pairs where the two reviewers disagreed |
| Dr Waad | Reviewer 1 — all 400 pairs |
| Dr Ainaa | Reviewer 2 — all 400 pairs |

---

## The three folders

| Folder | What is in it |
|---|---|
| **STEPS** | The documents you actually use, numbered in the order you use them. Work through them one at a time. |
| **REFERENCE** | Documents you look things up in. You never work through these. |
| **source** | The text files the documents are built from, and the build scripts. You only open this folder when changing wording. |

---

## STEPS — work through these in order

### 01 - Team Briefing.docx
**Use it at:** the team meeting.
**What to do:** hand it round, confirm the five roles in the table it contains, agree author order, and have people sign. **Collect the full names of Dr Waad and Dr Ainaa** — they are needed for the submission.
**Note:** the workload is uneven and worth saying out loud. The two residents carry about 47 hours each; Dr Amani about 7; Dr Samer about 9.

### 02 - Protocol and Proposal (to Ministry of Health).docx
**Use it at:** the ethics submission, immediately after the meeting.
**What to do:** the co-investigators and the team table are **already filled in**. Add the two missing surnames, the date and the signature, then send it to the **Ministry of Health research office**. No Ministry template is required; this document is the submission.
**Still worth asking:** is there a faster route for research that only uses existing records?

### 03 - HIS Data Access Request (English + Arabic).docx
### 03 - HIS Access Letter, Dr Murad Barkan (Arabic).docx
**Use it at:** the same time as step 02, if permitted.
**What to do:** send to the **Department of Continuous Education** at the hospital, asking for access to the Hospital Information System data. **Ask whether this can run at the same time as the ethics submission** — if it can, send both now and save several weeks.
**Note:** the Arabic letter to Dr Murad Barkan is written by hand and has no text file behind it. Edit it directly in Word. The English + Arabic version is built from `source`, so edits there will be overwritten — see *Changing wording* below.

### 04 - IT Data Export Request.docx
**Use it at:** only **after** the ethics approval letter is in your hand. The IT department confirmed on 2026-08-17 that it will not export anything before approval.
**Already answered:** the patient identifier is present and stable across visits — confirmed 2026-08-19. That was the assumption the whole study rested on, and it is now closed.
**Still to ask, and these do not need approval:**
1. Roughly how many pediatric emergency visits fall between 1 January 2024 and 31 December 2025?
2. **How will the masked records reach the reviewers?** The document asks for the treating doctor's name to be replaced by an anonymous code. Will reviewers open a masked view in the Hospital Information System, or should the pairs be exported as documents with the name already removed?

### 05 - Reviewer Workbook.docx
**Use it at:** the chart review, after the data arrives.
**What to do:** give a copy to Dr Waad, Dr Ainaa, Dr Amani and Dr Samer. Each fills in Steps 1 to 10 once **per pair of visits**. Everyone reads Part A before their first pair — it now names who does what and explains why the treating doctor's name has been removed.

### 06 - Reviewer 1 Coding Sheet.xlsx
### 07 - Reviewer 2 Coding Sheet.xlsx
**Use it at:** the chart review, alongside the workbook.
**What to do:** sheet 06 is Dr Waad's, sheet 07 is Dr Ainaa's. Give each **only their own file**. They must never see each other's. That separation is the entire reason the agreement statistic means anything — if the two files are compared before Dr Amani has settled the disagreements, that part of the paper is lost.

### 08 - Analysis Plan.docx
**Use it at:** after the coding is finished.
**What to do:** follow it as written. It was deliberately written **before any data was seen**, and that is what makes the findings credible. If something genuinely has to change, record the change, the date and the reason in its section 9 — do not quietly edit it.

---

## REFERENCE — look things up, do not work through

| Document | What it is for |
|---|---|
| **Full Study Protocol.docx** | The complete protocol. The methods section of the paper comes from this. Longer and more detailed than the proposal you submit. |
| **Coding Manual.docx** | The rules behind the classification, with worked examples. This is the methods document for the ethics file and the manuscript. **Reviewers use the Workbook instead** — do not hand them both. |
| **Data Dictionary.docx** | Every variable, one by one. Use it when talking to the IT department or when setting up the analysis. |
| **Sample Reviewer Data (SYNTHETIC).docx** | Forty **invented** pairs with the agreement tables worked through, so the team can see the shape of the output before real data exists. **No real patients. Delete this once the real pilot is done.** |

---

## Changing wording

All the documents except the Arabic letter are built from text files in `source`. **Edit the text file, not the Word file** — otherwise your change is lost the next time anything is rebuilt.

```
cd source
python build_all.py
```

That rebuilds every document into its correct numbered place. To rebuild only one:

```
python build_all.py 05
python build_all.py workbook
```

**Close the file in Word first.** Word locks an open document and the rebuild for that one file will fail — the script says which one and carries on with the rest.

**If you have hand-edited a Word file**, say so before rebuilding, so the change can be copied back into the text file first. Otherwise the rebuild overwrites it.

---

## What is blocked, and on what

| Step | Waiting for |
|---|---|
| 02 Ethics submission | The two missing surnames, author order, signatures. Nothing else. |
| 03 HIS access | Can probably go now — ask whether it may run alongside the ethics submission |
| 04 Data export | Ethics approval letter. The two system questions do not have to wait. |
| 05 to 08 | The data |

**One check is still outstanding before any of this:** ask colleagues in the emergency department and in pediatrics whether anyone is already doing this study. The thesis repositories and the Ministry research office have both been checked and are clear, but neither of them can see work in progress in your own department — and that is exactly what caught the previous project.
