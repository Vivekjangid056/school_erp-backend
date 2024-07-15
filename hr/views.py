from django.shortcuts import render, redirect , get_object_or_404
from .models import HrInterview
from .forms import HrInterviewForm

# Create your views here.

def interview_list(request):
    interview = HrInterview.objects.all()
    context = {
        'interview':interview
    }
    
    return render (request, 'interview_list.html',context=context)

def interview_register(request):
    if request.method == 'POST':
        interview_form = HrInterviewForm(request.POST, request.FILES)
        
        if interview_form.is_valid():
            try:
                interview = interview_form.save(commit=False)
                interview.save()
                return redirect('hr:list_of_interview')
            except Exception as e:
                print(f"Error saving interview details: {e}")
        else:
            print("Interview form errors:", interview_form.errors)
    else:
        interview_form = HrInterviewForm()
    
    return render(request, 'interview_form.html', {
        'interview_form': interview_form
    })
    
    
def interview_update(request, pk):
        hr_interview = get_object_or_404(HrInterview, pk=pk)
        
        if request.method == 'POST':
            interview_form = HrInterviewForm(request.POST, request.FILES, instance=hr_interview)
            
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