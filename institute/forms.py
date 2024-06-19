from django import forms
from .models import Institute
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = 'INSTITUTE'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'INSTITUTE'  # Set role to 'INSTITUTE'
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
