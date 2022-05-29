from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return HttpResponse('Hello Jagannath')


def home_page(request):
    return render(request,'my_app/home2.html')


def login_page(request):
    
    if(request.method == 'POST'):
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            msg='Hello '+username+', You are successfully logged in'
            messages.success(request,msg)
            return redirect('/')
        else:
            messages.info(request,"Credentials Invalid")    
            return redirect('/login')
    
    return render(request,'my_app/login.html')

def signup_page(request):
    
    if(request.method == 'POST'):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Your Account has been successfully created")
        
        return redirect('/login')
    
    if request.user.is_authenticated:
        return redirect('/') 
       
    return render(request,'my_app/signup.html')


def log_out(request):
    logout(request)
    messages.success(request,"Succesfully logged out")
    
    return redirect('/login')
    