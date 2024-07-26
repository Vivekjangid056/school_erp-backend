from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login
from accounts.models import User
from scholar_register.models import StudentProfile
from .forms import *
from django.contrib import messages
from django.db import transaction

# Create your views here.
def student_list(request):
    # user_institute = request.user.institute_id.first() #or
    user_institute = Institute.objects.get(user_id = request.user)
# for fetching the data from a table which is not directly connected with the current table but its f
# oreignkey table has a reference in the table then we user __
    students = StudentProfile.objects.filter(parent__institute = user_institute) 
    context = {
        'students':students
    }
    return render(request, 'students_list.html',context=context)

@transaction.atomic
def student_register(request):
    print("::::::::::::::::::::::::::::::::::::;;",request.user.institute_id)
    if request.method == 'POST':
        parent_registered = request.POST.get('parent_registered')
        profile_form = StudentProfileForm(request.POST, request.FILES)
        print("Parent registered:", parent_registered)
        
        if parent_registered == 'yes':
            existing_parent_id = request.POST.get('existing_parent')
            if not existing_parent_id:
                messages.error(request, "Please select an existing parent.")
                parents = StudentParents.objects.all()
                context = {
                    'profile_form': profile_form,
                    'parents': parents,
                }
                return render(request, 'students_form.html', context)
            
            try:
                parent = StudentParents.objects.get(id=existing_parent_id)
            except StudentParents.DoesNotExist:
                messages.error(request, "Selected parent not found.")
                parents = StudentParents.objects.all()
                context = {
                    'profile_form': profile_form,
                    'parents': parents,
                }
                return render(request, 'students_form.html', context)
            
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.parent = parent
                profile.save()
                messages.success(request, "Student registered successfully.")
                return redirect('students:list_of_students')
            else:
                print("Profile form errors:", profile_form.errors)
        else:
            user_form = ParentUserCreationForm(request.POST)
            parent_form = ParentProfileForm(request.POST, user=request.user)
            
            if user_form.is_valid() and parent_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                parent = parent_form.save(commit=False)
                parent.user = user
                parent.save()
                profile = profile_form.save(commit=False)
                profile.parent = parent
                profile.save()
                messages.success(request, "Student and parent registered successfully.")
                return redirect('students:list_of_students')
            else:
                print("User form errors:", user_form.errors)
                print("Parent form errors:", parent_form.errors)
                print("Profile form errors:", profile_form.errors)
        
        messages.error(request, "There were errors in the form. Please correct them and try again.")
        
        # Prepare context for invalid POST
        parents = StudentParents.objects.all()
        context = {
            'user_form': user_form if parent_registered == 'no' else ParentUserCreationForm(),
            'parent_form': parent_form if parent_registered == 'no' else ParentProfileForm(),
            'profile_form': profile_form,
            'parents': parents,
        }
        return render(request, 'students_form.html', context)
    else:
        # GET request
        user_form = ParentUserCreationForm()
        parent_form = ParentProfileForm()
        profile_form = StudentProfileForm()

    # Prepare context for GET
    parents = StudentParents.objects.all()
    context = {
        'user_form': user_form,
        'parent_form': parent_form,
        'profile_form': profile_form,
        'parents': parents,
    }
    
    return render(request, 'students_form.html', context)
    
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
    user = student_profile.parent.user
    student_profile.delete()
    return redirect('students:list_of_students')
