from dataclasses import fields
from datetime import datetime
from distutils.command.upload import upload
from django import forms
from .models import *
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class SingUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}) )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
   password = forms.CharField(label=_('Password'),strip=False,  widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class PostForm(forms.ModelForm):
    date = forms.DateField(label=_('Date'),  widget=forms.DateInput(attrs={'type':'date' ,'class':'my-3'}))
    class Meta:
        model = Post
        fields = ['title', 'desc', 'image' ,'date']
        labels = {'title':'Title', 'desc':'Description', 'image':'Add Image','date ': 'Date'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control my-3'}),
        'desc':forms.Textarea(attrs={'class':'form-control my-3 '})}