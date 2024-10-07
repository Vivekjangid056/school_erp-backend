from django import forms
from .models import HrInterview
from institute.models import Category
from teacher_management.models import LmDesignationMaster, LmDepartmentMaster
from accounts.models import AcademicSession, InstituteBranch



class HrInterviewForm(forms.ModelForm):
    class Meta:
        model = HrInterview
        fields = ['interview_no','interview_date','reference','first_name','middle_name','last_name','gender','father_name','mother_name','date_of_birth','category','current_salary','expected_salary','department','marital_status','designation','user_image','current_address','city','state','pin','mobile','mobile2','email','company_name','prev_comp_hr_no','work_profile','joining_date','leaving_date','leaving_reason','salary','recommendation_positive','recommendation_negative','rating','select_for_next_round','assign','date','status','overall_comment','remark']
        widgets = {
            'interview_date' : forms.DateInput(attrs={'type':'date'}),
            'date_of_birth' :  forms.DateInput(attrs={'type':'date'}),
            'joining_date' : forms.DateInput(attrs={'type':'date'}),
            'leaving_date' : forms.DateInput(attrs={'type':'date'}),
            'date' : forms.DateInput(attrs={'type':'date'}),
        }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            active_session = AcademicSession.objects.get(pk=self.session.get('session_id'))
            self.fields['category'].queryset = Category.objects.filter(institute = institute)
            self.fields['department'].queryset = LmDepartmentMaster.objects.filter(session = active_session, branch = active_branch)
            self.fields['designation'].queryset = LmDesignationMaster.objects.filter(session = active_session, branch = active_branch)
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.institute = self.user.institute_id.first()
        if commit:
            instance.save()
        return instance