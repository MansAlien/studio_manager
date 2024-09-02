from rest_framework import serializers

from .models import Country, Governorate, JobTitle


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle 
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country 
        fields = "__all__"

class GovernrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate 
        fields = "__all__"
