from django.contrib import messages
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from accounts.models import AcademicSession, InstituteBranch
from fees_module.forms import FeeStructureForm, PaymentScheduleForm, StudentFeePaymentForm
from fees_module.models import FeeStructure, PaymentSchedule, StudentFeePayment
from django.views.decorators.http import require_GET
from django.views.generic import CreateView, ListView, UpdateView, DeleteView




# <!------------------------FEE STRUCTURE CRUD___________________>

class FeeStructureCreateView(CreateView):
    model = FeeStructure
    form_class = FeeStructureForm
    template_name = 'fee_structure/structure_create.html'
    success_url = reverse_lazy('fees_module:list_fee_structure')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        fees = form.save(commit=False)
    
        # Get the active session
        institute = self.request.user.institute_id.first()
        active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
        active_branch = InstituteBranch.objects.filter(institute = institute, is_active=True).first()

        if not active_session:
            messages.error(self.request, "No active session found. Please create or activate a session.")
            return self.form_invalid(form)
        if not active_branch:
            messages.error(self.request, "No active branch found. Please create or activate a branch.")
    
        # Assign the institute and session fields
        fees.institute = institute
        fees.session = active_session
        fees.branch = active_branch
        fees.save()
    
        messages.success(self.request, "Fee structure created successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error in your form. Please check and try again.")
        return super().form_invalid(form)

class FeeStructureListView(ListView):
    model = FeeStructure
    template_name = 'fee_structure/structure_list.html'
    context_object_name = 'fee_structure_list'
    
    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            institute = user.institute_id.first()
            active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
            active_branch = InstituteBranch.objects.filter(institute=institute, is_active=True).first()

            if not active_session:
                messages.warning(self.request, "No active session found. Please activate a session to view Fee Structure.")
                return FeeStructure.objects.none()

            if not active_branch:
                messages.error(self.request, "No active branch found. Please create or activate a branch.")
                return FeeStructure.objects.none()

            # Filter by active session and active branch
            queryset = FeeStructure.objects.filter(institute=institute, session=active_session, branch=active_branch)
            return queryset

        return FeeStructure.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_session'] = AcademicSession.objects.filter(
            institute=self.request.user.institute_id.first(), is_active=True).first()
        context['active_branch'] = InstituteBranch.objects.filter(
            institute=self.request.user.institute_id.first(), is_active=True).first()
        return context

class FeeStructureUpdateView(UpdateView):
    model = FeeStructure
    form_class = FeeStructureForm
    context_object_name = 'form'
    template_name = 'fee_structure/structure_create.html'
    success_url = reverse_lazy('fees_module:list_fee_structure')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Fetch the institute related to the user
        institute = user.institute_id.first()  # Assuming the related name is `institute_id`

        # Fetch the branches related to the user's institute
        branches = InstituteBranch.objects.filter(institute=institute)
        print(branches)

        # Add branches to the context
        context['branches'] = branches
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "signature updated successfully!")
        return super().form_valid(form)

class FeeStructureDeleteView(DeleteView):
    model = FeeStructure
    success_url = reverse_lazy('fees_module:list_fee_structure')
    
# <_____________________________Payment Schedule VIEWS__________________________>

def payment_schedule_create(request):
    if request.method == 'POST':
        form = PaymentScheduleForm(request.POST)
        if form.is_valid():
            payment_schedule = form.save(commit=False)
            
            # Get the active session
            institute = request.user.institute_id.first()
            active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
            active_branch = InstituteBranch.objects.filter(institute=institute, is_active=True).first()

            if not active_session:
                messages.error(request, "No active session found. Please create or activate a session.")
                return render(request, 'payment_schedule/create_schedule.html', {'form': form})
            
            if not active_branch:
                messages.error(request, "No active branch found. Please create or activate a branch.")

            # Assign the institute and session fields
            payment_schedule.institute = institute
            payment_schedule.session = active_session
            payment_schedule.branch = active_branch
            payment_schedule.save()

            messages.success(request, "Payment schedule created successfully.")
            return redirect('fees_module:list_payment_schedule')
    else:
        form = PaymentScheduleForm()

    student_fee_payment_detail_url = reverse('fees_module:student_fee_payment_detail', kwargs={'id': 0})[:-2]

    context = {
        'form': form, 
        'student_fee_payment_detail_url': student_fee_payment_detail_url
    }
    return render(request, 'payment_schedule/create_schedule.html', context)
    
class PaymentScheduleListView(ListView):
    model = PaymentSchedule
    template_name = 'payment_schedule/list_schedule.html'
    context_object_name = 'payment_schedules'

    def get_queryset(self):
        # Get the active session and branch for the current user's institute
        institute = self.request.user.institute_id.first()
        active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
        active_branch = InstituteBranch.objects.filter(institute=institute, is_active=True).first()

        # Handle case where there's no active session or branch
        if not active_session:
            messages.warning(self.request, "No active session found. Please activate a session to view payment schedules.")
            return PaymentSchedule.objects.none()

        if not active_branch:
            messages.error(self.request, "No active branch found. Please create or activate a branch.")
            return PaymentSchedule.objects.none()

        # Return only the payment schedules for the active session and active branch
        return PaymentSchedule.objects.filter(institute=institute, session=active_session, branch=active_branch)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        institute = self.request.user.institute_id.first()
        active_session = AcademicSession.objects.filter(institute=institute, is_active=True).first()
        active_branch = InstituteBranch.objects.filter(institute=institute, is_active=True).first()

        context['active_session'] = active_session
        context['active_branch'] = active_branch

        return context

class PaymentScheduleUpdateView(UpdateView):
    model = PaymentSchedule
    form_class = PaymentScheduleForm
    context_object_name = 'form'
    template_name = 'payment_schedule/create_schedule.html'
    success_url = reverse_lazy('fees_module:list_payment_schedule')

    def form_valid(self, form):
        messages.success(self.request, "signature updated successfully!")
        return super().form_valid(form)

class PaymentScheduleDeleteView(DeleteView):
    model = PaymentSchedule
    success_url = reverse_lazy('fees_module:list_payment_schedule')
    
    
#  <__________________Installement Views __________________________>  
# create student fee payment
def create_student_fee_payment(request):
    if request.method == 'POST':
        form = StudentFeePaymentForm(request.POST, user = request.user)
        if form.is_valid():
            form.save()
            return redirect('fees_module:student_fee_payment_list')
    else:
        form = StudentFeePaymentForm(user = request.user)
    return render(request, 'create_student_fee_payment.html', {'form': form})

# List Student Fee Payments
def student_fee_payment_list(request):
    student_fee_payments = StudentFeePayment.objects.all()
    return render(request, 'student_fee_payment_list.html', {'student_fee_payments': student_fee_payments})

# update student fee payment

def update_student_fee_payment(request, pk):
    student_fee_payment = StudentFeePayment.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentFeePaymentForm(request.POST, instance=student_fee_payment)
        if form.is_valid():
            form.save()
            return redirect('fees_module:student_fee_payment_list')
    else:
        form = StudentFeePaymentForm(instance=student_fee_payment)
    return render(request, 'create_student_fee_payment.html', {'form': form})

# delete student fee payment

def delete_student_fee_payment(request, pk):
    student_fee_payment = StudentFeePayment.objects.get(pk=pk)
    if request.method == 'POST':
        student_fee_payment.delete()
        return redirect('fees_module:student_fee_payment_list')
    return render(request, 'delete_student_fee_payment.html', {'student_fee_payment': student_fee_payment})


class StudentFeePaymentDetailView(View):
    def get(self, request, id):
        try:
            student_fee_payment = StudentFeePayment.objects.get(id=id)
            data = {
                'installment_frequency': student_fee_payment.installment_frequency,
                'fee_structure': {
                    'total_fee': student_fee_payment.fee_structure.total_fee,
                },
            }
            return JsonResponse(data)
        except StudentFeePayment.DoesNotExist:
            return JsonResponse({'error': 'StudentFeePayment not found'}, status=404)