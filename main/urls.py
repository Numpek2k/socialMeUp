from django.urls import path
from . import  views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("friends/", views.friends, name="friends"),
    path("image/", views.image, name="image"),
]