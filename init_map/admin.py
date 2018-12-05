from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Spot,Polygon

admin.site.register((Polygon,Spot),LeafletGeoAdmin)
# admin.site.register(Polygon,LeafletGeoAdmin)