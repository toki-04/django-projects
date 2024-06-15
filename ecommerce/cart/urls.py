from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("<str:username>", views.cart, name="cart"),
]
