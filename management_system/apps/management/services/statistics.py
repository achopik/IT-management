from django.db.models import Count, Q

from management.models import Employee, Opportunity, OpportunityPriority, Department


def count_opportunities_by_priorities() -> dict:
    """
    Returns a dictionary containing count of all priority opportunities
    """

    result = {}
    for attr in OpportunityPriority:
        result.update(
            {
                f"{attr.value.lower()}_priority_opportunity":
                    Opportunity.objects.filter(
                        priority=attr.name
                    ).count()
            }
        )
    return result


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

    return {
        f"{domain_name}_opportunities": Opportunity.objects.filter(
            domain_name__icontains=domain_name
        ).count()
    }
