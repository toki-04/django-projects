from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    path("", views.community, name="community"),
    path("create-post/", views.create_post, name="create_post"),
]
