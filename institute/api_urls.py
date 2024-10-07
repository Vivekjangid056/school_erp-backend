from django.urls import path
from .api_views import *

urlpatterns = [
    path('notifications/', send_notifications, name='send_notifications'),

    # url for gallery
    path('gallery/', gallery_items_view, name='gallery_items'),

    # url for timetable
    path('timetable/',get_timetable, name='timetable_list_api'),

    # url for chat apis  
    path('chat-messages/', create_chat_messages, name = 'chat_messages' ),  # Create Chat Message
    path('class-chat-messages/', claas_chat_messages, name='class_chat_messages'),  # fetch Chat Message for class
    path('indivi-chat-messages/', individual_chat_messages, name='indivi_chat_messages'),  # fetch Chat Message for class
]