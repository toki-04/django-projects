from django.shortcuts import render, redirect
from .models import Post
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime


# Create your views here.


@login_required(login_url="/login/")
def community(request):
    posts = Post.objects.all().order_by("-date_created")
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user.id)

    else:
        profile = ""

    context = {
        "posts": posts,
        "profile": profile,
    }

    return render(request, "community/community.html", context)


def create_post(request):

    if request.method == "POST":
        if request.user.is_authenticated:

            data = request.POST
            profile = Profile.objects.get(user=data["user"])
            visibility = "public"
            text = data["text"]
            if request.FILES["image"]:
                date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                image = request.FILES["image"]
                image.name = date_now+image.name

            else:
                image = ""

            likes = 0
            comments = "0"
            shares = 0

            post = Post(
                profile=profile, visibility=visibility,
                text=text, image=image, likes=likes,
                comments=comments, shares=shares)

            post.save()

            return redirect("community:community")
