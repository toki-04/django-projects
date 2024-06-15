from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product.api.urls import product_router
from cart.api.urls import cart_router

router = DefaultRouter()

router.registry.extend(product_router.registry)
router.registry.extend(cart_router.registry)

urlpatterns = [
    path("", include(router.urls)),
]
