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
    path('institute-create/', institute_register_view, name='add_institute'),
    path('institute-list/', InstituteList.as_view(), name='institute_list'),
    path('institute-update/<int:pk>/', institute_update, name="institute_update"),
    path('institute-delete/<int:pk>/', InstituteDeleteView.as_view(), name="institute_delete"),

    path("student-login", student_login_view, name= "student_login"),
    # Branch Urls
    path('branch-create', institute_branch_create_view, name = 'add_branch'),
    path('branches_list', branches_list, name = 'list_of_branches'),
    path('branch-update/<int:pk>', institute_branch_update_view, name= 'branch_update'),
    path('branch-delete/<int:pk>', institute_branch_delete_view, name = 'branch_delete'),
    path('branch-change/', change_branch, name='change_branch'),

    #Session Urls
    path('session-create', session_create, name = 'add_session'),
    path('session-list', sessions_list, name = 'list_of_sessions'),
    path('session-update/<int:pk>', session_update, name = 'session_update'),
    path('session-delete/<int:pk>', session_delete, name = 'session_delete'),
    path('session-change/', change_session, name = 'session_change'),
]
