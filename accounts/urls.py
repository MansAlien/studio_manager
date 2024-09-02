from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, GovernorateViewSet, JobTitleViewSet

router = DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'governorate', GovernorateViewSet)
router.register(r'job_title', JobTitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
