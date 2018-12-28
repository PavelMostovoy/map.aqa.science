from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib import messages
from datetime import datetime
from .models import Spot, Polygon
from .forms import PostModelForm


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


def location(request):
    return render_to_response('location.html')  # responce


def main_page(request):
    obj = Spot.objects.all()
    context = {'point_s': obj}
    return render(request, 'index.html', context)  # responce
