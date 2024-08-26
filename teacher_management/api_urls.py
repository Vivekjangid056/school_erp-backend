from django.urls import path
from .api_views import login_view, logout_view



urlpatterns = [
    path('teacherlogin/', login_view, name='login'),
    path('teacherlogout/', logout_view, name='logout'),
] 
