from django import forms 
from .models import *



class LmCategoryMasterForm(forms.ModelForm):
    class Meta:
        model = LmCategoryMaster
        fields = "__all__"
        
class LmDesignationMasterForm(forms.ModelForm):
    class Meta:
        model = LmDesignationMaster
        fields = "__all__"       
        
class LmDepartmentMasterForm(forms.ModelForm):
    class Meta:
        model = LmDepartmentMaster
        fields = "__all__"
        
class LmAttendanceTypeForm(forms.ModelForm):
    class Meta:
        model = LmAttendanceType
        fields = ['name','code','nature','attendance'] 
        
class LmHolidayListForm(forms.ModelForm):
    class Meta:
        model = LmHolidayList
        fields = ['code','name','description']
    
class EmployeeMasterForm(forms.ModelForm):
    join_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    reliving_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    pass_port_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    drivint_license_issue_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    driving_license_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    class Meta:
        model = EmployeeMaster
        fields = "__all__"