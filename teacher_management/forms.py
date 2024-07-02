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
        