from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AttributeValueViewSet,
    AttributeViewSet,
    CaterogyViewSet,
    ProductLineViewSet,
    ProductViewSet,
    SubCaterogyViewSet,
)

router = DefaultRouter()
router.register(r'attribue', AttributeViewSet)
router.register(r'attribue_value', AttributeValueViewSet)
router.register(r'category', CaterogyViewSet)
router.register(r'product', ProductViewSet)
router.register(r'product_line', ProductLineViewSet)
router.register(r'sub_category', SubCaterogyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
