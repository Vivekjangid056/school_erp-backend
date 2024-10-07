from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from .models import *


# =============================== views for list_master CRUD ===============================
def category_master_list(request):
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return LmCategoryMaster.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return LmCategoryMaster.objects.none()
    data = LmCategoryMaster.objects.filter(
        branch=active_branch)
    context = {
        'data': data
    }
    print(data)
    return render(request, 'list_master/category_master_list.html', context=context)


class AddCategoryMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmCategoryMasterForm
    success_url = reverse_lazy('teacher:category_master_list')

    def form_valid(self, form):
        category = form.save(commit=False)
        institute = self.request.user.institute_id.first()
        session = self.request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        branch = self.request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        if not active_session:
            messages.warning(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        
        if not active_branch:
            messages.warning(self.request, "No active branch found. Please create or activate a branch.")
            return self.form_invalid(form)
        category.institute = institute
        category.branch = active_branch
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)


class updateMasterCategory(UpdateView):
    model = LmCategoryMaster
    template_name = "list_master/list_master_form.html"
    form_class = LmCategoryMasterForm
    success_url = reverse_lazy('teacher:category_master_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the institute related to the user
        institute = self.request.user.institute_id.first()

        # Fetch the branches related to the user's institute
        branches = InstituteBranch.objects.filter(institute=institute)
        print(branches)

        # Add branches to the context
        context['branches'] = branches
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class deleteMasterCategory(DeleteView):
    model = LmCategoryMaster
    success_url = reverse_lazy('teacher:category_master_list')

# ============================== designation views CRUD ===============================


def designation_master_list(request):
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return LmDesignationMaster.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return LmDesignationMaster.objects.none()
    data = LmDesignationMaster.objects.filter(
        branch=active_branch)
    context = {
        'data': data
    }
    return render(request, "list_master/designation_master_list.html", context=context)


class CreateDesignationMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDesignationMasterForm
    success_url = reverse_lazy('teacher:designation_master_list')

    def form_valid(self, form):
        designation = form.save(commit=False)
        user = self.request.user
        institute = Institute.objects.get(user_id=user)
        session = self.request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        branch = self.request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        if not active_session:
            messages.warning(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        
        if not active_branch:
            messages.warning(self.request, "No active branch found. Please create or activate a branch.")
            return self.form_invalid(form)
        designation.institute = institute
        designation.branch = active_branch
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)


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
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)
    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return LmDepartmentMaster.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return LmDepartmentMaster.objects.none()
    data = LmDepartmentMaster.objects.filter(
        branch=active_branch)
    context = {
        'data': data
    }
    return render(request, "list_master/department_master.html", context=context)


class CreateDepartmentMaster(CreateView):
    template_name = "list_master/list_master_form.html"
    form_class = LmDepartmentMasterForm
    success_url = reverse_lazy('teacher:department_master_list')

    def form_valid(self, form):
        department = form.save(commit=False)
        user = self.request.user
        institute = Institute.objects.get(user_id=user)
        session = self.request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        branch = self.request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        if not active_session:
            messages.warning(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        
        if not active_branch:
            messages.warning(self.request, "No active branch found. Please create or activate a branch.")
            return self.form_invalid(form)
        department.institute = institute
        department.branch = active_branch
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)


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


def attendance_type_list(request):
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return LmAttendanceType.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return LmAttendanceType.objects.none()

    data = LmAttendanceType.objects.filter(
        branch=active_branch)
    context = {
        'data': data
    }
    return render(request, "list_master/attendance_type_list.html", context=context)


class CreateAttendanceType(CreateView):
    template_name = "list_master/attendance_type_create.html"
    form_class = LmAttendanceTypeForm
    success_url = reverse_lazy('teacher:attendance_type_list')

    def form_valid(self, form):
        user = self.request.user
        institute = Institute.objects.get(user_id=user)
        session = self.request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        branch = self.request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        if not active_session:
            messages.warning(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        
        if not active_branch:
            messages.warning(self.request, "No active branch found. Please create or activate a branch.")
            return self.form_invalid(form)
        attendance_type = form.save(commit=False)
        attendance_type.institute=institute
        attendance_type.branch = active_branch
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)


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
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return LmHolidayList.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        return LmHolidayList.objects.none()
    data = LmHolidayList.objects.filter(
        branch=active_branch, session=active_session)
    context = {
        'data': data
    }
    return render(request, "list_master/holiday_list.html", context=context)


class CreateHolidayList(CreateView):
    template_name = "list_master/holiday_list_create.html"
    form_class = LmHolidayListForm
    success_url = reverse_lazy('teacher:holiday_list')

    def form_valid(self, form):
        user = self.request.user
        institute = Institute.objects.get(user_id=user)
        session = self.request.session.get('session_id')
        active_session = AcademicSession.objects.get(pk=session)
        branch = self.request.session.get('branch_id')
        active_branch = InstituteBranch.objects.get(pk=branch)
        if not active_session:
            messages.warning(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        
        if not active_branch:
            messages.warning(self.request, "No active branch found. Please create or activate a branch.")
            return self.form_invalid(form)
        holiday = form.save(commit=False)
        holiday.institute = institute
        holiday.branch = active_branch
        holiday.session = active_session
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)


class UpdateHolidayList(UpdateView):
    template_name = "list_master/holiday_list_update.html"
    model = LmHolidayList
    form_class = LmHolidayListForm
    success_url = reverse_lazy('teacher:holiday_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class DeleteHolidayList(DeleteView):


class DeleteHolidayList(DeleteView):
    model = LmHolidayList
    success_url = reverse_lazy('teacher:holiday_list')

# ============================== Employee Master CRUD ================================


def employee_create_view(request):
    institute = request.user.institute_id.first()
    print(":::::::::::::::::::::::::")

    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES, user=request.user, session=request.session)
        user_form = UserEmployeeForm(request.POST)

        if employee_form.is_valid() and user_form.is_valid():
            try:
                # Get active session and branch
                branch= request.session.get('branch_id')
                active_branch = InstituteBranch.objects.get(pk=branch)
                session= request.session.get('session_id')
                active_session = AcademicSession.objects.get(pk=session)

                # Check for active session
                if not active_session:
                    messages.warning(request, "No active session found. Please activate a session to view Categories.")
                    return render(request, "employees/employee_register.html", {'employee_form': employee_form, 'user_form': user_form})

                # Check for active branch
                if not active_branch:
                    messages.warning(request, "No active Branch found. Please activate a Branch to view Categories.")
                    return render(request, "employees/employee_register.html", {'employee_form': employee_form, 'user_form': user_form})

                # Save the user form
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data["password1"])
                user.save()

                # Save the employee form
                employee = employee_form.save(commit=False)
                employee.user = user  # Assign the saved User instance
                employee.institute = institute
                employee.session = active_session
                employee.branch = active_branch
                employee_form.save()  # Save the employee instance

                return redirect('teacher:list_of_employees')

            except Exception as e:
                print(f"Error saving form: {e}")
                messages.error(request, f"Error: {e}")

        else:
            print(employee_form.errors)
            print(user_form.errors)
    else:
        employee_form = EmployeeForm(user=request.user, session=request.session)
        user_form = UserEmployeeForm()

    context = {
        'employee_form': employee_form,
        'user_form': user_form
    }

    return render(request, "employees/employee_register.html", context=context)



class EmployeesList(ListView):
    template_name = "employees/employee_list.html"
    model = Employee
    context_object_name = 'employees_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            session = self.request.session.get('session_id')
            active_session = AcademicSession.objects.get(pk=session)
            branch = self.request.session.get('branch_id')
            active_branch = InstituteBranch.objects.get(pk=branch)

            if not active_session:
                messages.warning(
                    self.request, "No active session found. Please activate a session to view Categories.")
                return Employee.objects.none()

            if not active_branch:
                messages.warning(
                    self.request, "No active Branch found. Please activate a Branch to view Categories.")
                return Employee.objects.none()
            queryset = queryset.filter(
                branch=active_branch, session=active_session)
            print(queryset)
        return queryset


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    user = get_object_or_404(User, pk = employee.user.pk)
    if request.method == "POST":
        employee_form = EmployeeForm(
            request.POST, request.FILES, instance=employee)
        user_form= UserEmployeeForm(request.POST, instance=user)
        if employee_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password1"])
            user.save()

            employee = employee_form.save(commit=False)
            employee.user= user
            employee_form.save()
            # Replace with your actual redirect URL
            return redirect('teacher:list_of_employees')
    else:
        employee_form = EmployeeForm(instance=employee, session=request.session)
        user_form = UserEmployeeForm(instance = user)

        context={
            'employee_form':employee_form,
            'user_form':user_form
        }
    return render(request, 'employees/employee_register.html', context=context)


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('teacher:list_of_employees')


# <---------------Attendance for employees----------------------->

def employee_attendance_view(request):
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return EmployeeAttendance.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        EmployeeAttendance.objects.none()

    departments = LmDepartmentMaster.objects.filter(
        branch=active_branch, session=active_session)
    
    if request.method == 'POST':
        data = request.POST
        date = data.get('date')
        department_id = data.get('department')

        employees = Employee.objects.filter(department_id=department_id)

        for employee in employees:
            employee_id = employee.id
            attendance_status = data.get(f'attendance_status_{employee_id}')
            present = attendance_status == 'present'
            absent = attendance_status == 'absent'

            EmployeeAttendance.objects.update_or_create(
                branch=active_branch,
                session =active_session,
                employee_id=employee_id,
                date=date,
                defaults={'present': present, 'absent': absent}
            )

        # Redirecting to the list of employees
        return redirect('teacher:employee_attendance_list')
    context = {
        'departments': departments,
    }
    return render(request, 'employee_attendance.html', context)


def fetch_employee_attendance_data(request):
    department_id = request.GET.get('department_id')
    date = request.GET.get('date')

    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return EmployeeAttendance.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        EmployeeAttendance.objects.none()

    employees = Employee.objects.filter(branch=active_branch, session=active_session) if department_id == "all" else Employee.objects.filter(
        branch=active_branch, session=active_session, department_id=department_id)

    attendance_data = []
    for employee in employees:
        attendance_record = EmployeeAttendance.objects.filter(
            branch=active_branch, session=active_session ,employee=employee, date=date).first()
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
    user = request.user
    institute = Institute.objects.get(user_id=user)
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(
            request, "No active session found. Please activate a session to view Categories.")
        return EmployeeAttendance.objects.none()

    if not active_branch:
        messages.warning(
            request, "No active Branch found. Please activate a Branch to view Categories.")
        EmployeeAttendance.objects.none()
    departments = LmDepartmentMaster.objects.filter(
        branch=active_branch, session=active_session)
    return render(request, 'employee_attendance_list.html', {'departments': departments})
