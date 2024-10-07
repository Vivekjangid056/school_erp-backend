from django.urls import path
from .api_views import *

urlpatterns = [
    path("student-login", student_login_view, name="student_login"),
    path("student-dashboard", student_dashboard_view, name="student_dashboard"),
    path('teacherlogin/', teacher_login_view, name='teacher_login'),
    path('teacherlogout/', teacher_logout_view, name='teacher_logout'),
    # path('teacher-dashboard/', teacher_dashboard, name = 'teacher_dashboard'),
    # path('teacher-profile/', teacher_profile, name = 'teacher_profile'),
]