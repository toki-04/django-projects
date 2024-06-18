from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def community(request):
    return render(request, "community/community.html")
