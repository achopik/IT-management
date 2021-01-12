from django.urls import path

from rest_framework.routers import SimpleRouter
import rest_framework_simplejwt.views as jwt_views

from registration.views import (
    UserRegisterView,
    ActivationView,
    PasswordResetView,
    PasswordResetConfirmView,
)


# flake8: noqa: E501
urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("activate/<str:token>/", ActivationView.as_view(), name="activate"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("reset-password/", PasswordResetView.as_view(), name="reset_password"),
    path("reset-password/<str:token>/", PasswordResetConfirmView.as_view(), name="confirm_reset_password"),
]
