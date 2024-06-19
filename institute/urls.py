from django.urls import path
from .views import *

app_name = 'institute'  # Namespace for this app

urlpatterns = [
    path('institute-create/', InstituteRegisterView.as_view(), name='add_institute'),
    path('institute-list/', institute_list, name='institute_list'),
    path('institute-update<int:pk>', InstituteUpdateView.as_view(), name="institute_update"),
    path('institute-delete<int:pk>', InstituteDeleteView.as_view(), name="institute_delete")
]