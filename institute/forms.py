import bleach
from django import forms
from hr.models import ClassTimePeriod, TimeTable
from .models import *
from scholar_register.models import Attendance
from teacher_management.models import Employee
from accounts.models import Institute, User, InstituteBranch
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
        fields = ['first_name', 'last_name',
                  'username', 'email', 'phone_number', 'role']


# =================================== institute role form ====================================
class InstituteRoleForm(forms.ModelForm):
    branches = forms.ModelMultipleChoiceField(
        queryset=InstituteBranch.objects.none(),
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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user is not None:
            # Filter branches based on the user's institute_id
            self.fields['branches'].queryset = InstituteBranch.objects.filter(institute=self.user.institute_id.first())

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance

# =================================== Permissions form =======================================


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['menu', 'submenu', 'supersubmenu', 'can_add',
                  'can_edit', 'can_view', 'can_delete', 'can_print']

# ==================================List Of Masters Forms ====================================
class SignatureForm(forms.ModelForm):
    class Meta:
        model = LomSignature
        fields = "__all__"
        exclude = ['institute', 'session']


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
        exclude = ['institute', 'branch', 'session']


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
        exclude = ['branch', 'institute']


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
        exclude = ['institute', 'session', 'branch']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        print(self.session)
        if self.user and self.session:
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            self.fields['standard'].queryset = Standard.objects.filter(
                branch=active_branch)


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['standard', 'student',
                  'subject', 'date', 'present', 'absent']
        exclude = ['institute', 'session', 'branch']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class DocumnetsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = "__all__"
        exclude = ['institute', 'session', 'branch']


class FeeHeadsForm(forms.ModelForm):
    class Meta:
        model = FeeHeads
        fields = "__all__"
        exclude = ['institute']


class FeeInstallmentForm(forms.ModelForm):
    class Meta:
        model = FeeInstallments
        fields = "__all__"
        exclude = ['institute', 'session', 'branch']


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



# =================================== Employee Form =========================================
"""
This model is defined into the models.py file of teacher management app 
because of circular import error:- the circular import is like when a model is imported from another app into current 
models.py file and into the same another models.py file a models is imported from the current models 
file the this error comes into the picture (django don't allow circular import of any models)
"""

# form for session settingsd
class SubjectsForClassGroupForm(forms.ModelForm):
    class Meta:
        model = SubjectsForClassGroup
        fields = "__all__"
        exclude = ['institute', 'session', 'branch']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            active_session = AcademicSession.objects.get(pk = self.session.get('session_id'))
            self.fields['name'].queryset = Subjects.objects.filter(
                branch=active_branch, session=active_session)


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
        exclude = ['institute', 'branch']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            self.fields['standard'].queryset = Standard.objects.filter(
                branch=active_branch)


class DiscountSchemeForm(forms.ModelForm):
    class Meta:
        model = DiscountScheme
        fields = "__all__"
        exclude = ['institute', 'branch', 'session']


class NotificationModelForm(forms.ModelForm):
    receiver = forms.MultipleChoiceField(
        choices=NotificationModel.RECEIVER_CHOICES,
        widget=forms.CheckboxSelectMultiple  # You can also use SelectMultiple for a dropdown
    )

    class Meta:
        model = NotificationModel
        fields = "__all__"
        exclude = ['institute', 'branch']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Set default value for the 'user' field based on the user role
        if self.user.role == '2':
            self.fields['user'].initial = NotificationModel.INSTITUTE
        else:
            self.fields['user'].initial = NotificationModel.TEACHER

        # Make the 'user' field non-editable
        self.fields['user'].disabled = True

        # Adjust the 'receiver' field options based on the user role
        if self.user.role == '2':
            self.fields['receiver'].choices = NotificationModel.RECEIVER_CHOICES
        else:
            self.fields['receiver'].choices = [(NotificationModel.ALL_STUDENTS, 'All Students')]
            self.fields['receiver'].initial = [NotificationModel.ALL_STUDENTS]
            self.fields['receiver'].disabled = True

    def clean_receiver(self):
        return ','.join(self.cleaned_data.get('receiver', []))

    def clean_description(self):
        description = self.cleaned_data['description']
        # Allow only specific HTML tags and attributes
        allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']
        allowed_attributes = {'a': ['href', 'title']}
        cleaned_description = bleach.clean(
            description, tags=allowed_tags, attributes=allowed_attributes, strip=True)
        return cleaned_description

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance

# ______ forms for gallery section ______


class GalleryItemsForm(forms.ModelForm):
    class Meta:
        model = GalleryItems
        fields = ['name', 'url_tag', 'image', 'video']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'video': forms.ClearableFileInput(attrs={'accept': 'video/*'}),
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
            raise forms.ValidationError(
                "You must provide an image, video, or video URL.")
        if (image and video) or (image and url_tag) or (video and url_tag):
            raise forms.ValidationError(
                "You can only provide one of image, video, or video URL.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance
    
class ClassTimePeriodForm(forms.ModelForm):
    class Meta:
        model = ClassTimePeriod
        fields= ['period_no', 'start_time', 'end_time']
        widgets = {
                'start_time': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time'}),
                'end_time': forms.TimeInput(format='%I:%M %p', attrs={'type': 'time'})
            }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        print(self.user)

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
        fields = ['standard', 'section', 'subject', 'period', 'faculty',
                  'day_of_week',]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            active_session = AcademicSession.objects.get(pk=self.session.get('session_id'))
            self.fields['standard'].queryset = Standard.objects.filter(
                branch=active_branch)
            self.fields['section'].queryset = Section.objects.filter(
                institute=institute, branch=active_branch)
            self.fields['subject'].queryset = Subjects.objects.filter(
                branch=active_branch, session=active_session)
            self.fields['faculty'].queryset = Employee.objects.filter(
                institute=institute)
            self.fields['period'].queryset=ClassTimePeriod.objects.filter(
                institute=institute, session=active_session, branch=active_branch
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance
    
class CustomMenuForm(forms.ModelForm):
    class Meta:
        model = CustomMenu
        fields = "__all__"
        exclude = ['institute']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        print(self.user)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance

class GradingSystemForm(forms.ModelForm):
    class Meta:
        model = GradingSystem
        fields = ['grade', 'marks_from', 'marks_to']