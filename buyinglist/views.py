from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django import forms 
from .models import User
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfull logged in!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

def login_user(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
        
            if user is not None:
                login(user)
                messages.success(request,"You've logged in !")
                return redirect('home')
            else:
                form.add_error(None,"Invalid username or password")
    else:
        messages.success(request,"You must be registered to continue!")
        form = LoginForm()    
    return render(request,'login.html',{'form':form})
