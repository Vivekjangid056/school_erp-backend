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

class CasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = ['id', 'name']

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = ['id', 'name']

class MotherTongueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherToungue
        fields = ['id', 'name']

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = ['id', 'name']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name']

class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ['id', 'name']

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentParents
        fields= "__all__"

    
class StudentSerializer(serializers.ModelSerializer):
    parent = ParentSerializer(read_only=True)
    branch = InstituteBranchSerializer(read_only=True)
    caste = CasteSerializer(read_only=True)
    religion = ReligionSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    nationality = NationalitySerializer(read_only=True)
    mother_tongue = MotherTongueSerializer(read_only=True)
    standard = StandardSerializer(read_only=True)
    section = SectionSerializer(read_only=True)
    medium = MediumSerializer(read_only=True)
    house_name = HouseSerializer(read_only=True)
    class Meta:
        model=StudentProfile
        fields = "__all__"
    
    def get_session(self, obj):
        if isinstance(obj.session, AcademicSession):
            return AcademicSessionSerializer(obj.session).data
        return obj.session  # In case session is somehow a string, return it as is