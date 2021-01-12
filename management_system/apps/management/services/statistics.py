from management.models import Employee, Opportunity, OpportunityPriority


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
    Just combines all info about department
    """
    return {
        **count_all_employees_in_department(department_id),
        **count_employees_by_level(department_id)
    }


def count_employees_by_level(department_id: int) -> dict:
    """
    Returns a dictionary containing count of employees by their job level
    Employees are related to a certain department
    """

    levels = ("junior", "middle", "senior")
    result = {}

    for level in levels:
        employees = Employee.objects.filter(working_department_id=department_id)
        result.update(
            {
                f"{level}_level_employees": employees
                .filter(job_level__contains=level)
                .count()
            }
        )
    return result


def count_all_employees_in_department(department_id: int) -> dict:
    return {
        "total_employees": (
            Employee.objects
            .filter(working_department_id=department_id)
            .count()
        )
    }
