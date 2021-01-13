from django.db import models
from django.dispatch import receiver

from management.models import Department, Employee


@receiver(models.signals.pre_save, sender=Department)
def update_utilization(sender, instance, **kwargs):
    instance.utilization_current = (
        Employee.objects
        .filter(department=instance)
        .count()
    )
