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
    SalaryHistory,
    UserProfile,
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        
        permissions = user.user_permissions.values_list('codename', flat=True)
        token['permissions'] = list(permissions)  # Converting to a list for serialization
        return token

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
