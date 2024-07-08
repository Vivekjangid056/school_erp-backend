from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
    

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'phone_number', 'country_code']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ['registration_number', 'institute_name', 'branch_name', 'billing_name', 'address1', 'address2',
                  'state', 'district', 'pin', 'mobile_number', 'mobile_number2', 'fax_number', 'institute_email', 'website',
                  'principal_name', 'acc_start_year', 'session_start_month', 'accredited_by', 'scholar_prefix',
                  'scholar_suffix', 'emp_no_prefix', 'no_of_pg_in_tcbook', 'profile_image', 'auto_enroll_no',
                  'std_attd_assignment', 'live_class_show_time', 'allow_edit_emp_attd_time', 'show_std_contact_no_app',
                  'auto_admin_number', 'live_class_log_Std', 'suggest_auto_section', 'send_Std_wc_msg', 'auto_scholar_no',
                  'single_login', 'suggest_auto_house', 'allow_ss_in_app', 'auto_emp_no', 'std_attd_through_live_class',
                  'login_with_single_device', 'show_yt_opt_4_app', 'show_teach_mo_no_app', 'show_exam_list_res_wise']
