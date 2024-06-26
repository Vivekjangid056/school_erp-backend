from email import message
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from teacher_management.forms import LmAttendanceTypeForm, LmCategoryMasterForm, LmDepartmentMasterForm, LmDesignationMasterForm, LmHolidayListForm
from django.views.generic import UpdateView, CreateView, DeleteView, FormView, ListView
from .models import *


# Create your views here.



# views for list_master {C.R.U.D}
def category_master_list(request):
    data = LmCategoryMaster.objects.all()
    context = {
        'data' : data
    }
    print(data)
    return render(request, 'list_master/category_master_list.html', context=context)

class AddMasterCategory(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmCategoryMasterForm
    success_url = reverse_lazy('teacher:category_master_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class updateMasterCategory(UpdateView):
    model = LmCategoryMaster
    template_name = "list_master/list_master_form.html"
    form_class = LmCategoryMasterForm
    success_url = reverse_lazy('teacher:category_master_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class deleteMasterCategory(DeleteView):
    model = LmCategoryMaster
    success_url = reverse_lazy('teacher:category_master_list')    

# designation views {c.r.u.d} 
def designation_master_list(request):
    data = LmDesignationMaster.objects.all()
    context = {
        'data': data
    }
    return render(request,"list_master/designation_master_list.html",context=context)

class CreateDesignationMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDesignationMasterForm
    success_url = reverse_lazy('teacher:designation_master_list')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class UpdateDesignationMaster(UpdateView):
    template_name = "list_master/list_master_form.html"
    model = LmDesignationMaster
    form_class = LmDesignationMasterForm
    success_url = reverse_lazy('teacher:designation_master_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
       
class DeleteDesignationMaster(DeleteView):
    model = LmDesignationMaster
    success_url = reverse_lazy('teacher:designation_master_list')    
    
# Department maser views {c.r.u.d} 
def department_master_list(request):
    data = LmDepartmentMaster.objects.all()
    context = {
        'data': data
    }
    return render(request,"list_master/department_master.html",context=context)

class CreateDepartmentMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDepartmentMasterForm
    success_url = reverse_lazy('teacher:department_master_list')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class updateDepartmentMaster(UpdateView):
    template_name = "list_master/list_master_form.html"
    model = LmDepartmentMaster
    form_class = LmDepartmentMasterForm
    success_url = reverse_lazy('teacher:department_master_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class deleteDepartmentMaster(DeleteView):
    model = LmDepartmentMaster
    success_url = reverse_lazy('teacher:department_master_list')   
    
#     attendance type

def attendance_type(request):
    data = LmAttendanceType.objects.all()
    context = {
        'data': data
    }
    return render(request,"list_master/attendance_type_list.html",context=context)

class CreateAttendanceType(CreateView):
    template_name = "list_master/attendance_type_create.html"
    form_class = LmAttendanceTypeForm
    success_url = reverse_lazy('teacher:attendance_type_list')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class EditAttendanceType(UpdateView):
    template_name = "list_master/attendance_type_update.html"
    model = LmAttendanceType
    form_class = LmAttendanceTypeForm
    success_url = reverse_lazy('teacher:attendance_type_list')    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class DeleteAttendanceType(DeleteView):
    model = LmAttendanceType
    success_url = reverse_lazy('teacher:attendance_type_list')    
    
#holiday list c.r.u.d

def holiday_list(request):
    data = LmHolidayList.objects.all()
    context = {
        'data':data
    }
    return render(request,"list_master/holiday_list.html",context=context)

class CreateHolidayList(CreateView):
    template_name = "list_master/holiday_list_create.html"
    form_class = LmHolidayListForm
    success_url = reverse_lazy('teacher:holiday_list')
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class UpdateHolidayList(UpdateView):
    template_name = "list_master/holiday_list_update.html"
    model = LmHolidayList
    form_class = LmHolidayListForm
    success_url = reverse_lazy('teacher:holiday_list')    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    