from hrlib import *
from config import *
from docs_a import OUTDIR, APPLIES_ALL

def conduct():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This Code of Conduct sets out the standards of behaviour expected of everyone who works for or on behalf of Aurelia Systems. It applies to all employees, interns, contract staff and consultants, in the office, while working remotely, at client sites, at company events and on company or personal digital channels when used in connection with work."),
    ]))
    s.append(dict(title="Our values", items=[
        ("b", ["Integrity: we do what is right, even when no one is watching.",
               "Ownership: we take responsibility for outcomes and follow through.",
               "Respect: we treat colleagues, customers and partners with dignity.",
               "Excellence: we care about quality and keep learning.",
               "Collaboration: we win as a team."]),
    ]))
    s.append(dict(title="Professional behaviour", items=[
        ("c", "Employees must treat everyone with courtesy and respect. Discrimination on the basis of gender, caste, religion, disability, sexual orientation, age, region, language or any other protected characteristic is prohibited."),
        ("c", "Bullying, intimidation, abusive language, public humiliation and retaliation against anyone who raises a concern in good faith are not tolerated."),
        ("c", "Sexual harassment is dealt with under HR-POL-005 (Prevention of Sexual Harassment Policy) and not under this Code."),
        ("c", "Employees must dress appropriately for the business setting. The Company follows a smart-casual dress code, with business attire when meeting clients or senior stakeholders."),
        ("c", "The use of, or reporting to work under the influence of, alcohol, intoxicants or illegal drugs is prohibited on Company premises and at Company events held on premises. Smoking is permitted only in designated areas."),
    ]))
    s.append(dict(title="Conflicts of interest and outside work", items=[
        ("c", "Employees must avoid situations in which personal interests conflict, or appear to conflict, with the interests of the Company. Any actual or potential conflict must be disclosed in writing to the reporting manager and HR."),
        ("c", "Moonlighting is not permitted. An employee must not take up any other employment, consulting, freelance or paid engagement, or run a business, that conflicts with Company work or demands time during working hours, without prior written approval of the Head of Human Resources. Unpaid volunteering, teaching, and writing that does not use Company resources or confidential information are permitted with intimation to the manager."),
        ("c", "Employees must not hold a financial interest in, or hold a position in, a Company competitor, client or supplier (other than listed shares held as a passive investment) without prior disclosure."),
        ("c", "Employees must not hire or directly manage a close relative. A relative of an employee may be hired in another department after disclosure and approval of the Head of Human Resources."),
    ]))
    s.append(dict(title="Gifts, hospitality and anti-bribery", items=[
        ("c", "Employees must not offer, give, request or accept bribes or improper payments. This applies to dealings with government officials and private parties alike."),
        ("c", "Gifts and hospitality received from, or given to, clients and suppliers must be modest and infrequent. A single gift or hospitality item worth more than \u20b93,000, or gifts from one source totalling more than \u20b95,000 in a financial year, must be reported to HR and may be required to be returned or surrendered. Cash or cash equivalents must never be accepted."),
        ("c", "Festive gifts received at the office during Diwali and similar occasions may be accepted if within the limit above."),
    ]))
    s.append(dict(title="Confidentiality and intellectual property", items=[
        ("c", "Employees must protect the confidential information of the Company, its clients and partners, during and after employment. Confidential information includes source code, product plans, customer data, financial results, pricing and personnel information."),
        ("c", "All work product created in the course of employment, including code, designs, documents and inventions, is the intellectual property of the Company, as set out in the employment agreement."),
        ("c", "Employees must not copy or take Company data, source code or documents to personal devices or accounts. Use of generative AI tools must follow HR-POL-007."),
    ]))
    s.append(dict(title="Use of social media and public statements", items=[
        ("c", "Employees may maintain personal social media accounts but must not disclose confidential information, speak on behalf of the Company without authorisation, or post content that harasses, discriminates or damages the reputation of the Company, its employees or clients."),
        ("c", "Media enquiries must be referred to the Marketing department. Only the CEO and designated spokespersons may speak to the media on behalf of the Company."),
    ]))
    s.append(dict(title="Reporting concerns and whistleblowing", items=[
        ("c", f"Employees who see or suspect a violation of this Code, fraud, financial irregularity or a legal breach should report it to their manager, to HR, or confidentially through the Speak Up channel at {CO['speakup_mail']}, which is monitored by the Head of Human Resources and the Head of Finance."),
        ("c", "Concerns involving the Head of Human Resources, the Head of Finance or the CEO may be sent directly to the Audit Committee of the Board at auditcommittee@aurelia-sys.example."),
        ("c", "No employee will suffer retaliation for a report made in good faith. Retaliation is itself a violation of this Code and may lead to termination. A deliberately false report is also a violation."),
    ]))
    s.append(dict(title="Disciplinary process", items=[
        ("c", "A violation of this Code may result in disciplinary action depending on its seriousness: (a) verbal counselling; (b) written warning; (c) show-cause notice; (d) suspension pending inquiry; (e) withholding of increment or promotion; (f) termination of employment. The Company is not bound to follow these steps in sequence if the misconduct is serious."),
        ("c", "Before any major penalty (suspension, demotion or termination for misconduct), the employee will be given a written statement of the allegations, a reasonable opportunity (normally 5 working days) to respond, and, where facts are disputed, a hearing by an inquiry panel of at least two persons who are not directly involved in the matter."),
        ("c", "Examples of serious misconduct include theft or fraud, falsification of records or documents, wilful damage to Company property, breach of confidentiality, sexual harassment, violence or threats, bribery, moonlighting without approval, and repeated unauthorised absence."),
        ("c", "The employee may appeal a major penalty to the Head of Human Resources within 10 working days; the CEO's decision on the appeal is final."),
    ]))
    meta = dict(doc_id="HR-POL-004", title="Code of Conduct and Ethics", version="3.1", effective="01 April 2025", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 March 2027", applies=APPLIES_ALL, revisions=[
                    ("1.0", "01 June 2016", "Initial Code of Conduct.", "Founders"),
                    ("2.0", "10 April 2020", "Added whistleblowing and anti-bribery provisions.", "HR Team"),
                    ("3.0", "12 January 2023", "Added moonlighting restrictions and social media guidance.", "Sunita Rao"),
                    ("3.1", "20 March 2025", "Revised gift limit to \u20b93,000; clarified disciplinary process.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-004_Code_of_Conduct_and_Ethics_v3.1.pdf", meta, s)

def posh():
    s = []
    s.append(dict(title="Purpose, legal basis and scope", items=[
        ("p", "Aurelia Systems is committed to providing a workplace that is free from sexual harassment. This policy is framed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 (the POSH Act) and the rules made under it."),
        ("c", "This policy applies to all employees (permanent, probationary, contract, interns, trainees and consultants), visitors and vendors' staff. It covers the workplace and any place visited in the course of employment, including client sites, business travel, company transport, offsites, events and online/virtual interactions."),
        ("c", "The statutory remedies of the Act are available to women. The Company, as a matter of its own policy, extends the same complaint and inquiry process to employees of all genders for complaints of sexual harassment by any person."),
    ]))
    s.append(dict(title="What is sexual harassment", items=[
        ("c", "Sexual harassment includes any unwelcome act or behaviour, whether directly or by implication, such as: physical contact and advances; a demand or request for sexual favours; making sexually coloured remarks; showing pornography; and any other unwelcome physical, verbal or non-verbal conduct of a sexual nature."),
        ("c", "The following circumstances, if connected to or present in an act of the above, may amount to sexual harassment: implied or explicit promise of preferential treatment; implied or explicit threat of detrimental treatment; implied or explicit threat about present or future employment status; interference with work or creating an intimidating or hostile work environment; or humiliating treatment likely to affect health or safety."),
        ("b", ["Repeated unwelcome comments on appearance, clothing or relationships",
               "Sending sexually suggestive messages, images or jokes on chat, email or social media",
               "Persistent invitations or following after being declined",
               "Unwelcome touching, standing too close or blocking the way",
               "Staring or gestures of a sexual nature, including during video calls"]),
    ]))
    s.append(dict(title="Internal Committee (IC)", items=[
        ("c", "The Company has constituted an Internal Committee at its Bengaluru head office to receive and inquire into complaints from all offices. Local Committees for Pune and Hyderabad assist with logistics but all inquiries are conducted by the IC."),
        ("c", f"The IC is composed of: (a) Presiding Officer - {IC_PRESIDING}, Senior HR Business Partner (a senior woman employee); (b) two employee members committed to the cause of women or having legal knowledge or social work experience; and (c) one external member - {IC_EXTERNAL}. At least half of the members are women."),
        ("c", "The term of the IC members is three years. Details of the current IC members are displayed on notice boards at each office and on the intranet."),
        ("c", f"The IC can be contacted confidentially at {CO['posh_mail']} or by writing to the Presiding Officer in a sealed envelope marked 'Confidential - Internal Committee'."),
    ]))
    s.append(dict(title="How to make a complaint", items=[
        ("c", "An aggrieved person may make a written complaint to the IC, with supporting documents and the names and addresses of witnesses, within 3 months from the date of the incident (or the last incident in a series of incidents). The IC may extend this period by a further 3 months if it is satisfied that circumstances prevented the complainant from filing within time."),
        ("c", "If the complainant cannot make a written complaint, the Presiding Officer or any IC member will render all reasonable assistance in writing it down. Where the complainant is unable to complain on account of physical or mental incapacity or death, a legal heir or any person who knows the facts, with the consent of the IC, may complain on her behalf."),
        ("c", "On receipt of the complaint, the IC will send a copy to the respondent within 7 working days, and the respondent must reply within 10 working days of receipt."),
    ]))
    s.append(dict(title="Conciliation and inquiry", items=[
        ("c", "At the request of the complainant, the IC may, before starting an inquiry, take steps to settle the matter through conciliation. No monetary settlement can be made as the basis of conciliation. If a settlement is reached, the IC records it and no further inquiry is conducted."),
        ("c", "The IC will complete the inquiry within 90 days from the date of the complaint, following the principles of natural justice, giving both parties an opportunity to be heard and to submit evidence."),
        ("c", "The IC will submit its findings report to the Company within 10 days of completing the inquiry and provide a copy to both parties. The Company will act on the recommendations within 60 days of receiving the report."),
        ("c", "Pending the inquiry, on the complainant's written request, the IC may recommend interim measures such as transfer of the complainant or respondent, grant of up to 3 months of additional leave to the complainant (which is in addition to leave otherwise entitled), or restraining the respondent from reporting on the complainant's work."),
    ]))
    s.append(dict(title="Action and consequences", items=[
        ("c", "If the allegation is proved, the Company will take action in accordance with the service rules, which may include a written apology, warning, reprimand or censure, withholding of promotion or increments, termination of services, and community service, and may include deduction of compensation from the respondent's salary as determined under the Act."),
        ("c", "If the allegation is found to be malicious or the complainant or witness has given false evidence knowingly, action may be taken against the person. A complaint that is not proved is not, by itself, treated as malicious."),
        ("c", "Either party may appeal to the appropriate court or tribunal within 90 days of the recommendations as provided under the Act."),
    ]))
    s.append(dict(title="Confidentiality, protection and awareness", items=[
        ("c", "The contents of the complaint, the identity and addresses of the complainant, respondent and witnesses, inquiry proceedings, recommendations and action taken are confidential and must not be published, communicated or made known to the public, press or any third party. Breach of confidentiality attracts a penalty under the Act."),
        ("c", "Retaliation against a complainant or witness is strictly prohibited."),
        ("c", "The Company conducts POSH awareness sessions for all employees at least once every year, and orientation for IC members. New joiners complete the POSH e-learning module within 30 days of joining."),
        ("c", "The IC prepares an annual report of the number of complaints received and disposed of, which is included in the Company's annual report as required by law and submitted to the District Officer."),
    ]))
    meta = dict(doc_id="HR-POL-005", title="Prevention of Sexual Harassment (POSH) Policy", version="2.0", effective="01 June 2024", owner="Kavitha Sundaram, Presiding Officer, Internal Committee",
                approver="Arvind Menon, Chief Executive Officer", review="31 May 2026 (due)", applies=APPLIES_ALL + " and visitors/vendor staff", queries=CO["posh_mail"], revisions=[
                    ("1.0", "15 February 2017", "Initial POSH policy and constitution of the IC.", "HR Team"),
                    ("1.1", "01 September 2021", "IC reconstituted; online harassment included.", "HR Team"),
                    ("2.0", "28 May 2024", "Extended process to all genders; added virtual workplace coverage.", "Kavitha Sundaram")])
    build_policy(OUTDIR + "HR-POL-005_POSH_Policy_v2.0.pdf", meta, s)

def privacy():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", f"{CO['name']} (the Company) respects the privacy of its employees, candidates and contractors. This policy explains what personal data we collect about you in connection with your employment, why we collect it, how we use, share and protect it, how long we keep it, and what rights you have. It is framed to comply with the Digital Personal Data Protection Act, 2023 and the rules made under it, as in force from time to time, and other applicable Indian law."),
        ("c", "This policy applies to all employees (including probationers, interns and contract employees), job applicants, former employees and nominees or dependants whose data is given to us by an employee (for example, family members covered by insurance)."),
        ("c", "In relation to this data, the Company is the Data Fiduciary. Service providers who process data on our behalf are Data Processors."),
        ("c", "Customer and product data processed by the Company in its client services is dealt with under the Customer Data Protection Policy and not by this policy."),
    ]))
    s.append(dict(title="Personal data we collect", items=[
        ("t", ["Category", "Examples", "Source"], [
            ["Identity and contact", "Name, date of birth, gender, photograph, address, personal phone and email, emergency contact", "Employee, application form"],
            ["Government identifiers", "PAN, Aadhaar (masked), passport (where needed for travel), UAN, bank account details", "Employee"],
            ["Recruitment and background", "CV, interview notes, education and employment history, reference and background-verification results", "Candidate, BGV agency"],
            ["Employment records", "Offer and appointment letters, grade, designation, manager, appraisal records, disciplinary records, training records", "Company"],
            ["Compensation and payroll", "Salary, deductions, tax declarations, PF/ESI details, reimbursement claims, loans and advances", "Employee, Payroll"],
            ["Attendance and leave", "Badge swipes, check-in times, leave applications, remote-work days", "Systems, employee"],
            ["Health and benefits (sensitive)", "Medical certificates, fitness certificates, health insurance enrolment, maternity leave documents, disability accommodation requests", "Employee, insurer"],
            ["Family and dependants", "Spouse, children and parents' names and dates of birth for insurance and nomination (PF, gratuity)", "Employee"],
            ["Technology and security", "Laptop and account logs, VPN and email metadata, CCTV footage at office entrances and common areas", "Systems"],
        ], [20, 56, 24]),
        ("c", "We do not collect biometric data such as fingerprints or facial templates for attendance. Badge readers record only the badge number and time."),
        ("c", "We collect only the data necessary for the purposes in Section 3. You are responsible for providing accurate information and keeping it up to date in the HRMS."),
    ]))
    s.append(dict(title="Why we use your data and on what basis", items=[
        ("t", ["Purpose", "Legal basis"], [
            ["Recruitment, onboarding, contracts and background verification", "Consent (for BGV) and legitimate use for employment"],
            ["Payroll, tax deduction, PF, gratuity, insurance and statutory filings", "Legal obligation; legitimate use for employment"],
            ["Attendance, leave, performance management, promotions and disciplinary matters", "Legitimate use for employment purposes"],
            ["Safeguarding the Company's IT systems, premises and confidential information", "Legitimate use; security safeguards"],
            ["Health insurance, wellness programmes and accommodations", "Consent"],
            ["Employee communication, events, directory and internal photos", "Consent"],
            ["Responding to legal requests, inquiries (including POSH) and defending claims", "Legal obligation"],
        ], [60, 40]),
        ("c", "Where we rely on your consent, you may withdraw it at any time by writing to the Data Protection Officer. Withdrawal does not affect processing done before withdrawal and may affect our ability to provide the related benefit (for example, group health insurance)."),
        ("c", "We will not use your personal data for a new purpose that is incompatible with the purposes above without informing you and, where required, obtaining your consent."),
    ]))
    s.append(dict(title="Sharing of personal data", items=[
        ("c", "Within the Company, personal data is accessible only to those who need it for their role. Your reporting manager sees your leave, attendance and performance data; HR and Payroll see employment and compensation data; Finance sees data required for payments; and IT sees technology data. Salary information is restricted to HR, Payroll, Finance and the employee's Department Head."),
        ("c", "We share data with Data Processors under written contracts that require them to protect it and use it only on our instructions. These include: the payroll and HRMS provider; group health insurance provider and broker; background-verification agency; PF, gratuity and tax authorities; travel and cab vendors; and cloud and email service providers."),
        ("c", "We disclose personal data to government authorities, regulators, courts and law enforcement where required by law."),
        ("c", "Personal data is stored on servers located in India. If any vendor processes data outside India, it will be only to a country permitted by the Government of India and under appropriate safeguards."),
        ("c", "We do not sell personal data."),
    ]))
    s.append(dict(title="Retention", items=[
        ("t", ["Record type", "Retention period"], [
            ["Employee master record, appointment and exit documents", "8 years after separation"],
            ["Payroll, PF, gratuity and tax records", "8 years after the end of the financial year concerned"],
            ["Appraisal and disciplinary records", "5 years after separation"],
            ["Attendance and leave records", "5 years after the end of the leave year"],
            ["Medical certificates and health documents", "2 years after the end of the leave year or claim, unless needed for a statutory benefit"],
            ["POSH complaint and inquiry records", "As required by law, minimum 5 years from the date of closure"],
            ["Unsuccessful job applicants' data (CV and interview notes)", "12 months after the end of the recruitment process (longer only with consent for future roles)"],
            ["Background-verification reports", "3 years after joining (or 12 months for those who did not join)"],
            ["CCTV footage", "30 days, unless required for an investigation"],
            ["Email and chat logs of employees", "2 years, and for security incidents until the incident is closed"],
        ], [55, 45]),
        ("c", "After the retention period, data is securely deleted or anonymised, unless it must be retained under law or for a pending legal claim."),
    ]))
    s.append(dict(title="Your rights", items=[
        ("p", "Under the Act you have the following rights, which you may exercise by writing to the Data Protection Officer:"),
        ("b", ["Right to access: to obtain a summary of the personal data we process and the identities of those with whom it has been shared.",
               "Right to correction and updating: to have inaccurate or incomplete data corrected, completed or updated. Most personal details can be updated yourself in the HRMS.",
               "Right to erasure: to ask for erasure of data that is no longer necessary for the purpose for which it was collected, subject to retention required by law.",
               "Right to grievance redressal: to have any grievance about our handling of your data addressed.",
               "Right to nominate: to nominate another person to exercise your rights in the event of your death or incapacity."]),
        ("c", "We will respond to a rights request within 30 days. We may ask you to verify your identity. Requests that conflict with legal retention or the rights of others may be declined with reasons."),
        ("c", "If you are not satisfied with our response, you may approach the Data Protection Board of India as provided by the Act, after first raising the matter with us."),
    ]))
    s.append(dict(title="Security and breach response", items=[
        ("c", "The Company uses reasonable technical and organisational safeguards: role-based access control, multi-factor authentication, encryption in transit and at rest for HR systems, audit logging, and annual security awareness training."),
        ("c", f"Anyone who suspects a personal data breach (for example, an email with salary data sent to the wrong person, a lost laptop or unauthorised access to the HRMS) must report it immediately, and in any case within 2 hours, to {CO['security_mail']} and the Data Protection Officer at {CO['privacy_mail']}."),
        ("c", "The Company will assess every incident, take containment steps, and where required by law inform the Data Protection Board of India and the affected individuals in the prescribed form and time. As an internal standard, affected employees will be notified within 72 hours of the Company confirming a breach that is likely to cause them harm."),
        ("c", "Employees who handle personal data must complete the annual privacy training. Misuse of personal data, including accessing colleagues' records without a business need, is serious misconduct under HR-POL-004."),
    ]))
    s.append(dict(title="Monitoring of work systems", items=[
        ("c", "Company laptops, email, chat, VPN and network are Company property and are monitored for security, compliance and acceptable use as set out in HR-POL-007. Monitoring is carried out by the security team, is limited to what is necessary and proportionate, and does not include keystroke logging, screen recording, or webcam or microphone access."),
        ("c", "CCTV cameras are placed at entrances, reception, server rooms and common areas. There are no cameras in washrooms, restrooms, cabins used for private discussions or lactation rooms."),
    ]))
    s.append(dict(title="Data Protection Officer and contact", items=[
        ("c", f"The Data Protection Officer is {DPO}, Legal & Compliance Manager. Contact: {CO['privacy_mail']}."),
        ("c", "This policy may be updated from time to time. Material changes are notified to employees by email and published on the intranet."),
    ]))
    meta = dict(doc_id="HR-POL-006", title="Employee Data Privacy and Protection Policy", version="1.2", effective="01 November 2025", owner=f"{DPO}, Data Protection Officer",
                approver="Arvind Menon, Chief Executive Officer", review="31 October 2026 (due)", applies=APPLIES_ALL + ", job applicants and former employees", queries=CO["privacy_mail"], revisions=[
                    ("1.0", "01 March 2023", "Initial HR data privacy notice following the enactment of the DPDP Act, 2023.", DPO),
                    ("1.1", "15 June 2024", "Added retention schedule and vendor list.", DPO),
                    ("1.2", "20 October 2025", "Aligned with the DPDP Rules; added rights request process and breach notification standard.", DPO)])
    build_policy(OUTDIR + "HR-POL-006_Employee_Data_Privacy_Policy_v1.2.pdf", meta, s)

def infosec():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "This policy sets out the rules for the secure and acceptable use of Aurelia Systems' information, devices, networks and accounts. It applies to everyone who has access to Company systems, including interns, contractors and vendors."),
    ]))
    s.append(dict(title="Data classification", items=[
        ("t", ["Class", "Description", "Examples", "Handling"], [
            ["Public", "Approved for external release", "Website content, published blogs", "No restrictions"],
            ["Internal", "For employees only", "Policies, org charts, internal announcements", "Do not share outside the Company"],
            ["Confidential", "Business-sensitive", "Source code, client contracts, pricing, financials, roadmaps", "Share on need-to-know basis on approved tools only"],
            ["Restricted", "Highly sensitive; legal or regulatory impact", "Personal data of employees and customers, credentials, keys, salary data, health data", "Encrypted; access-logged; never sent on personal channels or pasted in external tools"],
        ], [12, 24, 36, 28]),
    ]))
    s.append(dict(title="Devices and access", items=[
        ("c", "Company work must be done on Company-issued, managed laptops. Personal devices (BYOD) may be used only to access email and chat through the approved mobile app with MDM enrolment; source code and Restricted data must never be stored on personal devices."),
        ("c", "Passwords must be at least 14 characters, unique to the Company account, and changed only if compromised. Multi-factor authentication (MFA) is mandatory for email, VPN, HRMS, code repositories and cloud consoles. Passwords must not be shared, even with the IT team."),
        ("c", "Laptops must have disk encryption and automatic screen lock after 5 minutes of inactivity enabled. Lock your screen when leaving your desk."),
        ("c", "USB mass-storage ports are disabled by default. A request for exemption must be approved by the CISO."),
        ("c", "Software may be installed only from the approved catalogue. Pirated or unlicensed software is prohibited."),
        ("c", "Lost or stolen devices must be reported to the IT Service Desk and the security team within 2 hours of discovery."),
    ]))
    s.append(dict(title="Email, internet and collaboration", items=[
        ("c", "Company email, chat and storage are for business use. Reasonable personal use is allowed if it does not interfere with work or breach this policy."),
        ("c", "Do not forward Company email to personal accounts, and do not use personal email or messaging apps (including WhatsApp groups) to share Confidential or Restricted information."),
        ("c", "Be alert to phishing. Report suspicious emails using the 'Report phishing' button in the email client. Do not click on links or open attachments from unknown senders."),
        ("c", "Accessing or downloading illegal, obscene, hateful or pirated content on Company systems is prohibited."),
    ]))
    s.append(dict(title="Use of generative AI tools", items=[
        ("c", "Employees may use only the Company-approved generative AI tools for work. Information classified as Confidential or Restricted (including source code, client information and any personal data) must not be entered into public or unapproved AI tools."),
        ("c", "Output from AI tools must be reviewed by the employee before use. The employee remains responsible for the accuracy, security and licensing of work they submit."),
        ("c", "AI tools must not be used to make final decisions about individuals (for example, hiring, appraisal or disciplinary decisions) without human review."),
    ]))
    s.append(dict(title="Remote work security", items=[
        ("c", "Use the corporate VPN when accessing internal systems from outside the office. Do not use public Wi-Fi for work without VPN."),
        ("c", "Do not allow family members or others to use your Company laptop. Keep screens from view when working in public."),
    ]))
    s.append(dict(title="Clean desk and physical security", items=[
        ("c", "Wear your ID badge visibly in the office and do not allow tailgating through access-controlled doors. Visitors must be registered and escorted."),
        ("c", "Do not leave documents containing Confidential or Restricted data on desks, printers or whiteboards. Shred printed material that is no longer required."),
    ]))
    s.append(dict(title="Incident reporting", items=[
        ("c", f"Report any suspected security incident, such as phishing clicks, malware, loss of a device, misdirected emails or unauthorised access, to {CO['security_mail']} or the IT Service Desk within 2 hours. Reporting promptly will not attract disciplinary action; concealment will."),
        ("c", f"Incidents involving personal data are also reported to the Data Protection Officer under HR-POL-006. The CISO, {CISO}, coordinates incident response."),
    ]))
    s.append(dict(title="Monitoring and consequences", items=[
        ("c", "The Company monitors the use of its systems for security and compliance, as set out in HR-POL-006. There is no expectation of privacy in the content of Company systems, subject to applicable law."),
        ("c", "Violations of this policy may result in disciplinary action under HR-POL-004, up to termination, and may be reported to law enforcement."),
    ]))
    meta = dict(doc_id="HR-POL-007", title="Information Security and Acceptable Use Policy", version="2.3", effective="01 February 2026", owner=f"{CISO}, CISO",
                approver="Arvind Menon, Chief Executive Officer", review="31 January 2027", applies=APPLIES_ALL + ", contractors and vendors", queries=CO["security_mail"], revisions=[
                    ("1.0", "01 October 2019", "Initial policy.", CISO),
                    ("2.0", "10 May 2022", "Added remote work and BYOD rules.", CISO),
                    ("2.3", "15 January 2026", "Added generative AI section; password length raised to 14 characters.", CISO)])
    build_policy(OUTDIR + "HR-POL-007_Information_Security_and_Acceptable_Use_Policy_v2.3.pdf", meta, s)

def grievance():
    s = []
    s.append(dict(title="Purpose and scope", items=[
        ("p", "Aurelia Systems wants employees to feel free to raise concerns about work, colleagues, managers or Company decisions, and to have them resolved fairly and quickly. This policy describes the stages of the grievance process and the timelines for each."),
        ("c", "A grievance may relate to, for example, working conditions, pay or benefits errors, leave or attendance decisions, appraisal process, behaviour of a colleague or manager, discrimination, or any policy matter. It applies to all employees."),
        ("c", "Complaints of sexual harassment are not handled under this policy and must be made to the Internal Committee under HR-POL-005. Concerns of fraud or serious ethical violations should be raised through Speak Up under HR-POL-004."),
    ]))
    s.append(dict(title="Grievance redressal stages", items=[
        ("t", ["Stage", "Raise with", "Timeline for response / resolution"], [
            ["Informal", "Reporting manager or skip-level manager", "Discuss directly; resolution expected within 5 working days"],
            ["Stage 1", "HR Business Partner (via the HR helpdesk ticket or email to hr@aurelia-sys.example)", "Acknowledgement within 2 working days; resolution within 7 working days"],
            ["Stage 2", "Grievance Committee: Head of HR, Department Head (not involved in the matter) and one employee representative", "Meeting within 7 working days; written decision within 15 working days of escalation"],
            ["Stage 3", "CEO (final appeal)", "Decision within 15 working days of appeal; the decision is final"],
        ], [14, 46, 40]),
        ("c", "An employee may skip the informal stage if the grievance concerns the reporting manager, or if the employee is uncomfortable approaching the manager."),
        ("c", "An employee who is not satisfied with a decision may escalate to the next stage within 10 working days of receiving the decision."),
    ]))
    s.append(dict(title="Making a grievance", items=[
        ("c", f"A grievance can be raised through {CO['helpdesk']}, by email to {CO['hr_mail']}, or in person with HR. It should state the facts, the dates, the people involved and the outcome the employee seeks."),
        ("c", "Employees may be accompanied by a colleague of their choice at any meeting under Stage 2."),
        ("c", "Anonymous grievances may be raised through Speak Up. The Company will examine them, but may be limited in its ability to investigate or respond if details are insufficient."),
    ]))
    s.append(dict(title="Principles", items=[
        ("b", ["Confidentiality: information is shared only with those who need to know to resolve the matter.",
               "Fairness: all parties are heard and decisions are based on facts.",
               "No retaliation: no employee will be penalised for raising a grievance in good faith.",
               "Records: the grievance register is maintained by HR; the outcome is communicated in writing."]),
    ]))
    s.append(dict(title="Review and reporting", items=[
        ("c", "HR reviews all grievances quarterly for trends and reports a summary (without personal details) to the CEO."),
    ]))
    meta = dict(doc_id="HR-POL-008", title="Grievance Redressal Policy", version="1.3", effective="01 January 2025", owner="Sunita Rao, Head of Human Resources",
                approver="Arvind Menon, Chief Executive Officer", review="31 December 2026", applies=APPLIES_ALL, revisions=[
                    ("1.0", "01 June 2018", "Initial policy.", "HR Team"),
                    ("1.2", "01 April 2022", "Added Grievance Committee (Stage 2).", "HR Team"),
                    ("1.3", "10 December 2024", "Added informal stage and timelines.", "Sunita Rao")])
    build_policy(OUTDIR + "HR-POL-008_Grievance_Redressal_Policy_v1.3.pdf", meta, s)

if __name__ == "__main__":
    conduct(); posh(); privacy(); infosec(); grievance(); print("ok")
