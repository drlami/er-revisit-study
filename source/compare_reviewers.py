# -*- coding: utf-8 -*-
"""Put the two reviewers' coding sheets side by side and mark every difference.

    cd source
    python compare_reviewers.py                     # uses the 40-pair FAKE DATA sheets
    python compare_reviewers.py R1.xlsx R2.xlsx out.xlsx

Produces one workbook with four tabs:

    Start here     - what this file is, in plain words
    Agreement      - how often the two reviewers gave the same answer
    Side by side   - all 40 pairs, both answers, differences shaded
    For Dr Amani   - only the pairs they disagreed on, ready to settle

No statistics beyond counting and percentages. This is the comparison step,
not the analysis step.
"""
import os
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
REF = os.path.join(BASE, "REFERENCE")

NAMES = {"Reviewer 1": "Dr Waad", "Reviewer 2": "Dr Ainaa"}

# The five judgements, given the plain-language name a clinician would use.
# (column in the coding sheet, plain name, the column holding the pointer,
#  the column holding the written reason if there is one)
JUDGEMENTS = [
    ("Step 5 Eligibility", "Does this pair belong in the study?",
     None, None),
    ("Step 6 Relatedness", "Is it the same problem as the first visit?",
     "Step 6 Basis - field", None),
    ("Step 7 Attribution", "Why did the child come back?",
     "Step 7 Basis - field", "Step 7 Basis - reason"),
    ("Step 8 Preventability", "Could the return have been prevented?",
     "Step 8 Basis - field", None),
    ("Step 9 Access barrier", "Was there a problem getting care?",
     "Step 9 Basis - field", None),
]

# What the reviewer read off the notes. These are facts, not opinions, so a
# difference here means one of them misread or mistyped - a different problem.
FACTS = [
    ("I-1 Vital signs documented", "Were vital signs written down?"),
    ("I-2 Relevant system examined?", "Was the relevant body part examined?"),
    ("I-3 Discharge instructions", "What discharge advice was written?"),
    ("I-4 Follow-up directed to", "Where were they told to go next?"),
    ("Was the discharge decision reasonable?", "Was sending the child home reasonable?"),
]

HEAD = PatternFill("solid", fgColor="17365D")
SUBHEAD = PatternFill("solid", fgColor="DEE7F0")
DIFF = PatternFill("solid", fgColor="FFC7CE")     # red - they differ
SAME = PatternFill("solid", fgColor="E2EFDA")     # green - they match
THIN = Side(style="thin", color="B0B0B0")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def read_sheet(path):
    ws = load_workbook(path)["Pairs"]
    headers = [c.value for c in ws[2]]
    rows = []
    for r in ws.iter_rows(min_row=3, values_only=True):
        if r[0] is None:
            continue
        rows.append(dict(zip(headers, r)))
    return rows


def val(row, col):
    """A blank cell and an empty string mean the same thing here."""
    v = row.get(col)
    return "" if v is None else str(v).strip()


def basis(row, field_col, reason_col):
    """One readable string: the field they pointed at, plus their reason."""
    f = val(row, field_col) if field_col else ""
    r = val(row, reason_col) if reason_col else ""
    if f and r:
        return "[%s] %s" % (f, r)
    return "[%s]" % f if f else r


def title_row(ws, row, texts, widths=None):
    for j, t in enumerate(texts, start=1):
        c = ws.cell(row=row, column=j, value=t)
        c.fill = HEAD
        c.font = Font(name="Aptos", size=10, bold=True, color="FFFFFF")
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BORDER
        if widths:
            ws.column_dimensions[get_column_letter(j)].width = widths[j - 1]
    ws.row_dimensions[row].height = 32


def sheet_start_here(ws, n_pairs, n1, n2):
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 100
    lines = [
        ("H1", "Comparing the two reviewers"),
        ("", ""),
        ("P", "%s and %s each read the same %d pairs of records, separately, "
              "without seeing each other's answers. This file puts their answers side by side."
              % (n1, n2, n_pairs)),
        ("", ""),
        ("P", "There is one question behind all of it: DID THE TWO DOCTORS GIVE THE SAME ANSWERS?"),
        ("", ""),
        ("P", "If they mostly agreed, the instructions are clear and the remaining pairs can go ahead. "
              "If they often disagreed, the instructions need fixing first - which is cheaper to "
              "discover now than after 360 more pairs."),
        ("", ""),
        ("H2", "The three other tabs"),
        ("B", "Agreement  -  how often they gave the same answer, question by question. Just counting."),
        ("B", "Side by side  -  every pair, both answers. Red means they differed, green means they matched."),
        ("B", "For Dr Amani  -  only the disagreements, one row each, with both reasons. This is the "
              "list she settles. The last two columns are empty for her to fill in."),
        ("", ""),
        ("H2", "What this file does NOT do"),
        ("P", "No statistics yet. This is counting and comparing only. The agreement figure that goes "
              "into the paper is calculated later, from the real data, not from this."),
        ("", ""),
        ("H2", "What to do with it"),
        ("B", "1. Open 'Agreement' and look at which question has the most disagreement."),
        ("B", "2. Open 'For Dr Amani' and send that list to her."),
        ("B", "3. At the team meeting, go through each disagreement and ask one question about it: "
              "was it unclear instructions, or a genuinely hard case? Only the first kind changes the workbook."),
    ]
    r = 2
    for kind, text in lines:
        c = ws.cell(row=r, column=2, value=text)
        if kind == "H1":
            c.font = Font(name="Aptos", size=16, bold=True, color="17365D")
        elif kind == "H2":
            c.font = Font(name="Aptos", size=12, bold=True, color="2F5597")
        else:
            c.font = Font(name="Aptos", size=11)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            ws.row_dimensions[r].height = 30 if len(text) > 100 else 15
        r += 1


def sheet_agreement(ws, a, b, n1, n2):
    title_row(ws, 1, ["What they were asked", "Pairs compared", "Same answer",
                      "Different answer", "% they agreed"],
              [52, 13, 12, 15, 13])
    r = 2

    def block(label, items, judgement):
        nonlocal r
        c = ws.cell(row=r, column=1, value=label)
        c.fill = SUBHEAD
        c.font = Font(name="Aptos", size=10, bold=True, color="17365D")
        for j in range(2, 6):
            ws.cell(row=r, column=j).fill = SUBHEAD
        r += 1
        for col, plain in items:
            if judgement:
                pairs = [(x, y) for x, y in zip(a, b) if val(x, col) or val(y, col)]
            else:
                pairs = list(zip(a, b))
            same = sum(1 for x, y in pairs if val(x, col) == val(y, col))
            n = len(pairs)
            ws.cell(row=r, column=1, value=plain)
            ws.cell(row=r, column=2, value=n)
            ws.cell(row=r, column=3, value=same)
            ws.cell(row=r, column=4, value=n - same)
            pc = ws.cell(row=r, column=5, value=(round(100.0 * same / n) if n else 0))
            pc.number_format = '0"%"'
            if n and same < n:
                ws.cell(row=r, column=4).fill = DIFF
            for j in range(1, 6):
                cell = ws.cell(row=r, column=j)
                cell.border = BORDER
                if not cell.font.bold:
                    cell.font = Font(name="Aptos", size=10)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            r += 1
        r += 1

    block("THE JUDGEMENTS - these are opinions, so some disagreement is normal",
          [(col, plain) for col, plain, _, _ in JUDGEMENTS], True)
    block("WHAT WAS WRITTEN IN THE NOTES - these are facts, so they should nearly always match",
          FACTS, False)

    both = sum(1 for x, y in zip(a, b)
               if all(val(x, c) == val(y, c) for c, _, _, _ in JUDGEMENTS))
    ws.cell(row=r, column=1, value="Pairs where they gave the same answer to ALL five judgements")
    ws.cell(row=r, column=1).font = Font(name="Aptos", size=10, bold=True)
    ws.cell(row=r, column=2, value="%d of %d" % (both, len(a))).font = Font(
        name="Aptos", size=10, bold=True)
    r += 2
    ws.cell(row=r, column=1,
            value="Note: 'Pairs compared' is smaller than the total where a judgement was "
                  "left blank on purpose - for example, no attribution is recorded on a pair "
                  "that was excluded from the study.").font = Font(
        name="Aptos", size=9, italic=True, color="595959")
    ws.freeze_panes = "A2"


def sheet_side_by_side(ws, a, b, n1, n2):
    heads = ["Pair", "Study ID"]
    widths = [6, 11]
    for _, plain, _, _ in JUDGEMENTS:
        heads += ["%s: %s" % (n1, plain), "%s: %s" % (n2, plain), "Same?"]
        widths += [26, 26, 8]
    title_row(ws, 1, heads, widths)

    for i, (x, y) in enumerate(zip(a, b)):
        r = i + 2
        ws.cell(row=r, column=1, value=x["Pair no."])
        ws.cell(row=r, column=2, value=val(x, "Study ID"))
        col = 3
        for c, _, _, _ in JUDGEMENTS:
            vx, vy = val(x, c) or "-", val(y, c) or "-"
            ok = vx == vy
            ws.cell(row=r, column=col, value=vx)
            ws.cell(row=r, column=col + 1, value=vy)
            ws.cell(row=r, column=col + 2, value="same" if ok else "DIFFERENT")
            for j in range(col, col + 3):
                ws.cell(row=r, column=j).fill = SAME if ok else DIFF
            col += 3
        for j in range(1, len(heads) + 1):
            cell = ws.cell(row=r, column=j)
            cell.border = BORDER
            cell.font = Font(name="Aptos", size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 28
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(heads)), len(a) + 1)


def sheet_for_amani(ws, a, b, n1, n2):
    heads = ["Pair", "Study ID", "The question", "%s said" % n1, "%s said" % n2,
             "%s - why" % n1, "%s - why" % n2,
             "What the family said on the return visit",
             "Dr Amani's decision", "Dr Amani - why"]
    title_row(ws, 1, heads, [6, 11, 30, 20, 20, 34, 34, 30, 20, 30])

    r = 2
    for x, y in zip(a, b):
        for col, plain, fcol, rcol in JUDGEMENTS:
            vx, vy = val(x, col), val(y, col)
            if vx == vy:
                continue
            ws.cell(row=r, column=1, value=x["Pair no."])
            ws.cell(row=r, column=2, value=val(x, "Study ID"))
            ws.cell(row=r, column=3, value=plain)
            ws.cell(row=r, column=4, value=vx or "(left blank)")
            ws.cell(row=r, column=5, value=vy or "(left blank)")
            ws.cell(row=r, column=6, value=basis(x, fcol, rcol))
            ws.cell(row=r, column=7, value=basis(y, fcol, rcol))
            ws.cell(row=r, column=8, value=val(x, "R-1 Reason for return - exact words"))
            for j in range(1, len(heads) + 1):
                cell = ws.cell(row=r, column=j)
                cell.border = BORDER
                cell.font = Font(name="Aptos", size=9)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                if j in (9, 10):
                    cell.fill = PatternFill("solid", fgColor="FFF2CC")
            ws.row_dimensions[r].height = 42
            r += 1
    ws.freeze_panes = "D2"
    return r - 2


def main():
    if len(sys.argv) >= 4:
        p1, p2, out = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        p1 = os.path.join(REF, "Reviewer 1 Coding Sheet - 40 pairs (FAKE DATA).xlsx")
        p2 = os.path.join(REF, "Reviewer 2 Coding Sheet - 40 pairs (FAKE DATA).xlsx")
        out = os.path.join(REF, "Pilot Comparison (FAKE DATA).xlsx")

    a, b = read_sheet(p1), read_sheet(p2)
    if len(a) != len(b):
        raise SystemExit("The two files have different numbers of pairs: %d and %d."
                         % (len(a), len(b)))
    for x, y in zip(a, b):
        if x["Pair no."] != y["Pair no."]:
            raise SystemExit("The two files are not in the same order - pair %s against %s."
                             % (x["Pair no."], y["Pair no."]))

    n1 = NAMES.get(val(a[0], "Reviewer"), val(a[0], "Reviewer") or "Reviewer 1")
    n2 = NAMES.get(val(b[0], "Reviewer"), val(b[0], "Reviewer") or "Reviewer 2")

    wb = Workbook()
    sheet_start_here(wb.active, len(a), n1, n2)
    wb.active.title = "Start here"
    sheet_agreement(wb.create_sheet("Agreement"), a, b, n1, n2)
    sheet_side_by_side(wb.create_sheet("Side by side"), a, b, n1, n2)
    n_dis = sheet_for_amani(wb.create_sheet("For Dr Amani"), a, b, n1, n2)
    wb.save(out)

    print("built: %s" % os.path.basename(out))
    print("  %d pairs compared" % len(a))
    print("  %d disagreements for Dr Amani to settle" % n_dis)


if __name__ == "__main__":
    main()
