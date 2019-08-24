from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from apps.catalogs.models import Category, Product
from apps.api.serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(ListAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializar_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializar_class = ProductDetailSerializer

