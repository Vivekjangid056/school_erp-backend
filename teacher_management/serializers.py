from rest_framework import serializers
from .models import Employee, EmployeeMaster

class EmployeeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    employee_name = EmployeeMasterSerializer()

    class Meta:
        model = Employee
        fields = '__all__'