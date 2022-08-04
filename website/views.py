from urllib import request
from django.shortcuts import render


def home(request):
    return render(request,'website/index.html')


def mockup(request):
    return render(request,'website/gaint-plus.html')
