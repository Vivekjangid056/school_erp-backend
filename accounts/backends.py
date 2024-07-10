from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from accounts.models import User


class SecondaryEmailBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user_instance = User.objects.get(secondary_email=email)
            user = user_instance.admin
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
