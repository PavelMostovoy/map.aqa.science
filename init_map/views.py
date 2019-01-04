from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib import messages
from datetime import datetime
from .models import Spot, Polygon, Coords, UserGeoLocation
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
        obj.save()
        messages.success(request, "Successfully Added ")
        return HttpResponseRedirect("/")

    return render(request, template, context)


def home(request):
    t = datetime.now()
    return render(request, 'home.html', {'time': t})  # responce


def map_representation(request):
    return render_to_response('Map1.html')  # responce


@login_required(login_url='/admin/')
def location(request):
    context = {}
    template = "add_coords.html"
    return render(request, template, context)  # responce


def main_page(request):
    obj = Spot.objects.all()
    obj2 = Polygon.objects.all()
    context = {'point_s': obj,
               'area_s' : obj2}
    return render(request, 'index.html', context)  # responce


@login_required(login_url='/admin/')
def save_user_geolocation(request):
    if request.method == 'POST':
        coord = Spot()
        print(request.user)
        print(request.POST)
        latitude = float(request.POST['latitude'][:10])
        longitude = float(request.POST['longitude'][:10])
        coord.geom = {"type": "Point", "coordinates": [longitude, latitude]}
        # coord.latitude = latitude
        # coord.longitude = longitude
        # coord.u_name = request.user
        coord.save()

        return HttpResponse("")
