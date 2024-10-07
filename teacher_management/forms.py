from django import forms 
from .models import *

class LmCategoryMasterForm(forms.ModelForm):
    class Meta:
        model = LmCategoryMaster
        fields = "__all__"
        exclude = ['institute', 'branch', 'session']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance
        
class LmDesignationMasterForm(forms.ModelForm):
    class Meta:
        model = LmDesignationMaster
        fields = "__all__"   
        exclude = ['institute', 'branch', 'session']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance
        
class LmDepartmentMasterForm(forms.ModelForm):
    class Meta:
        model = LmDepartmentMaster
        fields = "__all__"
        exclude = ['institute', 'branch', 'session']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance
        
class LmAttendanceTypeForm(forms.ModelForm):
    class Meta:
        model = LmAttendanceType
        fields = "__all__"
        exclude = ['institute', 'branch', 'session'] 
        
class LmHolidayListForm(forms.ModelForm):
    class Meta:
        model = LmHolidayList
        fields = "__all__"
        exclude = ['institute', 'branch', 'session']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
            }


class UserEmployeeForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'phone_number', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].initial = '3'  # Set initial value for role
        self.fields['role'].widget = forms.HiddenInput()  # Hide the role field

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data

    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ['user','institute', 'branch', 'session']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'reliving_date': forms.DateInput(attrs={'type': 'date'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'pass_port_end_date': forms.DateInput(attrs={'type': 'date'}),
            'driving_license_issue_date': forms.DateInput(attrs={'type': 'date'}),
            'driving_license_expiry_date': forms.DateInput(attrs={'type': 'date'}),
            }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        print(self.session)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            self.fields['category'].queryset = LmCategoryMaster.objects.filter(branch=active_branch)
            self.fields['department'].queryset = LmDepartmentMaster.objects.filter(branch=active_branch)
            self.fields['designation'].queryset = LmDesignationMaster.objects.filter(branch=active_branch)
            self.fields['category_cast'].queryset= Category.objects.filter(institute=institute)
            self.fields['staff_role'].queryset= InstituteRole.objects.filter(branch=active_branch, institute=institute)
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance