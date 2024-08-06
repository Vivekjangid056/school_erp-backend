from django import forms 
from .models import *

class LmCategoryMasterForm(forms.ModelForm):
    class Meta:
        model = LmCategoryMaster
        fields = "__all__"
        exclude = ['institute']

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
        exclude = ['institute']

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
        exclude = ['institute']

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
        fields = ['name','code','nature','attendance'] 
        
class LmHolidayListForm(forms.ModelForm):
    class Meta:
        model = LmHolidayList
        fields = ['code','name','description']
    
class EmployeeMasterForm(forms.ModelForm):
    class Meta:
        model = EmployeeMaster
        fields = "__all__"
        exclude = ['institute']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'reliving_date': forms.DateInput(attrs={'type': 'date'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'pass_port_end_date': forms.DateInput(attrs={'type': 'date'}),
            'drivint_license_issue_date': forms.DateInput(attrs={'type': 'date'}),
            'driving_license_expiry_date': forms.DateInput(attrs={'type': 'date'}),
            }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user is not None:
            self.fields['category'].queryset = LmCategoryMaster.objects.filter(institute = self.user.institute_id.first())
            self.fields['department'].queryset = LmDepartmentMaster.objects.filter(institute = self.user.institute_id.first())
            self.fields['designation'].queryset = LmDesignationMaster.objects.filter(institute = self.user.institute_id.first())
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance