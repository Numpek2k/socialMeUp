from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("profile/<int:postedById>", views.profile, name="profile"),
    path("addfriend/<int:friendId>", views.addfriend, name="friends"),
    path("post/<int:postById>", views.post, name="post"),
    path("addpost/", views.addpost, name="addpost"),
    path("addcomment/<int:fileId>", views.addcomment, name="addcomment"),
    path("forget_password/", views.forget_password, name="forget_password"),
    path("change_password/<str:token>", views.change_password, name="change_password"),
]