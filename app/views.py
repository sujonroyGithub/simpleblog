import email
from multiprocessing import context
from tokenize import group
from turtle import title
from datetime import datetime
from urllib.request import Request
from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate , login ,logout
from.forms import LoginForm, SingUpForm , PostForm
from django.contrib import messages
from.models import Post ,Contact

from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts})
    else:
        return HttpResponseRedirect('/')
   
def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html')
    else:
        return HttpResponseRedirect('/')
   
def contact(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            desc = request.POST.get('desc')
            contact = Contact(name=name,email=email,desc=desc,date=datetime.today())
            contact.save()
            messages.success(request, ' Your Information Has been Sent Sucessfully..')
            
            
        return render(request, 'contact.html')
    else:
        return HttpResponseRedirect('/')
    
def post(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, "post.html",{'posts':posts})
    else:
        return HttpResponseRedirect('/')
    
   
def addpost(request):
  if request.user.is_authenticated:
    if request.method == "POST":
          form = PostForm(request.POST, request.FILES)
          if form.is_valid():
          
             form.save()
             messages.success(request , "Successfully Added !!!")
             form =PostForm()
            
    else:
            form = PostForm()
    
    return render(request, "addpost.html",{'form':form} )
  else:
      return HttpResponseRedirect('/')
def editpost(request ,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = Post.objects.get(id=id)
            form = PostForm(request.POST, instance=id)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully Update !!!")
        else:
            id = Post.objects.get(id=id)
            form = PostForm(instance=id)
        return render(request, "editpost.html",{'form':form})
    else:
        return HttpResponseRedirect('/')      
def delete_post(request , post_id=None):
        if request.user.is_authenticated:
            if request.method == "POST":
                deletepost = Post.objects.get(id=post_id)
                deletepost.delete()
                return HttpResponseRedirect('/post')
        else:
            return HttpResponseRedirect("/")

def user_login(request):
    if not request.user.is_authenticated:
     if request.method == "POST":
      
        form = LoginForm(request= request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user =  authenticate(username=uname, password=upass)
            if user is not None:
                login(request , user)
                messages.success(request , " Logged in Successfully!!")
                return HttpResponseRedirect("/home")
     else:

        form = LoginForm()
     return render(request, 'login.html', {'form':form})
    else:
        return  HttpResponseRedirect('/home')
def user_singup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            messages.success(request, " Congratulations!!! You have Successfully Create a Account.")
            user =form.save()
            group =Group.objects.get(name='Blog Members')
            user.groups.add(group)
            return HttpResponseRedirect("/")
    else:

        form = SingUpForm()
    return render(request, 'singup.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")