from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services Page")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact Page")
