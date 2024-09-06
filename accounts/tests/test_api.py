from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from accounts.models import (
    City,
    Country,
    Deduction,
    Governorate,
    JobTitle,
    JobTitleHistory,
    UserProfile,
)
from accounts.serializers import (
    CitySerializer,
    CountrySerializer,
    DeductionSerializer,
    GovernrateSerializer,
    JobTitleHistorySerializer,
    JobTitleSerializer,
)

from .base_test import BaseAPITestCase


class CityAPITests(BaseAPITestCase):
    model = City
    serializer = CitySerializer

    def setUp(self):
        super().setUp()
        self.create_data = {"governorate": self.governorate.id, "name": "Test City"}
        self.update_data = {"governorate": self.governorate.id, "name": "Update Test City"}

class CountryAPITests(BaseAPITestCase):
    model = Country
    serializer = CountrySerializer

    def setUp(self):
        super().setUp()
        self.create_data = {"name": "Test Country"}
        self.update_data = {"name": "Update Test Country"}

class GovernorateAPITests(BaseAPITestCase):
    model = Governorate
    serializer = GovernrateSerializer

    def setUp(self):
        super().setUp()
        self.create_data = {"name": "Test Governorate"}
        self.update_data = {"name": "Update Test Governorate"}

class JobTitleAPITests(BaseAPITestCase):
    model = JobTitle
    serializer = JobTitleSerializer

    def setUp(self):
        super().setUp()
        self.create_data = {"name": "Test JobTitle"}
        self.update_data = {"name": "Update Test JobTitle"}

class DeductionAPITests(BaseAPITestCase):
    model = Deduction
    serializer = DeductionSerializer

    def setUp(self):
        super().setUp()
        self.create_data = {"name": "Test Deduction", "amount": 100, "user_profile": self.user.id} 
        self.update_data = {"name": "Test Deduction", "amount": 100, "user_profile": self.user.id} 

