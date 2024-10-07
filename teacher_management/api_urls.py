from django.urls import path
from .api_views import *

urlpatterns = [
    path('today-live-class-create/', today_live_class_create, name = 'today_live_class_create'),
    path('create-assignment/', create_assignment, name='create_assignment'),
    path('filter-data-for-teacher-assignment-list/', filter_data_for_teacher_assignment_list, name='filter_data_for_teacher_assignment_list'),
    path('assignment-approve-reject/', assignment_approve_reject, name= 'assignment_approve_reject'),
    path('assignment-submission-details', assignment_submission_details, name='assignment_submission_details')
]