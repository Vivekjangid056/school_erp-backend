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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path("", include("accounts.urls")),
    path("dashboard/", include("institute.urls")),
    path("dashboard/", include("scholar_register.urls")),
    path("dashboard/", include("teacher_management.urls")),

    # registering the corresponding api urls files
    path("dashboard/api/", include('institute.api_urls')),
    path("dashboard/api/", include('scholar_register.api_urls')),
    # path("dashboard/api/", include('teacher_management.api_urls')),
    path("api/", include('accounts.api_urls')),
    path("dashboard/", include("hr.urls")),
    # urls for apis
    path("api/", include("teacher_management.api_urls")),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

