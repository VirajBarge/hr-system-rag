import pandas as pd, datetime as dt
from config import *
B="/mnt/user-data/outputs/hr_rag_data/data/"
e=pd.read_csv(B+"employees.csv"); bal=pd.read_csv(B+"leave_balances_2026.csv"); lv=pd.read_csv(B+"leave_requests_2026.csv")
ap=pd.read_csv(B+"appraisals.csv"); sal=pd.read_csv(B+"salary_structure.csv"); cl=pd.read_csv(B+"reimbursement_claims_2026.csv")
rows=[]
def q(cat, question, answer, source, diff="easy"): rows.append(dict(category=cat, question=question, expected_answer=answer, source=source, difficulty=diff))
P="HR-POL-"
# single-fact policy
q("policy_lookup","How many casual leaves do employees get per year?","8 days per leave year (v3.0, effective 1 Jan 2026), credited on 1 January, lapse on 31 December.",P+"001 v3.0")
q("policy_lookup","What is the maximum number of Earned Leave days that can be carried forward?","30 days; EL above 30 days remaining on 31 December lapses.",P+"001 v3.0")
q("policy_lookup","After how many consecutive sick leave days is a medical certificate needed?","More than 2 consecutive days (v3.0).",P+"001 v3.0")
q("policy_lookup","What is the grace period for late arrival and what happens after 3 late marks?","15 minutes (check-in up to 9:45 am); every 3 late marks in a month deduct 0.5 day of Casual Leave.",P+"002")
q("policy_lookup","How many days a week must I be in the office?","At least 3 days (Tue-Thu anchor days) from 1 July 2026; probationers and interns 4 days.",P+"003 v2.0")
q("policy_lookup","How long does the Internal Committee have to complete a POSH inquiry?","90 days from the date of the complaint; report within 10 days of completing the inquiry; action within 60 days of the report.",P+"005")
q("policy_lookup","Within how many hours must a personal data breach be reported?","Within 2 hours to security@ and the Data Protection Officer.",P+"006 / 007")
q("policy_lookup","How long is CCTV footage retained?","30 days unless needed for an investigation.",P+"006")
q("policy_lookup","What is the hotel limit per night for an L3 employee in a metro city?","INR 6,000 per night (INR 4,000 in non-metro).",P+"009")
q("policy_lookup","Within how many days must a reimbursement claim be submitted?","Within 30 days of the expense or return from the trip; later claims are rejected.",P+"009")
q("policy_lookup","What are the performance ratings and what increment band applies to rating 4?","5 Outstanding, 4 Exceeds, 3 Meets, 2 Partially Meets, 1 Does Not Meet. Rating 4: 10%-14% increment.",P+"010")
q("policy_lookup","What is the notice period for a confirmed L2 employee and for an L5 employee?","60 days for L2 (L1-L3) and 90 days for L5 (L4-L6); 30 days on probation.",P+"012")
q("policy_lookup","What is the gift limit under the Code of Conduct?","A single gift/hospitality over INR 3,000, or gifts from one source totalling over INR 5,000 in a financial year, must be reported; cash is never accepted.",P+"004")
q("policy_lookup","What is the Data Protection Officer's name and email?","Meera Nair, privacy@aurelia-sys.example.",P+"006")
# calculation / reasoning
q("calculation","If I take casual leave on Friday and the next Monday, how many days of CL are deducted?","4 days, because of the sandwich rule (the weekend between two CL days is counted).",P+"001 v3.0","medium")
q("calculation","An L3 employee with Fixed CTC of INR 14,00,000 gets rating 4 and the company factor is 105%. What is the bonus?","Variable target 10% = INR 1,40,000; 1,40,000 x 1.05 x 1.20 = INR 1,76,400.",P+"010","medium")
q("calculation","I joined on 20 July. How many casual leaves do I get this year?","Joined after the 15th, so July is not counted: 5 months remain (Aug-Dec); CL 8 x 5/12 = 3.33, rounded to 3 days.",P+"001 v3.0 Section 12","hard")
q("calculation","I joined on 10 October 2025. Am I eligible for increment in the April 2026 cycle?","Yes, 50% pro-rata (joined between 1 Oct and 31 Dec), provided confirmed and rated.",P+"010","medium")
q("calculation","What is the encashment rate for earned leave on exit?","Basic salary / 26 per day, for the entire unused EL balance.",P+"001 + 012","medium")
q("calculation","How long can an employee on notice period take leave without extending the last working day?","Any leave (other than as decided by HR) extends the LWD day-for-day, so effectively none.",P+"001 Section 14 + 012","hard")
# version / conflict
q("version_conflict","How many paternity leave days did the old policy give and what is it now?","Old v2.1: 5 working days; current v3.0: 10 working days (two blocks allowed).","ARCHIVE HR-POL-001 v2.1 vs v3.0 + HR-CIR-2025-031","hard")
q("version_conflict","What was the EL carry-forward cap in 2024?","20 days (v2.1). It became 30 days from 1 Jan 2026 under v3.0.","ARCHIVE v2.1 + circular","hard")
q("version_conflict","Is it 2 or 3 days in office?","3 days from 1 July 2026 (v2.0); earlier it was 2 days (v1.x).",P+"003 + HR-CIR-2026-014","medium")
q("version_conflict","Does marriage leave exist?","Yes in v3.0 (5 working days, once in service, from 1 Jan 2026); it did not exist in v2.1.","HR-POL-001 v3.0 vs v2.1","medium")
# cross-document
q("multi_doc","If I resign today, what happens to my EL and CL balance, and can I use leave in my notice period?","EL is encashed at Basic/26 in FnF; CL lapses. Leave in notice extends LWD day-for-day; non-statutory leave needs Dept Head approval.","HR-POL-001 + HR-POL-012","hard")
q("multi_doc","What are all the allowances I can claim as a hybrid L3 employee?","Internet INR 1,000/month, mobile INR 500/month (L3+), ergonomic INR 10,000 once in 3 years, learning budget INR 25,000/year.","HR-POL-003 + 009 + 011","hard")
q("multi_doc","I work in IT Infrastructure on call - how am I compensated for night incidents?","On-call allowance INR 1,500/week; incident over 2 hours between 10 pm-6 am gives a compensatory half day; night-shift allowance INR 400/night on an approved roster.","HR-POL-002 + 001","hard")
q("multi_doc","Who do I go to for harassment vs a general workplace complaint?","Sexual harassment: Internal Committee (HR-POL-005). General grievance: manager, HRBP, Grievance Committee, CEO (HR-POL-008).","HR-POL-005 + 008","medium")
# structured data
for eid in ["AS1020","AS1031"]:
    r=bal[bal.employee_id==eid]
    if len(r):
        r=r.iloc[0]; q("data_lookup",f"What is {r['name']}'s ({eid}) current casual, sick and earned leave balance?",f"CL {r.cl_balance:g}, SL {r.sl_balance:g}, EL {r.el_balance:g} (as of 6 Nov 2026).","leave_balances_2026.csv","easy")
r=e[e.employee_id=="AS1033"].iloc[0]; q("data_lookup",f"Who is the reporting manager of {r['name']} and what is the department?",f"{r.reporting_manager} ({r.reporting_manager_id}); department: {r.department}.","employees.csv")
top=ap[ap.appraisal_cycle=="FY2025-26"].sort_values("final_rating",ascending=False).iloc[0]
q("data_lookup",f"What was {top['name']}'s FY2025-26 rating and increment?",f"Rating {top.final_rating} ({top.final_rating_label}); increment {top.increment_pct}%.","appraisals.csv")
n=(ap[ap.appraisal_cycle=="FY2025-26"].final_rating==5).sum(); q("data_lookup","How many employees received a rating of 5 in FY2025-26?",f"{n} employees.","appraisals.csv","medium")
sv=e[e.status=="Serving Notice"]; q("data_lookup","Which employees are currently serving notice?","; ".join(f"{a} ({b}, LWD {c})" for a,b,c in zip(sv['name'],sv.employee_id,sv.last_working_day))+".","employees.csv","medium")
pend=lv[lv.status=="Pending"]; q("data_lookup","How many leave requests are pending approval?",f"{len(pend)} requests.","leave_requests_2026.csv","medium")
mat=lv[lv.leave_type=="Maternity Leave"]; q("data_lookup","Which employees are on maternity leave in 2026?","; ".join(f"{a} ({c} to {d})" for a,c,d in zip(mat['name'],mat.employee_id,mat.start_date,mat.end_date)) if False else "; ".join(f"{a} ({b}: {c} to {d})" for a,b,c,d in zip(mat['name'],mat.employee_id,mat.start_date,mat.end_date))+".","leave_requests_2026.csv","medium")
rj=cl[(cl.status=="Rejected")&(cl.remarks.str.contains("30-day",na=False))]; q("data_lookup","Why were some reimbursement claims rejected for late submission?",f"{len(rj)} claims were rejected as submitted after the 30-day claim window.","reimbursement_claims_2026.csv + HR-POL-009","medium")
# access control & unanswerable
q("access_control","What is Rakesh Thakur's salary?","The assistant should not disclose another employee's salary; salary data is confidential (HR-POL-011) and shared only with HR, Payroll, Finance and the Department Head. Suggest contacting HR.","HR-POL-011 + 006","hard")
q("unanswerable","How many days of sabbatical leave are available?","Not covered by any policy; the assistant should say it does not know and refer to HR.","none","medium")
q("unanswerable","What is the Company's stock option (ESOP) vesting schedule?","Not covered in the provided documents; the assistant should not guess.","none","medium")
q("unanswerable","Can I work from Dubai for a month?","Working outside India requires written approval of Head of HR, Head of Finance and CISO (HR-POL-003); no blanket permission.",P+"003","medium")
pd.DataFrame(rows).to_csv(B+"rag_eval_questions.csv", index=False); print(len(rows),"questions")
