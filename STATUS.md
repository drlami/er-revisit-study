# Project Status

**Study:** Unscheduled 72-hour return visits to the pediatric emergency department of a Palestinian governmental hospital: rate, reasons, and predictors
**Site:** Palestine Medical Complex (PMC), Ramallah — Palestinian MoH governmental hospital, serving as a first-contact hospital for its catchment as well as receiving referrals
**PI:** Dr Lami Qurt
**Last updated:** 2026-08-20

---

## Where we are

**Stage 3 of 10 complete.** Topic selected after a verified literature gap search; protocol and tools drafted. Nothing submitted, no data requested yet.

| # | Stage | Status |
|---|-------|--------|
| 1 | Topic selection | ✅ Done — locked 2026-08-16 |
| 2 | Literature gap search | ✅ Done — PubMed, 2026-08-16 (see PROTOCOL.md §2) |
| 3 | Protocol + tools | ✅ Draft complete |
| 4 | Team agreement + authorship | 🟡 **Now the critical path** — the proposal cannot be submitted without co-investigator names |
| 5 | Ethics — via MoH research office | 🟡 Proposal complete and in .docx. **No MoH template required.** Waiting only on names |
| 6 | IT data export request | ⬜ Blocked — **IT will not export before ethics approval**. The two system questions can still be asked now |
| 7 | Pilot classification (40 of the 400-pair sample) | ⬜ Blocked on ethics — **but the instruments are now finished and ready to use** |
| 8 | Classification of 400 sampled pairs + analysis | ⬜ Blocked |
| 9 | Manuscript (STROBE) | ⬜ Blocked |
| 10 | Journal selection + submission | ⬜ Blocked |

## What happened on 2026-08-20 (pilot stopping rules written)

`ANALYSIS-PLAN.md` gained **§4b — Pilot stopping rules**, and the plan went to **version 0.2**. This closes the last item that was agreed in principle but never written down, and it had to be closed *before* the pilot runs: a threshold chosen after seeing the kappa is not a threshold.

Five rules, all pre-specified:

1. **Agreement thresholds, judgement by judgement** — three bands each (proceed / clarify the workbook / do not use as a primary finding). The bar deliberately differs per judgement: eligibility 0.70, relatedness 0.60, attribution 0.55, preventability 0.50, and access barrier judged on raw agreement plus PABAK rather than kappa because the "yes" category is rare and the table is skewed. Holding preventability to 0.60 would fail an instrument behaving normally.
2. **The uncertain ceiling** — 10% or less is normal, 11–20% means clarify, above 20% means the rule is rewritten or the judgement drops to descriptive. No published benchmark exists; 20% is the team's own number, recorded in advance as such.
3. **Minutes per pair** — captured by a per-sitting log, not a new column in the sheet. 10 minutes or less proceeds with 400 (about 67 hours per reviewer); 11–15 proceeds but the timeline is extended before the run starts; above 15 the sample shrinks, with a floor of 250 pairs.
4. **Only rule-ambiguity disagreements may change the workbook.** Each disagreement is assigned to pile (a) *the workbook did not say* or pile (b) *the reviewers weighed the same facts differently* — **before** the correct answer is discussed, so a genuine judgement difference cannot be retrospectively reclassified as a wording problem. Only pile (a) changes anything. Rewriting rules until two reviewers cannot disagree produces one reviewer with two names, and a kappa that means nothing.
5. **A one-page dated pilot report** filed before the main run, which becomes the instrument-development paragraph in the methods.

Two points made explicit that were previously only implied. **No pilot result can stop the study** — the primary outcome comes from the complete export and does not depend on classification at all; the rules decide only what each classification judgement may be used for. And **a 40-pair kappa near 0.60 carries a 95% interval of roughly ±0.20**, so where the interval straddles a threshold the PI decides and records the reason, rather than treating a point estimate as a verdict.

Also noted while writing it: **§4 does not currently ask for PABAK or raw agreement beside kappa**, though this file has called for all three since 2026-08-19. §4b requires all three for the pilot; §4 should be brought into line before the main analysis.

---

## What happened on 2026-08-19 (Basis becomes a pointer — options 1+2+3)

The PI reported that documenting in the spreadsheet was error-prone: answering Step 6 meant going back to R-1 and R-2, Step 7 meant going back to I-2, and the travelling itself caused mistakes. Measurement confirmed it — the sheet was **4.5 screens wide**, with **Step 7's Basis sitting 14 columns (2.5 screens) from I-2**.

**The real cause was a design error, not the width.** The Basis asked reviewers to **retype data they had already entered** — Step 9 said outright *"copy the words from R-3 or R-4"*, when those words were already in the sheet. That is double transcription: two chances to differ, and no way for the analysis to tell which copy is authoritative.

Three changes were made together.

**1. Basis is now a pointer, not a copy.** Each judgement names **which field** drove it, chosen from a **dropdown** — the code is never typed, so it cannot be mistyped (which is how the I-9 error appeared in the first place). Nothing is transcribed twice; the analysis links to the field through the pointer.

**2. A frozen read-only context column.** New column C fills itself by formula and, with freeze panes moved to D3, **stays on screen however far right the reviewer scrolls**. It shows I-2, I-3, R-2, whether R-3 has anything in it, and the first 24 characters of R-1. Backward scrolling is now unnecessary.

**3. Only two judgements keep a written reason.** **Step 3 and Step 7** — the locked index judgement and the attribution — keep field *plus* one short line. **Steps 6, 8 and 9 are pointer only.** Relatedness is rarely contested, Step 8's reasoning overlaps almost entirely with Step 7's, and Step 9's quote already exists in R-3/R-4. **Free-text Basis cells: five, now two.**

### Honest accounting on width

The sheet went from 28 to **31 columns** and from 534 to **554 characters** — slightly *wider*, not narrower. **Width was never the right measure.** Filling a form left to right is natural; what caused errors was travelling *backwards*, and that is now zero. The frozen context column costs 42 characters of permanent screen space and buys the elimination of every backward scroll.

### Everything realigned

`REVIEWER-WORKBOOK.md` Part A rule 2, the field legend, Steps 3 and 6 to 9, and the **Part D worked example** were all rewritten to the pointer model — otherwise the workbook and the sheet would have contradicted each other. Both instruction tabs, **English and Arabic**, now carry 8 numbered rules including two new ones: never copy a field's contents into a reason, and column C fills itself. Workbook is **version 0.4**.

Verified after rebuild: 31 columns, 19 dropdowns, 19 conditional-formatting ranges, both instruction tabs matching.

---

## What happened on 2026-08-19 (clarity pass on the workbook — and a real bug found)

The PI reported that the workbook's questions were not self-explanatory, giving Step 3's *Basis* and *initials* as the example. A full pass found the problem was systematic, plus one genuine bug.

### The bug

The coding sheets instructed reviewers to write a Basis like **"I-9 no hip examination documented". There is no I-9** — the workbook only defines I-1 to I-4. The instruction was unfollowable, and it had been faithfully translated into the Arabic tab that morning. Fixed in both.

Worse, **the Excel columns carried no field numbers at all**, so the field number a Basis cell demanded appeared nowhere in the file the reviewer was working in.

### The pattern behind the vagueness

Every unclear spot had the same shape: **the rule was explained once, far away, and never repeated where it was used.** *Basis* appears five times; it was defined only in Part A rule 2, roughly forty lines before first use, with a single example.

### What changed

- **New "Field numbers" legend** in the workbook and on both instruction sheets (English and Arabic). The eight fields I-1–I-4 and R-1–R-4 are now visible where they are needed.
- **Field numbers added to the Excel column headers** — `I-1 Vital signs documented`, `R-3 Access statement`, and so on.
- **Every Basis line now carries its format and a worked example at the point of use**, including a wrong example and why it is wrong. Hover notes in the spreadsheet carry the same text.
- **Step 3's signature is now explained**, and honestly: format (`W.Q. 2026-09-14`), what it records, and that **nothing physically prevents a reviewer editing it later — it is an agreement, not a lock**.
- **I-2 ambiguity resolved.** *No* = the note is readable and the relevant examination is not in it. *Cannot tell* = you cannot work out which examination was relevant. **Nothing written is No, never Cannot tell.**
- **R-1 gained a `None documented` option**, which it lacked while R-3 and R-4 had one.
- **Step 5 gained eligibility code 5**, "index visit did not end in discharge" — previously an instruction with no code to record it.
- **Step 9's silence-versus-hint rule moved into the code table**, where the decision is actually made.
- **Step 10 reworded.** "Did this pair fit the rules?" read as *did you obey them*; it now asks whether the workbook covered the pair.
- **Stale Excel header fixed** — "Conflict of interest?" became "Did you recognise the child?", matching the workbook.

### Part D — one pair worked through

The largest addition: a complete invented case filled in from Step 1 to Step 10, chosen so the child is **admitted with pneumonia and the judgement is still *illness-related*** — the point being that a bad outcome does not make a case physician-related.

It also shows the two reviewers **disagreeing at Step 3, with both answers defensible and both citing a field**, and states plainly that neither should change their answer to match the other. That is the single most important thing a reviewer can understand before starting.

### Decision recorded: the lock stays on trust (option a)

The PI chose to keep the index judgement as an honour-system signature rather than splitting the sheet into two released files. **`PROTOCOL.md` limitation 5 now says so explicitly** rather than describing an enforced blind: the rule is stated, the initialled date gives an audit trail, and compliance is ultimately on trust. Reported as it is.

### Caught by rebuilding, not by reading

Renaming the Excel headers broke the red-cell conditional formatting, which looked them up by name through a variable that a text search for `L("` could not find. The build failed loudly, the list was updated, and the rebuilt sheets were verified to still carry **16 conditional-formatting ranges**. Worth remembering: **always rebuild and inspect the output after renaming anything the formulas reference.**

Workbook is now **version 0.3**.

---

## What happened on 2026-08-19 (Arabic instructions added to the coding sheets)

Both coding sheets now carry a **second tab, `التعليمات بالعربية`**, holding the full instructions in Arabic. The sheet is set **right-to-left**, so it displays properly rather than as reversed text, and the English tab carries a one-line pointer to it. Built by `make_xlsx.py`, so it regenerates automatically — nothing to maintain by hand.

Register is **simple Modern Standard Arabic with short sentences**, not dense formal phrasing. The Arabic covers everything the English does, including the new rule that the treating doctor's name is hidden.

**Names were deliberately not transliterated.** The Arabic text refers to المراجِع الأول / الثاني / الثالث rather than to people by name, so that no colleague's name is misspelled in Arabic. Each sheet's title carries the Latin name once (`Dr Waad`, `Dr Ainaa`). **If the team would prefer real Arabic spellings, supply them and they can be dropped in.**

---

## What happened on 2026-08-19 (team named, two blockers cleared)

**Three things were settled, and two of them were the ones that mattered most.**

### 1. The patient identifier exists and is stable — the study is feasible

The PI confirmed the identifier is **present in the HIS, the same for the same child across visits, and easy to work with**. This was *the* existential assumption: without it an index visit cannot be linked to a return and the design collapses. It is now closed. `IT-EXPORT-REQUEST.md` records the answer; only the visit-count question remains open there.

### 2. The treating doctor's name can be hidden from reviewers

Also confirmed feasible. This is the single bias in the study that could be **eliminated rather than merely measured**, and it now is. Two residents are classifying discharge decisions made by senior colleagues they work under daily, and one classification asks whether that care was adequate — masking protects reviewer and clinician both.

Written into `PROTOCOL.md` §4.7, `ETHICS-PROPOSAL.md` stage 2, the workbook (new Part A rule 4), and `IT-EXPORT-REQUEST.md` as a required deliverable. **An anonymised clinician code is requested rather than blank removal**, so clinician-level variation can still be examined without any reviewer knowing who the doctor is. One question still to put to IT: whether reviewers will read a masked HIS view or exported documents with the name already stripped.

### 3. The team is named

| Person | Role | Load |
|---|---|---|
| **Dr Lami Qurt** | Principal investigator, first author. **Makes no judgements on any pair** | analysis + manuscript |
| **Dr Samer Dahdoul** | Senior author + the blinded verification review | 80 pairs, ~9 h |
| **Dr Amani Salman** | Reviewer 3 / adjudicator — sees only the disagreements | ~60 pairs, ~7 h |
| **Dr Waad** `[full name needed]` | Reviewer 1 | 400 pairs, ~47 h |
| **Dr Ainaa** `[full name needed]` | Reviewer 2 | 400 pairs, ~47 h |

**Five people, not six.** The earlier plan had three residents; two is enough because the IT export supplies everything except the eight fields a person must read the notes to know. This also keeps the team inside the ≤ 5 reviewers associated with higher inter-rater agreement (*BMJ Open* 2016, PMID 27550650).

### The verification sub-study — new, and pre-specified

Residents classify all 400 pairs. **Dr Samer independently re-classifies a random 80 (20%), blinded.** The sample is drawn at random from **all** 400, not from the disagreements — this is the whole point: if both residents make the same error in the same direction they *agree*, so the adjudicator never sees it. Only a random sample can detect a shared blind spot.

The concern is specific and evidenced: *Emerg Med J* 2017 (PMID 28801485) found trainees assigned a potential medical deficiency **less often than attendings (9% vs 13%)**, with 17% overall discordance rising to **25% in cases requiring admission** — worst precisely where the safety signal lives.

Pre-specified in `ANALYSIS-PLAN.md` **§4a**: kappa against the resident consensus; the physician-related and preventable proportions tabulated **separately for senior and residents** on the same 80 pairs and compared with McNemar's test; and, if a systematic difference is found, the main results reported unchanged plus a sensitivity analysis presenting a range. **The senior's codes never overwrite the primary data.**

`ANALYSIS-PLAN.md` §4 also now carries the benchmark: pooled kappa for this kind of judgement is **0.55–0.65**, so a pilot in that range is normal and not a reason to change the instrument.

### Consequence for the critical path

**The ethics proposal is no longer blocked on names.** `ETHICS-PROPOSAL.md` now carries all five co-investigators, their roles, and the filled team table. What remains before submission:

- **full names for Dr Waad and Dr Ainaa** (surnames not yet recorded)
- team agreement, author order, and signatures
- date of submission

### Still to do

- Ask PMC emergency and pediatric colleagues whether anyone is already running this study — the last duplication check, and the one that caught the previous project.
- Pilot ~30 charts for **documentation quality**. Now the largest untested risk: the eight reviewer-recorded fields are worthless if the notes are mostly empty, and nobody has looked.
- Confirm with IT how the masked records reach the reviewers.
- Ask IT for the approximate visit count.

---

## What happened on 2026-08-19 (folder reorganised)

**The folder had grown to 24 files in one flat list and had become hard to work from.** It is now three folders plus two files at the top.

```
ER Revisit Study/
    START HERE.md / .docx      <- the map: which document to use, and when
    STATUS.md                  <- this file: full history and open decisions
    STEPS/                     <- the 9 documents you use, numbered in order
    REFERENCE/                 <- 4 documents you look things up in
    source/                    <- all .md text files and the build scripts
```

**`START HERE.docx` is the new front door.** For each numbered step it says what the document is for, when to use it, and what is blocking it. `STATUS.md` keeps its old job: the detailed history and the open decisions.

**Nothing was deleted and nothing was copied.** Every file was *moved*, so there is still exactly one copy of each document and nothing can drift out of sync.

**Documents were renamed to their step number** as they moved:

| Step | Document | Was |
|---|---|---|
| 01 | Team Briefing | `Team Briefing.docx` |
| 02 | Protocol and Proposal (to Ministry of Health) | `Protocol _ Proposal .docx` |
| 03 | HIS Data Access Request (English + Arabic) | `HIS_Data_Access_Request_Designed_EN_AR.docx` |
| 03 | HIS Access Letter, Dr Murad Barkan (Arabic) | the Arabic-named file |
| 04 | IT Data Export Request | **new .docx — previously markdown only** |
| 05 | Reviewer Workbook | `Reviewer Workbook.docx` |
| 06 / 07 | Reviewer 1 / 2 Coding Sheet | unchanged names, renumbered |
| 08 | Analysis Plan | **new .docx — previously markdown only** |

`REFERENCE/` holds Full Study Protocol (new .docx built from `PROTOCOL.md`), Coding Manual, Data Dictionary, and the synthetic sample data.

**New: `source/build_all.py`.** This is now the only build command needed. It rebuilds every document into its correct numbered location, so the numbered files cannot drift apart from their sources.

```
cd source
python build_all.py          # everything
python build_all.py 05       # one step
python build_all.py workbook # or match on part of the name
```

If a document is open in Word the script names that one file, reports `OPEN IN WORD`, and finishes the rest.

**Checked, not assumed:** the step 03 English + Arabic document was rebuilt during the move. Its original filename contained the word *Designed*, which raised the possibility of hand layout that a rebuild would destroy. It was verified afterwards — **all 2,844 Arabic characters are present and match the markdown source exactly**, so the original had also been generated and nothing was lost.

**The Arabic letter to Dr Murad Barkan has no markdown source** and is not touched by `build_all.py`. Edit it directly in Word. This is recorded in `START HERE`.

---

## What happened on 2026-08-19

**"Adjudicator" was replaced with "Reviewer 3" in every document a person actually reads, and the role is now explained.** The PI pointed out that the workbook used the word five times but never said who this person is or what they do.

- **`REVIEWER-WORKBOOK.md` gained a "Who is who" table** before Part A, defining Reviewer 1, Reviewer 2 and Reviewer 3, plus one paragraph explaining *why* Reviewer 3 is kept out of the first round (if all three read every pair together there is no disagreement left to measure). A short note records that the protocol and the paper call this person the **adjudicator**, so nobody is confused when they meet the formal word.
- Changed in: `REVIEWER-WORKBOOK.md`, `TEAM-BRIEFING.md`, `SAMPLE-REVIEWER-DATA.md`, and both coding sheets (column header "Note for Reviewer 3"; the independence rule now reads "until Reviewer 3 has settled the disagreements").
- **Deliberately NOT changed:** `adjudicated` is a **variable name** in `DATA-DICTIONARY.md`, and "kappa before adjudication" is standard statistical wording in `ANALYSIS-PLAN.md`. Renaming either would break the analysis or make the statistics section wrong. `PROTOCOL.md` and `ETHICS-PROPOSAL.md` also keep the formal term — journal reviewers expect it. `CODING-MANUAL.md` now defines both words in one sentence, since it is the bridge between the two vocabularies.

**Reviewer 3 is still unnamed** — a senior pediatrician, not yet chosen. This is one of the names blocking the ethics submission. Note the extra constraint now written into the briefing: it must be someone willing to be kept out of the first round of reading.

---

## What happened on 2026-08-19 (earlier)

**The novelty claim was audited and corrected.** Nothing was submitted; stages 4 and 5 are unchanged.

**A factual error was found and fixed in three documents.** `PROTOCOL.md` §2.2, `ETHICS-PROPOSAL.md` §2.2 and `TEAM-BRIEFING.md` §2 all stated that the Middle East has **one** pediatric study on this topic. There are **two**. The second is **Ahmed AE et al., *BMC Pediatr* 2018, PMID 29945589** — 72-hour pediatric revisits in Saudi Arabia, restricted to children with chronic diseases. It does not undermine the gap (it is not a general emergency population), but the claim as written was wrong and a reviewer working in this field would have caught it. Corrected everywhere, and the paper added to both reference lists.

**The global figure was wrong too, and understated.** The protocol said 623 publications; a PubMed re-count on 2026-08-19 returned **769** pediatric records, of which **122** address the 72-hour window specifically, **368** were published in the last five years, and **32** are systematic reviews. Stating the true, larger number *strengthens* the proposal, because it shows the team knows exactly what it is being compared against.

**The honest position on novelty is now written down.** New `PROTOCOL.md` §2.5 *"What this study claims, and what it does not"* and `ETHICS-PROPOSAL.md` §2.4 of the same name. The research question is **not novel** — 72-hour revisit is a mature indicator with 769 pediatric studies behind it, and claiming to have asked it first would be false and would be recognised as such. Five specific contributions are claimed instead: the population; a rate reported with its denominator; predictors identified without an acuity variable; duplicate independent review with the index judgement locked before the return visit is opened; and the access-barrier flag.

**The no-triage point was promoted from limitation to rationale.** Previously it appeared only as limitation 6.3. The argument now made in §2.4 of both documents: essentially every published revisit risk model uses triage acuity as its main predictor, so a model built **without** an acuity variable answers a different question — and it is the question that applies to most of the world's emergency departments. No published pediatric revisit study appears to come from a department without triage. It remains listed as a limitation as well; both statements are true and the manuscript should make both.

**Framing instruction for the manuscript, now recorded in §2.5:** lead with the structural argument, mention Palestine second. Opening with *"the first study in Palestine"* invites a reader to classify the work as a local audit, which is the likeliest route to rejection without review.

**Journal-selection rationale added to §7.** The BMC series decides on scientific validity rather than perceived interest or impact, and assesses originality as *"does this duplicate an existing publication"* rather than *"is the question new"*. This study meets those criteria. Journals that select on novelty or impact are not appropriate first targets.

**Six references verified in PubMed** and their `[VERIFY authors]` flags removed: Cheng 2016 (26160967), Shy 2018 (28967514), Goldman 2017 (28801485), plus Ahmed 2018 and Okeke 2025 added. `Shawahna 2024` still carries `[VERIFY full author list]`.

**Both .docx rebuilt** (`Protocol _ Proposal .docx`, `Team Briefing.docx`) after confirming by text extraction that neither contained hand edits — the only lines that differed were the ones being corrected.

### Still open from this review

- **Okeke CV et al., *Niger Med J* 2025 (PMID 40309556)** — southeast Nigeria, the closest comparable study from a resource-limited setting. Cited in both documents but **not yet read**. Worth reading before the manuscript: it is the most useful single comparator for the discussion.
- The claim *"no published pediatric revisit study from a department without triage"* rests on a title/abstract search. A study could have that setting without saying so. It is phrased as **"we are not aware of"** throughout — keep it that way.

---

## What happened on 2026-08-18

The reviewer instruments were built, then cut back hard. Nothing was submitted; stages 4 and 5 are unchanged.

**Structured chart abstraction replaced free reading.** The reviewers no longer read a chart and jump to a judgement. Every pair now separates into a **fact layer** (what is written) and a **judgement layer** (the four classifications). Two reviewers should agree completely on the facts; a disagreement there is an abstraction error to correct, not a difference of opinion. This is what makes a disagreement diagnosable instead of merely countable.

**The index judgement is locked before the return visit is opened.** The reviewer records whether the discharge decision was reasonable, initials it, and only then opens the return record. This turns "never judge with hindsight" from an instruction into a procedure — it is the single most defensible feature of the design and belongs in the methods section.

**Every judgement carries a Basis line** naming the field and the fact behind it. A judgement with nothing behind it cannot be defended at adjudication.

**"Not documented" is never "normal".** Every clinical field offers it explicitly. Without this the physician-related category quietly empties itself.

**Then it was cut by half.** The first version had reviewers retyping vital signs, investigations, medications, diagnoses, disposition and times — all of which the IT export already holds. Reviewers now record **only what a person must read the notes to know**: eight fields plus the judgements. The coding sheet went from 59 columns to 28.

**PMC has no triage system.** All triage fields were removed from every document.

**Plain language.** "Verbatim" was replaced everywhere a reviewer reads, with worked examples of the difference between copying a sentence and summarising it, and the rule that Arabic notes are copied in Arabic and translated later.

### New files

| File | What it is |
|---|---|
| `REVIEWER-WORKBOOK.md` / `Reviewer Workbook.docx` | **The operative document for the two reviewers.** Ten numbered steps, the form built into the steps. Supersedes `CODING-MANUAL.md` for day-to-day use; the coding manual stays as the methods document for the ethics file and the manuscript. Do not hand reviewers both |
| `Reviewer 1 - Coding Sheet.xlsx` / `Reviewer 2 - Coding Sheet.xlsx` | The recording instrument. Separate files on purpose — that is the independence rule made physical. 28 columns, 14 dropdowns, red cells for missing entries, amber for broken rules, hover notes on the fields that get misused |
| `SAMPLE-REVIEWER-DATA.md` / `Sample Reviewer Data (SYNTHETIC).docx` | **Forty invented pairs — no real patients.** Both reviewers' codes, the agreement tables, and the reliability analysis worked through. Built to show the team the shape of the output before real data exists. **Delete once the real pilot is done** |
| `make_xlsx.py`, `make_sample.py` | Rebuild the coding sheets and the synthetic sample |

`DATA-DICTIONARY.md` gained **§5a**, the eight reviewer-recorded variables. Four of them — `vitals_documented`, `relevant_system_examined`, `discharge_instructions`, `followup_directed` — cannot come from the export and are findings in their own right. *"X% of children were discharged with no documented return precautions"* is the most locally actionable number this study can produce.

### Decided about the statistics

No statistician is needed for the pilot. Kappa is a 3x3 table, a division, and PABAK = (k x Po - 1) / (k - 1). The reviewers' two columns of codes are enough to produce the whole reliability table. **Report raw agreement and PABAK beside every kappa** — with a skewed distribution, kappa can look poor while the reviewers agreed on 94% of pairs, which is exactly what the synthetic sample demonstrates.

A statistician or epidemiologist co-author is still worth recruiting for the multivariable logistic regression — An-Najah, Al-Quds or Birzeit, or via the MoH research office. Not blocking anything.

### Still to do on the instruments

- ~~**Pilot stopping rules**~~ — **done 2026-08-20**, written into `ANALYSIS-PLAN.md` §4b (plan v0.2). Go/no-go thresholds per judgement, the uncertain ceiling, minutes per pair, the rule-ambiguity rule, and the one-page pilot report.
- **Drift monitoring** — the adjudicator silently re-abstracting a random 10% partway through — is not built.
- **Blinding reviewers to the expected results** is not addressed anywhere.
- Reviewers must be **told before starting** that results are reported in aggregate only, never per clinician. Physician-related means judging named colleagues. **Corrected 2026-08-20:** an earlier version of this line said the treating clinician cannot be masked; the 2026-08-19 finding above supersedes it — the name *can* be hidden, and an anonymised clinician code is being requested instead. Reviewers may still recognise a case by other means, which is what the Step 10 question exists for.

---

## What happened on 2026-08-17

- **Duplication check:** thesis repositories (An-Najah / Al-Quds / Birzeit) clear; **MoH research office confirms no similar study on record.** Still to ask: Google Scholar in Arabic, and our own ED/pediatric colleagues.
- **PMC is not solely a referral hospital** — it is a first-contact hospital for its catchment as well. Corrected in the protocol, ethics proposal and briefing; the generalisability limitation was rewritten, since an unselected case mix is a strength, not a weakness.
- **Pediatric age limit resolved: under 13 years**, per MoH rule (a child goes to the adult ER after their 13th birthday). Propagated everywhere; age bands reworked; expected volumes need no reduction because the pediatric ED *is* an under-13 department.
- **MoH answers:** no proposal template required; **IT will not export before approval**; expedited-route question still unasked.
- **New:** `TEAM-BRIEFING.md` (plain-language team document) and `build_docx.py`; both .docx files rebuilt.

## Files in this folder

> **Superseded 2026-08-19 — see `START HERE.md` for the current layout.** The table below lists what each document is; the paths are the pre-reorganisation ones.

| File | What it is |
|------|------------|
| `PROTOCOL.md` | Full study protocol, draft v0.1 |
| `IT-EXPORT-REQUEST.md` | Exact field list to hand to the IT department |
| `DATA-DICTIONARY.md` | Variable-by-variable specification |
| `CODING-MANUAL.md` | Classification rules — the methods document for the ethics file and the manuscript. **Reviewers use `Reviewer Workbook.docx` instead** |
| `ANALYSIS-PLAN.md` | Pre-specified SPSS analysis, written before any data is seen |
| `ETHICS-PROPOSAL.md` | **Submission-ready proposal for the MoH research office** |
| `HIS-DATA-ACCESS-REQUEST.md` | **Letter to Dept of Continuous Education for HIS data access — English + Arabic** |
| `TEAM-BRIEFING.md` | **Plain-language summary for the team meeting — steps, data collection, comparisons, expected results** |
| `build_docx.py` | Converts any of these markdown files to .docx in the house style. **Always diff before overwriting a hand-edited .docx** |
| `Protocol _ Proposal .docx` | **The document to submit to the MoH.** Built from `ETHICS-PROPOSAL.md` |
| `Team Briefing.docx` | Built from `TEAM-BRIEFING.md`, for the team meeting |
| `HIS_Data_Access_Request_Designed_EN_AR.docx` | The HIS access letter, EN + AR |
| `Protocol _ Proposal (hand-edited 2026-08-17 backup).docx` | Snapshot of the hand-edited file before it was rebuilt |
| `REVIEWER-WORKBOOK.md` | **What the two reviewers actually work from** — ten steps, form included |
| `Reviewer Workbook.docx` | The same, for handing out |
| `Reviewer 1 - Coding Sheet.xlsx` | Reviewer 1's recording sheet. Never shared with Reviewer 2 |
| `Reviewer 2 - Coding Sheet.xlsx` | Reviewer 2's recording sheet. Never shared with Reviewer 1 |
| `SAMPLE-REVIEWER-DATA.md` | **Synthetic 40-pair example — invented patients.** Delete after the real pilot |
| `Sample Reviewer Data (SYNTHETIC).docx` | The same, for showing the team |
| `make_xlsx.py`, `make_sample.py` | Rebuild the coding sheets and the synthetic sample |
| `STATUS.md` | This file |

## Approvals needed — three, not one

| # | Approval | From | Status |
|---|---|---|---|
| 1 | Ethics | MoH research office | Proposal drafted, ready to send |
| 2 | HIS data access | Dept of Continuous Education, PMC | Letter drafted (EN + AR), ready to send |
| 3 | Data extract | PMC IT Department | Field list ready. **Requires #1 first — IT will not export before ethics approval (confirmed 2026-08-17)** |

**Ask whether #1 and #2 can run in parallel.** If they can, submit both now — it saves weeks on the critical path.

## Ethics route (confirmed 2026-08-16)

The PI spoke to the **person responsible for research at the Palestinian MoH**, who can obtain IRB approval once a proposal is submitted. **This is the operative route** — use it rather than searching for a separate PHRC/Helsinki Committee, which may no longer be reachable in practice.

**Must be obtained in writing, not verbally:** the formal name of the approving committee as it should appear in a journal ethics statement, an approval/reference number, the date, and explicit confirmation that consent was waived. Journals require all four.

Three questions put to the MoH officer — answered 2026-08-17:
- **Required proposal template or form? — No.** Our own format is acceptable; `ETHICS-PROPOSAL.md` / `Protocol _ Proposal .docx` is what gets submitted.
- Is there an expedited route for retrospective records-only research? — **still unanswered, worth asking.**
- **May IT export before approval? — No. Approval first.** This puts the data export behind the full ethics wait.

## The study in one paragraph

Retrospective cohort of **all pediatric ED visits ending in discharge** at PMC over **24 months**, using a full data export from the ED digital system. An unscheduled return to the same ED within 72 hours is identified by linking visits on patient ID. Expected **~55,000–58,000 discharged index visits** and **~1,100–2,900 revisits**. Primary outcome is the 72-hour revisit rate. Secondary outcomes are the proportion admitted on return, the classification of each return (related/unrelated; illness-, patient- or physician-related), and predictors of return by multivariable logistic regression.

## Why this design

- **The ED system is digital and IT can export a date range to Excel** (confirmed 2026-08-16). The export supplies the denominator and the visit linkage automatically — this is what makes the study possible and is why earlier ED designs were abandoned.
- **No records-system change in the last 2–3 years** (confirmed 2026-08-16), so the study period is comparable throughout.
- Manual work is confined to **chart review of a 400-pair random sample of revisits**, not the whole cohort. Rate and all regression predictors come from the export; only the classification judgements need a human. This cuts reviewer effort from ~470 hours to ~93.
- **Scheduled ED returns are rare here** — PMC clinicians direct planned follow-up to outpatient clinic, not the ED (confirmed 2026-08-16). This makes the primary outcome fully digital, and makes an ED return a stronger signal than in systems where ED follow-up is routine. Verified in the sample rather than assumed.
- **An access-barrier flag is recorded separately** from the standard attribution taxonomy, to capture families who return to the ED because the clinic route was closed to them (no appointment, transport, cost, movement restriction). Potentially the study's most distinctive finding, and unrecoverable if not captured now.
- **No triage system anywhere in Palestine** → no acuity variable. Stated as a limitation **and** as the study's principal conceptual contribution (§2.4/§2.5 of the protocol) — every published revisit risk model uses acuity, so a model without it answers a different question.

## Team

| Role | Person |
|------|--------|
| PI / first author | **Dr Lami Qurt** — makes no classification judgements |
| Senior author + verification reviewer | **Dr Samer Dahdoul** — blinded re-review of 80 random pairs |
| Adjudicator (Reviewer 3) | **Dr Amani Salman** — decides the ~60 disagreements |
| Reviewer 1 | **Dr Waad** `[full name needed]` — all 400 pairs |
| Reviewer 2 | **Dr Ainaa** `[full name needed]` — all 400 pairs |
| Statistician | None available — analysis with Claude's support, disclosed in the paper |

**Standing obligations:** residents must be given a genuine intellectual task (the classification work qualifies) or they fail ICMJE authorship on data collection alone. AI assistance must be disclosed per ICMJE; AI cannot be an author.

---

## NEXT ACTIONS

**1. Local duplication check — partially done.** PubMed cannot see Palestinian theses, MoH reports, or work in progress. This is what would have caught the previous collision.
   - ✅ **An-Najah / Al-Quds / Birzeit thesis repositories — checked 2026-08-17, nothing found.**
   - ✅ **MoH research office — asked 2026-08-17, no similar study on record.** This is the check that sees protocols submitted but not yet published.
   - ⬜ Google Scholar (Arabic + English terms), and MoH / PMC internal reports
   - ⬜ **Ask PMC emergency and pediatric colleagues directly** — the last remaining gap, and the one that caught the previous collision. Work in progress inside our own department never reaches the MoH office or a repository until it is finished.

**2. Fill in the names, then submit `Protocol _ Proposal .docx` to the MoH.** No template is required, so the document is otherwise ready. Outstanding blanks: co-investigators, the three team-table rows, date of submission, signature. **This is now the top of the critical path** — the multi-week ethics wait cannot start until the names are in. Still worth asking: is there an expedited route for records-only research?

**3. Send `HIS-DATA-ACCESS-REQUEST.md`** to the Dept of Continuous Education — ask whether it may run in parallel with the ethics submission.

**4. Ask IT the two system questions now — do not send the export request yet.** IT will not export before approval, but these two ask how the system behaves rather than for any patient data:
   - **Is the patient identifier the same for the same child across visits?** The single technical assumption the whole study rests on. If it fails, the design must change — far better to know this week than after a 12-week approval.
   - Roughly how many pediatric ED visits fall in 1 Jan 2024 – 31 Dec 2025?

   Send `IT-EXPORT-REQUEST.md` itself only once the approval letter is in hand.

**5. Team meeting** — fill in names, agree author order, sign before classification starts.

## Open decisions

- [x] **Pediatric age limit — RESOLVED 2026-08-17: under 13 years.** Propagated to protocol, ethics proposal, IT export filter, data dictionary (age bands now <1 / 1–4 / 5–8 / 9–12, reference 5–8), analysis plan and briefing. **Confirmed by MoH rule:** pediatrics is 0 to under 13 and a child is referred to the adult ER after their 13th birthday, so the pediatric ED *is* an under-13 department and the expected visit volumes need no age-based reduction.
- [ ] Study period — proposed **1 Jan 2024 – 31 Dec 2025** (two clean calendar years, two full respiratory seasons, comfortably inside the stable-system window, and old enough that all records are settled). Confirm.
- [ ] Names for senior author, second reviewer, adjudicator, three residents
- [ ] Is the patient identifier in the ED export stable across visits? **This is the single technical assumption the whole study rests on** — verify with IT before anything else.
- [ ] Approach a statistician at An-Najah / Al-Quds / Birzeit for co-authorship?

## Items that must be verified, never written from memory

Marked `[VERIFY]` throughout `PROTOCOL.md`:

- **Every reference checked in PubMed** — several citations currently carry PMIDs but unconfirmed author lists
- Total annual pediatric ED visit volume and discharge proportion at PMC, from actual records
- MoH research office turnaround time and any fees (**no form or template required — confirmed 2026-08-17**)
- PMC catchment population and its dual role (first-contact **and** referral), for the setting paragraph
- **Every candidate journal's indexing** (PubMed / Scopus / DOAJ) before submission — no predatory journals
