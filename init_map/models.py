from djgeojson.fields import PointField
from django.db import models


class Spot(models.Model):

    geom = PointField()