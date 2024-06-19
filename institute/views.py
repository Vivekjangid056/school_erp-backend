from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomUserRegisterForm
from .forms import InstituteForm
from .models import Institute
from django.views.generic import UpdateView, CreateView, DeleteView

# Create your views here.

# def add_institute(request):
#     if request.method == 'POST':
#         form = InstituteForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('institute_list')  # Redirect to a success page
#     else:
#         form = InstituteForm()
    
#     return render(request, 'create.html', {'form': form})


def institute_list(request):
    institutes = Institute.objects.all()
    print(institutes)
    return render(request, 'tables-datatable.html', {'institutes' : institutes})


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    context_object_name = "form"
    template_name = 'update_form.html'
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)
    

class InstituteRegisterView(CreateView):
    template_name = 'institute_register.html'
    form_class = CustomUserRegisterForm
    second_form_class = InstituteForm
    success_url = reverse_lazy('institute:institute_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        profile_form = self.second_form_class(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Handle password setting
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(form=form, profile_form=profile_form)
        )
    

class InstituteDeleteView(DeleteView):
    model = Institute
    template_name = 'institute_delete.html'  # specify your template name
    success_url = reverse_lazy('institute:institute_list')  # specify the URL to redirect after successful deletion