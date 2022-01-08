from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput, FileInput
from .models import Files, Comments, Friends
from django.contrib.auth.models import User


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CustomUserCreatingForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 max_length=32, help_text='First name')
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                max_length=32, help_text='Last name')
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,
                             help_text='Enter a valid email address')
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class addFilesForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    image = forms.ImageField(widget=FileInput(attrs={'class': 'form-control', 'id': 'formFile'}))

    class Meta:
        model = Files
        fields = ['title', 'image', 'description']


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comments
        fields = ['content']


class AddFriendsForm(forms.Form):
    class Meta:
        model = Friends
