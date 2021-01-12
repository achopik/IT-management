from django.db import models

from management.models.basic_models import (
    Location, Skill, Technology
)
from management.models.choices import (
    EnglishLevel, OpportunityPriority, PositionStatus, Sex
)


class Employee(models.Model):
    """
    Represents an employee
    """

    email = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    sex = models.CharField(
        max_length=8,
        choices=Sex.choices(),
        default=Sex.MALE
    )
    birth_date = models.DateField(blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True
    )
    job_title = models.CharField(max_length=255)
    job_level = models.CharField(max_length=100)
    employment_start_date = models.DateField(auto_now_add=True)
    employment_duration = models.PositiveIntegerField(
        verbose_name="employment duration in days"
    )
    military_eligibility = models.BooleanField(default=True)
    military_served = models.BooleanField(default=True)
    military_defferal_status = models.BooleanField(default=True)
    military_defferal_end_date = models.DateField(blank=True, null=True)
    utilization_rate = models.PositiveSmallIntegerField(
        verbose_name="percent of employee's utilization"
    )
    workload = models.PositiveSmallIntegerField(
        verbose_name="percent of employee's workload"
    )
    main_technology = models.ForeignKey(
        Technology,
        on_delete=models.SET_NULL,
        null=True
    )
    technology_skills = models.ManyToManyField(Skill)
    role = models.CharField(max_length=255)
    working_department = models.ForeignKey(
        "management.Department",
        on_delete=models.SET_NULL,
        null=True
    )


class Department(models.Model):
    """
    Represents a develop department
    """
    name = models.CharField(max_length=255)
    resource_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
    )
    head = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="managed_department",
    )
    utilization_current = models.PositiveSmallIntegerField()


class Project(models.Model):
    """
    Represents a certain project
    """

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )
    account_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True
    )
    project_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="managed_project"
    )
    partner_name = models.CharField(max_length=255)
    partner_contact = models.URLField()
    description = models.TextField()
    site_link = models.URLField()
    type = models.CharField(max_length=100)


class Position(models.Model):
    """
    Represents a position in a project
    """

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    assignee_name = models.CharField(max_length=255)
    assignment = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
    )
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True
    )
    status_supervisor = models.CharField(max_length=255)
    supervisor = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="supervised_position"
    )
    status = models.CharField(
        max_length=20,
        choices=PositionStatus.choices(),
        default=PositionStatus.ACTIVE
    )
    english_level = models.CharField(
        max_length=30,
        choices=EnglishLevel.choices(),
        default=EnglishLevel.B2
    )


class Opportunity(models.Model):
    """
    An opportunity of a project realisation
    """

    customer_logo = models.FileField(null=True, blank=True)
    customer_name = models.CharField(max_length=255)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True
    )
    staffing_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name="staffed_opportunity"
    )
    name = models.CharField(max_length=255)
    priority = models.CharField(
        max_length=20,
        choices=OpportunityPriority.choices()
    )
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        verbose_name="related project"
    )
    project_start_date = models.DateField(auto_now_add=True)
    project_duration = models.PositiveIntegerField(
        verbose_name="project duration in days"
    )
    opportunity_probability = models.PositiveSmallIntegerField(
        "Opportunity probability rate in percents"
    )
    technology_name = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=255)
    sales_name = models.CharField(max_length=255)
    delivery_supervisor_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Opportunity"
        verbose_name_plural = "Opportunities"
