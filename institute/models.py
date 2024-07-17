from django.db import models
from django.core.validators import RegexValidator
from colorfield.fields import ColorField
from django.db.models import UniqueConstraint
from accounts.models import Institute, User


# =========================== Model For menu shown in admin panel =============================

class Branches(models.Model):
    pass

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


# List of session settings models
class SubjectsForClassGroup(models.Model):
    ALL = 'All'
    SELECTED = 'Selected'
    SUBJECT_TYPE_CHOICES = [
        (ALL, 'All'),
        (SELECTED, 'Selected'),
    ]
    name = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject_type = models.CharField(
        choices=SUBJECT_TYPE_CHOICES,
        default=SELECTED,
    )


class Section(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class DiscountScheme(models.Model):
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
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    document = models.FileField(upload_to='documents/', max_length=100)