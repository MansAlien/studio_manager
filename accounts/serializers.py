from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token
        token['username'] = user.username
        token['user_id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser

        # Get user permissions
        permissions = user.user_permissions.values_list('codename', flat=True)
        token['permissions'] = list(permissions)  # Converting to a list for serialization

        # Update the LoggedInUser model to reflect that the user is "online"
        logged_in_user, created = LoggedInUser.objects.get_or_create(user=user)
        
        # Store the token's unique ID (jti) as the session_key to mark the user as online
        logged_in_user.session_key = token['jti']
        logged_in_user.save()

        return token

class LoggedInUserSerializer(serializers.ModelSerializer):
    is_online = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'is_online']
    def get_is_online(self, obj):
        try:
            # Check if the user has a valid session_key in LoggedInUser model
            logged_in_user = LoggedInUser.objects.get(user=obj)
            return logged_in_user.session_key is not None
        except LoggedInUser.DoesNotExist:
            return False

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country 
        fields = "__all__"

class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction 
        fields = "__all__"

class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate 
        fields = "__all__"

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle 
        fields = "__all__"

class JobTitleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitleHistory 
        fields = "__all__"

class SalaryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryHistory 
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password", "is_active", "user_permissions", "is_superuser"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        fields = "__all__"
