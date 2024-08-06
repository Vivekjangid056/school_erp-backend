from email import message
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from teacher_management.forms import *
from django.views.generic import UpdateView, CreateView, DeleteView, FormView, ListView
from .models import *


# =============================== views for list_master CRUD ===============================
def category_master_list(request):
    institute = Institute.objects.get(user_id = request.user)
    data = LmCategoryMaster.objects.filter(institute_id = institute)
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
        category = form.save(commit = False)
        category.institute= self.request.user.institute_id.first()
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

# ============================== designation views CRUD =============================== 
def designation_master_list(request):
    institute = Institute.objects.get(user_id = request.user)
    data = LmDesignationMaster.objects.filter(institute = institute)
    context = {
        'data': data
    }
    return render(request,"list_master/designation_master_list.html",context=context)

class CreateDesignationMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDesignationMasterForm
    success_url = reverse_lazy('teacher:designation_master_list')
    
    def form_valid(self, form):
        designation = form.save(commit = False)
        designation.institute= self.request.user.institute_id.first()
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
    
# ========================== Department maser views CRUD ==============================
def department_master_list(request):
    institute = Institute.objects.get(user_id = request.user)
    data = LmDepartmentMaster.objects.filter(institute = institute)
    context = {
        'data': data
    }
    return render(request,"list_master/department_master.html",context=context)

class CreateDepartmentMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDepartmentMasterForm
    success_url = reverse_lazy('teacher:department_master_list')
    
    def form_valid(self, form):
        department = form.save(commit = False)
        department.institute= self.request.user.institute_id.first()
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
    
# ================================= attendance type ===================================

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
    
# ============================= holiday list CRUD ================================

def holiday_list(request):
    institute = Institute.objects.get(user_id = request.user)
    data = LmHolidayList.objects.filter(institute = institute)
    context = {
        'data':data
    }
    return render(request,"list_master/holiday_list.html",context=context)

class CreateHolidayList(CreateView):
    template_name = "list_master/holiday_list_create.html"
    form_class = LmHolidayListForm
    success_url = reverse_lazy('teacher:holiday_list')
    
    def form_valid(self,form):
        holiday = form.save(commit=False)
        holiday.institute = self.request.user.institute_id.first()
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


# ============================== Employee Master CRUD ================================
def employee_master_create_view(request):
    if request.method == "POST":
        user = request.user
        form = EmployeeMasterForm(request.POST,request.FILES, user=user)
        if form.is_valid():
            try:
                form.save()
                return redirect('teacher:list_of_employee_master')
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("exception occured", form.errors)
    else:
        print(request.user.institute_id.first().pk)
        form = EmployeeMasterForm()
    
    return render(request, "employees_master/employee_master_register.html", {'form': form})


class EmployeeMasterList(ListView):
    template_name = "employees_master/employee_list.html"
    model = EmployeeMaster
    context_object_name = 'employee_master_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            institute_id = user.institute_id
            queryset = queryset.filter(institute_id=institute_id.first())
            print(queryset)
        return queryset


def employee_master_update(request, pk):
    employee = get_object_or_404(EmployeeMaster, pk=pk)
    if request.method == "POST":
        form = EmployeeMasterForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('teacher:list_of_employee_master')  # Replace with your actual redirect URL
    else:
        form = EmployeeMasterForm(instance=employee)
    return render(request, 'employees_master/employee_master_register.html', {'form': form})


class EmployeeMasterDelete(DeleteView):
    model = EmployeeMaster
    success_url = reverse_lazy('teacher:list_of_employee_master')
    
# class DeleteHolidayList(DeleteView):
class DeleteHolidayList(DeleteView):
    model = LmHolidayList
    success_url = reverse_lazy('teacher:holiday_list')
    
# <---------------Attendance for employees----------------------->

def employee_attendance_view(request):
    departments = LmDepartmentMaster.objects.all()
    if request.method == 'POST':
        data = request.POST
        date = data.get('date')
        department_id = data.get('department')

        employees = EmployeeMaster.objects.filter(department_id=department_id)

        for employee in employees:
            employee_id = employee.id
            attendance_status = data.get(f'attendance_status_{employee_id}')
            present = attendance_status == 'present'
            absent = attendance_status == 'absent'

            EmployeeAttendance.objects.update_or_create(
                employee_id=employee_id,
                date=date,
                defaults={'present': present, 'absent': absent}
            )

        return redirect('teacher:employee_attendance_list')  # Redirecting to the list of employees
    context = {
        'departments': departments,
    }
    return render(request, 'employee_attendance.html', context)

def fetch_employee_attendance_data(request):
    department_id = request.GET.get('department_id')
    date = request.GET.get('date')

    employees = EmployeeMaster.objects.all() if department_id == "all" else EmployeeMaster.objects.filter(department_id=department_id)

    attendance_data = []
    for employee in employees:
        attendance_record = EmployeeAttendance.objects.filter(employee=employee, date=date).first()
        attendance_data.append({
            'id': employee.id,
            'name': f"{employee.first_name} {employee.last_name}",
            'emp_no': employee.emp_no,
            'date': date,
            'present': attendance_record.present if attendance_record else False,
            'absent': attendance_record.absent if attendance_record else False
        })
    return JsonResponse({'attendance_data': attendance_data})


def employee_attendance_list(request):
    departments = LmDepartmentMaster.objects.all()
    return render(request, 'employee_attendance_list.html', {'departments': departments})