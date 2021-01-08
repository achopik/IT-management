from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from registration.tasks import send_password_reset_mail
from registration.tokens import check_token

from rest_framework import serializers
from rest_framework.validators import ValidationError


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email"
        )

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Account with given email already exists"
            )
        return value


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    @staticmethod
    def validate_email(value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account with given email")
        return value

    def save(self, **kwargs):
        email = self.data['email']
        user = User.objects.get(email=email)
        send_password_reset_mail.delay(user.id)

    def update(self, instance, validated_data):
        pass  # No instances to update

    def create(self, validated_data):
        pass  # No instances to create


class PasswordResetConfirmSerializer(serializers.Serializer):

    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    def validate(self, attrs):

        password1 = attrs['new_password1']
        password2 = attrs['new_password2']

        try:
            token = self.context.get('view').kwargs['token']
            uid = check_token(token)
            self.user = User.objects.get(id=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({'token': ['Invalid value']})

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Passwords don't match")
        password_validation.validate_password(password1, self.user)
        self.password = password1
        return attrs

    def save(self):
        self.user.set_password(self.password)
        self.user.save()

    def create(self, validated_data):
        pass  # No instances to update

    def update(self, instance, validated_data):
        pass  # No instances to create
