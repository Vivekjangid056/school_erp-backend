from django.shortcuts import redirect, render, get_object_or_404
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
        profile_form = StudentProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('students:list_of_students')
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("User Form Errors:", user_form.errors)
            print("Profile Form Errors:", profile_form.errors)
            return render(request, 'students_form.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })
    else:
        user_form = StudentUserCreationForm()
        profile_form = StudentProfileForm()
    return render(request, 'students_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def student_update(request,pk):
        student_profile = get_object_or_404(StudentProfile, pk=pk)
        if request.method == 'POST':
            profile_form = StudentProfileForm(request.POST, instance=student_profile)
            if profile_form.is_valid():
                try:
                    profile = profile_form.save(commit=False)
                    profile.save()
                    return redirect('students:list_of_students')
                except Exception as e:
                    print(f"Error saving form: {e}")
        else:
            profile_form = StudentProfileForm(instance=student_profile)
        return render(request,'students_update.html',{
            'profile_form': profile_form
        })
def student_delete(request, pk):
    student_profile = get_object_or_404(StudentProfile, pk=pk)
    user = student_profile.user
    student_profile.delete()
    user.delete()
    return redirect('students:list_of_students')