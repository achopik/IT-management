from typing import Union

from django.contrib.auth.models import User

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


class TokenWorker:
    """
    Class providing static methods for generation and confirmation of JWT
    """

    @classmethod
    def check_token(cls, token) -> Union[int, bool]:
        """
        Returns user id and confirms user if token is valid and user exists
        """

        uid = cls._get_user_id(token)
        user = User.objects.get(id=uid)
        if uid and user:
            user.profile.is_confirmed = True
            user.profile.save()
            return uid
        return False

    @staticmethod
    def create_token(user) -> str:
        """
        Generates token for a certain user
        """
        token = AccessToken.for_user(user)
        return str(token)

    @staticmethod
    def _get_user_id(token) -> Union[int, bool]:
        try:
            user_id = AccessToken(token, verify=True).get('user_id')
            return user_id
        except TokenError:
            return False
