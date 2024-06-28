from rest_framework.routers import DefaultRouter
from django.urls import path, include
from community.api.urls import post_router

router = DefaultRouter()

# app 1
# app 2
# customers

router.registry.extend(post_router.registry)

urlpatterns = [
    path("", include(router.urls)),
]
