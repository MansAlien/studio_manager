from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.serializers import (
    AttributeSerializer,
    AttributeValueSerializer,
    CategorySerializer,
    ProductLineSerializer,
    ProductSerializer,
    SubCategorySerializer,
)

from .models import (
    Attribute,
    AttributeValue,
    Category,
    Product,
    ProductLine,
    SubCategory,
)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = [IsAuthenticated]

class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    permission_classes = [IsAuthenticated]

class CaterogyViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductLineViewSet(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
    permission_classes = [IsAuthenticated]

class SubCaterogyViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

