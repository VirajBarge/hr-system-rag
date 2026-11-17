# Aurelia Systems Pvt. Ltd. - Synthetic HR Corpus (for an HR RAG)

Everything here is fictional. One company fact sheet drives every PDF and CSV, so the documents agree with each other (and disagree only where noted under "Built-in traps"). "Today" in this world is **6 Nov 2026**.

## Company fact sheet
- Bengaluru HQ, Pune, Hyderabad; ~147 people records (136 active, 3 serving notice, 8 exited); 11 departments; grades L1-L6.
- Leave year = calendar year. Performance cycle = financial year (Apr-Mar). HRMS = "Aurelia PeopleHub".
- Hours 9:30-18:30 Mon-Fri; hybrid 3 days/week from 1 Jul 2026; salary paid last working day.

## Folders
| Folder | Contents |
|---|---|
| policies/ | 13 HR policies (HR-POL-001 to 013), superseded Leave Policy v2.1 (ARCHIVE_), Holiday Calendar 2026, Employee Handbook FAQ |
| circulars/ | 3 policy-change circulars (leave revision, hybrid revision, Diwali/year-end) |
| forms/ | Leave application form, expense claim form |
| letters/ | Sample offer letter (with CTC annexure), 3 appraisal letters, PIP letter, relieving/experience letter (all generated from the CSV rows) |
| payslips/ | 5 October 2026 payslips (match payroll_october_2026.csv) |
| data/ | 11 CSVs (below) |
| manifest.csv | Every file with page/row counts |

## CSVs (data/)
| File | Key columns |
|---|---|
| employees.csv | employee_id, name, department, grade, employment_type, work_location, date_of_joining, probation_status, reporting_manager_id, status, last_working_day, notice_period_days |
| salary_structure.csv | annual_ctc, fixed_ctc, variable_target_pct, basic/hra/special_allowance_monthly, employer_pf, gratuity, gross_monthly |
| payroll_october_2026.csv | paid_days, lop_days, gross_earnings, reimbursements, employee_pf, professional_tax, income_tax_tds, net_pay |
| appraisals.csv | FY2024-25 and FY2025-26: self/manager/final rating, increment_pct, increment_eligibility, promotion_recommended, bonus multipliers |
| leave_requests_2026.csv | leave_type, start/end_date, days (sandwich rule applied to CL/SL), status, approver_id |
| leave_balances_2026.csv | CL/SL/EL entitlement, taken, balance; floating holidays; EL carry-forward and accrual |
| attendance_summary_jul_oct_2026.csv | days_in_office, days_wfh, leave_days, late_marks, avg_daily_hours |
| reimbursement_claims_2026.csv | category, amounts, status, remarks (limit/30-day rule outcomes) |
| holidays_2026.csv, departments.csv | reference tables |
| rag_eval_questions.csv | 41 test questions with expected answers and source files |

## Built-in traps (for testing the RAG)
- **Version conflict:** Leave Policy v2.1 (superseded) vs v3.0 (current): CL 7 vs 8, EL cap 20 vs 30, paternity 5 vs 10, etc.
- **Date-dependent rules:** hybrid policy 2 days -> 3 days on 1 Jul 2026.
- **Cross-document answers:** e.g. EL on exit (leave + exit policy), allowances (hybrid + travel + compensation).
- **Role-dependent rules:** notice period, hotel limits, variable pay by grade.
- **Access control:** other employees' salary should not be disclosed.
- **Unanswerable questions:** sabbatical, ESOP.
- Policies with overdue review dates (POSH, Privacy) exist on purpose.

## Regenerating
Source scripts (config.py, data.py, hrlib.py, docs_a-d.py, build_eval.py) are included in /source. Change numbers in config.py and rerun in this order: data.py, docs_a.py, docs_b.py, docs_c.py, docs_d.py, build_eval.py.
