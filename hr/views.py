from django.shortcuts import render, redirect , get_object_or_404
from .models import HrInterview
from .forms import HrInterviewForm
from accounts.models import AcademicSession, InstituteBranch
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HrInterview, AcademicSession

def interview_list(request):
    if not request.user.is_authenticated:
        # Redirect to login or another appropriate page for unauthenticated users
        return redirect('accounts:super-admin-login')

    user = request.user
    institute = user.institute_id.first()

    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(request, "No active session found. Please activate a session to view interviews.")
        interview = HrInterview.objects.none()  # Return an empty queryset
    
    if not active_branch:
        messages.warning(request, "No active branch found. Please activate a branch to view interviews.")
        interview = HrInterview.objects.none()
    else:
        interview = HrInterview.objects.filter(institute=institute, session=active_session, branch = active_branch)

    context = {
        'interview': interview
    }

    return render(request, 'interview_list.html', context=context)


def interview_register(request):
    if request.method == 'POST':
        user = request.user
        interview_form = HrInterviewForm(request.POST, request.FILES, user = request.user, session = request.session)
        branch= request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        session= request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        if not active_session:
            messages.warning(request, "No active session found. Please create or activate a session.")
            return HrInterview.objects.none()
        if not active_branch:
            messages.warning(request, "No active branch found. Please activate a branch to schedule interviews.")
        
        if interview_form.is_valid():
            try:
                interview = interview_form.save(commit=False)
                interview.user = user
                interview.session = active_session
                interview.branch = active_branch
                interview.save()
                return redirect('hr:list_of_interview')
            except Exception as e:
                print(f"Error saving interview details: {e}")
        else:
            print("Interview form errors:", interview_form.errors)
    else:
        interview_form = HrInterviewForm(user = request.user)
    
    return render(request, 'interview_form.html', {
        'interview_form': interview_form
    })
    
    
def interview_update(request, pk):
        hr_interview = get_object_or_404(HrInterview, pk=pk)
        
        if request.method == 'POST':
            interview_form = HrInterviewForm(request.POST, request.FILES, instance=hr_interview, user=request.user, session=request.session)
            
            if interview_form.is_valid():
                try:
                    interview = interview_form.save(commit=False)
                    interview.save()
                    return redirect('hr:list_of_interview')
                except Exception as e:
                    print(f"Error saving form:{e}")
        else:
            interview_form = HrInterviewForm(instance=hr_interview)
        return render(request, 'interview_form.html',{
            'interview_form':interview_form
        })    
        
def interview_delete(request,pk):
    interview_profile = get_object_or_404(HrInterview, pk=pk)
    interview_profile.delete()
    
    return redirect('hr:list_of_interview')