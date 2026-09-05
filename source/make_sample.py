# -*- coding: utf-8 -*-
"""Generate a SYNTHETIC 40-pair reviewer dataset and its reliability output."""
import io, sys

# pair, scenario, elig1, elig2, rel1, rel2, att1, att2, prev1, prev2, acc1, acc2
# 0 = not applicable / not recorded
D = [
(1,"8-month-old, bronchiolitis day 2, saturations and feeding documented normal, discharged. Returns day 4 with respiratory distress, admitted.",1,1,1,1,1,1,2,2,2,2),
(2,"3-year-old, gastroenteritis, tolerating oral fluids at discharge. Returns 14 h later, well and hydrated, mother anxious about loose stool.",1,1,1,1,2,2,1,1,2,2),
(3,"4-year-old, limp and fever, no hip examination documented, no investigations. Returns 26 h later, septic arthritis, admitted.",1,1,1,1,3,3,1,1,2,2),
(4,"2-year-old, febrile URTI, antipyretic advice. Returns 36 h later still febrile, otitis media found, antibiotic started.",1,1,1,1,1,1,2,2,2,2),
(5,"5-year-old, forearm fracture, backslab applied. Returns 18 h later with pain and swelling, cast too tight, split.",1,1,1,1,3,3,1,1,2,2),
(6,"6-year-old, asthma exacerbation, salbutamol given, discharged without oral steroid. Returns 30 h later worse, admitted.",1,1,1,1,3,1,1,2,2,2),
(7,"3-year-old, febrile illness, discharged. Returns 48 h later after falling from a chair, forehead laceration sutured.",1,1,2,2,0,0,2,2,2,2),
(8,"10-month-old, fever, vital signs and full examination documented normal. Returns 24 h later lethargic, sepsis, admitted.",1,1,1,1,1,1,2,2,2,2),
(9,"4-year-old, viral illness, antibiotic prescribed. Returns 60 h later; mother reports she could not obtain the medicine from the pharmacy.",1,1,1,1,2,2,1,1,1,1),
(10,"2-year-old, viral illness, told to follow up in outpatient clinic in 2 days. Returns 40 h later; record notes no clinic appointment before next month. Unchanged, discharged.",1,1,1,1,1,1,2,2,1,1),
(11,"5-year-old, pneumonia on oral antibiotics, clinic follow-up advised. Returns 48 h later still febrile; record notes the family could not travel to the clinic. Admitted.",1,1,1,1,1,1,2,2,1,1),
(12,"18-month-old, gastroenteritis, oral rehydration instructions documented. Returns 20 h later vomiting persistently, IV fluids, admitted.",1,1,1,1,1,1,2,2,2,2),
(13,"7-year-old, abdominal pain, no bloods and no reassessment documented. Returns 30 h later, appendicitis, surgery.",1,1,1,1,3,3,1,1,2,2),
(14,"1-year-old, fever, told at the index visit to come back to the ED the next day for review. Returns 22 h later for that review.",2,2,0,0,0,0,0,0,0,0),
(15,"9-year-old, headache, discharged. Returns 50 h later for a medical certificate only, no clinical assessment recorded.",3,3,0,0,0,0,0,0,0,0),
(16,"3-month-old, poor feeding. Index note has no examination, no vital signs and no diagnosis recorded. Returns 30 h later, admitted.",4,4,0,0,0,0,0,0,0,0),
(17,"6-month-old, bronchiolitis, saturations documented 96 percent, feeding well. Returns 36 h later feeding poorly, admitted.",1,1,1,1,1,1,2,2,2,2),
(18,"4-year-old, croup, dexamethasone given, observed and discharged. Returns 28 h later with stridor at rest, admitted.",1,1,1,1,1,1,2,2,2,2),
(19,"2-year-old, gastroenteritis. Returns 18 h later, mother reports no improvement; child well and hydrated on assessment, discharged.",1,1,1,1,2,2,1,1,2,2),
(20,"11-year-old, tonsillitis, amoxicillin prescribed. Returns 44 h later with a rash, possible drug reaction.",1,1,1,1,1,1,2,3,2,2),
(21,"5-year-old, fever without source, no urine test performed. Returns 40 h later, urinary tract infection diagnosed.",1,1,1,1,3,3,1,1,2,2),
(22,"3-year-old, wheeze, salbutamol given, no inhaler or spacer instruction documented. Returns 34 h later wheezing, treated and discharged.",1,1,1,1,3,2,1,1,2,2),
(23,"7-month-old, fever after routine vaccination, reassurance given. Returns 24 h later, child well, reassured again.",1,1,1,1,2,2,1,2,2,2),
(24,"8-year-old, head injury, head injury advice documented in full. Returns 30 h later vomiting, CT normal, discharged.",1,1,1,1,1,1,2,2,2,2),
(25,"2-year-old, febrile convulsion, advice given and documented. Returns 46 h later after a second convulsion, admitted.",1,1,1,1,1,1,2,2,2,2),
(26,"4-month-old, colic, examined and discharged. Returns 20 h later crying, examination normal, reassurance.",1,1,1,1,2,2,1,1,2,2),
(27,"10-year-old, ankle injury, no x-ray performed. Returns 60 h later with persistent pain, x-ray now shows a fracture.",1,1,1,1,3,3,1,1,2,2),
(28,"6-year-old, gastroenteritis, no weight and no hydration status documented. Returns 30 h later dehydrated, IV fluids.",1,1,1,1,3,1,1,3,2,2),
(29,"1-year-old, URTI, discharged. Returns 52 h later with a rash, viral exanthem diagnosed, discharged.",1,1,1,1,1,1,2,2,2,2),
(30,"3-year-old, foreign body in ear, not removed, referred to the ENT clinic. Returns 36 h later; record notes the ENT clinic could not give an appointment.",1,1,1,1,1,1,2,2,1,1),
(31,"9-month-old, bronchiolitis, discharged. Returns 30 h later; record notes the family was delayed reaching the hospital because of a closed road.",1,1,1,1,1,1,2,2,1,3),
(32,"5-year-old, pharyngitis, discharged. Returns 40 h later after a dog bite, wound cleaned and vaccinated.",1,1,2,2,0,0,2,2,2,2),
(33,"2-year-old, pneumonia, oral antibiotic prescribed. Returns 44 h later; the child has vomited every dose of the antibiotic.",1,1,1,1,1,2,3,1,2,2),
(34,"12-year-old, abdominal pain, examined and discharged. Returns 24 h later, constipation diagnosed and treated.",1,1,1,1,1,1,2,2,2,2),
(35,"7-month-old, fever, urine sample recorded as not obtained. Returns 36 h later, urinary tract infection diagnosed, admitted.",1,1,1,3,3,4,1,3,2,2),
(36,"4-year-old, burn dressing applied, told to attend the clinic in 3 days. Returns to the ED 30 h later with the dressing soaked; dressing redone.",1,2,1,0,1,0,2,0,2,0),
(37,"3-year-old, viral illness, discharged. Returns 66 h later with a new limp, transient synovitis diagnosed.",1,1,1,2,1,1,2,2,2,2),
(38,"6-month-old, fever, examined and discharged with advice. Returns 28 h later still febrile, admitted for observation.",1,1,1,1,1,1,2,2,2,2),
(39,"8-year-old, asthma, inhaler prescribed. Returns 50 h later wheezing; record notes the family could not afford the inhaler.",1,1,1,1,2,2,1,1,1,1),
(40,"5-year-old, gastroenteritis, discharged tolerating fluids. Returns 32 h later, child well, father requested a second opinion.",1,1,1,1,2,2,1,2,2,2),
]

ELIG = {1:"1 eligible", 2:"2 scheduled", 3:"3 administrative", 4:"4 insufficient documentation"}


def crosstab(rows, cats):
    t = {(a, b): 0 for a in cats for b in cats}
    for a, b in rows:
        t[(a, b)] += 1
    return t


def stats(rows, cats):
    n = len(rows)
    t = crosstab(rows, cats)
    po = sum(t[(c, c)] for c in cats) / float(n)
    pe = 0.0
    for c in cats:
        r = sum(t[(c, b)] for b in cats)
        col = sum(t[(a, c)] for a in cats)
        pe += (r * col) / float(n * n)
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    kk = len(cats)
    pabak = (kk * po - 1) / float(kk - 1)
    se = (po * (1 - po) / (n * (1 - pe) ** 2)) ** 0.5 if pe < 1 else float("nan")
    return n, t, po, pe, k, pabak, se


def tabmd(title, t, cats, labels):
    out = ["| %s | %s | Row total |" % (title, " | ".join("R2 = " + labels[c] for c in cats))]
    out.append("|" + "---|" * (len(cats) + 2))
    for a in cats:
        row = [t[(a, b)] for b in cats]
        out.append("| **R1 = %s** | %s | %d |" % (labels[a], " | ".join(str(v) for v in row), sum(row)))
    cols = [sum(t[(a, b)] for a in cats) for b in cats]
    out.append("| **Column total** | %s | **%d** |" % (" | ".join(str(v) for v in cols), sum(cols)))
    return "\n".join(out)


REL = {1: "related", 2: "unrelated", 3: "uncertain"}
ATT = {1: "illness", 2: "patient", 3: "physician", 4: "uncertain"}
PRV = {1: "preventable", 2: "not prev.", 3: "uncertain"}
ACC = {1: "yes", 2: "no", 3: "uncertain"}

both_eligible = [d for d in D if d[2] == 1 and d[3] == 1]
rel = [(d[4], d[5]) for d in both_eligible]
att = [(d[6], d[7]) for d in both_eligible if d[6] and d[7]]
prv = [(d[8], d[9]) for d in both_eligible]
acc = [(d[10], d[11]) for d in both_eligible]

L = []
w = L.append

w("# Sample Reviewer Data — SYNTHETIC")
w("")
w("**Study:** Unscheduled 72-hour return visits to the pediatric ED, PMC Ramallah")
w("**Purpose:** worked example of how 40 pilot pairs are recorded and analysed")
w("**Created:** 2026-08-18")
w("")
w("---")
w("")
w("## THESE ARE NOT REAL PATIENTS")
w("")
w("Every case below is **invented**. No record was consulted, no patient exists, and no number here describes anything that happened at PMC or anywhere else. The cases were written to look plausible so that the arithmetic and the layout can be tested before the real data arrives.")
w("")
w("**Do not cite any figure in this document. Do not put it in the ethics file. Do not circulate it without this page attached.** When the real pilot is done, this file is deleted.")
w("")
w("---")
w("")
w("## 1. What this document is for")
w("")
w("Three things:")
w("")
w("- to show the reviewers what a completed set of 40 pairs looks like;")
w("- to show what has to be typed into the spreadsheet, and in what shape;")
w("- to show what comes out at the end, and how it is read.")
w("")
w("The workbook records far more per pair than appears here. This document keeps only the codes, because the codes are what the reliability analysis uses.")
w("")
w("---")
w("")
w("## 2. Code key")
w("")
w("**R1 is Reviewer 1 and R2 is Reviewer 2** — the two physicians who classify every pair independently, without seeing each other's work. Where their codes match, they agreed. Where the codes differ, the pair goes to the adjudicator, Reviewer 3, and it is those differences that kappa measures.")
w("")
w("| Judgement | Codes |")
w("|---|---|")
w("| Eligibility (Step 5) | 1 eligible, 2 scheduled, 3 administrative, 4 insufficient documentation |")
w("| Relatedness (Step 6) | 1 related, 2 unrelated, 3 uncertain |")
w("| Attribution (Step 7) | 1 illness-related, 2 patient-related, 3 physician-related, 4 uncertain |")
w("| Preventability (Step 8) | 1 preventable, 2 not preventable, 3 uncertain |")
w("| Access barrier (Step 9) | 1 yes, 2 no, 3 uncertain |")
w("")
w("A dash means the field does not apply: the pair was excluded at Step 5, or the return was coded unrelated, in which case attribution is not recorded.")
w("")
w("---")
w("")
w("## 3. The 40 pairs")
w("")
w("The last column shows **Reviewer 1's eligibility code, then Reviewer 2's**, separated by a slash. Two identical numbers mean the reviewers agreed: 1 / 1 both eligible, 2 / 2 both scheduled, 3 / 3 both administrative, 4 / 4 both insufficient documentation. Only pair 36 differs.")
w("")
w("| # | Case | Eligibility R1 / R2 |")
w("|---|---|---|")
for d in D:
    e = "%d / %d" % (d[2], d[3])
    w("| %d | %s | %s |" % (d[0], d[1], e))
w("")
w("---")
w("")
w("## 4. The coding sheet")
w("")
w("This is the whole input to the reliability analysis: one row per pair, two columns per judgement.")
w("")
w("**Rel** is relatedness (Step 6), **Att** attribution (Step 7), **Prev** preventability (Step 8), **Acc** access barrier (Step 9). **R1** is Reviewer 1 and **R2** is Reviewer 2, so each judgement takes two columns, one per reviewer. The numbers are the codes in section 2.")
w("")
w("| # | Rel R1 | Rel R2 | Att R1 | Att R2 | Prev R1 | Prev R2 | Acc R1 | Acc R2 |")
w("|---|---|---|---|---|---|---|---|---|")
for d in D:
    cells = ["-" if v == 0 else str(v) for v in d[4:12]]
    w("| %d | %s |" % (d[0], " | ".join(cells)))
w("")
w("---")
w("")
w("## 5. Who is counted, and who is not")
w("")
n_ex = len([d for d in D if d[2] in (2, 3, 4) and d[3] in (2, 3, 4)])
n_disp = len([d for d in D if (d[2] == 1) != (d[3] == 1)])
w("| Group | n | Effect |")
w("|---|---|---|")
w("| Pairs in the pilot | 40 | |")
w("| Excluded at Step 5 by **both** reviewers | %d | Removed from all four analyses |" % n_ex)
w("| **Eligibility disputed** between reviewers (pair 36) | %d | Removed from the four kappas; the adjudicator decides eligibility |" % n_disp)
w("| Pairs contributing to relatedness, preventability, access | %d | |" % len(both_eligible))
w("| Pairs contributing to attribution | %d | Two further pairs coded unrelated by both, so attribution does not apply |" % len(att))
w("")
w("> **The denominators are not all the same, and that is correct.** Each judgement is computed on the pairs where both reviewers actually made that judgement. Report the denominator next to every kappa, or a reader cannot check your arithmetic.")
w("")
w("---")
w("")
w("## 6. Agreement tables")
w("")

blocks = [("Relatedness", rel, [1, 2, 3], REL),
          ("Attribution", att, [1, 2, 3, 4], ATT),
          ("Preventability", prv, [1, 2, 3], PRV),
          ("Access barrier", acc, [1, 2, 3], ACC)]

results = []
for name, rows, cats, labels in blocks:
    n, t, po, pe, k, pabak, se = stats(rows, cats)
    results.append((name, n, po, k, pabak, se))
    w("### %s (n = %d)" % (name, n))
    w("")
    w(tabmd("", t, cats, labels))
    w("")
    lo, hi = max(-1.0, k - 1.96 * se), min(1.0, k + 1.96 * se)
    w("Observed agreement Po = **%.3f** (%d of %d). Expected agreement Pe = %.3f. "
      "Kappa = (%.3f − %.3f) / (1 − %.3f) = **%.2f**, 95%% CI %.2f to %.2f. "
      "PABAK = (%d × %.3f − 1) / %d = **%.2f**."
      % (po, int(round(po * n)), n, pe, po, pe, pe, k, lo, hi, len(cats), po, len(cats) - 1, pabak))
    w("")

w("---")
w("")
w("## 7. Results, as they would be reported")
w("")
THRESH = {"Relatedness": 0.60, "Attribution": 0.40, "Preventability": 0.40, "Access barrier": 0.40}
UNC = {"Relatedness": (rel, 3), "Attribution": (att, 4), "Preventability": (prv, 3), "Access barrier": (acc, 3)}

w("| Judgement | n | Agreement | Kappa (95% CI) | PABAK | Uncertain | Against the stopping rule |")
w("|---|---|---|---|---|---|---|")
for name, n, po, k, pabak, se in results:
    rows_, ucode = UNC[name]
    unc = sum(1 for a, b in rows_ for v in (a, b) if v == ucode) / float(2 * n)
    verdict = "green, continue" if k >= THRESH[name] else "amber, revise and re-pilot"
    w("| %s | %d | %.1f%% | %.2f (%.2f to %.2f) | %.2f | %.1f%% | %s |"
      % (name, n, po * 100, k, max(-1.0, k - 1.96 * se), min(1.0, k + 1.96 * se), pabak, unc * 100, verdict))
w("")
w("---")
w("")
w("## 8. How to read this")
w("")
rel_n, rel_po, rel_k = results[0][1], results[0][2], results[0][3]
att_n, att_po, att_k = results[1][1], results[1][2], results[1][3]
w("**Compare the first two rows, and the whole problem with kappa is in front of you.**")
w("")
w("| | Reviewers agreed on | Kappa |")
w("|---|---|---|")
w("| Relatedness | %d of %d, %.1f%% | %.2f |" % (int(round(rel_po * rel_n)), rel_n, rel_po * 100, rel_k))
w("| Attribution | %d of %d, %.1f%% | %.2f |" % (int(round(att_po * att_n)), att_n, att_po * 100, att_k))
w("")
w("The reviewers agreed **more often** on relatedness than on attribution, and kappa is **lower** for it. That is not an error. Nearly every return in this sample was coded *related*, so two reviewers guessing blindly would still have agreed most of the time, and kappa subtracts that expected agreement. Attribution was spread across several categories, so agreement there was harder to reach by chance and kappa rewards it.")
w("")
w("This is why the agreement percentage and PABAK sit beside every kappa. A reader given the kappa alone would rank your relatedness judgement as the weaker of the two, when the reviewers actually disagreed about it half as often.")
w("")
w("Confidence intervals are truncated at 1.00, because kappa cannot exceed it. Every kappa here carries a wide interval, because 40 pairs is a small number. **The pilot cannot certify reliability. It can only detect disaster.** The kappa you publish comes from the full 400.")
w("")
w("> **This fictional sample passes on every criterion. Do not expect that.** It was written by one person in one sitting, so it is more consistent than two tired reviewers working separately over three weeks will be. A real pilot that comes back amber on attribution or preventability is the normal result, not a failure.")
w("")
w("---")
w("")
w("## 9. What to do with the disagreements")
w("")
w("Sort each one into exactly one of three bins:")
w("")
w("1. **Abstraction error** — one reviewer missed something that was written in the chart. Fix by retraining, not by changing the rules.")
w("2. **Rule ambiguity** — the workbook genuinely did not say. This, and only this, changes the workbook.")
w("3. **Genuine clinical disagreement** — same facts, both defensible. Leave it alone.")
w("")
w("In this fictional sample, pair 6 (asthma discharged without a steroid) and pair 28 (gastroenteritis with no hydration status documented) are the third kind. Writing a rule to force those into line would manufacture agreement, and the kappa you then report would mean nothing.")
w("")
w("Pair 36 is the second kind: one reviewer read *attend the clinic in 3 days* as a scheduled return, the other did not. That is a wording gap in Step 5, and it is exactly what the pilot exists to find.")
w("")
w("---")
w("")
w("## 10. What you actually have to type")
w("")
w("Section 4 is the whole input. Nine columns, forty rows, in Excel. Nothing else is needed to produce section 7.")
w("")
w("Enter it exactly as shown, with a dash for fields that do not apply. Send that sheet and the analysis comes back. No statistical software has to be installed on your machine, and no one has to learn SPSS to get this table.")

io.open(sys.argv[1], "w", encoding="utf-8").write("\n".join(L))
print("wrote markdown")
for name, n, po, k, pabak, se in results:
    print("%-16s n=%2d  agree=%.3f  kappa=%.2f  pabak=%.2f" % (name, n, po, k, pabak))
