from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField
from django.db.models import UniqueConstraint
from accounts.models import Institute, User, AcademicSession


# =========================== Model For menu shown in admin panel =============================
class MainMenu(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class SubMenu(models.Model):
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, related_name='submenus')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class SuperSubMenu(models.Model):
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name='supersubmenus')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InstituteRole(models.Model):
    institute = models.ForeignKey(Institute, on_delete= models.CASCADE, related_name="institute_role")
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    branches = models.ManyToManyField(Institute, related_name='roles')
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Permission(models.Model):
    role = models.ForeignKey(InstituteRole, on_delete=models.CASCADE, related_name='permissions')
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, null=True, blank=True)
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, null=True, blank=True)
    supersubmenu = models.ForeignKey(SuperSubMenu, on_delete=models.CASCADE, null=True, blank=True)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_print = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['role', 'menu', 'submenu', 'supersubmenu'], name='unique_role_menu_submenu_supersubmenu')
        ]

    def __str__(self):
        return f'{self.role} - {self.menu} - {self.submenu} - {self.supersubmenu}'

# List of Masters models

class LomSignature(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='lom_signature')
    signature_name = models.CharField(max_length=100)
    signature_heading = models.CharField(max_length= 100)

    def __str__(self):
        return self.signature_name


class Category(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class House(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='house')
    name = models.CharField(max_length=100)
    color_code = ColorField(default='#ffffff')

    def __str__(self):
        return self.name


class Medium(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='medium')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Religion(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='religion')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Caste(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='caste')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Reference(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='reference')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Nationality(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='nationality')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MotherToungue(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='maothe_tongue')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FamiliRelation(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='family_relation')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EnquiryType(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='enquiry_type')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PaymentMode(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='payment_mode')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassGroups(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='class_groups')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Standard(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='standard')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='subjects')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='subjects')
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  


class Documents(models.Model):
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='documents')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FeeHeads(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='fee_heads')
    head_name = models.CharField(max_length=100)
    tax_rate = models.IntegerField()
    default_fees = models.IntegerField(default=0)

    def __str__(self):
        return self.head_name


class FeeInstallments(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='fee_installments')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LeavingReasonTC(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='leaving_reason')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NameOfSainikSchool(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='name_of_sainik_school')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NameOfTheBank(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='name_of_bank')
    name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=200)
    branch_address = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class StudentType(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='student_type')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChildStatus(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='child_status')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NextClass(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='next_class')
    name = models.CharField(max_length=50)



class ClassWiseSubjects(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='class_wise_subjects')
    subject_name = models.ForeignKey(Subjects, on_delete= models.CASCADE)
    compulsary = models.BooleanField(default= False)
    activity = models.BooleanField(default= False)
    additional = models.BooleanField(default= False)
    skill = models.BooleanField(default= False)
    show_in_marlsheet = models.BooleanField(default= False)
    practical_fee = models.IntegerField()


class DocumentsRequired(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='documents_required')
    document_name = models.ForeignKey(Documents, on_delete= models.CASCADE)
    for_new = models.BooleanField(default=False)
    for_old = models.BooleanField(default=False)


# List of session settings models
class SubjectsForClassGroup(models.Model):
    ALL = 'All'
    SELECTED = 'Selected'
    SUBJECT_TYPE_CHOICES = [
        (ALL, 'All'),
        (SELECTED, 'Selected'),
    ]
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='subjects_for_class_groups')
    name = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_type = models.CharField(
        choices=SUBJECT_TYPE_CHOICES,
        default=SELECTED,
    )


class Section(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='section')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='section')
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.standard.name} - {self.name}"
    
class DiscountScheme(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='discount_scheme')
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class NotificationModel(models.Model):
    INSTITUTE = "1"
    TEACHER = "2"

    SENDER_CHOICES = [
        (TEACHER, 'Teacher'),
        (INSTITUTE, 'Institute'),
    ]
    user = models.CharField(choices=SENDER_CHOICES, default=INSTITUTE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='notification')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    document = models.FileField(upload_to='documents/', max_length=100)
    
class GalleryItems(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE,related_name='institute_gallery')
    name = models.CharField(max_length=255)
    url_tag = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/',blank=True, null=True)
    video = models.FileField(upload_to='gallery/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    MESSAGE_TYPES = [
        ('text','Text'),
        ('image','Image'),
        ('doc','Document'),
        ('video','Video'),
    ]
    
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_message')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_message',blank=True,null=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True,blank=True )
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True,blank=True )
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    message = models.TextField()
    is_individual = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver if self.is_individual else 'class'}"