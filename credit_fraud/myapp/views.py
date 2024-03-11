from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello world')
    
def room(request):
    return HttpResponse('I am Saifee')
def myself(request):
    return HttpResponse('Welcome to the app')

def epl(request):
    return HttpResponse('I love football')