from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField
from django.db.models import UniqueConstraint
from accounts.models import Institute, User
from institute.models import Caste, Category, ChildStatus, DiscountScheme, FeeInstallments, House, Medium, MotherToungue, Nationality, PaymentMode, Religion, Section, Standard, StudentType
# Create your models here.

# model for student registration


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

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # institute = models.ForeignKey(Institute, on_delete = models.CASCADE)
    session = models.CharField(max_length=100)
    form_no = models.BigIntegerField()
    date_of_admission = models.DateField()
    registration_date = models.DateField()
    stream = models.CharField(max_length=100,choices=STREAM_CHOICES,blank=True) #optional
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date_of_deactivae = models.DateField(blank=True) #optional
    rte = models.BooleanField(default=False)
    bpl = models.BooleanField(default=False)
    installment_mode = models.ForeignKey(FeeInstallments,on_delete=models.CASCADE)
    # basic info
    prefix = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    sr_no = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=255)
    admission_no = models.BigIntegerField()
    enroll_no = models.BigIntegerField()
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    mother_tongue = models.ForeignKey(MotherToungue,on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100,blank=True) #optional
    gender = models.CharField(choices=GENDER_CHOICES)
    dob = models.DateField()
    student_aadhar = models.CharField(blank=True,max_length=100) #optional
    caste = models.ForeignKey(Caste,on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium,on_delete=models.CASCADE)
    rural_or_urban = models.CharField(choices=AREA_CHOICES)
    disablity_type = models.CharField(choices=DISABLITY_CHOICES)
    blood_group = models.CharField(choices=BLOOD_GROUPS)
    house_name = models.ForeignKey(House,on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=255,blank=True) #optional
    staff_refrence = models.CharField(max_length=255,blank=True)  #optional
    admission_confirm_date = models.DateField(blank=True) #optional
    board_type = models.CharField(max_length=255)
    
    # parent info
    fathers_name = models.CharField(max_length=255)
    fathers_occupation = models.CharField(max_length=255,blank=True) #optional
    fathers_mob_no = models.CharField(max_length=255)
    fathers_email = models.CharField(max_length=255,blank=True) #optional
    mothers_name = models.CharField(max_length=255)
    mothers_occupation = models.CharField(max_length=255,blank=True) #optional
    mothers_mob_no = models.CharField(max_length=255,blank=True) #optional
    mothers_email = models.CharField(max_length=255,blank=True) #optional
    fahers_aadhar_no = models.CharField(max_length=255,blank=True) #optional
    mothers_aadhar_no = models.CharField(max_length=255,blank=True) #optional
    father_annual_income = models.CharField(max_length=255,blank=True) #optional
    mother_annual_income = models.CharField(max_length=255,blank=True) #optional
    father_qualification = models.CharField(max_length=255,blank=True) #optional
    mother_qualification = models.CharField(max_length=255,blank=True) #optional
    father_pan_no = models.CharField(max_length=255,blank=True) #optional
    mother_pan_no = models.CharField(max_length=255,blank=True) #optional
    guardian_name = models.CharField(max_length=255,blank=True)  #optional
    guardian_mobile = models.CharField(max_length=255,blank=True)  #optional
    guardian_relation = models.CharField(max_length=255,blank=True)  #optional
    fee_deposited_by = models.CharField(max_length=255,blank=True)  #optional
    sms_mob_no = models.CharField(max_length=255,blank=True)  #optional
    student_type = models.ForeignKey(StudentType,on_delete=models.CASCADE) 
    child_status = models.ForeignKey(ChildStatus,on_delete=models.CASCADE) 
    discount_scheme = models.ForeignKey(DiscountScheme,on_delete=models.CASCADE)
     
    #  address info
    
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255,blank=True) #optional
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin = models.CharField(
        max_length=6, 
        validators=[
            RegexValidator(regex='^\d{6}$', message='PIN must be 6 digits.')
        ]
    )
    
    # previous school info
    
    previous_school_name = models.CharField(max_length=255,blank=True) #optional
    previous_school_address = models.CharField(max_length=255,blank=True) #optional
    reason_of_leaving = models.CharField(max_length=255,blank=True) #optional
    previous_year = models.CharField(max_length=255,blank=True) #optional
    previous_class = models.CharField(max_length=255,blank=True) #optional
    obtain_marks = models.IntegerField(blank=True) #optional
    maximum_marks = models.IntegerField(blank=True) #optional
    percentage = models.FloatField(blank=True) #optional
    result = models.CharField(max_length=10,blank=True) #optional
    previous_school_board = models.CharField(max_length=100,blank=True) #optional
    previous_school_rollNo = models.CharField(max_length=100,blank=True) #optional
    previous_school_class = models.CharField(max_length=100,blank=True) #optional
    third_lang_studied = models.CharField(max_length=100,blank=True) #optional
    
    student_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    fathers_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    mothers_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    guardians_photo = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    
    # moneyyyy
    caution_money_reciept_no = models.CharField(max_length=255,blank=True) #optional
    caution_money_reciept_date = models.CharField(max_length=255,blank=True) #optional
    amount = models.IntegerField()
    counsellor_name = models.CharField(max_length=255)
    remark = models.CharField(max_length=255,blank=True) #optional
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.registration_number}"