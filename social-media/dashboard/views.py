from django.shortcuts import render
from user_profile.models import Profile

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user.id)

    else:
        profile = ""

    context = {
        "profile": profile
    }
    return render(request, "dashboard/dashboard.html", context)

# TODO: do this after you finish the community todo


def change_profile(request):
    pass


def change_about_me(request):
    pass
