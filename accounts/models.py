from django.conf import settings
from django.contrib.auth import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class JobTitle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Governorate(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    governorate = models.ForeignKey(Governorate, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    GENDER = {
        "M": "Male",
        "F": "Female",
    }
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    # department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True)
    start = models.DateField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    age = models.PositiveIntegerField(null=True)
    salary = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.user.username

class JobTitleHistory(models.Model):
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user_profile} - {self.job_title}"


class SalaryHistory(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user_profile} - {self.amount}"


class Deduction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discription = models.TextField(default="")
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        User, related_name="logged_in_user", on_delete=models.CASCADE
    )
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username

