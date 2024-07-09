from django.urls import path
from .views import *


app_name = 'students'  # This sets the application namespace

urlpatterns = [
    path('student-list/', student_list, name='list_of_students'),
    path('student-register/', student_register, name='student_register'),
    path('student-update/<int:pk>/', student_update, name='student_update'),
    path('student-delete/<int:pk>/', student_delete, name='student_delete'),
]
