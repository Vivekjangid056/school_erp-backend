from django.shortcuts import render
from .forms import InstituteForm
from .models import Institute

# Create your views here.

def add_institute(request):
    form = InstituteForm
    return render(request, "form.html", {"form" : form})

def institute_list(request):
    institute = Institute.objects.all()
    print(institute)
    return render(request, 'institute_list.html', {'institute' : institute})
