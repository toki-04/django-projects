from django.http import JsonResponse
from django.shortcuts import render

from product.models import Product
from product.api.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def product_list(request, format=None):
    if request.method == "GET":
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data)


def index(request):
    # 1 - light, 2 - medium, 3 - dark
    filter_roast = 2

    # 1 - 12, 2 - 16, 3 - 32
    filter_size = 2

    # 1 - decaf, 2 - easy-late, 3 - ground, 4 - organic
    # 5 - reserved, 6 - seasonal, 7 - whole-bean
    filter_coffee_type = 2

    product = Product.objects.all()
    if filter_roast:
        product = product.filter(roast__id=filter_roast)
    if filter_size:
        product = product.filter(size__id=filter_size)
    if filter_coffee_type:
        product = product.filter(coffee_type__id=filter_coffee_type)

    context = {
        "product": product
    }

    return render(request, "home/index.html", context)
