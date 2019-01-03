from django import forms
from leaflet.forms.widgets import LeafletWidget  # provide mode than currently needed
# from leaflet.forms.fields import PointField  # could be used for only one geometry

from .models import Spot, Polygon


class PostModelForm(forms.ModelForm):
    # geom = PointField()

    class Meta:
        geom = LeafletWidget(attrs={'settings_overrides': {
                'DEFAULT_CENTER': (46.469526, 30.741174),}})
        model = Spot
        fields = (
            'geom',
        )
        #
        widgets = {'geom': geom}
