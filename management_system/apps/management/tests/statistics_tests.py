import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from management.models import Opportunity, Department, Employee
from management.services.statistics import (
    get_domain_opportunity_stats,
    get_all_department_stats,
    count_opportunities_by_priorities
)


pytestmark = pytest.mark.django_db(transaction=True, reset_sequences=True)


class DomainStatsTest(APITestCase):

    url = "domain-statistics-detail"

    @pytest.mark.usefixtures("opportunity_obj")
    def test_domain_statistics_endpoint_available(self):
        """
        Checks if we can use opportunity domain statistics endpoint without errors
        """
        opp = Opportunity.objects.first()
        self.__class__.url = reverse(self.url, args=[opp.domain_name])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("opportunity_obj")
    def test_domain_statistics_endpoint_send_data(self):
        """
        Checks if endpoint opportunity domain statistics sends data
        """
        response = self.client.get(self.url)
        opportunity = Opportunity.objects.first()
        self.assertIn(f"{opportunity.domain_name}_count", response.data)
        self.assertEqual(response.data[f"{opportunity.domain_name}_count"], 1)


class StatisticsServicesTest(APITestCase):

    @pytest.mark.usefixtures("department_obj", "employee_obj")
    def test_department_stats_service(self):
        department = Department.objects.first()
        employee = Employee.objects.first()
        employee.working_department = department
        employee.job_level = "junior"
        employee.save()
        result = get_all_department_stats(department.id)
        self.assertIn("junior_level_employees", result)
        self.assertEqual(1, result["junior_level_employees"])

    @pytest.mark.usefixtures("opportunity_obj")
    def test_domain_stats_service(self):
        opportunity = Opportunity.objects.first()
        result = get_domain_opportunity_stats(opportunity.domain_name)
        self.assertIn(f"{opportunity.domain_name}_count", result)
        self.assertEqual(result[f"{opportunity.domain_name}_count"], 1)
