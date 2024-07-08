from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# Create your views here.

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("dashboard/")
        
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = Admin.objects.filter(email = email)
            if not user_obj.exists():
                messages.info(request, "account not found")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(email=email, password = password)
            print(email)
            if user_obj and user_obj.is_superadmin:
                login(request, user_obj)
                return redirect('/dashboard/')
            if user_obj and user_obj.role == '2':
                login(request, user_obj)
                return redirect('/dashboard')
            
            messages.info(request, 'invalid password')
            return redirect('')
        
        return render(request, 'admin_login.html')
    
    except Exception as e:
        print(e)
        return render(request, 'admin_login.html', {'error': str(e)})



@login_required
def admin_dashboard(request):
    user = request.user
    user_id = user.id
    print(user_id)
    institutes = Institute.objects.filter(user_id = user_id)
    print(institutes)
    context = {
        'user' : user,
        'institute_list':institutes
    }
    return render(request, 'dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:super-admin-login') 


class InstituteList(ListView):
    model = Institute
    context_object_name = 'institutes'
    template_name = 'institute_list.html'


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    context_object_name = "form"
    template_name = 'update_form.html'
    success_url = reverse_lazy('accounts:institute_list')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)
    

class InstituteRegisterView(CreateView):
    template_name = 'institute_register.html'
    form_class = InstituteAdminRegisterForm
    second_form_class = InstituteForm
    success_url = reverse_lazy('accounts:institute_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        profile_form = self.second_form_class(request.POST, request.FILES)
        
        print(f"User Form Errors: {form.errors}")
        print(f"Profile Form Errors: {profile_form.errors}")

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Handle password setting
        user.save()
        profile = profile_form.save(commit=False)
        profile.user_id = user  # Set the admin field to the newly created admin
        profile.save()
        return redirect(self.success_url)

    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(form=form, profile_form=profile_form)
        )
    

class InstituteDeleteView(DeleteView):
    model = Institute
    success_url = reverse_lazy('accounts:institute_list')


# def check_session_timeout(request):
#     last_activity = request.session.get('last_activity')
#     if last_activity:
#         now = timezone.now()
#         elapsed_time = (now - last_activity).total_seconds()
#         if elapsed_time > settings.SESSION_COOKIE_AGE:
#             return redirect('logout')  # Redirect to your logout view or URL
#     request.session['last_activity'] = timezone.now()

