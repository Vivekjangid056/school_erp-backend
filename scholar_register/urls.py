from django.urls import path
from .views import *
from . import views


app_name = 'students'  # This sets the application namespace

urlpatterns = [
    path('student-list/', views.student_list, name='list_of_students'),
    path('student-register/',views.student_register, name='student_register'),
]
