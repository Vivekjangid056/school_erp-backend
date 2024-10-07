from django.urls import path
from .api_views import get_student_fees_details


urlpatterns=[
    path('student-fees-details/', get_student_fees_details, name='get_student_fees_details'),
]