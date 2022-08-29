from urllib import request
from django.shortcuts import render


def home(request):
    return render(request,'website/index.html')

def services(request):
    return render(request,'website/products.html')

# def terms(request):
#     return render(request,'website/terms.html')


# def returnPolicy(request):
#     return render(request,'website/returnPolicy.html')


def error_404(request,exception):
    return render(request,'website/notFound.html')