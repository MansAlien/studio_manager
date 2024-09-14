from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

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


def check_permission(user, model_name, permission_type="view"):
    """Check if the user has the specified permission for a given model."""
    permission_codename = f"{permission_type}_{model_name.lower()}"
    if not user.has_perm(f'accounts.{permission_codename}'):
        raise PermissionDenied(f"You do not have permission to {permission_type} {model_name}.")

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
            check_permission(self.request.user, 'city')
            return super().get_queryset()

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            check_permission(self.request.user, 'country')
            return super().get_queryset()

class DeductionViewSet(viewsets.ModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            check_permission(self.request.user, 'deduction')
            return super().get_queryset()
    
class GovernorateViewSet(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
            check_permission(self.request.user, 'governorate')
            return super().get_queryset()

class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            check_permission(self.request.user, 'jobtitle')
            return super().get_queryset()
    
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
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
            check_permission(self.request.user, 'user')
            return super().get_queryset()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            check_permission(self.request.user, 'userprofile')
            return super().get_queryset()
