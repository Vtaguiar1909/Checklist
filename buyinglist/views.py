from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from django import forms 
from .models import User
# Create your views here.

def home(request):
    users = User.objects.all()
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        
        else:
            messages.success(request,"There was an error Loggin in, Please try again !")
            return redirect('home')
    else:
        return render(request,'home.html',{'users':users})