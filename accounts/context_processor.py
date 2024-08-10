from .models import AcademicSession, InstituteBranch

def session_data(request):
    user = request.user
    if user.is_authenticated:
        institute = user.institute_id.first()
        active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
        if active_session:
            request.session['session_id'] = active_session.id
        return {
            'institute': institute,
            'active_session': active_session,
        }
    return {}

def branch_data(request):
    user = request.user
    if user.is_authenticated:
        institute = user.institute_id.first()
        active_branch = InstituteBranch.objects.filter(institute = institute, is_active = True).first()
        if active_branch:
            request.session['branch_id'] = active_branch.id
        return {
            'institute':institute,
            'active_branch':active_branch,
        }
    return {}