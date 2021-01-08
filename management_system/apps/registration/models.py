from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Representing User's profile.
    Currently used as value for email confirmation state
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
