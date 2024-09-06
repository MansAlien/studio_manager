from django.contrib.auth.models import User
from rest_framework import serializers

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
        fields = ["username", "password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        fields = "__all__"
