from django.shortcuts import redirect, render
from django.contrib.auth import login

from accounts.models import User
from scholar_register.models import StudentProfile
from .forms import StudentUserCreationForm, StudentProfileForm
# Create your views here.

def student_list(request):
    students = StudentProfile.objects.all()
    
    context = {
        'students':students 
    }
    
    return render(request, 'students_list.html',context=context)

def student_register(request):
    if request.method == 'POST':
        user_form = StudentUserCreationForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('students:student_register')
        
    else:
        user_form = StudentUserCreationForm()
        profile_form = StudentProfileForm()
            
        return render(request, 'students_form.html',{
            'user_form':user_form ,
            'profile_form':profile_form
        })    