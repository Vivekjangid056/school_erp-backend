from rest_framework import serializers
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"
        
class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GalleryItems
        fields = ['name','image','video','url_tag']