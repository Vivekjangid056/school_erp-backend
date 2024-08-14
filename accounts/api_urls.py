from django.urls import path
from .api_views import *

urlpatterns = [
    path("student/login/", student_login_view, name="student_login"),
]