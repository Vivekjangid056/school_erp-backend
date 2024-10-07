from django.db import models
from accounts.models import Institute, InstituteBranch, AcademicSession
from institute.models import Section, Standard, Subjects
from scholar_register.models import StudentProfile
# Create your models here.


class ExamType(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name= 'exam_type_institute')
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name = 'exam_type_institute_branch')
    session= models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='exam_type_session')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name = 'exam_type_standard')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"class {self.standard.name} {self.name}"

class ExamTimeTable(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name="exam_time_table_institute")
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='exam_time_table_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='exam_time_table_session')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='exam_time_table_standard')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='exam_time_table_subject')
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE, related_name= 'exam_time_table_exam_type')
    date= models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=500, null=True, blank=True)
    note = models.CharField(max_length=500)


class ExaminationMarks(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name="examination_mark_institute")
    branch = models.ForeignKey(InstituteBranch, on_delete=models.CASCADE, related_name='examination_mark_branch')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='examination_mark_session')
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='examination_mark_standard')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name = 'examination_mark_section')
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE, related_name='examination_mark_exam_type')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='examination_mark_subject')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='examination_mark_student_profile')
    max_marks = models.IntegerField()
    obtained_marks = models.CharField(max_length=20)

    def __str__(self):
        return f"examination marks of {self.student.first_name} {self.student.last_name} for subject <{self.subject.name}>"


