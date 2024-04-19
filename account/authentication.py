from django.contrib.auth.models import User
from account.models import Profile
from django.shortcuts import get_object_or_404


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None

    def get_user(self, id):
        return get_object_or_404(User, pk=id)


# https://python-social-auth.readthedocs.io/en/latest/pipeline.html#extending-the-pipeline

def create_profile(backend, user, response, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    profile, _ = Profile.objects.get_or_create(user=user)
    if backend.name == "twitter":
        profile.photo = response.get("profile_image_url_https")
        profile.save()
