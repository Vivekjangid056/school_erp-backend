from rest_framework import serializers
from hr.models import TimeTable
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"

class GalleryItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryItems
        fields = ['id', 'name', 'type', 'url_tag', 'image_url', 'video_url', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video:
            return request.build_absolute_uri(obj.video.url)
        return None


class TimeTableSerializer(serializers.ModelSerializer):
    standard = serializers.CharField(source='standard.name')
    section = serializers.CharField(source='section.name')
    subject = serializers.CharField(source='subject.name')
    faculty = serializers.CharField(source='faculty.user.first_name')

    class Meta:
        model = TimeTable
        fields = [ 'standard', 'section', 'period_no', 'start_time', 'end_time', 'subject', 'faculty']

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields="__all__"

class StudentClassChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields=['id', 'first_name', 'student_photo']


class ClassChatMessageSerializer(serializers.ModelSerializer):
    student = StudentClassChatSerializer(read_only = True)
    class Meta:
        model = ChatMessage
        fields=['institute', 'branch', 'session', 'sender', 'standard', 'section', 'message_type', 'message', 'is_individual', 'time_stamp', 'student']