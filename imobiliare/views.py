from django.shortcuts import render
from .models import Announce

# Create your views here.


def home(request):
    announces = Announce.objects.all()
    context = {'announces': announces}
    return render(request, 'imobiliare/home.html', context)


def login_register(request):
    return render(request, 'imobiliare/login_register.html')


def announce_details(request, id):
    announce = Announce.objects.get(id=id)
    context = {'announce': announce}
    return render(request, 'imobiliare/announce_details.html', context)