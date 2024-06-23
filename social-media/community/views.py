from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime


# Create your views here.


@login_required(login_url="/login/")
def community(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "community/community.html", context)


def create_post(request):

    if request.method == "POST":
        data = request.POST
        user = User.objects.get(id=data["user"])
        visibility = "public"
        text = data["text"]
        if request.FILES["image"]:
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            image = request.FILES["image"]
            image.name = date_now+image.name

            print("*"*20)
            print(image)
            print("*"*20)
        else:
            image = ""

        likes = 0
        comments = "0"
        shares = 0

        post = Post(
            user=user, visibility=visibility,
            text=text, image=image, likes=likes,
            comments=comments, shares=shares)

        post.save()

        return redirect("community:community")
