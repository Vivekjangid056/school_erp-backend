from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from scholar_register.models import *

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(request=self.context.get('request'), username = email, password = password)
            if user:
                if user.is_active and user.role == User.STUDENT:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('user is not active or not a student')
            else:
                raise serializers.ValidationError("Unable to login with given credentials")
        else:
            raise serializers.ValidationError("must include email and password")
        
        return data



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
    class Meta:
        model=StudentProfile
        fields = ['parent', 'branch', 'session' , 'sr_no', 'roll_number', 'first_name', 'middle_name', 
                  'last_name', 'gender', 'dob', 'date_of_admission', 'standard', 'section','enroll_no', 
                  'address1', 'address2', 'pin', 'district', 'state','blood_group', 'house_name', 
                  'student_aadhar', 'student_photo', 'fathers_photo', 'mothers_photo']
