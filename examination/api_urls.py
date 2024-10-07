from django.urls import path
from .api_views import examination_marks_details_students

urlpatterns = [
    path('examination-marks-details-students', examination_marks_details_students, name='examination_marks_details_students')
]