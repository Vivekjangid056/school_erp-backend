from django.urls import path
from .views import *

urlpatterns = [
    path("/institute-create", add_institute, name= "add_institute"),
    path("/institute-list", institute_list, name="institute_list")
]