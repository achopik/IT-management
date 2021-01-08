from celery import shared_task

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import reverse
from django.template.loader import get_template

from .tokens import create_token


@shared_task
def send_confirmation_mail(user_id):
    user = User.objects.get(id=user_id)
    token = create_token(user)
    url = "http://localhost:8000" + reverse(
        "activate",
        kwargs={"token": token}
    )

    message = get_template("registration/activation_email.html").render(
        {"activation_url": url,
         "username": user.username}
    )

    mail = EmailMessage(
        "Trading Service Email Confirmation",
        message,
        to=[user.email],
        from_email=settings.EMAIL_HOST_USER,
    )
    mail.content_subtype = "html"
    mail.send()


@shared_task
def send_password_reset_mail(user_id):
    user = User.objects.get(id=user_id)
    token = create_token(user)
    url = "http://localhost:8000" + reverse(
        "confirm_reset_password",
        kwargs={"token": token}
    )

    message = get_template("registration/reset_email.html").render(
        {"confirm_url": url,
         "username": user.username}
    )

    mail = EmailMessage(
        "Trading Service Password Reset",
        message,
        to=[user.email],
        from_email=settings.EMAIL_HOST_USER,
    )
    mail.content_subtype = "html"
    mail.send()
