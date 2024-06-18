from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("community:community")

    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "authentication/login.html", context)


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("authentication:login")
    else:
        form = SignupForm()

    context = {
        "form": form
    }
    return render(request, "authentication/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("home:index")
