from django.db import models


class Location(models.Model):
    """
    Represents a geographic location of something
    """

    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    office = models.CharField(max_length=255)


class Technology(models.Model):
    """
    Represents a certain technology
    """

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Skill(models.Model):
    """
    Represents a certain skill in some technology
    """
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE
    )
    skill = models.CharField(
        max_length=255,
        verbose_name="A certain skill description"
    )


class Group(models.Model):
    """
    A certain group with its lead
    """

    name = models.CharField(max_length=255)
    lead = models.ForeignKey(
        "management.Employee",
        on_delete=models.SET_NULL,
        null=True
    )
    utilization_current = models.PositiveSmallIntegerField()


class Team(Group):
    """
    A team with its lead and target
    """

    utilization_target = models.ForeignKey(
        Technology,
        on_delete=models.SET_NULL,
        null=True
    )
