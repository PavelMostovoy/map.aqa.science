from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from datetime import datetime

# Create your views here.


def home(request):
    t = datetime.now()
    return render (request,'home.html',{'time':t}) #responce


def map_representation(request):
    return render_to_response('Map1.html')  # responce


def location(request):
    return render_to_response('location.html')  # responce


def temp(request):
    return render_to_response('index.html')  # responce