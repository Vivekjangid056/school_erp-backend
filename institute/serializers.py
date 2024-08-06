from rest_framework import serializers

from hr.models import TimeTable
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"
        
class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GalleryItems
        fields = ['name','image','video','url_tag']
        
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
        fields = ['institute','sender','receiver','standard','section','message_type','message','is_individual','time_stamp']
        
    def validate_message_type(self, value):
        if value not in dict(ChatMessage.MESSAGE_TYPES).keys():
            raise serializers.ValidationError("Invalid message type.")
        return value
    
    def validate(self, data):
        # Ensure the standard and section fields are always included
        if 'standard' not in data or data['standard'] is None:
            raise serializers.ValidationError({'standard': 'Standard Id is required'})
        if 'section' not in data or data['section'] is None:
            raise serializers.ValidationError({'section': 'Section Id is required'})
        
        # Conditional validation based on is_individual
        is_individual = data.get('is_individual', False)
        if is_individual:
            if 'receiver' not in data or data['receiver'] is None:
                raise serializers.ValidationError({'receiver': 'Receiver Id is required when is_individual is True'})
        else:
            if 'receiver' in data:
                raise serializers.ValidationError({'receiver': 'Receiver Id should not be provided when is_individual is False'})

        # Validation for message type
        if data['message_type'] == 'image':
            if not data['message'].startswith('https://') and not data['message'].startswith('http://'):
                raise serializers.ValidationError({'message': 'Image URL must start with http:// or https://'})

        return data    
    
    # def save(self, *args, **kwargs):
    #     sender = kwargs.pop['sender', None]
    #     receiver = kwargs.pop['receiver', None]
    #     super().save(*args, **kwargs)
    #     if self.sender or self.receiver:
    #         if self.sender.user_is == "5" or self.receiver