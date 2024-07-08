from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = '1'
        user.save(using=self._db)
        return user
    
    
"""Here are 5 role choices are defines hard coded By assuming that aal the user wiil be registered within the given
   roles defined
    1:- Super_admin = will store the the Superadmin credentials and all the operations will be performed for 
        superadmin on the basis of the id of the super_admin
   
    2:- Institute_Owner = the second role is defined for the institute owner it will be treated as a superadmin for 
        all the institute related operations
        
    3:- Management_Employee = this is a critical role 
        the institute owner will decide who can have this role privilages. this role will have almost all permissions 
        as the institute owner, but they can not create another role like this but this role will rely on 2nd 
        stage in the hierarchy of power after Institute_Owner
        
    4:- Employee= this role will contain the all employee related to the institute including all the teachers
    
    5:- Students = All the Students"""    


class User(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = '1'
    INSTITUTE_OWNER = '2'
    MANAGEMENT_EMPLOYEE = '3'
    EMPLOYEE = '4'
    STUDENT = '5'


    ROLE_CHOICES = [
        (SUPER_ADMIN, 'Super_admin'),
        (INSTITUTE_OWNER, 'Institute_Owner'),
        (MANAGEMENT_EMPLOYEE, 'Management_Employee'),
        (EMPLOYEE, 'Employee'),
        (STUDENT, 'Student')
    ]

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country_code = CountryField(blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default= False)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_set',  # Custom name for reverse accessor
        help_text='The groups this user belongs to. A user can belong to multiple groups. A group grants access to a set of permissions.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_permissions',  # Can keep the default here
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


class Institute(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
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
    institute_email = models.EmailField(blank=False,max_length=100)
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