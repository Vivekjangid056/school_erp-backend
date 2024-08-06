from rest_framework import serializers
from .models import Employee, EmployeeMaster


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'