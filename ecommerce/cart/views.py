from django.shortcuts import render

# Create your views here.


def cart(request, id):
    return render(request, "cart/cart.html")
