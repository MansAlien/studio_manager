from django.contrib.auth.models import User
from rest_framework import serializers
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
        logged_in_user, created= LoggedInUser.objects.get_or_create(user=user_rec)
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

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email", "username", "password", "is_active", "user_permissions", "is_superuser"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', "is_active", "is_superuser"]
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Pop the password out of validated_data to handle it separately
        password = validated_data.pop('password')
        user = User(**validated_data)
        # Set the password using Django's set_password() to hash it
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # If password is provided in the update, hash it properly
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    job_title_name = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile 
        fields = ["id", "job_title", "job_title_name", "city", "date_of_birth", "start", "address", "age", "gender", "salary", "user"]

    def get_job_title_name(self, obj):
        return obj.job_title.name if obj.job_title else None

class EmployeeDataSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()
    job_title_name = serializers.SerializerMethodField()
    is_online = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'id', 'is_superuser', 'is_active',
            'username', 'name', 'job_title',
            'job_title_name', 'age', 'gender',
            'salary', 'is_online'
        ]

    def get_name(self, obj):
        """Returns the full name by combining first_name and last_name from User model."""
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_username(self, obj):
        """Returns the username from User model."""
        return obj.user.username

    def get_is_superuser(self, obj):
        """Returns the is_superuser from User model."""
        return obj.user.is_superuser

    def get_is_active(self, obj):
        """Returns the is_active from User model."""
        return obj.user.is_active

    def get_job_title_name(self, obj):
        """Returns the job title name if it exists."""
        return obj.job_title.name if obj.job_title else None

    def get_is_online(self, obj):
        """Fetch the online status from the LoggedInUser model."""
        logged_in_user = LoggedInUser.objects.filter(user=obj.user).first()
        return logged_in_user.is_online if logged_in_user else False

class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlacklistedAccessToken 
        fields = ["token"]
