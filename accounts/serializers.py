from django.contrib.auth.models import User
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import (
    BlacklistedAccessToken,
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
        token['username'] = user.username
        token['user_id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        permissions = user.user_permissions.values_list('codename', flat=True)
        token['permissions'] = list(permissions)  # Converting to a list for serialization

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        user_rec = User.objects.get(username=user)
        logged_in_user= LoggedInUser.objects.get(user=user_rec)
        user_rec = logged_in_user.user
        
        # If the user already has an access token, blacklist the old token
        if logged_in_user.access_token:
            try:
                old_token = logged_in_user.access_token
                BlacklistedAccessToken.objects.create(token=old_token)
                print(f"Blacklisted old token for user {user_rec.username}")

            except Exception as e:
                print(f"Error blacklisting token: {e}")

        # Store the new access token in LoggedInUser
        logged_in_user.access_token = data['access']
        logged_in_user.is_online = True
        logged_in_user.save()

        return data

class LoggedInUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggedInUser
        fields = "__all__"

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

class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlacklistedAccessToken 
        fields = ["token"]
