from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts import views

from .views_api import (
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
    path("", views.home, name="home"),
    path('api/accounts/', include(router.urls)),
]
