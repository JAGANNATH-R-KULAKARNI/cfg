from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello Jagannath')


def home_page(request):
    return render(request,'my_app/home2.html')