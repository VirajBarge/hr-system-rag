import random, datetime as dt, os
import pandas as pd
from config import *

random.seed(2026)
OUT = "/mnt/user-data/outputs/hr_rag_data/data"
os.makedirs(OUT, exist_ok=True)

M_FIRST = ["Aarav","Vihaan","Arjun","Rohit","Karthik","Siddharth","Rahul","Ankit","Pranav","Varun","Nikhil","Harsh","Manish","Suresh","Deepak","Akash","Gaurav","Vivek","Sandeep","Tarun","Mohit","Kunal","Aditya","Yash","Rakesh","Imran","Faisal","Joseph","Prakash","Naveen"]
F_FIRST = ["Ananya","Diya","Priya","Sneha","Kavya","Divya","Pooja","Neha","Shruti","Anjali","Meghana","Isha","Swati","Ritu","Nandini","Lavanya","Aishwarya","Bhavana","Tanvi","Sana","Fatima","Mariam","Harini","Sowmya","Rekha","Pallavi","Nisha","Radhika","Shalini","Vidya"]
LAST = ["Sharma","Iyer","Nair","Reddy","Patil","Kulkarni","Gowda","Rao","Menon","Joshi","Desai","Shetty","Naidu","Pillai","Bhat","Hegde","Kapoor","Mehta","Chatterjee","Banerjee","Singh","Khan","Fernandes","D'Souza","Agarwal","Verma","Jain","Gupta","Kamath","Shenoy","Raman","Krishnan","Mishra","Pandey","Thakur","Deshpande"]
LOCS = ["Bengaluru"]*60 + ["Pune"]*22 + ["Hyderabad"]*18
PT_STATE = {"Bengaluru": "Karnataka", "Pune": "Maharashtra", "Hyderabad": "Telangana"}
ROLES = {
 "Engineering": ["Software Engineer","Senior Software Engineer","Backend Engineer","Frontend Engineer","Full Stack Engineer","Mobile Engineer"],
 "Product & Design": ["Product Analyst","Product Manager","UX Designer","Senior UX Designer","Visual Designer"],
 "Data & AI": ["Data Analyst","Data Engineer","ML Engineer","Senior Data Scientist","MLOps Engineer"],
 "Quality Assurance": ["QA Engineer","Senior QA Engineer","SDET","Test Analyst"],
 "IT & Infrastructure": ["DevOps Engineer","Cloud Engineer","IT Support Executive","Security Analyst","Systems Administrator"],
 "Sales": ["Sales Executive","Account Executive","Business Development Associate","Senior Account Executive"],
 "Marketing": ["Marketing Executive","Content Strategist","Digital Marketing Specialist","Brand Associate"],
 "Customer Success": ["Customer Success Associate","Support Engineer","Customer Success Manager","Onboarding Specialist"],
 "Human Resources": ["HR Executive","Talent Acquisition Specialist","HR Business Partner","Payroll Specialist"],
 "Finance & Accounts": ["Accounts Executive","Financial Analyst","Senior Accountant","Accounts Payable Associate"],
 "Administration": ["Admin Executive","Facilities Coordinator","Office Administrator"],
}
DEPT_SIZES = {"Engineering": 36, "Product & Design": 10, "Data & AI": 14, "Quality Assurance": 12, "IT & Infrastructure": 10,
              "Sales": 14, "Marketing": 8, "Customer Success": 14, "Human Resources": 7, "Finance & Accounts": 7, "Administration": 4}
BANDS = {"L1": (4.2, 6.5), "L2": (6.5, 11), "L3": (11, 18), "L4": (18, 30), "L5": (30, 55), "L6": (55, 95)}  # CTC lakhs

def rdate(a, b):
    return a + dt.timedelta(days=random.randint(0, (b - a).days))

emps = []
used = set()
def newname(g):
    while True:
        n = f"{random.choice(M_FIRST if g=='M' else F_FIRST)} {random.choice(LAST)}"
        if n not in used:
            used.add(n); return n

def add(eid, name, g, dept, role, grade, jd, loc, mgr, etype="Full-time"):
    emps.append(dict(employee_id=eid, name=name, gender=g, department=dept, designation=role, grade=grade,
                     employment_type=etype, work_location=loc, date_of_joining=jd, reporting_manager_id=mgr))

# named leadership
add("AS1001", "Arvind Menon", "M", "Administration", "Chief Executive Officer", "L6", dt.date(2016, 6, 1), "Bengaluru", "")
add("AS1002", "Sunita Rao", "F", "Human Resources", "Head of Human Resources", "L5", dt.date(2018, 2, 12), "Bengaluru", "AS1001")
add("AS1003", "Rajesh Kulkarni", "M", "Finance & Accounts", "Head of Finance (CFO)", "L6", dt.date(2017, 4, 3), "Bengaluru", "AS1001")
add("AS1004", "Neha Bhargava", "F", "Engineering", "Head of Engineering (CTO)", "L6", dt.date(2016, 6, 1), "Bengaluru", "AS1001")
for n in ["Arvind Menon","Sunita Rao","Rajesh Kulkarni","Neha Bhargava","Meera Nair","Kavitha Sundaram","Imran Sheikh"]:
    used.add(n)

heads = {"Engineering": "AS1004", "Human Resources": "AS1002", "Finance & Accounts": "AS1003", "Administration": "AS1001"}
nid = 1005
for dept, size in DEPT_SIZES.items():
    if dept not in heads:
        g = random.choice("MF"); eid = f"AS{nid}"; nid += 1
        add(eid, newname(g), g, dept, f"Head of {dept}", "L5", rdate(dt.date(2017, 1, 1), dt.date(2021, 12, 31)), random.choice(["Bengaluru"]*3 + ["Pune","Hyderabad"]), "AS1001")
        heads[dept] = eid

# special named people
special = {"Imran Sheikh": ("M", "IT & Infrastructure", "Chief Information Security Officer (CISO)", "L5", dt.date(2019, 8, 5)),
           "Meera Nair": ("F", "Administration", "Legal & Compliance Manager / Data Protection Officer", "L4", dt.date(2019, 3, 18)),
           "Kavitha Sundaram": ("F", "Human Resources", "Senior HR Business Partner (IC Presiding Officer)", "L4", dt.date(2018, 9, 24))}
for nm, (g, d, r, gr, jd) in special.items():
    eid = f"AS{nid}"; nid += 1
    add(eid, nm, g, d, r, gr, jd, "Bengaluru", heads[d] if d != "IT & Infrastructure" else heads[d])

# fill departments
for dept, size in DEPT_SIZES.items():
    have = sum(1 for e in emps if e["department"] == dept)
    n_mgr = max(1, size // 8)
    for i in range(size - have):
        g = random.choice("MMFF") if dept not in ("Human Resources",) else random.choice("FFFM")
        eid = f"AS{nid}"; nid += 1
        r = random.random()
        if i < n_mgr and dept != "Administration": grade = "L4"
        elif r < .18: grade = "L1"
        elif r < .55: grade = "L2"
        else: grade = "L3"
        role = random.choice(ROLES[dept])
        if grade == "L4": role = {"Engineering": "Engineering Manager"}.get(dept, f"{dept.split(' &')[0]} Manager")
        if grade == "L1": role = "Associate " + role.split()[-1] if random.random() < .3 else role
        jd = rdate(dt.date(2019, 1, 1), dt.date(2026, 10, 15)) if grade != "L4" else rdate(dt.date(2019, 1, 1), dt.date(2023, 12, 31))
        if grade == "L1" and random.random() < .5: jd = rdate(dt.date(2024, 6, 1), dt.date(2026, 10, 20))
        add(eid, newname(g), g, dept, role, grade, jd, random.choice(LOCS), "")

# interns / contract
for i in range(6):
    g = random.choice("MF"); eid = f"AS{nid}"; nid += 1
    dept = random.choice(["Engineering","Data & AI","Marketing","Quality Assurance","Product & Design"])
    add(eid, newname(g), g, dept, "Intern - " + dept.split(" &")[0], "L1", rdate(dt.date(2026, 6, 1), dt.date(2026, 10, 1)), random.choice(LOCS), "", etype="Intern")
for i in range(5):
    g = random.choice("MF"); eid = f"AS{nid}"; nid += 1
    dept = random.choice(["Engineering","IT & Infrastructure","Customer Success","Quality Assurance"])
    add(eid, newname(g), g, dept, random.choice(ROLES[dept]), "L2", rdate(dt.date(2025, 3, 1), dt.date(2026, 8, 1)), random.choice(LOCS), "", etype="Contract")

df = pd.DataFrame(emps)
# reporting managers
mgrs = df[df.grade.isin(["L4", "L5"])]
def assign(row):
    if row.reporting_manager_id or row.employee_id == "AS1001": return row.reporting_manager_id
    if row.grade == "L4": return heads[row.department]
    pool = df[(df.department == row.department) & (df.grade == "L4")].employee_id.tolist()
    return random.choice(pool) if pool else heads[row.department]
df["reporting_manager_id"] = df.apply(assign, axis=1)
df.loc[df.employee_id.isin(["AS1005"]), "reporting_manager_id"] = "AS1001"
df["reporting_manager_id"] = df.apply(lambda r: "AS1001" if r.employee_id in heads.values() and r.employee_id != "AS1001" and r.employee_id not in ("AS1002","AS1003","AS1004") else r.reporting_manager_id, axis=1)
df.loc[df.employee_id.isin(["AS1002","AS1003","AS1004"]), "reporting_manager_id"] = "AS1001"
# fix self-manager: department heads themselves report to CEO
for eid in heads.values():
    if eid != "AS1001": df.loc[df.employee_id == eid, "reporting_manager_id"] = "AS1001"
df.loc[df.employee_id == "AS1001", "reporting_manager_id"] = ""

# status
df["date_of_joining"] = pd.to_datetime(df["date_of_joining"]).dt.date
df["status"] = "Active"
df["last_working_day"] = pd.Series([None]*len(df), dtype="object")
df["probation_status"] = df.date_of_joining.apply(lambda d: "On Probation" if (TODAY - d).days < 183 else "Confirmed")
df.loc[df.employment_type == "Intern", "probation_status"] = "Not Applicable"
df.loc[df.employment_type == "Contract", "probation_status"] = "Not Applicable"
# exits: 8 exited, 3 serving notice (non-leadership)
cand = df[(df.grade.isin(["L2", "L3", "L1"])) & (df.employment_type == "Full-time") & (df.probation_status == "Confirmed")].sample(11, random_state=7).index.tolist()
for i in cand[:8]:
    jd = df.at[i, "date_of_joining"]
    lwd = rdate(max(jd + dt.timedelta(days=200), dt.date(2025, 11, 1)), dt.date(2026, 9, 28))
    df.at[i, "status"] = "Exited"; df.at[i, "last_working_day"] = lwd
for i in cand[8:]:
    df.at[i, "status"] = "Serving Notice"; df.at[i, "last_working_day"] = rdate(dt.date(2026, 11, 20), dt.date(2027, 1, 15))
df["email"] = df.name.str.lower().str.replace(r"[^a-z ]", "", regex=True).str.replace(" ", ".") + "@aurelia-sys.example"
df["tenure_years"] = df.apply(lambda r: round(((r.last_working_day if r.last_working_day else TODAY) - r.date_of_joining).days / 365.25, 1), axis=1)
df["notice_period_days"] = df.apply(lambda r: 30 if r.probation_status == "On Probation" else (0 if r.employment_type == "Intern" else GRADES[r.grade][5]), axis=1)
manager_name = dict(zip(df.employee_id, df.name))
df["reporting_manager"] = df.reporting_manager_id.map(manager_name).fillna("")

# ---------------- SALARY STRUCTURE ----------------
def pt(loc): return 200
sal = []
for r in df.itertuples():
    if r.employment_type == "Intern":
        stipend = random.choice([15000, 18000, 20000, 25000])
        sal.append(dict(employee_id=r.employee_id, annual_ctc=stipend * 12, fixed_ctc=stipend * 12, variable_target_pct=0, variable_target_amount=0,
                        basic_monthly=stipend, hra_monthly=0, special_allowance_monthly=0, employer_pf_monthly=0, gratuity_monthly=0, gross_monthly=stipend,
                        employee_pf_monthly=0, professional_tax_monthly=0, last_revision_date="", salary_type="Stipend")); continue
    lo, hi = BANDS[r.grade]
    ctc = round(random.uniform(lo, hi) * 100000 / 1000) * 1000
    if r.employee_id == "AS1001": ctc = 9600000
    var_pct = GRADES[r.grade][1] if r.employment_type == "Full-time" else 0
    var_amt = round(ctc * var_pct / 100 / 100) * 100 if False else round(ctc * var_pct / (100 + var_pct) / 100) * 100
    fixed = ctc - var_amt
    basic = round(fixed * 0.40 / 12)
    hra = round(basic * 0.5)
    epf = 1800
    grat = round(basic * 0.0481)
    special = round(fixed / 12 - basic - hra - epf - grat)
    gross = basic + hra + special
    sal.append(dict(employee_id=r.employee_id, annual_ctc=ctc, fixed_ctc=fixed, variable_target_pct=var_pct, variable_target_amount=var_amt,
                    basic_monthly=basic, hra_monthly=hra, special_allowance_monthly=special, employer_pf_monthly=epf, gratuity_monthly=grat,
                    gross_monthly=gross, employee_pf_monthly=1800, professional_tax_monthly=200,
                    last_revision_date="2026-04-01" if (dt.date(2026, 4, 1) - r.date_of_joining).days > 180 else "", salary_type="CTC"))
sal = pd.DataFrame(sal)
sal["health_insurance_cover"] = df.employment_type.map(lambda t: "Not Applicable" if t == "Intern" else "INR 5,00,000 floater (self + spouse + 2 children)")
sal = sal.merge(df[["employee_id", "name", "grade", "department"]], on="employee_id")
sal = sal[["employee_id", "name", "department", "grade", "salary_type"] + [c for c in sal.columns if c not in ("employee_id","name","department","grade","salary_type")]]

# ---------------- APPRAISALS ----------------
def eligible_cycle(jd, fy_end_year):
    cutoff_full = dt.date(fy_end_year - 1, 9, 30); cutoff_pro = dt.date(fy_end_year - 1, 12, 31)
    return "Full" if jd <= cutoff_full else ("Pro-rata" if jd <= cutoff_pro else "Not eligible")
apps = []
for r in df.itertuples():
    if r.employment_type == "Intern" or r.employee_id == "AS1001": continue
    for fy, endy, lwd_ok in (("FY2024-25", 2025, dt.date(2025, 5, 15)), ("FY2025-26", 2026, dt.date(2026, 5, 15))):
        if r.date_of_joining > dt.date(endy - 1, 12, 31): continue
        if r.last_working_day and r.last_working_day <= dt.date(endy, 3, 31): continue
        rating = random.choices([5, 4, 3, 2, 1], weights=[5, 20, 58, 14, 3])[0]
        self_r = min(5, max(2, rating + random.choice([0, 0, 1, 1])))
        lo, hi = INCREMENT_BANDS[rating]
        inc = round(random.uniform(lo, hi), 1) if hi else 0.0
        elig = eligible_cycle(r.date_of_joining, endy)
        if elig == "Pro-rata": inc = round(inc * 0.5, 1)
        if elig == "Not eligible": inc = 0.0
        promo = "Yes" if (rating >= 4 and r.grade != "L6" and (dt.date(endy, 4, 1) - r.date_of_joining).days > 540 and random.random() < .35 and r.grade in ("L1","L2","L3")) else "No"
        bonus_mult = BONUS_MULT[rating]
        company_factor = 95 if fy == "FY2024-25" else 105
        apps.append(dict(employee_id=r.employee_id, name=r.name, department=r.department, grade_at_review=r.grade, appraisal_cycle=fy,
                         reviewer_id=r.reporting_manager_id, self_rating=self_r, manager_rating=min(5, max(1, rating + random.choice([0, 0, 0, -1]))),
                         final_rating=rating, final_rating_label=RATINGS[rating], goal_score_pct=min(100, max(35, int(random.gauss(55 + rating * 8, 6)))),
                         values_score_pct=min(100, max(40, int(random.gauss(55 + rating * 8, 7)))), increment_eligibility=elig,
                         increment_pct=inc, promotion_recommended=promo, bonus_target_pct=GRADES[r.grade][1] if r.employment_type == "Full-time" else 0,
                         individual_bonus_multiplier_pct=bonus_mult, company_performance_factor_pct=company_factor,
                         pip_recommended="Yes" if rating == 1 else "No", effective_date=f"{endy}-04-01",
                         letter_issued_on=f"{endy}-05-{random.randint(8,15):02d}"))
apps = pd.DataFrame(apps)

# ---------------- LEAVE ----------------
active = df[(df.status != "Exited") & (df.employment_type != "Intern")].copy()
# also interns get CL/SL only (policy: interns get 1 CL per month, no EL) -> keep out for simplicity but mention in policy
leave_rows, req = [], []
lid = 1
def working_days(a, b): return sum(1 for i in range((b - a).days + 1) if is_workday(a + dt.timedelta(days=i)))
def calc_days(ltype, a, b):
    if ltype in ("Casual Leave", "Sick Leave"): return (b - a).days + 1       # sandwich rule
    if ltype in ("Maternity Leave",): return (b - a).days + 1
    return working_days(a, b)
def pick_start(lo, hi, wd=None):
    while True:
        d = rdate(lo, hi)
        if is_workday(d) and (wd is None or d.weekday() in wd): return d
def reason(t):
    return random.choice({
     "Casual Leave": ["Personal work","Family function","Bank / government office visit","Home maintenance","Child's school event"],
     "Sick Leave": ["Fever and cold","Viral infection","Migraine","Stomach infection","Dental procedure","Back pain"],
     "Earned Leave": ["Family vacation","Visit to hometown","Travel","Festival at home","Personal break","Wedding in family"]}[t])

e_status = {}
for r in active.itertuples():
    jd = r.date_of_joining
    y0 = dt.date(2026, 1, 1)
    start_ref = max(jd, y0)
    months_left = 12 - (start_ref.month - 1) - (1 if (start_ref > y0 and start_ref.day > 15) else 0)
    months_left = max(0, months_left)
    frac = months_left / 12
    cl_ent = round(LEAVE_V3["cl"] * frac); sl_ent = round(LEAVE_V3["sl"] * frac)
    if r.employment_type == "Contract": cl_ent, sl_ent = (cl_ent, sl_ent)
    # EL
    if jd < y0:
        opening_el = round(min(LEAVE_V3["el_cap"], random.choice([0, 2, 4, 5.5, 7, 9, 10.5, 12, 15, 18, 20, 24])) * min(1, (dt.date(2025,12,31)-jd).days/365 + .2), 1)
        accr_months = 10  # Jan..Oct credited by 06-Nov
    else:
        opening_el = 0.0
        accr_months = max(0, 10 - (start_ref.month - 1) - (1 if start_ref.day > 15 else 0))
    el_accrued = round(accr_months * LEAVE_V3["el_per_month"], 1)
    el_eligible_to_use = r.probation_status != "On Probation"
    e_status[r.employee_id] = dict(cl_ent=cl_ent, sl_ent=sl_ent, opening_el=opening_el, el_accrued=el_accrued)
    horizon_end = min(TODAY - dt.timedelta(days=1), r.last_working_day - dt.timedelta(days=1) if r.last_working_day else TODAY)
    lo = start_ref + dt.timedelta(days=3)
    if lo >= horizon_end: continue
    used = {"Casual Leave": 0, "Sick Leave": 0, "Earned Leave": 0}
    def make(ltype, a, b, status="Approved", rs=None, half=False, days=None):
        global lid
        days = days if days is not None else (0.5 if half else calc_days(ltype, a, b))
        applied = a - dt.timedelta(days=(0 if ltype == "Sick Leave" else random.randint(1, 14)))
        if applied > TODAY: applied = TODAY
        mg = r.reporting_manager_id or "AS1001"
        req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type=ltype, start_date=a, end_date=b, days=days,
                        half_day="Yes" if half else "No", reason=rs or "", applied_on=applied, status=status,
                        approver_id=mg, approved_on=(applied + dt.timedelta(days=random.choice([0, 0, 1, 1, 2]))) if status in ("Approved", "Rejected") else "",
                        remarks=""))
        lid += 1
        return days
    # casual
    left = cl_ent; tries = 0
    target = random.randint(0, cl_ent)
    while used["Casual Leave"] < target and tries < 10:
        tries += 1
        half = random.random() < .2
        span = 1 if half else random.choice([1, 1, 1, 2, 2, 3])
        a = pick_start(lo, horizon_end, wd=[0, 1, 2, 3, 4] if span == 1 else [0, 1, 2])
        b = a + dt.timedelta(days=span - 1)
        if not is_workday(b) or b > horizon_end: continue
        dys = 0.5 if half else span
        if used["Casual Leave"] + dys > cl_ent: continue
        used["Casual Leave"] += make("Casual Leave", a, b, rs=reason("Casual Leave"), half=half)
    # sick
    target = random.randint(0, sl_ent); tries = 0
    while used["Sick Leave"] < target and tries < 10:
        tries += 1
        span = random.choice([1, 1, 1, 2, 2, 3, 4]); a = pick_start(lo, horizon_end, wd=[0, 1, 2, 3, 4] if span <= 2 else [0, 1])
        b = a + dt.timedelta(days=span - 1)
        if not is_workday(b) or b > horizon_end or used["Sick Leave"] + span > sl_ent: continue
        n = make("Sick Leave", a, b, rs=reason("Sick Leave"))
        if span > 2: req[-1]["remarks"] = "Medical certificate submitted"
        used["Sick Leave"] += n
    # earned (not during probation)
    if el_eligible_to_use:
        avail = opening_el + el_accrued
        trips = random.choice([0, 1, 1, 2, 2, 3]); budget = avail * random.uniform(.3, .85)
        for _ in range(trips):
            span = random.choice([2, 3, 4, 5, 5, 7, 10]); a = pick_start(lo, horizon_end)
            b = a + dt.timedelta(days=span + random.randint(0, 3))
            while not is_workday(b): b -= dt.timedelta(days=1)
            d = calc_days("Earned Leave", a, b)
            if b > horizon_end or used["Earned Leave"] + d > budget or d > avail: continue
            used["Earned Leave"] += make("Earned Leave", a, b, rs=reason("Earned Leave"))
    # upcoming approved / pending (Nov-Dec)
    if el_eligible_to_use and random.random() < .35 and (not r.last_working_day):
        a = pick_start(dt.date(2026, 11, 12), dt.date(2026, 12, 28)); b = a + dt.timedelta(days=random.choice([1, 2, 4]))
        while not is_workday(b): b += dt.timedelta(days=1)
        d = calc_days("Earned Leave", a, b)
        if used["Earned Leave"] + d + 1 < opening_el + el_accrued:
            st = random.choice(["Approved", "Approved", "Pending"])
            make("Earned Leave", a, b, status=st, rs="Year-end break")
            if st == "Approved": used["Earned Leave"] += 0  # tracked separately as upcoming
    # rejected / cancelled examples
    if random.random() < .06:
        a = pick_start(lo, horizon_end); make("Casual Leave", a, a, status="Rejected", rs="Personal work", days=1); req[-1]["remarks"] = "Rejected: critical release that day"
    if random.random() < .05:
        a = pick_start(lo, horizon_end); make("Earned Leave", a, a + dt.timedelta(days=1), status="Cancelled", rs="Plan changed"); req[-1]["remarks"] = "Cancelled by employee"

# floating holidays (2 each for most)
fl_names = {d: n for d, n in FLOATING_HOLIDAYS_2026}
fl_used = {}
for r in active.itertuples():
    if r.date_of_joining > dt.date(2026, 8, 31): continue
    cnt = random.choice([0, 1, 2, 2, 2])
    ds = random.sample([d for d, _ in FLOATING_HOLIDAYS_2026 if d < TODAY], k=min(cnt, 2)) if cnt else []
    fl_used[r.employee_id] = len(ds)
    for d in ds:
        req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Floating Holiday", start_date=d, end_date=d, days=1,
                        half_day="No", reason=fl_names[d], applied_on=d - dt.timedelta(days=random.randint(3, 20)), status="Approved",
                        approver_id=r.reporting_manager_id or "AS1001", approved_on=d - dt.timedelta(days=2), remarks="")); lid += 1

# special leaves
fem = active[(active.gender == "F") & (active.employment_type == "Full-time") & (active.probation_status == "Confirmed")]
for r in fem.sample(2, random_state=3).itertuples():
    a = dt.date(2026, random.choice([3, 5]), random.randint(2, 20)); 
    while not is_workday(a): a += dt.timedelta(days=1)
    b = a + dt.timedelta(days=181)
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Maternity Leave", start_date=a, end_date=b, days=182, half_day="No",
                    reason="Maternity (26 weeks, first child)", applied_on=a - dt.timedelta(days=60), status="Approved", approver_id=r.reporting_manager_id,
                    approved_on=a - dt.timedelta(days=50), remarks="Statutory maternity benefit")); lid += 1
mal = active[(active.gender == "M") & (active.employment_type == "Full-time") & (active.probation_status == "Confirmed")]
for r in mal.sample(3, random_state=4).itertuples():
    a = pick_start(dt.date(2026, 2, 1), dt.date(2026, 9, 1), wd=[0]); b = a + dt.timedelta(days=11)
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Paternity Leave", start_date=a, end_date=b, days=working_days(a, b), half_day="No",
                    reason="Birth of child", applied_on=a - dt.timedelta(days=15), status="Approved", approver_id=r.reporting_manager_id, approved_on=a - dt.timedelta(days=12), remarks="")); lid += 1
for r in active[active.probation_status == "Confirmed"].sample(3, random_state=5).itertuples():
    a = pick_start(dt.date(2026, 2, 1), dt.date(2026, 8, 30), wd=[0]); b = a + dt.timedelta(days=4)
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Marriage Leave", start_date=a, end_date=b, days=5, half_day="No",
                    reason="Own marriage", applied_on=a - dt.timedelta(days=40), status="Approved", approver_id=r.reporting_manager_id, approved_on=a - dt.timedelta(days=35), remarks="Invitation card submitted")); lid += 1
for r in active.sample(2, random_state=6).itertuples():
    a = pick_start(dt.date(2026, 3, 1), dt.date(2026, 9, 15), wd=[0, 1, 2]); b = a + dt.timedelta(days=4)
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Bereavement Leave", start_date=a, end_date=b, days=working_days(a, b), half_day="No",
                    reason="Demise of immediate family member", applied_on=a, status="Approved", approver_id=r.reporting_manager_id, approved_on=a, remarks="")); lid += 1
for r in active.sample(4, random_state=8).itertuples():
    a = pick_start(dt.date(2026, 4, 1), dt.date(2026, 10, 28)); 
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Loss of Pay", start_date=a, end_date=a + dt.timedelta(days=1) if is_workday(a + dt.timedelta(days=1)) else a, days=2 if is_workday(a + dt.timedelta(days=1)) else 1,
                    half_day="No", reason="Leave balance exhausted", applied_on=a - dt.timedelta(days=2), status="Approved", approver_id=r.reporting_manager_id, approved_on=a - dt.timedelta(days=1), remarks="Leave without pay")); lid += 1
# comp off earned/availed
for r in active.sample(10, random_state=9).itertuples():
    a = pick_start(dt.date(2026, 5, 1), dt.date(2026, 10, 25)); 
    req.append(dict(leave_id=f"LV-2026-{lid:05d}", employee_id=r.employee_id, leave_type="Comp Off", start_date=a, end_date=a, days=1, half_day="No", reason="Weekend release support",
                    applied_on=a - dt.timedelta(days=3), status="Approved", approver_id=r.reporting_manager_id, approved_on=a - dt.timedelta(days=2), remarks="Worked on Saturday for production release")); lid += 1

leaves = pd.DataFrame(req).sort_values(["start_date", "employee_id"]).reset_index(drop=True)
leaves["leave_id"] = [f"LV-2026-{i+1:05d}" for i in range(len(leaves))]
leaves = leaves.merge(df[["employee_id", "name"]], on="employee_id")
leaves = leaves[["leave_id", "employee_id", "name", "leave_type", "start_date", "end_date", "days", "half_day", "reason", "applied_on", "status", "approver_id", "approved_on", "remarks"]]

# balances (as of 06-Nov-2026)
bal = []
appr = leaves[leaves.status == "Approved"].copy()
for r in df[(df.status != "Exited") & (df.employment_type != "Intern")].itertuples():
    st = e_status.get(r.employee_id)
    if not st: continue
    mine = appr[appr.employee_id == r.employee_id]
    def taken(t): return mine[(mine.leave_type == t) & (mine.start_date < TODAY)].days.sum()
    def upc(t): return mine[(mine.leave_type == t) & (mine.start_date >= TODAY)].days.sum()
    pend = leaves[(leaves.employee_id == r.employee_id) & (leaves.status == "Pending")].days.sum()
    fl_taken = taken("Floating Holiday")
    bal.append(dict(employee_id=r.employee_id, name=r.name, as_of_date=TODAY, leave_year=2026,
        cl_entitlement=st["cl_ent"], cl_taken=taken("Casual Leave"), cl_balance=st["cl_ent"] - taken("Casual Leave") - upc("Casual Leave"),
        sl_entitlement=st["sl_ent"], sl_taken=taken("Sick Leave"), sl_balance=st["sl_ent"] - taken("Sick Leave") - upc("Sick Leave"),
        el_opening_carry_forward=st["opening_el"], el_accrued_ytd=st["el_accrued"], el_taken=taken("Earned Leave"), el_upcoming_approved=upc("Earned Leave"),
        el_pending_approval=pend, el_balance=round(st["opening_el"] + st["el_accrued"] - taken("Earned Leave") - upc("Earned Leave"), 1),
        floating_holidays_entitled=2, floating_holidays_used=fl_taken, floating_holidays_balance=2 - fl_taken,
        comp_off_taken=taken("Comp Off"), lop_days=taken("Loss of Pay"),
        el_usable_note="EL can be availed only after confirmation" if r.probation_status == "On Probation" else ""))
bal = pd.DataFrame(bal)

# ---------------- REIMBURSEMENTS ----------------
cats = [("Travel - Flight", 3500, 14000), ("Travel - Train/Bus", 600, 3500), ("Hotel", 2500, 9000), ("Meals (per diem)", 400, 1500),
        ("Local Conveyance", 150, 1800), ("Internet Bill", 700, 1000), ("Client Entertainment", 1500, 8000), ("Learning & Certification", 3000, 25000),
        ("Mobile Bill", 300, 500), ("Ergonomic Allowance", 4000, 10000)]
cl = []
cid = 1
act = df[(df.status != "Exited") & (df.employment_type != "Intern") & (df.probation_status != "On Probation")]
for r in act.sample(70, random_state=11).itertuples():
    for _ in range(random.choice([1, 1, 2, 3])):
        c, lo_, hi_ = random.choice(cats)
        if c == "Mobile Bill" and r.grade in ("L1", "L2"): c = "Internet Bill"
        amt = random.randrange(lo_, hi_, 50)
        if c == "Internet Bill": amt = min(1000, amt)
        if c == "Mobile Bill": amt = min(500, amt)
        if c == "Learning & Certification": amt = min(LEARNING_BUDGET, amt)
        exp = rdate(dt.date(2026, 3, 1), dt.date(2026, 10, 28))
        sub = exp + dt.timedelta(days=random.randint(1, 45))
        if sub > TODAY: sub = TODAY
        late = (sub - exp).days > 30
        hotel_lim = GRADES[r.grade][2] if r.work_location else 0
        over = (c == "Hotel" and amt > hotel_lim)
        status = random.choices(["Paid", "Approved", "Pending", "Rejected"], weights=[75, 8, 10, 7])[0]
        remark = ""
        if late: status = "Rejected"; remark = "Submitted after 30-day claim window"
        elif over and status != "Pending": remark = f"Amount above grade limit ({inr(hotel_lim)}/night); excess not reimbursed" if status == "Paid" else ""
        if c == "Mobile Bill" and r.grade in ("L1", "L2"): status = "Rejected"; remark = "Mobile allowance applies to L3 and above"
        paid_on = (sub + dt.timedelta(days=random.randint(5, 20))) if status == "Paid" else ""
        if paid_on and paid_on > TODAY: status = "Approved"; paid_on = ""
        cl.append(dict(claim_id=f"RC-2026-{cid:04d}", employee_id=r.employee_id, name=r.name, grade=r.grade, category=c, expense_date=exp, claim_submitted_on=sub,
                       amount_claimed=amt, amount_approved=(min(amt, hotel_lim) if (c == "Hotel" and over) else amt) if status in ("Paid", "Approved") else 0,
                       status=status, approver_id=r.reporting_manager_id or "AS1001", paid_on=paid_on, remarks=remark)); cid += 1
claims = pd.DataFrame(cl).sort_values("expense_date").reset_index(drop=True)

# ---------------- PAYROLL OCT 2026 ----------------
def tds_month(gross_monthly, ctc_variable=0):
    annual = gross_monthly * 12 + ctc_variable * 0
    taxable = max(0, annual - 75000)
    slabs = [(400000, 0), (800000, .05), (1200000, .10), (1600000, .15), (2000000, .20), (2400000, .25), (10**9, .30)]
    tax, prev = 0, 0
    for lim, rt in slabs:
        if taxable > prev: tax += (min(taxable, lim) - prev) * rt
        prev = lim
    if taxable <= 1200000: tax = 0
    return round(tax * 1.04 / 12)
pay = []
oct1, oct31 = dt.date(2026, 10, 1), dt.date(2026, 10, 31)
paid_claims_oct = claims[(claims.status == "Paid") & (pd.to_datetime(claims.paid_on).dt.month == 10)].groupby("employee_id").amount_approved.sum()
for r in df.itertuples():
    if r.status == "Exited" and r.last_working_day < oct1: continue
    if r.date_of_joining > oct31: continue
    s = sal[sal.employee_id == r.employee_id].iloc[0]
    days_in = 31
    start = max(r.date_of_joining, oct1); end = min(r.last_working_day, oct31) if r.last_working_day else oct31
    payable_cal = (end - start).days + 1
    lop = leaves[(leaves.employee_id == r.employee_id) & (leaves.leave_type == "Loss of Pay") & (pd.to_datetime(leaves.start_date).dt.month == 10)].days.sum()
    paid_days = payable_cal - lop
    f = paid_days / days_in
    basic = round(s.basic_monthly * f); hra = round(s.hra_monthly * f); spl = round(s.special_allowance_monthly * f)
    gross = basic + hra + spl
    reimb = int(paid_claims_oct.get(r.employee_id, 0))
    pf = round(s.employee_pf_monthly * f) if s.salary_type == "CTC" else 0
    ptx = int(s.professional_tax_monthly) if s.salary_type == "CTC" else 0
    tds = tds_month(s.gross_monthly) if s.salary_type == "CTC" else 0
    net = gross + reimb - pf - ptx - tds
    pay.append(dict(employee_id=r.employee_id, name=r.name, pay_month="October 2026", calendar_days=days_in, lop_days=lop, paid_days=paid_days,
                    basic=basic, hra=hra, special_allowance=spl, gross_earnings=gross, reimbursements=reimb, employee_pf=pf, professional_tax=ptx,
                    income_tax_tds=tds, total_deductions=pf + ptx + tds, net_pay=net, employer_pf=round(s.employer_pf_monthly * f),
                    bank_name=random.choice(["HDFC Bank","ICICI Bank","Axis Bank","State Bank of India","Kotak Mahindra Bank"]), pay_date="2026-10-31"))
pay = pd.DataFrame(pay)

# ---------------- ATTENDANCE (Jul-Oct 2026) ----------------
att = []
lv_days = {}
for row in leaves[leaves.status == "Approved"].itertuples():
    for i in range((row.end_date - row.start_date).days + 1):
        d = row.start_date + dt.timedelta(days=i)
        if is_workday(d) or row.leave_type in ("Casual Leave", "Sick Leave", "Maternity Leave"):
            if row.leave_type in ("Floating Holiday", "Comp Off") or is_workday(d) or row.leave_type in ("Casual Leave", "Sick Leave", "Maternity Leave"):
                lv_days[(row.employee_id, d.month)] = lv_days.get((row.employee_id, d.month), 0) + (0.5 if row.half_day == "Yes" else 1 if d.weekday() < 5 and is_workday(d) else 0)
for r in df.itertuples():
    if r.status == "Exited" or r.employment_type == "Intern" and False: continue
    for m in (7, 8, 9, 10):
        wd = sum(1 for i in range(31) if (dt.date(2026, m, 1) + dt.timedelta(days=i)).month == m and is_workday(dt.date(2026, m, 1) + dt.timedelta(days=i)))
        if r.date_of_joining > dt.date(2026, m, 28): continue
        lv = min(wd, lv_days.get((r.employee_id, m), 0))
        office_req = 4 if r.probation_status == "On Probation" or r.employment_type == "Intern" else 3
        weeks = wd / 5
        office = max(0, round(random.gauss(office_req * weeks * 0.97, 1.2)))
        office = min(int(wd - lv), office)
        wfh = max(0, int(wd - lv - office))
        late = random.choices([0, 1, 2, 3, 4, 5], weights=[45, 22, 14, 10, 6, 3])[0]
        att.append(dict(employee_id=r.employee_id, name=r.name, month=f"2026-{m:02d}", working_days=wd, days_in_office=office, days_wfh=wfh, leave_days=lv,
                        late_marks=late, regularisations_used=random.choices([0, 1, 2, 3], weights=[55, 25, 14, 6])[0],
                        avg_daily_hours=round(random.gauss(8.5, .5), 1), cl_deducted_for_late_marks=0.5 * (late // 3)))
att = pd.DataFrame(att)

# ---------------- HOLIDAYS / DEPARTMENTS ----------------
hol = pd.DataFrame([dict(date=d, day=d.strftime("%A"), holiday=n, type="Fixed Holiday", falls_on_weekend="Yes" if d.weekday() >= 5 else "No") for d, n in FIXED_HOLIDAYS_2026] +
                   [dict(date=d, day=d.strftime("%A"), holiday=n, type="Floating Holiday (choose any 2)", falls_on_weekend="Yes" if d.weekday() >= 5 else "No") for d, n in FLOATING_HOLIDAYS_2026]).sort_values("date")
dep = pd.DataFrame([dict(department=n, code=c, head_id=heads[n], head_name=manager_name[heads[n]],
                         headcount_active=int(((df.department == n) & (df.status != "Exited")).sum())) for n, c in DEPARTMENTS])

# order columns & write
emp_out = df[["employee_id", "name", "gender", "email", "department", "designation", "grade", "employment_type", "work_location", "date_of_joining",
              "probation_status", "reporting_manager_id", "reporting_manager", "notice_period_days", "status", "last_working_day", "tenure_years"]]
emp_out.to_csv(f"{OUT}/employees.csv", index=False)
sal.to_csv(f"{OUT}/salary_structure.csv", index=False)
pay.to_csv(f"{OUT}/payroll_october_2026.csv", index=False)
apps.to_csv(f"{OUT}/appraisals.csv", index=False)
leaves.to_csv(f"{OUT}/leave_requests_2026.csv", index=False)
bal.to_csv(f"{OUT}/leave_balances_2026.csv", index=False)
att.to_csv(f"{OUT}/attendance_summary_jul_oct_2026.csv", index=False)
claims.to_csv(f"{OUT}/reimbursement_claims_2026.csv", index=False)
hol.to_csv(f"{OUT}/holidays_2026.csv", index=False)
dep.to_csv(f"{OUT}/departments.csv", index=False)
pd.to_pickle(dict(df=df, sal=sal, pay=pay, apps=apps, bal=bal, leaves=leaves), "/home/claude/hr/data.pkl")
for n, d in [("employees", emp_out), ("salary", sal), ("payroll", pay), ("appraisals", apps), ("leave_requests", leaves), ("leave_balances", bal), ("attendance", att), ("claims", claims)]:
    print(n, d.shape)
