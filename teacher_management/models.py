from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField
from institute.models import *
from institute.models import Category
from accounts.models import *

# Create your models here.


class LmCategoryMaster(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name= 'lmcategory')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name = 'lm_category_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name = 'lm_category_session')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LmDesignationMaster(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name= 'lmdesignation')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name = 'lm_designation_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name = 'lm_designation_session')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LmDepartmentMaster(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name= 'lmdepartment')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name = 'lm_department_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name = 'lm_department_session')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
        
class LmAttendanceType(models.Model):
    
    PRESENT = 'Present'
    ABSENT = 'Absent'
    LEAVE = 'Leave'
    
    NATURE_CHOICES = [
        (PRESENT,'Present'),
        (ABSENT,'Absent'),
        (LEAVE,'Leave'),
    ]
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='lm_attendace_type')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='lm_attendance_type_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='lm_attendance_type_session')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    nature = models.CharField(max_length=100,choices=NATURE_CHOICES,default=PRESENT)
    attendance = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name     
    
class LmHolidayList(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='lmholiday')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='lm_holiday_list_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='lm_holiday_list_session')
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

class EmployeeMaster(models.Model):
    MALE = '1'
    FEMALE = '2'
    OTHER = '3'

    MARRIED = '4'
    SINGLE = '5'
    DIVORCED = '6'
    WIDOWED = '7'
    SEPARATED = '8'

    PART_TIME ='9'
    PERMANENT ='10'
    ACTIVE ='11'

    CASH ='12'
    ONLINE ='13'
    CHEQUE ='14'
    DD ='15'
    UPI ='16'
    CREDIT_CARD ='17'
    DEBIT_CARD = '18'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    MARITAL_STATUS_CHOICES =[
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed'),
        (SEPARATED, 'Separated')
    ]

    EMPLOYEE_STATUS_CHOICES =[
        (PART_TIME, 'Part time'),
        (PERMANENT, 'Permanent'),
        (ACTIVE, 'Active')
    ]

    PAYMENT_MODE_CHOICES = [
        (CASH, 'Cash'),
        (ONLINE, 'Online'),
        (CHEQUE, 'Cheque'),
        (DD, 'DD'),
        (UPI, 'UPI'),
        (CREDIT_CARD, 'Credit Card'),
        (DEBIT_CARD, 'Debit Card')
    ]

    # ========================= Basic Informations ========================================
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='institute')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='employee_master_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='employee_master_session')
    prefix = models.CharField(max_length=10)
    emp_no = models.CharField(max_length=10)
    join_date = models.DateField(auto_created=True)
    blood_group = models.CharField(max_length=10, null=True, blank= True)
    gender = models.CharField(choices= GENDER_CHOICES, default=MALE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length= 200)
    mother_name = models.CharField(max_length= 200)
    date_of_birth = models.DateField()
    category_cast= models.ForeignKey(Category, on_delete= models.CASCADE)
    pan_no = models.CharField(max_length= 10)
    aadhar_no = models.CharField(max_length= 12)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, default= SINGLE)
    reliving_reason = models.CharField(max_length= 200, blank=True, null=True)
    reliving_date = models.DateField(blank=True,null=True)
    is_driver = models.BooleanField(default=False)

    # ========================== Contacr Information ======================================
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length= 200, null=True, blank= True)
    city = models.CharField(max_length= 200)
    state = models.CharField(max_length= 200)
    pin = models.CharField(max_length= 6)
    mobile_number = models.CharField(max_length= 200)
    office_contact = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 200)

    # ========================== Official Information =====================================
    department = models.ForeignKey(LmDepartmentMaster, on_delete=models.CASCADE)
    designation = models.ForeignKey(LmDesignationMaster, on_delete=models.CASCADE)
    category = models.ForeignKey(LmCategoryMaster, on_delete=models.CASCADE, related_name='employee_master')
    # Reporting_authority = models.ForeignKey(max_length= 200)
    roll_no_10th = models.CharField(max_length= 200, null=True, blank= True)
    board_year_10th = models.CharField(max_length= 200, null=True, blank= True)
    school_location = models.CharField(max_length= 200, null=True, blank= True)
    employee_status = models.CharField(choices=EMPLOYEE_STATUS_CHOICES, default=PERMANENT)
    Pass_port_no = models.CharField(max_length= 200, null=True, blank= True)
    pass_port_end_date = models.DateField(null=True, blank= True)
    punch_machine_id = models.CharField(max_length= 200)

    # =========================== Document Information ====================================
    bank_account_no = models.CharField(max_length= 50)
    ifsc_code = models.CharField(max_length= 20)
    Banke_name = models.CharField(max_length= 200)
    branch_address = models.CharField(max_length= 200)
    payment_mode = models.CharField(choices=PAYMENT_MODE_CHOICES, default=CASH)
    qualification = models.CharField(max_length= 200)
    experience = models.CharField(max_length= 200)
    experience_detail = models.CharField(max_length= 200)
    uan_no = models.CharField(max_length= 200)
    pf_no = models.CharField(max_length= 200)
    esi_no = models.CharField(max_length= 200)
    apply_maximum_pf_limit = models.BooleanField(default=False)

    # ============================ License Information ====================================
    driving_license_no = models.CharField(max_length= 200)
    drivint_license_issue_date = models.DateField()
    driving_license_expiry_date = models.DateField()
    driving_license_issue_palace = models.CharField(max_length= 200)
    # employee_level = models.ForeignKey(max_length= 200)
    remarks = models.CharField(max_length= 200)
    employee_image = models.ImageField(upload_to='images/',blank=True,null=True)
    signature_image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f"[{self.first_name} {self.last_name} | Emp No: ({self.prefix}{self.emp_no}) | Father Name : {self.father_name}]"
    
class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='employee_attendance_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='employee_attendance_session')
    date = models.DateField()
    present = models.BooleanField(default=False)    
    absent = models.BooleanField(default=False)    


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name="employee_profile")
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='employee_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='employee_session')
    employee_details = models.OneToOneField(EmployeeMaster, on_delete= models.CASCADE, related_name='employee_profile')
    staff_role =  models.ForeignKey(InstituteRole, on_delete= models.CASCADE)
    middle_name = models.CharField(max_length=100 , blank=True)   #optional
    nick_name = models.CharField(max_length=50,blank=True) #optional
    position = models.CharField(max_length=50,blank=True)   #optional
    confirm_email= models.EmailField(max_length= 200, null=True, blank=True)
    user_image = models.ImageField(upload_to='images/',blank=True,null=True)  #optional
    
    def __str__(self):
        return self.employee_details.first_name