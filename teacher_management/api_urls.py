from django.urls import path
from .emp_views import login_view



urlpatterns = [
    path('teacherlogin/', login_view, name='login'),
] 