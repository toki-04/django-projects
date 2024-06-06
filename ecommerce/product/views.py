from django.shortcuts import render
from .models import Product

# Create your views here.


def product(request, id):
    product = Product.objects.get(id=id)

    context = {
        "product": product
    }

    return render(request, "product/product.html", context)
