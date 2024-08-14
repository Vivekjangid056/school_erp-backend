from django.urls import path
from .api_views import login_view, logout_view



urlpatterns = [
    path('teacher/login/', login_view, name='login'),
    path('teacher/logout/', logout_view, name='logout'),
] 
