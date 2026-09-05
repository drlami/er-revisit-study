# Statistical Analysis Plan

**Study:** Unscheduled 72-hour return visits to the pediatric ED, PMC Ramallah
**Version:** 0.2 — 2026-08-20 (0.1, 2026-08-16, plus §4b pilot stopping rules; written before any data existed)
**Software:** IBM SPSS Statistics `[record version used]`

> **This plan is written before any data has been seen.** That is the point of it. Pre-specifying the analysis is what separates a finding from a fishing expedition, and reviewers increasingly ask whether the plan predated the data. Do not amend it after looking at results; if something must change, record the change, the date, and the reason in §9.

---

## 1. Building the dataset

Performed once, on the raw IT export, before any analysis.

**Step 1 — Clean.** Standardise date/time formats. Check for duplicate visit identifiers. Check age is plausible (0 to <13 years). Record how many rows are removed and why.

**Step 2 — Identify index visits.** Keep visits with disposition = discharged home. Exclude admitted, transferred, died, left against medical advice, left without being seen, and records where discharge cannot be confirmed. **Record the count at each exclusion step — this becomes the STROBE flow diagram.**

**Step 3 — Link returns.** Sort by patient identifier, then by arrival time. For each index visit, look forward for the next visit by the same patient. Compute:

```
hours_to_return = (arrival time of next visit) − (discharge time of index visit)
```

Flag `return_72h = 1` if `0 < hours_to_return ≤ 72`, else `0`.

**Step 4 — Manual check.** Take a random sample of **50 flagged pairs and 50 unflagged visits** and verify the linkage by opening the records. This confirms the patient identifier behaves as IT stated. Report the result in the manuscript methods — it is a cheap, credible validation step.

**Step 5 — Apply return-visit exclusions** (scheduled returns, administrative visits) from the classification review, and recount.

**Step 6 — Pseudonymise.** Replace the patient identifier with a study number. Store the linkage key separately. From this point on the analysis file contains no identifiers.

---

## 2. Primary outcome

**72-hour unscheduled revisit rate**

```
rate = (number of index visits followed by an unscheduled return within 72 h)
       ÷ (total number of eligible discharged index visits) × 100
```

Report as a percentage with a **95% confidence interval** (SPSS: *Analyze → Descriptive Statistics → Frequencies*, then compute the CI for a proportion, or use *Analyze → Compare Means → One-Sample Proportions* depending on version).

**Report the denominator explicitly.** This is the single thing the only comparable regional study (AlAteeq 2026) failed to do, and it is why their result cannot be compared to anything.

Also report the rate **by calendar year** and **by season** to show stability.

**Scheduled returns.** Local practice directs planned follow-up to outpatient clinic rather than the ED, so scheduled ED returns are expected to be rare. This is verified, not assumed: report the proportion of scheduled returns found in the 400-pair classified sample, with its 95% CI. If that proportion is **≤5%**, the crude rate stands as the primary outcome and the scheduled proportion is reported alongside it. If it **exceeds 5%**, report a corrected unscheduled rate as well:

```
corrected rate = crude rate × (1 − proportion scheduled in sample)
```

State which of the two applied.

---

## 3. Secondary outcomes — descriptive

All reported with counts and percentages; continuous variables as median and IQR unless clearly normally distributed, in which case mean and SD.

1. **Reasons for return** — frequency table of presenting complaints at the return visit, ranked.
2. **Disposition at the return visit** — discharged / admitted / transferred / died. **The proportion admitted on return is a headline figure** (comparators: 29.1% in Jamjoom 2026 ≥14 y; 42% in *Emerg Med J* 2017).
3. **Relatedness** — related / unrelated / uncertain.
4. **Attribution** — illness-related / patient-related / physician-related / uncertain. Comparator distribution: 94.9% / 1.6% / 3.5% (*Am J Med Qual* 2016).
5. **Preventability** — preventable / not preventable / uncertain.
6. **Access barriers** — proportion of returns with a documented access barrier, with 95% CI, broken down by type (no clinic appointment / could not reach clinic / could not obtain medication / cost / other). **Report this even if the proportion is low** — a low figure is itself informative, and a high one is the study's most distinctive finding.
7. **Time to return** — median hours and IQR; histogram in 12-hour bands.

Items 3–6 are estimated from the **400-pair classified sample**, not the full cohort, and every such proportion is reported with its 95% confidence interval and the sample denominator stated. Items 1, 2 and 7 come from the full export.

---

## 4. Inter-rater agreement

**Cohen's kappa** for each of the four classification judgements (relatedness, attribution, preventability, access barrier), calculated on the two independent reviewers' codes **before adjudication**.

SPSS: *Analyze → Descriptive Statistics → Crosstabs → Statistics → Kappa*, with the two reviewers' codes as the two variables.

Report kappa with 95% CI and interpret conventionally (<0.20 poor, 0.21–0.40 fair, 0.41–0.60 moderate, 0.61–0.80 good, >0.80 very good). Report the number of cases requiring adjudication.

Report the kappa you actually get. A moderate kappa on a subjective judgement is an honest, publishable result; the adjudication step is what handles it. **Benchmark:** a systematic review of record review (*BMJ Open* 2016, PMID 27550650) pooled kappa at **0.55–0.65** for judgements of this type. A pilot result in that range is normal and is not a reason to change the instrument.

### 4a. Verification sub-analysis — resident against senior classification

**Pre-specified before any data is seen.** Dr Samer Dahdoul independently classifies a random 20% of the sampled pairs (n = 80), blinded to the residents' codes.

Analyse as follows:

1. **Agreement.** Cohen's kappa between the senior reviewer's code and the resident consensus code (the agreed code where the two residents agreed; the adjudicated code where they did not), for each of the four judgements. Report with 95% confidence intervals and raw percentage agreement beside each.
2. **Direction, not just magnitude.** For **attribution** and **preventability**, tabulate the proportion coded physician-related, and the proportion coded preventable, **separately for the senior reviewer and for the resident consensus**, on the same 80 pairs. Compare with McNemar's test. This is the analysis that matters: *Emerg Med J* 2017 found trainees assigned a potential medical deficiency less often than attendings (9% vs 13%), so a lower resident proportion is the specific result to look for.
3. **If a systematic difference is found** (McNemar p < 0.05, or an absolute difference exceeding 5 percentage points in the physician-related proportion), report the main results unchanged **and** add a sensitivity analysis presenting the physician-related and preventable proportions as a range bounded by the two estimates. State the difference plainly in the limitations. **Do not silently re-code the main dataset.**
4. **If no systematic difference is found**, report the kappa and the two proportions, and state that classification by residents did not differ detectably from classification by a senior physician in this sample — which strengthens the main analysis.

**Power note.** With n = 80 this sub-analysis detects only fairly large differences. It is a check for a substantial systematic bias, not a precise estimate, and should be described as such rather than over-interpreted.

---

### 4b. Pilot stopping rules

**Written before the pilot is run and before any real pair has been opened.** A threshold chosen after seeing the result is not a threshold. The five rules below are fixed in advance so that the decision to proceed, to clarify the workbook, or to stop relying on a judgement is made against a rule rather than against a hope.

**What the pilot is.** The first 40 pairs of the 400-pair sample, classified independently by both reviewers under Reviewer Workbook v0.4. Its purpose is to test the instrument, not to produce findings. **The pilot's own classifications are discarded**, and those 40 pairs are classified again under v1.0 together with the remaining 360 (Reviewer Workbook Part C; Coding Manual §9). No pilot figure appears in the manuscript except as a methods sentence describing how the instrument was revised. **The agreement reported in §4 is the v1.0 agreement measured on the 400 pairs, never the pilot's.**

**What the pilot cannot stop.** The primary outcome — the 72-hour return rate and its confidence interval — is computed from the complete export and does not depend on chart classification at all. No pilot result can invalidate it. What these rules decide is what each *classification* judgement is allowed to be used for.

---

#### Rule 1 — agreement thresholds, judgement by judgement

Calculated on the 40 pilot pairs, before adjudication. Report **three numbers together** for every judgement: kappa with its 95% confidence interval, raw percentage agreement, and PABAK (prevalence-adjusted bias-adjusted kappa, computed as `(k × Po − 1) ÷ (k − 1)`, where `Po` is raw agreement and `k` is the number of categories). All three are needed because when one category dominates, kappa can read poorly while the two reviewers agreed on almost every pair.

| Judgement | Proceed as written | Clarify the workbook, then proceed | Do not use as a primary finding |
|---|---|---|---|
| Step 5 Eligibility | kappa ≥ 0.70 | 0.50 – 0.69 | below 0.50 |
| Step 6 Relatedness | kappa ≥ 0.60 | 0.40 – 0.59 | below 0.40 |
| Step 7 Attribution | kappa ≥ 0.55 | 0.35 – 0.54 | below 0.35 |
| Step 8 Preventability | kappa ≥ 0.50 | 0.30 – 0.49 | below 0.30 |
| Step 9 Access barrier | agreement ≥ 90% **and** PABAK ≥ 0.60 | agreement 80 – 89% | agreement below 80% |

**Why the bar is not the same for all five.** Eligibility is close to a factual screen and should agree well. Relatedness sits at the pooled benchmark for record review (0.55–0.65, *BMJ Open* 2016, PMID 27550650). Attribution and preventability are the most subjective judgements in the instrument, and preventability is the one that performs worst in record review generally; holding it to 0.60 would fail an instrument that is behaving normally. Step 9 is judged on agreement and PABAK rather than kappa because a documented access barrier is uncommon, so the table is heavily skewed and kappa becomes unstable on 40 pairs.

**A 40-pair estimate is imprecise and must be read as such.** A kappa near 0.60 measured on 40 pairs carries a 95% confidence interval of roughly ±0.20. Report the interval beside every pilot kappa. **Where the interval straddles a threshold, the PI makes the decision and records the reason in the pilot report (Rule 5).** The point estimate is evidence, not a verdict.

**"Do not use as a primary finding" does not mean the study stops.** It means that judgement is reported descriptively with its measured reliability stated beside it, is kept out of the abstract and out of any comparative claim, and is named in the limitations as a judgement that could not be classified reliably in this setting. That is an honest and publishable result, and a more informative one than a proportion whose reliability was never tested.

---

#### Rule 2 — the uncertain ceiling

Uncertain is a real answer, and a reported uncertainty rate is a normal finding (Reviewer Workbook Part B, rule 4). But when it is chosen often, the category has started absorbing the work the rule should be doing.

Per judgement, taking the **higher** of the two reviewers' rates across the 40 pilot pairs:

- **10% or less** — normal. Proceed.
- **11% to 20%** — the rule is under-specified. Clarify the workbook, then proceed.
- **Above 20%** — rewrite that judgement's rule before the main run, or move the judgement to the third column of Rule 1.

There is no published benchmark for this, and 20% is the team's own judgement, set in advance and recorded here as such. **Uncertain is never recoded as missing and never merged into another category.** It is reported as a category of its own, with its denominator.

---

#### Rule 3 — minutes per pair

A feasibility rule, not a quality rule. Each resident classifies 400 pairs alongside clinical duties, so the pilot is where it becomes clear whether that is real.

**How the time is captured.** No timing column is being added to the coding sheet. Each reviewer keeps a short log — date, clock time started, clock time finished, pairs completed — and minutes per pair is the total minutes divided by pairs completed, per reviewer, across the whole pilot.

- **10 minutes or less** — proceed with 400 pairs (about 67 hours per reviewer, roughly 16 sittings at the 25-pair limit).
- **11 to 15 minutes** — proceed with 400, but the PI extends the timeline or adds sittings **before** the main run starts, not during it (15 minutes per pair is about 100 hours per reviewer).
- **Above 15 minutes** — reduce the classified sample below 400. Recompute the precision the smaller sample buys, state it, and record the change in §9. As an anchor: a proportion near 10% estimated from 400 pairs carries a 95% confidence interval of about ±3 percentage points; from 200 pairs, about ±4. **Do not go below 250 pairs** — below that the access-barrier estimate, the most distinctive finding this study can offer, becomes too imprecise to be worth reporting.

If the sample is reduced, the verification sub-study of §4a shrinks with it, since it is 20% of whatever the final sample is. §4a already detects only large systematic differences at n = 80; below that it should be described as a check rather than an estimate.

---

#### Rule 4 — what may change the workbook, and what may not

Every disagreement is opened at the pilot meeting. **Before the correct answer is discussed**, the PI assigns each disagreement to one of two piles:

**(a) The workbook did not say.** The rule was silent, or the situation did not arise in the shape the rule was written for. → **These, and only these, change the workbook.**

**(b) The workbook said, and the two reviewers weighed the same facts differently.** → The adjudicator decides the pair. **The workbook is left alone.**

The order matters. Assigning the pile before discussing the answer is what stops a genuine difference of judgement from being reclassified after the fact as a wording problem, which is the easy and invisible way to make disagreement disappear.

**Why pile (b) must never change the workbook.** Rewriting the rules until two reviewers can no longer disagree does not produce agreement; it produces one reviewer operating under two names. The disagreement rate is the quantity being measured, and an instrument tuned to suppress it reports a kappa that means nothing.

**The primary evidence for pile (a)** is the Step 10 column *"Was there anything about this pair the workbook did not tell you how to handle?"*. A pair flagged Yes by either reviewer is presumed pile (a) unless the meeting decides otherwise. A pair flagged Yes **independently by both** reviewers is pile (a), and needs no discussion to establish it.

**The workbook is revised once, not iteratively** (Reviewer Workbook Part C; Coding Manual §9). A second pilot is not run. If the revision turns out to be large enough that a second pilot feels necessary, that is itself a signal the judgement is not defined well enough to carry a primary finding, and the third column of Rule 1 applies to it.

---

#### Rule 5 — recording the decision

One page, dated, filed with the study documents **before** the main classification begins. It carries:

1. the agreement table — kappa, 95% confidence interval, raw agreement and PABAK, for each of the five judgements;
2. the uncertain rate, per judgement and per reviewer;
3. minutes per pair, per reviewer;
4. the number of disagreements in pile (a) and in pile (b);
5. the decision for each of the five judgements — proceed, clarify, or do not use as a primary finding — each with one line of reasoning;
6. the workbook changes made, as a numbered list.

This page becomes the methods paragraph describing instrument development, and it is the document to produce if a reviewer asks whether the thresholds predated the result.

**This section was written before any real pair existed. It is not an amendment under §9.**

---

## 5. Primary analytic model

**Multivariable binary logistic regression.** Outcome: unscheduled return within 72 hours (1/0). Unit of analysis: the discharged index visit.

**Candidate predictors — fixed in advance, chosen on clinical grounds, not by the data:**

| Predictor | Form |
|---|---|
| Age band | <1 y / 1–4 y / 5–8 y / 9–12 y (categorical, reference 5–8 y) |
| Sex | Male / female |
| Index diagnosis category | Grouped (see `DATA-DICTIONARY.md`), reference = respiratory |
| Arrival time of day | Day (08:00–15:59) / evening (16:00–23:59) / night (00:00–07:59) |
| Weekend or public holiday arrival | Yes / no |
| Season | Winter / spring / summer / autumn |
| ED length of stay | Continuous (hours) |
| Any medication prescribed at index visit | Yes / no |
| Antibiotic prescribed at index visit | Yes / no |
| Any investigation performed at index visit | Yes / no |
| Prior ED visit in preceding 30 days | Yes / no |

**Do not use stepwise selection.** Enter all pre-specified predictors together. Stepwise procedures capitalise on chance and are routinely criticised by reviewers.

**Reporting:** adjusted odds ratios with 95% CI and p-values; model fit by Hosmer–Lemeshow test and Nagelkerke R²; sample size entering the model.

**Clustering:** children may contribute more than one index visit. The primary model uses standard logistic regression, with a **sensitivity analysis restricted to each child's first eligible index visit only** to confirm the findings are not driven by repeat attenders. If SPSS Complex Samples or GENLIN with GEE is available, a clustered model by patient is preferred and should be reported as the sensitivity analysis instead.

**Events per variable:** with an expected 1,100–2,900 events and 11 predictors (roughly 15 degrees of freedom once categories are expanded), the conventional 10-events-per-variable rule is met with a wide margin.

---

## 6. Secondary model

Among return visits only: **logistic regression for admission at the return visit**, with the same predictor set plus attribution category. Run only if the number of admitted returns exceeds 100; otherwise report descriptively and say so.

---

## 7. Missing data

- Report missingness for every variable in the baseline table.
- Primary analysis is **complete-case**.
- If any single variable is missing in more than 10% of records, state it prominently and consider dropping that variable from the model rather than imputing.
- No multiple imputation in the primary analysis. If it is added later as a sensitivity analysis, record that as a protocol amendment in §9.

---

## 8. Tables and figures planned

| Output | Content |
|---|---|
| **Figure 1** | STROBE flow diagram — all visits → eligible index visits → returns identified → returns classified |
| **Table 1** | Characteristics of all eligible index visits, and comparison of those with vs without a 72-hour return (unadjusted) |
| **Table 2** | Reasons for return and disposition at the return visit |
| **Table 3** | Classification: relatedness, attribution, preventability — with kappa |
| **Table 4** | Multivariable logistic regression: adjusted ORs with 95% CI |
| **Figure 2** | Distribution of time to return, in 12-hour bands |

---

## 9. Amendments to this plan

Any change made after data inspection is recorded here with date and reason. An empty section at submission is a good sign.

| Date | Change | Reason |
|---|---|---|
| | | |

---

## 10. Note on statistical support

No statistician is available to the team. The analysis will be carried out by the PI with Claude's support. Two consequences follow, and both are non-negotiable:

1. **This must be disclosed in the manuscript** per ICMJE — AI cannot be an author, and the human authors take full responsibility for the analysis and its interpretation.
2. Approaching a statistician at An-Najah, Al-Quds or Birzeit for co-authorship remains worthwhile and would strengthen the paper. See `STATUS.md` open decisions.
