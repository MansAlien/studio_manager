from accounts.models import City, Country, Governorate, JobTitle
from accounts.serializers import (
    CitySerializer,
    CountrySerializer,
    GovernrateSerializer,
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
