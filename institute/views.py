from django.shortcuts import render, redirect
from .forms import InstituteForm
from .models import Institute

# Create your views here.

def add_institute(request):
    if request.method == 'POST':
        form = InstituteForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('institute_list')  # Redirect to a success page
    else:
        form = InstituteForm()
    
    return render(request, 'create.html', {'form': form})

def institute_list(request):
    institute = Institute.objects.all()
    print(institute)
    return render(request, 'tables-datatable.html', {'institute' : institute})
