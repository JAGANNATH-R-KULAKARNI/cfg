from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail

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
            messages.info(request,"Invalid Credentials")    
            return redirect('/login')
    
    return render(request,'my_app/login.html')

def signup_page(request):
    
    if(request.method == 'POST'):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        if(User.objects.filter(username=username)):
            messages.info(request,username+' already exists !')
            return redirect('/signup')
        
        if(not username.isalnum()):
            messages.info(request,'Username must be Alpha-Numberic !')
            return redirect('/signup')
        
        if(User.objects.filter(email=email)):
            messages.info(request,email+' already exists !')
            return redirect('/signup')    
        
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

def forgot_password(request):
    
    if(request.method == 'POST'):
        email=request.POST['email']
        
        if(not User.objects.filter(email=email).first()):
            messages.info(request,'User with email '+email+' not found')
            return redirect('/forgot')
        else:
            send_mail('New Email', 'Hello Jagannath, email from django app', 'jagannathrkulakarni.171845@gmail.com', ['4ni19is038_b@nie.ac.in'], fail_silently=False)
            messages.success(request,'Link has been sent to '+email)
            return redirect('/forgot')
        
    return render(request,'my_app/forgotpasswd.html')



def change_password(request):
    return render(request,'my_app/changepasswd.html')
    