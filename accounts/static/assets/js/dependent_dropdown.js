document.addEventListener('DOMContentLoaded', function() {
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    const menuContent = document.getElementById('menu-content');

    const menuData = {
        'system-settings': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Institute</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Report Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">create user</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">create roles</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Templates</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Gateway Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Gateway Report</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Template Master</span>
            </a>
        `,
        'enquiry': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">New Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">My Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">View Enquiry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Online Registration</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to Shortlist</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to Enroll</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Convert to SR/Admission</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">Session Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-envelope"></i>
                <span key="t-dashboards">System Settings</span>
            </a>
        `,
        'scholar-register': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Record</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Dashboard</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Grievance/Suggestion</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">RTE Student</span>
            </a>
             <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Active/Deactive Students</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Re Study Students</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Transfer</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Assign(Subject wise)/span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Assign(Student wise)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Branch link</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">House Assign</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Log</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Report</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Issue Certificate</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Gate Pass</span>
            </a>
        `,
        'accounts': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payments</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipts</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Contra</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Journal</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Active/Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Accounts Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Expense Request</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Expense Approval/span>
            </a>
        `,
        'fees-module': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Deposit</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Deposit(All)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cheque Reconciliation</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cheque Reconciliation Bulk</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">View Fee Receipts</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Discount</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">vFee Refund</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fees Ledger Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipt Admission Form</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Search Admission Form</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Other Receipt</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">No Dues Receipt</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Admission Process</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Setting</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Class Discount</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Daybook Receipt</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Receipt Import</span>
            </a>
        `,
        'teacher-management': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Teacher Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Teacher & Subject Assignment</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">'Class Teacher' Assignment</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Time Table</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Proxy/Substitution</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
        `,
        'hr': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Leave</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Salary</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Interview</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List of Masters</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">TDS Documents</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Job Applications</span>
            </a>
        `,
        'examination': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Admit Card Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Print Admit card</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Exam Time Table Setting</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Examination</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Class Test</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">PTM Format</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Marks List(Blank Format)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Roll Number</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Publish Exam. Result</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">White Sheet</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Publish Marksheet</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">IB Board</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Cambridge Board</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Marks Swap</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Green Sheet</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Marks Detail Import</span>
            </a>
        `,
        'library': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Library Profile</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Masters</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Member Details</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Library Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Bill Records</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Book Records</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Books Management</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Library Report</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards"> Periodical Books Records</span>
            </a>
        `,
        'transport': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Transport Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Driver Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Allotment & Charges</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Allotment & Charges (Multi)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Transport Management</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
        `,
        'hostel': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Hostel Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Hostel Allotment & Charges</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Hostel Allotment (Multi</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Warden & Hostel Allotment</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Manage</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
        `,
        'Attendance': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Masters</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Attendance & Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Machine ID Assign</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Card Block/Allow</span>
            </a>
        `,
        'mobile module': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student App Login</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Change Password</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Home Work</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Notification</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Alert</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Events(Gallery)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Subject Syllabus (Lesson)</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Syllabus Progress</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Live Class</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Assignments</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
        `,
        'visitor-master': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor Pass Format</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Visitor Reports</span>
            </a>
        `,
        'task-management': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Task</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">My Task</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Task For Approval</span>
            </a>
        `,
        'store-inventory': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Purchase Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Purchase Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Sales Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Sales Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payments receipts Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Return Entry</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Minimum Quantity Setting</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Settings</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Reports</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Payment Link</span>
            </a>
        `,
        'store-inventory': `
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Dashboard</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Zone Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Master</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Papers</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Tests/Exams Due</span>
            </a>
            <a href="javascript: void(0);" class="waves-effect">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Tests/Exams Conducted</span>
            </a>
            `
    };

    dropdownItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            const menuKey = this.getAttribute('data-menu');
            if (menuData[menuKey]) {
                menuContent.innerHTML = menuData[menuKey];
            }
        });
    });
});
