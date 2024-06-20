document.addEventListener('DOMContentLoaded', function () {
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    const menuContent = document.getElementById('menu-content');


    const menuData = {
        'system-settings': `
        <li class="menu-title" key="t-menu">System Settings</li>
            <a href="${urls.instituteList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Institute</span>
            </a>
            <a href="javascript: void(0);" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#system-settings-list-of-masters" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List of Masters</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="system-settings-list-of-masters" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.listOfSignature}"><i class="fas fa-signature"></i>Signature</a>
                </li>
                <li class="sidebar-item ">
                    <a href="${urls.listOfCaste}"><i class="fas fa-user-tag"></i>Caste</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfCategory}"><i class="fas fa-layer-group"></i>Category</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfHouse}"><i class="fas fa-home"></i>House</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfMedium}"><i class="fas fa-book-open"></i>Medium</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfReligion}"><i class="fas fa-praying-hands"></i>Religion</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfReference}"><i class="fas fa-book"></i>Reference</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfNationality}"><i class="fas fa-globe"></i>Nationality</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfMotherTongue}"><i class="fas fa-language"></i>Mother Tongue</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfFamilyRelation}"><i class="fas fa-users"></i>Family Relation</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfEnquiryType}"><i class="fas fa-question-circle"></i>Enquiry Type</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfPaymentMode}"><i class="fas fa-money-bill"></i>Payment Mode</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfClassGroups}"><i class="fas fa-layer-group"></i>Class Groups</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfStandard}"><i class="fas fa-chalkboard-teacher"></i>Class</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfSubject}"><i class="fas fa-book-reader"></i>Subject</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfDocument}"><i class="fas fa-folder-open"></i>Documents</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfFeeHeads}"><i class="fas fa-file-invoice-dollar"></i>Fee Heads</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfFeeInstallments}"><i class="fas fa-file-invoice"></i>Fee Instalments</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfLeavingReason}"><i class="fas fa-map-marked-alt"></i>Leaving Reason (TC)</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfSainikSchool}"><i class="fas fa-school"></i>Name of Sainik School</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfNameOfBank}"><i class="fas fa-university"></i>Name of the Bank</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfStudentType}"><i class="fas fa-user-tag"></i>Student Type</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfChildStatus}"><i class="fas fa-user-tag"></i>Child Status</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#system-settings-session-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="system-settings-session-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Subjects for Class Groups</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Section</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Classes in Class Groups</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-praying-hands"></i>Class-wise Subjects</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book"></i>Documents Required</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Fee Structure</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Subject-wise Fee Installment</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Discount Scheme</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Sub-subjects</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#system-settings-report-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Report Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="system-settings-report-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Demand Slip Format</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Employee ID Card Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Fee Certificate Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Fee Receipt Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-praying-hands"></i>Create Report Heading</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book"></i>Assign Headers to Reports</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Academic Certificate Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Character Certificate Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>TC (CBSE) Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>TC (RBSE) Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Custom Certificate</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>SR Form Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Admission Form Format</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Logo</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Student ID Card Format</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">create user</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">create roles</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Templates</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Gateway Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Gateway Report</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Template Master</span>
            </a>
        `,
        'enquiry': `
        <li class="menu-title" key="t-menu">Enquiry</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">New Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">My Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">View Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Online Registration</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#enquiry-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="enquiry-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Created By Reports</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Statuc-wise Reports</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Reminder-Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Assigned Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-praying-hands"></i>Lead Source Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book"></i>Summary Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Custom Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Session-wise Report</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to Shortlist</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to Enroll</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to SR/Admission</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#enquiry-session-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="enquiry-session-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Enquiry Print Format</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Enquiry Settings</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Enquiry Term & Condition</a>
                </li>
            </ul>
           <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#enquiry-system-settings" aria-expanded="false" aria-controls="pages">
           <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="enquiry-system-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Class (List)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Medium</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Reference</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Enquiry Type</a>
                </li>
            </ul>
        `,
        'scholar-register': `
        <li class="menu-title" key="t-menu">scholar-register</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Record</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Dashboard</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Grievance/Suggestion</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">RTE Student</span>
            </a>
             <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Active/Deactive Students</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Re Study Students</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Transfer</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Assign(Subject wise)/span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Assign(Student wise)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Branch link</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">House Assign</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Log</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#Scholar-register-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="Scholar-register-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Custom Reports</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Custom sms</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Student Strength Class-wise</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Student Strength Catagory-wise</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-praying-hands"></i>Student Strength Relegion-wise</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book"></i>Student Strength Age-wise</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Student Subject Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Issued T.C Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Issued Study Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Issued Character Certificate Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Admission Form</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>SR Form</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Balnk Admission Form</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Student ID Card</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Age Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Documents Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>House Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Sibling Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Migration Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Student Log Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-globe"></i>Student Strength Report</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#scholar-register-issue-certificate" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Issue Certificate</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="scholar-register-issue-certificate" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Study Certificate</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Character Certificate</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Transfer Certificate</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Custom Certificate</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#scholar-register-Gate-pass" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Gate Pass</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="scholar-register-Gate-pass" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Gate Pass Format</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Gate Pass Create</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Gate Pass Report</a>
                </li>
            </ul>
        `,
        'accounts': `
        <li class="menu-title" key="t-menu">Accounts</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipts</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Contra</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Journal</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#accounts-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="accounts-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Party</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>bank</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Ledgers/Head</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#scholar-register-issue-certificate" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Issue Certificate</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="scholar-register-issue-certificate" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Incom & expenditure</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Day Book</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Ledger</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Expense Request</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Expense Approval/span>
            </a>
        `,
        'fees-module': `
        <li class="menu-title" key="t-menu">Fees Module</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Deposit</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Deposit(All)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cheque Reconciliation</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cheque Reconciliation Bulk</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">View Fee Receipts</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Discount</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">vFee Refund</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#fees-module-fees-ledger-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fees Module Ledger</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="fees-module-fees-ledger-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Print Demand Slip</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Day Book</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Day Book (Discount Report)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Day Book (School Report)</a>
                </li>
                <li class="sidebar-item">
                <a href="#"><i class="fas fa-book-open"></i>Day Book (Fee Account Register)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Day Book (Admission Form)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Cheque Status(PDC)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Cheque Status(Receipt)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Due Fee Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Due Fee (Head-wise)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Due Report (Installment-wise)</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Installment Assignment</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Due Fee Quarter-wise</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Fee Refund</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Sibling Due Fee Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Discount Request Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Day Book Summary</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipt Admission Form</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Search Admission Form</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Other Receipt</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">No Dues Receipt</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#fees-module-fees-admission-process" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Admission Process</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="fees-module-fees-admission-process" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Prospectus Fee</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Registration Fee</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Registration to Admission</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Prospectus Report</a>
                </li>
                <li class="sidebar-item">
                <a href="#"><i class="fas fa-book-open"></i>Registration Report</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Admission Summary</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Admission Report</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#fees-module-fees-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="fees-module-fees-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Installment Mode</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class Fee Structure</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Installment mode Assign</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Reciept Settings</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Class Discount</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Daybook Receipt</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipt Import</span>
            </a>
        `,
        'teacher-management': `
        <li class="menu-title" key="t-menu">Teacher Management</li>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#teacher-management-list-master" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="teacher-management-list-master" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Catagory Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Designation Master</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>Department Master</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Attendance Type</a>
                </li>
                <li class="sidebar-item">
                <a href="#"><i class="fas fa-book-open"></i>Attendance Settings</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Holiday List</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Exception List</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#teacher-management-attendance-setting" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance Setting</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="teacher-management-attendance-setting" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Calendar Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>ID Card Employee</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Teacher Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Teacher & Subject Assignment</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">'Class Teacher' Assignment</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Time Table</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Proxy/Substitution</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#teacher-management-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fees Module Ledger</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="teacher-management-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Employee Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Custom Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Common SMS</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Daily Attendance Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Monthly Attendance Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>ID Card</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Print Class Time</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Proxy/Substitution Report</a>
                </li>
        `,
        'hr': `
        <li class="menu-title" key="t-menu">HR</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-employee" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-employee" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Create Employee</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Upload DocumentSalary StructureI</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-layer-group"></i>ID Card</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Employee Mapping</a>
                </li>
                <li class="sidebar-item">
                <a href="#"><i class="fas fa-book-open"></i>Salary Import</a>
                </li>
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-book-open"></i>Employee Service Diary</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-leave" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Leave</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-leave" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>My Leave Request</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Leave Request Approval</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Leave Allowed</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Leave Op. Balance</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-salary" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Leave</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-salary" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Employee Salary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Manual Ded./Earning</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Manual TDS</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Monthly Attendance</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Interview</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Custom Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Employee Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Common SMS</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Daily Attendance Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Monthly Attendance Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Late Coming</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Leave Balence</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Salary Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>In Out Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Salary Report (Multi Month)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Working Hours Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Earning Report</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-list-of-masters" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List Of Masters</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-list-of-masters" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Catagory</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Designation</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Department</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Document</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Department-wise Document</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Attendance Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Attendance Hours Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Leave Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Shift</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Holidays</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Exception Work Days</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Calendar</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Salary Heads</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>ID Card Format</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Pay Slip Format</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-tds-document" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">TDS Document</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-tds-document" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>City Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Disability Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Invst. U/S 80C</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Education Loan</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Mediclaim Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Others Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Investment Declaration</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>TDS Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>EPF Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>ESIC Setting</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Job Applications</span>
            </a>
        `,
        'examination': `
        <li class="menu-title" key="t-menu">Examination</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Admit Card Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Print Admit card</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Exam Time Table Setting</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#examination-examination" aria-expanded="false" aria-controls="pages">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Examination</span>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="examination-examination" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Height Weight</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Marks Entry</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Marks Import/Export</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>NonScholastic Assessment Entry</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>School Meeting Entry</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Report Card</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Result Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Header Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Footer Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Examination Upper Header Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Grade Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>NonScholastic Subject Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>NonScholastic SubSubject Mast</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>NonScholastic GradeMaster</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Non-scholastic link with result</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>School Meetings Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Students Remark</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#examination-class-test" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Class Test</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="examination-classtest" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Class Test Result</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Marks Entry ClassTest</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class Test Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Marks Import/Export</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Report Card</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">PTM Format</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Marks List(Blank Format)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Roll Number</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Publish Exam. Result</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">White Sheet</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Publish Marksheet</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#examination-ib-board" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">IB Board</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="examination-ib-board" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Theme Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Theme Tamplate</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Subject Tamplate</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Result Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Result</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#examination-cambridge-board" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cambridge Board</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="examination-cambridge-board" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Skill Grade Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Students Remarks</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Report Card</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Result Master</a>
                </li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Marks Swap</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Green Sheet</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Marks Detail Import</span>
            </a>
        `,
        'library': `
        <li class="menu-title" key="t-menu">Library</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Library Profile</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-master" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-master" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Almirah Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Rack Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Category Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Publisher Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vendor Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Author Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Periodicity</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Language</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Periodical Master</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-member-details" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Member Details</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-member-details" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Member Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Library Members Record</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-library-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Library Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-library-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Book Issue Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room Assign</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-bill-record" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Bill Record</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-bill-record" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Book Bill</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Bill Detail</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Book Records</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-books-management" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Books Management</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-books-management" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Quick Issue/Deposit</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Books Issue/Deposit</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Damage Record</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Lost</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Withdrawal Record</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Withdrawal Approval</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Periodical Subscription</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Books Import</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Change Book Status</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#library-library-report" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">library-report</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="library-library-report" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Books Inventory Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Book Summary Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Books Ledger Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Books Issue Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Member Ledger Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Defaulter Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Custom Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>History/Ledger</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards"> Periodical Books Records</span>
            </a>
        `,
        'transport': `
        <li class="menu-title" key="t-menu">Transpost</li>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#transport-transport-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Transport Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="transport-transport-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Transport Profile</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Area</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Fuel Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Insurance Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Insurance</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Speed Certificate</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle PUC</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Service</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#transport-driver-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Driver Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="transport-driver-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Driver Designation</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Driver Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Category Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Department Master</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Allotment & Charges</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Allotment & Charges (Multi)</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#transport-transport-management" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Transport Management</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="transport-transport-management" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Driver & Vehicle Details</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Transport Instalment</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Fuel Details</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Stoppage</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Route Master</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#transport-reports" aria-expanded="false" aria-controls="pages">
            <div>v
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="transport-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Route wise</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle wise</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Route wise (Student)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Stoppage wise (Student)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle wise (Student)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vehicle Fitness</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Fee Report</a>
                </li>
            </ul>
        `,
        'hostel': `
        <li class="menu-title" key="t-menu">Hostel</li>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hostel-hostel-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">hostel Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hostel-hostel-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Hostel Profile</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Set Inning Time</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Building</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Floor</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room Category</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room Charges</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Hostel Amenities</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Hostel Instalment</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Hostel Allotment & Charges</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Hostel Allotment (Multi</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Warden & Hostel Allotment</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hostel-student-manage" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Manage</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hostel-student-manage" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Student In-Out</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Guardian In-Out</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Caution Money</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Hostel Receipt</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student De-activate</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Item Issue</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Item Deposit</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Hostel Attendance</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hostel-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hostel-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Building/Wing wise Summary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Floor wise Summary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Category(Facility) wise Summary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Room wise Summary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Hostel Summary</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Students Allotment Details</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Students In/Out</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Fee Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Attendance report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Monthly Attendance Report</a>
                </li>
            </ul>
        `,
        'attendance': `
        <li class="menu-title" key="t-menu">Attendance</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#attendance-master" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="attendance-master" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Holiday List</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Inning Timing Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Holiday Calendar</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class Calendar Assign</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#attendance-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="attendance-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Holiday Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Holiday Calendar List</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Daily Att. Report (Summary)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Monthly Attendance Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student In/Out Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Summary</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Machine ID Assign</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Card Block/Allow</span>
            </a>
        `,
        'mobile-module': `
        <li class="menu-title" key="t-menu">Mobile Module</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student App Login</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Change Password</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Home Work</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Notification</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Alert</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Events(Gallery)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Syllabus (Lesson)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Syllabus Progress</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Live Class</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Assignments</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#mobile-module-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="mobile-module-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Home Work Daily Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Home Work Monthly Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Syllabus Progress</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Notification Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Alert Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Live Class Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>App Download Report</a>
                </li>
            </ul>
        `,
        'visitor-master': `
        <li class="menu-title" key="t-menu">Visitor Master</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor Pass Format</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor entry</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#visitor-master-visitor-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="visitor-master-visitor-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Holiday List</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Inning Timing Setting</a>
                </li>
            </ul>
        `,
        'task-management': `
        <li class="menu-title" key="t-menu">Task Management</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Task</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">My Task</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Task For Approval</span>
            </a>
        `,
        'store-inventory': `
        <li class="menu-title" key="t-menu">Store Inventory</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Purchase Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Purchase Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Sales Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Sales Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payments receipts Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Minimum Quantity Setting</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#store-inventory-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="store-inventory-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Profile</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Product Category</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Unit of Measurement</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Payment Mode</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Create Reference</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Item Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Item Set</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Vendor Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Reports Template</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Sales Invoice Setting</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Payment Invoice Setting</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#store-inventory-reports" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="store-inventory-reports" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Payment Received Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Ledger Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Sales Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Sales Report (Student wise)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Sales Report (Item wise)</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Sales Return Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Purchase Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Min Required Stock Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Available Stock Report</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Student Due Report</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Link</span>
            </a>
        `,
        'online-examination': `
        <li class="menu-title" key="t-menu">Online Examination</li>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Dashboard</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Zone Master</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#online-examination-master" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="online-examination-master" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="#"><i class="fas fa-signature"></i>Instructions</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Question Type</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Questions</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Questions Import</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Examination Name</a>
                </li>
                <li class="sidebar-item ">
                    <a href="#"><i class="fas fa-user-tag"></i>Class Test Name</a>
                </li>
            </ul>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Papers</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Tests/Exams Due</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Tests/Exams Conducted</span>
            </a>
            `
    };

    // Set default menu content
    const defaultMenu = 'system-settings'; // Set this to the default menu you want to show
    if (menuData[defaultMenu]) {
        menuContent.innerHTML = menuData[defaultMenu];
    }


function initializeChevronToggle() {
    // Select all elements with the class 'sidebar-link d-flex justify-content-between align-items-center' that have a 'data-bs-toggle' attribute
    $('[data-bs-toggle="collapse"]').each(function () {
        var target = $(this).attr('data-bs-target'); // Get the target collapse ID

        // Add event listeners for show and hide events
        $(target).on('show.bs.collapse', function () {
            $(this).prev('a').find('.collapse-chevron').removeClass('fa-chevron-left').addClass('fa-chevron-down');
        }).on('hide.bs.collapse', function () {
            $(this).prev('a').find('.collapse-chevron').removeClass('fa-chevron-down').addClass('fa-chevron-left');
        });
    });
}

$(document).ready(function () {
    initializeChevronToggle(); // Call the function initially

    // Assuming 'dropdownItems' is an array-like object of elements that trigger the sidebar content change
    dropdownItems.forEach(item => {
        item.addEventListener('click', function (event) {
            event.preventDefault();
            const menuKey = this.getAttribute('data-menu');
            if (menuData[menuKey]) {
                menuContent.innerHTML = menuData[menuKey];
                initializeChevronToggle(); // Reinitialize the chevron toggle function after updating the content
            }
        });
    });
});
});