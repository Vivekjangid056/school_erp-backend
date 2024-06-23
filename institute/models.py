from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField

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

class LomSignature(models.Model):
    signature_name = models.CharField(max_length=100)
    signature_heading = models.CharField(max_length= 100)

    def __str__(self):
        return self.signature_name


class Caste(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=100)
    color_code = ColorField(default='#ffffff')

    def __str__(self):
        return self.name


class Medium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MotherToungue(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FamiliRelation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EnquiryType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PaymentMode(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassGroups(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Standard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Documents(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FeeHeads(models.Model):
    head_name = models.CharField(max_length=100)
    tax_rate = models.IntegerField()
    default_fees = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FeeInstallments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Signature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LeavingReasonTC(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NameOfSainikSchool(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NameOfTheBank(models.Model):
    name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=200)
    branch_address = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class StudentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChildStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class NextClass(models.Model):
    name = models.CharField(max_length=50)


class SubjectForClassGroup(models.Model):
    pass


class SessionSettingsClass(models.Model):
    current_class = models.ForeignKey(Standard, on_delete=models.CASCADE)
    next_class = models.ForeignKey(NextClass, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=50)


class ClassWiseSubjects(models.Model):
    subject_name = models.ForeignKey(Subjects, on_delete= models.CASCADE)
    compulsary = models.BooleanField(default= False)
    activity = models.BooleanField(default= False)
    additional = models.BooleanField(default= False)
    skill = models.BooleanField(default= False)
    show_in_marlsheet = models.BooleanField(default= False)
    practical_fee = models.IntegerField()


class DocumentsRequired(models.Model):
    document_name = models.ForeignKey(Documents, on_delete= models.CASCADE)
    for_new = models.BooleanField(default=False)
    for_old = models.BooleanField(default=False)
    
# list of users models
 
# class User(models.Model):
#     employee_name = models.CharField(max_length=100)  #data will dynamically come from faculty section
#     first_name = models.CharField(max_length=50)
#     middle_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50 ,  blank = True)   #optional
#     user_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     register_mobile_no = models.CharField(max_length=12, 
#         validators=[
#             RegexValidator(regex='^\d{10,12}$', message='Mobile number must be 10 to 12 digits.')
#         ]
#     )
#     nick_name = models.CharField(max_length=50,blank=True) #optional
#     position = models.CharField(max_length=50,blank=True)   #optional
    
#     user_image = models.ImageField(upload_to='images/',blank=True,null=True)  #optional