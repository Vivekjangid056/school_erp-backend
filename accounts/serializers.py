from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from scholar_register.models import *
from institute.models import CustomMenu
from teacher_management.models import Employee, EmployeeAttendance, LmDepartmentMaster, LmDesignationMaster

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={
            'required': 'email is required',
            'blank': 'email cannot be blank'
        }
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={
            'required': 'password is required',
            'blank': 'password cannot be blank'
        }
    )

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if user:
                if user.is_active and user.role == User.STUDENT:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("Invalid credentials or user is not a student.")
            else:
                raise serializers.ValidationError("Invalid credentials or user is not a student.")
        else:
            raise serializers.ValidationError("Must include both email and password.")
        
        return data


class InstituteSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='registration_number')
    name = serializers.CharField(source='institute_name')
    class Meta:
        model = Institute
        fields = ['id', 'name']

class InstituteBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteBranch
        fields = ['id', 'name']

class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = ['id', 'name']

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['id', 'name']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name']


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentParents
        fields= ['fathers_name', 'fathers_email', 'fathers_mob_no', 'mothers_name', 'mothers_mob_no', 
                 'mothers_email']
    
class StudentSerializer(serializers.ModelSerializer):
    session = AcademicSessionSerializer(read_only=True)
    parent = ParentSerializer(read_only=True)
    branch = InstituteBranchSerializer(read_only=True)
    standard = StandardSerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    house_name = HouseSerializer(read_only=True)
    institute = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = StudentProfile
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'sr_no', 'roll_number',
                  'gender', 'dob', 'date_of_admission', 'enroll_no', 'address1', 'address2', 'pin', 
                  'district', 'state', 'blood_group', 'house_name', 'student_aadhar', 
                  'student_photo', 'fathers_photo', 'mothers_photo', 'parent', 'institute', 'branch', 'session', 
                  'standard', 'section',]

    def get_institute(self, obj):
        # Get the parent object and extract the institute
        parent = obj.parent
        if parent and parent.institute:
            return InstituteSerializer(parent.institute).data
        return None



class AllStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields =['id', 'first_name', 'middle_name', 'last_name', 'session', 'branch']


class CustomMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomMenu
        fields = ['name', 'url', 'image']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmDesignationMaster
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmDepartmentMaster
        fields = ['id', 'name']

class EmployeeMasterSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only = True)
    designation = DesignationSerializer(read_only = True)
    session = AcademicSessionSerializer(read_only = True)
    branch = InstituteBranchSerializer(read_only = True)
    class Meta:
        model = Employee
        fields = ['session', 'branch','pan_no', 'date_of_birth', 'aadhar_no', 
                  'address_line_1', 'address_line_2', 'designation', 'department']
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAttendance
        fields = ['id', 'name']