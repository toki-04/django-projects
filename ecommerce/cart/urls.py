from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("my-cart/<str:username>/", views.cart, name="my-cart"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
]
