from django import forms
from leaflet.forms.widgets import LeafletWidget # provide mode than currently needed
# from leaflet.forms.fields import PointField # could be used for only one geometry

from .models import Spot,Polygon


class PostModelForm(forms.ModelForm):
    # geom = PointField()

    class Meta:
        model = Spot
        fields = [
            'geom',
            'description',
            'picture'
           ]
        widgets = {'geom': LeafletWidget()}