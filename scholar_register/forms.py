from django import forms
from accounts.models import User
from .models import StudentProfile
class StudentUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','phone_number','role']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = '5'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.role = '5'
        if commit:
            user.save()
        return user
    def clean_Password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password don't match")
        return password2
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['session','form_no','date_of_admission','registration_date','stream', 'standard','section','date_of_deactivae','rte','bpl','installment_mode','prefix','suffix','sr_no','reg_no', 'admission_no','enroll_no','nationality','mother_tongue','middle_name','gender','dob','student_aadhar','caste','religion','category','medium','rural_or_urban','disablity_type','blood_group','house_name','place_of_birth','staff_refrence','admission_confirm_date','board_type','fathers_name','fathers_occupation','fathers_mob_no','fathers_email','mothers_name','mothers_occupation','mothers_mob_no','mothers_email','fahers_aadhar_no','mothers_aadhar_no','father_annual_income','mother_annual_income','father_qualification','mother_qualification','father_pan_no','mother_pan_no','guardian_name','guardian_mobile','guardian_relation','fee_deposited_by','sms_mob_no','student_type','child_status','discount_scheme','address1','address2','district','state','pin','previous_school_name','previous_school_address','reason_of_leaving','previous_year','previous_class','obtain_marks','maximum_marks','percentage','result','previous_school_board','previous_school_rollNo','previous_school_class','third_lang_studied','student_photo','fathers_photo','mothers_photo','guardians_photo','caution_money_reciept_no','caution_money_reciept_date','amount','counsellor_name','remark']
        widgets = {
            'date_of_admission': forms.DateInput(attrs={'type': 'date'}),
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_deactivae': forms.DateInput(attrs={'type': 'date'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'admission_confirm_date': forms.DateInput(attrs={'type': 'date'}),
            'caution_money_reciept_date': forms.DateInput(attrs={'type': 'date'}),
        }