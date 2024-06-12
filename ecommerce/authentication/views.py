from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home:index")

    else:
        form = LoginForm()

    return render(request, "authentication/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authentication:login")
    else:
        form = SignupForm()

    return render(request, "authentication/signup.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("authentication:login")
