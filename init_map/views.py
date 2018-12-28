from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from datetime import datetime
from .models import Spot


# Create your views here.


def home(request):
    t = datetime.now()
    return render(request, 'home.html', {'time': t})  # responce


def map_representation(request):
    return render_to_response('Map1.html')  # responce


def location(request):
    return render_to_response('location.html')  # responce


@login_required(login_url='/admin/')
def main_page(request):
    obj = Spot.objects.all()
    context = {'point_s': obj}
    return render(request, 'index.html', context)  # responce
