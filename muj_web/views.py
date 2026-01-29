from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.urls import path

from django.shortcuts import render

def domovska_stranka(request):
    return render(request, 'index.html')

def muj_art(request):
    return render(request, 'art.html')
