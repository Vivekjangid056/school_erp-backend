from django import forms
from .models import Institute

class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'  # or specify individual fields like ['field1', 'field2', ...]
        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control '}),
            'institute_name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'billing_name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number2': forms.TextInput(attrs={'class': 'form-control'}),
            'fax_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'principal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'acc_start_year': forms.TextInput(attrs={'class': 'form-control'}),
            'session_start_month': forms.TextInput(attrs={'class': 'form-control'}),
            'accredited_by': forms.TextInput(attrs={'class': 'form-control'}),
            'scholar_prefix': forms.TextInput(attrs={'class': 'form-control'}),
            'scholar_suffix': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_no_prefix': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_pg_in_tcbook': forms.TextInput(attrs={'class': 'form-control'}),
            'auto_enroll_no': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'std_attd_assignment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'live_class_show_time': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'allow_edit_emp_attd_time': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_std_contact_no_app': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto_admin_number': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'live_class_log_Std': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'suggest_auto_section': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'send_Std_wc_msg': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto_scholar_no': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'change_zoom_url': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'single_login': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'suggest_auto_house': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'allow_ss_in_app': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto_emp_no': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'std_attd_through_live_class': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'login_with_single_device': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_yt_opt_4_app': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_teach_mo_no_app': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_exam_list_res_wise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        def is_checkbox(self, field):
            return isinstance(self.fields[field].widget, forms.CheckboxInput)
