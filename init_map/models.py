from djgeojson.fields import PointField, PolygonField
from django.db import models
from django.contrib.auth.models import User
import datetime


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/date/instance/<filename>
    return '{0}/spot_id_{1}/{2}'.format(datetime.datetime.utcnow().date(), instance.id, filename)


class Spot(models.Model):
    geom = PointField()
    description = models.TextField(default="mock description")
    picture = models.ImageField(default="mock image", upload_to=user_directory_path)

    @property
    def popup_content(self):
        return '<img src="{}" /><p>{}</p> <p>{}</p>'.format(
            self.picture.url,
            self.description,
            self.geom.get("coordinates","not provided"),)


class Polygon(models.Model):
    geom = PolygonField(models.Model)
    description = models.TextField(default="mock description")

    @property
    def popup_content(self):
        return '<p>{}</p>'.format(
            self.description)


class Coords(models.Model):
    lat = models.CharField(max_length=12)
    lon = models.CharField(max_length=12)


class UserGeoLocation(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
