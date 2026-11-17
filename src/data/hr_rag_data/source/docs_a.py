from hrlib import *
from config import *

OUTDIR = "/mnt/user-data/outputs/hr_rag_data/policies/"
APPLIES_ALL = "All employees of Aurelia Systems Pvt. Ltd. (Bengaluru, Pune, Hyderabad)"

# =============================================================== LEAVE POLICY
def leave_policy(p, fname):
    cur = p["version"] == "3.0"
    cert_days = 2 if cur else 3
    cl_consec = 3 if cur else 2
    sections = []
    sections.append(dict(title="Purpose, scope and applicability", items=[
        ("p", "Aurelia Systems believes that rest, health and time with family are essential to sustained performance. This policy sets out the types of leave available to employees, how leave is earned, how it is applied for and approved, and what happens to unused leave."),
        ("c", "This policy applies to all full-time employees, contract employees on Aurelia payroll, and (to the limited extent stated in Section 12) interns of Aurelia Systems across all offices."),
        ("c", "Leave is a facility granted by the Company and is not an absolute right. Approval is subject to business requirements, subject to the statutory entitlements described in Section 7, which cannot be declined."),
        ("c", "This policy should be read with HR-POL-002 (Attendance and Working Hours), HR-POL-012 (Separation and Exit) and the annual Holiday Calendar."),
    ] + ([("note", f"This is Version {p['version']} of the Leave Policy. It was effective from {p['effective']} and has been SUPERSEDED by Version 3.0 effective 01 January 2026. It is retained for audit and historical reference only. Employees must refer to Version 3.0 for all leave entitlements applicable from 01 January 2026.", "Superseded document")] if not cur else [])))
    sections.append(dict(title="Definitions and leave year", items=[
        ("c", "Leave year: The leave year runs from 1 January to 31 December (calendar year)."),
        ("c", "Working day: Monday to Friday, excluding the fixed holidays published in the Holiday Calendar for the year. Saturdays and Sundays are weekly offs."),
        ("c", "Confirmed employee: An employee who has successfully completed probation and received a confirmation letter (see HR-POL-013)."),
        ("c", f"Leave balance: The number of days of a leave type available to an employee on a given date, visible in {CO['hrms']} under My Leave."),
        ("c", "Immediate family: Spouse, children, parents, siblings and parents-in-law of the employee."),
    ]))
    ent_rows = [
        ["Casual Leave (CL)", f"{p['cl']} days per leave year", "Credited in full on 1 January (prorated for new joiners)", "No - lapses on 31 December", "No"],
        ["Sick Leave (SL)", f"{p['sl']} days per leave year", "Credited in full on 1 January (prorated for new joiners)", "No - lapses on 31 December", "No"],
        ["Earned Leave (EL)", f"{p['el_year']} days per leave year", f"Accrued at {p['el_per_month']} days per completed month of service", f"Yes - up to {p['el_cap']} days", "Yes - only at separation"],
        ["Floating Holiday", f"{p['floating']} day{'s' if p['floating']>1 else ''} per leave year", "Chosen from the list in the Holiday Calendar", "No", "No"],
        ["Maternity Leave", "26 weeks (first two children); 12 weeks (third child onwards)", "As per Maternity Benefit Act, 1961", "Not applicable", "No"],
        ["Paternity Leave", f"{p['paternity']} working days", "Per birth/adoption event", "Not applicable", "No"],
        ["Bereavement Leave", f"{p['bereavement']} working days", "Per event", "Not applicable", "No"],
    ]
    if cur:
        ent_rows.insert(6, ["Adoption Leave", f"{p['adoption_weeks']} weeks", "For adopting parent of a child under three months (see 7.7)", "Not applicable", "No"])
        ent_rows.append(["Marriage Leave", f"{p['marriage']} working days", "Once during service, for own marriage", "Not applicable", "No"])
    ent_rows.append(["Compensatory Off", "Earned on approved weekend/holiday work", "Valid for 60 days from the date of work", "No", "No"])
    sections.append(dict(title="Summary of leave entitlements", items=[
        ("p", f"The table below summarises the leave available to a confirmed full-time employee under Version {p['version']} of this policy. Detailed rules follow in the subsequent sections."),
        ("t", ["Leave type", "Entitlement", "Credit / accrual", "Carry forward", "Encashable"], ent_rows, [17, 21, 28, 18, 16]),
    ]))
    sections.append(dict(title="Casual Leave (CL)", items=[
        ("c", f"Casual Leave is meant for short, unforeseen or personal needs. Every employee is entitled to {p['cl']} days of CL in a leave year."),
        ("c", f"CL may be taken for a minimum of half a day. Not more than {cl_consec} consecutive days of CL may be taken at a time (including weekends or holidays counted under the sandwich rule in Section 13)."),
        ("c", "CL cannot be clubbed with Earned Leave to extend a continuous absence beyond the limits in Section 11, except with written approval of the Department Head."),
        ("c", "Unused CL lapses on 31 December. It is not carried forward and is not encashed."),
    ]))
    sections.append(dict(title="Sick Leave (SL)", items=[
        ("c", f"Sick Leave covers illness or injury of the employee, including medical appointments and recovery. Every employee is entitled to {p['sl']} days of SL in a leave year."),
        ("c", "The employee must inform the reporting manager by 10:30 am on the first day of absence (message or call) and apply in the HRMS within two working days of returning."),
        ("c", f"A medical certificate from a registered medical practitioner is mandatory when SL exceeds {cert_days} consecutive days. For absences exceeding 5 consecutive working days, a fitness certificate is required before resuming duty."),
        ("c", "If SL is exhausted, the employee may, with manager approval, use Earned Leave (confirmed employees) or Casual Leave for illness. Beyond that, the absence is treated as Leave Without Pay (Section 10)."),
        ("c", "Unused SL lapses on 31 December. It is not carried forward and is not encashed."),
        ("c", "Medical information submitted under this section is sensitive personal data and is handled in accordance with HR-POL-006 (Data Privacy)."),
    ]))
    sections.append(dict(title="Earned Leave (EL) / Privilege Leave", items=[
        ("c", f"Earned Leave accrues at {p['el_per_month']} days for each completed calendar month of service, giving {p['el_year']} days in a full leave year. An employee who joins on or before the 15th of a month earns EL for that month; an employee who joins after the 15th starts accruing from the next month."),
        ("c", "EL is credited to the balance at the end of every month. Employees on probation accrue EL but may avail it only after confirmation, except with Department Head approval in exceptional cases."),
        ("c", f"Unused EL is carried forward to the next leave year up to a maximum of {p['el_cap']} days. EL above {p['el_cap']} days remaining on 31 December lapses. The cap applies at year-end only; the in-year balance (carry-forward plus accrual) may temporarily exceed {p['el_cap']} days."),
        ("c", "EL cannot be encashed during employment. On separation, the entire unused EL balance is encashed at the rate of Basic salary divided by 26 per day, as part of the full and final settlement (HR-POL-012)."),
        ("c", "A maximum of 15 working days of EL may be taken at a stretch. Longer continuous absence requires the written approval of the Head of Human Resources."),
        ("c", "EL should be planned in advance. Managers may decline or reschedule EL during critical business periods such as financial year-end close, major releases or client go-live freezes, but may not unreasonably withhold EL for more than 60 days in succession."),
    ]))
    spec = [
        ("h", "Maternity Leave"),
        ("c", "Female employees are entitled to maternity leave under the Maternity Benefit Act, 1961, provided they have worked for at least 80 days in the 12 months immediately preceding the expected date of delivery."),
        ("c", "The entitlement is 26 weeks for the first two surviving children (of which up to 8 weeks may be taken before the expected delivery date) and 12 weeks for the third child onwards (up to 6 weeks before delivery). Leave for miscarriage or medical termination of pregnancy is 6 weeks; for tubectomy, 2 weeks; and up to one month for illness arising from pregnancy, delivery or premature birth."),
        ("c", "Maternity leave is paid in full and is counted in calendar days, including intervening weekends and holidays. It does not reduce CL, SL or EL balances, and EL continues to accrue during maternity leave."),
        ("c", "On return, the employee may request a work-from-home arrangement for up to 3 months, subject to the nature of the role and mutual agreement with the manager and HR. The Company operates a crèche arrangement through a tie-up with a partner facility near the Bengaluru office."),
        ("h", "Paternity Leave"),
        ("c", f"A confirmed male employee is entitled to {p['paternity']} working days of paid paternity leave on the birth of a child" + (", which may be availed in up to two blocks within 6 months of the date of birth." if cur else ", to be availed within 3 months of the date of birth, in a single block.")),
        ("h", "Bereavement Leave"),
        ("c", f"On the death of a member of the immediate family, an employee is entitled to {p['bereavement']} working days of paid bereavement leave. For the death of other relatives, the employee may use CL or EL."),
    ]
    if cur:
        spec += [
            ("h", "Adoption Leave"),
            ("c", f"An adopting mother, or a commissioning mother, of a child below three months of age is entitled to {p['adoption_weeks']} weeks of paid adoption leave from the date the child is handed over. An adopting father is entitled to paternity leave under 7.5."),
            ("h", "Marriage Leave"),
            ("c", f"A confirmed employee is entitled to {p['marriage']} consecutive working days of paid marriage leave once during service for their own marriage. The request must be made at least 30 days in advance, and leave must be taken within 60 days of the wedding date. A copy of the invitation or marriage certificate must be submitted to HR."),
        ]
    sections.append(dict(title="Statutory and special leave", items=spec))
    sections.append(dict(title="Public holidays and Floating Holidays", items=[
        ("c", "The Company observes the fixed holidays listed in the annual Holiday Calendar published each December. A fixed holiday that falls on a Saturday or Sunday is not substituted with another day."),
        ("c", f"In addition, every employee may choose {p['floating']} Floating Holiday{'s' if p['floating']>1 else ''} per leave year from the optional list in the Holiday Calendar (for example, regional or religious festivals). Floating Holidays must be applied for in {CO['hrms']} at least 3 working days in advance, are not carried forward and are not encashed."),
        ("c", "Employees who join mid-year are entitled to the full number of Floating Holidays if they join on or before 30 June, and to one Floating Holiday if they join between 1 July and 31 August; thereafter none are available in that year."),
    ]))
    sections.append(dict(title="Compensatory Off", items=[
        ("c", "An employee who is required, with prior written approval of the Department Head, to work on a weekly off or a fixed holiday earns compensatory off: 0.5 day for working at least 4 hours and 1 day for working at least 8 hours."),
        ("c", "Compensatory off must be availed within 60 days from the date of work, failing which it lapses. It cannot be encashed or carried forward. Employees on on-call duty are covered by HR-POL-002 and not by this section."),
    ]))
    sections.append(dict(title="Leave Without Pay (LOP)", items=[
        ("c", "Where an employee has exhausted all eligible leave, or is absent without approval, the days are treated as Leave Without Pay. LOP may also be granted on request for personal reasons, with approval of the Department Head and HR, for up to 30 consecutive days and not more than 90 days in a leave year."),
        ("c", "Salary for LOP days is deducted at the rate of monthly gross salary divided by the number of calendar days in that month. EL, CL and SL do not accrue and Floating Holidays are not reduced during LOP, but LOP of more than 15 days in a year defers the probation or appraisal eligibility date by the number of LOP days."),
    ]))
    sections.append(dict(title="Applying for and approving leave", items=[
        ("c", f"All leave must be applied for through {CO['hrms']}. Verbal approval or approval over chat or email does not substitute for a system application, and leave not recorded in the system is treated as unauthorised absence."),
        ("t", ["Leave duration (working days)", "Minimum advance notice", "Approver(s)"], [
            ["Up to 3 days", "3 working days (CL: 1 working day; SL: inform same day)", "Reporting Manager"],
            ["4 to 10 days", "7 working days", "Reporting Manager (up to 5 days); Reporting Manager and Department Head (6 to 10 days)"],
            ["11 to 15 days", "15 calendar days", "Reporting Manager and Department Head; HR is intimated"],
            ["More than 15 days (non-statutory)", "30 calendar days", "Reporting Manager, Department Head and Head of Human Resources"],
        ], [26, 34, 40]),
        ("c", "Managers should approve or reject a leave application within 2 working days. An application that is neither approved nor rejected within 5 working days is escalated to the Department Head and HR."),
        ("c", "An employee may cancel approved leave before it begins. Leave cancelled after it has begun can be reversed only for the remaining days, with manager approval."),
        ("c", "In emergencies (such as a medical emergency or bereavement) the employee must inform the reporting manager as early as practicable and regularise the application within 2 working days."),
    ]))
    sections.append(dict(title="New joiners, probation, interns and contract employees", items=[
        ("c", "CL and SL for the leave year in which an employee joins are prorated by the number of full months remaining in the year, counting the joining month only if the employee joins on or before the 15th. Fractions are rounded to the nearest whole day."),
        ("c", "EL accrues from the date of joining as set out in Section 6, but can be availed only after confirmation."),
        ("c", "Interns are entitled to 1 day of Casual Leave for every month of internship and to the fixed holidays. Interns are not entitled to EL, SL, Floating Holidays or encashment of any leave."),
        ("c", "Contract employees on Aurelia payroll are entitled to the leave described in this policy unless their contract states otherwise."),
    ]))
    sections.append(dict(title="Sandwich rule and weekends", items=[
        ("c", "Weekly offs and fixed holidays that fall between two days of Casual Leave or Sick Leave are counted as leave (the sandwich rule). For example, CL taken on Friday and the following Monday is counted as 4 days of CL."),
        ("c", "The sandwich rule does not apply to Earned Leave, Floating Holidays, Compensatory Off or statutory and special leave, where only working days are counted; the sole exception is maternity leave, which is counted in calendar days."),
        ("c", "A weekend or holiday immediately before or after a leave period is not counted as leave unless the leave is on both sides of it."),
    ]))
    sections.append(dict(title="Leave during notice period and on separation", items=[
        ("c", "During the notice period, leave other than statutory leave and Sick Leave supported by a medical certificate requires the approval of the Department Head. Any leave taken (including SL and CL) during the notice period extends the last working day by the same number of days, unless the Head of Human Resources decides otherwise in writing."),
        ("c", "Unused EL is encashed on separation as per Section 6. CL, SL, Floating Holidays and Compensatory Off lapse and are not encashed."),
        ("c", "If an employee has taken more EL than accrued at the time of separation, the excess is recovered from the full and final settlement at the rate of Basic salary divided by 26 per day."),
    ]))
    sections.append(dict(title="Unauthorised absence and misuse", items=[
        ("c", "Absence without approval or intimation is unauthorised absence and is treated as LOP. Repeated unauthorised absence is misconduct under the Code of Conduct (HR-POL-004)."),
        ("c", "If an employee is absent for more than 3 consecutive working days without intimation, HR will send a written notice to the registered address and email requiring the employee to report within 48 hours. Failure to respond may be treated as voluntary abandonment of service."),
        ("c", "Submission of false medical certificates or false reasons for leave is a serious misconduct and may result in disciplinary action up to termination."),
    ]))
    sections.append(dict(title="Records, queries and policy review", items=[
        ("c", f"Leave balances and history are available to each employee in {CO['hrms']}. Discrepancies must be reported through {CO['helpdesk']} within 30 days."),
        ("c", f"Queries on this policy may be sent to {CO['hr_mail']}. The Head of Human Resources is the final authority for interpretation."),
        ("c", "The Company may amend this policy from time to time. Amendments are communicated by HR circular and take effect from the date stated in the circular."),
    ]))
    revs = [("1.0", "05 January 2018", "Initial leave policy (financial-year leave cycle).", "HR Team"),
            ("2.0", "02 March 2021", "Introduced Floating Holiday and work-from-home related leave rules.", "HR Team"),
            ("2.1", "20 March 2023", "Annual revision aligning leave year to calendar year; CL 7, SL 7, EL 15.", "Sunita Rao")]
    if cur:
        revs.append(("3.0", "12 December 2025", p["revision_note"], "Sunita Rao"))
    meta = dict(doc_id="HR-POL-001", title="Leave Policy", version=p["version"], effective=p["effective"], owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 December 2026" if cur else "Not applicable (superseded)",
                applies=APPLIES_ALL, status="Current" if cur else "SUPERSEDED - do not use", revisions=revs)
    build_policy(OUTDIR + fname, meta, sections)

# =============================================================== ATTENDANCE
def attendance_policy():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy defines standard working hours, how attendance is recorded, how late arrivals and irregularities are treated, and the allowances that apply to on-call and shift work. It applies to all employees, interns and contract employees."),
        ("c", "Leave-related matters are governed by HR-POL-001 (Leave Policy) and in-office/remote work arrangements by HR-POL-003 (Hybrid Work Policy)."),
    ]))
    s.append(dict(title="Working days and hours", items=[
        ("c", "The standard working week is Monday to Friday. Saturday and Sunday are weekly offs."),
        ("c", "Standard office hours are 9:30 am to 6:30 pm, which includes a one-hour lunch break that may be taken flexibly between 12:30 pm and 2:30 pm. This provides 8 working hours per day and 40 hours per week."),
        ("c", "Core hours are 11:00 am to 4:00 pm on working days. During core hours employees must be available for meetings and collaboration, whether in the office or working remotely."),
        ("c", "Employees in Customer Success, IT & Infrastructure and Sales may follow shift or regional-hours rosters approved by the Department Head and communicated by HR."),
    ]))
    s.append(dict(title="Recording attendance", items=[
        ("c", f"Attendance is recorded through the badge reader at office entrances and through the check-in feature of {CO['hrms']} for days worked remotely. Check-in and check-out are mandatory every working day."),
        ("c", "Attendance data is personal data of the employee and is processed and retained in accordance with HR-POL-006 (Data Privacy). It is accessible to the employee, the reporting manager, HR and Payroll."),
        ("c", "Missed or incorrect punches (for example, a forgotten badge) must be regularised in the HRMS within 3 working days. An employee may regularise a maximum of 3 days in a month on their own; any further regularisation needs a justification approved by the reporting manager."),
    ]))
    s.append(dict(title="Late arrival and late marks", items=[
        ("c", "A grace period of 15 minutes is allowed: check-in up to 9:45 am is treated as on time. Check-in after 9:45 am is recorded as a late mark."),
        ("c", "For every 3 late marks in a calendar month, 0.5 day of Casual Leave is deducted. If CL is exhausted, the deduction is made from Earned Leave (confirmed employees), and if no leave is available, as Leave Without Pay. Late marks reset on the first day of each month."),
        ("c", "Each employee may take up to 2 permissions per month of up to 2 hours each, applied for in the HRMS in advance (or within 1 working day in emergencies). A permission is not a late mark and does not reduce leave."),
        ("c", "Late marks are not recorded where the employee is on approved client travel, in a release or incident war-room, or on a day when the check-in system was unavailable, as confirmed by IT."),
    ]))
    s.append(dict(title="Half-day, short hours and absence", items=[
        ("c", "A half-day leave (first half or second half) counts as 0.5 day and must be applied for in the HRMS. An employee who works fewer than 4.5 hours in a day without applying for leave is treated as absent for the full day."),
        ("c", "A day on which an employee works 4.5 hours or more but less than 8 hours without approved leave or permission is recorded as a short-hours day. If an employee has more than 3 short-hours days in a month, the reporting manager will discuss it with the employee; repeated short hours may be treated as a performance matter."),
        ("c", "Absence without approval or intimation is dealt with under Section 15 of the Leave Policy."),
    ]))
    s.append(dict(title="Overtime, weekend work and on-call duty", items=[
        ("c", "All employees at grades L1 to L6 are treated as exempt from overtime pay. Work on weekly offs or fixed holidays must be approved in advance by the Department Head and is compensated through Compensatory Off under the Leave Policy."),
        ("c", "Employees in IT & Infrastructure, Customer Success and Engineering who are rostered for on-call duty receive an on-call allowance of \u20b91,500 per week of rostered duty, paid with the next month's salary. If an on-call employee is required to work an incident for more than 2 hours between 10:00 pm and 6:00 am, they receive a compensatory half day off the following working day."),
        ("c", "Employees who work a night shift (a shift that includes the period from 10:00 pm to 6:00 am) on a roster approved by HR receive a night-shift allowance of \u20b9400 per night."),
    ]))
    s.append(dict(title="Safe transport", items=[
        ("c", "Employees who are required to remain in the office after 8:00 pm are eligible for a company-arranged cab drop on request, booked through the Administration desk by 6:00 pm."),
        ("c", "For women employees travelling between 8:00 pm and 6:00 am, company-arranged transport is mandatory, and the Company will follow the safety requirements of the respective state authorities for the office location."),
    ]))
    s.append(dict(title="Payroll cut-off", items=[
        ("c", "Attendance and leave inputs for a month are frozen on the 25th of that month. Corrections after the cut-off are processed in the next month's payroll."),
        ("c", "Salary is credited on the last working day of each month."),
    ]))
    meta = dict(doc_id="HR-POL-002", title="Attendance and Working Hours Policy", version="2.2", effective="01 January 2026", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 December 2026", applies=APPLIES_ALL, revisions=[
                    ("1.0", "01 June 2018", "Initial policy.", "HR Team"),
                    ("2.0", "15 January 2021", "Introduced grace period and late-mark rules.", "HR Team"),
                    ("2.2", "12 December 2025", "Updated on-call and night-shift allowances; added permission rules.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-002_Attendance_and_Working_Hours_Policy_v2.2.pdf", meta, s)

# =============================================================== HYBRID WORK
def hybrid_policy():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "Aurelia Systems follows a hybrid model that combines in-person collaboration with the flexibility to work remotely. This policy sets out the minimum office presence, the rules for working from home and from other locations, and the allowances available for remote work."),
        ("c", "This policy applies to all employees whose role is classified as hybrid-eligible. Roles that require physical presence (for example, Administration, hardware support and facilities) are exempt and follow the schedule set by their Department Head."),
    ]))
    s.append(dict(title="Hybrid schedule", items=[
        ("c", "With effect from 1 July 2026, all hybrid-eligible employees must work from their assigned office for a minimum of 3 days per week. Tuesday, Wednesday and Thursday are anchor days on which all employees are expected to be in the office."),
        ("c", "Employees who are on probation and interns must be in the office for a minimum of 4 days per week (Tuesday to Thursday plus one more day agreed with the manager) so that they can learn through in-person mentoring."),
        ("c", "On Mondays and Fridays employees may work from home without separate approval. Department Heads may specify different anchor days for a team (for example, because of a client schedule) by informing HR in writing."),
        ("c", "Public holidays and approved leave during the week reduce the minimum in-office days on a pro-rata basis (for example, a week with one fixed holiday on an anchor day requires 2 in-office days)."),
    ]))
    s.append(dict(title="Ad-hoc work from home", items=[
        ("c", "An employee may work from home on an anchor day for genuine reasons such as illness, a home emergency or a utility outage, by informing the reporting manager before 9:30 am. Such ad-hoc work from home is limited to 6 days per quarter."),
        ("c", "Work from home is not a substitute for leave. An employee who is unwell and unable to work must apply for Sick Leave."),
    ]))
    s.append(dict(title="Fully remote and work-from-anywhere arrangements", items=[
        ("c", "A fully remote arrangement is available only for roles approved in advance by the Department Head and the Head of Human Resources. It is reviewed every 6 months."),
        ("c", "Work from Anywhere (WFA): an employee may work from a location in India other than their assigned office for up to 15 working days in a leave year, with at least 5 working days' notice, manager approval, and a stable internet connection and a secure workspace. WFA days count as work-from-home days."),
        ("c", "Working from outside India is not permitted without the written approval of the Head of Human Resources, the Head of Finance and the CISO, because of tax, permanent-establishment, immigration and data-security implications. Employees who work from abroad without approval may face disciplinary action."),
    ]))
    s.append(dict(title="Equipment and allowances", items=[
        ("c", f"The Company provides a laptop and standard accessories to every employee. Employees who work from home on a regular schedule may claim an internet reimbursement of up to {inr(INTERNET_ALLOW)} per month against a bill in the employee's or a family member's name, submitted through {CO['hrms']} within 30 days of the bill date."),
        ("c", f"Confirmed employees may claim a one-time ergonomic allowance of up to {inr(ERGO_ALLOW)} (for a chair, desk or monitor stand) once every 3 years, against original invoices."),
        ("c", f"Employees at grade L3 and above are entitled to a mobile reimbursement of up to {inr(MOBILE_ALLOW)} per month against the bill."),
        ("c", "Electricity charges, furniture rent and home-office rent are not reimbursed."),
    ]))
    s.append(dict(title="Expectations of remote working", items=[
        ("b", ["Be available and responsive on chat and video during core hours (11:00 am to 4:00 pm).",
               "Use a company-managed laptop on the corporate VPN and follow HR-POL-007 (Information Security and Acceptable Use Policy).",
               "Keep your calendar accurate and attend team meetings with video on unless bandwidth is a problem.",
               "Work from a safe and private workspace. Confidential calls must not be taken in public places.",
               "Report any injury sustained while working from home during working hours to HR within 48 hours."]),
    ]))
    s.append(dict(title="Monitoring and non-compliance", items=[
        ("c", "In-office presence is tracked through badge swipes and attendance check-ins. This data is used only for attendance, space planning and policy compliance, as described in HR-POL-006."),
        ("c", "If an employee does not meet the in-office requirement on more than 3 occasions in a quarter without approval, the manager will counsel the employee. Continued non-compliance will be reflected in the performance review under the Values and Collaboration competencies, and may lead to disciplinary action."),
    ]))
    meta = dict(doc_id="HR-POL-003", title="Hybrid Work Policy", version="2.0", effective="01 July 2026", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="30 June 2027", applies=APPLIES_ALL, revisions=[
                    ("1.0", "10 January 2022", "Initial hybrid policy: minimum 2 days in office.", "HR Team"),
                    ("1.1", "01 April 2024", "Added Work from Anywhere (15 days) and ergonomic allowance.", "HR Team"),
                    ("2.0", "12 June 2026", "Minimum in-office days raised from 2 to 3 per week; Tue-Thu anchor days; 4 days for probationers and interns.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-003_Hybrid_Work_Policy_v2.0.pdf", meta, s)

if __name__ == "__main__":
    leave_policy(LEAVE_V3, "HR-POL-001_Leave_Policy_v3.0_CURRENT.pdf")
    leave_policy(LEAVE_V21, "ARCHIVE_HR-POL-001_Leave_Policy_v2.1_SUPERSEDED.pdf")
    attendance_policy()
    hybrid_policy()
    print("ok")
