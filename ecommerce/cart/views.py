from django.shortcuts import render
from .models import Cart
from django.contrib.auth.models import User

from django.http import JsonResponse
from .models import Cart
from cart.api.serializers import CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def cart(request, username):
    user = User.objects.get(username=username)
    cart = Cart.objects.filter(created_by=user.id)

    context = {
        "cart": cart
    }
    return render(request, "cart/cart.html", context)


def add_to_cart(request):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        roast = data["roast"]
        size = data["size"]
        quantity = data["quantity"]
        price = data["price"]
        image_url = data["image_url"]
        created_by = int(data["created_by"])
        print(created_by)
        user = User.objects.get(id=created_by)

        cart = Cart(name=name, roast=roast, size=size, quantity=quantity,
                    price=price, image_url=image_url, created_by=user)
        cart.save()

    return render(request, "home/index.html")
