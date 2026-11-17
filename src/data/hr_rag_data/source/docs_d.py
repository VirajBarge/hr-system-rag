import pandas as pd, datetime as dt
from hrlib import *
from config import *

BASE = "/mnt/user-data/outputs/hr_rag_data/"
D = pd.read_pickle("/home/claude/hr/data.pkl")
EMP, SAL, PAY, APPS, BAL, LV = D["df"], D["sal"], D["pay"], D["apps"], D["bal"], D["leaves"]

def long(d):
    d = pd.to_datetime(d); return d.strftime("%d %B %Y")

def sign_block(name, title):
    return [Spacer(1, 26), P(f"<b>{name}</b><br/>{title}<br/>{CO['name']}", "letter")]

# ------------------------------------------------------------ holiday calendar
def holiday_calendar():
    s = [Spacer(1, 6), P("Holiday Calendar 2026", "title"), P(f"{CO['name']}  |  Applicable to Bengaluru, Pune and Hyderabad offices", "subtitle"),
         P("Document ID: HR-CAL-2026  |  Published: 15 December 2025  |  Version 1.0", "small"), Spacer(1, 8),
         P("Fixed holidays (11)", "h1")]
    rows = [[d.strftime("%d %b %Y"), d.strftime("%A"), n, "Falls on weekend - no substitute holiday" if d.weekday() >= 5 else "Working day holiday"] for d, n in FIXED_HOLIDAYS_2026]
    s.append(table(["Date", "Day", "Occasion", "Remark"], rows, [18, 16, 40, 26]))
    s += [Spacer(1, 6), P("Of the 11 fixed holidays, 1 (Independence Day, 15 August) falls on a Saturday, so employees get 10 weekday holidays in 2026.", "body"),
          P("Floating (optional) holidays - choose any 2", "h1")]
    rows = [[d.strftime("%d %b %Y"), d.strftime("%A"), n] for d, n in FLOATING_HOLIDAYS_2026]
    s.append(table(["Date", "Day", "Occasion"], rows, [20, 20, 60]))
    s += note_box("Each employee may take 2 Floating Holidays in the 2026 leave year, chosen from the six dates above. Apply in PeopleHub at least 3 working days in advance. Floating Holidays cannot be carried forward or encashed. See HR-POL-001 Leave Policy v3.0, Section 8.", "How floating holidays work")
    s += [P("General notes", "h2"), P("1. Saturdays and Sundays are weekly offs. 2. Fixed holidays that fall on weekends are not substituted. 3. Employees on call or on shift duty on a fixed holiday earn compensatory off as per the Leave Policy. 4. The Diwali holiday has been observed on Monday 9 November 2026 (the festival day itself falls on Sunday 8 November). 5. Pune office observes Maharashtra Day on 1 May together with Labour Day as one holiday.", "body")]
    build(BASE + "policies/HR-CAL-2026_Holiday_Calendar_2026.pdf", s, "Holiday Calendar 2026", "HR-CAL-2026", "1.0")

# ------------------------------------------------------------ FAQ handbook
def faq():
    v = LEAVE_V3
    qa = [
     ("Leave", [
      ("How many casual leaves do I get in a year?", f"You get {v['cl']} days of Casual Leave per leave year (1 January to 31 December). It is credited in full on 1 January, prorated if you join mid-year, and lapses on 31 December. You can take at most {3} consecutive days of CL at a time."),
      ("How many sick leaves do I get? When do I need a medical certificate?", f"You get {v['sl']} days of Sick Leave per year. A medical certificate is needed if SL exceeds 2 consecutive days, and a fitness certificate if you are absent for more than 5 consecutive working days. Inform your manager by 10:30 am on the first day."),
      ("How does Earned Leave work?", f"Earned Leave accrues at {v['el_per_month']} days per completed month ({v['el_year']} days a year). You can carry forward up to {v['el_cap']} days to the next year. It is encashed only when you leave the company, at Basic / 26 per day. Probationers accrue EL but can use it only after confirmation."),
      ("Can I encash my leave while I am still employed?", "No. Earned Leave is encashed only at separation. CL, SL, Floating Holidays and Comp Off are never encashed."),
      ("What is the sandwich rule?", "If a weekend or holiday falls between two days of Casual Leave or Sick Leave, those days are also counted as leave. For example, CL on Friday and Monday counts as 4 days. It does not apply to Earned Leave."),
      ("How much notice do I need to give for leave?", "Up to 3 days: 3 working days' notice (1 working day for CL; SL inform the same day). 4 to 10 days: 7 working days. 11 to 15 days: 15 calendar days. More than 15 days (non-statutory): 30 calendar days and Head of HR approval."),
      ("How many days of maternity and paternity leave are there?", f"Maternity leave is 26 weeks for the first two children and 12 weeks from the third child, as per the Maternity Benefit Act. Paternity leave is {v['paternity']} working days. Adoption leave is {v['adoption_weeks']} weeks for a child under three months. Marriage leave is {v['marriage']} working days and bereavement leave is {v['bereavement']} working days."),
      ("How many floating holidays do I get?", "Two per year, chosen from the optional list in the Holiday Calendar (Makar Sankranti/Pongal, Holi, Bakrid, Onam, Raksha Bandhan, Guru Nanak Jayanti in 2026)."),
      ("What happens to EL if I resign?", "Your unused EL balance is paid out in the full and final settlement. Any leave taken during your notice period extends your last working day by the same number of days."),
     ]),
     ("Attendance and work location", [
      ("What are the office hours?", "9:30 am to 6:30 pm, Monday to Friday, with a one-hour flexible lunch. Core hours are 11:00 am to 4:00 pm."),
      ("What is a late mark?", "Checking in after 9:45 am (a 15-minute grace period applies). Every 3 late marks in a month lead to a deduction of 0.5 day of Casual Leave."),
      ("How many days a week must I be in the office?", "From 1 July 2026, at least 3 days a week, with Tuesday, Wednesday and Thursday as anchor days. Probationers and interns must be in the office 4 days a week."),
      ("Can I work from another city or country?", "Work from Anywhere is allowed for up to 15 working days a year within India with manager approval and 5 working days' notice. Working from outside India needs approval from the Head of HR, Head of Finance and the CISO."),
      ("Do I get overtime pay?", "No. Work on weekends or holidays approved in advance earns compensatory off (0.5 day for 4 hours, 1 day for 8 hours), valid for 60 days. On-call duty earns \u20b91,500 per week for rostered employees."),
     ]),
     ("Pay and benefits", [
      ("When is salary paid?", "On the last working day of every month. Attendance and leave inputs are frozen on the 25th."),
      ("What is my CTC made of?", "Basic is 40% of Fixed CTC, HRA is 50% of Basic, Special Allowance is the balance, plus employer PF of \u20b91,800 per month and gratuity of 4.81% of Basic. Variable pay is a percentage of Fixed CTC by grade (L1 5%, L2 8%, L3 10%, L4 12%, L5 15%, L6 20%)."),
      ("What health insurance do I have?", "Group health insurance of \u20b95,00,000 on a family floater (you, spouse and up to 2 children) from day one, paid by the Company. Parents can be added at your cost through a top-up."),
      ("When is gratuity payable?", "After 5 years of continuous service (except death or disablement). It is 15 days of last drawn Basic per completed year, up to \u20b920,00,000."),
      ("What is the internet and mobile reimbursement?", f"Hybrid employees can claim up to {inr(INTERNET_ALLOW)} a month for internet. Employees at L3 and above can claim up to {inr(MOBILE_ALLOW)} a month for mobile bills. A one-time ergonomic allowance of {inr(ERGO_ALLOW)} is available every 3 years."),
     ]),
     ("Performance and growth", [
      ("When is the appraisal cycle?", "The cycle follows the financial year (April to March). Goals are set in April, a mid-year check-in happens in October, and the annual review runs from April to mid-May with letters by 15 May. Increments are effective 1 April and bonus is paid with June salary."),
      ("What are the performance ratings?", "5 Outstanding, 4 Exceeds Expectations, 3 Meets Expectations, 2 Partially Meets Expectations, 1 Does Not Meet Expectations."),
      ("Who is eligible for an increment?", "Confirmed employees who joined on or before 30 September get the full increment; those who joined 1 October to 31 December get 50%; later joiners are reviewed in the next cycle. Employees serving notice or on a PIP on 31 March are not eligible."),
      ("What do I need to be promoted?", "A rating of 4 or 5 in the latest cycle, at least 3 in the previous cycle, 18 months in your current grade, demonstration of next-grade competencies and a business need."),
      ("How do I appeal my rating?", "In writing to your HR Business Partner within 10 working days of the rating communication. A Review Panel decides within 15 working days."),
     ]),
     ("Exit, probation and policies", [
      ("How long is probation and what is the notice period?", "Probation is 6 months (extendable by up to 3 months). The notice period is 30 days on probation, 60 days for confirmed L1 to L3, and 90 days for L4 to L6."),
      ("Can I buy out my notice period?", "Yes, with approval of your Department Head and HR. You pay monthly gross divided by 30 for each day of shortfall."),
      ("How long does full and final settlement take?", "Within 45 days of your last working day, subject to clearance."),
      ("Where do I report a grievance?", "First your manager (informal), then your HR Business Partner (Stage 1), the Grievance Committee (Stage 2) and finally the CEO (Stage 3). Sexual harassment complaints go to the Internal Committee at ic@aurelia-sys.example."),
      ("How do I claim travel or other expenses?", "Submit the claim in PeopleHub within 30 days of the expense, with bills for amounts of \u20b9500 or more. Late claims are rejected."),
      ("Who is the Data Protection Officer?", f"{DPO}, reachable at {CO['privacy_mail']}. Report any data breach within 2 hours to {CO['security_mail']}."),
      ("Can I take up a freelance project on weekends?", "No. Moonlighting and paid outside work that conflicts with Company work are not allowed without written approval of the Head of HR."),
     ]),
    ]
    s = [Spacer(1, 6), P("Employee Handbook - Quick Guide and FAQ", "title"), P(f"{CO['name']}  |  2026 Edition", "subtitle"),
         P("This guide summarises the most frequently asked questions. It is a summary only. In case of any difference, the full policy document (HR-POL-001 to HR-POL-013) prevails.", "body")]
    n = 0
    for sec, items in qa:
        s.append(P(sec, "h1"))
        for q, a in items:
            n += 1
            s += [KeepTogether([P(f"Q{n}. {q}", "h2"), P(a, "body")])]
    build(BASE + "policies/HR-HBK-2026_Employee_Handbook_Quick_Guide_FAQ.pdf", s, "Employee Handbook - Quick Guide and FAQ", "HR-HBK-2026", "2026.1")

# ------------------------------------------------------------ circulars
def circular(num, date, subject, body, fname, sign=("Sunita Rao", "Head of Human Resources")):
    s = [Spacer(1, 4), P(f"<b>CIRCULAR No. {num}</b>", "letter"), P(f"Date: {date}", "letter"), P("To: All employees (Bengaluru, Pune, Hyderabad)", "letter"),
         P(f"<b>Subject: {subject}</b>", "letter"), HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=8)]
    s += body + sign_block(*sign)
    build(BASE + "circulars/" + fname, s, subject, num, "", letterhead=True, footer_note="Internal circular - for employees of Aurelia Systems only")

def circulars():
    L = lambda t: P(t, "letter")
    circular("HR-CIR-2025-031", "12 December 2025", "Revision of Leave Policy effective 1 January 2026", [
        L("Dear colleagues,"),
        L("In recognition of the importance of rest and family time, the Company has revised the Leave Policy. Version 3.0 (HR-POL-001) comes into effect from <b>1 January 2026</b> and replaces Version 2.1 (effective 1 April 2023). The key changes are summarised below."),
        table(["Item", "Earlier (v2.1)", "From 1 Jan 2026 (v3.0)"], [
            ["Casual Leave", "7 days", "8 days"], ["Sick Leave", "7 days", "8 days"],
            ["Earned Leave", "15 days a year (1.25 per month)", "18 days a year (1.5 per month)"],
            ["EL carry-forward cap", "20 days", "30 days"], ["Max consecutive CL", "2 days", "3 days"],
            ["Medical certificate required if SL exceeds", "3 consecutive days", "2 consecutive days"],
            ["Paternity leave", "5 working days", "10 working days (can be taken in two blocks)"],
            ["Bereavement leave", "3 working days", "5 working days"],
            ["Floating holidays", "1 per year", "2 per year"],
            ["Marriage leave", "Not available", "5 working days, once in service"],
            ["Adoption leave", "Not available", "12 weeks for a child under three months"]], [32, 30, 38]),
        Spacer(1, 8),
        L("The additional CL, SL and EL for 2026 have been credited to all eligible employees' balances in PeopleHub. The higher EL carry-forward cap of 30 days has been applied to balances carried forward from 2025 into 2026. The sandwich rule, leave approval matrix and encashment rules are unchanged."),
        L("Please refer to the Leave Policy v3.0 on PeopleHub for details. For queries, write to hr@aurelia-sys.example.")],
        "HR-CIR-2025-031_Leave_Policy_Revision_effective_1_Jan_2026.pdf")
    circular("HR-CIR-2026-014", "12 June 2026", "Revised Hybrid Work Policy effective 1 July 2026", [
        L("Dear colleagues,"),
        L("After reviewing feedback from teams and the results of our in-person collaboration pilot, the Company has revised its Hybrid Work Policy. <b>Version 2.0 (HR-POL-003) is effective from 1 July 2026.</b>"),
        P("What is changing", "h2"),
        table(["Item", "Until 30 June 2026", "From 1 July 2026"], [
            ["Minimum days in office", "2 days a week", "3 days a week"],
            ["Anchor days", "None", "Tuesday, Wednesday and Thursday"],
            ["Probationers and interns", "2 days a week", "4 days a week"],
            ["Ad-hoc work from home on an anchor day", "Not defined", "Up to 6 days per quarter with manager intimation"]], [34, 30, 36]),
        Spacer(1, 8),
        L("Work from Anywhere (15 days a year within India), the internet reimbursement of \u20b91,000 per month and the ergonomic allowance of \u20b910,000 once in 3 years are unchanged. Department Heads who need a different anchor-day pattern for a team should write to HR before 25 June 2026."),
        L("Thank you for your continued flexibility and commitment.")],
        "HR-CIR-2026-014_Hybrid_Work_Policy_Revision_effective_1_Jul_2026.pdf")
    circular("HR-CIR-2026-019", "26 October 2026", "Diwali holiday and year-end calendar", [
        L("Dear colleagues,"),
        L("The Company will observe <b>Monday, 9 November 2026</b> as the Diwali holiday (Govardhan Puja / Balipratipada). The festival day itself falls on Sunday, 8 November."),
        L("Employees on production support or on-call duty on 9 November will receive compensatory off as per the Leave Policy. The Company will remain closed on 25 December 2026 (Christmas Day). The last date for submitting leave and reimbursement claims for inclusion in the December payroll is Friday, 25 December 2026 (payroll cut-off is the 25th of every month)."),
        L("Employees who have not yet used both Floating Holidays for 2026 are reminded that the remaining optional holiday in the calendar is Guru Nanak Jayanti on Tuesday, 24 November 2026. Floating Holidays lapse on 31 December and cannot be carried forward or encashed."),
        L("Happy Diwali to you and your families.")],
        "HR-CIR-2026-019_Diwali_Holiday_and_Year_End_Calendar.pdf")

# ------------------------------------------------------------ forms
def forms():
    def line(lbl): return [P(f"<b>{lbl}</b>", "cell"), P("", "cell")]
    # leave application form
    s = [Spacer(1, 4), P("Leave Application Form", "title"), P("Form HR-FRM-001  |  Use only if PeopleHub is unavailable; otherwise apply in PeopleHub > My Leave", "subtitle")]
    def tab(rows, w=(28, 72)):
        t = Table([[Paragraph(esc(a), ST["cellb"]), Paragraph(esc(b), ST["cell"])] for a, b in rows], colWidths=[CW * w[0] / 100, CW * w[1] / 100], rowHeights=None)
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (0, -1), LIGHT), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
        return t
    s += [P("A. Employee details", "h2"), tab([("Employee name", ""), ("Employee ID", ""), ("Department / Grade", ""), ("Reporting manager", "")]),
          P("B. Leave details", "h2"), tab([("Type of leave (tick one)", "[ ] Casual   [ ] Sick   [ ] Earned   [ ] Floating Holiday   [ ] Comp Off   [ ] Maternity   [ ] Paternity   [ ] Marriage   [ ] Bereavement   [ ] LOP"),
                                           ("From (date) / To (date)", ""), ("Total working days (half day = 0.5)", ""), ("Reason for leave", ""), ("Contact number during leave", ""), ("Handover arranged with", "")]),
          P("C. Declaration", "h2"), P("I confirm that the above information is correct. I understand that leave is subject to approval, that weekends and holidays between two days of CL/SL are counted as leave (sandwich rule), and that a medical certificate is required if Sick Leave exceeds 2 consecutive days.", "body"),
          tab([("Employee signature / date", "")]), P("D. For office use", "h2"),
          tab([("Reporting manager (Approved / Rejected)", ""), ("Department Head (if more than 5 days)", ""), ("HR (if more than 15 days)", ""), ("Leave balance after this leave", "CL ____   SL ____   EL ____")])]
    build(BASE + "forms/HR-FRM-001_Leave_Application_Form.pdf", s, "Leave Application Form", "HR-FRM-001", "3.0")
    # reimbursement form
    s = [Spacer(1, 4), P("Expense Reimbursement Claim Form", "title"), P("Form HR-FRM-002  |  Submit within 30 days of the expense or return from travel", "subtitle")]
    s += [P("A. Employee details", "h2"), tab([("Employee name / ID", ""), ("Grade / Department", ""), ("Purpose of expense / trip", ""), ("Travel dates (if applicable)", "")]),
          P("B. Expense details", "h2"),
          table(["#", "Date", "Category", "Description", "Bill no.", "Amount (INR)"], [[str(i), "", "", "", "", ""] for i in range(1, 9)] + [["", "", "", "", "<b>Total</b>", ""]], [5, 14, 20, 31, 15, 15], zebra=False),
          Spacer(1, 8), P("Categories: Flight / Train / Hotel / Meals (per diem) / Local conveyance / Internet / Mobile / Client entertainment / Learning / Ergonomic. Attach original bills for each expense of \u20b9500 and above. Hotel and meal claims above grade limits are reimbursed only up to the limit (HR-POL-009).", "small"),
          P("C. Declaration and approvals", "h2"), tab([("Employee signature / date", ""), ("Reporting manager approval / date", ""), ("Department Head (trip cost above \u20b950,000)", ""), ("Finance verification / date", "")])]
    build(BASE + "forms/HR-FRM-002_Expense_Reimbursement_Claim_Form.pdf", s, "Expense Reimbursement Claim Form", "HR-FRM-002", "2.0")

# ------------------------------------------------------------ employee-specific letters
def pick(eid): 
    return EMP[EMP.employee_id == eid].iloc[0], SAL[SAL.employee_id == eid].iloc[0]

def offer_letter():
    cand = EMP[(EMP.grade == "L3") & (EMP.status == "Active") & (EMP.employment_type == "Full-time") & (EMP.probation_status == "Confirmed")].iloc[0]
    e, sl = pick(cand.employee_id)
    jd = e.date_of_joining
    L = lambda t: P(t, "letter")
    s = [Spacer(1, 2), L(f"Date: {long(jd - dt.timedelta(days=21))}"), L(f"<b>Private and Confidential</b><br/>{e['name']}"),
         L(f"<b>Subject: Offer of employment - {e.designation} ({e.grade})</b>"), L(f"Dear {e['name'].split()[0]},"),
         L(f"We are pleased to offer you the position of <b>{e.designation}</b> in the <b>{e.department}</b> department of {CO['name']}, at grade <b>{e.grade}</b>, based at our <b>{e.work_location}</b> office. Your expected date of joining is <b>{long(jd)}</b>, and you will report to {e.reporting_manager}."),
         L(f"Your total annual compensation (CTC) will be <b>{inr(sl.annual_ctc)}</b>, comprising Fixed CTC of {inr(sl.fixed_ctc)} and a variable pay target of {inr(sl.variable_target_amount)} ({sl.variable_target_pct}% of Fixed CTC), as detailed in Annexure A. Variable pay is paid as annual performance bonus in accordance with the Performance Appraisal Policy (HR-POL-010)."),
         L("Your employment will be on probation for six months from the date of joining. During probation the notice period is 30 days on either side. After confirmation, the notice period applicable to your grade will be 60 days (grades L1 to L3) or 90 days (L4 to L6)."),
         L("This offer is subject to: satisfactory background verification and reference checks; submission of the documents listed in the Onboarding and Probation Policy (HR-POL-013); and your confirming that you are not bound by any restrictive agreement with a previous employer. You will be covered by the Company's group health insurance of \u20b95,00,000 from the date of joining."),
         L("Please sign and return a copy of this letter within 7 days to accept the offer. We look forward to welcoming you to Aurelia Systems.")]
    s += sign_block("Sunita Rao", "Head of Human Resources") + [Spacer(1, 6), P("Accepted: ______________________   Date: ______________", "letter"), PageBreak()]
    basic, hra, spl, epf, gr = [int(sl[c]) * 12 for c in ("basic_monthly", "hra_monthly", "special_allowance_monthly", "employer_pf_monthly", "gratuity_monthly")]
    s += [P("Annexure A - Compensation breakup", "h1"), P(f"Employee: {e['name']}  |  Grade: {e.grade}", "body"),
          table(["Component", "Monthly (INR)", "Annual (INR)"], [
              ["Basic salary (40% of Fixed CTC)", inr(sl.basic_monthly, False), inr(basic, False)],
              ["House Rent Allowance (50% of Basic)", inr(sl.hra_monthly, False), inr(hra, False)],
              ["Special Allowance", inr(sl.special_allowance_monthly, False), inr(spl, False)],
              ["Employer PF contribution", inr(sl.employer_pf_monthly, False), inr(epf, False)],
              ["Gratuity provision (4.81% of Basic)", inr(sl.gratuity_monthly, False), inr(gr, False)],
              ["<b>Fixed CTC</b>", inr(sl.fixed_ctc / 12, False), inr(sl.fixed_ctc, False)],
              [f"Variable pay target ({sl.variable_target_pct}% of Fixed CTC)", "-", inr(sl.variable_target_amount, False)],
              ["<b>Total CTC</b>", "-", inr(sl.annual_ctc, False)]], [50, 25, 25]),
          Spacer(1, 8), P(f"Monthly gross salary (Basic + HRA + Special Allowance): {inr(sl.gross_monthly)}. Deductions: employee PF \u20b91,800, professional tax \u20b9200, TDS as applicable. Benefits: group health insurance \u20b95,00,000 family floater; group personal accident \u20b910,00,000; group term life 3x Fixed CTC; learning budget \u20b925,000 a year.", "body")]
    build(BASE + "letters/Sample_Offer_Letter_%s.pdf" % e.employee_id, s, "Offer Letter", f"HR-LTR-OFR-{e.employee_id}", "", letterhead=True, footer_note="Confidential - Offer letter")

def appraisal_letters():
    # three employees with different outcomes in FY2025-26
    a = APPS[(APPS.appraisal_cycle == "FY2025-26") & (APPS.grade_at_review.isin(["L1", "L2", "L3", "L4"]))]
    picks = []
    for crit in [(a.final_rating == 4) & (a.promotion_recommended == "Yes"), (a.final_rating == 3) & (a.increment_eligibility == "Full"), (a.final_rating == 5)]:
        sub = a[crit]
        if len(sub): picks.append(sub.iloc[0])
    for r in picks:
        e, sl = pick(r.employee_id)
        prev_ctc = sl.annual_ctc / (1 + r.increment_pct / 100)
        L = lambda t: P(t, "letter")
        new_grade = {"L1": "L2", "L2": "L3", "L3": "L4"}.get(r.grade_at_review, r.grade_at_review) if r.promotion_recommended == "Yes" else r.grade_at_review
        bonus = int(round(sl.variable_target_amount * r.company_performance_factor_pct / 100 * r.individual_bonus_multiplier_pct / 100))
        s = [L(f"Date: {long(r.letter_issued_on)}"), L(f"<b>Private and Confidential</b><br/>{e['name']} ({e.employee_id})<br/>{e.designation}, {e.department}"),
             L(f"<b>Subject: Performance review outcome and revision of compensation - {r.appraisal_cycle}</b>"), L(f"Dear {e['name'].split()[0]},"),
             L(f"We have completed the performance review for {r.appraisal_cycle} following the calibration process. Your final performance rating is <b>{r.final_rating} - {r.final_rating_label}</b>."),
             L(f"Based on your rating and eligibility ({r.increment_eligibility.lower()} cycle), your compensation has been revised by <b>{r.increment_pct}%</b> with effect from <b>1 April 2026</b>. Your revised annual CTC is <b>{inr(sl.annual_ctc)}</b> (previously {inr(prev_ctc)}). The arrears for April 2026 were paid with your May 2026 salary.")]
        if r.promotion_recommended == "Yes":
            s.append(L(f"We are also pleased to inform you that you have been <b>promoted from grade {r.grade_at_review} to grade {new_grade}</b> with effect from 1 April 2026, in recognition of your performance and growth. The promotion increment is included in the revision above, subject to the pay range of the new grade."))
        s.append(L(f"Annual performance bonus for {r.appraisal_cycle}: variable target {inr(sl.variable_target_amount)} x Company performance factor {r.company_performance_factor_pct}% x individual multiplier {r.individual_bonus_multiplier_pct}% = approximately <b>{inr(bonus)}</b>, payable with June 2026 salary, subject to you being in service on the date of payment."))
        s.append(L("If you disagree with your rating, you may appeal in writing to your HR Business Partner within 10 working days of this communication, as per the Performance Appraisal Policy (HR-POL-010). Thank you for your contribution to Aurelia Systems."))
        s += sign_block("Sunita Rao", "Head of Human Resources")
        build(BASE + f"letters/Sample_Appraisal_Letter_{r.employee_id}_{r.appraisal_cycle}.pdf", s, "Appraisal Letter", f"HR-LTR-APR-{r.employee_id}", "", letterhead=True, footer_note="Confidential - Appraisal letter")

def pip_letter():
    act = set(EMP[EMP.status == "Active"].employee_id)
    r = APPS[(APPS.final_rating == 1) & (APPS.appraisal_cycle == "FY2025-26") & (APPS.employee_id.isin(act))]
    if not len(r): r = APPS[(APPS.final_rating == 2) & (APPS.appraisal_cycle == "FY2025-26") & (APPS.employee_id.isin(act))]
    r = r.iloc[0]; e, sl = pick(r.employee_id)
    L = lambda t: P(t, "letter")
    start = dt.date(2026, 5, 18); end = start + dt.timedelta(days=59)
    s = [L(f"Date: {long(start)}"), L(f"<b>Private and Confidential</b><br/>{e['name']} ({e.employee_id})<br/>{e.designation}, {e.department}"),
         L("<b>Subject: Performance Improvement Plan (PIP)</b>"), L(f"Dear {e['name'].split()[0]},"),
         L(f"Your performance in {r.appraisal_cycle} was rated {r.final_rating} - {r.final_rating_label}. As discussed with your manager and HR, you are being placed on a Performance Improvement Plan for <b>60 days, from {long(start)} to {long(end)}</b>, under the Performance Appraisal Policy (HR-POL-010)."),
         P("Areas for improvement and goals", "h2"),
         table(["Area", "Expected outcome by end of PIP", "Measure"], [
             ["Delivery", "Complete assigned sprint commitments on time", "At least 90% of committed items delivered each sprint"],
             ["Quality", "Reduce defects returned from review/QA", "Fewer than 2 reopened items per sprint"],
             ["Communication", "Share weekly status and flag risks early", "Weekly update sent every Friday"]], [20, 45, 35]),
         Spacer(1, 6),
         L(f"You will have weekly check-ins with your manager, {e.reporting_manager}, and HR will review progress at 30 days and at the end of the PIP. During the PIP you are not eligible for increments, promotion or bonus. The possible outcomes are: successful completion, a one-time extension of up to 30 days, or separation in accordance with HR-POL-012 if the improvement is not achieved."),
         L("Please sign below to acknowledge receipt. This does not mean that you agree with the assessment.")]
    s += sign_block("Sunita Rao", "Head of Human Resources") + [P("Employee acknowledgement: ______________________   Date: ______________", "letter")]
    build(BASE + f"letters/Sample_PIP_Letter_{e.employee_id}.pdf", s, "Performance Improvement Plan", f"HR-LTR-PIP-{e.employee_id}", "", letterhead=True, footer_note="Confidential - Performance Improvement Plan")

def exit_letters():
    ex = EMP[EMP.status == "Exited"].iloc[0]; e, sl = pick(ex.employee_id)
    L = lambda t: P(t, "letter")
    lwd = long(e.last_working_day)
    s = [L(f"Date: {long(pd.to_datetime(e.last_working_day) + dt.timedelta(days=5))}"), L(f"<b>{e['name']}</b> ({e.employee_id})"),
         L("<b>Subject: Relieving and Experience Letter</b>"), L("To whom it may concern,"),
         L(f"This is to certify that <b>{e['name']}</b> was employed with {CO['name']} as <b>{e.designation}</b> in the {e.department} department from <b>{long(e.date_of_joining)}</b> to <b>{lwd}</b>, a period of approximately {e.tenure_years} years. The employee has been relieved from the services of the Company at the close of business on {lwd}, after completing the notice period and the exit formalities, and has no dues pending towards the Company."),
         L(f"During the tenure, the employee's conduct and performance were found to be satisfactory. We thank {e['name'].split()[0]} for the contribution and wish the best for future endeavours.")]
    s += sign_block("Sunita Rao", "Head of Human Resources")
    build(BASE + f"letters/Sample_Relieving_Experience_Letter_{e.employee_id}.pdf", s, "Relieving and Experience Letter", f"HR-LTR-REL-{e.employee_id}", "", letterhead=True, footer_note="Confidential")

def payslips():
    for eid in ["AS1004", "AS1010", "AS1030", "AS1060", "AS1090"]:
        if eid not in set(PAY.employee_id): continue
        p = PAY[PAY.employee_id == eid].iloc[0]; e, sl = pick(eid)
        st = [Spacer(1, 2), P(f"<b>Payslip for the month of {p.pay_month}</b>", "letter")]
        info = [["Employee name", e["name"], "Employee ID", eid], ["Designation", e.designation, "Department", e.department],
                ["Grade", e.grade, "Location", e.work_location], ["Date of joining", long(e.date_of_joining), "Pay date", long(p.pay_date)],
                ["Bank", p.bank_name, "Paid days / LOP days", f"{int(p.paid_days)} / {int(p.lop_days)}"]]
        t = Table([[Paragraph(f"<b>{esc(a)}</b>", ST["cell"]), Paragraph(esc(b), ST["cell"]), Paragraph(f"<b>{esc(c)}</b>", ST["cell"]), Paragraph(esc(d), ST["cell"])] for a, b, c, d in info],
                  colWidths=[CW * .2, CW * .32, CW * .2, CW * .28])
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BACKGROUND", (0, 0), (0, -1), LIGHT), ("BACKGROUND", (2, 0), (2, -1), LIGHT), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
        st += [t, Spacer(1, 10)]
        earn = [["Basic", inr(p.basic, False)], ["House Rent Allowance", inr(p.hra, False)], ["Special Allowance", inr(p.special_allowance, False)], ["Reimbursements", inr(p.reimbursements, False)]]
        ded = [["Provident Fund (employee)", inr(p.employee_pf, False)], ["Professional Tax", inr(p.professional_tax, False)], ["Income Tax (TDS)", inr(p.income_tax_tds, False)], ["", ""]]
        rows = [[earn[i][0], earn[i][1], ded[i][0], ded[i][1]] for i in range(4)]
        rows.append([f"<b>Total earnings</b>", f"<b>{inr(p.gross_earnings + p.reimbursements, False)}</b>", "<b>Total deductions</b>", f"<b>{inr(p.total_deductions, False)}</b>"])
        st += [table(["Earnings", "Amount (INR)", "Deductions", "Amount (INR)"], rows, [32, 18, 32, 18], zebra=False), Spacer(1, 8),
               P(f"<b>Net pay: {inr(p.net_pay)}</b>", "letter"), P(f"Employer PF contribution this month: {inr(p.employer_pf)} (not part of net pay). Annual CTC: {inr(sl.annual_ctc)}.", "small"),
               Spacer(1, 4), P("This is a computer-generated payslip and does not require a signature. Salary information is confidential (HR-POL-011).", "small")]
        build(BASE + f"payslips/Payslip_{eid}_Oct_2026.pdf", st, "Payslip - October 2026", f"PAY-{eid}-2026-10", "", letterhead=True, footer_note="Confidential - Payslip")

if __name__ == "__main__":
    holiday_calendar(); faq(); circulars(); forms(); offer_letter(); appraisal_letters(); pip_letter(); exit_letters(); payslips(); print("ok")
