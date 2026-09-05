# -*- coding: utf-8 -*-
"""Build SYNTHETIC pre-filled copies of the reviewer coding sheets.

    cd source
    python make_fake_data.py

Writes four workbooks into REFERENCE/:

    Reviewer 1 Coding Sheet - 40 pairs (FAKE DATA).xlsx
    Reviewer 2 Coding Sheet - 40 pairs (FAKE DATA).xlsx
    Reviewer 1 Coding Sheet - 400 pairs (FAKE DATA).xlsx
    Reviewer 2 Coding Sheet - 400 pairs (FAKE DATA).xlsx

THESE ARE NOT REAL PATIENTS. Every row is invented. No chart was opened and no
child exists. The files are here so that the pilot analysis and the full
analysis can be written, run and checked before any real data arrives.

The 40-pair files are the same 40 cases as REFERENCE/Sample Reviewer Data
(SYNTHETIC).docx, so the two tell the same story. The 400-pair files start with
those same 40 pairs -- as the real study will, the pilot being the first forty
pairs of the sample -- and add 360 more.

The sheet itself is not rebuilt here: this calls make_xlsx.build(), the same
function that produces the empty sheets in STEPS/, so the practice copies can
never drift from the real ones.
"""
import os
import random
import sys

sys.dont_write_bytecode = True

import make_xlsx

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
REF = os.path.join(BASE, "REFERENCE")

BANNER = ("SYNTHETIC PRACTICE DATA - NOT REAL PATIENTS. Every row in this file is "
          "invented. Do not quote any number from it, do not put it in the ethics "
          "file, and do not use it as a reviewer's working copy. It exists so the "
          "analysis can be written and tested before the real data arrives.")

BANNER_AR = ("بيانات تدريبية "
             "مُختلقة - ليست "
             "لمرضى حقيقيين. "
             "كل سطر في هذا "
             "الملف مكتوب "
             "للتجربة فقط. "
             "لا تقتبس منه أي "
             "رقم، ولا تستخدمه "
             "كنسخة عمل للمراجِع.")

# ---------------------------------------------------------------- code maps
V = {"A": "All documented", "P": "Partly documented", "N": "None documented"}
E = {"Y": "Yes", "N": "No", "C": "Cannot tell"}
D = {"N": "None documented", "G": "Generic advice only", "S": "Specific return precautions"}
F = {"N": "None documented", "E": "Return to ED", "O": "Outpatient clinic",
     "P": "Primary health centre", "X": "Other"}
S3 = {"A": "Adequate", "I": "Inadequate", "C": "Cannot tell from the record"}
ELIG = {1: "1 eligible", 2: "2 scheduled", 3: "3 administrative",
        4: "4 insufficient documentation", 5: "5 not discharged - tell the PI"}
REL = {1: "1 related", 2: "2 unrelated", 3: "3 uncertain"}
ATT = {1: "1 illness-related", 2: "2 patient-related", 3: "3 physician-related", 4: "4 uncertain"}
PRV = {1: "1 preventable", 2: "2 not preventable", 3: "3 uncertain"}
ACC = {1: "1 yes", 2: "2 no", 3: "3 uncertain"}

NONE_DOC = "None documented"

# ------------------------------------------------------- written reasoning
# Two reviewers never phrase a reason identically, so each judgement draws from
# a small bank and the two reviewers draw different entries from it. {sys} is
# the body system the complaint pointed at.
STEP3 = {
    ("A", "I-1"): ["observations recorded in full and normal for age",
                   "temperature, pulse and saturations all written before discharge",
                   "vital signs documented and stable at discharge"],
    ("A", "I-2"): ["{sys} examined and the findings written in the note",
                   "{sys} examination documented and normal on the day",
                   "the note carries a {sys} examination, not just a general look"],
    ("A", "I-3"): ["written return precautions given, with what to watch for",
                   "specific return advice documented for the family"],
    ("A", "I-4"): ["follow-up destination named clearly in the note",
                   "the family were told where to go and it is written down"],
    ("A", "more than one"): ["observations, examination and return advice all documented",
                             "examination and specific return advice both written"],
    ("I", "I-1"): ["no observations recorded anywhere in the index note",
                   "only temperature written; no pulse, no saturations"],
    ("I", "I-2"): ["{sys} not examined anywhere in the note",
                   "no {sys} examination documented at the index visit",
                   "the complaint was the {sys} and no {sys} examination is written"],
    ("I", "I-3"): ["no return precautions written, only general advice",
                   "nothing written about when to bring the child back"],
    ("I", "I-4"): ["no follow-up destination given to the family",
                   "the family were not told where to go next"],
    ("I", "more than one"): ["neither examination nor return advice documented",
                             "observations incomplete and no return precautions given"],
    ("I", "none fit"): ["the gap was in the treatment given, not in any of the eight fields",
                        "what was missing is not one of the eight fields - see the Step 10 note"],
    ("C", "more than one"): ["the note is too short to judge - no examination, observations or diagnosis",
                             "nothing recorded to judge the decision on"],
    ("C", "I-2"): ["cannot tell whether the {sys} was examined; nothing written either way",
                   "the {sys} examination is neither documented nor excluded"],
}

STEP7 = {
    (1, "I-1"): ["observations were normal at the index visit and the child deteriorated after it",
                 "nothing in the recorded observations pointed to what came next"],
    (1, "I-2"): ["{sys} examined and documented normal; the illness declared itself later",
                 "nothing was missable at the index visit - the {sys} examination is recorded normal",
                 "the {sys} was examined and clear; this is the illness moving on"],
    (1, "I-3"): ["the family came back exactly as the written advice told them to",
                 "the return precautions worked - they returned when told to"],
    (1, "R-1"): ["the words of the return describe the natural course of the same illness",
                 "the reason for return is the illness progressing, not care that fell short"],
    (2, "I-3"): ["specific return advice was given and the child was well on reassessment",
                 "advice was documented; the return was driven by worry, not new findings"],
    (2, "R-1"): ["the family's own words describe anxiety rather than a new problem",
                 "returned for reassurance; examination unchanged from the index visit"],
    (2, "R-4"): ["the medicine was prescribed and available; it was not taken as directed",
                 "the treatment was in the family's hands and did not go in"],
    (3, "I-1"): ["observations were incomplete and the abnormality was not picked up",
                 "the missing observations are what let this go"],
    (3, "I-2"): ["{sys} never examined at the index visit",
                 "the finding that mattered was in the {sys}, which was not examined",
                 "no {sys} examination, and that is where the diagnosis was"],
    (3, "I-3"): ["no return precautions given, so the family had nothing to act on",
                 "the discharge advice did not cover what actually happened"],
    (3, "none fit"): ["the gap was in the treatment given, not in any of the eight fields"],
    (4, "I-2"): ["cannot tell - the {sys} examination is not documented either way",
                 "the note does not say enough about the {sys} to decide"],
    (4, "more than one"): ["the record does not say enough to separate illness from care",
                           "too little written to attribute this either way"],
    (1, "I-4"): ["the family went where they were told and the illness moved on anyway",
                 "follow-up was arranged; the return is the illness itself"],
    (2, "R-3"): ["the family's own words describe a barrier they met, not a care gap",
                 "what they say happened is outside the index visit"],
    # fallbacks, used when a reviewer keeps the field but changes the code
    (1, "more than one"): ["more than one field points the same way - this is the illness"],
    (2, "more than one"): ["more than one field points to the family's handling of it"],
    (3, "more than one"): ["more than one field was left undocumented at the index visit"],
}


def pick(bank, key, sysword, salt):
    """Choose one phrasing. The salt makes the two reviewers word it differently."""
    opts = bank.get(key)
    if not opts:
        opts = bank.get((key[0], "more than one")) or ["see the Step 10 note"]
    return opts[salt % len(opts)].format(sys=sysword)


# ------------------------------------------------------------ the 40 pilot
# Same forty cases, and the same Step 5 to Step 9 codes, as
# REFERENCE/Sample Reviewer Data (SYNTHETIC).docx.
#
# ovr = the second reviewer's differences. Everything not named there is coded
# the same by both, which is what real double coding looks like.
def C(pair, sys, v, e, d, f, s3, s3f, r1, r2d, elig=1, rel=1, att=1, attf="I-2",
      prv=2, prvf="I-3", acc=2, acct=None, r3=NONE_DOC, r4=NONE_DOC,
      ovr=None, covered="Yes", note="None", knew="No"):
    return dict(pair=pair, sys=sys, v=v, e=e, d=d, f=f, s3=s3, s3f=s3f, r1=r1,
                r2d=r2d, r3=r3, r4=r4, elig=elig, rel=rel, att=att, attf=attf,
                prv=prv, prvf=prvf, acc=acc, acct=acct, ovr=ovr or {},
                covered=covered, note=note, knew=knew)


PILOT = [
 C(1, "chest", "A", "Y", "S", "E", "A", "I-2",
   "الولد صار يلهث وما بيرضع منيح",
   "No", att=1, attf="I-2", prv=2),
 C(2, "abdomen", "A", "Y", "S", "E", "A", "I-2",
   "لسا عنده إسهال والأم قلقانة",
   "No", att=2, attf="I-3", prv=1, prvf="I-3"),
 C(3, "hip", "P", "N", "G", "N", "I", "I-2",
   "ما بقدر يدوس على رجله وصار أسخن",
   "Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 C(4, "ear", "A", "Y", "G", "E", "A", "I-2",
   "الحرارة ما نزلت من إمبارح",
   "Yes", att=1, attf="I-2", prv=2, ovr={"v": "P"}),
 C(5, "forearm", "A", "Y", "G", "O", "I", "I-3",
   "إيده صارت توجعه كثير وورمت",
   "No", att=3, attf="I-3", prv=1, prvf="I-3"),
 C(6, "chest", "A", "Y", "G", "E", "I", "none fit",
   "الكحة والزيق رجعو أسوأ من قبل",
   "No", att=3, attf="none fit", prv=1, prvf="none fit",
   ovr={"s3": "A", "s3f": "I-2", "att": 1, "attf": "I-2", "prv": 2, "prvf": "I-3"},
   covered="No", note="No oral steroid was given at the index visit. That is a treatment gap and none of the eight fields covers it."),
 C(7, "skin", "A", "Y", "G", "E", "A", "I-2",
   "وقع عن الكرسي وانشق جبينه",
   "Yes", rel=2, att=None, prv=2, prvf="I-3"),
 C(8, "general", "A", "Y", "S", "E", "A", "more than one",
   "صار خامل وما بيتفاعل زي قبل",
   "Yes", att=1, attf="I-2", prv=2),
 C(9, "throat", "A", "Y", "G", "P", "A", "I-2",
   "الحرارة ما راحت",
   "No", att=2, attf="R-4", prv=1, prvf="I-3", acc=1,
   acct="Could not obtain the medicine",
   r4="ما لقينا الدوا في الصيدلية"),
 C(10, "general", "A", "Y", "S", "O", "A", "I-4",
   "ما في دور في العيادة والطفل ما تحسن",
   "No", att=1, attf="I-4", prv=2, acc=1,
   acct="No clinic appointment available",
   r3="قالوا لنا ما في موعد قبل الشهر الجاي"),
 C(11, "chest", "A", "Y", "S", "O", "A", "I-2",
   "الحرارة كملت وما قدرنا نوصل العيادة",
   "No", att=1, attf="I-2", prv=2, acc=1, acct="Could not reach clinic",
   r3="ما قدرنا نوصل العيادة، الطريق كانت مسكرة"),
 C(12, "abdomen", "A", "Y", "S", "E", "A", "I-3",
   "بستفرغ كل شي بشربه",
   "No", att=1, attf="I-2", prv=2),
 C(13, "abdomen", "P", "N", "G", "N", "I", "I-2",
   "الوجع صار أقوى ونزل على اليمين",
   "Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 C(14, "general", "A", "Y", "S", "E", "A", "I-3",
   "جينا للمراجعة زي ما قالوا لنا",
   "No", elig=2),
 C(15, "general", "A", "Y", "G", "N", "A", "I-2",
   "بدنا تقرير طبي للمدرسة",
   "No", elig=3),
 C(16, "general", "N", "N", "N", "N", "C", "more than one",
   "ما بيرضع وصار ناعس كثير",
   "Yes", elig=4,
   note="Index note has no examination, no vital signs and no diagnosis. Nothing to judge."),
 C(17, "chest", "A", "Y", "S", "E", "A", "I-1",
   "بطل يرضع منيح",
   "No", att=1, attf="I-1", prv=2, ovr={"d": "G"}),
 C(18, "throat", "A", "Y", "S", "E", "A", "I-2",
   "صوته صار مبحوح وبيصفر وهو قاعد",
   "No", att=1, attf="I-2", prv=2),
 C(19, "abdomen", "A", "Y", "G", "E", "A", "I-2",
   "ما في تحسن، الإسهال زي ما هو",
   "No", att=2, attf="I-3", prv=1, prvf="I-3"),
 C(20, "skin", "A", "Y", "G", "E", "A", "I-2",
   "طلع عليه طفح بعد ما أخذ الدوا",
   "Yes", att=1, attf="R-1", prv=2, ovr={"prv": 3}),
 C(21, "abdomen", "A", "N", "G", "E", "I", "I-2",
   "الحرارة ما نزلت وصار يوجعه وقت التبول",
   "Yes", att=3, attf="I-2", prv=1, prvf="I-2", covered="No",
   note="No urine test was done at the index visit. Investigations are not one of the eight fields; I coded on the missing examination."),
 C(22, "chest", "A", "Y", "N", "E", "I", "I-3",
   "الزيق رجع من جديد",
   "No", att=3, attf="I-3", prv=1, prvf="I-3", ovr={"att": 2, "attf": "I-3"}),
 C(23, "general", "A", "Y", "G", "E", "A", "I-2",
   "الحرارة ما نزلت والأم خافت",
   "No", att=2, attf="I-3", prv=1, prvf="I-3", ovr={"prv": 2}),
 C(24, "head", "A", "Y", "S", "E", "A", "I-3",
   "استفرغ مرتين بالليل",
   "No", att=1, attf="I-3", prv=2),
 C(25, "general", "A", "Y", "S", "E", "A", "I-3",
   "صار عنده تشنج تاني",
   "No", att=1, attf="I-3", prv=2),
 C(26, "abdomen", "A", "Y", "G", "E", "A", "I-2",
   "ما بطل بكي طول الليل",
   "No", att=2, attf="R-1", prv=1, prvf="I-3"),
 C(27, "ankle", "A", "N", "G", "O", "I", "I-2",
   "الوجع ما راح وما بقدر يدوس",
   "Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 C(28, "abdomen", "P", "N", "G", "E", "I", "I-1",
   "صار ناشف وما بشرب إشي",
   "No", att=3, attf="I-1", prv=1, prvf="I-1",
   ovr={"att": 1, "attf": "I-2", "prv": 3}),
 C(29, "skin", "A", "Y", "G", "E", "A", "I-2",
   "طلع طفح على كل جسمه",
   "Yes", att=1, attf="I-2", prv=2, ovr={"e": "C"}),
 C(30, "ear", "A", "Y", "G", "X", "A", "I-2",
   "الجسم لسا بأذنه",
   "No", att=1, attf="I-4", prv=2, acc=1,
   acct="No clinic appointment available",
   r3="عيادة الأنف والأذن ما أعطتنا موعد"),
 C(31, "chest", "A", "Y", "S", "E", "A", "I-2",
   "نفسه ضاق أكثر من إمبارح",
   "No", att=1, attf="I-2", prv=2, acc=1, acct="Other",
   r3="تأخرنا نوصل، الطريق كانت مسكرة",
   ovr={"acc": 3}),
 C(32, "skin", "A", "Y", "G", "E", "A", "I-2",
   "عضه كلب في الشارع",
   "Yes", rel=2, att=None, prv=2, prvf="I-3"),
 C(33, "chest", "A", "Y", "S", "O", "A", "I-2",
   "بستفرغ الدوا كل مرة",
   "No", att=1, attf="I-2", prv=3, prvf="I-3",
   r4="بستفرغ المضاد كل ما ناخده",
   ovr={"att": 2, "attf": "R-4", "prv": 1}, covered="No",
   note="The medicine was obtained but vomited every time. This is neither an access barrier nor a documentation gap."),
 C(34, "abdomen", "A", "Y", "G", "E", "A", "I-2",
   "الوجع ما راح",
   "Yes", att=1, attf="I-2", prv=2),
 C(35, "abdomen", "A", "Y", "G", "E", "A", "I-2",
   "الحرارة رجعت وصار يبكي وقت التبول",
   "Yes", att=3, attf="I-2", prv=1, prvf="I-2",
   ovr={"rel": 3, "att": 4, "attf": "more than one", "prv": 3}),
 C(36, "skin", "A", "Y", "G", "O", "A", "I-4",
   "الضمادة انبلت وبدنا نغيرها",
   "No", att=1, attf="I-4", prv=2, ovr={"elig": 2}),
 C(37, "hip", "A", "Y", "G", "E", "A", "I-2",
   "صار يعرج على رجله اليمين",
   "Yes", att=1, attf="I-2", prv=2, ovr={"rel": 2, "att": None}),
 C(38, "general", "A", "Y", "S", "E", "A", "I-2",
   "الحرارة لسا عالية",
   "No", att=1, attf="I-2", prv=2),
 C(39, "chest", "A", "Y", "G", "O", "A", "I-2",
   "الزيق رجع وما معنا ثمن البخاخ",
   "No", att=2, attf="R-3", prv=1, prvf="I-3", acc=1, acct="Cost",
   r3="ما قدرنا نشتري البخاخ، غالي علينا"),
 C(40, "abdomen", "A", "Y", "S", "E", "A", "I-3",
   "بدنا رأي ثاني، الأب ما اطمأن",
   "No", att=2, attf="R-1", prv=1, prvf="I-3", ovr={"prv": 2}),
]

# ------------------------------------- templates for the remaining 360 pairs
# (weight, case). The weights set the mix: mostly eligible and related, with
# the smaller categories appearing often enough to be worth a row in a table.
def T(w, **kw):
    kw.setdefault("pair", 0)
    return (w, C(**kw))


AR = {
    "worse_breathing": ["نفسه ضاق أكثر",
                        "صار يلهث وبيشد على صدره",
                        "الزيق زاد من الليل"],
    "fever_on": ["الحرارة ما نزلت",
                 "لسا سخن وما في تحسن",
                 "الحرارة رجعت بالليل"],
    "vomiting": ["بستفرغ كل شي",
                 "ما بيمسك إشي في معدته",
                 "الاستفراغ ما وقف"],
    "no_better": ["ما في أي تحسن",
                  "زي ما هو ما تغير إشي",
                  "قلقانين عليه، ما تحسن"],
    "pain": ["الوجع صار أقوى",
             "بضل يبكي من الوجع",
             "الوجع ما راح مع المسكن"],
    "rash": ["طلع عليه طفح",
             "ظهر حبوب على جسمه"],
    "drowsy": ["صار خامل وناعس",
               "ما بيتفاعل زي قبل"],
    "limp": ["صار يعرج",
             "ما بدو يدوس على رجله"],
    "not_feeding": ["بطل يرضع",
                    "ما بياكل ولا بيشرب"],
    "second_op": ["بدنا رأي ثاني",
                  "ما اطمأنّا للفحص الأول"],
    "scheduled": ["جينا للمراجعة زي ما قالوا لنا",
                  "قالوا نرجع بعد يوم للفحص"],
    "admin": ["بدنا تقرير طبي",
              "جينا نأخذ ورقة للمدرسة",
              "بدنا نسخة من التحاليل"],
}

ACCESS_AR = {
    "appt": "ما في موعد في العيادة قبل أسبوعين",
    "reach": "ما قدرنا نوصل العيادة، الطريق مسكرة",
    "cost": "ما معنا ثمن الدوا",
    "other": "تأخرنا على الحاجز",
}
MED_AR = {
    "none": "ما لقينا الدوا في الصيدلية",
    "vomit": "بستفرغ الدوا كل مرة",
    "refuse": "رفض ياخد الدوا",
}

TEMPLATES = [
 # ---- illness-related, good documentation (the commonest picture)
 T(14, sys="chest", v="A", e="Y", d="S", f="E", s3="A", s3f="I-2",
   r1="worse_breathing", r2d="No", att=1, attf="I-2", prv=2),
 T(10, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="more than one",
   r1="fever_on", r2d="Yes", att=1, attf="I-2", prv=2),
 T(8, sys="abdomen", v="A", e="Y", d="S", f="E", s3="A", s3f="I-3",
   r1="vomiting", r2d="No", att=1, attf="I-2", prv=2),
 T(7, sys="throat", v="A", e="Y", d="S", f="E", s3="A", s3f="I-2",
   r1="fever_on", r2d="Yes", att=1, attf="I-2", prv=2),
 T(6, sys="ear", v="A", e="Y", d="G", f="E", s3="A", s3f="I-2",
   r1="pain", r2d="Yes", att=1, attf="I-2", prv=2),
 T(5, sys="skin", v="A", e="Y", d="G", f="E", s3="A", s3f="I-2",
   r1="rash", r2d="Yes", att=1, attf="R-1", prv=2),
 T(5, sys="head", v="A", e="Y", d="S", f="E", s3="A", s3f="I-3",
   r1="vomiting", r2d="No", att=1, attf="I-3", prv=2),
 T(5, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="I-1",
   r1="drowsy", r2d="Yes", att=1, attf="I-1", prv=2),
 T(4, sys="chest", v="A", e="Y", d="S", f="O", s3="A", s3f="I-2",
   r1="fever_on", r2d="No", att=1, attf="I-2", prv=2),

 # ---- patient-related
 T(8, sys="abdomen", v="A", e="Y", d="G", f="E", s3="A", s3f="I-2",
   r1="no_better", r2d="No", att=2, attf="I-3", prv=1, prvf="I-3"),
 T(6, sys="general", v="A", e="Y", d="G", f="E", s3="A", s3f="I-2",
   r1="second_op", r2d="No", att=2, attf="R-1", prv=1, prvf="I-3"),
 T(4, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="I-3",
   r1="no_better", r2d="No", att=2, attf="I-3", prv=2),
 T(4, sys="chest", v="A", e="Y", d="S", f="O", s3="A", s3f="I-2",
   r1="fever_on", r2d="No", att=2, attf="R-4", prv=1, prvf="I-3",
   r4=MED_AR["vomit"], covered="No",
   note="Medicine obtained but not kept down. Not an access barrier."),
 T(3, sys="general", v="A", e="Y", d="G", f="P", s3="A", s3f="I-4",
   r1="no_better", r2d="No", att=2, attf="R-4", prv=1, prvf="I-3",
   r4=MED_AR["refuse"]),

 # ---- physician-related
 T(6, sys="hip", v="P", e="N", d="G", f="N", s3="I", s3f="I-2",
   r1="limp", r2d="Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 T(5, sys="abdomen", v="P", e="N", d="G", f="N", s3="I", s3f="I-2",
   r1="pain", r2d="Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 T(4, sys="chest", v="A", e="Y", d="N", f="E", s3="I", s3f="I-3",
   r1="worse_breathing", r2d="No", att=3, attf="I-3", prv=1, prvf="I-3"),
 T(4, sys="ankle", v="A", e="N", d="G", f="O", s3="I", s3f="I-2",
   r1="pain", r2d="Yes", att=3, attf="I-2", prv=1, prvf="I-2"),
 T(3, sys="abdomen", v="P", e="N", d="G", f="E", s3="I", s3f="I-1",
   r1="vomiting", r2d="No", att=3, attf="I-1", prv=1, prvf="I-1"),
 T(3, sys="chest", v="A", e="Y", d="G", f="E", s3="I", s3f="none fit",
   r1="worse_breathing", r2d="No", att=3, attf="none fit", prv=1, prvf="none fit",
   covered="No", note="Treatment gap at the index visit; none of the eight fields covers it."),
 T(3, sys="forearm", v="A", e="Y", d="G", f="O", s3="I", s3f="I-3",
   r1="pain", r2d="No", att=3, attf="I-3", prv=1, prvf="I-3"),

 # ---- uncertain attribution
 T(4, sys="general", v="P", e="C", d="G", f="E", s3="C", s3f="I-2",
   r1="fever_on", r2d="Yes", att=4, attf="I-2", prv=3, prvf="I-2"),
 T(3, sys="abdomen", v="P", e="C", d="G", f="N", s3="C", s3f="more than one",
   r1="no_better", r2d="No", att=4, attf="more than one", prv=3, prvf="I-2"),

 # ---- documented access barriers
 T(5, sys="general", v="A", e="Y", d="S", f="O", s3="A", s3f="I-4",
   r1="no_better", r2d="No", att=1, attf="I-4", prv=2, acc=1,
   acct="No clinic appointment available", r3=ACCESS_AR["appt"]),
 T(4, sys="chest", v="A", e="Y", d="S", f="O", s3="A", s3f="I-2",
   r1="fever_on", r2d="No", att=1, attf="I-2", prv=2, acc=1,
   acct="Could not reach clinic", r3=ACCESS_AR["reach"]),
 T(4, sys="throat", v="A", e="Y", d="G", f="P", s3="A", s3f="I-2",
   r1="fever_on", r2d="No", att=2, attf="R-4", prv=1, prvf="I-3", acc=1,
   acct="Could not obtain the medicine", r4=MED_AR["none"]),
 T(3, sys="chest", v="A", e="Y", d="G", f="O", s3="A", s3f="I-2",
   r1="worse_breathing", r2d="No", att=2, attf="R-3", prv=1, prvf="I-3", acc=1,
   acct="Cost", r3=ACCESS_AR["cost"]),
 T(2, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="I-2",
   r1="fever_on", r2d="No", att=1, attf="I-2", prv=2, acc=1,
   acct="Other", r3=ACCESS_AR["other"]),

 # ---- unrelated returns
 T(4, sys="skin", v="A", e="Y", d="G", f="E", s3="A", s3f="I-2",
   r1="rash", r2d="Yes", rel=2, att=None, prv=2, prvf="I-3"),
 T(3, sys="head", v="A", e="Y", d="S", f="E", s3="A", s3f="I-3",
   r1="pain", r2d="Yes", rel=2, att=None, prv=2, prvf="I-3"),

 # ---- not eligible
 T(6, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="I-3",
   r1="scheduled", r2d="No", elig=2),
 T(5, sys="general", v="A", e="Y", d="G", f="N", s3="A", s3f="I-2",
   r1="admin", r2d="No", elig=3),
 T(7, sys="general", v="N", e="N", d="N", f="N", s3="C", s3f="more than one",
   r1="not_feeding", r2d="Yes", elig=4,
   note="Index note carries no examination, observations or diagnosis."),
 T(2, sys="general", v="A", e="Y", d="S", f="E", s3="A", s3f="I-2",
   r1="worse_breathing", r2d="No", elig=5,
   note="The index visit ended in admission, not discharge. This pair should not be in the sample."),
]

# how often the second reviewer differs, judgement by judgement
DISAGREE = {"elig": 0.04, "rel": 0.07, "att": 0.17, "prv": 0.19, "acc": 0.06,
            "s3": 0.11, "facts": 0.05}


def generate(n, start_pair, seed=20260820):
    """Invent n more cases beyond the pilot forty."""
    rng = random.Random(seed)
    pool = []
    for w, case in TEMPLATES:
        pool.extend([case] * w)

    out = []
    for i in range(n):
        base = dict(rng.choice(pool))
        base["pair"] = start_pair + i
        base["r1"] = rng.choice(AR.get(base["r1"], [base["r1"]]))
        base["ovr"] = dict(base.get("ovr") or {})

        # a little drift in what was written down, so the sheet is not 30 clones
        if rng.random() < 0.25:
            base["d"] = rng.choice("NGS")
        if rng.random() < 0.20:
            base["f"] = rng.choice("NEOP")

        ovr = base["ovr"]
        if base["elig"] == 1:
            if rng.random() < DISAGREE["elig"]:
                ovr["elig"] = rng.choice([2, 3, 4])
            if rng.random() < DISAGREE["rel"]:
                ovr["rel"] = 2 if base["rel"] == 1 else 1
                if ovr["rel"] == 2:
                    ovr["att"] = None
                else:
                    ovr["att"], ovr["attf"] = 1, "I-2"
            if base["att"] and "att" not in ovr and rng.random() < DISAGREE["att"]:
                alt = [c for c in (1, 2, 3, 4) if c != base["att"]]
                ovr["att"] = rng.choice(alt)
                ovr["attf"] = {1: "I-2", 2: "I-3", 3: "I-2", 4: "more than one"}[ovr["att"]]
            if rng.random() < DISAGREE["prv"]:
                ovr["prv"] = rng.choice([c for c in (1, 2, 3) if c != base["prv"]])
            if rng.random() < DISAGREE["acc"]:
                ovr["acc"] = 3 if base["acc"] == 1 else rng.choice([1, 3])
                if ovr["acc"] == 1:
                    ovr["acct"] = "Other"
        else:
            if rng.random() < DISAGREE["elig"]:
                ovr["elig"] = 1

        if rng.random() < DISAGREE["s3"]:
            ovr["s3"] = rng.choice([c for c in "AIC" if c != base["s3"]])
        if rng.random() < DISAGREE["facts"]:
            k = rng.choice(["v", "e", "d"])
            ovr[k] = rng.choice({"v": "APN", "e": "YNC", "d": "NGS"}[k])
        if rng.random() < 0.02:
            base["knew"] = "Yes"
        if rng.random() < 0.05 and base["covered"] == "Yes":
            base["covered"] = "No"
            base["note"] = "The workbook does not say how to handle this one."
        out.append(base)
    return out


# --------------------------------------------------------------- rendering
REVIEWER_INITIALS = {"Reviewer 1": "Waad", "Reviewer 2": "Ainaa"}


def review_date(pair, which):
    """Spread the reviews over working days, R2 a couple of days behind R1."""
    import datetime
    start = datetime.date(2026, 9, 14) if pair <= 40 else datetime.date(2026, 10, 5)
    step = (pair - 1) // 4 if pair <= 40 else (pair - 41) // 6
    d = start + datetime.timedelta(days=step + (2 if which == 2 else 0))
    while d.weekday() == 4:            # Friday
        d += datetime.timedelta(days=1)
    return d.isoformat()


def render(case, reviewer):
    """Turn one case into the row this reviewer typed."""
    which = 2 if reviewer.endswith("2") else 1
    c = dict(case)
    if which == 2:
        c.update(case["ovr"])

    pair = case["pair"]
    salt = pair + (7 if which == 2 else 0)

    # ---- the gates the sheet's own colouring enforces
    elig, rel, att = c["elig"], c["rel"], c["att"]
    prv, acc, acct = c["prv"], c["acc"], c["acct"]
    if elig != 1:
        rel = att = prv = acc = None
        acct = None
    elif rel == 2:
        att = None
    if acc != 1:
        acct = None

    sysword = c["sys"]
    row = {
        "Pair no.": pair,
        "Study ID": "2026-%04d" % pair,
        "Reviewer": reviewer,
        "Date of review": review_date(pair, which),
        "I-1 Vital signs documented": V[c["v"]],
        "I-2 Relevant system examined?": E[c["e"]],
        "I-3 Discharge instructions": D[c["d"]],
        "I-4 Follow-up directed to": F[c["f"]],
        "Was the discharge decision reasonable?": S3[c["s3"]],
        "Step 3 Basis - field": c["s3f"],
        "Step 3 Basis - reason": pick(STEP3, (c["s3"], c["s3f"]), sysword, salt),
        "Initials + date locked": "%s %s" % (REVIEWER_INITIALS[reviewer],
                                             review_date(pair, which)),
        "R-1 Reason for return - exact words": c["r1"],
        "R-2 Diagnosis different from index?": c["r2d"],
        "R-3 Access statement - exact words": c["r3"],
        "R-4 Medicine statement - exact words": c["r4"],
        "Step 5 Eligibility": ELIG[elig],
        "Note for Dr Amani": c["note"],
        "Workbook covered this pair?": c["covered"],
        "Did you recognise the child?": c["knew"],
    }

    if rel:
        row["Step 6 Relatedness"] = REL[rel]
        row["Step 6 Basis - field"] = "R-2" if c["r2d"] == "Yes" else "R-1"
    if att:
        row["Step 7 Attribution"] = ATT[att]
        row["Step 7 Basis - field"] = c["attf"]
        row["Step 7 Basis - reason"] = pick(STEP7, (att, c["attf"]), sysword, salt)
    if prv:
        row["Step 8 Preventability"] = PRV[prv]
        row["Step 8 Basis - field"] = c["prvf"]
    if acc:
        row["Step 9 Access barrier"] = ACC[acc]
        if acct:
            row["Step 9 Barrier type"] = acct
        if acc == 1:
            has3 = c["r3"] != NONE_DOC
            has4 = c["r4"] != NONE_DOC
            row["Step 9 Basis - field"] = ("both" if has3 and has4
                                           else "R-3" if has3 else "R-4" if has4
                                           else "none - nothing documented")
        else:
            row["Step 9 Basis - field"] = "none - nothing documented"
    return row


def main():
    cases40 = [dict(c) for c in PILOT]
    cases400 = cases40 + generate(360, 41)

    built = []
    for label, cases in [("40 pairs", cases40), ("400 pairs", cases400)]:
        for n in (1, 2):
            reviewer = "Reviewer %d" % n
            path = os.path.join(
                REF, "Reviewer %d Coding Sheet - %s (FAKE DATA).xlsx" % (n, label))
            make_xlsx.build(path, reviewer,
                            rows=[render(c, reviewer) for c in cases],
                            n_rows=len(cases),
                            banner=BANNER, banner_ar=BANNER_AR)
            built.append((path, len(cases)))
    for path, n in built:
        print("built %3d rows  %s" % (n, os.path.basename(path)))


if __name__ == "__main__":
    main()
