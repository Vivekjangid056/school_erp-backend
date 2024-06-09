from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", super_admin_login, name='super-admin-login'),
    path("dashboard/", admin_dashboard, name = "admin-dashboard")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)