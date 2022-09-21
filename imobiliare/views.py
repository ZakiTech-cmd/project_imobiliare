from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'imobiliare/home.html')


def room(request):
    return render(request, 'imobiliare/login.html')