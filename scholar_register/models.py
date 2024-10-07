from django.db import models
from django.core.validators import RegexValidator
from accounts.models import *
from institute.models import Caste, Category, ChildStatus, DiscountScheme, House, Medium, MotherToungue, Nationality, PaymentMode, Religion, Section, Standard, StudentType, Subjects
from teacher_management.models import Employee
# Create your models here.

class StudentParents(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "student_parent_id")
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE, related_name="student_parent_institute_id")
    fathers_name = models.CharField(max_length=255)
    fathers_email = models.CharField(max_length=255,blank=True) #optional
    fathers_mob_no = models.CharField(max_length=255)
    fathers_occupation = models.CharField(max_length=255,blank=True) #optional
    fathers_aadhar_no = models.CharField(max_length=255,blank=True) #optional
    father_annual_income = models.CharField(max_length=255,blank=True) #optional
    father_qualification = models.CharField(max_length=255,blank=True) #optional
    father_pan_no = models.CharField(max_length=255,blank=True) #optional
    mothers_name = models.CharField(max_length=255)
    mothers_email = models.CharField(max_length=255,blank=True) #optional
    mothers_mob_no = models.CharField(max_length=255,blank=True) #optional
    mothers_occupation = models.CharField(max_length=255,blank=True) #optional
    mothers_aadhar_no = models.CharField(max_length=255,blank=True) #optional
    mother_annual_income = models.CharField(max_length=255,blank=True) #optional
    mother_qualification = models.CharField(max_length=255,blank=True) #optional
    mother_pan_no = models.CharField(max_length=255,blank=True) #optional
    guardian_name = models.CharField(max_length=255,blank=True)  #optional
    guardian_mobile = models.CharField(max_length=255,blank=True)  #optional
    guardian_relation = models.CharField(max_length=255,blank=True)  #optional
    fee_deposited_by = models.CharField(max_length=255,blank=True)  #optional
    sms_mob_no = models.CharField(max_length=255,blank=True)  #optional
    student_type = models.ForeignKey(StudentType,on_delete=models.CASCADE) 
    child_status = models.ForeignKey(ChildStatus,on_delete=models.CASCADE) 
    discount_scheme = models.ForeignKey(DiscountScheme,on_delete=models.CASCADE)

class StudentProfile(models.Model):
    
    STREAM_CHOICES = (
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('maths', 'Maths'),
        ('arts', 'Arts')
    )
    
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    )
    
    AREA_CHOICES = (
        ('rural','Rural'),
        ('urban','Urban'),
    )
    
    DISABLITY_CHOICES = (
        ('NOT APPLICABLE','NOT APPLICABLE'),
        ('BLINDNESS','BLINDNESS'),
        ('LOW VISION','LOW VISION'),
        ('HEARING','HEARING'),
        ('AUTISM','AUTISM'),
        ('MENTAL RETARDNESS','MENTAL RETARDNESS'),
        ('LEARNING DISABLITY','LEARNING DISABLITY'),
        ('CEREBRAL PALSY','CEREBRAL PALSY'),
        ('MULTIPLE DISABLITIES','MULTIPLE DISABLITIESY'),
        ('SPEECH','SPEECH'),
    )
    
    BLOOD_GROUPS = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB- ',' AB-'),
        ('O+ ',' O+'),
        ('O- ',' O-')
    )

    parent = models.ForeignKey(StudentParents, on_delete = models.CASCADE, related_name='student_id')
    branch = models.ForeignKey(InstituteBranch, on_delete = models.CASCADE, related_name = "student_branch")
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='student_profile_session')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True, null=True) #optional
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES)
    dob = models.DateField()
    caste = models.ForeignKey(Caste,on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    mother_tongue = models.ForeignKey(MotherToungue,on_delete=models.CASCADE)
    form_no = models.BigIntegerField()
    date_of_admission = models.DateField()
    registration_date = models.DateField()
    stream = models.CharField(max_length=100,choices=STREAM_CHOICES,blank=True,null=True) #optional
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date_of_deactivae = models.DateField(blank=True, null=True) #optional
    rte = models.BooleanField(default=False)
    bpl = models.BooleanField(default=False)
    # basic info
    roll_number = models.CharField(max_length=10)
    prefix = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    sr_no = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=255)
    admission_no = models.BigIntegerField()
    enroll_no = models.BigIntegerField()
    student_aadhar = models.CharField(blank=True,max_length=100) #optional
    medium = models.ForeignKey(Medium,on_delete=models.CASCADE)
    rural_or_urban = models.CharField(choices=AREA_CHOICES)
    disablity_type = models.CharField(choices=DISABLITY_CHOICES)
    blood_group = models.CharField(choices=BLOOD_GROUPS)
    house_name = models.ForeignKey(House,on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=255,blank=True,null=True) #optional
    staff_refrence = models.CharField(max_length=255,blank=True,null=True)  #optional
    admission_confirm_date = models.DateField(blank=True, null=True) #optional
    board_type = models.CharField(max_length=255)
    #  address info
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255,blank=True,null=True) #optional
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(regex='^\d{6}$', message='PIN must be 6 digits.')
        ]
    )
    
    # previous school info
    
    previous_school_name = models.CharField(max_length=255,blank=True,null=True) #optional
    previous_school_address = models.CharField(max_length=255,blank=True,null=True) #optional
    reason_of_leaving = models.CharField(max_length=255,blank=True,null=True) #optional
    previous_year = models.CharField(max_length=255,blank=True,null=True) #optional
    previous_class = models.CharField(max_length=255,blank=True,null=True) #optional
    obtain_marks = models.IntegerField(blank=True,null=True) #optional
    maximum_marks = models.IntegerField(blank=True,null=True) #optional
    percentage = models.FloatField(blank=True,null=True) #optional
    result = models.CharField(max_length=10,blank=True,null=True) #optional
    previous_school_board = models.CharField(max_length=100,blank=True,null=True) #optional
    previous_school_rollNo = models.CharField(max_length=100,blank=True,null=True) #optional
    previous_school_class = models.CharField(max_length=100,blank=True,null=True) #optional
    third_lang_studied = models.CharField(max_length=100,blank=True,null=True) #optional
    
    student_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    fathers_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    mothers_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    guardians_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    
    # moneyyyy
    caution_money = models.IntegerField()
    caution_money_reciept_no = models.CharField(max_length=255,blank=True,null=True) #optional
    caution_money_reciept_date = models.DateField(null=True, blank=True) #optional
    counsellor_name = models.CharField(max_length=255)
    remark = models.CharField(max_length=255,blank=True,null=True) #optional
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reg_no}"


class Attendance(models.Model):
    session = models.ForeignKey(AcademicSession, on_delete= models.CASCADE, related_name = 'ttendance_session')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='attendance_branch')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'attendance_student')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='attendance_subject')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='attendance_standard')
    date = models.DateField()
    present = models.BooleanField(default=False)
    absent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} - {self.subject.name} - {self.date} - {self.present}"
    
class StudentLeaveApplication(models.Model):
    institute = models.ForeignKey(Institute, on_delete= models.CASCADE, related_name = 'leave_application_institute')
    branch = models.ForeignKey(InstituteBranch, on_delete= models.CASCADE, related_name = 'leave_application_branch')
    session = models.ForeignKey(AcademicSession, on_delete= models.CASCADE, related_name = 'leave_application_session')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'leave_application_student')
    checked_by = models.ForeignKey(Employee, on_delete=models.CASCADE , null=True, blank=True, related_name="leave_application_teacher")
    start_date= models.DateField()
    end_date = models.DateField()
    leaving_reason = models.TextField(max_length=500)
    attachment = models.FileField(upload_to='documents/' ,max_length=255, null=True, blank=True)
    is_approved = models.BooleanField(default=False)


class StudentComplaintsOrSuggestions(models.Model):

    request_choices = (
        ('suggestion','Suggestion'),
        ('complaint','Complaint'),
    )

    suggestion_choices = (
        ('academic','Academic'),
        ('Non Academic','Non-Academic'),
    )
    institute = models.ForeignKey(Institute, on_delete= models.CASCADE, related_name = 'student_complaint_institute')
    branch = models.ForeignKey(InstituteBranch, on_delete= models.CASCADE, related_name = 'student_complaint_branch')
    session = models.ForeignKey(AcademicSession, on_delete= models.CASCADE, related_name = 'student_complaint_session')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name = 'student_complaint_student')
    request_type = models.CharField(max_length=200, choices=request_choices)
    suggestion_type = models.CharField(max_length=200, choices=suggestion_choices)
    query= models.TextField(max_length=1000)

from teacher_management.models import Assignments
class AssignmentSubmission(models.Model):
    Status_Choices = (
        ('Pending', 'pending'),
        ('Approved', 'approved'),
        ('Reject', 'reject'),
        ('Submitted', 'submitted')
    )
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='assignment_submission_institute')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='assignment_submission_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='assignment_submission_session')
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='assignment_submission_assignment')
    reviewed_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignment_submission_employee', null=True, blank=True)
    student= models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='assignment_submission_student', null=True, blank=True)
    status = models.CharField(max_length=30, choices=Status_Choices, default="pending")
    remarks = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    attachment = models.FileField(upload_to='documents/', max_length=100, null=True, blank=True)