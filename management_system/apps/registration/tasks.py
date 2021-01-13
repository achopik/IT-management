from celery import shared_task

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import reverse
from django.template.loader import get_template

from registration.tokens import TokenWorker


class MailSender:
    """
    Base class for mail sending. Override:
    template_path, view_name, subject to get needed functionality.

    Use send_mail() method to send mail and
    Use <Child class name>(user_id) to re-initialize sender.
    Class can have only one instance for performance purposes.
    Do not override __new__ method in order to save that property
    """

    mail_class = EmailMessage
    url_template = "http://localhost:8000"
    template_path = None
    view_name = None
    subject = None

    def __init__(self, user_id):
        self.user = User.objects.get(id=user_id)
        self.token = TokenWorker.create_token(self.user)
        self.url = self.generate_url(viewname=self.view_name, token=self.token)
        self.context = self.generate_mail_context()
        self.message = self.get_message_template(**self.context)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MailSender, cls).__new__(cls)
        cls.instance.__init__(kwargs['user_id'])
        return cls.instance

    def get_message_template(self, **kwargs):
        assert self.template_path is not None, "Template path can't be blank"
        return get_template(self.template_path).render(kwargs)

    def generate_url(self, **kwargs):
        assert 'viewname' in kwargs, "Can't produce a url without a viewname"
        return self.url_template + reverse(
            kwargs.pop('viewname'),
            kwargs=kwargs
        )

    def generate_mail_context(self):
        return {
            "message_url": self.url,
            "username": self.user.username
        }

    def send_mail(self):
        mail = self.mail_class(
            self.subject or "IT-management mailing service",
            self.message,
            to=(self.user.email, ),
            from_email=settings.EMAIL_HOST_USER
        )
        mail.content_subtype = "html"
        mail.send()


class ConfirmationEmailSender(MailSender):
    template_path = "registration/activation_email.html"
    view_name = "activate"
    subject = "IT-management Service Email Confirmation"


class PasswordResetEmailSender(MailSender):
    template_path = "registration/reset_email.html"
    view_name = "confirm_reset_password"
    subject = "IT-management Service Password Reset"


"""
Celery task wrappers for senders
"""


@shared_task
def send_confirmation_mail(user_id):
    sender = ConfirmationEmailSender(user_id=user_id)
    sender.send_mail()


@shared_task
def send_password_reset_mail(user_id):
    sender = PasswordResetEmailSender(user_id=user_id)
    sender.send_mail()
