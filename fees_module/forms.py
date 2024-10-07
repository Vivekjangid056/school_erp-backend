from django import forms

from accounts.models import AcademicSession, InstituteBranch
from institute.models import Standard
from .models import FeeStructure, PaymentSchedule, StudentFeePayment

# class StudentFeePaymentForm(forms.ModelForm):
#     class Meta:
#         model = StudentFeePayment
#         fields = ['student', 'installment', 'amount_paid', 'payment_date']
        
#         widgets = {
#             'payment_date': forms.DateInput(attrs={'type': 'date'}),
#         }
        


class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['standard', 'total_fee']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            self.fields['standard'].queryset = Standard.objects.filter(institute=self.user.institute_id.first(), branch = active_branch)

class PaymentScheduleForm(forms.ModelForm):
    class Meta:
        model = PaymentSchedule
        fields = ['student_fee_payment', 'amount_paid', 'payment_date','due_amount','payment_due_date']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentFeePaymentForm(forms.ModelForm):        # ui side its installement Schedule
    class Meta:
        model = StudentFeePayment
        fields = ['student', 'fee_structure', 'paying_amount', 'installment_frequency']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            active_session = AcademicSession.objects.get(pk=self.session.get('session_id'))
            self.fields['fee_structure'].queryset = FeeStructure.objects.filter(branch = active_branch, session = active_session)