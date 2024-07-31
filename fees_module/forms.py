from django import forms

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
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['standard'].queryset = Standard.objects.filter(institute=self.user.institute_id.first())

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
        fields = ['student', 'fee_structure', 'installment_frequency']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }