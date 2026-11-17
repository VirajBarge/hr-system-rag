"""Single source of truth for the fictional company 'Aurelia Systems Pvt. Ltd.'
Every policy PDF and every CSV reads numbers from here so documents never contradict each other."""
import datetime as dt

TODAY = dt.date(2026, 11, 6)

CO = dict(
    name="Aurelia Systems Pvt. Ltd.",
    short="Aurelia Systems",
    cin="U72900KA2016PTC089412",
    founded=2016,
    hq="4th Floor, Prestige Tech Hub, Outer Ring Road, Marathahalli, Bengaluru, Karnataka 560103",
    pune="Block C, Panchshil Business Park, Hinjewadi Phase 2, Pune, Maharashtra 411057",
    hyd="Level 7, Mindspace IT Park, HITEC City, Hyderabad, Telangana 500081",
    hr_mail="hr@aurelia-sys.example",
    payroll_mail="payroll@aurelia-sys.example",
    privacy_mail="privacy@aurelia-sys.example",
    security_mail="security@aurelia-sys.example",
    speakup_mail="speakup@aurelia-sys.example",
    posh_mail="ic@aurelia-sys.example",
    hrms="Aurelia PeopleHub",
    helpdesk="PeopleHub > Help > Raise an HR ticket",
)

# People who appear by name in policies (also seeded into employees.csv)
CEO = ("AS1001", "Arvind Menon")
CHRO = ("AS1002", "Sunita Rao")            # Head of Human Resources
CFO = ("AS1003", "Rajesh Kulkarni")        # Head of Finance
CTO = ("AS1004", "Neha Bhargava")          # Head of Engineering
DPO = "Meera Nair"                         # Data Protection Officer (Legal & Compliance, reports to CHRO for HR data matters)
IC_PRESIDING = "Kavitha Sundaram"
IC_EXTERNAL = "Adv. Lakshmi Prabhu (external member, legal expert)"
CISO = "Imran Sheikh"

GRADES = {  # grade: (title band, variable target %, hotel metro, hotel non-metro, meal per diem, notice days)
    "L1": ("Associate / Trainee", 5, 4000, 2500, 700, 60),
    "L2": ("Engineer / Executive", 8, 4000, 2500, 700, 60),
    "L3": ("Senior Engineer / Senior Executive", 10, 6000, 4000, 1000, 60),
    "L4": ("Lead / Manager", 12, 6000, 4000, 1000, 90),
    "L5": ("Senior Manager / Director", 15, 9000, 6500, 1500, 90),
    "L6": ("VP and above", 20, 9000, 6500, 1500, 90),
}

DEPARTMENTS = [  # name, code, head level
    ("Engineering", "ENG"), ("Product & Design", "PRD"), ("Data & AI", "DAI"),
    ("Quality Assurance", "QAT"), ("IT & Infrastructure", "ITI"), ("Sales", "SAL"),
    ("Marketing", "MKT"), ("Customer Success", "CSU"), ("Human Resources", "HRD"),
    ("Finance & Accounts", "FIN"), ("Administration", "ADM"),
]

# ---------------- LEAVE POLICY PARAMETERS (two versions on purpose) ----------------
LEAVE_V3 = dict(
    version="3.0", doc_id="HR-POL-001", effective="01 January 2026", approved="12 December 2025",
    cl=8, sl=8, el_year=18, el_per_month=1.5, el_cap=30, paternity=10, bereavement=5,
    marriage=5, floating=2, adoption_weeks=12, status="Current",
    revision_note="Increased CL, SL and EL entitlements; raised EL carry-forward cap; extended paternity and bereavement leave; added marriage leave, adoption leave and a second floating holiday.",
)
LEAVE_V21 = dict(
    version="2.1", doc_id="HR-POL-001", effective="01 April 2023", approved="20 March 2023",
    cl=7, sl=7, el_year=15, el_per_month=1.25, el_cap=20, paternity=5, bereavement=3,
    marriage=0, floating=1, adoption_weeks=0, status="Superseded by v3.0 on 01 January 2026",
    revision_note="Annual revision aligning leave year to calendar year and introducing floating holidays.",
)

# ---------------- HOLIDAYS 2026 ----------------
FIXED_HOLIDAYS_2026 = [
    (dt.date(2026, 1, 1), "New Year's Day"),
    (dt.date(2026, 1, 26), "Republic Day"),
    (dt.date(2026, 3, 19), "Ugadi / Gudi Padwa"),
    (dt.date(2026, 4, 3), "Good Friday"),
    (dt.date(2026, 5, 1), "Labour Day / Maharashtra Day"),
    (dt.date(2026, 8, 15), "Independence Day"),
    (dt.date(2026, 9, 14), "Ganesh Chaturthi"),
    (dt.date(2026, 10, 2), "Gandhi Jayanti"),
    (dt.date(2026, 10, 20), "Dussehra (Vijayadashami)"),
    (dt.date(2026, 11, 9), "Diwali (Govardhan Puja / Balipratipada)"),
    (dt.date(2026, 12, 25), "Christmas Day"),
]
FLOATING_HOLIDAYS_2026 = [
    (dt.date(2026, 1, 14), "Makar Sankranti / Pongal"),
    (dt.date(2026, 3, 4), "Holi"),
    (dt.date(2026, 5, 27), "Bakrid / Eid al-Adha"),
    (dt.date(2026, 8, 26), "Onam"),
    (dt.date(2026, 8, 28), "Raksha Bandhan"),
    (dt.date(2026, 11, 24), "Guru Nanak Jayanti"),
]
FIXED_SET = {d for d, _ in FIXED_HOLIDAYS_2026}

def is_workday(d):
    return d.weekday() < 5 and d not in FIXED_SET

# ---------------- APPRAISAL PARAMETERS ----------------
RATINGS = {5: "Outstanding", 4: "Exceeds Expectations", 3: "Meets Expectations",
           2: "Partially Meets Expectations", 1: "Does Not Meet Expectations"}
INCREMENT_BANDS = {5: (15, 20), 4: (10, 14), 3: (6, 9), 2: (0, 4), 1: (0, 0)}
BONUS_MULT = {5: 150, 4: 120, 3: 100, 2: 50, 1: 0}
DISTRIBUTION = {5: "up to 5%", 4: "about 20%", 3: "55% to 60%", 2: "about 12%", 1: "up to 3%"}

# ---------------- TRAVEL ----------------
INTERNET_ALLOW = 1000      # per month, hybrid employees on submission of bill
ERGO_ALLOW = 10000         # one-time, every 3 years
LEARNING_BUDGET = 25000    # per year
MOBILE_ALLOW = 500         # per month (L3 and above)

def inr(n, symbol=True):
    n = int(round(n))
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:]); head = head[:-2]
        if head: parts.insert(0, head)
        s = ",".join(parts + [tail])
    return ("\u20b9" if symbol else "") + ("-" if n < 0 else "") + s
