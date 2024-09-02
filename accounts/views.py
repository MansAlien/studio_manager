from rest_framework import viewsets

from .models import Country, Governorate, JobTitle
from .serializers import CountrySerializer, GovernrateSerializer, JobTitleSerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class GovernorateViewSet(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernrateSerializer
