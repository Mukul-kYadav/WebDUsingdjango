from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def index(request):
    return HttpResponse("Hello-World")

def muku(request):
    return HttpResponse("hello-muku")

def jane(request):
    return HttpResponse("hello-jane")

def greet(request, name):
    return render(request, "lesrnapp/greet.html")

def greet(request, name):
    return render(request, "learnapp/greet.html", {
        "name": name.capitalize()
    })

def index(request):
    return render(request, "learnapp/index.html")