from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    City,
    Country,
    Deduction,
    Governorate,
    JobTitle,
    JobTitleHistory,
    LoggedInUser,
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
    LoggedInUserSerializer,
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

class LoggedInUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoggedInUserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            check_permission(self.request.user, 'userprofile')
            return super().get_queryset()

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the user's LoggedInUser entry
            user = request.user
            logged_in_user = LoggedInUser.objects.get(user=user)
            
            # Clear the session_key to mark the user as "offline"
            logged_in_user.session_key = None
            logged_in_user.save()

            # Blacklist the refresh token if using JWT Blacklist
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
