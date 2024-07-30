from django.urls import path
from .api_views import *

urlpatterns = [
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/<int:pk>/', notification_detail, name='notification_detail'),
    
    # url for gallery
    path('gallery/', gallery_list, name='gallery_list'),
]