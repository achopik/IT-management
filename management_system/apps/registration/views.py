from registration.serializers import (
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    UserRegisterSerializer,
)
from registration.tasks import send_confirmation_mail
from registration.tokens import TokenWorker

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class UserRegisterView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_confirmation_mail.delay(serializer.data["id"])
        headers = self.get_success_headers(serializer.data)

        return Response(
            {
                "message": "User has been created successfully! Check your email.",
                "user": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class ActivationView(generics.RetrieveAPIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        message = {
            "detail": "Registration confirmation error. Please, try again",
        }
        res = TokenWorker.check_token(kwargs['token'])
        if res:
            message["detail"] = "Registration complete. Please login"

        return Response(
            message,
            status=status.HTTP_200_OK
        )


class PasswordResetView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Password reset e-mail has been sent."},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password has been changed"},
            status=status.HTTP_200_OK
        )
