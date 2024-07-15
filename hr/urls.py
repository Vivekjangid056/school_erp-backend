from django.urls import path
from .views import *


app_name = 'hr'  # This sets the application namespace

urlpatterns = [
    path('interview-list/',interview_list, name='list_of_interview'),
    path('interview-register/',interview_register, name='registration_of_interview'),
    path('interview-update/<int:pk>/',interview_update, name='update_interview'),
    path('interview-delete/<int:pk>/',interview_delete, name='delete_interview'),
]