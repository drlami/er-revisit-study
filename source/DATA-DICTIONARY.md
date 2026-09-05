# Data Dictionary

**Study:** Unscheduled 72-hour return visits to the pediatric ED, PMC Ramallah
**Version:** 0.1 — 2026-08-16

Three groups of variables:
- **[E]** — comes directly from the IT export
- **[D]** — derived by us during dataset construction
- **[C]** — produced by reviewer classification of return visits

---

## 1. Identifiers

| Variable | Type | Values / format | Source | Notes |
|---|---|---|---|---|
| `patient_id_raw` | text | as held by the system | [E] | **Deleted after linkage.** Replaced by `study_id`. Never appears in the analysis file |
| `study_id` | integer | 1…n | [D] | Sequential study number per child |
| `visit_id` | text | as held | [E] | Unique per visit; used to detect duplicate rows |

---

## 2. Index visit — from the export

| Variable | Type | Values / format | Source | Notes |
|---|---|---|---|---|
| `arrival_dt` | datetime | `DD/MM/YYYY HH:MM` | [E] | |
| `discharge_dt` | datetime | `DD/MM/YYYY HH:MM` | [E] | The 72-hour clock starts here |
| `age_years` | decimal | 0–12.99 | [E] | From DOB if age not held directly |
| `sex` | categorical | 1 = male, 2 = female | [E] | |
| `disposition` | categorical | 1 = discharged home, 2 = admitted, 3 = transferred, 4 = left against medical advice, 5 = left without being seen, 6 = died, 99 = unclear | [E] | Only **1** enters the cohort as an index visit |
| `diagnosis_text` | text | free text and/or code | [E] | Kept exactly as the system holds it; grouped into `dx_group` |
| `meds_given` | text | drug names | [E] | |
| `investigations` | text | as held | [E] | Presence is sufficient |
| `clinician_code` | text | anonymised | [E] | If available |
| `locality` | text | as held | [E] | If available |
| `arrival_mode` | categorical | 1 = walk-in, 2 = ambulance, 3 = referred, 99 = unknown | [E] | If available |

---

## 3. Derived variables

| Variable | Type | Values | Definition |
|---|---|---|---|
| `age_band` | categorical | 1 = <1 y, 2 = 1–4 y, 3 = 5–8 y, 4 = 9–12 y | From `age_years`. Reference category for modelling = **3** |
| `dx_group` | categorical | see §6 below | Grouping of `diagnosis_text` |
| `arrival_period` | categorical | 1 = day 08:00–15:59, 2 = evening 16:00–23:59, 3 = night 00:00–07:59 | From `arrival_dt` |
| `weekend_holiday` | binary | 0 = no, 1 = yes | Local weekend and public holidays `[DECIDE — confirm which days count as weekend at PMC]` |
| `season` | categorical | 1 = winter (Dec–Feb), 2 = spring (Mar–May), 3 = summer (Jun–Aug), 4 = autumn (Sep–Nov) | From `arrival_dt` |
| `ed_los_hours` | decimal | hours | `discharge_dt − arrival_dt` |
| `any_med` | binary | 0 / 1 | Any medication prescribed or given at the index visit |
| `antibiotic` | binary | 0 / 1 | Any systemic antibiotic. Topical and ophthalmic preparations do **not** count |
| `any_investigation` | binary | 0 / 1 | Any laboratory or imaging investigation performed |
| `prior_visit_30d` | binary | 0 / 1 | Any ED visit by the same child in the 30 days before this index visit |
| `hours_to_return` | decimal | hours | Next arrival − this discharge. Blank if no subsequent visit |
| `return_72h` | binary | 0 / 1 | **PRIMARY OUTCOME.** 1 if `0 < hours_to_return ≤ 72` and the return is not excluded per the coding manual |

---

## 4. Return visit — from the export

Same fields as §2, prefixed `ret_`: `ret_arrival_dt`, `ret_diagnosis_text`, `ret_disposition`, `ret_meds_given`, and so on.

| Variable | Type | Values | Notes |
|---|---|---|---|
| `ret_admitted` | binary | 0 / 1 | 1 if `ret_disposition` = 2. **Key secondary outcome** |
| `dx_changed` | binary | 0 / 1 | Return-visit diagnosis differs from index diagnosis |

---

## 5a. Chart abstraction variables

Read from the record by each reviewer, because the export cannot supply them. Recorded per reviewer with the `_r1`, `_r2`, `_final` suffixes, exactly like the classification variables below.

| Variable | Type | Values | Notes |
|---|---|---|---|
| `vitals_documented` | categorical | 1 = all documented, 2 = partly documented, 3 = none documented | What was **recorded**, not whether it was normal. Supports the index-adequacy judgement and is a documentation-quality finding in its own right |
| `relevant_system_examined` | binary | 1 = yes, 2 = no, 3 = cannot tell | Was the system relevant to the presenting complaint examined and documented. The strongest single predictor of a physician-related attribution |
| `discharge_instructions` | categorical | 1 = none documented, 2 = generic advice only, 3 = specific return precautions | Not held anywhere in the export. Directly actionable locally |
| `followup_directed` | categorical | 1 = none documented, 2 = return to ED, 3 = outpatient clinic, 4 = primary health centre, 5 = other | Gives `access_barrier` its context: a clinic route cannot fail if the family was never sent to one |
| `index_decision_reasonable` | categorical | 1 = adequate, 2 = inadequate, 3 = cannot tell from the record | **Recorded before the return visit is opened.** This sequencing is what makes the no-hindsight rule a procedure rather than an instruction |
| `reason_return_text` | text | the record's exact words | Copied exactly as written, never paraphrased, in the language the note was written in. Becomes the reasons table |
| `access_text` | text | the record's exact words, or "none documented" | Trigger field for `access_barrier` |
| `medicine_text` | text | the record's exact words, or "none documented" | Trigger field for `access_barrier` |

Reviewers record nothing that the export already holds — no times, diagnoses, medications, investigations or disposition. See `Reviewer Workbook.docx` and the coding sheets.

---

## 5. Classification variables

Recorded **separately for each reviewer**, then a final adjudicated value. Suffixes: `_r1`, `_r2`, `_final`.

| Variable | Type | Values | Notes |
|---|---|---|---|
| `eligible` | categorical | 1 = eligible, 2 = excluded: scheduled return, 3 = excluded: administrative, 4 = excluded: insufficient documentation, 5 = excluded: index visit did not end in discharge | Code 5 means the pair should not have been sampled — report to the PI. Coding manual §2 |
| `relatedness` | categorical | 1 = related, 2 = unrelated, 3 = uncertain | Coding manual §3 |
| `attribution` | categorical | 1 = illness-related, 2 = patient-related, 3 = physician-related, 4 = uncertain | Coding manual §4 |
| `preventable` | categorical | 1 = preventable, 2 = not preventable, 3 = uncertain | Coding manual §5 |
| `access_barrier` | categorical | 1 = yes, 2 = no, 3 = uncertain | Coding manual §5b. **Recorded independently of `attribution`** — a case may be illness-related *and* carry an access barrier |
| `access_barrier_type` | categorical | 1 = no clinic appointment available, 2 = could not reach clinic (transport/distance/checkpoint), 3 = could not obtain medication, 4 = cost, 5 = other (specify in free text) | Only completed when `access_barrier` = 1 |
| `reason_text` | text | free text | Reason for return in the record's own words |
| `reviewer_note` | text | free text | Notes for the adjudicator |
| `adjudicated` | binary | 0 / 1 | 1 if the two reviewers disagreed and reviewer 3 decided |

Kappa is computed on `_r1` versus `_r2`. Analysis uses `_final`.

### 5b. Basis variables — why each judgement was made

Restructured **2026-08-19**. Each judgement records **which field drove it**, chosen from a fixed list rather than typed. Two judgements also carry one line of written reasoning. **No field's contents are ever copied into a Basis** — the pointer is the link, so nothing is stored twice and no two copies can disagree.

| Variable | Type | Values | Notes |
|---|---|---|---|
| `basis_index_field` | categorical | I-1, I-2, I-3, I-4, R-1, R-2, R-3, R-4, more than one, none fit | Which field drove `index_decision_reasonable` |
| `basis_index_reason` | text | one short line | Reasoning only, never the field's contents |
| `basis_relatedness_field` | categorical | as above | Pointer only — no written reason for `relatedness` |
| `basis_attribution_field` | categorical | as above | Which field drove `attribution` |
| `basis_attribution_reason` | text | one short line | The judgement the paper turns on, so it keeps a reason |
| `basis_preventable_field` | categorical | as above | Pointer only — reasoning overlaps with attribution |
| `basis_access_field` | categorical | R-3, R-4, both, none — nothing documented | Pointer only. The quoted words live in `access_text` / `medicine_text` |

**Analytic use.** These are not outcome variables. They serve three purposes: they let the adjudicator check a judgement against the record without asking the reviewer what they meant; they make it possible to report **which fields most often drive a physician-related attribution** (a genuine secondary finding — likely `relevant_system_examined`); and they expose reviewers who are judging without evidence, since a judgement whose pointer is *none fit* every time is a warning sign.

`basis_*` variables carry `_r1`, `_r2` and `_final` suffixes like everything else.

---

## 6. Diagnosis grouping (`dx_group`)

Draft grouping — **to be finalised after seeing the actual diagnosis labels in the export**, and before any classification begins. The grouping must be fixed before analysis, not adjusted afterwards.

| Code | Group | Includes |
|---|---|---|
| 1 | Respiratory | URTI, bronchiolitis, pneumonia, asthma/wheeze, croup, tonsillitis, otitis media |
| 2 | Gastrointestinal | Gastroenteritis, vomiting, diarrhoea, abdominal pain, constipation |
| 3 | Fever without source | Fever with no localising diagnosis recorded |
| 4 | Trauma and injury | Fractures, lacerations, head injury, burns, foreign body |
| 5 | Neurological | Seizure, febrile convulsion, headache, altered consciousness |
| 6 | Dermatological / allergic | Rash, urticaria, allergic reaction, cellulitis, skin infection |
| 7 | Genitourinary | UTI, scrotal or genital complaints |
| 8 | Other medical | Everything else with a recorded diagnosis |
| 99 | Not recorded / uninterpretable | |

**Reference category for regression: 1 (respiratory)** — the largest group, which gives the most stable comparisons.

---

## 7. Data handling rules

1. **Never edit the raw export.** Keep it read-only. Do all work on a copy.
2. Every derived variable is created by a recorded, repeatable step — an SPSS syntax file, not manual editing. Save the syntax; it is the audit trail and reviewers may ask for it.
3. Missing values are left **blank**, never coded as 0, "N/A" or "-".
4. The linkage key (`patient_id_raw` ↔ `study_id`) is stored in a separate password-protected file held only by the PI, and destroyed once the analysis is complete.
5. No file containing `patient_id_raw` leaves institutional equipment.
6. Version-date every file. The analysis dataset used for the final manuscript is frozen and archived.

---

## 8. Fields to confirm on receipt of the export

Check these before designing anything further — they determine what the final variable list can be:

- [ ] Is `patient_id_raw` genuinely the same for the same child across visits?
- [ ] Are both arrival **and** discharge times populated, or only arrival?
- [ ] Is `disposition` recorded consistently, and what are the actual category labels used?
- [ ] Is `diagnosis_text` coded (ICD or similar) or free text? Free text needs a grouping pass by a clinician.
- [ ] Are medications a usable list, or free text requiring manual reading?
- [ ] What proportion of rows are missing each essential field?
