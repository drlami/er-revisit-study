# Coding Manual — Classification of Return Visits

**Study:** Unscheduled 72-hour return visits to the pediatric ED, PMC Ramallah
**Version:** 0.1 — 2026-08-16
**For:** the two independent reviewers and the adjudicator

---

## 1. What you are doing, and why it matters

You are given **pairs of visits**: an index visit that ended in discharge, and a return visit by the same child within 72 hours. For each pair you make **four judgements**, using the full clinical record of both visits.

You will receive a **random sample of 400 pairs**, not all of them. The return *rate* is calculated from the full electronic dataset; your job is the part a computer cannot do.

Two reviewers do this **independently and without discussing cases**. A third senior reviewer — **Reviewer 3**, called the **adjudicator** in the protocol and the paper — settles disagreements. We then report Cohen's kappa — a published measure of how much you agreed before adjudication.

This matters more than it looks. A 2017 study in *Emerg Med J* found **25% disagreement between consultants and trainees** about why the same patients came back. That is exactly why a single reviewer's opinion is not publishable and duplicate independent review is. Your disagreements are not a problem with the study — they are part of its output.

**Do not discuss cases with the other reviewer until adjudication.** If you do, the kappa becomes meaningless and that part of the paper is lost.

---

## 2. Before you classify: is this pair eligible at all?

Answer these first. If any answer sends the pair out, record the reason and stop.

| Question | If YES |
|---|---|
| Was the return **planned or advised** at the index visit? (e.g. "come back tomorrow", planned wound check, planned repeat blood test) | **EXCLUDE** — this is not an unscheduled return |

> **Expect very few exclusions here.** At PMC, clinicians send patients needing planned review to **outpatient clinic, not to the ED**. Almost every return you see should be unscheduled. We are counting the exceptions rather than assuming there are none — the number you find gets reported in the paper, so record it carefully even though it will be small.
>
> Note the difference between *"return to ED tomorrow"* (scheduled → exclude) and *"follow up in clinic"* followed by the family coming to the ED anyway (**unscheduled → include**, and see Judgement 4).
| Was the return **purely administrative**? (medical certificate, report, prescription refill with no clinical assessment) | **EXCLUDE** |
| Is the index visit record so incomplete that you cannot tell what happened? | **EXCLUDE** — record as "insufficient documentation" |
| Did the index visit actually end in **discharge**? | If NO → **EXCLUDE** (should already have been filtered, but check) |

Everything else is classified.

---

## 3. Judgement 1 — Relatedness

**Question:** Is the return visit related to the problem presented at the index visit?

| Code | Definition |
|---|---|
| **Related** | The return concerns the same illness, a complication of it, a progression of it, or a side effect of treatment given for it |
| **Unrelated** | The return concerns a genuinely different problem |
| **Uncertain** | Documentation does not allow a decision |

**Rules**

- Judge on the **clinical problem**, not on whether the written diagnosis label matches. A child seen for "fever" who returns with "pneumonia" is **related** — same illness, better characterised the second time.
- A **complication of treatment** given at the index visit is **related** (e.g. vomiting after an antibiotic prescribed at the index visit).
- A **new injury** in a child previously seen for illness is **unrelated**.
- When in genuine doubt between related and unrelated, choose **related**. This is the conservative direction: it keeps the case in the safety-relevant group rather than discarding it.

---

## 4. Judgement 2 — Attribution

**Question:** What best explains why this child came back?

Use the established three-category taxonomy (*Am J Med Qual* 2016, PMID 26160967). Choose **one** category — the one that contributed most.

### Illness-related
The return reflects the **natural course of the disease**. Care at the index visit was appropriate given what was knowable at the time.

- The illness progressed as illnesses do
- A condition declared itself over time that was not yet apparent
- Expected worsening before improvement

> *Example:* 7-month-old seen on day 2 of bronchiolitis, mild, feeding well, appropriately discharged with advice. Returns on day 4 with increased work of breathing and is admitted. **Illness-related.** Bronchiolitis characteristically peaks on days 3–5. Nothing was missed.

### Patient-related
The return is driven mainly by **caregiver factors**, not by the disease and not by the index encounter.

- Anxiety, or seeking reassurance, with no clinical change
- Instructions misunderstood or not followed
- Medication not obtained or not given
- Return simply to ask a question

> *Example:* 3-year-old with gastroenteritis, tolerating oral fluids at discharge, given oral rehydration instructions. Returns 12 hours later; on assessment the child is well, hydrated, no new findings, and the mother reports she was unsure how much fluid to give. **Patient-related.**

### Physician-related
The return is attributable to **something about the index encounter** that could reasonably have been done differently *with the information available at the time*.

- Diagnosis missed or incorrect
- Treatment inadequate, wrong, or wrongly dosed
- Discharged too early given the findings documented
- Necessary investigation not performed
- Discharge instructions inadequate or absent

> *Example:* 4-year-old with limp and fever, discharged with no examination of the hip documented and no investigations. Returns 24 hours later, septic arthritis diagnosed, admitted. **Physician-related.**

### The rule that keeps this fair

> **Judge only on what was documented and knowable at the index visit. Never judge with hindsight.**

An illness that could not reasonably have been diagnosed at the index visit is **illness-related**, even if the outcome was serious. The question is never "did something bad happen?" — it is "was the decision reasonable given what was in front of the clinician?"

If two categories genuinely both apply, choose the one that contributed **most**. If you truly cannot separate them, code **Uncertain** and let the adjudicator decide. Do not guess to avoid an uncertain code.

---

## 5. Judgement 3 — Preventability

**Question:** Could this return plausibly have been prevented by different action at the index visit?

| Code | Meaning |
|---|---|
| **Preventable** | Yes — different assessment, treatment, or instructions would probably have avoided the return |
| **Not preventable** | No — the return was an appropriate response to a genuine change |
| **Uncertain** | Cannot determine |

Note that **preventable is not the same as physician-related**. A patient-related return caused by a misunderstanding may well have been preventable by clearer instructions. Keep the two judgements separate.

---

## 5b. Judgement 4 — Access barrier

**Question:** Is there anything in the record indicating the family returned to the ED because they **could not access** the alternative they were directed to?

| Code | Meaning |
|---|---|
| **Yes** | Documented access barrier — clinic appointment unavailable or too distant in time, could not reach the clinic, could not obtain the prescribed medication, cost, transport, distance, checkpoint or movement restriction |
| **No** | No such barrier documented |
| **Uncertain** | Cannot determine |

**Why this is a separate question.** At PMC, follow-up is directed to outpatient clinic. When a family comes back to the ED instead, the standard taxonomy would tend to label that "patient-related" — implying the caregiver did something wrong. Often they did not: they came because the clinic route was closed to them. That is a **health-system access failure**, and in a setting with movement restrictions it may be one of the most important things this study can show.

Keep it separate from Judgement 2 so the attribution figures stay comparable with published studies. A case can be *illness-related* **and** carry an access-barrier flag; the two are independent.

**Code YES only on documented evidence**, not on inference. If the record says "mother reports could not get clinic appointment" → Yes. If the record is silent → No, not Uncertain. Reserve Uncertain for records that hint at a barrier without stating one.

---

## 6. Also record for every pair

| Field | Notes |
|---|---|
| Reason for return, in the caregiver's or clinician's words | Short free text — used for the reasons table |
| Presenting complaint at the return visit | |
| Diagnosis at the return visit | |
| Disposition at the return visit | Discharged / admitted / transferred / died |
| Was the return-visit diagnosis different from the index diagnosis? | Yes / No |
| Free-text note | Anything that will help the adjudicator |

---

## 7. Worked examples for calibration

Everyone reviews these **before starting**, then compares answers as a group. This is the only point at which discussion is permitted.

| # | Scenario | Related? | Attribution | Preventable? |
|---|---|---|---|---|
| 1 | 2-year-old, febrile URTI, discharged with antipyretic advice. Returns 36 h later still febrile, examined, otitis media found, antibiotic started, discharged. | Related | Illness-related | Not preventable |
| 2 | 5-year-old, forearm fracture, backslab applied, discharged. Returns 18 h later with pain and swelling; cast too tight, split. | Related | Physician-related | Preventable |
| 3 | 8-month-old, gastroenteritis, discharged tolerating fluids. Returns 20 h later, well and hydrated, mother anxious about ongoing loose stool. | Related | Patient-related | Preventable *(clearer instructions)* |
| 4 | 6-year-old, asthma exacerbation, treated with salbutamol, discharged without oral steroid. Returns 30 h later with a worse exacerbation, admitted. | Related | Physician-related | Preventable |
| 5 | 3-year-old, seen for febrile illness and discharged. Returns 48 h later after falling from a chair, forehead laceration sutured. | **Unrelated** | Illness-related *(n/a — record as unrelated)* | Not preventable |
| 6 | 10-day-old `[if within study age range]`, seen for poor feeding, discharged. Returns 24 h later, lethargic, sepsis diagnosed, admitted to NICU. | Related | **Depends on documentation** — if vital signs and a full examination were documented as normal, illness-related; if observations were not recorded, physician-related | Judge accordingly |
| 7 | 4-year-old, viral illness, discharged. Returns 60 h later; mother reports she could not obtain the prescribed medication from the pharmacy. | Related | Patient-related | Preventable |
| 8 | 18-month-old, bronchiolitis day 2, mild, discharged appropriately with documented normal saturations and good feeding. Returns day 4 with respiratory distress, admitted. | Related | Illness-related | Not preventable |
| 9 | 2-year-old, viral illness, told to follow up in outpatient clinic in 2 days. Returns to ED 40 h later; record notes the clinic had no appointment before next month. Child assessed, unchanged, discharged. | Related | Illness-related | Not preventable |
| 10 | 5-year-old with pneumonia on oral antibiotics, told to follow up in clinic. Returns to ED 48 h later, still febrile; record notes the family could not travel to the clinic. Admitted. | Related | Illness-related | Not preventable |

**Access-barrier flag for the examples above:** #7 → **Yes** (could not obtain medication). #9 → **Yes** (no clinic appointment available). #10 → **Yes** (could not travel). All others → **No**.

Two examples deserve attention:

- **Example 6** shows that the same clinical outcome falls into different categories depending on what was documented. That is the correct behaviour of this instrument, not a flaw in it.
- **Examples 9 and 10** show why Judgement 4 exists. Without it, both would be filed as "patient-related" — implying the family was at fault, when the clinic route was simply not open to them. The attribution stays illness-related; the access barrier is recorded separately.

---

## 8. Practical rules

1. **Do not discuss cases with the other reviewer.** Independence is the point.
2. **Read both records fully** before deciding anything.
3. **Do not look up the child's later course** beyond the return visit. Judge the pair only.
4. If a case involves you or a close colleague as the treating clinician, **hand it to the adjudicator** and record why.
5. Record **Uncertain** honestly. A reported uncertainty rate is a normal, publishable finding; a guessed classification is a hidden error.
6. Work in blocks of no more than 25 pairs at a sitting. Fatigue degrades agreement.
7. Keep a running list of cases that did not fit the rules. After the pilot we revise this manual once, and only once, before the main classification begins.

---

## 9. Pilot

The first **40 pairs of the 400-pair sample** are a pilot. All reviewers classify all 40. We then:

- calculate kappa,
- review every disagreement together,
- amend this manual where the rules proved unclear,
- and re-issue it as **version 1.0**.

The pilot classifications are **discarded** and those 40 pairs are re-classified under version 1.0 with the rest. Only version 1.0 results enter the analysis.

---

## 10. Authorship note

This classification work is a genuine intellectual contribution and, together with drafting a section of the manuscript and approving the final version, satisfies ICMJE authorship criteria. Data entry alone does not. Reviewers must also participate in interpreting the results and revising the manuscript to qualify as authors.
