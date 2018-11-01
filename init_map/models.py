from djgeojson.fields import PointField
from django.db import models


class Spot(models.Model):

    geom = PointField()
    description = models.TextField(default="mock description")
    picture = models.ImageField(default="mock image", upload_to='/media/')

    @property
    def popup_content(self):
        return '<img src="{}" /><p>{}</p>'.format(
            self.picture.url,
            self.description)