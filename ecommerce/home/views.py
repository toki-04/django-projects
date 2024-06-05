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
    product = Product.objects.all()

    context = {
        "product": product
    }

    return render(request, "home/index.html", context)
