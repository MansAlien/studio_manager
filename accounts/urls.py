from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CityViewSet,
    CountryViewSet,
    DeductionViewSet,
    GovernorateViewSet,
    JobTitleHistoryViewSet,
    JobTitleViewSet,
    SalaryHistoryViewSet,
    UserProfileViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'country', CountryViewSet)
router.register(r'deduction', DeductionViewSet)
router.register(r'governorate', GovernorateViewSet)
router.register(r'job_title', JobTitleViewSet)
router.register(r'job_title_history', JobTitleHistoryViewSet)
router.register(r'salary_history', SalaryHistoryViewSet)
router.register(r'user', UserViewSet)
router.register(r'user_profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
