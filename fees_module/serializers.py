from rest_framework import serializers
from .models import PaymentSchedule


class PaymentScheduleSerializer(serializers.ModelSerializer):
    payment_date = serializers.DateField(format="%Y-%m-%d")
    payment_due_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model=PaymentSchedule
        fields= "__all__"