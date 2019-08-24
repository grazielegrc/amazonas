from django.shortcuts import render
from apps.catalogs.models import Product

def products_list(request):
    products = Product.objects.filter(published_at__isnull=False).order_by('description')
    return render(request, 'catalogs/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalogs/product_detail.html', {'product': product})