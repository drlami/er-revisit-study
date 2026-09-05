# -*- coding: utf-8 -*-
"""Rebuild every document in the study, into its correct numbered location.

    cd source
    python build_all.py            # rebuild everything
    python build_all.py 05         # rebuild only step 05
    python build_all.py workbook   # or match on any part of the name

Run this after editing any .md file in this folder. It is the only build command
you need -- it replaces calling build_docx.py and make_xlsx.py by hand, and it is
what keeps the numbered files in STEPS/ and REFERENCE/ from drifting apart.

If a file is open in Word, the rebuild for that one file fails with a clear
message and the others still finish. Close Word and run it again.
"""
import io
import os
import subprocess
import sys

sys.dont_write_bytecode = True  # keep the source folder free of __pycache__

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
STEPS = os.path.join(BASE, "STEPS")
REF = os.path.join(BASE, "REFERENCE", "Samples")

# (tag, source .md, output path)
DOCS = [
    ("01", "TEAM-BRIEFING.md",          os.path.join(STEPS, "01 - Team Briefing.docx")),
    ("02", "ETHICS-PROPOSAL.md",        os.path.join(STEPS, "02 - Protocol and Proposal (to Ministry of Health).docx")),
    ("03", "HIS-DATA-ACCESS-REQUEST.md", os.path.join(STEPS, "03 - HIS Data Access Request (English + Arabic).docx")),
    ("04", "IT-EXPORT-REQUEST.md",      os.path.join(STEPS, "04 - IT Data Export Request.docx")),
    ("05", "REVIEWER-WORKBOOK.md",      os.path.join(STEPS, "05 - Reviewer Workbook.docx")),
    ("08", "ANALYSIS-PLAN.md",          os.path.join(STEPS, "08 - Analysis Plan.docx")),
    ("protocol", "PROTOCOL.md",         os.path.join(REF, "Full Study Protocol.docx")),
    ("manual", "CODING-MANUAL.md",      os.path.join(REF, "Coding Manual.docx")),
    ("dictionary", "DATA-DICTIONARY.md", os.path.join(REF, "Data Dictionary.docx")),
    ("sample", "SAMPLE-REVIEWER-DATA.md", os.path.join(REF, "Sample Reviewer Data (SYNTHETIC).docx")),
    ("start", os.path.join("..", "START HERE.md"), os.path.join(BASE, "START HERE.docx")),
]

# The two coding sheets are built by make_xlsx.py, not from markdown. The
# pre-filled practice copies in REFERENCE/ are built by make_fake_data.py.
SHEETS = [
    ("06", os.path.join(STEPS, "06 - Reviewer 1 Coding Sheet.xlsx"), "Reviewer 1"),
    ("07", os.path.join(STEPS, "07 - Reviewer 2 Coding Sheet.xlsx"), "Reviewer 2"),
]


def wanted(tag, src, out, filt):
    if not filt:
        return True
    f = filt.lower()
    return f in tag.lower() or f in src.lower() or f in os.path.basename(out).lower()


def main():
    filt = sys.argv[1] if len(sys.argv) > 1 else None
    ok, failed, skipped = [], [], []

    for tag, src, out in DOCS:
        if not wanted(tag, src, out, filt):
            skipped.append(tag)
            continue
        srcpath = os.path.join(HERE, src)
        if not os.path.exists(srcpath):
            failed.append((os.path.basename(out), "source missing: %s" % src))
            continue
        r = subprocess.run([sys.executable, os.path.join(HERE, "build_docx.py"), srcpath, out],
                           capture_output=True, text=True)
        if r.returncode == 0:
            ok.append(os.path.basename(out))
        else:
            err = r.stderr.strip().splitlines()
            reason = err[-1] if err else "unknown error"
            if "Permission denied" in reason:
                reason = "OPEN IN WORD - close it and run again"
            failed.append((os.path.basename(out), reason))

    # coding sheets
    if any(wanted(tag, "coding sheet", out, filt) for tag, out, _ in SHEETS):
        import importlib.util
        spec = importlib.util.spec_from_file_location("mx", os.path.join(HERE, "make_xlsx.py"))
        mx = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mx)
        for tag, out, label in SHEETS:
            if not wanted(tag, "coding sheet", out, filt):
                continue
            try:
                mx.build(out, label)
                ok.append(os.path.basename(out))
            except PermissionError:
                failed.append((os.path.basename(out), "OPEN IN EXCEL - close it and run again"))
            except Exception as exc:
                failed.append((os.path.basename(out), str(exc)))

    # synthetic practice copies in REFERENCE/ -- fake data, 40 and 400 pairs
    if wanted("fake", "practice data", "Coding Sheet (FAKE DATA).xlsx", filt):
        r = subprocess.run([sys.executable, os.path.join(HERE, "make_fake_data.py")],
                           capture_output=True, text=True)
        if r.returncode == 0:
            ok.extend(l.split("rows", 1)[-1].strip() for l in r.stdout.strip().splitlines())
        else:
            err = r.stderr.strip().splitlines()
            reason = err[-1] if err else "unknown error"
            if "Permission denied" in reason:
                reason = "OPEN IN EXCEL - close it and run again"
            failed.append(("practice copies (FAKE DATA)", reason))
    else:
        skipped.append("fake")

    print("")
    for name in ok:
        print("  built    %s" % name)
    for name, why in failed:
        print("  FAILED   %s  --  %s" % (name, why))
    print("\n%d built, %d failed%s" % (len(ok), len(failed),
                                       (", %d skipped by filter" % len(skipped)) if filt else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
