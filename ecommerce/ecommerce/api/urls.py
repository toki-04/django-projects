from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product.api.urls import product_router

router = DefaultRouter()

router.registry.extend(product_router.registry)

urlpatterns = [
    path("", include(router.urls)),
]
