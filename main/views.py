from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from .models import Comments, Friends, Files


# Create your views here.


def login(response):
    return redirect('login')


def register(response):
    if response.method == "POST":
        form = CustomUserCreatingForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreatingForm()
    return render(response, 'main/register.html', {'form': form})


def profile(response):
    return render(response, "main/profile.html" )


def home(response):
    return render(response, "main/home.html")


def friends(response):
    return render(response, "main/friends.html")


def image(response):
    return render(response, "main/image.html")


