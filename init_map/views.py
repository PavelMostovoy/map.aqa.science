from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib import messages
from datetime import datetime
from .models import Spot, Polygon
from .forms import PostModelForm, PostCoordForm


# Create your views here.


@login_required(login_url='/admin/')
def add_item(request):
    form = PostModelForm(request.POST or None)
    template = 'add_item.html'
    context = {
        "form": form,
    }

    if form.is_valid():
        obj = form.save(commit=False)
        print(form)
        obj.save()
        messages.success(request, "Successfully Added ")
        return HttpResponseRedirect("/")

    return render(request, template, context)


@login_required(login_url='/admin/')
def add_coords(request):
    form = PostCoordForm(request.POST)
    template = 'add_coords.html'
    coords = []
    context = {
        "coords": coords,
        "form": form,
    }
    import time
    time.sleep(5)
    print(context["coords"])
    return render(request, template, context)


def home(request):
    t = datetime.now()
    return render(request, 'home.html', {'time': t})  # responce


def map_representation(request):
    return render_to_response('Map1.html')  # responce


def location(request):
    return render_to_response('location.html')  # responce


def main_page(request):
    obj = Spot.objects.all()
    obj2 = Polygon.objects.all()
    context = {'point_s': obj,
               'area_s' : obj2}
    return render(request, 'index.html', context)  # responce
