from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="/login/")
def community(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, "community/community.html", context)
