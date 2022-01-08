from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import *
from .models import Comments, Friends, Files


# Create your views here.


def login(response):
    if response.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


def register(response):
    if response.user.is_authenticated:
        return redirect('home')
    if response.method == "POST":
        form = CustomUserCreatingForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreatingForm()
    return render(response, 'main/register.html', {'form': form})


def profile(response, postedById):
    if not response.user.is_authenticated:
        return redirect('login')
    if not User.objects.filter(id=postedById).exists():
        return HttpResponse("<H1> User not found! </H1>")
    files = Files.objects.filter(postedBy_id=postedById).order_by("-add_date")
    userByID = User.objects.get(id=postedById)
    return render(response, 'main/profile.html', {'files': files, 'userByID': userByID})


def home(response):
    if not response.user.is_authenticated:
        return redirect('login')
    files = Files.objects.all().order_by("-add_date")
    return render(response, 'main/home.html', {'files': files})


def post(response, postById):
    if not response.user.is_authenticated:
        return redirect('login')
    if not Files.objects.filter(id=postById).exists():
        return HttpResponse("<H1> File not found! </H1>")
    fileById = Files.objects.get(id=postById)
    form = AddCommentForm()
    return render(response, 'main/post.html', {'file': fileById, 'form': form})


def addpost(response):
    if not response.user.is_authenticated:
        return redirect('login')
    if response.method == 'POST':
        form = addFilesForm(response.POST, response.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.postedBy = response.user
            post.add_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = addFilesForm()
    return render(response, 'main/addPost.html', {'form': form})


def addcomment(response,fileId):
    if not response.user.is_authenticated:
        return redirect('login')
    if response.method == 'POST':
        form = AddCommentForm(response.POST)
        if form.is_valid():
            file = Files.objects.filter(pk=fileId)
            if file.exists():
                comment = form.save(commit=False)
                comment.postedBy = response.user
                comment.file = file.get(pk=fileId)
                comment.save()
                return redirect('/post/'+str(fileId))
            else:
                form.add_error('text', "Post doesn't exist")
    return redirect('home')


def addfriend(response,friendId):
    if not response.user.is_authenticated:
        return redirect('login')
    if User.objects.filter(id=friendId).exists():
        whom = User.objects.get(id=friendId)
        who = response.user
        try:
            Friends.objects.get(idWhom=whom, idWho=who)
        except Friends.DoesNotExist:
            if who == whom:
                return redirect('/profile/'+str(friendId))
            else:
                Friends(idWho=who, idWhom=whom).save()
                Friends(idWho=whom, idWhom=who).save()
                return redirect('/profile/'+str(friendId))
    else:
        return HttpResponse("<H1> User not exist </H1>")
    return redirect('/profile/'+str(friendId))