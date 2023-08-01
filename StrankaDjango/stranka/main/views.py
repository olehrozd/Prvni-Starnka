from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def bmw(request):
    bexa = Car.objects.all()
    return render(request, 'main/bmw.html', {'bexa': bexa})

def tesla(request):
    return render(request, 'main/tesla.html')

def mercedes(request):
    return render(request, 'main/mercedes.html')



