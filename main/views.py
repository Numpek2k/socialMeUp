from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import *
from .models import Comments, Friends, Files
from itsdangerous import TimedJSONWebSignatureSerializer as serializer


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
    friends = User.objects.all().filter(Q(friends__idWho=response.user))
    if not friends:
        files = Files.objects.all().order_by("-add_date")
        return render(response, 'main/home.html', {'files': files})
    else:
        filesByFriend = Files.objects.all().filter(postedBy__in=friends).order_by("-add_date")
        return render(response, 'main/home.html', {'files': filesByFriend})


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


def addcomment(response, fileId):
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
                return redirect('/post/' + str(fileId))
            else:
                form.add_error('text', "Post doesn't exist")
    return redirect('home')


def addfriend(response, friendId):
    if not response.user.is_authenticated:
        return redirect('login')
    if User.objects.filter(id=friendId).exists():
        whom = User.objects.get(id=friendId)
        who = response.user
        try:
            Friends.objects.get(idWhom=whom, idWho=who)
        except Friends.DoesNotExist:
            if who == whom:
                return redirect('/profile/' + str(friendId))
            else:
                Friends(idWho=who, idWhom=whom).save()
                Friends(idWho=whom, idWhom=who).save()
                return redirect('/profile/' + str(friendId))
    else:
        return HttpResponse("<H1> User not exist </H1>")
    return redirect('/profile/' + str(friendId))


def forget_password(response):
    if response.method == 'POST':
        form = ForgetPasswordForm(response.POST)
        if form.is_valid():
            email = form.data.get('email')
            user = User.objects.filter(email=email)
            if user.exists():
                secret_key = '8kxsj1rf$gxrmg3!^ky451nl1eyyy+w$w%(8^xv5vth4o8@ho6'
                time_expired = 600
                s = serializer(secret_key, time_expired)
                token = s.dumps({'user_id': user.get().id}).decode('UTF-8')
                send_mail('Change password', 'http://127.0.0.1:8000/change_password/' + token,
                          'palcelizacpl@gmail.com', [email])
            return redirect('login')
    else:
        form = ForgetPasswordForm()

    return render(response, 'main/forget_password.html', {'form': form})


def try_user_id(token):
    secret_key = '8kxsj1rf$gxrmg3!^ky451nl1eyyy+w$w%(8^xv5vth4o8@ho6'
    s = serializer(secret_key)
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None

    return User.objects.get(id=user_id)


def change_password(response, token):
    if response.method == 'POST':
        user = try_user_id(token)
        form = ChangePasswordForm(response.POST, user)
        if user is None:
            form.add_error('password1', 'This token is invalid or expired')
            return render(response, 'main/change_password.html', {'form': form})
        if form.is_valid():
            password = form.data.get('password1')
            user.password = make_password(password)
            user.save()
            return redirect('login')

    else:
        form = ChangePasswordForm()

    return render(response, 'main/change_password.html', {'form': form})
