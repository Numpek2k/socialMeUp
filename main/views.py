from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(response):
    return render(response, "main/login.html")


def register(response):
    return render(response, "main/register.html")


def profile(response):
    return render(response, "main/profile.html")


def home(response):
    return render(response, "main/home.html")


def friends(response):
    return render(response, "main/friends.html")


def image(response):
    return render(response, "main/image.html")


