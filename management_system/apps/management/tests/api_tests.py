import pytest

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase


pytestmark = pytest.mark.django_db(transaction=True, reset_sequences=True)


class LocationTests(APITestCase):

    url = reverse("location-detail", args=["1"])

    @pytest.mark.usefixtures("location_obj")
    def test_location_endpoint_available(self):
        """
        Checks if we can get location endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("location_obj")
    def test_location_list(self):
        """
        Checks if location detail endpoint sends data
        """
        response = self.client.get(self.url)
        print(response.data)
        self.assertGreater(len(response.data), 3)


class TechnologyTest(APITestCase):

    url = reverse("technology-detail", args=["1"])

    @pytest.mark.usefixtures("technology_obj")
    def test_technology_endpoint_available(self):
        """
        Checks if we can use technology endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("technology_obj")
    def test_get_technology_detail(self):
        """
        Checks if technology list endpoint sends data
        """
        response = self.client.get(self.url)
        self.assertIn('name', response.data.keys())


class GroupTest(APITestCase):

    url = reverse("group-detail", args=["1"])

    @pytest.mark.usefixtures("group_obj")
    def test_group_endpoint_available(self):
        """
        Checks if we can use group endpoint without errors
        """
        response = self.client.get(self.url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("group_obj")
    def test_group_detail(self):
        """
        Checks if endpoint "group detail" sends data
        """
        response = self.client.get(self.url)
        self.assertGreater(len(response.data), 1)


class SkillTest(APITestCase):

    url = reverse("skill-detail", args=["1"])

    @pytest.mark.usefixtures("skill_obj")
    def test_skill_endpoint_available(self):
        """
        Checks if we can use skill endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("skill_obj")
    def test_skill_list(self):
        """
        Checks if endpoint skill detail sends data
        """
        response = self.client.get(self.url)
        self.assertGreater(len(response.data), 2)


class EmployeeTest(APITestCase):

    url = reverse("employee-list")

    @pytest.mark.usefixtures("employee_obj")
    def test_employee_endpoint_available(self):
        """
        Checks if we can use employee endpoint without errors
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.usefixtures("employee_obj")
    def test_employee_list(self):
        """
        Checks if endpoint "employee list" sends data
        """
        response = self.client.get(self.url)
        self.assertGreater(len(response.data), 3)
