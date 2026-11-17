from hrlib import *
from config import *
from docs_a import OUTDIR, APPLIES_ALL

def travel():
    g = GRADES
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy governs business travel and reimbursable expenses so that employees travel comfortably and economically and are reimbursed promptly. It applies to all employees travelling or incurring expenses on Company business."),
        ("c", "Employees are expected to spend Company money as carefully as their own. Where this policy is silent, the test is whether the expense is necessary, reasonable and supported by a bill."),
    ]))
    s.append(dict(title="Approval and booking", items=[
        ("c", f"All business travel must be approved in advance in {CO['hrms']} by the reporting manager. Where the estimated trip cost exceeds \u20b950,000, the Department Head must also approve. International travel needs the approval of the Department Head and the Head of Finance."),
        ("c", "Flights and hotels must be booked through the Company travel desk (Administration) at least 7 days in advance wherever possible, choosing the lowest logical fare. Last-minute bookings require a reason."),
        ("c", "Travel advances of up to 80% of the estimated cost may be requested for trips of 3 days or more. Advances must be settled within 7 working days of return, failing which the advance is recovered from salary."),
    ]))
    s.append(dict(title="Modes of travel", items=[
        ("t", ["Mode", "L1 to L3", "L4 to L5", "L6"], [
            ["Domestic flight", "Economy", "Economy", "Economy (business class for flights over 3 hours with CEO approval)"],
            ["International flight", "Economy", "Economy", "Business class for flights over 6 hours"],
            ["Train", "AC 3-Tier", "AC 2-Tier", "AC First Class / Executive Chair Car"],
            ["Local travel", "Auto, metro, bus or app-based cab for client visits", "App-based cab", "App-based cab"],
        ], [20, 26, 22, 32]),
        ("c", "Use of a personal car for approved official travel is reimbursed at \u20b910 per km, and a personal two-wheeler at \u20b94 per km, supported by a log of dates, distance and purpose. Fuel or parking is not claimed separately when mileage is claimed."),
        ("c", "Commuting between home and the regular place of work is not reimbursable."),
    ]))
    s.append(dict(title="Hotel and meals", items=[
        ("p", "Hotel accommodation and meal allowances are capped by grade. Metro cities for this purpose are Bengaluru, Mumbai, Delhi NCR, Chennai, Hyderabad, Pune and Kolkata. All other locations are non-metro."),
        ("t", ["Grade", "Hotel per night - metro", "Hotel per night - non-metro", "Meal per diem (per day of travel)"],
         [[k, inr(v[2]), inr(v[3]), inr(v[4])] for k, v in g.items()], [14, 28, 30, 28]),
        ("c", "Hotel limits include taxes, and are per night for a single occupancy room. If the hotel tariff exceeds the limit, the excess is borne by the employee. Exceptions need prior approval of the Department Head, for example during major events when rooms are not available within the limit."),
        ("c", "The meal per diem applies to each day of overnight travel, supported by bills, and does not cover alcohol. Meals provided by the host or included in the hotel tariff are deducted."),
    ]))
    s.append(dict(title="Other reimbursable expenses", items=[
        ("t", ["Expense", "Eligibility and limit", "Documents"], [
            ["Internet bill (hybrid employees)", f"{inr(INTERNET_ALLOW)} per month", "Bill, submitted within 30 days"],
            ["Mobile bill", f"{inr(MOBILE_ALLOW)} per month, L3 and above only", "Bill"],
            ["Ergonomic allowance", f"{inr(ERGO_ALLOW)} once every 3 years, confirmed employees", "Original invoice"],
            ["Client entertainment", "Up to \u20b92,500 per person per meal, with prior manager approval", "Bill; names of guests and purpose"],
            ["Learning and certification", f"Up to {inr(LEARNING_BUDGET)} per employee per leave year with manager pre-approval", "Receipt, proof of completion"],
            ["Local conveyance on business trips", "Actual, for autos, metro, cabs", "Bills for \u20b9500 and above; app screenshot or self-certification for smaller amounts"],
        ], [24, 46, 30]),
        ("c", f"Courses or certifications costing more than {inr(LEARNING_BUDGET)} require approval of the Department Head and the employee must remain in service for 12 months after completion; otherwise the amount is recovered pro-rata from the full and final settlement."),
        ("c", "The following are not reimbursed: alcohol, fines and penalties, personal items, entertainment unrelated to the trip, travel of family members, hotel mini-bar and laundry (unless the trip exceeds 5 nights), and lost cash."),
    ]))
    s.append(dict(title="Submitting claims", items=[
        ("c", f"Claims must be submitted in {CO['hrms']} under My Claims within 30 days from the date of the expense, or from the date of return in the case of trips. Claims submitted after 30 days will be rejected."),
        ("c", "Original bills or e-invoices are mandatory for each expense of \u20b9500 or above. For smaller expenses, a self-declaration is accepted up to \u20b92,000 per month."),
        ("c", "The reporting manager must approve or reject a claim within 5 working days. Finance validates the claim and releases payment within 20 days of submission of a complete claim, with the next payroll."),
        ("c", "False claims, altered bills or claims for personal expenses constitute serious misconduct under HR-POL-004 and may lead to dismissal and recovery of the amount."),
    ]))
    meta = dict(doc_id="HR-POL-009", title="Travel and Expense Reimbursement Policy", version="3.0", effective="01 April 2026", owner="Rajesh Kulkarni, Head of Finance",
                approver="Arvind Menon, Chief Executive Officer", review="31 March 2027", applies=APPLIES_ALL, queries="finance@aurelia-sys.example", revisions=[
                    ("1.0", "01 June 2017", "Initial policy.", "Finance"),
                    ("2.0", "01 April 2022", "Introduced grade-wise hotel and meal limits.", "Finance"),
                    ("3.0", "15 March 2026", "Revised hotel limits; added learning budget, ergonomic and internet allowances; 30-day claim rule.", "Rajesh Kulkarni")])
    build_policy(OUTDIR + "HR-POL-009_Travel_and_Expense_Policy_v3.0.pdf", meta, s)

def appraisal():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "The Performance Management process helps every employee understand what is expected of them, receive regular feedback, be recognised for results and grow. It also provides the basis for decisions on increments, variable pay, promotions and development."),
        ("c", "This policy applies to all confirmed full-time employees. Employees on probation are assessed under HR-POL-013. Interns are not covered by this process, and contract employees are covered only if their contract states so."),
        ("c", "The performance cycle follows the financial year, from 1 April to 31 March."),
    ]))
    s.append(dict(title="Performance cycle and calendar", items=[
        ("t", ["Activity", "Timeline", "Owner"], [
            ["Goal setting (3 to 5 goals agreed with the manager)", "1 April to 30 April", "Employee and manager"],
            ["Mid-year check-in (feedback conversation; no rating)", "October", "Employee and manager"],
            ["Self-review", "1 April to 10 April (following year-end)", "Employee"],
            ["Manager review and proposed rating", "11 April to 20 April", "Reporting manager"],
            ["Calibration of ratings", "21 April to 30 April", "Department Heads and HR"],
            ["Final approvals (CEO for rating 5 and promotions)", "1 May to 7 May", "Head of HR, CEO"],
            ["Communication of rating and increment letters", "8 May to 15 May", "Manager and HR"],
            ["Increments effective from", "1 April (arrears paid with May salary)", "Payroll"],
            ["Annual performance bonus paid", "With June salary", "Payroll"],
        ], [48, 30, 22]),
    ]))
    s.append(dict(title="Goals and assessment framework", items=[
        ("c", "Each employee sets 3 to 5 goals (OKR format) with measurable outcomes, agreed with the reporting manager within 30 days of the start of the cycle, and records them in the HRMS. Goals may be revised at the mid-year check-in if business priorities change."),
        ("c", "Performance is assessed on two components: Goals (weight 70%) and Values and Competencies (weight 30%)."),
        ("c", "The competencies assessed are: Delivery and Quality; Ownership; Collaboration; Learning and Growth; and, for grades L4 and above, Leadership and People Development."),
        ("c", "The weighted score is an input to the calibration process. The final rating is decided at calibration and may differ from the score, after considering the difficulty of goals, the context and comparison across peers."),
    ]))
    s.append(dict(title="Rating scale", items=[
        ("t", ["Rating", "Label", "Meaning", "Guideline distribution"], [
            [str(k), RATINGS[k], m, DISTRIBUTION[k]] for k, m in [
                (5, "Consistently far above expectations; exceptional impact beyond role"),
                (4, "Frequently exceeds expectations; strong, reliable contributor"),
                (3, "Fully meets expectations of the role and grade"),
                (2, "Meets some expectations but with notable gaps; improvement required"),
                (1, "Does not meet expectations; significant improvement required")]
        ], [11, 25, 42, 22]),
        ("c", "The distribution is a guideline used in calibration to ensure fairness across teams. It is not a forced ranking, and a team may have a different distribution with justification."),
        ("c", "A rating of 5 requires written justification and approval of the CEO."),
    ]))
    s.append(dict(title="Increments, bonus and promotions", items=[
        ("t", ["Final rating", "Merit increment band", "Individual bonus multiplier"],
         [[f"{k} - {RATINGS[k]}", f"{INCREMENT_BANDS[k][0]}% to {INCREMENT_BANDS[k][1]}%" if INCREMENT_BANDS[k][1] else "0%", f"{BONUS_MULT[k]}%"] for k in (5, 4, 3, 2, 1)], [40, 30, 30]),
        ("c", "The exact increment within a band depends on the employee's position in the pay range for the grade, criticality of the role and the increment budget approved by the Board for the year."),
        ("c", "Eligibility for the cycle depends on the date of joining: employees who joined on or before 30 September of the cycle year are eligible for the full increment; those who joined between 1 October and 31 December are eligible for 50% of the increment applicable to their rating (pro-rata); those who joined after 31 December are not eligible and are reviewed in the next cycle."),
        ("c", "Employees who have resigned or are serving notice period on 31 March, or who are on a Performance Improvement Plan on that date, are not eligible for an increment or bonus for that cycle."),
        ("c", "Annual performance bonus = Variable pay target x Company performance factor x Individual bonus multiplier. The variable pay target is a percentage of Fixed CTC by grade as per HR-POL-011. The Company performance factor is declared by the Board after the financial results (95% for FY2024-25; 105% for FY2025-26). Employees with a rating of 1 receive no bonus. Example: an L3 employee with Fixed CTC of \u20b914,00,000 (target 10% = \u20b91,40,000), rating 4 (multiplier 120%) and a Company factor of 105% receives \u20b91,40,000 x 1.05 x 1.20 = \u20b91,76,400."),
        ("c", "Bonus is paid only to employees who are in service and not serving notice on the date of payment (with June salary)."),
        ("c", "Promotion requires: a rating of 4 or 5 in the latest cycle and at least 3 in the previous one; a minimum of 18 months in the current grade; demonstration of the competencies of the next grade; and a business need for the role. Promotions are approved by the Department Head and HR, and by the CEO for promotions to L4 and above. A promotion increment of 8% to 12% is given in addition to the merit increment, subject to the pay range of the new grade."),
        ("c", "Out-of-cycle promotions may be approved by the CEO in exceptional cases."),
    ]))
    s.append(dict(title="Performance Improvement Plan (PIP)", items=[
        ("c", "An employee rated 1, or whose performance has been below expectations for two consecutive quarters, may be placed on a Performance Improvement Plan of 60 days, extendable once by up to 30 days."),
        ("c", "The PIP document states the gaps, specific measurable improvement goals, the support available, and weekly check-ins with the manager. HR is present at the start and the end of the PIP."),
        ("c", "Outcomes: (a) successful completion, after which the employee returns to the normal process; (b) extension; or (c) unsuccessful, which may lead to separation with notice as per HR-POL-012. During the PIP the employee is not eligible for increments, promotion or bonus."),
    ]))
    s.append(dict(title="Appeals", items=[
        ("c", "An employee who disagrees with the final rating may appeal in writing to the HR Business Partner within 10 working days of the communication of the rating, stating the reasons and evidence."),
        ("c", "A Review Panel consisting of the Head of Human Resources and a Department Head from another function will review the appeal and decide within 15 working days. The decision of the panel is final."),
    ]))
    s.append(dict(title="Records and confidentiality", items=[
        ("c", "Appraisal records are confidential and accessible only to the employee, the reporting chain, HR and the Review Panel, and are retained as set out in HR-POL-006."),
        ("c", "Managers must give timely feedback during the year. No rating should come as a surprise at the year-end review."),
    ]))
    meta = dict(doc_id="HR-POL-010", title="Performance Appraisal Policy", version="4.0", effective="01 April 2025", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 March 2027", applies="All confirmed full-time employees", revisions=[
                    ("1.0", "01 April 2017", "Initial appraisal process.", "HR Team"),
                    ("3.0", "01 April 2022", "Introduced OKRs and calibration.", "HR Team"),
                    ("4.0", "20 March 2025", "Added company performance factor in bonus; pro-rata eligibility for Oct-Dec joiners; 18-month promotion rule.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-010_Performance_Appraisal_Policy_v4.0.pdf", meta, s)

def compben():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy describes how pay is structured at Aurelia Systems and the benefits available to employees. It should be read together with the offer letter, the appointment letter and the annexure of salary breakup issued to each employee.")]))
    s.append(dict(title="Salary structure", items=[
        ("c", "Total annual compensation (CTC) consists of Fixed CTC and a Variable pay target. Variable pay target is expressed as a percentage of Fixed CTC and depends on the grade."),
        ("t", ["Component", "How it is determined"], [
            ["Basic salary", "40% of Fixed CTC"],
            ["House Rent Allowance (HRA)", "50% of Basic salary (all locations)"],
            ["Special Allowance", "Balancing component after all other fixed components"],
            ["Employer PF contribution", "12% of PF wages, with PF wages capped at the statutory ceiling of \u20b915,000 per month, i.e. \u20b91,800 per month"],
            ["Gratuity provision", "4.81% of annual Basic salary (part of Fixed CTC; paid as per the law)"],
            ["Variable pay (target)", "A percentage of Fixed CTC by grade, paid as annual performance bonus (see HR-POL-010)"],
        ], [30, 70]),
        ("t", ["Grade", "Band", "Variable pay target (% of Fixed CTC)"], [[k, v[0], f"{v[1]}%" if v[1] else "Nil"] for k, v in GRADES.items()], [14, 52, 34]),
        ("c", "Monthly gross salary is the sum of Basic, HRA and Special Allowance. Employer PF and gratuity are part of CTC but are not paid in the monthly salary."),
        ("c", "Interns receive a fixed monthly stipend and are not covered by the structure above."),
    ]))
    s.append(dict(title="Salary payment and deductions", items=[
        ("c", f"Salary is credited to the employee's bank account on the last working day of each month. Payslips are available in {CO['hrms']}. Attendance and leave inputs are frozen on the 25th of the month."),
        ("c", "The following are deducted from monthly salary: employee PF contribution of 12% of PF wages (\u20b91,800 per month); professional tax of \u20b9200 per month; income tax deducted at source (TDS) as per the employee's tax regime declaration; and recoveries such as loss-of-pay days, advances and any amounts due to the Company."),
        ("c", "The new tax regime applies by default. An employee who wishes to opt for the old tax regime must declare it in the HRMS by 30 April and submit proofs of investments by 15 January. Form 16 is issued by 15 June."),
        ("c", "New joiners are paid from the date of joining, and the salary for a part month is calculated on the basis of calendar days in that month."),
        ("c", "Salary details are confidential. Employees must not disclose their own salary to others in the Company, and must not access others' salary information. Salary information is shared only with those who need it for their role."),
    ]))
    s.append(dict(title="Annual increment and bonus", items=[
        ("c", "Increments and annual performance bonus are determined through the appraisal process described in HR-POL-010. Increments take effect from 1 April and bonus is paid with June salary, subject to the eligibility conditions in that policy."),
    ]))
    s.append(dict(title="Provident fund and gratuity", items=[
        ("c", "All eligible employees are enrolled in the Employees' Provident Fund. The employee and the Company each contribute 12% of PF wages as defined in Section 2. Employees must provide their UAN at joining. On leaving, the PF account is transferred through the UAN."),
        ("c", "Gratuity is payable to an employee who has completed five years of continuous service, on resignation, retirement, death or disablement, as per the applicable gratuity law. The amount is 15 days' last drawn Basic salary for each completed year of service (calculated as Basic x 15 / 26 x years of service), subject to the statutory ceiling of \u20b920,00,000. In the case of death or disablement, the five-year condition does not apply."),
    ]))
    s.append(dict(title="Insurance and health benefits", items=[
        ("c", "Group health insurance of \u20b95,00,000 on a family floater basis covers the employee, spouse and up to two dependent children from the date of joining. The premium is paid by the Company. Pre-existing conditions are covered from day one and maternity expenses are covered up to \u20b950,000 for normal delivery and \u20b975,000 for caesarean delivery after a waiting period of 9 months."),
        ("c", "Parents or parents-in-law may be added at the employee's cost through a group top-up, with the premium deducted from salary in equal instalments. Enrolment is open within 30 days of joining and during the annual window in December."),
        ("c", "Group personal accident insurance of \u20b910,00,000 and group term life insurance equal to 3 times annual Fixed CTC (maximum \u20b91 crore) are provided to all confirmed employees at no cost."),
        ("c", "A confidential Employee Assistance Programme provides free counselling to employees and their immediate family, up to 6 sessions per person per year."),
        ("c", "Interns are not covered under the group health insurance. Contract employees are covered if stated in their contract."),
    ]))
    s.append(dict(title="Other benefits and allowances", items=[
        ("c", f"Learning budget: each employee may be reimbursed up to {inr(LEARNING_BUDGET)} per leave year for approved courses and certifications, subject to HR-POL-009."),
        ("c", "Employee referral bonus: \u20b925,000 for referring a candidate who is hired in grades L1 to L3, and \u20b950,000 for L4 and above. It is paid with the salary after the referred employee completes 6 months of service, if the referrer is still in service. HR employees and the hiring manager are not eligible for referral bonus for the role."),
        ("c", "Salary advance: a confirmed employee may request one salary advance of up to one month's net pay in a leave year for an emergency, recovered in 3 equal monthly instalments. An advance is not available during the notice period."),
        ("c", "Service awards are given at 3, 5 and 10 years of service, and spot awards may be given by managers up to \u20b95,000 per award."),
        ("c", "Allowances for hybrid work (internet, mobile, ergonomic) are described in HR-POL-003 and for on-call and night shifts in HR-POL-002."),
    ]))
    meta = dict(doc_id="HR-POL-011", title="Compensation and Benefits Policy", version="2.4", effective="01 April 2026", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 March 2027", applies=APPLIES_ALL, revisions=[
                    ("1.0", "01 June 2017", "Initial policy.", "HR Team"),
                    ("2.0", "01 April 2021", "Introduced Fixed and Variable structure and group top-up.", "HR Team"),
                    ("2.4", "15 March 2026", "Increased insurance cover to \u20b95,00,000; revised referral bonus; added EAP.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-011_Compensation_and_Benefits_Policy_v2.4.pdf", meta, s)

def exit_policy():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy explains how employment ends at Aurelia Systems: resignation, termination, retirement and other separations, notice periods, handover, clearance and the full and final settlement. It applies to all employees.")]))
    s.append(dict(title="Resignation and notice period", items=[
        ("c", f"An employee who wishes to resign must submit a written resignation through {CO['hrms']} (or by email to the reporting manager and HR). HR will acknowledge it and the reporting manager and HR will hold a discussion within 5 working days. Resignation is accepted by the Department Head and HR within 5 working days."),
        ("t", ["Employee category", "Notice period"], [
            ["Employees on probation", "30 days"],
            ["Confirmed employees at grades L1 to L3", "60 days"],
            ["Confirmed employees at grades L4 to L6", "90 days"],
            ["Contract employees", "As per contract"],
            ["Interns", "No notice required; 7 days' intimation requested"],
        ], [60, 40]),
        ("c", "The notice period is counted in calendar days from the date of acceptance of the resignation (or the date of submission, if accepted without a different date)."),
        ("c", "The same notice period applies to the Company if it terminates the services of a confirmed employee without cause. The Company may pay salary in lieu of notice for all or part of the period."),
        ("c", "Leave during the notice period is governed by Section 14 of the Leave Policy (HR-POL-001): leave extends the last working day by the same number of days, unless HR decides otherwise in writing."),
    ]))
    s.append(dict(title="Notice shortfall and buyout", items=[
        ("c", "An employee may request early release. The Department Head and HR may approve it depending on project and handover status. If approved, the employee pays the Company for the shortfall (buyout) at the rate of monthly gross salary divided by 30, multiplied by the number of days of shortfall, which is recovered from the full and final settlement."),
        ("c", "The Company may waive the notice period fully or partly without any payment by the employee."),
        ("c", "If an employee leaves without serving the notice period and without approval, the shortfall is recovered as above, and the Company may withhold the relieving and experience letters until it is settled. Such an exit is marked 'Not eligible for rehire' unless HR decides otherwise."),
    ]))
    s.append(dict(title="Handover, clearance and exit interview", items=[
        ("c", "The employee must prepare a handover plan with the manager within 5 working days of resignation and complete knowledge transfer before the last working day."),
        ("c", "On or before the last working day, the employee must return all Company assets (laptop, ID card, access card, accessories, documents), and obtain No-Dues clearance from IT, Administration, Finance, the reporting manager and HR through the HRMS. System access is disabled at the end of the last working day."),
        ("c", "An exit interview is held by HR. Feedback is confidential and used only for improving the organisation."),
    ]))
    s.append(dict(title="Full and final settlement (FnF)", items=[
        ("c", "The Company settles all dues within 45 days of the last working day, subject to clearance."),
        ("t", ["Component", "Treatment"], [
            ["Salary up to the last working day", "Paid (LOP days deducted)"],
            ["Earned Leave balance", "Encashed at Basic / 26 per day (see HR-POL-001)"],
            ["CL, SL, Floating Holidays, Comp Off", "Lapse; not encashed"],
            ["Annual performance bonus", "Not payable if the employee is not in service on the payment date"],
            ["Gratuity", "Paid if the employee has completed 5 years of continuous service"],
            ["Reimbursements", "Valid, approved claims are paid; claims must be submitted before the last working day"],
            ["Recoveries", "Notice shortfall, excess leave taken, unsettled advances or loans, unreturned assets, learning cost recovery"],
        ], [36, 64]),
        ("c", "A statement of FnF is shared with the employee in the HRMS. Tax on FnF is deducted as per law."),
        ("c", "The employee's PF account is transferred to the next employer through the UAN. Form 16 is issued in the normal cycle."),
    ]))
    s.append(dict(title="Relieving and experience letters", items=[
        ("c", "A relieving letter is issued after clearance, on or within 7 working days of the last working day. An experience letter confirming designation and tenure is issued with it."),
        ("c", "Employment verification requests from future employers or background-check agencies are answered by HR on confirmation of the former employee's consent, and confirm only designation, dates of service and (if asked and consented) last drawn CTC."),
    ]))
    s.append(dict(title="Termination, retirement and other separations", items=[
        ("c", "The Company may terminate an employee for misconduct after following the process in HR-POL-004. Termination for misconduct does not require notice or payment in lieu."),
        ("c", "Termination for unsatisfactory performance follows the PIP process in HR-POL-010 and the notice period applicable to the employee."),
        ("c", "The retirement age is 60 years. Employees may be retained on contract beyond this age by mutual agreement."),
        ("c", "In the case of death in service, the Company pays the full and final settlement, gratuity and group insurance benefits to the nominee or legal heir, and the nominee may continue to be covered under group health insurance for 3 months after the date of death."),
        ("c", "Employees who have left in good standing, with a rating of 3 or better in the last cycle and who have served their notice period, are eligible for rehire after a cooling-off period of 3 months."),
    ]))
    meta = dict(doc_id="HR-POL-012", title="Separation and Exit Policy", version="2.1", effective="01 January 2025", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 December 2026", applies=APPLIES_ALL, revisions=[
                    ("1.0", "01 June 2017", "Initial policy.", "HR Team"),
                    ("2.0", "10 March 2022", "Notice period linked to grade; introduced buyout.", "HR Team"),
                    ("2.1", "10 December 2024", "FnF timeline set at 45 days; rehire rules added.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-012_Separation_and_Exit_Policy_v2.1.pdf", meta, s)

def onboarding():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy covers the process from the issue of an offer letter to confirmation of employment, including onboarding formalities, induction and the probation period. It applies to all new full-time employees; interns follow a shorter programme run by their departments.")]))
    s.append(dict(title="Offer and pre-joining", items=[
        ("c", "The offer letter states the designation, grade, location, CTC and joining date, and is valid for 7 days from the date of issue. The offer is conditional on satisfactory background verification, reference checks and submission of the documents listed below."),
        ("t", ["Document", "Details"], [
            ["Identity and address proof", "PAN (mandatory), Aadhaar (masked copy) or passport, and current address proof"],
            ["Education certificates", "Highest qualification and all degrees listed in the CV"],
            ["Previous employment", "Relieving letter, experience letters, last 3 months' payslips and Form 16 of the previous employer"],
            ["Bank details", "Cancelled cheque or bank statement"],
            ["Statutory details", "UAN (if existing), PF nomination, gratuity nomination"],
            ["Photographs and declarations", "Passport-size photograph; declarations on conflicts of interest and confidentiality"],
        ], [30, 70]),
        ("c", f"Personal data collected during onboarding is processed as set out in HR-POL-006. Copies of government IDs are stored encrypted and access is limited to HR."),
        ("c", "Background verification covers education, previous employment and criminal records, and is carried out by an agency with the candidate's written consent. An adverse finding may lead to withdrawal of the offer or termination."),
    ]))
    s.append(dict(title="First week and induction", items=[
        ("c", "HR conducts a welcome session on the first working day covering policies, the HRMS, benefits and insurance enrolment. IT issues the laptop and access on the day of joining."),
        ("c", "Each new joiner is assigned a buddy for the first 90 days. The reporting manager shares a 30-60-90-day plan within the first week."),
        ("c", "New joiners must complete the mandatory e-learning modules on Code of Conduct, POSH, Information Security and Data Privacy within 30 days of joining."),
        ("c", "Group health insurance is effective from the date of joining. The employee must submit dependants' details within 30 days."),
    ]))
    s.append(dict(title="Probation", items=[
        ("c", "All new employees are on probation for 6 months from the date of joining. The probation period may be extended by up to 3 months, in writing, if performance or conduct requires it."),
        ("c", "During probation: the notice period is 30 days on either side; Earned Leave accrues but can be used only after confirmation (see HR-POL-001); the minimum in-office requirement is 4 days per week (HR-POL-003); and the employee is assessed through the probation reviews. An employee who is confirmed before the annual review is included in that cycle, subject to the eligibility rules in HR-POL-010."),
        ("c", "Probation reviews are held at the end of month 3 and month 5. The manager records feedback in the HRMS, discusses it with the employee, and recommends confirmation, extension or discontinuation to HR."),
        ("c", "Confirmation is communicated by a confirmation letter, effective from the date stated, normally the day after completion of the probation. If no letter is issued, the employee is not deemed confirmed; the employee should contact HR if the letter is not received within 15 days of the end of probation."),
        ("c", "LOP of more than 15 days during probation extends the probation by the number of LOP days."),
    ]))
    s.append(dict(title="Transfers and changes after joining", items=[
        ("c", "The Company may transfer an employee to another office or department based on business needs, with reasonable notice, which is normally 30 days. Relocation assistance for permanent transfers is determined case by case by HR."),
        ("c", "Changes in personal details, bank details, address and nominations must be updated in the HRMS within 15 days."),
    ]))
    meta = dict(doc_id="HR-POL-013", title="Onboarding and Probation Policy", version="1.4", effective="01 January 2026", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 December 2026", applies="All new full-time employees", revisions=[
                    ("1.0", "01 June 2018", "Initial policy.", "HR Team"),
                    ("1.3", "10 January 2024", "Added buddy programme and 30-60-90 plan.", "HR Team"),
                    ("1.4", "12 December 2025", "Updated mandatory e-learning timelines; clarified probation LOP rule.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-013_Onboarding_and_Probation_Policy_v1.4.pdf", meta, s)

if __name__ == "__main__":
    travel(); appraisal(); compben(); exit_policy(); onboarding(); print("ok")
