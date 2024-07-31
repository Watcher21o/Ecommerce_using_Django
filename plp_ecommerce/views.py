from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'plp_ecommerce/product_list.html',context)