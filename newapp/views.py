from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})


def viewdata(request):
    return render(request, 'viewdata.html', {'navbar': 'viewdata'})