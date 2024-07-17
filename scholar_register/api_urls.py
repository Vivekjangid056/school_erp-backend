from django.urls import path
from .api_views import *

app_name = "api"

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
]