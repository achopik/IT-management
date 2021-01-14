import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from management.models import Opportunity


pytestmark = pytest.mark.django_db(transaction=True, reset_sequences=True)


class DepartmentStstsTest(APITestCase):

    url = reverse("department-statistics-detail", args=["1"])

    @pytest.mark.usefixtures("department_obj")
    def test_department_statistics_endpoint_available(self):
        """
        Checks if we can use department statistics endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("department_obj")
    def test_department_statistics_endpoint_send_data(self):
        """
        Checks if endpoint department statistics sends data
        """
        response = self.client.get(self.url)
        self.assertIn("statistics", response.data)
        self.assertIn("total_employees", response.data["statistics"])


class OpportunityStatsTest(APITestCase):

    url = reverse("opportunity-statistics-list")

    @pytest.mark.usefixtures("opportunity_obj")
    def test_opportunity_statistics_endpoint_available(self):
        """
        Checks if we can use opportunity statistics endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("opportunity_obj")
    def test_opportunity_statistics_endpoint_send_data(self):
        """
        Checks if endpoint opportunity statistics sends data
        """
        response = self.client.get(self.url)
        self.assertIn("statistics", response.data)


class DomainStatsTest(APITestCase):

    url = "domain-statistics-detail"

    @pytest.mark.usefixtures("opportunity_obj")
    def test_opportunity_statistics_endpoint_available(self):
        """
        Checks if we can use opportunity statistics endpoint without errors
        """
        opp = Opportunity.objects.first()
        self.__class__.url = reverse(self.url, args=[opp.domain_name])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("opportunity_obj")
    def test_opportunity_statistics_endpoint_send_data(self):
        """
        Checks if endpoint opportunity statistics sends data
        """
        response = self.client.get(self.url)
        self.assertIn("statistics", response.data)
