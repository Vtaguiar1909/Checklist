from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,LoginForm, ItemForm
from .models import Item
# Create your views here.

def home(request):
    if request.method =="GET":
        pk = request.user.id
        items = Item.objects.filter(owner=pk)
        if request.user.is_authenticated:
            if items is not None:
                return render(request,'home.html',{'items':items})
        else:
            return render(request,'home.html',{'items':items})
    
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            request.session.set_expiry(300)
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
                login(request,user)
                request.session.set_expiry(300)
                return redirect('home')
            else:
                messages.success(request,"You must be registered to continue!")
                form = LoginForm()
                return redirect('register')
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})    

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You have been logged out ...")
        return redirect('home')
    else:
        messages.success(request,"You're not logged in !")
        return redirect('home')

def add_item(request):
    form = ItemForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                item = form.save(commit=False)
                item.owner = request.user
                item.save() 
                messages.success(request,"Succeded in adding the item !")
                return redirect('home')
        return render(request,'buyinglist.html',{'form':form})
    elif (not request.user.is_authenticated):
        messages.success("You must be logged in to succeed")
        return redirect('login')
    else:
        return redirect('home')
    
def update_item(request,pk):
    if request.user.is_authenticated:
        current_item = Item.objects.get(id=pk)
        form = ItemForm(request.POST or None,instance=current_item)
        print(pk,current_item)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated !")
            return redirect('home')
        return render(request,'update_item.html',{"form":form})
    else:
        messages.success(request,"Must be logged in!")
        return redirect("home")

def delete_item(request,pk):
    if request.user.is_authenticated:
        current_item = Item.objects.get(id=pk)
        current_item.delete()
        messages.success(request,"Deleted !")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in !")
        return redirect('login')
