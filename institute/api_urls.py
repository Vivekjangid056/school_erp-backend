from django.urls import path
from .api_views import *

urlpatterns = [
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/<int:pk>/', notification_detail, name='notification_detail'),
    
    # url for gallery
    path('gallery/', gallery_list, name='gallery_list'),
    
    # url for timetable
    path('timetable',timetable_list, name='timetable_list_api'),
    
    # url for chat apis  
    path('chat-messages/', CreateChatMessageView.as_view(), name = 'chat_messages' ),  # Create Chat Message
    path('class-chat-messages/', ClassChatMessageView.as_view(), name='class_chat_messages'),  # fetch Chat Message for class
    path('Indivi-chat-messages/', IndividualChatMessageView.as_view(), name='indivi_chat_messages'),  # fetch Chat Message for class
]