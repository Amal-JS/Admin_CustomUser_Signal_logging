from django.contrib.auth.backends import ModelBackend
from . models import Custom_User  
from django.core.exceptions import ObjectDoesNotExist

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Custom_User.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Custom_User.objects.get(pk=user_id)
        except Custom_User.DoesNotExist:
            return None
