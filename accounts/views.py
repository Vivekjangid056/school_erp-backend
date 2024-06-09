from pyexpat.errors import messages
from django.shortcuts import render, redirect, HttpResponseRedirect

from School_Erp import settings
from .models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login

# Create your views here.

def super_admin_login(request):
    try:
        # if request.user.is_authenticated:
        #     return redirect("/dashboard")
        
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = User.objects.filter(email = email)
            if not user_obj.exists():
                messages.info(request, "account not found")
                return HttpResponseRedirect(request.Meta.get('HTTP_REFERER'))
            user_obj = authenticate(email=email, password = password)

            if user_obj and user_obj.is_superadmin:
                login(request, user_obj)
                return redirect('/dashboard/')
            
            messages.info(request, 'invalid password')
            return redirect('/')
        
        return render(request, 'admin_login.html')
    
    except Exception as e:
        print(e)


# def check_session_timeout(request):
#     last_activity = request.session.get('last_activity')
#     if last_activity:
#         now = timezone.now()
#         elapsed_time = (now - last_activity).total_seconds()
#         if elapsed_time > settings.SESSION_COOKIE_AGE:
#             return redirect('logout')  # Redirect to your logout view or URL
#     request.session['last_activity'] = timezone.now()


def admin_dashboard(request):
    user = request.user
    return render(request, 'dashboard-saas.html', {'user':user})