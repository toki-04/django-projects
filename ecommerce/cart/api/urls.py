from rest_framework.routers import DefaultRouter
from .views import CartViewSet

cart_router = DefaultRouter()
cart_router.register(r"cart", CartViewSet)
