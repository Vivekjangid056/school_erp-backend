from django.db import models
from accounts.models import Institute, AcademicSession, InstituteBranch
from institute.models import Standard
from scholar_register.models import StudentProfile

# Create your models here.


class FeeStructure(models.Model):
    institute = models.ForeignKey(Institute, on_delete= models.CASCADE, related_name = "fee_structure_institute")
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name="fee_structure_session")
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='fee_structure_branch')
    standard = models.OneToOneField(Standard, on_delete=models.CASCADE, related_name='fee_structure_standard')
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.standard.name} - {self.total_fee}"


class StudentFeePayment(models.Model):                 # ui side its installement Schedule
    HALF_YEARLY = 'Half-Yearly'
    Monthly = 'Monthly'
    NoInstallement = 'No Installement'
    INSTALLMENT_FREQUENCY_CHOICES = [
        (HALF_YEARLY, 'Half-Yearly'),
        (Monthly, 'Monthly'),
        (NoInstallement, 'No Installement'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    branch = models.ForeignKey(InstituteBranch, on_delete= models.CASCADE, related_name= 'student_fee_payment_branch')
    session = models.ForeignKey(AcademicSession,on_delete=models.CASCADE, related_name= 'student_fee_payment_session')
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    paying_amount = models.IntegerField()
    installment_frequency = models.CharField(max_length=20, choices=INSTALLMENT_FREQUENCY_CHOICES)

    def __str__(self):
        return f"{self.student.first_name} - {self.fee_structure.standard} - {self.installment_frequency}"


    @property
    def total_installments(self):
        if self.installment_frequency == self.HALF_YEARLY:
            return 2
        elif self.installment_frequency == self.MONTHLY:
            return 12
        return 0
    
    @property
    def installment_amount(self):
        if self.total_installments > 0:
            return self.fee_structure.total_fee / self.total_installments
        return self.fee_structure.total_fee
    

class PaymentSchedule(models.Model):
    institute = models.ForeignKey(Institute, on_delete= models.CASCADE, related_name = 'payment_schedule')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='payment_schedule')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name = 'payment_schedule_branch')
    student_fee_payment = models.ForeignKey(StudentFeePayment, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.IntegerField()
    due_amount = models.IntegerField(blank=True, null=True)
    payment_date = models.DateField()
    payment_due_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.student_fee_payment.student} - {self.amount_paid} on {self.payment_date}"

   