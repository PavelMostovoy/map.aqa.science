from djgeojson.fields import PointField
from django.db import models
import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/date/instance/<filename>
    return '{0}/spot_id_{1}/{2}'.format(datetime.datetime.utcnow().date(),instance.id, filename)

class Spot(models.Model):

    geom = PointField()
    description = models.TextField(default="mock description")
    picture = models.ImageField(default="mock image",upload_to=user_directory_path)

    @property
    def popup_content(self):
        return '<img src="{}" /><p>{}</p>'.format(
            self.picture.url,
            self.description)
