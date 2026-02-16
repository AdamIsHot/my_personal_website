from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.urls import path

from django.shortcuts import render
from muj_web.models import Clanek

def domovska_stranka(request):
    return render(request, 'index.html')

def muj_art(request):
    return render(request, 'art.html')

def moje_clanky(request):
    vsechny_clanky = Clanek.objects.all()
    return render(request, 'clanky.html')

