# Team Briefing — 72-Hour ED Return Visit Study

**Study:** Unscheduled 72-hour return visits to the pediatric emergency department of a Palestinian governmental hospital — rate, reasons, and predictors
**Site:** Palestine Medical Complex (PMC), Ramallah
**PI:** Dr Lami Qurt
**For:** the team meeting — 2026-08-17

> This is the short version, written for discussion. The full detail is in `PROTOCOL.md`, `CODING-MANUAL.md` and `ANALYSIS-PLAN.md` in the same folder. Read this one first.

---

## 1. The question, in one paragraph

When we discharge a child from our emergency department, how often does that child come back within 72 hours? Why do they come back? And can we tell in advance which children are likely to?

Early unplanned return to the ED is used worldwide as a quality and safety indicator. **It has never been measured in Palestine.**

---

## 2. Why this study is worth doing

- **No patient-level pediatric ED research has ever been published from Palestine.** The only Palestinian pediatric-ED paper (Shawahna 2024) counted *equipment* in 30 emergency departments. It described no patients.
- **The whole Arab world has only two studies on this topic in children**, both from big children's hospitals in Saudi Arabia. The first (AlAteeq 2026, Riyadh) counted 300 children who came back **but never said how many children were sent home in total** — so no rate can be worked out from it, and it cannot be compared with anything. The second (Ahmed 2018) included only children with long-term illnesses, not all children. We will report the total, and we will include every child. That alone makes our paper more useful than either of them.
- **Our setting changes the meaning of the number.** There is no triage system anywhere in Palestine. PMC is a first-contact hospital, not only a referral centre — families come to us directly — and after-hours primary care is largely unavailable, so our ED is the first point of contact, not a safety net. Movement restrictions affect whether a family can come back at all. So our revisit rate measures the health system, not only clinical judgement. **This is the idea that makes the paper publishable internationally — not just a local number.**
- **Being honest about what is new matters.** Coming back to the emergency department within 72 hours has been studied 769 times in children around the world. We are not the first to ask the question and we must not say we are — reviewers in this field would spot it immediately. What is new is where we ask it and how. In particular: almost every published method for working out which children will come back depends on a triage score, and we have no triage. Nobody has published this from a department without triage. **Lead with that, and mention Palestine second** — if we open with "the first study in Palestine", reviewers read it as a local audit and stop there.

---

## 3. What we are measuring

| | |
|---|---|
| **Population** | Every child **under 13** seen in the PMC pediatric ED and **discharged home**. By MoH rule pediatrics is 0 to under 13; older children go to the adult ER, so this is the whole department |
| **Period** | 1 January 2024 – 31 December 2025 (2 full years, 2 winter seasons) |
| **The event we count** | The same child comes back to the same ED within **72 hours of discharge**, not planned |
| **Main result** | % of discharged children who return within 72 hours |
| **Also** | Why they returned, how many were admitted on return, and what predicts return |

**The 72-hour clock starts at discharge**, not at arrival.

---

## 4. How we collect the data — two separate tracks

This is the most important thing to understand about the design. **We are not reading 58,000 charts.** The computer does the counting; we only do the thinking.

### Track A — the full export (the computer's job)

IT gives us **one Excel file: one row per pediatric ED visit** over the two years. Roughly 64,000 rows.

Fields requested: patient number, visit number, arrival time, discharge time, age, sex, diagnosis, disposition, medications given, investigations done, and — if available — clinician code and locality.

We then do this on the file, not on paper:

1. Keep only visits that ended in **discharge home** → these are our *index visits* (~55,000–58,000 expected).
2. Sort by patient number, then by time.
3. For each index visit, look forward: did this same child come back? If the next arrival is **within 72 hours of discharge**, flag it as a return.
4. That gives us the rate, the time-to-return, the return diagnosis and the return disposition — **automatically, for every single case.**

> **The one assumption everything rests on:** the patient identifier must be the *same number for the same child across visits*. If the system issues a new number each visit, we cannot link visits and the study must be redesigned. **We ask IT this before anything else begins.**
>
> We also hand-check 50 flagged and 50 unflagged pairs against the actual records to prove the linkage works. This check goes into the paper.

### Track B — the 400-pair chart review (our job)

The computer can tell us *that* a child came back. It cannot tell us *why*. That needs a doctor.

So we take a **random sample of 400 return pairs** — not all of them — and two reviewers read both records (index visit + return visit) and answer four questions about each pair.

**Why 400 and not all of them:** 400 pairs gives a proportion accurate to about ±5%, which is more than enough. Reading all of them would take roughly 470 hours. Reading 400 takes about **93 hours across the team** — realistic alongside clinical work.

**The four judgements for each pair:**

| # | Question | Answers |
|---|---|---|
| 1 | Is the return **related** to the first visit? | Related / Unrelated / Uncertain |
| 2 | **Why** did they come back? | Illness-related / Patient-related / Physician-related / Uncertain |
| 3 | Was it **preventable**? | Preventable / Not preventable / Uncertain |
| 4 | Was there an **access barrier**? | Yes / No / Uncertain |

Definitions, rules and 10 worked examples are in `CODING-MANUAL.md`. Everyone reads it and works through the 10 examples together **before** starting.

**Three rules that are not negotiable:**

1. **The two reviewers work independently and do not discuss cases.** If we discuss, our agreement statistic becomes meaningless and that section of the paper is lost.
2. **Judge only on what was documented and knowable at the time.** Never with hindsight. A serious outcome does not automatically mean someone made an error. The question is always: *was the decision reasonable given what was in front of the doctor?*
3. **A third senior reviewer settles disagreements.** Disagreement is expected and is part of the output, not a failure of it.

**A pilot first:** the first **40 of the 400 pairs** are a practice run. We all classify them, compare, fix any unclear rules in the manual, then **discard those 40 results** and redo them properly with the rest.

---

## 5. Judgement 4 — the part that is ours alone

This deserves its own section, because it is probably the most original thing in the study.

At PMC we tell families to follow up **in outpatient clinic**. When a family comes back to the ED instead, the standard international taxonomy files that as **"patient-related"** — which implies the family did something wrong.

Often they did not. They came back because the clinic route was **closed to them**: no appointment for weeks, no transport, cost, distance, a checkpoint.

That is not a caregiver failure. It is a **health-system access failure** — and in our setting it may be the single most important thing this study can show. So we record it as a **separate flag**, independent of the "why" question. A case can be illness-related *and* carry an access barrier.

**We code it YES only when the record actually says so** — never on our own inference. No published estimate for this exists anywhere, because nobody has measured it. That is exactly the point.

---

## 6. How we will compare the results

Three comparisons, in order of importance.

### (a) Against the published international literature

| What we measure | Published benchmark | Source |
|---|---|---|
| 72-hour revisit rate | **2.4% – 7.5%** | Multiple international studies |
| Admitted on return | **29% – 42%** | Jamjoom 2026 (≥14y, 29.1%); Emerg Med J 2017 (42%) |
| Illness / Patient / Physician split | **94.9% / 1.6% / 3.5%** | Am J Med Qual 2016 |
| Reviewer disagreement | **~25%** between consultants and trainees | Emerg Med J 2017 |
| Returns going to a *different* hospital | **~11%** — invisible to us | Ann Emerg Med 2018 |
| Access barriers | **No benchmark exists** | — this is new |

If our rate sits inside the international range, the finding is *"a system without triage or after-hours primary care performs comparably."* If it sits well above it, the finding is *"the absence of primary care pushes families back to the ED."* **Either result is publishable.** We are not hoping for a particular number.

### (b) Within our own data — who returns vs who does not

We compare the ~55,000 children who did not return against the ~1,100–2,900 who did, across every variable we have, then run a **multivariable logistic regression** to find which factors independently predict return.

**The 11 predictors are fixed in advance** — chosen on clinical grounds, before we see any data:

age band · sex · diagnosis group · time of day of arrival · weekend/holiday · season · length of stay in ED · any medication given · antibiotic given · any investigation done · previous ED visit in the last 30 days

> **We do not use stepwise selection.** All 11 go into the model together. Choosing predictors by what looks significant in the data is a known statistical error, and reviewers reject it.

### (c) Over time, within the study period

Rate by year and by season, to show the number is stable and not an artefact of one bad winter.

---

## 7. What results we expect — in detail

These are **expectations to be tested, not findings.** Writing them down before we see the data is deliberate: it stops us from rewriting the story afterwards to fit whatever we happen to find.

### The headline numbers

| Result | What we expect | Comment |
|---|---|---|
| Total pediatric ED visits, 2 years | ~64,000 | To be confirmed with IT. No age-based reduction applies — the pediatric ED is an under-13 department, so its volume already is our volume |
| Discharged home — our denominator | ~55,000 – 58,000 | |
| **72-hour revisit rate** | **2 – 5%** | The primary result. Plausibly higher here than in high-income systems, because our ED is the only after-hours option |
| Number of return visits | **~1,100 – 2,900** | Ample for the regression either way |
| Admitted on the return visit | **~25 – 40%** | A high figure means real illness, not anxiety — it strengthens the paper |
| Median time to return | **~24 – 48 hours** | Most returns cluster on day 2 |

### The 400 classified pairs

| Judgement | What we expect | Why it matters |
|---|---|---|
| Related to the index visit | **80 – 90%** | Most returns are the same illness continuing |
| Scheduled returns (excluded) | **under 5%** | We direct follow-up to clinic, not ED. **If this exceeds 5% we must publish a corrected rate** — so record it carefully |
| Illness-related | **~85 – 95%** | Should be the large majority, as internationally |
| Patient-related | **~2 – 10%** | |
| **Physician-related** | **~3 – 8%** | The sensitive number. Small everywhere. We report it honestly, whatever it is |
| Preventable | **~10 – 25%** | Not the same as physician-related — clearer instructions can prevent a patient-related return |
| **Access barrier documented** | **Unknown — no published estimate** | The novel figure. **A low result is still worth reporting**; a high result is the study's most distinctive finding |
| Cohen's kappa (agreement) | **0.4 – 0.7** | Moderate-to-good is normal and publishable for a judgement like this. A near-perfect kappa would be suspicious |

### The predictors — our clinical hypotheses

| Factor | Expected direction |
|---|---|
| Age under 1 year | **Higher** risk of return |
| Respiratory diagnosis | **Higher** — bronchiolitis and asthma naturally worsen on days 3–5 |
| Fever without a source | **Higher** — the illness has not declared itself yet |
| Night arrival | **Higher** — shorter assessment, fewer staff |
| No investigation performed | **Higher** |
| Previous ED visit in the last 30 days | **Higher** — the strongest predictor in most published studies |
| Trauma / injury | **Lower** — the problem is resolved at the first visit |

### What we will publish

**Figure 1** patient flow · **Table 1** returners vs non-returners · **Table 2** reasons and disposition · **Table 3** classification with kappa · **Table 4** regression odds ratios · **Figure 2** time to return

**Target journals** — indexing to be verified before submission: *BMC Pediatrics*, *BMC Emergency Medicine*, *Pediatric Emergency Care*, *International Journal of Emergency Medicine*, *EMHJ*, *IJID Regions*.

### What we are honest about — the limitations

1. **A child who goes to a different hospital is invisible to us.** Internationally that is about 11% of all returns, so our rate is an underestimate. We say so plainly.
2. **No triage system exists**, so we have no measure of how sick the child was at the first visit and cannot adjust for severity.
3. **Single centre.** PMC serves its own catchment directly as well as receiving referrals, so our case mix is closer to ordinary pediatric ED practice than a purely tertiary hospital's would be — but one governmental hospital may still not represent every Palestinian ED.
4. **Attribution is a retrospective judgement from records** — reduced but not eliminated by using two independent reviewers.
5. **Documentation quality in routine care limits what we can see.**

---

## 8. The steps — where we are, and what happens next

| # | Step | Status |
|---|---|---|
| 1 | Choose the topic | ✅ Done — 16 Aug 2026 |
| 2 | Literature search, confirm the gap | ✅ Done — PubMed |
| 3 | Write protocol and tools | ✅ Done — all documents drafted |
| 4 | **Check nobody locally is doing this already** | 🟡 Thesis repositories clear, and the MoH research office confirms no similar study on record (17 Aug). **Still to ask: our own ED and pediatric colleagues** |
| 5 | **Team agreement + author order** | ⬜ **This meeting** |
| 6 | Ethics approval via the MoH research office | 🟡 Proposal ready to send — **the long pole, 4–12 weeks** |
| 7 | HIS access letter to Dept of Continuous Education | 🟡 Letter ready, Arabic + English |
| 8 | IT produces the data export | ⬜ Field list ready — **blocked: IT will not export before ethics approval** |
| 9 | Build and check the dataset | ⬜ |
| 10 | Pilot: 40 pairs, then fix the manual | ⬜ |
| 11 | Classify the 400 pairs | ⬜ ~93 hours across the team |
| 12 | Analysis in SPSS | ⬜ Plan already written |
| 13 | Write the manuscript, STROBE format | ⬜ |
| 14 | Submit | ⬜ |

**Everything from step 8 onward is blocked until ethics approval arrives** — IT will not release the export before it. That is why steps 4 to 7 must all happen this week.

One exception worth pursuing now: the **two questions for IT** — is the patient number the same across visits, and how many visits are in the date range — ask about how the system behaves, not for any patient data. They should not need approval, and the first determines whether the study is feasible at all.

---

## 9. Who does what

| Role | Person | Job |
|---|---|---|
| PI / first author | **Dr Lami Qurt** | Runs the study, does the analysis, writes the paper. Makes **no** judgements on any pair |
| Senior author + checking reviewer | **Dr Samer Dahdoul** | Clinical oversight and final approval. Also re-reads a random **80 of the 400 pairs** without seeing anyone's answers (about 9 hours) |
| Reviewer 1 | **Dr Waad** | Classifies all 400 pairs, alone (about 47 hours) |
| Reviewer 2 | **Dr Ainaa** | Classifies the same 400 pairs, alone, never seeing Dr Waad's answers (about 47 hours) |
| Reviewer 3 — "adjudicator" in the protocol | **Dr Amani Salman** | Reads **only** the pairs where Dr Waad and Dr Ainaa disagreed — about 60 — and decides the final answer (about 7 hours) |
| Statistician | None available | Analysis by the PI with AI assistance — **disclosed in the paper** |

### Authorship — please read this carefully

Under **ICMJE rules, collecting data is not enough to make someone an author.** To qualify, each person must also:

1. help **interpret** the results,
2. **write or revise** part of the manuscript, and
3. **approve** the final version.

The classification work **does** count as a genuine intellectual contribution. But it earns authorship only if you also do 1, 2 and 3. **We agree author order now, in writing, before any classification starts** — not afterwards.

AI assistance will be disclosed in the manuscript as required. AI cannot be an author.

---

## 10. Decisions needed at this meeting

1. **Confirm the roles above and agree author order.** The names are filled in; what is still needed is everyone's agreement and signature, and the **full names of Dr Waad and Dr Ainaa** for the submission.
2. **Author order** — agreed and written down.
3. **Confirm the study period** — 1 Jan 2024 to 31 Dec 2025.
4. **Who asks IT the two questions?** (Is the patient number the same for the same child across visits? How many pediatric ED visits are in this date range?) Nothing can start until we know.
5. **Who asks around** whether anyone at PMC or in the MoH is already doing this study?
6. **Do we invite a statistician** from An-Najah / Al-Quds / Birzeit as a co-author?
7. **Realistic weekly hours** each reviewer can give to the 400 pairs.

---

## 11. The one-sentence version

*We will use the ED computer system to count how many children come back within 72 hours of being sent home, read 400 of those cases carefully to understand why, and report both the number and the reasons — which has never been done in Palestine, and which will show whether children return because illness is unpredictable, or because there was nowhere else for them to go.*
