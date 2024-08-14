from django.urls import path
from .api_views import *

urlpatterns = [
    path('notifications/list/', notification_list, name='notification_list'),
    path('notifications/create/', notification_list, name='notification_create'),
    path('notifications/<int:pk>/', notification_detail, name='notification_detail'),
    
    # url for gallery
    path('gallery/list/', gallery_list, name='gallery_list'),
    
    # url for timetable
    path('timetable/list/',timetable_list, name='timetable_list_api'),
    
    # url for chat apis
    path('chat-messages/create/', CreateChatMessageView.as_view(), name = 'chat_messages' ),  # Create Chat Message
    path('chat-messages/class/', ClassChatMessageView.as_view(), name='class_chat_messages'),  # fetch Chat Message for class
    path('chat-messages/individual/', IndividualChatMessageView.as_view(), name='indivi_chat_messages'),  # fetch Chat Message for class
]