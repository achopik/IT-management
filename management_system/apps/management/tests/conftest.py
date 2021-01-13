from datetime import date

from mixer.backend.django import mixer

import pytest

from management.models import (
    Department, Employee, Group,
    Location, Opportunity, Position,
    PositionStatus, Project, Skill,
    Team, Technology,
)


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def technology_obj():
    return mixer.blend(Technology)


@pytest.fixture
def skill_obj(technology_obj):
    return mixer.blend(Skill, technology=technology_obj)


@pytest.fixture
def location_obj():
    return mixer.blend(Location)


@pytest.fixture
def department_obj():
    return mixer.blend(Department)


@pytest.fixture
def employee_obj(location_obj, technology_obj):
    return Employee.objects.create(
        location=location_obj,
        main_technology=technology_obj,
        employment_duration=20,
        utilization_rate=20,
        workload=20,
    )


@pytest.fixture
def group_obj(employee_obj):
    return mixer.blend(Group, lead=employee_obj)


@pytest.fixture
def team_obj(employee_obj):
    return mixer.blend(Team, lead=employee_obj)


@pytest.fixture
def opportunity_obj(location_obj):
    return mixer.blend(
        Opportunity,
        location=location_obj,
        staffing_location=location_obj
    )


@pytest.fixture
def position_obj(opportunity_obj, employee_obj, location_obj):
    return mixer.blend(
        Position,
        opportunity=opportunity_obj,
        assignment=employee_obj,
        location=location_obj,
        supervisor=employee_obj,
    )


@pytest.fixture
def project_obj(opportunity_obj, department_obj, employee_obj):
    return mixer.blend(
        Project,
        opportunity=opportunity_obj,
        department=department_obj,
        account_manager=employee_obj,
        project_manager=employee_obj,
    )
