from django.db.models import Count, Q

from management.models import Employee, Opportunity, OpportunityPriority, Department


def count_opportunities_by_priorities() -> dict:
    """
    Returns a dictionary containing count of all priority opportunities
    """

    opportunity_priorities = Opportunity.objects.aggregate(
        **{
            f"{attr.value.lower()}":
                Count('priority', filter=Q(priority=attr.name))
            for attr in OpportunityPriority
        },
    )
    return opportunity_priorities


def get_all_department_stats(department_id: int) -> dict:
    """
    Returns employee total count and counts by level
    """

    levels = ("junior", "middle", "senior")
    statistics = Department.objects.filter(id=department_id).aggregate(
        **{
            f"{level}_level_employees": Count(
                "employee", filter=Q(employee__job_level__iexact=level)
            ) for level in levels
        },
        total_employees=Count("employee")
    )
    return statistics


def get_domain_opportunity_stats(domain_name: str) -> dict:
    """
    Returns info about opportunities by a specified domain
    """

    return Opportunity.objects.aggregate(
        **{
            f"{domain_name}_count":
                Count('domain_name', filter=Q(domain_name__icontains=domain_name))
        }
    )
