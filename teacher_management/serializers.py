from rest_framework import serializers

from scholar_register.models import AssignmentSubmission
from .models import Employee, LiveClass, Assignments
from accounts.models import Institute, InstituteBranch, AcademicSession
from institute.models import Standard, Section, Subjects
from django.utils import timezone
from teacher_management.models import Assignments


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TodayLiveClassSerializer(serializers.ModelSerializer):
    institute_id = serializers.PrimaryKeyRelatedField(source='institute', queryset=Institute.objects.all())
    branch_id = serializers.PrimaryKeyRelatedField(source='branch', queryset=InstituteBranch.objects.all())
    session_id = serializers.PrimaryKeyRelatedField(source='session', queryset=AcademicSession.objects.all())
    standard_id = serializers.PrimaryKeyRelatedField(source='standard', queryset=Standard.objects.all())
    section_id = serializers.PrimaryKeyRelatedField(source='section', queryset=Section.objects.all())
    subject_id = serializers.PrimaryKeyRelatedField(source='subject', queryset=Subjects.objects.all())
    employee_id = serializers.PrimaryKeyRelatedField(source='employee', queryset=Employee.objects.all())

    class Meta:
        model = LiveClass
        fields = [
            'institute_id', 'branch_id', 'session_id', 'employee_id', 'standard_id', 'section_id', 'subject_id',
            'chapter', 'message', 'class_date', 'class_time'  # Include new fields here
        ]

class AssignmentSerializer(serializers.ModelSerializer):
    institute_id = serializers.PrimaryKeyRelatedField(source='institute', queryset=Institute.objects.all())
    branch_id = serializers.PrimaryKeyRelatedField(source='branch', queryset=InstituteBranch.objects.all())
    session_id = serializers.PrimaryKeyRelatedField(source='session', queryset=AcademicSession.objects.all())
    employee_id = serializers.PrimaryKeyRelatedField(source='employee', queryset=Employee.objects.all())
    standard_id = serializers.PrimaryKeyRelatedField(source='standard', queryset=Standard.objects.all())
    section_id = serializers.PrimaryKeyRelatedField(source='section', queryset=Section.objects.all())
    subject_id = serializers.PrimaryKeyRelatedField(source='subject', queryset=Subjects.objects.all())
    
    class Meta:
        model = Assignments
        fields = ['institute_id', 'branch_id', 'session_id', 'employee_id', 'standard_id', 'section_id', 'subject_id', 'title', 'submission_date', 'message', 'attachment']

    def validate_submission_date(self, value):
        # Validate submission date to ensure it's not in the past
        if value < timezone.now().date():
            raise serializers.ValidationError("Submission date cannot be in the past.")
        return value


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['institute', 'branch', 'session', 'assignment', 'student', 'status', 'remarks', 'date', 'attachment']


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields=['id', 'name']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'standard']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'name', 'standard']

class AssignmentsDropdownListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields= ['id', 'title']

class AssignmentSubmissionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['id', ]
