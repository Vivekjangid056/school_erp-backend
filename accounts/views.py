from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import User
from .forms import *
from scholar_register.models import StudentProfile
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'index.html')

def admin_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard/")

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if isinstance(user, User) and (user.is_superuser or user.role == '1'):
                login(request, user)
                return redirect('/dashboard/')
            elif isinstance(user, User) and user.role == '2':
                login(request, user)
                return redirect('/dashboard/')
            elif isinstance(user, User) and user.role == '3':
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.info(
                    request,
                    'You do not have permission to access the admin dashboard.'
                )
        else:
            messages.info(request,
                          'Invalid email or password. Please try again.')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'admin_login.html')


@login_required
def admin_dashboard(request):
    user = request.user
    user_id = user.id
    institute = Institute.objects.filter(user_id=user_id).first()
    context = {
        'institute': institute
    }
    return render(request, 'dashboard.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:super-admin-login')



class InstituteList(ListView, LoginRequiredMixin):
    model = Institute
    context_object_name = 'institutes'
    template_name = 'institute_list.html'


class InstituteUpdateView(UpdateView, LoginRequiredMixin):
    model = Institute
    form_class = InstituteForm
    context_object_name = "form"
    template_name = 'institute_update_form.html'
    success_url = reverse_lazy('accounts:institute_list')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)


@login_required
def institute_register_view(request):
    if request.method == 'POST':
        user_form = InstituteRegisterForm(request.POST)
        profile_form = InstituteForm(request.POST, request.FILES)

        print(f"User Form Errors: {user_form.errors}")
        print(f"Profile Form Errors: {profile_form.errors}")

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])  # Handle password setting
            user.save()
            profile = profile_form.save(commit=False)
            profile.user_id = user  # Set the admin field to the newly created admin
            profile.save()
            return redirect(reverse_lazy('accounts:institute_list'))
        else:
            context = {
                'form': user_form,
                'profile_form': profile_form,
            }
            return render(request, 'institute_register.html', context)
    else:
        user_form = InstituteRegisterForm()
        profile_form = InstituteForm()

    context = {
        'form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'institute_register.html', context)


class InstituteDeleteView(DeleteView):
    model = Institute
    success_url = reverse_lazy('accounts:institute_list')


def institute_branch_create_view(request):
    user = request.user
    try:
        user_institute = user.institute_id.first()
    except AttributeError:
        messages.error(request, "You don't have an associated institute.")
        return redirect("some_error_page")

    number_of_branches_permitted = int(user_institute.number_of_branches)
    number_of_branches_created = InstituteBranch.objects.filter(institute=user_institute).count()

    if number_of_branches_created < number_of_branches_permitted:
        if request.method == "POST":
            branch_form = InstituteBranchForm(request.POST)
            if branch_form.is_valid():
                try:
                    branch = branch_form.save(commit=False)
                    branch.institute = user_institute
                    branch.save()
                    messages.success(request, "Branch created successfully.")
                    return redirect("accounts:list_of_branches")
                except Exception as e:
                    messages.error(request, f"Error saving form: {e}")
            else:
                messages.error(request, f"Branch form errors: {branch_form.errors}")
        else:
            branch_form = InstituteBranchForm()
    else:
        messages.error(request, "You've reached the maximum number of permitted branches.")
        return render(request, 'branch_error.html')

    context = {
        'branch_form': branch_form,
    }
    return render(request, 'branch_register.html', context)


def branches_list(request):
    if request.user.role == "1":
        institutes = Institute.objects.all()
        branches = InstituteBranch.objects.all()
        context = {
            'institutes':institutes,
            'branches':branches
        }
        return render(request, 'branches_list.html', context=context)
    else:
        user = request.user
        try:
            user_institute = user.institute_id.first()
        except AttributeError:
            messages.error(request, "You don't have an associated institute.")
            return redirect("some_error_page")
        branches =InstituteBranch.objects.filter(institute = request.user.institute_id.first())
        number_of_branches_permitted = int(user_institute.number_of_branches)
        number_of_branches_created = InstituteBranch.objects.filter(institute=user_institute).count()

        context = {
        'branches':branches,
        'number_of_branches_permitted':number_of_branches_permitted,
        'number_of_branches_created':number_of_branches_created

        }
        return render(request, 'branches_list.html', context=context)

def institute_branch_update_view(request, pk):
    branch = get_object_or_404(InstituteBranch, pk=pk)

    if request.method == "POST":
        branch_form = InstituteBranchUpdateForm(request.POST, instance=branch)
        if branch_form.is_valid():
            try:
                branch = branch_form.save()
                messages.success(request, "Branch updated successfully.")
                return redirect("accounts:list_of_branches")
            except Exception as e:
                messages.error(request, f"Error updating branch: {e}")
        else:
            messages.error(request, f"Branch form errors: {branch_form.errors}")
    else:
        branch_form = InstituteBranchUpdateForm(instance=branch)

    context = {
        'branch_form': branch_form,
        'branch': branch,
    }
    return render(request, 'branch_register.html', context)


def institute_branch_delete_view(request, pk):
    branch = get_object_or_404(InstituteBranch, pk=pk)
    branch.delete()
    return redirect('accounts:list_of_branches')

# def check_session_timeout(request):
#     last_activity = request.session.get('last_activity')
#     if last_activity:
#         now = timezone.now()
#         elapsed_time = (now - last_activity).total_seconds()
#         if elapsed_time > settings.SESSION_COOKIE_AGE:
#             return redirect('logout')  # Redirect to your logout view or URL
#     request.session['last_activity'] = timezone.now()
