from django.contrib.auth.models import User
from django.db import models
import time
from datetime import date
from multiupload.fields import MultiFileField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class VisitedPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    comment = models.TextField(null=True, blank=True)

    