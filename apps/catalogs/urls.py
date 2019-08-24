from django.urls import path
from apps.catalogs.views import products_list, product_detail, add_comment_to_product

urlpatterns = [
    path('products/', products_list, name='products-list'),
    path('products/<int:pk>', product_detail, name='product-detail'),
    path('products/<int:pk>/comment', add_comment_to_product, name='add_comment_to_product'),
]