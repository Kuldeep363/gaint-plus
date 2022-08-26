from urllib import request
from django.shortcuts import render


def home(request):
    return render(request,'website/index.html')

def services(request):
    return render(request,'website/products.html')

def mockup(request):
    return render(request,'website/gaint-plus.html')
