from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Institute(models.Model):
    
    registration_number = models.CharField(max_length=20,primary_key=True,blank=False)  #reg.number/aff.number
    institute_name = models.CharField(max_length=250,blank=False)
    branch_name = models.CharField(max_length=250,blank=True) #optional
    address1 = models.CharField(blank=False,max_length=100)
    address2 = models.CharField(blank=True,max_length=100) #optional
    billing_name = models.CharField(max_length=200,blank=False)
    state = models.CharField(max_length=200,blank=False)
    district = models.CharField(max_length=200,blank=False)
    pin = models.CharField(
        max_length=6, 
        validators=[
            RegexValidator(regex='^\d{6}$', message='PIN must be 6 digits.')
        ]
    )
    mobile_number = models.CharField(
        max_length=12, 
        validators=[
            RegexValidator(regex='^\d{10,12}$', message='Mobile number must be 10 to 12 digits.')
        ]
    )
    mobile_number2 = models.CharField(
        max_length=12, 
        blank=True,
        validators=[
            RegexValidator(regex='^\d{10,12}$', message='Mobile number must be 10 to 12 digits.')
        ]
    )  # optional
    fax_number = models.CharField(max_length=100,blank=True) #optional
    email = models.EmailField(blank=False,max_length=100)
    website = models.CharField(blank=True,max_length=255)
    principal_name = models.CharField(blank=True,max_length=100)
    acc_start_year = models.CharField(blank=False,max_length=100) #account start year
    session_start_month = models.CharField(blank=False,max_length=15)
    accredited_by = models.CharField(blank=False,max_length=20)
    scholar_prefix = models.CharField(blank=True,max_length=50)      #optional
    scholar_suffix = models.CharField(blank=True,max_length=50)   #optional
    emp_no_prefix = models.CharField(max_length=100,blank=True) #optional,employee number prefix
    no_of_pg_in_tcbook = models.CharField(max_length=255,blank=True) #number of page in one tc book
    
    auto_enroll_no = models.BooleanField(default=False)   #auto enrollment number
    std_attd_assignment = models.BooleanField(default=False) #student attendance through assignment
    live_class_show_time = models.BooleanField(default=False)
    allow_edit_emp_attd_time = models.BooleanField(default=False)  #allow to edit emp attendance time
    show_std_contact_no_app = models.BooleanField(default=False)    #show student contact number in application in mobile or ios
    
    change_zoom_url =models.BooleanField(default = False)
    auto_admin_number = models.BooleanField(default=False) #auto admission number
    live_class_log_Std = models.BooleanField(default=False)#live class join log of students
    suggest_auto_section = models.BooleanField(default=False)
    send_Std_wc_msg = models.BooleanField(default=False)#send student welcome message to class teacher
    auto_scholar_no = models.BooleanField(default=False) #auto scholar number
    
    auto_scholar_no = models.BooleanField(default=False)
    single_login = models.BooleanField(default=False)
    suggest_auto_house = models.BooleanField(default=False)
    allow_ss_in_app = models.BooleanField(default=True) #allow screenshots in app 
    auto_emp_no = models.BooleanField(default=False)
    
    std_attd_through_live_class = models.BooleanField(default=False) #student attendance through live classes
    login_with_single_device = models.BooleanField(default=False)
    show_yt_opt_4_app = models.BooleanField(default=False)  #show youtube option for mobile/ios app
    show_teach_mo_no_app = models.BooleanField(default=False)  #show teacher mobile number in application for android/ios
    show_exam_list_res_wise = models.BooleanField(default=False)   #show exam list result wise
    
    profile_image = models.ImageField(upload_to='images/',blank=True,null=True) #optional
    
    
    def __str__(self):
        return self.institute_name
    
    class Meta:
        verbose_name = 'Institute'
        verbose_name_plural = 'Institutes'



# List of Masters models

class Signature(models.Model):
    name = models.CharField(max_length=100)
