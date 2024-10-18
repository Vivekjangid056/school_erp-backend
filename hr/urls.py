from django.urls import path
from .views import *


app_name = 'hr'  # This sets the application namespace

urlpatterns = [
    path('interview-list/',interview_list, name='list_of_interview'),
    path('interview-register/',interview_register, name='registration_of_interview'),
    path('interview-update/<int:pk>/',interview_update, name='update_interview'),
    path('interview-delete/<int:pk>/',interview_delete, name='delete_interview'),
    
    path('student-id-card-list',student_id_card_list,name='student_id_card_list'),
    path('student-id-card-view/<int:pk>/',student_id_card_view,name='student_id_card_view'),
    
    path('teacher-id-card-list',teacher_id_card_list,name='teacher_id_card_list'),
    path('teacher-id-card-view/<int:pk>/',teacher_id_card_view,name='teacher_id_card'),
]