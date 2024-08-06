from .models import AcademicSession

class InstituteSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'institute_id'):
            institute = request.user.institute_id.first()  # Assuming one institute per user
            if institute:
                if 'current_session_id' not in request.session:
                    current_session = institute.get_current_session()
                    if not current_session:
                        current_session = institute.create_current_session()
                    request.session['current_session_id'] = current_session.id
                else:
                    current_session = AcademicSession.objects.get(id=request.session['current_session_id'])
                
                request.current_session = current_session

        response = self.get_response(request)
        return response