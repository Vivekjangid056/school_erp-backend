# serializers.py
from rest_framework import serializers
from teacher_management.models import Assignments, Employee
from .models import StudentLeaveApplication, StudentProfile, Attendance, AssignmentSubmission
from accounts.serializers import StandardSerializer, SectionSerializer
from teacher_management.models import LiveClass
from institute.models import Subjects

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", 'first_name']


class StudentSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'sr_no', 'roll_number', 'standard', 'section']


class StudentLeaveApplicationSerializer(serializers.ModelSerializer):
    number_of_days = serializers.SerializerMethodField()
    student= StudentSerializer(read_only =True)
    checked_by = EmployeeSerializer(read_only =True)
    class Meta:
        model = StudentLeaveApplication
        fields = ['id', 'start_date', 'end_date', 'leaving_reason', 'attachment',
                'is_approved', 'number_of_days', 'student', 'checked_by']

    def get_number_of_days(self, obj):
        if obj.start_date and obj.end_date:
            delta = (obj.end_date - obj.start_date).days + 1
            return delta
        return 0

class StudentLeaveApplicationSerializerSaveData(serializers.ModelSerializer):
    class Meta:
        model = StudentLeaveApplication
        fields = "__all__"

class TeacherDataSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'mobile_number', 'employee_image', 'subject', 'experience']

    def get_subject(self, obj):
        return "English"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields= ['id', 'name']

class LiveClassTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= ['id', 'first_name', 'last_name', 'mobile_number']

class LiveClassesSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    employee = LiveClassTeacherSerializer(read_only=True)
    class Meta:
        model = LiveClass
        fields = ['id','chapter', 'message', 'class_date', 'class_time', 'subject', 'employee']

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['institute', 'branch', 'session', 'student', 'status', 'remarks', 'date', 'attachment']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = ['institute', 'branch', 'session', 'employee', 'standard', 'section', 'subject', 'submission_date', 'message', 'attachment']
