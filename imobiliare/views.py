from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .models import Announce
# from .forms import AnnounceForm
from django.db.models import Q

# Create your views here.


def home(request):
    announces = Announce.objects.all()
    context = {'announces': announces}
    return render(request, 'imobiliare/home.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Utilizator inexistent')
            return render(request, 'imobiliare/login_register.html', {'page': 'login'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nume utilizator sau parola gresita')

    context = {'page': 'login'}
    return render(request, 'imobiliare/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):

    if request.user.is_authenticated:
        return render('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        confirmation_password = request.POST.get('confirmation_password')

        if password != confirmation_password:
            messages.error(request, 'Parolele nu coincid')
            return render(request, 'imobiliare/login_register.html', {'page': 'register'})

        try:
            user = User.objects.create_user(
                username=username, password=password, is_active=False)
        except:
            messages.error(request, 'Utilizatorul nu a putut fi inregistrat')

        if user is not None:
            messages.success(
                request, 'Utilizatorul a fost creat cu succes, asteptati activarea contului!')
            return redirect('login')

    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username
    #         user.save()
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'An error occured during registration')

    return render(request, 'imobiliare/login_register.html', {'page': 'register'})


def announce_details(request, id):
    announce = Announce.objects.get(id=id)
    context = {'announce': announce}
    return render(request, 'imobiliare/announce_details.html', context)


def my_announces(request):
    announces = Announce.objects.filter(creator=request.user)
    context = {'announces': announces, 'announces_no': len(announces)}
    return render(request, 'imobiliare/my_announces.html', context)

# decorator
@login_required(login_url='login')
def createAnnounce(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        floor = request.POST.get('floor')
        county = request.POST.get('county')
        location = request.POST.get('location')
        image = request.POST.get('image')
        phone = request.POST.get('phone_number')

        try:
            announce = Announce.objects.create(creator=request.user, title=title, description=description,
                                               price=price, floor=floor, county=county, location=location, image=image, phone_number=phone)
        except:
            messages.error(request, 'A aparut o erroare la crearea anuntului!')
            return render(request, 'imobiliare/create_announce.html')

        return redirect('/announce_details/' + str(announce.id))

    # form = AnnounceForm()

    # if request.method == 'POST':
    #     form = AnnounceForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    return render(request, 'imobiliare/create_announce.html')


@login_required(login_url='login')
def updateAnnounce(request, id):
    announce = Announce.objects.get(id=id)
    # form = AnnounceForm(instance=announce)

    if request.user != announce.creator and not request.user.is_superuser:
        return HttpResponse('Nu poti modifica acest anunt!')

    if request.method == 'POST':
        announce.title = request.POST.get('title')
        announce.description = request.POST.get('description')
        announce.price = request.POST.get('price')
        announce.floor = request.POST.get('floor')
        announce.county = request.POST.get('county')
        announce.location = request.POST.get('location')
        announce.image = request.POST.get('image')
        announce.phone_number = request.POST.get('phone_number')

        try:
            announce.save()
        except:
            messages.error(
                request, 'A aparut o erroare la salvarea anuntului!')
            return render(request, 'imobiliare/edit_announce.html')

        return redirect('/announce_details/' + str(announce.id))

    # if request.method == 'POST':
        # form = AnnounceForm(request.POST, instance=announce)
        # if form.is_valid():
        #     form.save()
        #     return redirect('home')

    context = {'announce': announce}
    return render(request, 'imobiliare/edit_announce.html', context)


@login_required(login_url='login')
def deleteAnnounce(request, id):
    announce = Announce.objects.get(id=id)

    if request.user != announce.creator and not request.user.is_superuser:
        return HttpResponse('Nu poti sterge acest anunt!')

    if request.method == 'POST':
        announce.delete()
        return redirect('home')

    return render(request, 'imobiliare/delete.html', {'obj': announce})


def searchAnnounce(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        search_location = request.POST.get('search_location')

        announces = Announce.objects.filter((Q(title__contains=search_text) | Q(description__contains=search_text)) &
                                            (Q(county__contains=search_location) | Q(location__contains=search_location)))

        return render(request, 'imobiliare/home.html', {'announces': announces})
