from django import forms
from .models import *
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = '1'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = '1'  # Set role to 'INSTITUTE'
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'role']


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ['registration_number', 'institute_name', 'branch_name', 'billing_name', 'address1', 'address2',
                  'state', 'district', 'pin', 'mobile_number', 'mobile_number2', 'fax_number', 'email', 'website',
                  'principal_name', 'acc_start_year', 'session_start_month', 'accredited_by', 'scholar_prefix',
                  'scholar_suffix', 'emp_no_prefix', 'no_of_pg_in_tcbook', 'profile_image', 'auto_enroll_no',
                  'std_attd_assignment', 'live_class_show_time', 'allow_edit_emp_attd_time', 'show_std_contact_no_app',
                  'auto_admin_number', 'live_class_log_Std', 'suggest_auto_section', 'send_Std_wc_msg', 'auto_scholar_no',
                  'single_login', 'suggest_auto_house', 'allow_ss_in_app', 'auto_emp_no', 'std_attd_through_live_class',
                  'login_with_single_device', 'show_yt_opt_4_app', 'show_teach_mo_no_app', 'show_exam_list_res_wise']


# institute role form
class InstituteRoleForm(forms.ModelForm):
    class Meta:
        model = InstituteRole
        fields = ['name', 'description', 'is_active', 'branches', 'menu']


class SignatureForm(forms.ModelForm):
    class Meta:
        model = LomSignature
        fields = "__all__"

class CasteForm(forms.ModelForm):
    class Meta:
        model = Caste
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"

class MediumForm(forms.ModelForm):
    class Meta:
        model = Medium
        fields = "__all__"

class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion
        fields = "__all__"

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"


class NationalityForm(forms.ModelForm):
    class Meta:
        model = Nationality
        fields = "__all__"


class MotherTongueForm(forms.ModelForm):
    class Meta:
        model = MotherToungue
        fields = "__all__"


class FamilyRelationForm(forms.ModelForm):
    class Meta:
        model = FamiliRelation
        fields = "__all__"


class EnquiryTypeForm(forms.ModelForm):
    class Meta:
        model = EnquiryType
        fields = "__all__"


class PaymentModeForm(forms.ModelForm):
    class Meta:
        model = PaymentMode
        fields = "__all__"


class ClassGroupsForm(forms.ModelForm):
    class Meta:
        model = ClassGroups
        fields = "__all__"


class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = "__all__"


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"


class DocumnetsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = "__all__"


class FeeHeadsForm(forms.ModelForm):
    class Meta:
        model = FeeHeads
        fields = "__all__"

class FeeInstallmentForm(forms.ModelForm):
    class Meta:
        model = FeeInstallments
        fields = "__all__"


class LeavingReasonForm(forms.ModelForm):
    class Meta:
        model = LeavingReasonTC
        fields = "__all__"


class NameOfSainikSchoolForm(forms.ModelForm):
    class Meta:
        model = NameOfSainikSchool
        fields = "__all__"

class NameOfBankForm(forms.ModelForm):
    class Meta:
        model = NameOfTheBank
        fields = "__all__"


class StudentTypeForm(forms.ModelForm):
    class Meta:
        model = StudentType
        fields = "__all__"


class ChildStatusForm(forms.ModelForm):
    class Meta:
        model = ChildStatus
        fields = "__all__"