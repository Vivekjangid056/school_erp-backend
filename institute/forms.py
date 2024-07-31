import bleach
from django import forms

from hr.models import TimeTable
from .models import *
from scholar_register.models import Attendance
from teacher_management.models import Employee, EmployeeMaster
from accounts.models import Institute, User
from django.contrib.auth.forms import UserCreationForm

# ================================= User Register Form =======================================
class CustomUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = '1'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = '2'  # Set role to 'INSTITUTE'
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role']


# =================================== institute role form ====================================
class InstituteRoleForm(forms.ModelForm):
    branches = forms.ModelMultipleChoiceField(
        queryset=Institute.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    menu = forms.ModelChoiceField(
        queryset=MainMenu.objects.all(),
        widget=forms.Select(),  # Use Select widget
        required=True
    )
    class Meta:
        model = InstituteRole
        fields = ['name', 'description', 'is_active', 'menu', 'branches']

# =================================== Permissions form =======================================
class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['menu', 'submenu', 'supersubmenu', 'can_add', 'can_edit', 'can_view', 'can_delete', 'can_print']


# ==================================List Of Masters Forms ====================================
class SignatureForm(forms.ModelForm):
    class Meta:
        model = LomSignature
        fields = "__all__"
        exclude = ['institute']

class CasteForm(forms.ModelForm):
    class Meta:
        model = Caste
        fields = "__all__"
        exclude = ['institute']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ['institute']


class HouseForm(forms.ModelForm):
    color_code = ColorField(default='#ffffff')
    class Meta:
        model = House
        fields = ['name', 'color_code']
        exclude = ['institute']


class MediumForm(forms.ModelForm):
    class Meta:
        model = Medium
        fields = "__all__"
        exclude = ['institute']

class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion
        fields = "__all__"
        exclude = ['institute']

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"
        exclude = ['institute']


class NationalityForm(forms.ModelForm):
    class Meta:
        model = Nationality
        fields = "__all__"
        exclude = ['institute']


class MotherTongueForm(forms.ModelForm):
    class Meta:
        model = MotherToungue
        fields = "__all__"
        exclude = ['institute']


class FamilyRelationForm(forms.ModelForm):
    class Meta:
        model = FamiliRelation
        fields = "__all__"
        exclude = ['institute']


class EnquiryTypeForm(forms.ModelForm):
    class Meta:
        model = EnquiryType
        fields = "__all__"
        exclude = ['institute']


class PaymentModeForm(forms.ModelForm):
    class Meta:
        model = PaymentMode
        fields = "__all__"
        exclude = ['institute']


class ClassGroupsForm(forms.ModelForm):
    class Meta:
        model = ClassGroups
        fields = "__all__"
        exclude = ['institute']


class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = "__all__"
        exclude = ['institute']


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
        exclude = ['institute']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['standard'].queryset = Standard.objects.filter(institute=self.user.institute_id.first())
                
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['standard','student', 'subject', 'date', 'present', 'absent']
        exclude = ['institute']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class DocumnetsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = "__all__"
        exclude = ['institute']


class FeeHeadsForm(forms.ModelForm):
    class Meta:
        model = FeeHeads
        fields = "__all__"
        exclude = ['institute']

class FeeInstallmentForm(forms.ModelForm):
    class Meta:
        model = FeeInstallments
        fields = "__all__"
        exclude = ['institute']


class LeavingReasonForm(forms.ModelForm):
    class Meta:
        model = LeavingReasonTC
        fields = "__all__"
        exclude = ['institute']


class NameOfSainikSchoolForm(forms.ModelForm):
    class Meta:
        model = NameOfSainikSchool
        fields = "__all__"
        exclude = ['institute']

class NameOfBankForm(forms.ModelForm):
    class Meta:
        model = NameOfTheBank
        fields = "__all__"
        exclude = ['institute']


class StudentTypeForm(forms.ModelForm):
    class Meta:
        model = StudentType
        fields = "__all__"
        exclude = ['institute']


class ChildStatusForm(forms.ModelForm):
    class Meta:
        model = ChildStatus
        fields = "__all__"
        exclude = ['institute']
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_details','middle_name','nick_name','position','user_image']
        
        
        
# =================================== Employee Form =========================================

"""
This model is defined into the models.py file of teacher management app 
because of circular import error:- the circular import is like when a model is imported from another app into current 
models.py file and into the same another models.py file a models is imported from the current models 
file the this error comes into the picture (django don't allow circular import of any models)
"""


class EmployeeRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    confirm_email = forms.EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = '3'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails do not match")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data



class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_details', 'staff_role', 'middle_name', 'nick_name', 'position', 'confirm_email', 'user_image']
        # 'institute' is excluded from fields

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['employee_details'].queryset = EmployeeMaster.objects.filter(institute=self.user.institute_id.first())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance


# form for session settingsd
class SubjectsForClassGroupForm(forms.ModelForm):
    class Meta:
        model = SubjectsForClassGroup
        fields = "__all__"
        exclude = ['institute']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['name'].queryset = Subjects.objects.filter(institute = self.user.institute_id.first())

    
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
        exclude = ['institute']

    
class DiscountSchemeForm(forms.ModelForm):
    class Meta:
        model = DiscountScheme
        fields = "__all__"
        exclude = ['institute']

    
class NotificationModelForm(forms.ModelForm):
    class Meta:
        model = NotificationModel
        fields = "__all__"
        exclude = ['institute']

    def clean_description(self):
        description = self.cleaned_data['description']
        # Allow only specific HTML tags and attributes
        allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']
        allowed_attributes = {'a': ['href', 'title']}
        cleaned_description = bleach.clean(description, tags=allowed_tags, attributes=allowed_attributes, strip=True)
        return cleaned_description
    
#______ forms for gallery section ______

class GalleryItemsForm(forms.ModelForm):
    class Meta:
        model = GalleryItems
        fields = ['name','url_tag','image','video']
        widgets = {
			'image': forms.ClearableFileInput(attrs={'accept':'image/*'}),
			'video': forms.ClearableFileInput(attrs={'accept':'video/*'}),
		}
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        url_tag = cleaned_data.get('url_tag')

        if not image and not video and not url_tag:
            raise forms.ValidationError("You must provide an image, video, or video URL.")
        if (image and video) or (image and url_tag) or (video and url_tag):
            raise forms.ValidationError("You can only provide one of image, video, or video URL.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance    
    
class TimetableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['standard', 'section', 'subject', 'faculty', 'day_of_week', 'period_no', 'start_time', 'end_time']    
        widgets = {
            'start_time': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time'})
        }
   
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            institute = self.user.institute_id.first()
            print(f"User Institute: {institute}")
            self.fields['standard'].queryset = Standard.objects.filter(institute=institute )
            self.fields['section'].queryset = Section.objects.filter(institute= self.user.institute_id.first())
            self.fields['subject'].queryset = Subjects.objects.filter(institute= self.user.institute_id.first())
            self.fields['faculty'].queryset = Employee.objects.filter(institute= self.user.institute_id.first())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance      