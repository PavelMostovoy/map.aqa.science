from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Spot, Polygon, Coords

admin.site.register((Polygon, Spot, Coords), LeafletGeoAdmin)
# admin.site.register(Polygon,LeafletGeoAdmin)