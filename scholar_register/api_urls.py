from django.urls import path
from .api_views import *

app_name = "api"

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('student-leave-apply/', apply_leave, name='student_leave_apply'),
    path('get-student-leave-applications/', get_leave_applications, name= "get_student_leave_applications"),
    path('student-leave-approval', student_leave_approval, name= "student_leave_approval"),
    path('student-attendance/', student_attendance, name='student_attendance'),
    path('student-activity/', student_activity, name='student_activity'),
    path('faculty-list/', faculty_list, name='faculty_list'),
    path('fetch-live-classes-data/', fetch_live_classes_data, name='fetch_live_classes_data'),
    path('list-assignments-for-student/', list_assignments_for_student, name='list_assignments_for_student'),
    path('submit-assignment/', submit_assignment, name='submit_assignment')
]