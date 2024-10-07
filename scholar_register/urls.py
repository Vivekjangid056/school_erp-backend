from django.urls import path
from .views import *
app_name = 'students'  # This sets the application namespace
urlpatterns = [
    path('student-list/', student_list, name='list_of_students'),
    path('student-register/', student_register, name='student_register'),
    path('student-update/<int:pk>/', student_update, name='student_update'),
    path('student-delete/<int:pk>/', student_delete, name='student_delete'),

    # student complaint urls
    path('complaint-register/<int:student_id>/<int:institute_id>/<int:branch_id>/<int:session_id>/', 
        student_suggestion_complaint, name ='student_suggestion_complaint'),
    path('complaint-update', update_suggestion_complaint, name ='update_suggestion_complaint'),
    path('complaint-delete', delete_suggestion_complaint, name ='delete_suggestion_complaint'),
]