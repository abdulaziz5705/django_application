from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def login(request):
    return render(request, 'login.html')


def regester(request):
    return render(request, 'regester.html')
