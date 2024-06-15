from django.shortcuts import render
from .models import Cart
from django.contrib.auth.models import User
# Create your views here.


def cart(request, username):
    user = User.objects.get(username=username)
    cart = Cart.objects.filter(created_by=user.id)

    context = {
        "cart": cart
    }
    return render(request, "cart/cart.html", context)
