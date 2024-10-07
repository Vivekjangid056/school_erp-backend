from teacher_management.models import Employee
from .models import AcademicSession, InstituteBranch
from django.contrib import messages
from django.shortcuts import redirect

def session_data(request):
    user = request.user

    if user.is_authenticated and user.role in ["1", "2", "3", "4"]:
        # Get institute
        if user.role in ["1", "2"]:  # Admin roles
            institute = user.institute_id.first()
        else:  # Employee roles
            try:
                employee = Employee.objects.get(user=user)
                institute = employee.institute
            except Employee.DoesNotExist:
                messages.error(request, "You don't have an associated employee record.")
                return {}

        if not institute:
            messages.error(request, "No institute associated with the user.")
            return {}

        # Check if session data exists in the user's session
        session_id = request.session.get('session_id')

        if session_id:
            active_session = AcademicSession.objects.filter(id=session_id, institute=institute).first()
        else:
            # If session is not stored in the session, fetch the active session from the database
            active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
            if active_session:
                request.session['session_id'] = active_session.id

        # Fetch all sessions for the institute
        sessions = AcademicSession.objects.filter(institute=institute)

        return {
            'active_session': active_session,
            'sessions': sessions  # Pass all sessions to the template
        }

    return {}


def branch_data(request):
    user = request.user
    
    if user.is_authenticated and user.role in ["1", "2", "3", "4"]:
        # Get institute
        if user.role in ["1", "2"]:  # Admin roles
            institute = user.institute_id.first()
        else:  # Employee roles
            try:
                employee = Employee.objects.get(user=user)
                institute = employee.institute
            except Employee.DoesNotExist:
                messages.error(request, "You don't have an associated employee record.")
                return {}

        if not institute:
            messages.error(request, "No institute associated with the user.")
            return {}

        # Check if branch data exists in the user's session
        branch_id = request.session.get('branch_id')

        if branch_id:
            active_branch = InstituteBranch.objects.filter(id=branch_id, institute=institute).first()
        else:
            # If branch is not stored in the session, fetch the active branch from the database
            active_branch = InstituteBranch.objects.filter(institute=institute, is_active=True).first()
            if active_branch:
                request.session['branch_id'] = active_branch.id

        # Fetch all branches for the institute
        branches = InstituteBranch.objects.filter(institute=institute)

        return {
            'active_branch': active_branch,
            'branches': branches  # Pass all branches to the template
        }

    return {}

