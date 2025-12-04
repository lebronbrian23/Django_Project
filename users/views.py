from django.http import HttpResponseRedirect

from django.urls import reverse

from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, 'users/index.html',{
        "message": "Welcome back,"
    })

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html',{
        "message": "Logged out,"
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, 'users/login.html', {"message": "Invalid username and/or password."})

    return render(request, 'users/login.html')