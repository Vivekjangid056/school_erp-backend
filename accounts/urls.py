from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', super_admin_login, name='super-admin-login'),
    path('dashboard/', admin_dashboard, name='admin-dashboard'),
    path('logout/', logout_view, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

