from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from accounts.models import (
    City,
    Country,
    Deduction,
    Governorate,
    JobTitle,
    UserProfile,
)


class BaseAPITestCase(APITestCase):
    model = None
    serializer = None
    create_data = {}
    update_data = {}
    detail_field = "name"

    #SetUp
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="123456")
        self.user_profile = UserProfile.objects.get(id=self.user.id)
        self.deduction = Deduction.objects.create(user_profile=self.user_profile, name="Test Deduction", amount=100)
        self.client.login(username="testuser", password="123456")
        self.country = Country.objects.create(name="Test Country")
        self.governorate = Governorate.objects.create(country=self.country, name="Test Governorate")
        self.city = City.objects.create(governorate=self.governorate, name="Test City")
        self.job_title = JobTitle.objects.create(name="Test JobTitle")

    def get_url(self, action, **kwargs):
        return reverse(f"{self.model.__name__.lower()}-{action}", kwargs=kwargs)

    #Create
    def test_create_instance(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        url = self.get_url("list")
        response = self.client.post(url, self.create_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.model.objects.count(), 2)

    #Reade
    def test_get_instance_list(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        url = self.get_url("list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #Reade
    def test_get_instance_detail(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        url = self.get_url("detail", pk=1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[self.detail_field], self.create_data[self.detail_field])

    #Update
    def test_update_instance(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        url = self.get_url("detail", pk=1)
        response = self.client.put(url, self.update_data)
        self.assertEqual(response.status_code, 200)
        updated_instance = self.model.objects.get(pk=1)
        self.assertEqual(getattr(updated_instance, self.detail_field), self.update_data[self.detail_field])

    #Delete
    def test_delete_instance(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        url = self.get_url('detail', pk=1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.model.objects.count(), 0)

    #Unauthenticated
    def test_unauthenticated_access(self):
        if not self.model:
            self.skipTest("Base test case skipped because 'model' is not defined.")
        self.client.logout()
        url = self.get_url('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
