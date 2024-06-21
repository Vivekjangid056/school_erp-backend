"""
URL configuration for School_Erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path("", include("accounts.urls")),
    path("dashboard/", include("institute.urls")),
    # path("dashboard/", include("enquiry.urls")),
    # path("dashboard/", include("finance.urls")),
    # path("dashboard/", include("fees_modules.urls")),
    # path("dashboard/", include("teacher_management.urls")),
    # path("dashboard/", include("hr.urls")),
    # path("dashboard/", include("examination.urls")),
    # path("dashboard/", include("library.urls")),
    # path("dashboard/", include("transport.urls")),
    # path("dashboard/", include("hostel.urls")),
    # path("dashboard/", include("attendance.urls")),
    # path("dashboard/", include("mobile_module.urls")),
    # path("dashboard/", include("scholar_register.urls")),
    # path("dashboard/", include("online_exam.urls")),
    # path("dashboard/", include("store_inventory.urls")),
    # path("dashboard/", include("task_management.urls")),
    # path("dashboard/", include("visitor_master.urls")),
]
