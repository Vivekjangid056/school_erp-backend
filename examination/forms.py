from django import forms

from accounts.models import AcademicSession, InstituteBranch
from institute.models import Standard, Subjects, Section
from .models import ExamTimeTable, ExamType, ExaminationMarks

class ExamTypeForm(forms.ModelForm):
    class Meta:
        model = ExamType
        fields = ['standard', 'name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)

            # Dynamically populate standards and subjects
            self.fields['standard'].queryset = Standard.objects.filter(institute=institute, branch=active_branch)

class ExamTimeTableForm(forms.ModelForm):
    class Meta:
        model = ExamTimeTable
        fields = ['exam_type', 'standard', 'subject', 'date', 'start_time', 'end_time', 'venue', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)
            active_session = AcademicSession.objects.get(pk = self.session.get('session_id'))

            # Dynamically populate standards and subjects
            self.fields['standard'].queryset = Standard.objects.filter(institute=institute, branch=active_branch)
            self.fields['subject'].queryset = Subjects.objects.filter(institute=institute, branch=active_branch, session=active_session)


class ExaminationMarksForm(forms.ModelForm):
    class Meta:
        model = ExaminationMarks
        fields = ['standard', 'section', 'exam_type', 'subject']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)
        if self.user and self.session:
            institute = self.user.institute_id.first()
            branch = self.session.get('branch_id')
            active_branch=InstituteBranch.objects.get(pk=branch)

            # Dynamically populate standards and subjects
            self.fields['standard'].queryset = Standard.objects.filter(institute=institute, branch=active_branch)
