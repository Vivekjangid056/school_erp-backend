from rest_framework import serializers
from .models import ExamTimeTable
from institute.models import Subjects

class ExamTimeTableSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields=['id', 'name']

class ExamTimeTableSerializer(serializers.ModelSerializer):
    subject = ExamTimeTableSubjectSerializer(read_only = True)
    class Meta:
        model= ExamTimeTable
        fields= ['subject', 'date', 'start_time', 'end_time', 'note', 'venue']