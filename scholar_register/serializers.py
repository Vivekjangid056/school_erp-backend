# serializers.py
from rest_framework import serializers
from scholar_register.models import StudentProfile

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
