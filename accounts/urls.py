from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .api_views import *

app_name = "accounts"

urlpatterns = [
    path('', home, name = "home"),
    path('admin-login', admin_login, name='super-admin-login'),
    path('dashboard/', admin_dashboard, name='admin-dashboard'),
    path('logout/', logout_view, name='logout'),

    # Institute Urls
    path('institute-create/', InstituteRegisterView.as_view(), name='add_institute'),
    path('institute-list/', InstituteList.as_view(), name='institute_list'),
    path('institute-update/<int:pk>/', InstituteUpdateView.as_view(), name="institute_update"),
    path('institute-delete/<int:pk>/', InstituteDeleteView.as_view(), name="institute_delete"),

    #mobile app api urls
    path("student-login", student_login_view, name= "student_login")
]
