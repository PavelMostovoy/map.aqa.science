from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Spot

admin.site.register(Spot, LeafletGeoAdmin)