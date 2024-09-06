from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    City,
    Country,
    Deduction,
    Governorate,
    JobTitle,
    JobTitleHistory,
    SalaryHistory,
    UserProfile,
)
from .serializers import (
    CitySerializer,
    CountrySerializer,
    DeductionSerializer,
    GovernorateSerializer,
    JobTitleHistorySerializer,
    JobTitleSerializer,
    SalaryHistorySerializer,
    UserProfileSerializer,
    UserSerializer,
)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class DeductionViewSet(viewsets.ModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer
    permission_classes = [IsAuthenticated]
    
class GovernorateViewSet(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer

class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    permission_classes = [IsAuthenticated]
    
class JobTitleHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobTitleHistory.objects.all()
    serializer_class = JobTitleHistorySerializer
    permission_classes = [IsAuthenticated]

class SalaryHistoryViewSet(viewsets.ModelViewSet):
    queryset = SalaryHistory.objects.all()
    serializer_class = SalaryHistorySerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
