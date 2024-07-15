from django.db import models
from django.core.validators import RegexValidator

from institute.models import Category
from teacher_management.models import Employee, LmDepartmentMaster, LmDesignationMaster

# Create your models here.

class HrInterview(models.Model):
    
    MALE = '1'
    FEMALE = '2'
    OTHER = '3'
    MARRIED = '4'
    SINGLE = '5'
    WIDOWED = '7'
    SEPARATED = '8'
    YES = '9'
    NO = '10'
    PROCESS = '11'
    SELECT = '12'
    REJECT = '13'
    
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES =[
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (WIDOWED, 'Widowed'),
        (SEPARATED, 'Separated')
    ]
    
    RATINGS = [(i , str(i)) for i in range(1,11)]
    
    SELECTION_FOR_NEXT_RD = [
        (YES,'YES'),
        (NO,'NO')
    ]
    
    STATUS_CHOICES = [
        (PROCESS , 'PROCESS'),
        (SELECT , 'SELECT'),
        (REJECT , 'REJECT')
    ]
    
    # ================ General Information =============
    
    interview_no = models.IntegerField()
    interview_date = models.DateField()
    reference = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, related_name='hr_interviews_reference') #optional
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20, blank=True) #optional
    last_name = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES) 
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    current_salary = models.IntegerField()
    expected_salary = models.IntegerField()
    department = models.ForeignKey(LmDepartmentMaster, on_delete=models.CASCADE)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES)
    designation = models.ForeignKey(LmDesignationMaster, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='images/',blank=True,null=True)  #optional
    
    # ============== CONTACT INFO ===========================
    
    current_address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=40)
    pin = models.CharField(
        max_length=6, 
        validators=[
            RegexValidator(regex='^\d{6}$', message='PIN must be 6 digits.')
        ]
    )
    mobile = models.CharField(max_length=12)
    mobile2 = models.CharField(max_length=12, blank=True)  #optional
    email = models.EmailField()
    
    # ===================== Qualification  Info ==========================  
    
    
    
    # ======================== Previous Company Details =================== 
    
    company_name = models.CharField(max_length=255)
    prev_comp_hr_no = models.CharField(max_length=20)
    work_profile = models.CharField(max_length=255)
    joining_date = models.DateField()
    leaving_date = models.DateField(max_length=255)
    leaving_reason = models.CharField(max_length=255)
    salary = models.IntegerField()
    
    # = = = = = = = = = = = = = = = = Feedback = = = = = = = = = = = = = = = = =
    
    recommendation_positive = models.BooleanField(default=False)
    recommendation_negative = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATINGS)
    select_for_next_round = models.CharField(choices=SELECTION_FOR_NEXT_RD)
    assign = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='hr_interviews_assign')
    date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES)
    overall_comment = models.CharField(max_length=255)
    remark = models.CharField(max_length=100)