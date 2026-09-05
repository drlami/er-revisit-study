# Data Export Request — IT Department

**To:** IT Department, Palestine Medical Complex
**From:** Dr Lami Qurt, Department of Pediatrics
**Re:** Data export for an approved research study on pediatric emergency department return visits
**Date:** ____________

> **Do not send this until MoH ethics approval has been granted.** Confirmed with the MoH research office on 2026-08-17: **IT will not produce the export before approval.** Attach the approval letter when you send this request.
>
> **The questions in the final section are a separate matter and can be asked now.** They ask how the system behaves, not for any patient data, so they should not require approval.
>
> **Confirmed 2026-08-19:** the patient identifier **is present in the HIS and is stable across visits**, and the treating doctor's name **can be withheld** from the review extract. Both were previously open questions and both are now settled, so the study is feasible as designed. The remaining question below is about cohort size only.

---

## What is requested

**One Excel file** containing **one row per pediatric emergency department visit** for the period:

**1 January 2024 – 31 December 2025**

Filter: patients aged **under 13 years** at the time of the visit, presenting to the **pediatric emergency department**. Per Ministry of Health rules, pediatrics at PMC covers ages 0 to under 13 and older patients attend the adult emergency department, so this filter should describe the whole pediatric ED rather than restrict it. Please confirm that is how the system classifies these visits.

Please include **all** such visits — those admitted and those discharged. The study needs both in order to calculate the denominator correctly.

---

## Fields required

### Essential — the study cannot proceed without these

| # | Field | Why it is needed |
|---|-------|------------------|
| 1 | **Patient identifier** (medical record number or equivalent) | To link a return visit to the earlier visit. **This is the single most important field.** |
| 2 | **Visit identifier** (unique per visit) | To ensure each visit is counted once |
| 3 | **Date and time of arrival** | To calculate the 72-hour interval |
| 4 | **Date and time of departure / discharge** | The 72-hour window runs from discharge |
| 5 | **Disposition** (discharged home / admitted / transferred / left against medical advice / left without being seen / died) | Defines who enters the cohort |
| 6 | **Age at visit** (or date of birth) | Eligibility and a key predictor |
| 7 | **Sex** | Standard descriptive variable |
| 8 | **Diagnosis at the visit** (coded and/or free text, as held) | The main clinical exposure variable |

### Important — improves the study substantially

| # | Field | Why it is needed |
|---|-------|------------------|
| 9 | **Medications prescribed or given at the visit** (name, and route if held) | Tests whether treatment at the index visit predicts return |
| 10 | **Investigations ordered** (laboratory, imaging — presence is enough) | Marker of index-visit workup intensity |
| 11 | **Treating clinician grade or identifier** (anonymised code is fine) | Allows examination of clinician-level variation |
| 12 | **Residence / locality** | Distance and access are plausible predictors in this setting |

### Useful if available

| # | Field |
|---|-------|
| 13 | Mode of arrival (walk-in / ambulance / referred) |
| 14 | Referral source |
| 15 | Whether discharge instructions were recorded |

---

## Format

- **Excel (.xlsx) or CSV** — either is fine
- **One row per visit**, one header row, consistent column names
- Dates and times in a single consistent format — please state which (e.g. `DD/MM/YYYY HH:MM`)
- Empty cells for missing values rather than text such as "N/A", "none" or "-"
- If the export must be split, split **by date range**, not by patient

---

## Data protection

- The patient identifier is required **solely to link repeat visits by the same child**. It will be replaced by a study number as soon as linkage is complete, and the linkage key will be held separately by the principal investigator and destroyed at the end of the study.
- The file will be stored on password-protected institutional equipment and shared with no one outside the named research team.
- No identifiable data will appear in any analysis, presentation or publication.
- If the system can generate a **stable pseudonymised patient code** instead of the real medical record number — a code that is the same for the same child across visits but is not the MRN — that is preferred, and the real identifier is then not needed at all.

---

## Questions for IT

**1. Is the patient identifier stable across visits?** — **ANSWERED 2026-08-19: yes.** The identifier is present in the HIS, is the same for the same child across visits, and is straightforward to work with. This was the single assumption the study rested on.

**2. Approximately how many pediatric ED visits fall in this date range?**
A rough count is enough. It confirms the expected cohort size before any work begins. **Still outstanding.**

---

## Required: the treating doctor's name must not appear in the review extract

The 400 sampled pairs are read by two pediatric residents who work in the same department as the doctors whose discharge decisions they are assessing. One of the classifications asks whether care at the first visit was adequate.

**Please supply the records for chart review with the treating doctor's name removed or replaced by a code.** Confirmed as feasible on 2026-08-19.

- An **anonymised clinician code** is ideal rather than blank removal — the same doctor should carry the same code across visits, so clinician-level variation can still be examined (field 11 in the table above) without any reviewer knowing who the doctor is.
- The code key is not needed by the research team and should **not** be supplied.
- This applies to the **records the reviewers read**, not only to the spreadsheet: if reviewers will open records in the HIS directly, please advise whether a masked view is possible, or whether the pairs should instead be exported as documents with the name already removed.

---

**Contact:** Dr Lami Qurt, Department of Pediatrics — ____________
